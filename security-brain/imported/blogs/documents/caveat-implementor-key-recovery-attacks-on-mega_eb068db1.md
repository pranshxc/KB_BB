---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-06_caveat-implementor-key-recovery-attacks-on-mega.md
original_filename: 2023-03-06_caveat-implementor-key-recovery-attacks-on-mega.md
title: Caveat Implementor! Key Recovery Attacks on MEGA
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- supply-chain
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- supply-chain
language: en
raw_sha256: eb068db1476369676f750ba35a57db4f7b0849d180c7004e14b9898763ba82d0
text_sha256: c8e48e15c0bc60a667d6cdeb08870110ec96429691b5098af34a1069340a3e22
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Caveat Implementor! Key Recovery Attacks on MEGA

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-06_caveat-implementor-key-recovery-attacks-on-mega.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `eb068db1476369676f750ba35a57db4f7b0849d180c7004e14b9898763ba82d0`
- Text SHA256: `c8e48e15c0bc60a667d6cdeb08870110ec96429691b5098af34a1069340a3e22`


## Content

---
title: "Caveat Implementor! Key Recovery Attacks on MEGA"
url: "https://mega-caveat.github.io"
final_url: "https://mega-caveat.github.io/"
authors: ["Martin R. Albrecht (@martinralbrecht)", "Miro Haller (@M__Haller)", "Lenka Mareková", "Kenneth G. Paterson (@Yogehi)"]
programs: ["MEGA"]
bugs: ["Cryptographic issues"]
publication_date: "2023-03-06"
added_date: "2023-03-10"
source: "pentester.land/writeups.json"
original_index: 1416
---

Toggle navigation MEGA

  * Background
  * Attacks
  * Disclosure
  * Paper
  * Q & A
  * Research Team

# _Caveat Implementor!_  
Key Recovery Attacks on MEGA

* * *

