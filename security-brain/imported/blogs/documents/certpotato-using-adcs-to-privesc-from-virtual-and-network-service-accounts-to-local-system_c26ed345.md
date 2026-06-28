---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-02_certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-lo.md
original_filename: 2022-12-02_certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-lo.md
title: CertPotato – Using ADCS to privesc from virtual and network service accounts
  to local system
category: documents
detected_topics:
- sso
- access-control
- ssrf
- command-injection
- mfa
- automation-abuse
tags:
- imported
- documents
- sso
- access-control
- ssrf
- command-injection
- mfa
- automation-abuse
language: en
raw_sha256: c26ed345895e4e10d0d4bddd5a1fc144083aa4db3a22916446507b5b633f25f8
text_sha256: 379fdc67fc34bdb173961ddf2c27918fc65331bf5d383424bce6d4ef74a104c6
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# CertPotato – Using ADCS to privesc from virtual and network service accounts to local system

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-02_certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-lo.md
- Source Type: markdown
- Detected Topics: sso, access-control, ssrf, command-injection, mfa, automation-abuse
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `c26ed345895e4e10d0d4bddd5a1fc144083aa4db3a22916446507b5b633f25f8`
- Text SHA256: `379fdc67fc34bdb173961ddf2c27918fc65331bf5d383424bce6d4ef74a104c6`


## Content

---
title: "CertPotato – Using ADCS to privesc from virtual and network service accounts to local system"
page_title: "SensePost | CertPotato – Using ADCS to privesc from virtual and network service accounts to local system"
url: "https://sensepost.com/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/"
final_url: "https://sensepost.com/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/"
authors: ["Hocine Mahtout (@Sant0rryu)"]
programs: ["Microsoft"]
bugs: ["Local Privilege Escalation", "ADCS"]
publication_date: "2022-12-02"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 1826
---

The goal of this blog post is to present a privilege escalation I found while working on ADCS. We will see how it is possible to elevate our privileges to NT AUTHORITY\SYSTEM from virtual and network service accounts of a domain-joined machine (for example from a webshell on a Windows server) using ADCS. I want to call this attack chain “CertPotato” as homage to other *Potato tools and as a way to better remember it.

A popular technique for getting SYSTEM from a virtual or network service account is [Delegate 2 Thyself](https://exploit.ph/delegate-2-thyself.html) by Charlie Clark. This technique involves using RBCD to elevate your privileges. In this article, I propose an alternative approach to become local SYSTEM using ADCS.

## ADCS 101

### Public Key Infrastructure

A PKI (Public Key Infrastructure) is an infrastructure used to create, manage, and revoke certificates as well as public/private keys.

Active Directory Certificate Service (ADCS) is the Microsoft implementation of PKI infrastructure in an Active Directory/Windows environment. This service was added in Windows Server 2000, is easy to install and fully integrates itself with different Microsoft services. For example, here is a non exhaustive list of the different usages of PKI infrastructure:

  * TLS certificates (HTTPS / LDAPS / RDP)
  * Signing binaries, PowerShell scripts or even drivers
  * User authentication
  * File system encryption

### Certificate templates

To simplify the creation of certificates in Active Directory, there are certificate templates.

These templates are used to specify specific parameters and rights related to the certificate that will be issued from them. For example, in a certificate template we can set the following parameters:

  * Period of validity
  * Who has the right to enroll
  * How we can use these certificates also called Extended Key Usage (EKU)

By default, when the ADCS role is installed, different default templates are provided. One of them is the **Machine** template which can be requested by any machine account that is a member of the Domain Computers domain group:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/7b8085317776524c7baf28e4ad6f3b28.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/7b8085317776524c7baf28e4ad6f3b28.png)Example of a template

### Request a certificate

A certificate request is always sent to the ADCS server. It is based on a template and requires authentication.

If the request is approved by the certification authority, then the certificate is delivered and usable in line with the EKUs defined in the template.

### User authentification (PKINIT)

Kerberos supports asymmetric authentication, that is PKINIT authentication. Instead of encrypting the timestamp during pre-authentication (KRB_AS_REQ) with a password derivative (NT hash for RC4 encryption), it is possible to sign the timestamp with the private key associated with a valid certificate.

However, for PKINIT authentication to be feasible there are several conditions, one of these conditions is that the obtained certificate must have one of the following 5 EKUs:

  * Client Authentification
  * PKINIT Client Authentification
  * Smart Card Logon
  * Any Purpose
  * SubCA

