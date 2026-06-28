---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-02_securing-databricks-cluster-init-scripts.md
original_filename: 2023-05-02_securing-databricks-cluster-init-scripts.md
title: Securing Databricks cluster init scripts
category: documents
detected_topics:
- cloud-security
- access-control
- command-injection
- api-security
- sso
- otp
tags:
- imported
- documents
- cloud-security
- access-control
- command-injection
- api-security
- sso
- otp
language: en
raw_sha256: aac934a734c24d031a0e3ebc5fa7c282dd3ab864741dd79336fefbd8652f0f1b
text_sha256: 42dc94f03c485343e82f5b6364fe2f77629182d29d84d329402edac8a1b5f8f9
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Securing Databricks cluster init scripts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-02_securing-databricks-cluster-init-scripts.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, command-injection, api-security, sso, otp
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `aac934a734c24d031a0e3ebc5fa7c282dd3ab864741dd79336fefbd8652f0f1b`
- Text SHA256: `42dc94f03c485343e82f5b6364fe2f77629182d29d84d329402edac8a1b5f8f9`


## Content

---
title: "Securing Databricks cluster init scripts"
page_title: "Securing Databricks cluster init scripts - SEC Consult"
url: "https://sec-consult.com/blog/detail/securing-databricks-cluster-init-scripts/"
final_url: "https://sec-consult.com/blog/detail/securing-databricks-cluster-init-scripts/"
authors: ["Elia Florio", "Florian Roth (@cyb3rops)", "Marius Bartholdy"]
programs: ["Databricks"]
bugs: ["Privilege escalation", "Cloud"]
publication_date: "2023-05-02"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1198
---

1. [ Home ](/)
  2. [ Blog ](/blog/)
  3. Securing Databricks cluster init scripts

# Securing Databricks cluster init scripts

02.05.2023 

This blog was co-authored by Elia Florio, Sr. Director of Detection & Response at Databricks and Florian Roth and Marius Bartholdy, security researchers with SEC Consult.

![](/fileadmin/_processed_/b/6/csm_sec-consult-h-databricks_9f7f4afe2a.png)

