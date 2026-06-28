---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-18_terrapin-attack.md
original_filename: 2023-12-18_terrapin-attack.md
title: Terrapin Attack
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
- cloud-security
- supply-chain
language: en
raw_sha256: cbac490303d4fae1707574ec990b86cabcf72bdfc57d740cd09bbdd6da278e24
text_sha256: 6410d6c80bce3e9c79db9535517755b447743ecd1bd655533034ce2c3c806b3b
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Terrapin Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-18_terrapin-attack.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `cbac490303d4fae1707574ec990b86cabcf72bdfc57d740cd09bbdd6da278e24`
- Text SHA256: `6410d6c80bce3e9c79db9535517755b447743ecd1bd655533034ce2c3c806b3b`


## Content

---
title: "Terrapin Attack"
url: "https://terrapin-attack.com"
final_url: "https://terrapin-attack.com/"
authors: ["Fabian Bäumer (@TrueSkrillor)", "Marcus Brinkmann (@lambdafu)", "Jörg Schwenk (@JoergSchwenk)"]
programs: ["OpenSSH", "AsyncSSH"]
bugs: ["Downgrade attack", "MiTM", "Prefix truncation attack", "Cryptographic issues"]
publication_date: "2023-12-18"
added_date: "2024-01-08"
source: "pentester.land/writeups.json"
original_index: 611
---

# Terrapin Attack

  * Paper
  * Vulnerability Scanner
  * Q&A
  * [Patches](patches.html)

