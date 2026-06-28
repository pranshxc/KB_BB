---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-25_new-attack-paths-as-requested-service-tickets.md
original_filename: 2022-09-25_new-attack-paths-as-requested-service-tickets.md
title: New Attack Paths? AS Requested Service Tickets
category: documents
detected_topics:
- access-control
- idor
- command-injection
- otp
- rate-limit
- api-security
tags:
- imported
- documents
- access-control
- idor
- command-injection
- otp
- rate-limit
- api-security
language: en
raw_sha256: 1e825402bfa5ef4d24c67687b9af74b056de803c5f0ac08f228d3a665e5406ec
text_sha256: 47c61b9bf0ba479371892fdce1a6a956315a5a5d78796a3ee20853a4647b1b04
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# New Attack Paths? AS Requested Service Tickets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-25_new-attack-paths-as-requested-service-tickets.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection, otp, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `1e825402bfa5ef4d24c67687b9af74b056de803c5f0ac08f228d3a665e5406ec`
- Text SHA256: `47c61b9bf0ba479371892fdce1a6a956315a5a5d78796a3ee20853a4647b1b04`


## Content

---
title: "New Attack Paths? AS Requested Service Tickets"
page_title: "New Attack Paths? AS Requested Service Tickets - Semperis"
url: "https://www.semperis.com/blog/new-attack-paths-as-requested-sts/"
final_url: "https://www.semperis.com/blog/new-attack-paths-as-requested-sts/"
authors: ["Charlie Clark (@exploitph)"]
programs: ["Microsoft"]
bugs: ["Local Privilege Escalation", "Windows", "Kerberos", "Active Directory"]
publication_date: "2022-09-25"
added_date: "2022-09-29"
source: "pentester.land/writeups.json"
original_index: 2116
---

[Back to blogs listing](/blog/)

# New Attack Paths? AS Requested Service Tickets

  * Active Directory Security
  * Read 10 MIN

**Table of Contents**

  * Kerberos recap
  * The issue with AS requested service tickets
  * New ways to Kerberoast
  * Bypassing detections
  * Other consequences of AS requested service tickets
  * Detection of AS requested service tickets

**Charlie Clark**

