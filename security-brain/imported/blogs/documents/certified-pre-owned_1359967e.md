---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-17_certified-pre-owned.md
original_filename: 2021-06-17_certified-pre-owned.md
title: Certified Pre-Owned
category: documents
detected_topics:
- idor
- access-control
- sso
- saml
- command-injection
- rate-limit
tags:
- imported
- documents
- idor
- access-control
- sso
- saml
- command-injection
- rate-limit
language: en
raw_sha256: 1359967e192cf36c049053cd54831f9e816d322166dc3e571e4903b7a89f4786
text_sha256: 94a7879964f1de8456061c84d5ae0c9184a7bd3cb713d1a6c72dfb3f655a74d1
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Certified Pre-Owned

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-17_certified-pre-owned.md
- Source Type: markdown
- Detected Topics: idor, access-control, sso, saml, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `1359967e192cf36c049053cd54831f9e816d322166dc3e571e4903b7a89f4786`
- Text SHA256: `94a7879964f1de8456061c84d5ae0c9184a7bd3cb713d1a6c72dfb3f655a74d1`


## Content

---
title: "Certified Pre-Owned"
page_title: "Certified Pre-Owned - SpecterOps"
url: "https://posts.specterops.io/certified-pre-owned-d95910965cd2"
final_url: "https://specterops.io/blog/2021/06/17/certified-pre-owned/"
authors: ["Will Schroeder (@harmj0y)", "Lee Christensen (@tifkin_)"]
programs: ["Microsoft"]
bugs: ["Active Directory Privilege Escalation", "ADCS", "Windows"]
publication_date: "2021-06-17"
added_date: "2022-11-17"
source: "pentester.land/writeups.json"
original_index: 3565
---

[ Back to Blog  ](/blog)

