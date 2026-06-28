---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-14_ad-security-research-breaking-trust-transitivity.md
original_filename: 2023-03-14_ad-security-research-breaking-trust-transitivity.md
title: 'AD Security Research: Breaking Trust Transitivity'
category: documents
detected_topics:
- cloud-security
- access-control
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- cloud-security
- access-control
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 1994378f1e8d658121d2ea5d4f5c43282e742b769eb6bf935245f77a56678dbf
text_sha256: bb399956fdb922f2d645301cf874e9dbde3d4685a9b61fbee3c02756efb7d92d
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# AD Security Research: Breaking Trust Transitivity

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-14_ad-security-research-breaking-trust-transitivity.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `1994378f1e8d658121d2ea5d4f5c43282e742b769eb6bf935245f77a56678dbf`
- Text SHA256: `bb399956fdb922f2d645301cf874e9dbde3d4685a9b61fbee3c02756efb7d92d`


## Content

---
title: "AD Security Research: Breaking Trust Transitivity"
page_title: "Transitive Trust and Active Directory: Semperis AD 101"
url: "https://www.semperis.com/blog/ad-security-research-breaking-trust-transitivity/"
final_url: "https://www.semperis.com/blog/ad-security-research-breaking-trust-transitivity/"
authors: ["Charlie Clark (@exploitph)"]
programs: ["Microsoft (Windows)"]
bugs: ["Active Directory Privilege Escalation"]
publication_date: "2023-03-14"
added_date: "2023-03-23"
source: "pentester.land/writeups.json"
original_index: 1375
---

[Back to blogs listing](/blog/)

# Transitive Trust and Breaking Trust Transitivity: AD Security 101

  * Active Directory Security
  * Read 12 MIN

**Charlie Clark**

While playing with Kerberos tickets, I discovered an issue that allowed me to authenticate to other domains within an Active Directory (AD) forest across external non-transitive trusts. This means that **there is in fact no such thing as a “non-transitive trust.”** The term is at best misleading and offers systems administrators a false sense of security. **As part of the issue discussed in this post, attackers can authenticate to other domains across a non-transitive trust and potentially elevate privileges within the forest of the trusting domain.** This post details the discovered issue.

After reporting this issue to Microsoft, I received the following response:

![Figure 1. MSRC response](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 1. MSRC response_

As Microsoft determined that the issue does not affect security and therefore does not plan to change the behavior, there is no way to avoid the issue —apart from simply **not using external trusts**.

### Trusts and transitivity

**Note:** This post assumes a basic understanding of trusts and how they work. (For more information on those topics, I suggest reading [Will Schroeder](https://twitter.com/harmj0y)’s [great post](https://blog.harmj0y.net/redteaming/a-guide-to-attacking-domain-trusts/) on trusts.) The post does not cover intra-forest trusts (i.e., trusts within a single forest)—other than as they apply to the specific attack path discussed—or selective authentication trusts – which are incredibly rare in real environments.

The remaining trusts are forest trusts and external trusts.

  * **Forest trusts** are trusts between two forests. More accurately, they are _transitive_ trusts between the root domains of two forests. Any user from any domain within the trusted forest can authenticate to any domain within the trusting forest.
  * **External trusts** are trusts between two domains. These trusts are _non-transitive_. Only users within the trusted domain can authenticate against **only** **the trusting domain** (_Figure 2_).

![Figure 2. External non-transitive trust](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 2. External non-transitive trust_

Microsoft [describes](https://learn.microsoft.com/en-us/azure/active-directory-domain-services/concepts-forest-trust) trust transitivity as follows:

_Transitivity determines whether a trust can be extended outside of the two domains with which it was formed._

  * _A transitive trust can be used to extend trust relationships with other domains._
  * _A non-transitive trust can be used to deny trust relationships with other domains._

This description is clear: For non-transitive trusts, only the two domains involved in the trust can authenticate to each other and not beyond.

**Unfortunately, as I will demonstrate in this post, this is not the case.**

### Lab setup

To properly demonstrate the non-transitive trust issue, I set up the lab with several multi-domain forests that share external trusts (_Figure 3_).

![Figure 3. Lab setup](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 3. Lab setup_

This setup involves three (3) forests. Two (2) of the forests contains three (3) domains. The third forest contains two (2) domains. The domains **semperis.lab** and **treetest.lab** share a bidirectional external non-transitive trust (_Figure 4_).

![Figure 4. External Trust 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 4. External Trust 1_

The domains **grandchild1.child1.semperis.lab** and **semperisaz.lab** also share a bidirectional external non-transitive trust (_Figure 5_).

![Figure 5. External Trust 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 5. External Trust 2_

This setup makes it possible to demonstrate the implications and limitations of the non-transitive trust issue.

### How Kerberos cross-trust authentication works

To authenticate to a service across a trust using Kerberos, you need a referral (also known as a referral ticket granting ticket [TGT]). This is a ticket requested from your local domain controller (DC) for the foreign domain. To demonstrate how ticket requests are performed across trusts, this section focuses on the **semperis.lab** forest. However, this information is applicable to any “allowed” trust path.

**Note:** This post assumes a basic understanding of normal Kerberos authentication flow. (For a detailed explanation of that flow, see [Sean Metcalf](https://twitter.com/PyroTek3)’s [Detecting Kerberoasting Activity](https://adsecurity.org/?p=3458) post.) The remainder of the post uses [Rubeus](https://github.com/GhostPack/Rubeus) to request tickets manually.

The simplest example of cross-trust authentication is the authentication of a service on a domain that has a direct trust with the local domain. The trust that the domain **grandchild1.child1.semperis.lab** has with **child1.semperis.lab** (_Figure 5_) is an example of this type of trust. In this situation, after obtaining an initial TGT, the first step in obtaining a service ticket for an account in **grandchild1.child1.semperis.lab** to a service in **child1.semperis.lab** is to obtain a referral for **child1.semperis.lab** (_Figure 6, Figure 7_).

![Figure 6. Referral request for child1.semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 6. Referral request for child1.semperis.lab_

![Figure 7. Referral request](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 7. Referral request_

The request was made to a DC (**SGC1DC1.grandchild1.child1.semperis.lab**) within the domain (**grandchild1.child1.semperis.lab**) local to the authenticating user (**lowpriv**). The request was made for the service **krbtgt/child1.semperis.lab.** The fact that the ServiceRealm (srealm) is the local domain (**grandchild1.child1.semperis.lab**) within the resulting ticket shows that this ticket is a referral.

This referral can now be used to request service tickets (STs) from the foreign DC (**SC1DC1.child1.semperis.lab**) for the service **host/SC1DC1.child1.semperis.lab**(_Figure 8, Figure 9_).

![Figure 8. Example use of referral](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 8. Example use of referral_

![Figure 9. Requesting ST using referral](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 9. Requesting ST using referral_

To take this one step further, if a service on the forest root domain (**semperis.lab**) is required, a referral for this domain cannot be directly requested from the local (**grandchild1.child1.semperis.lab**) domain. A referral for **krbtgt/semperis.lab** is requested from the local DC **sgc1dc1.grandchild1.child1.semperis.lab**. However, the DC returns a ticket for the service **krbtgt/child1.semperis.lab** , indicating that this referral is for the domain **child1.semperis.lab** , not for **semperis.lab**(_Figure 10, Figure 11_).

![Figure 10. Referral request for semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 10. Referral request for semperis.lab_

![Figure 11. Requesting referral for semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 11. Requesting referral for semperis.lab_

You can see this issue by trying to use this ticket to request an ST for the **semperis.lab** domain. Doing so results in an _AP_ERR_BAD_INTEGRITY_ error. This is because the referral ticket is encrypted with the trust key for the **grandchild1.child1.semperis.lab** **- >** **child1.semperis.lab** trust. The DCs in the **semperis.lab** root domain have no knowledge of this key and so are unable to decrypt the ticket (_Figure 12, Figure 13_).

![Figure 12. Root domain ST request](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 12. Root domain ST request_

![Figure 13. Requesting ST from semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 13. Requesting ST from semperis.lab_

To request a service ticket for the root domain **semperis.lab** , first a referral for **semperis.lab** must be requested from a DC in the domain **child1.semperis.lab,** using this referral.  _Figure 14 and Figure 15_ show a request made to the foreign DC (**sc1dc1.child1.semperis.lab**), using the referral for the domain **child1.semperis.lab** to request a further referral for the root domain **semperis.lab**.

![Figure 14. Referral request for semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 14. Referral request for semperis.lab_

![Figure 15. Requesting referral for semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 15. Requesting referral for semperis.lab_

Note that to request this ticket, the **_/targetdomain_** argument is required. By default, Rubeus uses the domain within the ticket passed to it to fill in the domain in the TGS-REQ. In this case, that domain would be **grandchild1.child1.semperis.lab** and would result in an ERR_WRONG_REALM error because the domain local to the DC is **child1.semperis.lab**. This information will be important in the next section.

Lastly, this resulting referral for **semperis.lab** can be used to request STs for the **semperis.lab** domain.  _Figure 16_ shows the ST request made from the user **lowpriv@grandchild1.child1.semperis.lab** to the DC **SDC1.semperis.lab** for the SPN **host/SDC1.semperis.lab**. Because the trust path is allowed, this request was successful even though the two domains involved do not have a direct trust (_Figure 17_).

![Figure 16. ST request for semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 16. ST request for semperis.lab_

![Figure 17. ST request for host/sdc1.semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 17. ST request for host/sdc1.semperis.lab_

This method of requesting referrals for trusting domains can be followed to request STs for any service within any domain for which the trust path is allowed.

### Making the non-transitive trust transitive

So, how it is possible to traverse external trusts to authenticate to domains that should be prohibited?

The domains **semperisaz.lab** and **grandchild1.child1.semperis.lab** have a bidirectional external trust. Therefore, after retrieving a TGT for any account within the domain **semperisaz.lab** , it is possible to request a referral for **grandchild1.child1.semperis.lab** (_Figure 18, Figure 19_).

![Figure 18. Referral to granchild1.child1.semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 18. Referral to granchild1.child1.semperis.lab_

![Figure 19. Request referral for grandchild1.child1.semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 19. Request referral for grandchild1.child1.semperis.lab_

This referral can be used to request STs for services on the domain **grandchild1.child1.semperis.lab**. However, an attempt to obtain a referral to other domains within the same forest (e.g., **child1.semperis.lab**) returns an ERR_PATH_NOT_ACCEPTED error, as expected (_Figure 20_).

![Figure 20. Path not accepted error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 20. Path not accepted error_

This error occurs because the **semperisaz.lab** **- >** **granchild1.child1.semperis.lab** trust is non-transitive. Therefore, the path from **semperisaz.lab** to **child1.semperis.lab** is not allowed (_Figure 21_).

![Figure 21. Requesting referral for child1.semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 21. Requesting referral for child1.semperis.lab_

However, you _can_ request a _local_ TGT for **grandchild1.child1.semperis.lab**. I call this a local TGT because, unlike the referral—which has a ServiceRealm (srealm) of **semperisaz.lab** —the ServiceRealm of this TGT is **grandchild1.child1.semperis.lab** (_Figure 22, Figure 23_).

![Figure 22. Requesting local TGT For grandchild1.child1.semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 22. Requesting local TGT For grandchild1.child1.semperis.lab_

![Figure 23. Requesting a local TGT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 23. Requesting a local TGT_

Using this local TGT, a referral for **child1.semperis.lab** can now be requested (_Figure 24, Figure 25_).

![Figure 24. Referral for child1.semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 24. Referral for child1.semperis.lab_

![Figure 25. Local TGT to request referral for child1.semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 25. Local TGT to request referral for child1.semperis.lab_

You now have a usable referral that can be used to request STs for **child1.semperis.lab** , using _any_ account from the **semperisaz.lab** domain and without making _any_ changes to trusts or accounts within AD.  _Figure 26_ and _Figure 27_ show an ST request from the DC **sc1dc1.child1.semperis.lab** for the service **host/sc1dc1.child1.semperis.lab** as the user **lowpriv@semperisaz.lab**.

![Figure 26. Requesting ST for DC In child1.semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 26. Requesting ST for DC In child1.semperis.lab_

![Figure 27. Requesting ST for host/sc1dc1.child1.semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 27. Requesting ST for host/sc1dc1.child1.semperis.lab_

Furthermore, this method can be used to hop around any domain within the same forest in which **grandchild1.child1.semperis.lab** exists. We can demonstrate this by requesting a referral to the root domain **semperis.lab**. A referral was requested for **semperis.lab** from the DC **sc1dc1.child1.semperis.lab** as the user lowpriv@semperisaz.lab (_Figure 28, Figure 29_).

![Figure 28. Requesting referral for semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 28. Requesting referral for semperis.lab_

![Figure 29. Requesting referral to semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 29. Requesting referral to semperis.lab_

Fortunately, hopping across further trusts outside of the forest (external or forest trusts) is not possible using this method. As _Figure 3_ shows, the root domain **semperis.lab** has a bidirectional external trust with **treetest.lab.** This trust can be used to demonstrate that limitation (_Figure 30, Figure 31_).

![Figure 30. Requesting referral for treetest.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 30. Requesting referral for treetest.lab_

![Figure 31. Requesting referral for treetest.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 31. Requesting referral for treetest.lab_

This at least stops an attacker using this method from trust hopping into another forest. Still, this non-transitive trust issue is clearly useful for attackers trying to elevate privileges within a forest from across a trust. Attackers could query domain information from supposedly disallowed domains, query more sensitive domains or domains with potentially weaker security, or perform Kerberoasting attacks or NTLM authentication coercion on domains that are assumed to be disallowed.

### Hopping further

Although attackers cannot hop further using the method described in this post alone, the issue could open new avenues of attack. I previously wrote a post demonstrating the ability to [create machine accounts across trusts](https://exploit.ph/strange-case-of-trusts-machines-dns.html) and the implications of that. By incorporating that method of domain hopping with this new method, it is possible to overcome the limitation described at the end of the previous section.

Using the referral retrieved for **semperis.lab**(at the end of the previous section), it is possible to request a ticket for the **LDAP** service on a DC in **semperis.lab**. Here, a ST for **ldap/sdc1.semperis.lab** was requested using the referral for **semperis.lab** as the user lowpriv@semperisaz.lab (_Figure 32, Figure 33_).

![Figure 32. Request ST for ldap](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 32. Request ST for ldap_

![Figure 33. Request ST for ldap/sdc1.semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 33. Request ST for ldap/sdc1.semperis.lab_

This ST can be injected and used to create a machine account directly in **semperis.lab** if the configuration allows **Authenticated Users** , which is the default (_Figure 34_).

![Figure 34. Create machine account in semperis.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 34. Create machine account in semperis.lab_

This action causes the DC **sdc1.semperis.lab** to create the machine account **TestComp** within the **semperis.lab** domain (_Figure 35_).

![Figure 35. Create machine account TestComp](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 35. Create machine account TestComp_

The new **TestComp** machine account is a local account within the domain **semperis.lab**. Now, you can retrieve a TGT for that machine account (_Figure 36, Figure 37_).

![Figure 36. Machine account TGT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 36. Machine account TGT_

![Figure 37. Requesting TGT for TestComp](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 37. Requesting TGT for TestComp_

This machine account TGT is allowed to request a referral to the trusting domain **treetest.lab**. The machine account TGT can be used to request a referral for the **treetest.lab** domain from the DC **SDC1.semperis.lab**(_Figure 38, Figure 39_).

![Figure 38. Requesting referral for treetest.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 38. Requesting referral for treetest.lab_

![Figure 39. Request referral for treetest.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 39. Request referral for treetest.lab_

Lastly, the issue described in this post can be used to gain access to the inaccessible **dsptest.lab** domain. First, request a local TGT for **treetest.lab**. The local TGT is requested using the referral for **treetest.lab** as the account **TestComp$@semperis.lab** from the DC **TDC1.treetest.lab** (_Figure 40, Figure 41_).

![Figure 40. Requesting local TGT for treetest.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 40. Requesting local TGT for treetest.lab_

![Figure 41. Requesting local TGT for treetest.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 41. Requesting local TGT for treetest.lab_

Next, use this local TGT to request a referral for **dsptest.lab**.  _Figure 42_ and _Figure 43_ shows that a referral was requested for the domain **dsptest.lab** from the DC **TDC1.treetest.lab** as the user **TestComp$@semperis.lab**.

![Figure 42. Requesting referral for dsptest.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 42. Requesting referral for dsptest.lab_

![Figure 43. Requesting referral for dsptest.lab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 43. Requesting referral for dsptest.lab_

Clearly, combining these two methods could make it possible to hop very deep into AD enterprise infrastructures, using any low-privileged account on a domain that has an external trust to any domain within a forest.

### Detection of trust transitivity vulnerability

Unfortunately, given Microsoft’s response, the only way to avoid the issue is to remove external trusts.

If removing all external trusts is not possible, you’ll need to monitor for Windows event [4769](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4769) (_A Kerberos service ticket was requested_). The first indication to look for is that a local TGT was requested from an account in a different forest (_Figure 44_).

![Figure 44. 4769 for local TGT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 44. 4769 for local TGT_

Here, the _Account Domain_ field is a domain that belongs to a different forest and the _Service Name_ is **krbtgt**. This event is followed by another event 4769, requesting a referral (_Figure 45_).

![Figure 45. 4769 for referral](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)_Figure 45. 4769 for referral_

Here, the _Account Domain_ is a domain within a different forest and the _Service Name_ is another domain within the local forest.

Note that these two events can occur on different DCs within the same domain. The events do _not_ need to occur on the same DC. At this point, any requested STs (event 4769) that use this referral will have an _Account Domain_ that contains a domain that should not be allowed to authenticate to the local domain.

Look for monitoring for these events and detection of this type of attack in a future release of Semperis [Directory Services Protector](/ds-protector/) (DSP).

### Who can you trust?

As you can see, the official description of external non-transitive trusts is misleading. As it stands, **when you create an external non-transitive trust, you must accept that any account within the trusted domain will be able to authenticate against _any_ domain within the _entire_ forest in which the trusting domain resides**.

As demonstrated in the Hopping Further section of this post, best practice is to disallow Authenticated Users from creating machine accounts. Not doing so not only puts domains within the forest at higher risk of attack, but also puts any domains (and the forest in which they reside) that have an external trust with any domain within the forest at a higher risk due to the ability to create machine accounts across trusts and authenticating against domains that should be disallowed. (More information on the machine account quota and how to prevent low-privileged machine account creation can be found on [Kevin Robertson](https://twitter.com/kevin_robertson)’s excellent post “[MachineAccountQuota is USEFUL Sometimes](https://www.netspi.com/blog/technical/network-penetration-testing/machineaccountquota-is-useful-sometimes/)”.)

If nothing else, I hope this post informs systems administrators of the real forest-wide risk involved in implementing external trusts.

### Timeline

  * May 4, 2022: MSRC case created
  * May 12, 2022: Case status changed to “Review/Repro”
  * June 17, 2022: Case status changed to “Develop” with email that stated “We confirmed the behavior you reported. We’ll continue our investigation and determine how to address this issue.”
  * June 17, 2022: Case status changed to “Complete – Resolved”
  * August 24, 2022: Comment left on case to find out case status
  * September 2, 2022: Follow-up comment left on case to find out case status
  * September 14, 2022: Follow-up email sent to find out case status
  * September 29, 2022: Email received explaining that issue was not determined to affect security
  * March 7, 2023: Public disclosure

### Acknowledgements

  * [Will Schroeder](https://twitter.com/harmj0y) for the creation of Rubeus, without which this research might not have been possible
  * Everyone that reviewed this post and provided feedback, including: 
  * [Elad Shamir](https://twitter.com/elad_shamir)
  * Harjinder Nijjar
  * [Andrew Schwartz](https://twitter.com/4ndr3w6S)
  * [Jonny Johnson](https://twitter.com/jsecurity101)

### Learn more

Want more AD security research? Check out these articles.

  * [New Attack Paths? AS Requested Service Tickets](/blog/new-attack-paths-as-requested-sts/)
  * [A Diamond (Ticket) in the Ruff](/blog/a-diamond-ticket-in-the-ruff/)
  * [SyncJacking: Hard Matching Vulnerability Enables Azure AD Account Takeover](/blog/syncjacking-azure-ad-account-takeover/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### Sign Up for the Latest Semperis News