While helping [Andrew Schwartz](https://twitter.com/4ndr3w6S) with his [Kerberos FAST post](https://www.trustedsec.com/blog/i-wanna-go-fast-really-fast-like-kerberos-fast/) (which has more information about what FAST is and how it works, so have a read), I noticed something interesting. AS-REQs for machine accounts are unarmored. [Kerberos armoring](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831747\(v=ws.11\)#kerberos-armoring-flexible-authentication-secure-tunneling-fast) is described by Microsoft:

> **Kerberos armoring uses a ticket-granting ticket (TGT) for the device to protect authentication service exchanges with the KDC, so the computer’s authentication service exchange is not armored. The user’s TGT is used to protect its TGS exchanges with the KDC.**

This made me wonder whether it was possible to request service tickets (STs) from the authentication service (AS). The ability to request STs from the AS has several consequences, including new attack paths, detection bypasses, and potential weakening of security controls. All the issues discussed in this post were reported to Microsoft and were “considered to be by design” (_Figure 1_).

### Related reading

  * **[Active Directory Security: Top Risks& Best Practices](https://www.semperis.com/blog/active-directory-security/what-is-active-directory-security/)**

### Kerberos recap

First, here’s a high-level overview of the typical Kerberos flow (_Figure 2_ , sourced from [ADSecurity](https://adsecurity.org/?p=1515)):

  1. An account requests a TGT from the domain controller (DC).
  2. The DC responds with a TGT, which has its own session key.
  3. The TGT and its session key are used to request a service ticket (ST) from the DC.
  4. The DC responds with an ST, which has its own session key.
  5. The ST and its session key are used to authenticate against the end service.
  6. The end service either grants or prohibits access.

![Figure 2. Typical Kerberos flow \(AD Security\), illustrating the steps in the previous list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 2. Typical Kerberos flow (ADSecurity)_

The fact that a session key is issued for each ticket is an important feature for the following research. This session key is passed back to the requesting account within an encrypted section of the response; the encryption key is already known to the requestor.

For instance, the TGT session key is stored within a section that is encrypted with the key used to prove the requestor’s identity when requesting a TGT. This key is normally the long-term key (password hash) of the account. But in the case of Public Key Cryptography for Initial Authentication (PKINIT) in the Kerberos protocol, the key is derived from the certificate. The ST session key is stored within a section that is encrypted with the TGT session key.

The ticket session key is required to use the ticket in the next step of the Kerberos flow.

A Kerberos request has two main sections:

  * padata (pre-authentication data)
  * req-body (request body)

The req-body is sent mostly in plaintext and contains several pieces of information:

  * **kdc-options** : various options
  * **cname** : name of the requesting account (optional)
  * **realm** : domain name
  * **sname** : service principal name (SPN) for the resulting ticket (optional)
  * **from** : time from which the client wants the ticket to be valid (optional)
  * **till** : time until which the client wants the ticket to be valid
  * **rtime** : the requested renew time (optional)
  * **nonce** : random number
  * **etype** : list of supported encryption types of the client
  * **addresses** : list of addresses of the requesting client (optional)
  * **enc-authorization-data** : various authorization data sections, encrypted with the session key that is usually used for local privileges (optional)
  * **additional-tickets** : list of tickets required for the request (optional)

A Kerberos reply has several sections and contains an encrypted part:

  * **pvno** : version number
  * **msg-type** : type of message (11 AS, 13 TGS)
  * **padata** : pre-authentication data (optional)
  * **crealm** : client domain name
  * **cname** : name of the requesting account
  * **ticket** : resulting ticket
  * **enc-part** : encrypted data for use by the client

### The issue with AS requested service tickets

The part of the Kerberos flow that this post focuses on is AS-REQ/AS-REP, which is usually used to request a TGT. In normal operations, an AS-REQ has one of two values within its **sname** field inside the req-body:

  * _krbtgt/domain.local:_ used to request an initial TGT
  * _kadmin/changepw_ : used to request a short-lived ticket, which can be used to reset passwords using a KRB-PRIV message (defined in [RFC 3244](https://www.rfc-editor.org/rfc/rfc3244.html))

I noticed that with [Kerberos Flexible Authentication Secure Tunneling (FAST)](https://www.rfc-editor.org/rfc/rfc6113.html) enforced, machine accounts still sent their AS-REQs unarmored. I wondered whether an AS-REQ could be used to request an ST directly, rather than a TGT. This caused me to modify Rubeus to determine whether specifying another SPN within the **sname** of an AS-REQ would cause the DC to reply with an ST for that SPN. As it turns out, the answer was “yes” (_Figure 3_).

![Figure 3. Screenshot of an AS requested ST](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 3. Service ticket requested from the AS_

By using a machine account, I can request an ST without using armoring when FAST is enforced. What else is possible?

### New ways to Kerberoast

[Kerberoasting](https://adsecurity.org/?p=3458), discovered by [Tim Medin](https://twitter.com/TimMedin), is a method to recover the plaintext password or [NT hash](https://github.com/hashcat/hashcat/pull/2607) for a service account, generally a user account with an SPN. Kerberoasting is possible because part of an ST is encrypted with the service account’s long-term key (password hash). By extracting the encrypted part of the ticket, it is possible to form a hash from various cleartext passwords and attempt to decrypt the encrypted part. If decryption is successful, then the hash used is the long-term key used to encrypt the ticket. That key can then ultimately be used to authenticate as the service account.

Furthermore, any account can request an ST for any service. Therefore, the ability to authenticate to Active Directory (AD) is required to perform the attack. At least, that _used_ to be true.

#### Kerberoasting without pre-authentication

First, I tried to use an account that did not require pre-authentication ([DONT_REQ_PREAUTH](https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/useraccountcontrol-manipulate-account-properties)) to request an ST. When an account does not require pre-authentication to authenticate, a TGT can be requested without requiring pre-authentication data, which is encrypted with some form of credential (e.g., password hash, certificate). If an attacker has not obtained a valid credential for an account, valid pre-authentication cannot be generated. If pre-authentication is not required, this is not an issue.

When a ticket is requested without pre-authentication, the result still includes an encrypted part. This encrypted part is encrypted with the credential key used for authentication and contains the session key for the ticket included within the reply. This is the encrypted data used in the [ASREPRoast attack](https://harmj0y.medium.com/roasting-as-reps-e6179a65216b) by [Will Schroeder](https://twitter.com/harmj0y). The resulting TGT is usable only with access to the requesting accounts key, since the TGT session key is required.

However, for Kerberoasting, access to the session key is not required. Only the resulting ST—or more accurately, the encrypted part of the ST, which is not secured with the requesting accounts key—is required. Therefore, if any account is configured to not require pre-authentication, it is possible to Kerberoast without **any** credentials. This method of Kerberoasting has been implemented in Rubeus within [this PR](https://github.com/GhostPack/Rubeus/pull/139).

##### Demonstration

Because access to a valid account has not yet been achieved, LDAP cannot be queried. Instead, a list of potential service accounts is required. [Previous research](https://swarm.ptsecurity.com/kerberoasting-without-spns/) by [Arseniy Sharoglazov](https://twitter.com/_mohemiv) shows that STs can be requested using only the username of the service account rather than requiring the actual SPN—very useful for this research.

A list of usernames can be generated in several ways, including user enumeration using null sessions on a DC, generating a list of usernames using open-source intelligence (OSINT), or guessing potential usernames. Any list of potential usernames can be easily verified by sending an AS-REQ without pre-authentication. A valid username that requires pre-authentication receives a **KDC_ERR_PREAUTH_REQUIRED** error (_Figure 4_).

![Figure 4. Screenshot showing an AS-REQ without pre-auth for a valid username that requires pre-auth](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 4. User requires pre-authorization_

A valid username that does not require pre-authentication receives a TGT (_Figure 5_).

![Figure 5. Screenshot showing response for a user that does not require pre-auth](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 5. User does not require pre-authorization_

An invalid username receives a **KDC_ERR_C_PRINCIPAL_UNKNOWN** error (_Figure 6_).

![Figure 6. Response for an invalid username](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 6. User does not exist_

For demonstration purposes, a list is generated using a null session on the DC, using [enum4linux-ng](https://github.com/cddmp/enum4linux-ng)’s RID cycling method (_-R_), as _Figure 7_ shows.

![Figure 7. Screenshot showing generated list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 7. enum4linux-ng RID cycling_

Using this list of usernames, determining accounts that do not require pre-authentication is easy in AD (_Figure 8_).

![Figure 8. Output of a scan for accounts that do not require pre-auth](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 8. Scan for accounts not requiring pre-authentication_

Note that AS-REQs without pre-authentication are not logged as a Windows event unless the account does not require pre-authentication.

With the list of usernames and the username of an account that does not require pre-authentication, the attack can be launched (_Figure 9_).

![Figure 9. Screenshot showing Kerberoasting without pre-auth](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 9. Kerberoasting without pre-authorization_

The resulting output can then be used to attempt offline password cracking.

#### Proof of concept: RoastInTheMiddle

Another interesting consequence is the ability to Kerberoast from a [Man-in-the-Middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) (MitM) position. This type of attack generally is not possible with TGS-REQs because the optional **cksum** field within the _authenticator_ inside the [AP-REQ](https://www.rfc-editor.org/rfc/rfc4120#section-5.5.1) protects the _req-body_ of the request and is frequently included by genuine Windows Kerberos clients. Therefore, modifying the **sname** of a TGS-REQ without updating the checksum within the authenticator invalidates the authenticator checksum and returns a **KRB_AP_ERR_MODIFIED** error. But this is not a problem for AS-REQs because the **req-body** , and consequently the **sname** field, are not protected.

While testing this approach, I discovered that AS-REQs can be replayed many times. An attacker needs to capture only one AS-REQ to send a lot of AS-REQs with different **sname** values.

##### Demonstration

To demonstrate this approach, I wrote a rough proof of concept (POC). This POC, [RoastInTheMiddle](https://github.com/0xe7/RoastInTheMiddle), implements an [ARP spoof](https://en.wikipedia.org/wiki/ARP_spoofing) between DCs and victim systems to perform an MitM attack. The POC then passes traffic through while listening for AS-REQs. When an AS-REQ is found, the POC performs a Kerberoast. The POC is not attack-ready but demonstrates that an attack is possible.

First, the POC starts four threads, a sniffer, an ARP spoofer, a re-assembler (for requests that are split across multiple packets), and the roaster (_Figure 10_).

![Figure 10. Screenshot showing the RoastInTheMiddle POC starting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 10. RoastInTheMiddle starting up_

When it sees an AS-REQ, the POC starts trying to Kerberoast the supplied list, which can contain usernames or SPNs (_Figure 11_).

![Figure 11. Screenshot showing POC Kerberoasting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 11. RoastInTheMiddle Kerberoasting_

As Figure 11 shows, this attempt results in any received STs being output in hashcat format, ready for offline password cracking.

The ability to MitM AS-REQs, then modify and replay them, might also be useful in developing other attacks. I attempted to modify the _kdc-options_ to include the [**proxiable**](https://www.rfc-editor.org/rfc/rfc4120#section-2.5) flag, which results in a ticket with the **proxiable** flag set. However, I was unable to find an attack path using that ticket and flag. This behavior might also enable the use of other accounts to perform a Kerberoast, enabling attackers to avoid burning a compromised account.

##### Improvements

Some improvements might be possible for this process. First, it is possible to coerce an AS-REQ from a TGS-REQ by intercepting it and replying with a **KRB_AP_ERR_BAD_INTEGRITY** error. Doing so forces the client to reauthenticate by sending an AS-REQ.

It should also be possible to perform this attack using DHCPv6 nameserver injection (like [mitm6](https://github.com/dirkjanm/mitm6) by [Dirk-jan Mollema](https://twitter.com/_dirkjan) or [Inveigh](https://github.com/Kevin-Robertson/Inveigh) by [Kevin Robertson](https://twitter.com/kevin_robertson)), responding to SRV DNS queries for the LDAP service and then dealing with the following LDAP connection.

Support for modifying the **etypes** within the request enables encryption type downgrade attacks when the environment allows, as described by Will Schroeder [here](https://blog.harmj0y.net/redteaming/kerberoasting-revisited/).

Lastly, the POC requires the installation of [Npcap](https://npcap.com/) on the system running the POC (which uses [sharppcap](https://github.com/dotpcap/sharppcap)), primarily for ARP spoofing. If you take the IPv6 route or implement the ARP replies by using raw sockets, you can remove this dependency.

### Bypassing detections

Many Kerberos detections rely on [4769 events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4769) (_A Kerberos service ticket was requested_). However, requesting a service ticket using an AS-REQ does not produce 4769 events but rather [4768 events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4768) (_A Kerberos authentication ticket (TGT) was requested_).

_Figure 12_ shows a 4768 event when an ST is requested using an AS-REQ.

![Figure 12. Image of event 4768](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 12. Event 4768 for a service ticket_

Therefore, attackers using this method can easily circumvent many detections that rely on 4769 events.

### Other consequences of AS requested service tickets

Although I was unable to request [S4U2self](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-sfu/02636893-7a1f-4357-af9a-b672e3e3de13) tickets from the AS, STs retrieved from the AS lack the [Ticket Checksum](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-pac/76c10ef5-de76-44bf-b208-0d8750fc2edd) (brought in to protect S4U2self tickets against the [bronze bit attack](https://www.netspi.com/blog/technical/network-penetration-testing/cve-2020-17049-kerberos-bronze-bit-theory/) by [Jake Karnes](https://twitter.com/jakekarnes42)).

Lastly, an ST requested from the TGS is generally returned with a PAC (_Figure 13_).

![Figure 13. Screenshot of ST \(with PAC\) request from the TGS](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 13. Requesting an ST with a PAC from the TGS_

It is possible to request an ST without a PAC from the TGS, but doing so requires changing the service accounts **NO_AUTH_DATA_REQUIRED** bit in the _useraccountcontrol_ attribute (_Figure 14_).

![Figure 14. Output showing attribute](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 14. useraccountcontrol attribute for SDC1 and pgreen_

When this configuration is in place, the returned ST lacks a PAC, as shown by the difference in size of the returned ticket (_Figure 15_).

![Figure 15. Screenshot of ST \(without PAC\) request from TGS](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 15. Requesting an ST without a PAC from the TGS_

An ST without a PAC can be requested from the AS simply by setting the [PA-PAC-OPTIONS](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-kile/99721a01-c859-48d1-8310-ec1bab9b2838) PA data section to false by adding the **/nopac** switch to Rubeus (_Figure 16_).

![Figure 16. Output showing ST request \(without a PAC\) from the AS](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 16. Requesting an ST without a PAC from the AS_

This approach might be used as an alternative to creating silver tickets, by requesting an ST without a PAC, then injecting another PAC by including it within the **enc-authorization-data** section of the request. It might also provide other potential attack paths.

### Detection of AS requested service tickets

Because Microsoft apparently does not find these issues worth fixing, detection from within your organization is the only option. As shown previously, when an ST is requested from the AS, event 4768 is logged (_Figure 17_).

![Figure 17. Screenshot of event 4768](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 17. Event 4768 for a service ticket_

In this event, you can see that the _Service Name_ and _Service ID_ are _not_ **krbtgt.** All genuine tickets requested from the AS, including **kadmin/changepw** tickets, have a _Service Name_ and _Service ID_ of **krbtgt** (_Figure 18_).

![Figure 18. Screenshot showing normal event 4768](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 18. Normal event 4768_

Checking network traffic for AS-REQs that are not for the **krbtgt/domain** or**kadmin/changepw** should also detect these requests (_Figure 19_).

![Figure 19. Screenshot of AS-REQ ST request in Wireshark](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 19. AS-REQ ST request in Wireshark_

**This research, along with Microsoft’s response, demonstrates the need for continuous monitoring and proper hardening measures.** The ability to circumvent current detections and perform effective attacks, like Kerberoasting, from an unauthenticated position is a serious issue that should not be ignored. The research described here could lead to further novel attacks, potentially putting organizations at higher risk.

> **Ensure that detections are in place when these types of ticket requests are made.**

### Acknowledgements

I’d like to that the following people for their contributions to this research:

  * [Andrew Schwartz](https://twitter.com/4ndr3w6S) for sending me down this path with his [Kerberos FAST post](https://www.trustedsec.com/blog/i-wanna-go-fast-really-fast-like-kerberos-fast/) (which you should also read)
  * [Elad Shamir](https://twitter.com/elad_shamir) for letting me bounce these ideas off him
  * [Will Schroeder](https://twitter.com/harmj0y) for writing Rubeus
  * [Tomer Nahum](https://twitter.com/TomerNahum1), [Sapir Federovsky](https://twitter.com/sapirxfed), and [Andrea Pierini](https://twitter.com/decoder_it) for proofreading this post and providing criticism

### Timeline

  * May 25, 2022: Reported to MSRC
  * May 27, 2022: MSRC changed status to Review/Repro
  * July 13, 2022: MSRC responded that the behavior was “by design”
  * September 27, 2022: Public disclosure

### Learn more from Semperis Research

  * [Know Your AD Vulnerability: CVE-2022-26923](/blog/ad-vulnerability-cve-2022-26923/)
  * [A Diamond (Ticket) in the Ruff](/blog/a-diamond-ticket-in-the-ruff/)
  * [Defending Against Active Directory Attacks That Leave No Trace](/resources/defending-against-active-directory-attacks-that-leave-no-trace/)
  * [Purple Knight](https://www.semperis.com/purple-knight/)
  * [Directory Services Protector](/active-directory-security/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### Sign Up for the Latest Semperis News