## The situation

In our test environment, we have three machines:

  * DC (192.168.1.1): the domain controller (Windows server 2022 fully updated) on which the certificate authority is also located;
  * IIS (192.168.1.2): an application server (Windows server 2022 fully updated) on which the IIS service is installed;
  * A Kali Linux machine (192.168.1.3).

_Note: There are many methods to bypass antivirus software, however this is not the subject of this article, so we have disabled it in this environment._

Let’s assume that we have successfully uploaded a web shell on the IIS server. If we run the whoami command we can see the following result:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/cbc6d511fff3c5e65c942269ca6582f5.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/cbc6d511fff3c5e65c942269ca6582f5.png)whoami from our webshell

By default the service account used is `_**iis apppool\defaultaappool**_` a Microsoft virtual account. But what is a service account?

### Service accounts

According to Microsoft: “[A service account is a user account that’s created explicitly to provide a security context for services that are running on Windows Server operating systems](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn617203\(v=ws.11\))“. On a Windows machine, there are several built-in service accounts:

  * LocalSystem (NT AUTHORITY\SYSTEM);
  * NetworkService (NT AUTHORITY\Network Service);
  * LocalService (NT AUTHORITY\Local Service).

These three accounts have different privileges on the machine. Only the LocalSystem account and the NetworkService account use the computer account, if they need to authenticate to other machines on the internal network.

Services can also be run using alternate accounts like local or domain accounts.

Moreover, since Windows Server 2008 R2, new services accounts were introduced:

  * Standalone managed service accounts (sMSA);
  * Group-managed service accounts (gMSA);
  * Virtual accounts.

These accounts make management services easier for administrators. For example, password management (complexity, renewal, so on) is fully handled by Active Directory.

Standalone and Group managed service accounts are both domain accounts, so if they need to authenticate to other machines on the network they use their domain credentials. Virtual accounts are defined as local managed service accounts, in a domain context environment if network authentication is needed the computer account will also be used.

Examples of services which use virtual accounts to run their applications: IIS, Exchange, MSSQL.

Depending on the installed services there can be more virtual accounts. The **iis apppool\defaultapppool** account is one of them.

### Back to the topic

If we try to enumerate a remote share from our webshell:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/6d6fc5124a76bf1e23b858c433ab5742.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/6d6fc5124a76bf1e23b858c433ab5742.png)Enumerate a remote share from our webshell

We will see that it is not the **defaultapppool** account that will try to authenticate to our server but the **IIS$** machine account:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/f7967e1ac9f3cecd23b80c04d3c62b49.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/f7967e1ac9f3cecd23b80c04d3c62b49.png)The machine account is used

That implies that when requesting remote information, the operating system falls back to the machine account of the computer (**IIS$**) to perform the authentication which is a valid account on the Active Directory. Furthering this principle we can try to list Active Directory information using for example the net binary, and we will be able to retrieve the list of the domain users:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/df2f675e5a6241575eea5427ac1ae883.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/df2f675e5a6241575eea5427ac1ae883.png)Listing domain users from our webshell

Since we are able to request domain information, we can also retrieve Certificate Authority information:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/b721acc8721dca0f2d79b33473c353b8.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/b721acc8721dca0f2d79b33473c353b8.png)Retrieve CA information

As well as information on a specific template (in this case the default Machine template):

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/4cae64d055e6d51810de837e1802fab7.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/4cae64d055e6d51810de837e1802fab7.png)Retrieve template information

We could relay the machine authentication to the web enrollment service ([ESC8](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)), however we assume here that either the service is not present or that anti-relay measures have been put in place (EPA for example).

## Abusing this situation

So, our IIS service runs as a virtual account, therefore for domain operations we act as the underlying machine account. Our goal is to target ADCS and request a certificate, but to do that we need the password of the machine account (which requires a privessc to begin with), or a usable TGT of it. That’s where TGTdeleg comes into play.

### Get a usable TGT