[Research & Tradecraft](https://specterops.io/blog/category/research/)

# Certified Pre-Owned

Author

[Will Schroeder](https://specterops.io/blog/author/will-schroeder/)

Read Time

28 mins

Published

Jun 17, 2021

##### Share

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fspecterops.io%2Fblog%2F2021%2F06%2F17%2Fcertified-pre-owned%2F&title=Certified+Pre-Owned&source=SpecterOps) [ ](https://twitter.com/share?url=https%3A%2F%2Fspecterops.io%2Fblog%2F2021%2F06%2F17%2Fcertified-pre-owned%2F&text=Certified+Pre-Owned) [ ](mailto:?Subject=I%20thought%20you'd%20like%20this%20post:%20Certified Pre-Owned&Body=https://specterops.io/blog/2021/06/17/certified-pre-owned/) [ ](https://specterops.io/blog/category/research/feed/)

**L;DR**  _Active Directory Certificate Services has a lot of attack potential! Check out our whitepaper “_[ _Certified Pre-Owned: Abusing Active Directory Certificate Services_](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf) _” for complete details. We’re also_[ _presenting this material at Black Hat USA 2021_](https://www.blackhat.com/us-21/briefings/schedule/#certified-pre-owned-abusing-active-directory-certificate-services-23168) _._

**[EDIT 06/22/21]** — We’ve updated some of the details for ESC1 and ESC2 in this post which will be shortly updated in the whitepaper.

For the past several months, we ([Will Schroeder](https://twitter.com/harmj0y) and [Lee Christensen](https://twitter.com/tifkin_)) have been diving into the security of [Active Directory Certificate Services](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831740\(v=ws.11\)) (AD CS). While several aspects of Active Directory have received thorough attention from a security perspective, Active Directory Certificate Services has been relatively overlooked. AD CS is Microsoft’s PKI implementation that provides everything from encrypting file systems, to digital signatures, to user authentication (a large focus of our research), and more. While AD CS is not installed by default for Active Directory environments, from our experience in enterprise environments it is widely deployed, and the security ramifications of misconfigured certificate service instances are enormous.![](https://miro.medium.com/max/1400/0*uf2o4Dwroh6Xb77l)

Today we’re releasing the results of our research so far (there is still much to look at, and we know we have missed things) in the form of an extensive whitepaper and a defensive PowerShell toolkit for auditing these issues. The toolkit is heavily defensive focused, but we will also release two offensive tools in ~45 days at [Black Hat](https://www.blackhat.com/us-21/briefings/schedule/#certified-pre-owned-abusing-active-directory-certificate-services-23168), as we believe that the issues described in the paper are severe and widespread enough to warrant a delay in the offensive tool release. The whitepaper also contains substantial preventative and detective guidance.

**Whitepaper** — “[ _Certified Pre-Owned: Abusing Active Directory Certificate Services_](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf) _”_

**Defensive Toolkit** — [PSPKIAudit](https://github.com/GhostPack/PSPKIAudit) (based on [PSPKI](https://github.com/PKISolutions/PSPKI))

**Offensive Toolkit** —(code will be pushed at [Black Hat](https://www.blackhat.com/us-21/briefings/schedule/#certified-pre-owned-abusing-active-directory-certificate-services-23168), preemptive IOCs/Yara rules are currently live) [Certify](https://github.com/GhostPack/Certify) and [ForgeCert](https://github.com/GhostPack/ForgeCert)

AD CS and its security implications are complicated, and we highly recommend reading the whitepaper for complete context. This post is a  _brief_ summary of the paper, and we will release a number of additional posts in the coming weeks and months to highlight elements of the research.

So why care about this? Certificate abuse can grant an attacker:

![](https://miro.medium.com/max/700/1*QXxrJdEIdwUEHzmBYPco-A.png)

Of note, nearly every environment with AD CS that we’ve examined for domain escalation misconfigurations has been vulnerable. It’s hard for us to overstate what a big deal these issues are.

**_Sidenote:_**_because of the number of attacks we ended up documenting in this research, we have tagged each attack with an ID (e.g., ESC2) as well as each defense (e.g., DETECT3). This is for ease of mapping of attacks to appropriate defenses in the whitepaper._

### Active Directory Certificate Services Crash Course

### Common Terms and Acronyms

There are a lot of terms and acronyms we’re going to be using throughout this post (and paper), so here’s a quick breakdown of a few for reference:

**PKI** (Public Key Infrastructure) — a system to manage certificates/public key encryption

**AD CS** (Active Directory Certificate Services) — Microsoft’s PKI implementation

**CA**(Certificate Authority) — PKI server that issues certificates

**Enterprise CA** — CA integrated with AD (as opposed to a standalone CA), offers certificate templates

**Certificate Template** — a collection of settings and policies that defines the contents of a certificate issued by an enterprise CA

**CSR** (Certificate Signing Request) — a message sent to a CA to request a signed certificate

**EKU** (Extended/Enhanced Key Usage) — one or more object identifiers (OIDs) that define how a certificate can be used

### Overview

AD CS is a server role that functions as Microsoft’s public key infrastructure PKI implementation. As expected, it integrates tightly with Active Directory and enables the issuing of certificates, which are X.509-formatted digitally signed electronic documents that can be used for encryption, message signing, and/or authentication (our research focus).

The information included in a certificate binds an identity (the subject) to a public/private key pair. An application can then use the key pair in operations as proof of the identity of the user. Certificate Authorities (CAs) are responsible for issuing certificates.

At a high level, clients generate a public-private key pair, and the public key is placed in a certificate signing request (CSR) message along with other details such as the subject of the certificate and the certificate template name. Clients then send the CSR to the Enterprise CA server. The CA server then checks if the client is allowed to request certificates. If so, it determines if it will issue a certificate by looking up the certificate template AD object (more on these shortly) specified in the CSR. The CA will check if the certificate template AD object’s permissions allow the authenticating account to obtain a certificate. If so, the CA generates a certificate using the “blueprint” settings defined by the certificate template (e.g., EKUs, cryptography settings, issuance requirements, etc.) and using the other information supplied in the CSR if allowed by the certificate’s template settings. The CA signs the certificate using its private key and then returns it to the client.

That’s a lot of text. So here’s a graphic:

![](https://miro.medium.com/max/700/0*hnpRmQCVuKwsSfR6)

### Certificate Templates

AD CS Enterprise CAs issue certificates with settings defined by AD objects known as certificate templates. These templates are collections of enrollment policies and predefined certificate settings and contain things like “ _How long is this certificate valid for?_ ”,  _“What is the certificate used for?”,_ “ _How is the subject specified?_ ”,  _“Who is allowed to request a certificate?”_ , and a myriad of other settings:

![](https://miro.medium.com/max/398/0*jFuo4SOGFmb-4rvn)

The  _pKIExtendedKeyUsage_ attribute on an AD certificate template object contains an array of object identifiers (OIDs) enabled for the template. These EKU object identifiers affect what the certificate can be used for (PKI Solutions has a breakdown of the [EKU OIDs available from Microsoft](https://www.pkisolutions.com/object-identifiers-oid-in-pki/)). Our research focused on EKUs that, when present in a certificate, permit authentication to Active Directory. We originally thought that only the “Client Authentication“ OID (1.3.6.1.5.5.7.3.2) enabled this; however, our research also found that the following OID scenarios can enable certificate-based authentication:

![](https://miro.medium.com/max/700/1*nwJTAixwc3CtiwtPVnlD4Q.png)

*_The 1.3.6.1.5.2.3.4 OID is not present in AD CS deployments by default and_[ _needs to be added manually_](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/additional-mitigations#deploying-domain-joined-device-certificates) _, but it does work for_[ _client authentication_](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-pkca/c83e95a4-ac5e-4519-b885-37a4d1b8d08b#:~:text=id-pkinit-kpclientauth) _._

Templates also have a number of other interesting settings which we explore in depth in the whitepaper. The paper also covers template “[Issuance Requirements](https://social.technet.microsoft.com/wiki/contents/articles/7421.active-directory-certificate-services-ad-cs-public-key-infrastructure-pki-design-guide.aspx#Issuance_requirements)” which can function as preventative controls, which we will briefly touch on in this post.

### Subject Alternative Names

A Subject Alternative Name (SAN) [is an extension](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.6) that allows additional identities to be bound to a certificate beyond just the subject of the certificate. For example, if a web server hosts content for multiple domains, each applicable domain could be included in the SAN so that the web server only needs a single HTTPS certificate instead of one for each domain.

This is all well and good for HTTPS certificates, but when combined with certificates that allow domain authentication, a dangerous scenario can arise. By default during certificate-based authentication, [certificates are mapped to Active Directory accounts](https://docs.microsoft.com/en-us/windows/security/identity-protection/smart-cards/smart-card-certificate-requirements-and-enumeration#client-certificate-mappings) based on a user principal name (UPN) specified in the SAN.  _So, if an attacker can specify an arbitrary SAN when requesting a certificate that enables domain authentication, and the CA creates and signs a certificate using the attacker-supplied SAN, the attacker can become any user in the domain!_ Domain escalation scenarios can result from various AD CS template misconfigurations that allow unprivileged users to supply an arbitrary SAN in a certificate enrollment. We’ll cover these situations in the **Domain Escalation** section.

### Active Directory Authentication with Certificates

Last year, [@_ethicalchaos_](https://twitter.com/_ethicalchaos_) made a PR to Rubeus to implement PKINIT abuse, and covers more details on this in depth in their post on [attacking smart card based Active Directory networks](https://ethicalchaos.dev/2020/10/04/attacking-smart-card-based-active-directory-networks/). This was a missing link for us offensively, and means that we can now use Rubeus to request a Kerberos ticket granting ticket (TGT) using a certificate enabled for domain authentication:

![](https://miro.medium.com/max/700/0*ljUy3-mcv1RGbASj)

That’s right,  _we don’t need a physical smart card or the Windows Credential Store to perform this certificate-based Kerberos authentication!_ Benjamin Delpy’s ([@gentilkiwi](https://twitter.com/gentilkiwi)) [Kekeo](https://github.com/gentilkiwi/kekeo) has supported this for years, but the Rubeus implementation made it more readily usable for our operations.

During our research, we also found that some protocols use Schannel — the security package backing SSL/TLS — to authenticate domain users. LDAPS is a commonly enabled use case. For example, the following screenshot shows the PowerShell script [Get-LdapCurrentUser](https://github.com/leechristensen/Random/blob/master/PowerShellScripts/Get-LdapCurrentUser.ps1) authenticating to LDAPS using a certificate for authentication and performing an [LDAP whoami](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/faf0b8c6-8c59-439f-ac62-dc4c078ed715) to see what account authenticated:

![](https://miro.medium.com/max/559/0*BuPV3ABZyAMnEPsw)

### Account Persistence

If an Enterprise CA exists, a user (or machine) can request a cert for any template available to them for enrollment. The whitepaper covers theft of existing certificates, but we’re only going to touch on “active” malicious enrollments here. Our goal, in the context of user credential theft, is to request a certificate for a template that allows us to authenticate to Active Directory as that user (or machine). For complete details, see the “Account Persistence” section in the whitepaper.

The **Certify.exe find /clientauth** command will query LDAP for available templates that we can examine for our desired criteria:

![](https://miro.medium.com/max/700/0*gUcE6gQPN3iimoi0)

This can also be done via PSPKIAudit with **Get-AuditCertificateTemplate | ?{$_.HasAuthenticationEku}**

![](https://miro.medium.com/max/700/0*cK5ojxZad1FOjUzB)

If we have GUI access to a host, we can manually request a certificate through  _certmgr.msc_. Alternatively, [Certify](https://github.com/GhostPack/Certify) (or **certreq.exe**) can be used be used for these malicious enrollments:

![](https://miro.medium.com/max/700/0*c8JGRkOFJ2x7jiTS)

These issued certificates can then be used with Rubeus to authenticate to Active Directory as this user, for as long as the certificate is valid. ** _This is an alternative method of long-term credential theft that doesn’t touch LSASS and can be performed from a non-elevated context!_**

![](https://miro.medium.com/max/500/0*PujOjPBnHtA9FFkf)

This also works for machine certificates, which can be combined with S4U2Self to obtain a Kerberos service ticket to any service on the host (e.g., CIFS, HTTP, RPCSS, etc.) as any user. Elad Shamir’s [excellent post about Kerberos delegation attacks](https://shenaniganslabs.io/2019/01/28/Wagging-the-Dog.html) details this attack scenario.

And since certificates are independent authentication material, ** _these certificates will still be usable even if the user (or computer) resets their password!_**

### Domain Escalation

While there isn’t anything  _necessarily_ inherently insecure about AD CS (except for ESC8 as detailed below), it is surprisingly easy to misconfigure its various elements, resulting in ways for unelevated users to escalate in the domain. We’ll briefly cover the main sets of misconfigurations, but again, see the whitepaper for complete details.

### Misconfigured Certificate Templates — ESC1

In order to abuse this misconfiguration, the following conditions must be met:

**The Enterprise CA grants low-privileged users enrollment rights.** The Enterprise CA’s configuration must permit low-privileged users the ability to request certificates. See the “ _Background — Certificate Enrollment_ ” in the whitepaper paper for more details.

**Manager approval is disabled.** This setting necessitates that a user with certificate manager permissions review and approve the requested certificate before the certificate is issued. See the “ _Background — Certificate Enrollment — Issuance Requirements_ ’ section in the whitepaper paper for more details.

**No authorized signatures are required.** This setting requires any CSR to be signed by an existing authorized certificate. See the “ _Background — Certificate Enrollment — Issuance Requirements_ ” section in the whitepaper for more details.

**An overly permissive certificate template security descriptor grants certificate enrollment rights to low-privileged users.** Having certificate enrollment rights allows a low-privileged attacker to request and obtain a certificate based on the template. Enrollment rights are granted via the certificate template AD object’s security descriptor.

**The certificate template defines EKUs that enable authentication**. Applicable EKUs include Client Authentication (OID 1.3.6.1.5.5.7.3.2), PKINIT Client Authentication (1.3.6.1.5.2.3.4), Smart Card Logon (OID 1.3.6.1.4.1.311.20.2.2), Any Purpose (OID 2.5.29.37.0), or no EKU (SubCA).

**The certificate template allows requesters to specify a subjectAltName (SAN) in the CSR**. If a requester can specify the SAN in a CSR, the requester can request a certificate as anyone (e.g., a domain admin user). The certificate template’s AD object specifies if the requester can specify the SAN in its  _mspki-certificate-name-flag_ property. The mspki-certificate-name-flag property is a bitmask and if the [CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-crtd/1192823c-d839-4bc3-9b6b-fa8c53507ae1) flag is present, a requester can specify the SAN. This is surfaced as the “Supply in request” option in the “Subject Name” tab in certtmpl.msc.

### Misconfigured Certificate Templates — ESC2

In order to abuse this misconfiguration, the following conditions must be met:

**The Enterprise CA grants low-privileged users enrollment rights.** Details are the same as in ESC1.**Manager approval is disabled.** Details are the same as in ESC1.

**No authorized signatures are required.** Details are the same as in ESC1.

**An overly permissive certificate template security descriptor grants certificate enrollment rights to low-privileged users.** Details are the same as in ESC1.

**The certificate template defines Any Purpose EKUs or no EKU**.

**[EDIT 06/22/21]**

While templates with these EKUs can’t be used to request authentication certificates as other users without the CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT flag being present (i.e., ESC1), an attacker can use them to authenticate to AD as the user who requested them and these two EKUs are certainly dangerous on their own.

We were initially a bit unclear about the capabilities of the**Any Purpose** and subordinate CA (**SubCA**) EKUs, but others reached out and helped us clarify our understanding. An attacker can use a certificate with the **Any Purpose** EKU for (surprise!) any purpose — client authentication, server authentication, code signing, etc. In contrast, an attacker can use a certificate with no EKUs — a subordinate CA certificate — for any purpose as well but could also use it to sign new certificates. As such, using a subordinate CA certificate, an attacker could specify arbitrary EKUs or fields in the new certificates.

HOWEVER, if the subordinate CA is not trusted by the NTAuthCertificates object (which it won’t be by default), the attacker cannot create new certificates that will work for domain authentication. Still, the attacker can create new certificates with any EKU and arbitrary certificate values, of which there’s plenty the attacker could potentially abuse (e.g., code signing, server authentication, etc.) and might have large implications for other applications in the network like SAML, AD FS, or IPSec.

We feel confident in stating that it’s very bad if an attacker can obtain an **Any Purpose** or subordinate CA (**SubCA**) certificate, regardless of whether it’s trusted by NTAuthCertificates or not.

**[/EDIT]**

### Enrollment Agent Templates — ESC3

In order to abuse this misconfiguration, the following conditions must be met:

**The Enterprise CA grants low-privileged users enrollment rights.** Details are the same as in ESC1.

**Manager approval is disabled.** Details are the same as in ESC1.

**No authorized signatures are required.** Details are the same as in ESC1.

**An overly permissive certificate template security descriptor grants certificate enrollment rights to low-privileged users.** Details are the same as in ESC1.

**The certificate template defines the Certificate Request Agent EKU**. The Certificate Request Agent OID (1.3.6.1.4.1.311.20.2.1) allows for requesting other certificate templates on behalf of other principals.

**Enrollment agent restrictions are not implemented on the CA.**

The Certificate Request Agent EKU (OID 1.3.6.1.4.1.311.20.2.1), known as “Enrollment Agent” in [Microsoft documentation](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-cersod/97f47d4c-2901-41fa-9616-96b94e1b5435), **allows a principal to enroll for a certificate on behalf of another user**. For anyone who enrolls in such a template, the resulting certificate can be used to co-sign requests on behalf of any user, for any Schema Version 1 template or any Schema Version 2+ template that requires the appropriate “Authorized Signatures/Application Policy” Issuance Requirement. This also assumes that there are no limiting [Enrollment Agent Restrictions](https://social.technet.microsoft.com/wiki/contents/articles/10942.ad-cs-security-guidance.aspx#Establish_Restricted_Enrollment_Agents) on the CA.

![](https://miro.medium.com/max/622/0*MZWeRBZPYXEOovt1)

The few sentences before this throwback meme might need a bit of clarification. If an attacker is able to enroll in a template with a “Certificate Request Agent” EKU, they can enroll  _on behalf of_ any user for any Version 1 certificate template, or any Version 2+ template configured to explicitly require this co-signing scenario. Schema Version 1 templates don’t implement this type of Issuance Requirement, so all are on the table. Specifically, the **User** and **Machine/Computer** templates are prime targets as they contain the Client Authentication EKU and are published by default (though this can be changed), and there are other Version 1 templates that can be vulnerable if published.

If a Version 1 template is duplicated for modification, it automatically becomes Schema Version 2 by default, meaning a “Certificate Request Agent” template will NOT work unless such an issuance requirement is explicitly specified.

A bit confusing? We know. We do our best to break this down in more depth in the whitepaper, but it’s a complex set of interwoven restrictions.

![](https://miro.medium.com/max/577/0*nMJV-TuHG4qBdtL4)

### Vulnerable Certificate Template Access Control — ESC4

Certificate templates are securable objects in Active Directory, meaning they have a security descriptor that specifies which Active Directory principals have specific permissions over the template. For more background on Active Directory ACLs, see [our (other) whitepaper on the subject](https://specterops.io/assets/resources/an_ace_up_the_sleeve.pdf).

We say that a template is misconfigured at the access control level if it has Access Control Entries (ACEs) that allow unintended, or otherwise unprivileged, Active Directory principals to edit sensitive security settings in the template. That is, if an attacker is able to chain access to a point that they can actively push a misconfiguration to a template that is not otherwise vulnerable (e.g., by enabling the CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT bit in the mspki-certificate-name-flag property for a template that allows for domain authentication), we end up with domain compromise scenarios similar to what we’ve already covered. An example of this we have seen in multiple environments is  _Domain Computers_ having FullControl or WriteDacl permissions over a certificate template’s AD object, allowing attackers with access to any AD computer modify the certificate template to a dangerous state. This is a scenario explored in [Christoph Falta’s GitHub repo](https://github.com/cfalta/PoshADCS).

### Vulnerable PKI Object Access Control — ESC5

We won’t touch on this one as heavily here, but a number of objects outside of certificate templates and the certificate authority itself can have a security impact on the entire AD CS system.

These possibilities include (but are not limited to):

CA server’s AD computer object (i.e., compromise through RBCD)

The CA server’s RPC/DCOM server

Any descendant AD object or container in the container **CN=Public Key Services,CN=Services,CN=Configuration,DC= <COMPANY>,DC=<COM>** (e.g., the Certificate Templates container, Certification Authorities container, the NTAuthCertificates object, the Enrollment Services container, etc.)

### EDITF_ATTRIBUTESUBJECTALTNAME2 — ESC6

Another way to supply arbitrary SANs, described in a [CQure Academy post](https://cqureacademy.com/blog/enhanced-key-usage), involves the EDITF_ATTRIBUTESUBJECTALTNAME2 flag. As Microsoft describes, “[ _If this flag is set on the CA, any request (including when the subject is built from Active Directory®) can have user defined values in the subject alternative name._](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn786426\(v=ws.11\)#controlling-user-added-subject-alternative-names)” This means that ANY template configured for domain authentication that also allows unprivileged users to enroll (e.g., the default**User** template) can be abused to obtain a certificate that allows us to authenticate as a domain admin (or any other active user/machine). As this [Keyfactor post describes](https://blog.keyfactor.com/hidden-dangers-certificate-subject-alternative-names-sans), this setting “just makes it work”, which is why it’s likely flipped in many environments by sysadmins who don’t fully understand the security implications.

Our normal reaction to seeing this setting in enterprise environments:

![](https://miro.medium.com/max/700/0*bypq3gWUk98SB8Vw)

### Vulnerable Certificate Authority Access Control — ESC7

Outside of certificate templates, a certificate authority itself [has permissions](https://social.technet.microsoft.com/wiki/contents/articles/10942.ad-cs-security-guidance.aspx#Roles_and_activities) (accessible through  _certsrv.msc_) that secure various CA actions. From a security perspective we care about the **ManageCA** (aka “CA Administrator”) and **ManageCertificates** (aka “Certificate Manager/Officer”) permissions.

The **ManageCA** permission grants a principal the ability to perform “Administrative” CA actions, including the modification of persistent configuration data. This includes the EDITF_ATTRIBUTESUBJECTALTNAME2 flag, allowing any principal with the **ManageCA** permission to fixate ESC6. This can be done with PSPKI’s [Enable-PolicyModuleFlag](https://www.sysadmins.lv/projects/pspki/enable-policymoduleflag.aspx) cmdlet.

The **ManageCertificates** permission allows the principal to approve pending certificate requests, negating the “Manager Approval” Issuance Requirement/protection. So while it can’t be used on its own to compromise the domain, it can function as a protection bypass.

### NTLM Relay to AD CS HTTP Endpoints — ESC8

We cover this in more detail in the  _“Background — Certificate Enrollment”_ section of the whitepaper, but AD CS supports several HTTP-based enrollment methods via additional server roles that administrators can optionally install:The certificate enrollment web interface, via installing the [ _Certificate Authority Web Enrollment_](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831649\(v=ws.11\)) role. Exposed as an IIS-hosted ASP web enrollment application running at  _http:// <ADCSSERVER>/certsrv/_Certificate enrollment service (CES), via installing the [ _Certificate Enrollment Web Service_](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831822\(v=ws.11\)) role. Works in tandem with the Certificate Enrollment Policy (CEP) web service, via installing the [ _Certificate Enrollment Policy Web Service_](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831625\(v=ws.11\)) role. Details in the whitepaper.The network device enrollment service (NDES), via installing the [ _Network Device Enrollment Service_](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831498\(v=ws.11\))role. Exposed as a series of interfaces described in the whitepaper.

These HTTP-based certificate enrollment interfaces are all vulnerable to NTLM relay attacks. Using NTLM relay, an attacker can impersonate an inbound-NTLM-authenticating victim user. While impersonating the victim user, an attacker could access these web interfaces and request a client authentication certificate based on the  _User_ or  _Machine_ certificate templates.

This attack, like all NTLM relay attacks, requires a victim account to authenticate to an attacker-controlled machine. An attacker can coerce authentication by many means, but a simple technique is to coerce a machine account to authenticate to the attacker’s host using the MS-RPRN  _RpcRemoteFindFirstPrinterChangeNotification(Ex)_ methods using a tool like [SpoolSample](https://github.com/leechristensen/SpoolSample/) or [Dementor](https://github.com/NotMedic/NetNTLMtoSilverTicket/blob/master/dementor.py). The attacker can then use NTLM relay to impersonate the machine account and request a client authentication certificate (e.g., the default **Machine/Computer** template) as the victim machine account. If the victim machine account can perform privileged actions such as domain replication (e.g., domain controllers or Exchange servers), the attacker could use this certificate to compromise the domain. Otherwise, the attacker could logon as the victim machine account and use S4U2Self as previously described to access the victim machine’s host OS.**Note:** Newer OS’es have patched the MS-RPRN coerced authentication “feature”. However, almost every environment we examine still has Server 2016 machines running, which are still vulnerable to this. There are other ways to coerce accounts to authenticate to an attacker as well.

In summary, if an environment has AD CS installed, along with a vulnerable web enrollment endpoint and at least one certificate template published that allows for domain computer enrollment and client authentication (like the default **Machine/Computer** template), ** _then an attacker can compromise ANY computer with the spooler service running!_**

![](https://miro.medium.com/max/577/0*KLuYWkOBoIK-ScF7)

These attack scenarios work because some enrollment HTTP endpoints do not have HTTPS enabled and none of them have any NTLM relay protections enabled by default. Organizations should disable these HTTP-based enrollment server roles if they are not in use. Otherwise, network defenders can disable NTLM authentication using GPOs or configuring the associated IIS applications to only accept Kerberos authentication. If organizations cannot remove the endpoints or outright disable NTLM authentication, they should only allow HTTPS traffic and configure the IIS applications to [Extended Protection for Authentication](https://msrc-blog.microsoft.com/2009/12/08/extended-protection-for-authentication/) .

This specific issue was reported to MSRC, along with the other template escalation misconfigurations. The official response was, “ _We determined your finding is valid but does not meet our bar for a security update release._ ”

**_Note:_**_While we have verified that this attack is possible, we are waiting to publicly demonstrate it at our_[ _Black Hat talk_](https://www.blackhat.com/us-21/briefings/schedule/#certified-pre-owned-abusing-active-directory-certificate-services-23168) _to help facilitate fixing the issue first._

### Domain Persistence

![](https://miro.medium.com/max/500/0*tTiLUQgMbNHXJCs9)

Active Directory Enterprise CAs are hooked into the authentication system of AD and the CA root certificate private key is used to sign newly issued certificates. If we stole this private key, would we be able to forge our own certificates that could be used (without a smart card) to authenticate to Active Directory as anyone in the organization?

Spoiler: yes. And this has already been [possible with Mimikatz/Kekeo for years](https://twitter.com/gentilkiwi/status/1117124090631008256). I guess we should call these golden certificates?

The certificate exists on the CA server itself, with its private key protected by machine DPAPI if a TPM/HSM is not used for hardware-based protection. If the key is not hardware protected, Mimikatz and SharpDPAPI can extract the CA certificate and private key from the CA:

![](https://miro.medium.com/max/700/0*Q_lHrLLkYOf7T5NH)

With this key, you can create and sign new certificates for ANY user and use these forged certificates to authenticate to AD for as long as the CA cert is valid (default of 5 years, but often longer). Our tool [ForgeCert](https://github.com/GhostPack/ForgeCert) (which will be released at Black Hat USA 2021 along with [Certify](https://github.com/GhostPack/Certify)) can perform these forgeries:

![](https://miro.medium.com/max/700/0*JqzrIURJ0KumD7bu)

Oh, and these certs ** _can’t be revoked,_** since they were never actually issued by the CA itself, as detailed by Benjamin Delpy:

![](https://miro.medium.com/max/585/0*Yfr7USs3uZkPUMb1)

Unfortunately, there isn’t a huge amount of public incident response guidance as far as AD CS. But if a root CA’s key is stolen, the entire AD CS system will likely need to be rebuilt, invalidating every issued certificate.

### Defensive Advice

Not only are we self-embargoing the offensive tool release for these abuses, but we’ve also spent a large amount of effort researching both preventative and detective controls for these attacks. Part of the motivation for breaking out attacks and associated defensive protections with individual identifiers was to make the whitepaper material as digestible as possible for defenders.

Besides identifying and mitigating the privilege escalation vulnerabilities, something we want to emphasize from an incident response perspective is that it is not enough to reset a compromised user’s password and/or reimage their machine. Certificate theft is trivial in most environments given code execution in a user or computer context and would allow an attacker to authenticate to AD for years — even after the account’s password has been reset. Therefore, when an account or machine is compromised, incident responders should identify and invalidate any certificates associated with the compromised accounts as well. [PSPKIAudit’s](https://github.com/GhostPack/PSPKIAudit) **Get-CertRequest** can help perform this type of triage.

As the defenses for these attacks are multi-pronged, at this point we’re recommending defenders study the attacks, read the extensive “Defensive Guidance” section of the whitepaper, and reference Microsoft’s [Securing PKI](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn786443\(v=ws.11\)) documentation. Defenders can also try out the [PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)’s **Invoke-PKIAudit** function the misconfigurations described in this post:

![](https://miro.medium.com/max/700/0*pC5NZspDjcIVTuLX)

### Wrap-up

Even months into this research, we believed that there wasn’t necessarily anything  _inherently_ insecure about Active Directory Certificate Services. While the entire system is very dangerous if an organization doesn’t fully understand AD CS or its security implications (as it’s extremely easy to misconfigure) there didn’t appear to be any “out of the box” vulnerabilities. That said, we have seen a proliferation of the ESC1–7 elevation issues in real environments since we began looking in January 2021. We feel administrators have been given a powerful weapon with the safety off for 20 years and there’s been little safety training. An attitude of, “ _Well, admins should have known better_ ” in this scenario, without even providing a way to audit or investigate these issues programmatically from a defensive context, is, well, a position we suppose.

However, beyond the template misconfiguration scenarios, the ESC8 relay situation is a ** _serious_** security issue. We reported this relay issue to MSRC on May 19th along with all domain escalation scenarios, and received a response on June 8th of “ _We determined your finding is valid but does not meet our bar for a security update release. We considered that servers with AD CS roles could mitigate this risk with a change in configuration settings to enable Extended Protection for Authentication (EPA), per this_[ _blog_](https://msrc-blog.microsoft.com/2009/12/08/extended-protection-for-authentication/) _post._ ” MSRC stated that they also opened up a bug concerning the template issues and our comments about poor telemetry with the AD CS feature team, who may consider additional design changes in a future release.

To be clear, based on our research, if you are running AD CS with ANY template a domain computer can enroll in that also allows domain authentication (e.g., the **Machine** /**Computer** template that is available by default), ANY system running the spooler service can be compromised. Based on our extensive experience assessing AD environments, we believe this is very bad. If you find you are vulnerable to this, consider contacting your nearest Microsoft representative and question them as to why this insecure default configuration is allowed. As of right now, they have no intentions of directly servicing the issue, but said they may fix it at some indeterminate future date.

From a defensive perspective, you should either  _immediately_ enumerate the Web Enrollment interfaces enabled in your environment (possible with PSPKIAudit) and then either remove them, disable NTLM authentication to them, or enforce HTTPS to them and [enable EPA on the IIS server component](https://msrc-blog.microsoft.com/2009/12/08/extended-protection-for-authentication/). For specifics on how to do this, please see “Defensive Guidance — Harden AD CS HTTP Endpoints — PREVENT8” in the whitepaper. We also strongly recommend organizations audit their AD CS architecture and certificate templates and ** _treat CA servers (including subordinate CAs) as Tier 0 assets with the same protections as Domain Controllers!_** The “Defensive Guidance”section of the whitepaper has more information on how to proactively prevent, detect, and respond to the attacks we’ve detailed.

Yes, we’re working to integrate the escalation paths into BloodHound, but as you can see this whole thing is rather complicated, and we want to get it right. But rest assured, it’s currently under development at the moment and will be released in FOSS BloodHound.

And finally, as a disclaimer, we are not stating that we know every security issue concerning AD CS. We took our best shot in this research, but we are confident that there are additional issues and attacker tradecraft implications that we (or others) will find in the coming months, or things we have missed.

### Acknowledgements

As is almost always the case, we’re standing on a number of shoulders with this research. The whitepaper gives a more complete treatment of prior work, but as a summary:

[Benjamin Delpy](https://twitter.com/gentilkiwi/) for his [extensive work](https://github.com/gentilkiwi/mimikatz/wiki/howto-~-decrypt-EFS-files) on smart cards/certificates with [Mimikatz and Kekeo](https://github.com/comaeio/OPCDE/tree/master/2017/From%20mimikatz%20to%20kekeo%2C%20passing%20by%20new%20Microsoft%20security%20technologies%20-%20Benjamin%20Delpy).

PKI Solutions for their [excellent posts on PKI in Active Directory](https://www.pkisolutions.com/thepkiblog/), as well as their [PSPKI PowerShell module](https://github.com/PKISolutions/PSPKI), which our auditing toolkit is based on.

The “[ _Windows Server 2008 — PKI and Certificate Security_](https://www.microsoftpressstore.com/store/windows-server-2008-pki-and-certificate-security-9780735640788)” book by Brian Komar.

The following open technical specifications provided by Microsoft:

[[MS-CERSOD]: Certificate Services Protocols Overview](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-cersod/ec4bb597-9e73-4d2b-a768-621239e21fca)

[[MS-CRTD]: Certificate Templates Structure](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-crtd/4c6950e4-1dc2-4ae3-98c3-b8919bb73822)

[[MS-CSRA]: Certificate Services Remote Administration Protocol](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-csra/40e74714-14bf-4f97-a264-35efbd63a813)

[[MS-ICPR]: ICertPassage Remote Protocol](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-icpr/9b8ed605-6b00-41d1-9a2a-9897e40678fc)

[[MS-WCCE]: Windows Client Certificate Enrollment Protocol](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-wcce/446a0fca-7f27-4436-965d-191635518466)

[Christoph Falta’s GitHub repo](https://github.com/cfalta/PoshADCS) which covers some details on attacking certificate templates, including virtual smart cards as well as some ideas on ACL based abuses.

CQURE’s “[ _The tale of Enhanced Key (mis)Usage_](https://cqureacademy.com/blog/enhanced-key-usage)” post which covers some Subject Alternative Name abuses.

Keyfactor’s 2016 post “[ _Hidden Dangers: Certificate Subject Alternative Names (SANs)_](https://blog.keyfactor.com/hidden-dangers-certificate-subject-alternative-names-sans)”

[@Elkement](https://twitter.com/elkement)’s posts  _“_[ _Sizzle @ hackthebox — Unintended: Getting a Logon Smartcard for the Domain Admin!_](https://elkement.blog/2019/06/01/sizzle-hackthebox-unintended-getting-a-logon-smartcard-for-the-domain-admin-2/)_”_ and  _“_[ _Impersonating a Windows Enterprise Admin with a Certificate: Kerberos PKINIT from Linux_](https://elkement.wordpress.com/2020/06/21/impersonating-a-windows-enterprise-admin-with-a-certificate-kerberos-pkinit-from-linux/)” detail certificate template misconfigurations.

Carl Sörqvist wrote up a detailed, and plausible, scenario for how some of these misconfigurations happen titled “[ _Supply in the Request Shenanigans_](https://blog.qdsecurity.se/2020/09/04/supply-in-the-request-shenanigans/)”.

[Ceri Coburn](https://twitter.com/_ethicalchaos_) released an excellent post in 2020 on “[ _Attacking Smart Card Based Active Directory Networks_](https://ethicalchaos.dev/2020/10/04/attacking-smart-card-based-active-directory-networks/)” detailing some smart card abuse and Rubeus additions.

Brad Hill published a whitepaper titled “[ _Weaknesses and Best Practices of Public Key Kerberos with Smart Cards_](https://research.nccgroup.com/wp-content/uploads/2020/07/weaknesses_and_best_practices_of_public_key_kerberos_with_smart_cards.pdf) which provided some good background on Kerberos/PKINIT from a security perspective.

Special thanks to [Mark Gamache](https://twitter.com/markgamacheNerd) for collaborating with us on parts of this work. He independently discovered many of these abuses, reached out to us, and brought many additional details to our attention while we were performing this research.

As always, we tried our best to cite the existing work out there that we came across, but we’re sure we missed things.

**Whitepaper** — “[ _Certified Pre-Owned: Abusing Active Directory Certificate Services_](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf) _”_

**Defensive Toolkit** — [PSPKIAudit](https://github.com/GhostPack/PSPKIAudit) (based on [PSPKI](https://github.com/PKISolutions/PSPKI))

**Offensive Toolkit** —(code will be pushed at [Black Hat](https://www.blackhat.com/us-21/briefings/schedule/#certified-pre-owned-abusing-active-directory-certificate-services-23168), preemptive IOCs/Yara rules are currently live) [Certify](https://github.com/GhostPack/Certify) and [ForgeCert](https://github.com/GhostPack/ForgeCert)

Post Views: 36,859

[ Will Schroeder ](https://specterops.io/blog/author/will-schroeder/)

Principal Security Researcher 

Will Schroeder (@harmj0y) is a Principal Security Researcher at SpecterOps specializing in machine learning and offensive development. He has co-authored numerous projects ranging from BloodHound to the “Certified Pre-Owned” white paper.