## News

  * The accepted paper including the artifact appendix is now available.
  * The Terrapin Attack will be presented at [Real World Crypto Symposium 2024](https://rwc.iacr.org/2024/program.php), [Black Hat USA 2024](https://www.blackhat.com/us-24/briefings/schedule/index.html#terrapin-attack-breaking-ssh-channel-integrity-by-sequence-number-manipulation-40179), and [USENIX Security Symposium 2024](https://www.usenix.org/conference/usenixsecurity24).
  * We compiled a comprehensive [list of SSH implementations](patches.html) adopting the "strict kex" countermeasure by OpenSSH.
  * Recommended Articles: [Ars Technica](https://arstechnica.com/security/2023/12/hackers-can-break-ssh-channel-integrity-using-novel-data-corruption-attack) (Dan Goodin), [The Register](https://www.theregister.com/2023/12/20/terrapin_attack_ssh) (Connor Jones)

* * *

## Introduction

SSH is an internet standard that provides secure access to network services, particularly remote terminal login and file transfer within organizational networks and to over 15 million servers on the open internet.

_Terrapin_ is a prefix truncation attack targeting the SSH protocol. More precisely, Terrapin breaks the integrity of SSH's secure channel. By carefully adjusting the sequence numbers during the handshake, an attacker can remove an arbitrary amount of messages sent by the client or server at the beginning of the secure channel without the client or server noticing it.

The attack can be performed in practice, allowing an attacker to downgrade the connection's security by truncating the extension negotiation message (RFC8308) from the transcript. The truncation can lead to using less secure client authentication algorithms and deactivating specific countermeasures against keystroke timing attacks in OpenSSH 9.5.

We also showed that Terrapin can be used to enable the exploitation of implementation flaws. For example, we found several weaknesses in the AsyncSSH servers' state machine, allowing an attacker to sign a victim's client into another account without the victim noticing. Hence, it will enable strong phishing attacks and may grant the attacker Man-in-the-Middle (MitM) capabilities within the encrypted session.

To perform the Terrapin attack in practice, we require MitM capabilities at the network layer (the attacker must be able to intercept and modify the connection's traffic). Additionally, the connection must be secured by either ChaCha20-Poly1305 or CBC with Encrypt-then-MAC. However, our scan indicates an extensive adoption of these encryption modes; therefore, Terrapin applies to most real-world SSH sessions.

* * *

## Attack Overview

![](media/img/terrapin-attack.png)

The image shows a practical application of the Terrapin attack. The attacker can drop the EXT_INFO message, used for negotiating several protocol extensions, without the client or server noticing it. Usually, packet deletion would be detected by the client when receiving the next binary packet sent by the server, as sequence numbers would mismatch. To avoid this, an attacker injects an ignored packet during the handshake to offset the sequence numbers accordingly. 

* * *

## Full Technical Paper

[Terrapin Attack: Breaking SSH Channel Integrity By Sequence Number Manipulation](TerrapinAttack.pdf), Fabian Bäumer, Marcus Brinkmann, Jörg Schwenk. 

Also available on the [USENIX Security '24 website](https://www.usenix.org/conference/usenixsecurity24/presentation/b%C3%A4umer) and [arXiv](https://arxiv.org/abs/2312.12422). The artifacts are available on [GitHub](https://github.com/RUB-NDS/Terrapin-Artifacts/).

* * *

## Vulnerability Scanner

We provide a simple console application, written in Go, which can be used to determine whether an SSH server or client is vulnerable to the Terrapin attack. The scanner connects to your SSH server (or listens for an incoming client connection) to detect whether vulnerable encryption modes are offered and if the strict key exchange countermeasure is supported. It does not perform a fully-fledged handshake, nor does it actually perform the attack.

Pre-built binaries for all major platforms and the source code are available on [GitHub](https://github.com/RUB-NDS/Terrapin-Scanner/releases/latest).

* * *

## FAQ

### I am an admin, should I drop everything and fix this?

Probably not.

The attack requires an active Man-in-the-Middle attacker that can intercept and modify the connection's traffic at the TCP/IP layer. Additionally, we require the negotiation of either ChaCha20-Poly1305, or any CBC cipher in combination with Encrypt-then-MAC as the connection's encryption mode. 

If you feel uncomfortable waiting for your SSH implementation to provide a patch, you can workaround this vulnerability by temporarily disabling the affected chacha20-poly1305@openssh.com encryption and -etm@openssh.com MAC algorithms in the configuration of your SSH server (or client), and use unaffected algorithms like AES-GCM instead. 

Fair word of warning: If configured improperly or your client does not support these algorithms, you may lose access to your server. Also, some (very) old versions of OpenSSH (6.2 and 6.3) are vulnerable to a [buffer overflow when using AES-GCM](https://www.openssh.com/txt/gcmrekey.adv).

### What can the attackers gain?

Within the paper we describe an extension downgrade attack, allowing an attacker to downgrade the security of an SSH connection when using SSH extension negotiation. The impact in practice heavily depends on the supported extensions. Most commonly, this will impact the security of client authentication when using an RSA public key. When using OpenSSH 9.5, it may also be used to deactivate certain countermeasures to keystroke timing attacks.

We also showed that the Terrapin attack can be used to enable certain attacks that exploit additional implementation flaws. For example, we used flaws in the internal state machine of AsyncSSH in combination with our attack to obtain a MitM position at the session layer. 

However, the potential consequences of the general Terrapin attack are dependent on the messages exchanged after the handshake concludes. If you are using a custom SSH service and do not resort to the authentication protocol, you should check that dropping the first few messages of a connection does not yield security risks. 

### Who is vulnerable?

Almost everyone. The Terrapin attack exploits weaknesses in the SSH transport layer protocol in combination with newer cryptographic algorithms and encryption modes introduced by OpenSSH over 10 years ago. Since then, these have been adopted by a wide range of SSH implementations, therefore affecting a majority of current implementations.

In practice, our attack can be applied against any connection using either ChaCha20-Poly1305 or any CBC-mode cipher in combination with the Encrypt-then-MAC paradigm. Theoretically, CTR-mode ciphers in combination with the Encrypt-then-MAC paradigm are vulnerable as well, although this weakness cannot be exploited in a real-world scenario.

### So how practical is the attack?

The Terrapin attack requires an active Man-in-the-Middle attacker, that means some way for an attacker to intercept and modify the data sent from the client or server to the remote peer. This is difficult on the Internet, but can be a plausible attacker model on the local network.

Besides that, we also require the use of a vulnerable encryption mode. Encrypt-then-MAC and ChaCha20-Poly1305 have been introduced by OpenSSH over 10 years ago. Both have become the default for many years and as such spread across the SSH ecosystem. Our scan indicated that at least 77% of SSH servers on the internet supported at least one mode that can be exploited in practice.

### Is my SSH client/server vulnerable?

Most likely, yes.

In more technical terms, if your SSH implementations supports (and is configured to offer) the `chacha20-poly1305@openssh.com` encryption algorithm, or any encryption algorithm suffixed `-cbc` in combination with any MAC algorithm suffixed `-etm@openssh.com`, you are vulnerable to Terrapin. 

You can use our vulnerability scanner to determine whether your client or server is vulnerable.

### I patched my SSH client/server, am I safe now?

It depends. The strict key exchange countermeasure implemented by OpenSSH and other vendors requires both, client and server, to support it, in order to take effect. Connecting a vulnerable client to a patched server, and vice versa, still results in a vulnerable connection.

### Does this vulnerability have a CVE number?

Yes. We got assigned a total of three CVE numbers. These are: 

  * CVE-2023-48795: General Protocol Flaw
  * CVE-2023-46445: Rogue Extension Negotiation Attack in AsyncSSH
  * CVE-2023-46446: Rogue Session Attack in AsyncSSH
  * CVE-2024-41909: General Protocol Flaw (Apache MINA SSHD)

### Is this a new attack?

The Terrapin attack can be considered the first attack in a new family of attacks targeting cryptographic network protocols and is the first ever practically exploitable prefix truncation attack that we know of. The only other mentioning of a prefix truncation attack was by Cédric Fournet on behalf of the miTLS team on an [IETF mailing list](https://mailarchive.ietf.org/arch/msg/tls/extoO9ETJLnEm3MRDTO23x70DFM/). Fournet described potential weaknesses in a draft version of TLS 1.3 that used to not reset sequence numbers when activating new keys, although his considerations remained theoretical as "[...] prefix truncations will probably cause the handshake to fail". The draft was subsequently changed and no prefix truncation attacks in TLS 1.3 are known to this date. 

### Why is the attack called "Terrapin"?

The name "Terrapin" started as an acronym, but considering how tortured it looked, we opted to drop the acronym part and only retained the name. We chose this name because SSH and terrapins have one thing in common: Shells. And I think we can all agree that terrapins (and turtles in general) are cute animals.

### How have vendors responded to this vulnerability?

Many vendors have updated their SSH implementation to support an optional strict key exchange. Strict key exchange is a backwards-incompatible change to the SSH handshake which introduces sequence number resets and takes away an attacker's capability to inject packets during the initial, unencrypted handshake. However, to take effect, both client and server must support this feature.

### What about other protocols?

To this date, we are not aware of any practical prefix truncation in other cryptographic network protocols. All versions of TLS reset the message sequence number to zero when changing key, therefore decoupling unencrypted and encrypted sequence numbers. Additionally, TLS authenticates the entire handshake thus preventing an attacker from inserting any message. While IPSec/IKE only authenticates parts of its handshake, the sequence numbers are reset similar to TLS, rendering it immune to our attack.

### What about other cipher modes?

AES-GCM (RFC5647) is not affected by Terrapin as it does not use the SSH sequence numbers. Instead, AES-GCM uses the IV obtained from key derivation as its nonce, incrementing it after sending a binary packet. In a healthy connection, this results in the nonce being at a fixed offset from the sequence number. 

The original Encrypt-and-MAC paradigma from RFC4253 protects the integrity of the plaintext, thus thwarting our attack, which yields one pseudorandom block during decryption. 

### Is this vulnerability severe enough to deserve a name, a logo and a web page?

Terrapin is not a simple software bug that can be fixed with an update to a single library or component. Instead, clients and servers need to be updated to protect the connection against prefix truncation attacks. This means we need to raise awareness of the issue across all SSH client and server implementations, which is a considerable effort. We expect that the general Terrapin attack will stay with us for many years, so we have a cute animal to keep us company while we help clients and servers to adopt the suggested countermeasures!

### How can I contact you?

You can reach us via mail, Twitter, or Mastodon:

  * Fabian Bäumer, Ruhr University Bochum, [@TrueSkrillor](https://x.com/TrueSkrillor), [@Skrillor@infosec.exchange](https://infosec.exchange/@Skrillor), fabian.baeumer@rub.de
  * Marcus Brinkmann, Ruhr University Bochum, [@lambdafu](https://x.com/lambdafu), [@lambdafu@mastodon.social](https://mastodon.social/@lambdafu), marcus.brinkmann@rub.de
  * Jörg Schwenk, Ruhr University Bochum, [@JoergSchwenk](https://x.com/JoergSchwenk), joerg.schwenk@rub.de

### Responsible Disclosure Timeline

  * 2023-10-17: Initial contact with OpenSSH and Ron Frederick (author of AsyncSSH)
  * 2023-11-08: AsyncSSH published a patched version fixing the implementation bugs
  * 2023-11-17: Initial contact with 17 other SSH implementation vendors (round 1)
  * 2023-11-17: Disclosed findings to the German CERT-Bund. Findings were later forwarded to partnered CERTs by CERT-Bund.
  * 2023-11-21: Initial contact with 12 other SSH implementations after initial feedback from round 1 (round 2)
  * 2023-12-11: Disclosed findings to the distros mailing list
  * 2023-12-18: Public Disclosure

[ ![Ruhr University Bochum Logo](media/img/Logo_RUB.png) ](https://ruhr-uni-bochum.de) [ ![HGI Logo](media/img/Logo_HGI.jpg) ](https://hgi.rub.de) [ ![CASA Logo](media/img/Logo_CASA.png) ](https://casa.rub.de)

Last updated 2024-09-02. The Terrapin website is free to use under a [CC0](//creativecommons.org/publicdomain/zero/1.0/) license. Web design by [Sarah Madden](http://sarahmadden.com/) and Christian Dresen. Adapted for Terrapin by Fabian Bäumer. The Terrapin logo was designed by [tnhs_project](https://www.fiverr.com/tnhs_project). | [Imprint](imprint.html)