As Charlie Clark mentions in his [post](https://exploit.ph/delegate-2-thyself.html), Benjamin Delpy found a way to get a usable TGT . This technique is called the [tgtdeleg trick](https://twitter.com/gentilkiwi/status/998219775485661184) and it’s also been implemented in [Rubeus](https://github.com/GhostPack/Rubeus#tgtdeleg).

#### What is the TGT delegation trick ?

Any account with an SPN record (machine or otherwise) that is granted unconstrained delegation rights is able to impersonate a user to authenticate to any service on any host. Indeed, when a user wants to access a service or a server with this right, the **AP_REQ** contains the Authenticator which is encrypted with the session key sent back with the first `TGS-REP` along with the Service Ticket.Among the elements contained in the authenticator, we will find a delegation TGT with the key associated to the user who wants to access the service with unconstrained delegation.

So if we manage to retrieve the **AP_REQ** packet and the key used to encrypt the authenticator, we will be able recover the delegation TGT of our user and its associated session key.

Using the functions of the SSPI/GSS-API, in particular the InitializeSecurityContext() function and providing the targeted SPN, we will obtain a structure (an SSPI SecBuffer structure) that will allow us to recover the **AP_REQ**. For the session key used to encrypt the authenticator, it can be retrieved from the [local Kerberos cache](https://github.com/GhostPack/Rubeus/blob/4c9145752395d48a73faf326c4ae57d2c565be7f/Rubeus/lib/LSA.cs#L1222).

So here’s the trick, with our user context, we call the InitializeSecurityContext() function with an SPN of a service or a machine having the unconstrained delegation rights as parameter. By default, domain controllers have this right, so we can choose the SPN `cifs/<dc_fqdn>`. We then extract the **AP_REQ** packet from the SSPI structure. Finally, with the session key retrieved from the local Kerberos cache we can then decrypt the authenticator and retrieve the delegation TGT of our current user and its associated session key.

#### Back to the topic

So we upload Rubeus on the compromised machine, then to obtain a delegation TGT we launch the following command `Rubeus.exe tgtdeleg /nowrap`:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/7769c1a6a40165f1ca7b790db3742c64.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/7769c1a6a40165f1ca7b790db3742c64.png)TGT delegation trick from our webshell

We obtain a valid TGT in base64. We can now use our Kali machine to request a certificate using **certipy**. To do this, we must first convert the base64 encoded kirbi file into a ccache file:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/9383b45a9eec8b14c630a5e65a933722.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/9383b45a9eec8b14c630a5e65a933722.png)Convert base64 kirbi file to ccache file

Once the TGT file is in the right format, you can load it with the command `export KRB5CCNAME_=<path_to_ticket.ccache>` . The **klist** command allows us to list the loaded Kerberos tickets, where we can see that we have obtained a TGT as **IIS$** , the machine account.

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/e241403158850d5a7c221078e6870a13.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/e241403158850d5a7c221078e6870a13.png)Import machine account TGT

### Request a machine certificate

Certipy can take TGT tickets loaded with the -k option as parameter. We can use the TGT of our machine account to list the certificate templates:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/88ea9156df2ace6922cf84eaa3e43080.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/88ea9156df2ace6922cf84eaa3e43080.png)Enumerate CA with our TGT

With our Kerberos ticket, we can then directly request a certificate with the default template **Machine**. Any certificate template with the EKU Client Authentication that our machine account can enroll on could have worked too:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/2aaa936cc017fc3bb8cbed7c20da8f67.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/2aaa936cc017fc3bb8cbed7c20da8f67.png)Request a Machine certifcate

As detailed in the article [NTLM relaying to AD CS – On certificates, printers and a little hippo](https://dirkjanm.io/ntlm-relaying-to-ad-certificate-services/) from [Dirk-jan Mollema](https://twitter.com/_dirkjan), with PKINIT authentication and the U2U extension, we can then obtain the hash of the machine account:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/48b08b1091b85404b512117a91f73e6a.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/48b08b1091b85404b512117a91f73e6a.png)PKINT authentification 

We can then confirm that the account hash is valid by using crackmapexec:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/39cb6facdb74e777e11bb25f14db0992.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/9402c5d4447cdb9c5902e7daa58b54a8.png)Confirm our hash is valid

So we managed to get the machine account of a domain-joined machine from a local service account. With the domain-joined machine account, you can then become an administrator on the compromised machine or search for vulnerabilities in the Active Directory.

