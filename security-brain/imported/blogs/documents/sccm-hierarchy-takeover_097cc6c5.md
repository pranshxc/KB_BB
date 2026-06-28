---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-26_sccm-hierarchy-takeover.md
original_filename: 2023-09-26_sccm-hierarchy-takeover.md
title: SCCM Hierarchy Takeover
category: documents
detected_topics:
- access-control
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- mfa
- api-security
language: en
raw_sha256: 097cc6c58db6f81467642eeec1dfc40086c8a8980a6bb86c8f9dae8fe8e8d558
text_sha256: 7b765b5c948fff269ddafa4cccfedeabca7004cae34f5b1aad24688f3c21d486
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# SCCM Hierarchy Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-26_sccm-hierarchy-takeover.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `097cc6c58db6f81467642eeec1dfc40086c8a8980a6bb86c8f9dae8fe8e8d558`
- Text SHA256: `7b765b5c948fff269ddafa4cccfedeabca7004cae34f5b1aad24688f3c21d486`


## Content

---
title: "SCCM Hierarchy Takeover"
page_title: "SCCM Hierarchy Takeover - SpecterOps"
url: "https://posts.specterops.io/sccm-hierarchy-takeover-41929c61e087"
final_url: "https://specterops.io/blog/2023/09/25/sccm-hierarchy-takeover/"
authors: ["Chris Thompson (@_Mayyhem)"]
bugs: ["SCCM site takeover"]
publication_date: "2023-09-26"
added_date: "2023-09-27"
source: "pentester.land/writeups.json"
original_index: 743
---

[ Back to Blog  ](/blog)