MEGA is a large-scale cloud storage and communication platform that aims to provide end-to-end encryption for stored data. Recent work by [Backendal, Haller and Paterson](https://mega-awry.io) invalidated these security claims by showing practical attacks against MEGA that could be mounted by the MEGA service provider. In response, the MEGA developers added lightweight sanity checks on the user RSA private keys used in MEGA, sufficient to prevent the previous attacks. We analysed these new sanity checks and show how they themselves could be exploited to mount novel attacks on MEGA that recover a target user's RSA private key with only slightly higher attack complexity than the original attacks. 

Skip to Paper

## Background

* * *

[MEGA](https://mega.io) is a cloud storage and communication platform with over 265 million user accounts, advertising itself as secure and private by design. On MEGA, user files should remain confidential even if the storage provider is malicious or has been compromised through a breach, implying security in a strong threat model. The security of MEGA in this setting was recently analysed in detail by [Backendal, Haller and Paterson](https://mega-awry.io), who described five attacks on the cryptographic protocol used by MEGA to authenticate users and encrypt user data. The first two of these attacks completely broke the confidentiality of user files. Further, [Ryan and Heninger](https://eprint.iacr.org/2022/914) significantly improved the first attack, reducing its requirement of 512 user logins to just 6.

At their heart, the original attacks exploit the lack of both key separation and integrity protection for stored keys in the MEGA design. A single user master key is used to encrypt both the user’s RSA private key and the user’s file encryption keys themselves, while AES in ECB mode is used for the encryption. The authors of the original attacks proposed an immediate and non-invasive mitigation step in the form of adding a MAC to the existing construction. In response, MEGA chose to not implement this or any of the other originally suggested countermeasures. Instead, they added [extra sanity checks](https://github.com/meganz/webclient/commit/d2a0d054d4dbb90f035b3b4b421f780adafaa78e) in the client software to do more validation of payloads during or after decryption. These checks were sufficient to prevent the previous attacks.

Shortly after, MEGA made one other change which further increased the attack surface of their code: they added [detailed error reporting](https://github.com/meganz/webclient/commit/cd4ab89b2cd0e388b0ea55753b86c8808f810138) during the decryption and sanity checking processes done by the client as part of the authentication protocol. The errors produced during these steps were mostly distinguishable from one another and the error messages were sent to the server in place of the usual authentication response. A malicious storage provider could exploit this, triggering the errors by supplying specially crafted inputs in an attempt to learn something about the decrypted data.

## Attacks

* * *

We discovered an ECB encryption oracle under a target user’s master key in the MEGA system. The oracle arises in the MEGAdrop feature, which is supposed to be independent of the authentication protocol, yet uses the same master key. This oracle provided an adversary with the ability to partially overwrite a target user’s RSA private key with chosen data, a powerful capability that we use in our attacks.

Our attacks allow an adversary to decrypt blocks encrypted using AES-ECB under the target user’s master key. In the MEGA infrastructure, this enables an attacker to recover blocks of the target user’s RSA private key. To recover the entire key, running either of our attacks to get four specific blocks is sufficient when combined with lattice techniques. Once the private key is recovered, the adversary could trivially recover the keys needed to decrypt any files shared with the target user as well as recover individual file encryption keys directly.

We present two distinct types of attack, each type exploiting different error conditions arising in the sanity checks and in subsequent cryptographic processing during MEGA’s user authentication procedure. The first type appears to be novel and exploits the manner in which the MEGA code handles modular inversion when recomputing \\(u = q^{−1} \bmod p\\). The second can be viewed as a small-subgroup attack. We prototyped the attacks to show that they work in practice on the MEGA webclient.

As a side contribution, we show how to improve the [original RSA key recovery attack](https://mega-awry.io/#rsa-key-recovery) against the unpatched version of MEGA to require only 2 logins instead of the original 512.

The following diagram shows the encoding format of RSA private keys in MEGA.

![MEGA's RSA private key encoding](img/secret_key_encoding.svg)

## Attack based on modular inverse computation

The first attack exploited an implicit error in the computation of modular inverses when sanity checking the RSA private key. It was an (un)fortunate consequence of an otherwise harmless bug in the code (not checking whether an inverse exists) which was caught by the client and reported to the server. The malicious server could use this oracle repeatedly to learn the value of the target AES-ECB plaintext block modulo a number of small primes, which enabled recovery of the full block using the Chinese Remainder Theorem (CRT). On average, the attack requires 627 login attempts per recovered AES-ECB plaintext block and 66 ECB encryption oracle queries per attacked user.

To obtain the entire private RSA key, the attack can be repeated on a block-by-block basis. If the attack was used directly to e.g. recover all of \\(p\\), the number of blocks needed would be 9, but using lattice techniques this can be reduced to 4. The attack complexity of recovering the full RSA private key using our first attack is then 2508 login attempts on average.

## Attack based on small subgroups

The second attack relied on how RSA decryption was carried out by the client during user authentication. It exploited a legacy artefact in the code that changed the resulting RSA plaintext length if a certain byte condition on the plaintext did not hold, in combination with an explicit error arising from a plaintext length check that was again reported to the server. The attack is a form of a [small order subgroup attack](https://doi.org/10.1007/BFb005224), in that it relies on the ECB encryption oracle to overwrite the RSA primes \\(p, q\\) with values such that \\((p − 1)(q − 1)\\) has known small prime factors. This forces the client’s decryption to take place in one of several small subgroups.

The attack also overwrites the user’s private key value \\(d\\) with a value that is completely known except in the target plaintext block. Then, the malicious server could use the length check oracle repeatedly to learn the value of \\(d\\), and hence the target plaintext block, modulo each of the small primes. The final step again combines these values using the CRT to recover the target block. We present two versons of this attack, requiring on average 2419 and 3169 login attempts per block, respectively, and up to 15 ECB encryption oracle queries per attacked user. This attack exploits different errors and checks from the first one: we include it to showcase that the existence of such checks and differentiated error reporting increases the attack surface.

## Disclosure

* * *

We informed MEGA about the vulnerabilities in their system on 29 September 2022, which MEGA acknowledged on 30 September 2022. We suggested mitigations, stressing the importance of providing proper cryptographic integrity for data stored under users’ master keys. We recommended auditing or replacing [MEGA’s asmcrypto.js](https://github.com/meganz/webclient/blob/v4.21.4/js/vendor/asmcrypto.js), the low-level library used by the MEGA webclient (an old, custom copy of [asmcrypto.js](https://github.com/asmcrypto/asmcrypto.js)), in which we found several bugs during our analysis. MEGA informed us about their planned overhaul of the protocol that should address the issues we highlighted and we provided feedback. Given the scale of the changes, we agreed to extend the original 90-day disclosure period. On 6 March 2023, MEGA published a [blogpost](https://blog.mega.io/e2ee-security-update/) detailing their client software upgrade. MEGA awarded a bug bounty.

## Paper

For more details see our paper.  
  
**_Caveat Implementor!_ Key Recovery Attacks on MEGA**  
Martin R. Albrecht, Miro Haller, Lenka Mareková, and Kenneth G. Paterson  
_Accepted at EUROCRYPT 2023._

[Read Paper](pdf/mega-key-recovery.pdf)

## Q & A

* * *

####  Which clients were affected? 

We looked at the official [MEGA Web Client](https://github.com/meganz/webclient) version 4.21.4. As per [MEGA’s blogpost](https://blog.mega.io/e2ee-security-update/), the fixes were deployed in web client version 4.32.4. See the post for the versions of the official mobile and desktop clients that were also upgraded.

####  What is the difference between the two attacks? 

The attacks share the same adversarial model and both make use of the ECB encryption oracle. They exploit different error conditions to achieve the same goal: the ability to decrypt ECB blocks encrypted under the master key.

####  Why was the original patch insufficent to prevent further attacks? 

On its own, the added sanity checks prevented the specific attacks of [Backendal, Haller and Paterson](https://mega-awry.io) and [Ryan and Heninger](https://eprint.iacr.org/2022/914). However, the patch did not address their root cause: the lack of key separation and integrity protection for stored keys. It is thus unsurprising that different attacks could be found.

####  Is the proof-of-concept code available? 

Yes, you can find our implementation [here](https://github.com/MEGA-caveat/mega-caveat-poc).

####  Are the attacks practical? 

In their current form, they require the attacked user to log in hundreds of times, more than the original RSA key recovery attack of [Backendal, Haller and Paterson](https://mega-awry.io). However, as the work of [Ryan and Heninger](https://eprint.iacr.org/2022/914) and our own optimisation of the original attack have shown, attacks that were previously thought impractical can quickly reach practical levels.

## Research Team

* * *

This research was conducted by [Prof. Dr. Martin R. Albrecht](https://malb.io), [Miro Haller](https://mirohaller.com), [Lenka Mareková](https://pure.royalholloway.ac.uk/en/persons/lenka-marekova), and [Prof. Dr. Kenny Paterson](https://inf.ethz.ch/people/person-detail.paterson.html).
