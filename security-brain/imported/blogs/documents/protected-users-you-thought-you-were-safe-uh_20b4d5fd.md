---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-31_protected-users-you-thought-you-were-safe-uh.md
original_filename: 2023-03-31_protected-users-you-thought-you-were-safe-uh.md
title: 'Protected Users: you thought you were safe uh?'
category: documents
detected_topics:
- command-injection
- otp
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- api-security
- mobile-security
language: en
raw_sha256: 20b4d5fddb7faaff188f12dbd0ca99611fefafca5096b71b6202d97880b6aed4
text_sha256: b367af7eaee37159fb32eb58d77bd075f35741a18f0bfa3f0ef2f44675222fcd
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Protected Users: you thought you were safe uh?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-31_protected-users-you-thought-you-were-safe-uh.md
- Source Type: markdown
- Detected Topics: command-injection, otp, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `20b4d5fddb7faaff188f12dbd0ca99611fefafca5096b71b6202d97880b6aed4`
- Text SHA256: `b367af7eaee37159fb32eb58d77bd075f35741a18f0bfa3f0ef2f44675222fcd`


## Content

---
title: "Protected Users: you thought you were safe uh?"
page_title: "SensePost | Protected Users: you thought you were safe uh?"
url: "https://sensepost.com/blog/2023/protected-users-you-thought-you-were-safe-uh/"
final_url: "https://sensepost.com/blog/2023/protected-users-you-thought-you-were-safe-uh/"
authors: ["Aurélien Chalot (@Defte_)", "Thomas SEIGNEURET (@_zblurx)"]
programs: ["Microsoft (Windows)"]
bugs: ["Active Directory", "Kerberos", "NTLM", "Internal pentest"]
publication_date: "2023-03-31"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1314
---

On the 31st of October 2022, a PR on [CrackMapExec from Thomas Seigneuret (@Zblurx)](https://github.com/Porchetta-Industries/CrackMapExec/pull/655) was merged. This PR fixed Kerberos authentication in the CrackMapExec framework. Seeing that, I instantly wanted to try it out and play a bit with it. While doing so I discovered a weird behaviour with the Protected Users group. In this blogpost I’ll explain what the Protected Users group is, why it is a nice security feature and yet why it is incomplete for the Administrator (RID500) user.

## I/ Usual internal assessment scenario and PtH/OPtH

In my [previous blogpost about Windows Access Tokens](https://sensepost.com/blog/2022/abusing-windows-tokens-to-compromise-active-directory-without-touching-lsass/) I described one of the most common scenarios we encounter on internal assessments. Basically we compromise one server, dump its SAM database and LSASS memory to retrieve cleartext credentials or NT hashes. We can also dump Kerberos tickets and generally any other material that we could use to connect elsewhere:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/c252d25f2b050eb097d1533fdfe8dafd.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/c252d25f2b050eb097d1533fdfe8dafd.png)

Whether it is in the SAM database or in the memory of the LSASS process, you will probably find NT hashes:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/7923b49b9f97f221bd81f4175e6d10b4.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/7923b49b9f97f221bd81f4175e6d10b4.png)

On Windows, having a NT hash is equivalent to having a cleartext password. If we take a look at the NTLM authentication protocol we can see that the challenge is cyphered using the NT hash of the user:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/a9e76f9015aa64cb23e3e74859f746bf.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/a9e76f9015aa64cb23e3e74859f746bf.png)

Since we have the NT hash we can cypher the challenge without knowing the corresponding cleartext password. 

On Kerberos it is pretty much the same. The Kerberos authentication protocol relies on four packets which are:

  * KRB_AS_REQ
  * KRB_AS_REP
  * KRB_TGS_REQ
  * KRB_TGS_REP

The process is the following:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/32462562aa759b9637df0822e552dae1.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/32462562aa759b9637df0822e552dae1.png)

The important part is the “timestamp ciphered with a key derived from the password of the user”. As a user, we can cipher the timestamp using a key that can be obtained using one of the following algorithms:

  * RC4 
  * DES
  * AES-128
  * AES-256