[Research & Tradecraft](https://specterops.io/blog/category/research/)

# SCCM Hierarchy Takeover

Author

[Chris Thompson](https://specterops.io/blog/author/christhompson/)

Read Time

13 mins

Published

Sep 25, 2023

##### Share

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F09%2F25%2Fsccm-hierarchy-takeover%2F&title=SCCM+Hierarchy+Takeover&source=SpecterOps) [ ](https://twitter.com/share?url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F09%2F25%2Fsccm-hierarchy-takeover%2F&text=SCCM+Hierarchy+Takeover) [ ](mailto:?Subject=I%20thought%20you'd%20like%20this%20post:%20SCCM Hierarchy Takeover&Body=https://specterops.io/blog/2023/09/25/sccm-hierarchy-takeover/) [ ](https://specterops.io/blog/category/research/feed/)

**One Site to Rule Them All**

### tl;dr:

**There is no security boundary between sites in the same hierarchy**.

When an administrative user is granted a security role in SCCM, such as Full Administrator or Infrastructure Administrator, in any primary site, the underlying database changes propagate upward to the central administration site (CAS) and then to other primary sites in the hierarchy.

This means that **if an attacker gains control of any primary site, they gain control of the entire SCCM hierarchy**.

![](https://specterops.io/wp-content/uploads/sites/3/2023/09/1Sq4hhh11fU4XQEoDtAZS6A.png)

Skip ahead to Mitigation or Detection!

### I Have the Best Words

First, there are a few SCCM-specific terms we need to be familiar with to better understand the problem. Feel free to skip ahead if you already know your site systems from your site servers.

  * **SCCM** : A client-server solution commonly used to deploy software and updates to Windows systems, currently named Microsoft Configuration Manager (ConfigMgr, Config Man, or MCM), but [formerly](https://craigtwall.com/how-sccm-became-memcm-or-just-configmgr/):  
– Microsoft Endpoint Configuration Manager (MECM)  
– Microsoft Endpoint Manager Configuration Manager (MEMCM)  
– System Center Configuration Manager (SCCM)  
– Systems Management Server (SMS)  
I’ll stop calling it SCCM when they change the name of [the subreddit](https://www.reddit.com/r/SCCM/). It’s easier than trying to keep up with Microsoft’s branding.
  * **Hierarchy** : all of the sites in one instance of SCCM
  * **Site** : an environment that provides services to a scope of clients (primary and secondary sites) and/or admins (central administration site and primary sites), represented by a three-character site code
  * **Site system role** : a role installed on a site system to host functionality for a site (e.g., site server, site database, distribution point)
  * **Site system** : a server that hosts a site system role (also unfortunately referred to as site system servers, but we will just call them site systems to avoid confusion with site servers)
  * **Site server** : the required site system where the site is installed that handles data processing and interacts with the site database
  * **Client** : a device where the SCCM client software is installed that is joined to a primary site
  * **Primary site** : the only type of site that client devices can be assigned to
  * **Primary site server** : the system that handles processing of all client data in a primary site, also referred to as just the “site server”
  * **Central administration site** : an optional top-level site that can be used to manage multiple primary sites
  * **Site database** : a required site system role for central administration sites, primary sites, and secondary sites that stores and processes data
  * **Site database server** : hosts the site database for a site, can be colocated on the site server or hosted on a remote system
  * **Secondary site** : a child of a primary site used to distribute content to clients in remote locations with low bandwidth connections
  * **ConfigMgr console** : The software that administrators use to manage a site
  * **SMS Provider** : a site system role that provides an interface for the ConfigMgr console to interact with the site database
  * **Security role** : a set of permissions applied to admin users to control access to SCCM objects (e.g., sites, device collections) and actions (e.g., read, modify, deploy)
  * **Security scope** : a container of objects to which a security role can be granted access (e.g., an admin is granted the permissions in security role A to the objects added to security scope B)

Here is a diagram of what an example SCCM hierarchy might look like:

![](https://specterops.io/wp-content/uploads/sites/3/2023/09/1kGVrrAJ2x1xLd2XgxTv6Ug.png)

Confused yet? Sorry — I didn’t make these names up, but these are the names we were given. This will be a good reference to come back to as we will use these terms throughout the rest of this post.

### The Problem

It really surprised me to observe this behavior in my lab as I was researching another technique for hierarchy takeover that required a handful of extra steps and no longer seems important. I always assumed that role-based access control in SCCM was defined on a per-site basis.

Apparently I’m just late to the party and this is well-known to SCCM admins, because **allowing hierarchy-wide access to SCCM administrators by default was a design decision** that is [well-documented by Microsoft](https://learn.microsoft.com/en-us/mem/configmgr/core/understand/fundamentals-of-role-based-administration):

> Sites aren’t used as administrative boundaries. In other words, don’t expand a standalone primary site to a hierarchy with a central administration site to separate administrative users.

> All security assignments are replicated and available throughout the hierarchy. Role-based administration configurations replicate to each site in the hierarchy as global data, and then are applied to all administrative connections.

Sure enough, when I granted a brand new Active Directory user the Full Administrator security role in an SCCM primary site, that user appeared as a Full Administrator in the CAS and other primary sites in the hierarchy.

But wait, isn’t it possible to create custom security roles and scopes in the ConfigMgr console to limit the permissions granted to a given administrative user (e.g., admin X can only read/write to Y objects in site Z)?

Yes, but attackers with administrative access to any site database in any primary site can grant themselves Full Administrator access to the All security scope for the All Systems collection and the change will be replicated throughout the hierarchy. If they are sneaky, they could even add themselves to a custom security role with the exact permissions for the exact security scope needed to meet their objectives.

With write access to the site database in any primary site, you can do anything.

In other words, **there is no way to configure SCCM role-based access control to prevent hierarchy takeover from any child primary site**.

Here are just a few of the ways an attacker could make these changes to a site database (where the site server is required to have admin privileges):

  1. As any authenticated domain user, coerce NTLM authentication via SMB from a site server and relay it to that site’s remote site database, SMS Provider, or passive site server
  2. As an administrator of any primary site, push install the SCCM client software on the site server, site database, SMS Provider, or passive site server to gain access to an account with db_owner database privileges
  3. Gain access to a site database via less predictable but common methods such as kerberoasting the database service account, misconfigured SQL links, database administrator (DBA) account compromise, etc.

Hierarchy takeover can then be executed using the following SQL statements, which [can be combined](https://twitter.com/_Mayyhem/status/1700602445603209236/photo/1) into a single [ntlmrelayx](https://github.com/fortra/impacket/blob/master/examples/ntlmrelayx.py) command:
  
  
  # Switch to site database
  USE CM_<SITE_CODE>;
  
  # Grant "Full Administrator" security role
  INSERT INTO RBAC_Admins
  (AdminSID,LogonName,IsGroup,IsDeleted,CreatedBy,CreatedDate,ModifiedBy,ModifiedDate,SourceSite)
  VALUES (<USER_HEX_AD_SID>,'<DOMAIN_SHORTNAME><USERNAME>',0,0,'','','','','<SITE_CODE>');
  
  # Grant "All Objects" scope
  INSERT INTO RBAC_ExtendedPermissions (AdminID,RoleID,ScopeID,ScopeTypeID)
  VALUES ((SELECT AdminID FROM RBAC_Admins WHERE LogonName = '<DOMAIN_SHORTNAME><USERNAME>'),'SMS0001R','SMS00ALL','29');
  
  # Grant "All Systems" scope
  INSERT INTO RBAC_ExtendedPermissions (AdminID,RoleID,ScopeID,ScopeTypeID)
  VALUES ((SELECT AdminID FROM RBAC_Admins WHERE LogonName = '<DOMAIN_SHORTNAME><USERNAME>'),'SMS0001R','SMS00001','1');
  
  # Grant "All Users and User Groups" scope
  INSERT INTO RBAC_ExtendedPermissions (AdminID,RoleID,ScopeID,ScopeTypeID)
  VALUES ((SELECT AdminID FROM RBAC_Admins WHERE LogonName = '<DOMAIN_SHORTNAME><USERNAME>'),'SMS0001R','SMS00004','1');"

Any account with local admin or database write privileges on any primary site database server or with [derivative/transitive access to these privileges](https://sixdub.medium.com/derivative-local-admin-cdd09445aac8) could make these changes and compromise the entire hierarchy as well.

### Why This Matters

This massively increases the blast radius of any primary site in a hierarchy being compromised, for example using the techniques documented in [Garrett Foster’s](https://posts.specterops.io/site-takeover-via-sccms-adminservice-api-d932e22b2bf) and my [previous research](https://posts.specterops.io/sccm-site-takeover-via-automatic-client-push-installation-f567ec80d5b1) on this topic. These attacks are extremely easy to execute and common across many organizations we have seen and heard about, the simplest path only requiring that:

  * any site server is reachable via SMB to coerce NTLM authentication (or authentication can be coerced another way, such as automatic client push installation);
  * any site database or SMS Provider for that site is hosted remotely from the site server, or there is a passive site server;
  * that remote site database (or site server in a high availability pair with a local site database) is reachable via MSSQL, that remote SMS Provider is reachable via HTTPS, or that site server, remote site database, or remote SMS Provider is reachable via SMB;
  * NTLM relay protections (e.g., NTLM disabled, SMB Signing, EPA, MFA) are not required; and
  * firewall rules between the attacker and the site server, site database, SMS Provider, or passive site server aren’t restricted to necessary sources (although this requirement can be bypassed in some cases — keep an eye out for more on this in a future post).

If the conditions above are met, an attacker can use [PetitPotam](https://github.com/topotam/PetitPotam) or [SpoolSample](https://github.com/leechristensen/SpoolSample) to coerce NTLM authentication from the site server, relay it to the database, and grant themselves administrative permissions.

There are also other possible paths that don’t involve relaying NTLM authentication from the site server, such as those involving other accounts with direct or derivative/transitive write access to the site database.

This gets particularly spicy when systems from different Active Directory forests are joined to sites in the same hierarchy, allowing **compromise of one primary site to result in crossing of forest security boundaries**.

If you or a loved one have been separating [tier-zero](https://posts.specterops.io/what-is-tier-zero-part-1-e0da9b7cdfca) or other assets of a higher security classification (e.g., domain controllers) into a separate primary site to help secure them, those assets are at risk of compromise from other primary sites that may not get the same attention from the security team.

### Mitigation

So what can we do about this?

If you have the convenience of building a new SCCM environment, follow some great advice from a long-time SCCM admin and friend and “just say no to CAS”. **Use a standalone primary site** instead. A CAS is only needed for environments that exceed 150,000 Windows clients.

In existing SCCM hierarchies containing any site with tier-zero assets, treat all administrative users, site servers, site databases, DBAs, SMS Providers, passive site servers, and possibly other site system roles with NTLM relay protocol connectivity to those systems (spoiler alert: [there are tons](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/ports)) as tier-zero themselves.

Alternatively, assign tier-zero systems to a separate hierarchy or [standalone primary site](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/design-a-hierarchy-of-sites#standalone-primary-site) specific to tier-zero assets if they need to be managed using SCCM.

Help **prevent relayed site server NTLM authentication** from being used to take over sites by requiring:

  * the site database and SMS Provider roles to be hosted on site servers
  * [SMB signing](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/overview-server-message-block-signing) on site databases, SMS Providers, and site servers
  * [Extended Protection for Authentication (EPA) on site databases](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/connect-to-the-database-engine-using-extended-protection?view=sql-server-ver16) and [Active Directory Certificate Services (AD CS) servers](https://support.microsoft.com/en-gb/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429)
  * [LDAP signing or channel binding](https://support.microsoft.com/en-au/topic/2020-and-2023-ldap-channel-binding-and-ldap-signing-requirements-for-windows-kb4520412-ef185fb8-00f7-167d-744c-f299a66fc00a) on domain controllers
  * [Multifactor authentication for SMS Provider calls](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/security/plan-for-security#sms-provider-authentication)
  * firewall rules that prevent unnecessary sources from connecting to:  
– SMB and MSSQL on site database servers  
– SMB and HTTPS on SMS Providers  
– SMB on primary and central administration site servers

Or you can just disable NTLM for the domain or these systems, but that is very difficult for most organizations in reality.

### Detection

There are a few things we can look out for, such a site system domain computer account authenticating from an IP address that doesn’t belong to it or a new user being granted a security role, for example Full Administrator.

Unfortunately, SCCM logs are intended for troubleshooting, not security, so we likely need to rely on Windows event logs or write something custom. While an audit status message is created when adding an administrative user via the console, adding an admin using direct database modifications is not logged.

I may just be missing it, but the only default SCCM log I could find after adding a new account to the Full Administrator role via MSSQL didn’t include much detail:

PS C:Program FilesMicrosoft Configuration ManagerLogs> Get-ChildItem | Select-String -Pattern “lowpriv”

hman.log:1155:INFO: AddAIUsersToAIToolsDBRole, User [MAYYHEMlowpriv] is added to role SMSDBROLE_AITOOL. $$<SMS_HIERARCHY_MANAGER><09–17–2023 17:26:15.614+420><thread=7064 (0x1B98)>

I did not find any other logs or status messages for adding an admin, whether added via the console or directly to the database. It may be more effective to monitor for impactful actions new admins could take, such as deploying applications, which are logged in status messages:

![](https://specterops.io/wp-content/uploads/sites/3/2023/09/1DPHcAHcbZDJgPM7jTQJhow.png)

[Status filter rules](https://learn.microsoft.com/en-us/mem/configmgr/core/servers/manage/use-status-system#manage-status-filter-rules) can be created to take action when a certain status message occurs and/or to send them to the Windows event log.

Alternatively, you can monitor Windows event logs for additions to the local SMS Admins group on site servers, which is updated when admins are added.

If you have any detections for SCCM abuses that you have found useful, please consider sharing them to help the rest of our community!

I keep an up-to-date list of defensive recommendations for SCCM in the [SharpSCCM wiki](https://github.com/Mayyhem/SharpSCCM/wiki#defensive-recommendations) as I learn more that may be helpful as well.

### Random Thoughts

Changes to the copy of the site database on secondary site servers do not seem to replicate up to their parent sites. I haven’t found a way to abuse this (…yet).

It does not seem possible to exclude the tables related to this escalation path from replicating up from primary sites to the central administration site and then to other primary sites. Even if it was possible, this change would definitely [not be supported by Microsoft](https://learn.microsoft.com/en-US/troubleshoot/mem/configmgr/setup-migrate-backup-recovery/support-policy-for-manual-database-changes) and could have unintended consequences.

I’ve only tested this in my lab, and I very well could have made some incorrect assumptions or conclusions. If you notice any mistakes or missing information in this post, I’d love to chat with you about how I can correct it.

### Coming Soon

My coworker Garrett Foster (@[garrfoster](https://twitter.com/garrfoster), author of [sccmhunter](https://github.com/garrettfoster13/sccmhunter)) and I have been collaborating on new approaches to site takeover, which we now know equates to hierarchy takeover, resulting in some very interesting attack paths we suspect many organizations are vulnerable to.

We will be authoring several more upcoming posts to provide offensive and defensive guidance for SCCM site and hierarchy takeovers and are working on a ton of new content for reproducing, mitigating, and detecting attacks involving SCCM.

We love researching this stuff. If you love it too and want to collaborate, have any questions, need some help, or are just starting your journey down this rabbit hole, hit us up in the #sccm channel in the [BloodHoundGang Slack](https://bloodhoundhq.slack.com/)!

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=41929c61e087)

* * *

[SCCM Hierarchy Takeover](https://posts.specterops.io/sccm-hierarchy-takeover-41929c61e087) was originally published in [Posts By SpecterOps Team Members](https://posts.specterops.io) on Medium, where people are continuing the conversation by highlighting and responding to this story.

Post Views: 14,215

[ Chris Thompson ](https://specterops.io/blog/author/christhompson/)

Senior Security Researcher 

Chris is a Sr. Security Researcher at SpecterOps, where he researches attack paths in widely-used software such as SCCM, MSSQL, and Intune and develops open-source tools to identify, abuse, and prevent them. Chris has led red teams, network, webapp, and wireless pentests, instructed at Black Hat , DEF CON, SO-CON, and SpecterBash, and spoken at Black Hat Arsenal, DEF CON Demo Labs, Troopers, SO-CON, and MMS.