Protecting the Databricks platform and continuously raising the bar with security improvements is the mission of our Security team and the main reason why we invest in our [bug bounty program](https://hackerone.com/databricks?type=team). Through this program, we encourage (and reward) submissions from talented industry professionals who bring potential concerns to our attention. [Working together](https://www.databricks.com/blog/2022/10/10/admin-isolation-shared-clusters.html) with the [larger security community](https://www.databricks.com/blog/2022/02/04/a-tale-about-vulnerability-research-and-early-detection.html), we can uncover and remediate newly discovered product issues and make the Databricks platform an even more secure and safe place.

  
When feasible and interesting to the security community, we also share success stories from collaborations that come out of our bug bounty program. Today we would like to showcase how a well-written report from SEC Consult helped accelerate the sunsetting of certain deprecated legacy features and the adoption [of our new feature, workspace files](https://www.databricks.com/blog/launching-new-files-experience-databricks-workspace.html).

This blog includes separate sections authored by Databricks and SEC Consult respectively. It goes into the technical details of the discovered security concerns, the affected configurations, the impact, and the solutions implemented to address the vulnerability. We would like to thank SEC Consult for their professionalism and collaboration on this disclosure.

## Intro

At end of January 2023, Databricks received a report from SEC Consult about a potential privilege escalation issue that may allow an authenticated, low-privileged user of a cluster to elevate privileges and gain admin-level access to other clusters within the boundary of the same workspace and organization.

  
Our initial investigation aligned with the finder’s report and showed that exploitation of this issue required (a) a potential attacker to be in possession of a valid authenticated account, and (b) the applicable workspace to have either legacy global init script for clusters enabled, or alternatively, the presence of a preconfigured init script (cluster-named or cluster-scoped) stored on DBFS. In contrast to the case of cluster init scripts stored in DBFS, where the vulnerability can only be exploited where a script is present, enablement of legacy global init script (without a script file) is enough to be exposed to this issue.

  
In both cases (legacy global init script enabled or cluster init scripts stored in DBFS), an authenticated low-privileged user could add or take control of an init script and execute additional commands using the elevated privileges associated with running init scripts. **Databricks has not found evidence of such privilege escalations occurring in practice.**

![](/fileadmin/_processed_/a/7/csm_sec-consult-c-databricks-fig1_17ed885586.png) Figure 1: Easy toggle available to disable legacy global init script 

It is important to note that legacy global init scripts already reached [deprecation status nearly 3 years ago](https://docs.databricks.com/release-notes/product/2020/december.html#new-global-init-script-framework-is-ga) and that customers could disable such legacy scripts by the simple switch of a toggle already present in the product UI ([AWS](https://docs.databricks.com/clusters/init-scripts.html#migrate-legacy-scripts) | [Azure](https://learn.microsoft.com/en-us/azure/databricks/clusters/init-scripts#migrate-legacy-scripts)).

The following table summarizes the most common scenarios for different types of init scripts ([AWS](https://docs.databricks.com/clusters/init-scripts.html#init-script-types) | [Azure](https://learn.microsoft.com/en-us/azure/databricks/clusters/init-scripts#init-script-types) | [GCP](https://docs.gcp.databricks.com/clusters/init-scripts.html#init-script-types-1)):

Init script type |  Applicable cloud |  Vulnerability status |  Previously deprecated  
---|---|---|---  
Legacy Global |  AWS, Azure |  Vulnerable |  Yes  
Cluster named |  AWS, Azure |  Vulnerable |  Yes  
Global |  AWS, Azure, GCP |  Not Vulnerable |  No  
Cluster-scoped (stored on DBFS) |  AWS, Azure, GCP |  Vulnerable |  No  
Cluster-scoped (stored as workspace files) |  AWS, Azure, GCP |  Not Vulnerable |  No  
Cluster-scoped (stored onAWS/Azure/GCP) |  AWS, Azure, GCP |  Not Vulnerable |  No  
  
In response to this report from SEC Consult, we took the opportunity to harden our platform and keep customers safe with a series of additional steps and new product features:

![](/fileadmin/_processed_/9/9/csm_sec-consult-c-databricks-fig2_56f503a9ee.png) Figure 2: New recommendation to use workspace files instead of DBFS 

  * We immediately disabled the creation of new workspaces using the deprecated init script types (namely: legacy global init script and cluster-named scripts);
  * We announced a strict End-Of-Life deadline (September 1, 2023) for all deprecated init script types to further accelerate the migration to safer alternatives;
  * We engaged remaining customers who didn’t follow our earlier recommendations of disabling deprecated init scripts and helped them migrate to safer alternatives by providing tools to automate the process both for [legacy global init scripts](https://kb.databricks.com/legacy-global-init-script-migration-notebook) and [cluster-named init scripts](https://kb.databricks.com/legacy-global-init-script-migration-notebook);
  * Our Product and Engineering teams added support for cluster-scoped init scripts to be stored in workspace files ([AWS](https://docs.databricks.com/files/workspace-init-scripts.html) | [Azure](https://learn.microsoft.com/en-us/azure/databricks/files/workspace-init-scripts) | [GCP](https://docs.gcp.databricks.com/files/workspace-init-scripts.html#store-init-scripts-in-workspace-files)), a more secure alternative [recently made generally available.](https://www.databricks.com/blog/launching-new-files-experience-databricks-workspace.html) We also changed the default location of cluster-scoped init scripts in the product UI to be workspace files and added a visible message for users who still attempt to use DBFS to store init scripts.

![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_04/sec-consult-c-databricks-fig3.png) Figure 3: Workspace files is the new default location to store init scripts 

Files support in the workspace allows Databricks users to store Python source code, reference data sets, or any other type of file content (including init scripts) directly alongside their notebooks ([AWS](https://docs.databricks.com/files/workspace.html) | [Azure](https://learn.microsoft.com/en-us/azure/databricks/files/workspace) | [GCP](https://docs.gcp.databricks.com/files/workspace.html)). Workspace files extend capabilities previously available in Databricks Repos throughout the entire platform, even if users are not working with version control systems. Workspace files also allows you to **secure access to individual files or folders** using that object’s Access Control Lists (ACLs) ([AWS](https://docs.databricks.com/security/auth-authz/access-control/workspace-acl.html#file-permissions-1) | [Azure](https://learn.microsoft.com/en-us/azure/databricks/security/auth-authz/access-control/workspace-acl#folder-permissions) | [GCP](https://docs.gcp.databricks.com/security/auth-authz/access-control/workspace-acl.html#folder-permissions-1)), which can be configured to limit access to users or groups.

### Guidance and recommendations

We've been encouraging customers to move away from legacy and deprecated init scripts for the past [three years](https://docs.databricks.com/release-notes/product/2020/december.html#new-global-init-script-framework-is-ga) and this security finding recently reported by SEC Consult only emphasizes why customers should complete this migration journey as soon as possible. At the same time, the [introduction of workspace files](https://www.databricks.com/blog/launching-new-files-experience-databricks-workspace.html) for init scripts ([AWS](https://docs.databricks.com/files/workspace-init-scripts.html) | [Azure](https://learn.microsoft.com/en-us/azure/databricks/files/workspace-init-scripts) | [GCP](https://docs.gcp.databricks.com/files/workspace-init-scripts.html#store-init-scripts-in-workspace-files)) marks the initial milestone of our plan for offering a modern and more secure storage alternative to DBFS.

  
Customers can increase the security for their Databricks deployments and mitigate the security issue discussed in this blog by doing the following:

  1. Immediately **disable legacy global init scripts** ([AWS](https://docs.databricks.com/clusters/init-scripts.html#migrate-legacy-scripts) | [Azure](https://learn.microsoft.com/en-us/azure/databricks/clusters/init-scripts#migrate-legacy-scripts)) if not actively used: it’s a safe, easy, and immediate step to close this potential attack vector.
  2. Customers with legacy global init scripts deployed should first **migrate legacy scripts to the new global init script type** ([this notebook](https://kb.databricks.com/legacy-global-init-script-migration-notebook) can be used to automate the migration work) and, after this migration step, proceed to disable the legacy version as indicated in the previous step.
  3. **Cluster-named init scripts** are similarly affected by the issue and are also deprecated: customers still using this type of init scripts should disable cluster-named init scripts ([AWS](https://docs.databricks.com/clusters/init-scripts.html#disable-legacy-cluster-named-init-scripts-for-a-workspace) | [Azure](https://learn.microsoft.com/en-us/azure/databricks/clusters/init-scripts#disable-legacy-cluster-named-init-scripts-for-a-workspace)), migrate them to cluster-scoped scripts, and make sure that the scripts are stored in the new workspace files storage location ([AWS](https://docs.databricks.com/files/workspace.html) | [Azure](https://learn.microsoft.com/en-us/azure/databricks/files/workspace) | [GCP](https://docs.gcp.databricks.com/files/workspace.html)). [This notebook](https://kb.databricks.com/cluster-named-init-script-migration-notebook) can be used to automate the migration work.
  4. Existing **cluster-scoped init scripts stored on DBFS** should be migrated to the alternative, safer workspace files location ([AWS](https://docs.databricks.com/files/workspace.html) | [Azure](https://learn.microsoft.com/en-us/azure/databricks/files/workspace) | [GCP](https://docs.gcp.databricks.com/files/workspace.html)).
  5. Use [Databricks Security Analysis Tool](https://www.databricks.com/blog/2023/02/03/announcing-multi-cloud-support-security-analysis-tool-sat.html) (SAT) to automate security health checks of your Databricks workspace configurations against Databricks security best practices.

  
The following section is a reproduction of the technical report authored by SEC Consult researcher Florian Roth and Marius Bartholdy. While the research described below was conducted and tested with Azure Databricks as an example, the findings related to the deprecated init scripts types affect other cloud providers as set forth in the table above.

  
Thank you again to SEC Consult, and all of the security researchers who are working with us to make Databricks more secure every day. If you are a security researcher, we will see you at [hackerone.com/databricks](https://hackerone.com/databricks).

[![](/fileadmin/_processed_/d/c/csm_sec-consult-c-databricks-youtube_7f640009cc.png)](https://r.sec-consult.com/dbyoutube) Click to watch our proof-of-concept video on Youtube 

## Researching Databricks init scripts security

By Florian Roth and Marius Bartholdy, SEC Consult

A low-privileged user was able to break the isolation between Databricks compute clusters within the boundary of the same workspace and organization by gaining remote code execution. This subsequently would have allowed an attacker to access all files and secrets in the workspace as well as escalating their privileges to those of a workspace administrator.

[The Databricks File System](https://docs.databricks.com/dbfs/index.html) (DBFS) is fully accessible by every user in a workspace. Since Cluster-scoped and legacy global init scripts were stored there as well, an authenticated attacker with default permissions could:

  1. Find and modify an existing cluster-scoped init script.
  2. Place a new script in the default location for legacy global init scripts.

![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_04/sec-consult-c-databricks-fig4.png) Figure 4: New init script and shell 

### 1) Attack chain using existing init script

The default option to provide deprecated init script types (such as legacy global or cluster-named) was to upload them to the DBFS. Due to the DBFS being shared between all compute clusters inside the same workspace, it was possible to find or guess any pre-existing init scripts that had previously been configured on a cluster and stored in DBFS. This could be achieved by listing the content of existing DBFS directories:
  
  
  display(dbutils.fs.ls("dbfs:/databricks/scripts"))

All found .sh files could potentially be cluster-scoped init scripts, therefore the goal was to replace them somehow. While it was not possible to directly overwrite the file, with the following code it could be renamed and a new script with the old name could be created. The new malicious script contained a simple reverse shell that would be periodically launched. Since the cluster configuration was only aware of the script names, as soon as the init script was triggered again, a reverse shell, with root privileges on the compute cluster, was received:

![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_04/sec-consult-c-databricks-fig5.png) Figure 5: Spark configuration secrets 

Secrets can only be retrieved at runtime by the compute instance itself via a managed identity. Even workspace administrators cannot read them. Since they are however available to the compute cluster as soon as it is initialized, it was possible to retrieve their clear text values. Spark configuration secrets can be found at /tmp/custom-spark.conf, while secrets in the environment variables are accessible by reading the ` /proc//environ` file of the right process.

![](/fileadmin/_processed_/d/4/csm_sec-consult-c-databricks-fig6_e3f8e93e4d.png) Figure 6 - Packet capture on the backdoored cluster revealing the apiToken 

Using a vulnerability initially found by [Joosua Santasalo from Secureworks](https://www.databricks.com/blog/2022/10/10/admin-isolation-shared-clusters.html), it is possible to leak Databricks API tokens of other users, including administrators if they operate on the same instance. The original finding was remediated by isolating users from each other and especially from administrators. However, with the presented vulnerability the isolation could be broken by executing attacker-controlled scripts, and the old exploit was consequently valid again.

Using the previously established reverse-shell it was possible to capture control-plane traffic. As soon as we started a task with the administrative user, for example running a simple notebook, the token was sent unencrypted and could be leaked:

![](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_04/sec-consult-c-databricks-fig7.png) Figure 7: Token with administrative privileges 

The captured token could then be used to authenticate requests to the Databricks REST API. The following example allows viewing secret scopes and therefore confirmed that the token had administrative privileges:

### 2) Attack chain using legacy global init scripts

The same attack vector affected legacy global init scripts. These were deprecated in 2020, but left enabled by default in all workspaces and were also stored on the DBFS, specifically at `dbfs:/databricks/init/`. Any cluster would execute their content on initialization. Therefore, simply creating a new script in that directory would eventually lead to code execution on all clusters.

## Conclusion

With the **Vulnerability Lab** , SEC Consult **operates its own internal security laboratory** , in order to ensure an international know-how advantage over attackers in the areas of network and application security. It is nice to see vendors taking the security status of their products seriously. In this case, Databricks took the opportunity to not only fix a certain vulnerability but to harden their platform.

You can find more technical details in our Security Advisory ["Bypassing cluster isolation in Databricks Platform"](https://sec-consult.com/vulnerability-lab/advisory/bypassing-cluster-isolation-in-databricks-platform/) by Florian Roth (Atos) and Marius Bartholdy (SEC Office Berlin).

We also want to thank the whole Databricks team for their outstanding coordination and responsible disclosure process.

[ Back ](/blog/)