The interesting thing is that RC4 cyphers the timestamp using the NT hash of the user. Since we have a valid NT hash, we can cipher the timestamp and have a valid KRB_AS_REQ packet. With the CrackMapExec framework we can now connect to remote servers using two well known attacks:

  * Pass the Hash (for the NTLM authentication protocol):

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/8033372237ca82b4efd3bcb18f0dcb44.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/f14d3e165212758ca207a9bfd5e56331.png)

  * OverPass the Hash (for the Kerberos authentication protocol):

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/8b10c46bb4a1631e82bd4407a484a477.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/02e6914e81fc0c1043f3f73b99756411.png)

These attacks rely on the fact that it is possible to use a NT hash to cypher a secret used to authenticate a user. To protect against this, one approach is to add sensitive users to the “Protected Users” group.

## II/ Protected Users group

The “Protected Users” group was introduced in Windows Server 2012R2. If we take a look at the [MSDN](https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group) article we can see that users in this group have hardened security options:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/90f2361e90cca21e39f2bcf3ac46d1b7.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/90f2361e90cca21e39f2bcf3ac46d1b7.png)

As you can see, NTLM authentication is disabled, the RC4 algorithm cannot be used to cipher the timestamp for Kerberos authentication and finally, Kerberos delegation is disabled. Let’s test this.

First I will add a new domain administrator user (admin2) that is in the “Protected Users” group:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/6b394e668501b2287e74b324041929e0.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/6b394e668501b2287e74b324041929e0.png)

Now let’s try to authenticate using NTLM:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/ef3243ecdb60a9d21d167c04d3bcb198.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/64cb6a62c98ca83b6c34a8666fe66e92.png)

As you can see it’s not working, we receive the “STATUS_ACCOUNT_RESTRICTION”. And now lets try using Kerberos:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/dbbd80f225de9f5fefb6e686531442b1.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/69d47bbd5758c84c1e7cf67677aa8514.png)

It’s not working either (KDC_ERR_PREAUTH_FAILED). So yeah it looks like the expected Protected Users security features apply to the admin2 user. But do they apply to all users ?

## III/ The strange behaviour

**1 – The RC4 key case**

While I was playing with the CrackMapExec PR, I randomly tried to authenticate using Kerberos as the WHITEFLAG/Administrator account and what I realised was that it works even if the user is in the Protected Users group:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/4fc3ba70098e19ac1a765860b0ed846f.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/d0bed304ff420efa7ffdf8cdcf6042ad.png)

In contrast, NTLM authentication fails:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/6f1837e7d745505972e3e8347b489bb0.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/d1320f63991dd9e64b6d2ae49c8156d5.png)

Which means that the restriction of the Protected Users group is not complete when it comes to the RID500 user of the Active Directory domain. We cannot connect using the NTLM authentication protocol but we can connect using the Kerberos authentication protocol with RC4.

**2 – The delegation case**

Another strange behaviour relates to Kerberos Delegation. Normally, when a user is in the Protected Users group, they cannot be delegated. Here I’m trying to abuse a RBCD delegation scenario from OCD$ to ADCS1$ to get a service ticket first as **pu_user** , which is a Protected Users, and second as **not_pu_user** , which is not. First, lets take a look at the delegation:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/6a637a856c716c55f40ede03fc812135.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/6a637a856c716c55f40ede03fc812135.png)

Lets look at the difference between RBCD delegating pu_user and not_pu_user:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/75132f56ff1aa523c3a23b35a8bbced5.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/1afcb093d920681701da9a3b681c59e5.png)

We clearly see a difference: Protected Users cannot be delegated. But wait, lets see how things are going with the RID 500 Administrator account…

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/8f2300f042cb789dccf1ffdcf47e0f3f.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/9df80df8a62b00b3da4c6d34a35c7831.png)

Even if the RID 500 Administrator account is in the Protected Users group, they can be delegated. Ok, but why ?

RBCD delegation abuse consists of the following two steps:

  * S4U2Self : Request a service ticket for an arbitrary user to the controlled account.
  * S4U2Proxy: Request a service ticket as the arbitrary user to the targeted machine account, using the previously obtained service ticket as an additional ticket. 