An alternative way to upgrade our machine account TGT to a NT hash is to use the [Shadow Credentials](https://posts.specterops.io/shadow-credentials-abusing-key-trust-account-mapping-for-takeover-8ee1a53566ab) technique. Indeed the machine account has the possibility to modify its properties (especially the attribute **msDS-KeyCredentialLink**).

### From machine account to SYSTEM

To become SYSTEM with the machine account, we will forge a Silver ticket on the CIFS service. To do this we need the domain SID, an arbitrary username (let’s choose Cellmax), the full domain name and NT hash of the machine account.

  * The domain SID can be obtained anonymously by running **rpcclient** on the domain controller:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/3dc2801c1edbf7411d56a2ecf90dec71.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/3dc2801c1edbf7411d56a2ecf90dec71.png)Retrieve domain SID

  * The full domain name can be obtained with crackmapexec:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/2c24ac036c7e3e6d7eebc6d84a3e3501.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/2c24ac036c7e3e6d7eebc6d84a3e3501.png)Retrieve full domain name

Once we have these elements, we can create our silver ticket using **impacket-ticketer** :

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/1d4a52e6df6e5ed32d6361e57f423d48.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/1d4a52e6df6e5ed32d6361e57f423d48.png)Load the silver ticket

Let’s load our Kerberos ticket using the export command:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/fbbf9670ba8784ab5f543f94ae3a87ee.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/fbbf9670ba8784ab5f543f94ae3a87ee.png)Load silver ticket

We can now use the psexec script from the impacket toolkit with the -k and -no-pass parameters to authenticate to the service using our silver ticket. We are now **SYSTEM** on the server:

[![](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/2a34f73bd33190fd8f676348aa6a2494.png)](/img/pages/blog/2022/certpotato-using-adcs-to-privesc-from-virtual-and-network-service-accounts-to-local-system/2a34f73bd33190fd8f676348aa6a2494.png)Become SYSTEM

## Conclusion

ADCS brings a new way to take control of a machine from a service account. From a simple shell as NetworkService or aVirtual Account, we can take complete control of the machine.

Several Windows events are generated when using this technique. During the use of the TGT delegation trick or PKINIT authentication, Kerberos logs are generated (event 4768) on the domain controller, and when interacting with the certification authority (CA), logs are generated on the server where the ADCS role is installed (events 4886, 4887). However, monitoring all these Windows events could be quite complicated as they correspond to normal activity in an Active Directory network.

Firstly, the vulnerability allowing initial access on the server as virtual or network services accounts must be fixed. Then for sensitive servers, gMSA and sMSA accounts can be a solution. As a reminder, Standalone and Group managed services accounts are both domain accounts, so if they need to authenticate to other machines on the network they use their domain credentials.

However it is necessary to ensure that the permissions on the Active Directory of these accounts are sufficiently restrictive. Thus, if one of these managed services accounts is compromised, an attacker will not be able pivot easily on the internal network.

## Acknowledgements

  * [Olivier Lyak](https://twitter.com/ly4k_) for the [Certipy](https://github.com/ly4k/Certipy) tool and the [associated articles](https://medium.com/@oliverlyak)
  * [Will Schroeder](https://twitter.com/harmj0y) and [Lee Christensen](https://twitter.com/tifkin_) for the [Certify](https://github.com/GhostPack/Certify) tool and the [Certified Pre-Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf) article
  * [Dirk-jan](https://twitter.com/_dirkjan) for the [PKINITtools](https://github.com/dirkjanm/PKINITtools).
  * [Benjamin Delpy](https://twitter.com/gentilkiwi) for implementing [delegation TGT on mimikatz](https://twitter.com/gentilkiwi/status/998219775485661184)
  * [Charlie Clark](https://exploit.ph/delegate-2-thyself.html) for the inspiring article [Delegate 2 Thyself](https://exploit.ph/delegate-2-thyself.html)
  * [Elad Shamir](https://twitter.com/elad_shamir) for the article [Wagging the Dog: Abusing Resource-Based Constrained Delegation to Attack Active Directory](https://shenaniganslabs.io/2019/01/28/Wagging-the-Dog.html)and for the article [Shadow Credentials: Abusing Key Trust Account Mapping for Account Takeover](https://posts.specterops.io/shadow-credentials-abusing-key-trust-account-mapping-for-takeover-8ee1a53566ab).
  * [Charlie Bromberg](https://twitter.com/_nwodtuhs/) for his [talk](https://youtu.be/7_iv_eaAFyQ) at the French conference LeHack 2022.
  * [Will Schroeder](https://twitter.com/harmj0y) again for his [article](https://posts.specterops.io/rubeus-now-with-more-kekeo-6f57d91079b9) explaining the TGT delegation trick.