When you try to impersonate Protected Users, the S4U2Self gives you a service ticket **without** the **forwardable** flag set. This is why the S4U2Proxy part fails with a KDC_BADOPTION error. However, when impersonating the RID 500 Administrator user, the **forwardable** flag is set regardless of whether the user is a Protected User:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/32013d0d480bbbe6f2e47fd7b889acba.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/11272a2cd7bb3841951807d2c09b0028.png)

## IV/ Exploitation scenario

**1 – The RC4 key case**

Using this bug we can execute a particular scenario. Let’s say that we have a fictitious company called Whiteflag. Two years ago they created their Active Driectory domain (whiteflag.local) without taking care of security. Thus, they were using the RID500 account of the domain (WHITEFLAG/Administrator) to administer their servers.

Fast forward a year ago, they asked for an internal assessment. Pentesters were able to compromise the domain and told the security team to add all domain administrators users to the Protected Users group. The security team did this but since they were not properly closing RDP sessions, the NT hash of the WHITEFLAG/Administrator account was still stored in the memory of the LSASS process.

Today you are hired to test their newly hardened Active Directory network. If you can compromise a server on which a RDP session is still active for the WHITEFLAG/Administrator account, you will be able to retrieve its NT hash. Since Protected Users restrictions are not enforced for that user you will be able to connect to the DC using Kerberos authentication.

Yeah I know, it’s a very specific scenario but hey, it could happen! Another interesting thing is that Kerberos delegation will also work for this account.

**2 – The delegation case**

Here the scenario is more straight forward. If every administrator account is in Protected Users and you need to abuse a RBCD delegation scenario (or any other Kerberos delegation), you can just choose to impersonate the RID 500 Administrator account and it will work!

## V/ Remediation

If we take a look at the attributes of the RID500 account we can see that the ms-DSSupportedProtocolEncryption value is set to 0x0

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/af9d51b0d42576ded9f3dce5ae8c2f85.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/af9d51b0d42576ded9f3dce5ae8c2f85.png)

This attribute holds a hexadecimal value that indicates which type of authentication protocol is enabled for that account. Since the value is 0x0, we can conclude that any authentication protocol can be used. If we set this value to 24 (0x18) which only enables AES-128 and AES-256:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/35b0b5ecfece09858c61dfb201ad9cf3.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/35b0b5ecfece09858c61dfb201ad9cf3.png)

We will see that we can still connect using the OverPass-the-Hash attack. The only way I found to completely disable RC4 is to restrict it for the entire Active Directory environment which could be dangerous if servers / applications still rely on this type of authentication.

To avoid the delegation trick you need to tick the option “Account is sensitive and cannot be delegated” even if the RID500 account is in Protected Users.

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/a9784f5469d6101870be7315a2101675.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/a9784f5469d6101870be7315a2101675.png)

Another fix would be to simply disable the RID500 domain account which, [according to the Microsoft documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-d--securing-built-in-administrator-accounts-in-active-directory), is dangerous as well:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/8f21bb42b33467ef2653f8c2cbeb58d2.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/8f21bb42b33467ef2653f8c2cbeb58d2.png)

Note that this bug was reported to MSRC. They replied that this behaviour is intended and is not a bug. Still, the RID500 account can be abused so be aware of it ;)!

* * *

This article was co-written by Aurélien CHALOT ([@Defte_](https://twitter.com/Defte_)) and Thomas SEIGNEURET ([@_zblurx](https://twitter.com/_zblurx)). We would also like to thank some friends for these late night talks we had in order to try to understand what was happening: Charlie BROMBER ([@_nwodtuhs](https://twitter.com/_nwodtuhs)), Martial PUYGRENIER ([@mpgn_x64](https://twitter.com/mpgn_x64)), Wilfried BECARD ([@tiyeuse](https://twitter.com/tiyeuse)) as well as the the [Hide&Sec](https://hideandsec.sh/) community.

This article is a cross-post from https://blog.whiteflag.io.
