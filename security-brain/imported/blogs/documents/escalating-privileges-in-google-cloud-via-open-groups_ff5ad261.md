---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-31_escalating-privileges-in-google-cloud-via-open-groups.md
original_filename: 2024-07-31_escalating-privileges-in-google-cloud-via-open-groups.md
title: Escalating Privileges in Google Cloud via Open Groups
category: documents
detected_topics:
- cloud-security
- access-control
- command-injection
- automation-abuse
- mobile-security
tags:
- imported
- documents
- cloud-security
- access-control
- command-injection
- automation-abuse
- mobile-security
language: en
raw_sha256: ff5ad2617c6e8e044936fd3b3d635ef7ae3bb68ab12e19734ab7a84c49c9927e
text_sha256: 9fad7c9cafd07af218c86d486a525f75c9c26a38e79eb1754d5f7112c7fb4e22
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating Privileges in Google Cloud via Open Groups

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-31_escalating-privileges-in-google-cloud-via-open-groups.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, command-injection, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `ff5ad2617c6e8e044936fd3b3d635ef7ae3bb68ab12e19734ab7a84c49c9927e`
- Text SHA256: `9fad7c9cafd07af218c86d486a525f75c9c26a38e79eb1754d5f7112c7fb4e22`


## Content

---
title: "Escalating Privileges in Google Cloud via Open Groups"
page_title: "Using Open Groups to Escalate Privileges in Google Cloud"
url: "https://www.netspi.com/blog/technical-blog/cloud-pentesting/escalating-privileges-in-google-cloud-via-open-groups/"
final_url: "https://www.netspi.com/blog/technical-blog/cloud-pentesting/escalating-privileges-in-google-cloud-via-open-groups/"
authors: ["Thomas Elling"]
programs: ["Google (GCP)"]
bugs: ["Cloud", "Privilege escalation"]
publication_date: "2024-07-31"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 119
---

[Technical](/blog/technical-blog/#post-container) / Cloud Pentesting 

# Escalating Privileges in Google Cloud via Open Groups 

July 31, 2024

### [Thomas Elling  ](/authors/telling/)

  * [](https://www.facebook.com/sharer/sharer.php?u=https://www.netspi.com/blog/technical-blog/cloud-pentesting/escalating-privileges-in-google-cloud-via-open-groups/)
  * [](https://twitter.com/intent/tweet?text=Escalating Privileges in Google Cloud via Open Groups &url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/escalating-privileges-in-google-cloud-via-open-groups/)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/escalating-privileges-in-google-cloud-via-open-groups/&title=Escalating Privileges in Google Cloud via Open Groups )

![Escalating Privileges in Google Cloud via Open Groups ](https://www.netspi.com/wp-content/uploads/2024/07/073124_TECH_Google-Vulnerability-Disclosure_Feature.webp)

Per [GCP IAM documentation](https://cloud.google.com/iam/docs/overview#google_group), Google Groups are valid principals for IAM policy bindings in Google Cloud. [Google also recommends](https://cloud.google.com/iam/docs/using-iam-securely#policy_management) using Groups when granting roles in GCP, as opposed to users. Groups can include groups outside of organizations like _devs@googlegroups.com_ or groups in an Organization like _admins@yourorg.com_. Google Groups can be managed via <https://groups.google.com/> and optionally through the Google Cloud Console.

Google Groups can be configured with various access settings at both the specific group and organization level. One important access setting is [“Who can join group”](https://support.google.com/groups/answer/2464926?hl=en#zippy=%2Csettings-reference). Most organizations will have anonymous internet access disabled by default, which leaves three common organization level settings: _Only invited users_ , _Anyone in the organization can ask_ , and _Anyone in the organization can join_.

This blog will detail how an attacker can escalate their privileges in Google Cloud by leveraging weak group join settings for groups that have been granted roles in GCP. Opportunities for Hunting and Detection are provided towards the end of the blog.

## TL;DR

  * A user that is a member of the organization can potentially escalate their privileges into Google Cloud if: 
  * A Google Group has been specified as a principal member in an IAM policy AND
  * the Google Group has been configured with open access permissions that allow any member of the organization to join the group.
  * Google Groups created via the main [Groups console](https://groups.google.com/) can be granted permissions within Google Cloud IAM Policy, even when the group has been configured with “Entire organization – can join group” access settings.
  * There does not appear to be any explicit, default guardrails in place to prevent administrators from assigning roles in GCP to Groups with open join settings.
  * This was reported to Google as a potential Privilege Escalation vector via Bug Hunters VRP. The report resulted in a classification of Type “Bug” and a Status of “Won’t Fix (Intended Behavior)”.

## Previous Research

  * Ashwin Vamshi – [Leaky Groups: Accidental Exposure in Google Groups](https://www.netskope.com/blog/leaky-groups-accidental-exposure-in-google-groups)
  * Ryan Kovatch – [Deciphering Google’s mysterious ‘batchexecute’ system](https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c)
  * Chris Moberly – [Tutorial on privilege escalation and post exploitation tactics in Google Cloud Platform environments](https://about.gitlab.com/blog/2020/02/12/plundering-gcp-escalating-privileges-in-google-cloud-platform/)

## Finding vulnerable Groups

As noted in the TL;DR, we need to find open groups that also have been granted roles in Google Cloud. This process is made a lot easier if you already have read access to list IAM Policy, so that you can target only the groups that actually have permissions. Without this extra information, you will be stuck with attempting to list and check every group.

From an offensive perspective, the main [Google Groups console](https://groups.google.com/) is probably the easiest way to quickly identify open groups. A member user, Developer Tools, and a little background research are all that is needed to get started.

Browsing to the Google Groups page with browser Dev Tools open shows requests related to a batchexecute endpoint.
  
  
  Decoded URL
  https://groups.google.com/u/2/_/GroupsFrontendUi/data/batchexecute?rpcids=rCA4W&source-path=/u/2/recent…
  
  Decoded POST body
  f.req=[[["rCA4W","[]",null,"generic"]]]…
  
  Response body
  )]}'
  
  104
  [["wrb.fr","rCA4W","[]",null,null,null,"generic"],…

Ryan Kovatch’s blog does a great job of explaining the format of the requests and responses for this endpoint. The main takeaway here is that we want to identify the particular rpcid that returns group settings information. This can be identified by browsing to the All Groups section and paginating through as many pages as possible to view every group in the organization. A batchexecute request containing the _zx9ptd_ rpcid should be present for every group listed.
  
  
  Decoded URL
  https://groups.google.com/u/2/_/GroupsFrontendUi/data/batchexecute?rpcids=zx9ptd&source-path=/u/2/all-groups&…
  
  Decoded POST body
  f.req=[[["zx9ptd","[\"demo-open-join@thisisnotarealorg.com\"]",null,"generic"]]]…
  
  Response body
  )]}'
  
  192
  [["wrb.fr","zx9ptd","[[\"110157945035653151646\",\"demo-open-join@thisisnotarealorg.com\"],[true,false,true],0]",null,null,null,"generic"],…

This request looks promising and the rpcid can be looked up by doing a quick search in the Dev Tools console.
  
  
  …
  _.gBa = new _.Oe("zx9ptd",_.fu,_.hu,[{
  key: _.Cj,
  value: !0
  }, {
  key: _.Ej,
  value: "/GroupsFrontendService.GetJoinPermissions"
  }]);
  …

Looking back at the responses for the zx9ptd request, the access settings of the Group can be determined by comparing an open group vs a closed group. The open group contains the following highlighted string in the response. This can then be used to identify open groups at scale by searching for a common group keyword and then paging through the groups. This string can then be searched via the Browser Developer Tools to find open groups.

Entire organization – can join group
  
  
  …,\"demo-open-join@thisisnotarealorg.com\"],[true,false,true],0]"…

Entire organization – can ask to join group
  
  
  …\"test1@thisisnotarealorg.com\"],[false,true,true],0]"…

Invited users – can join group
  
  
  …\"test2@thisisnotarealorg.com\"],[false,false,true],0]"…

While extremely rudimentary, this method can work at scale when you have thousands of groups to review. Manual checks can also be done easily by checking for a Join icon when browsing through the list of groups. A group with open join permissions will look like below.

![](https://www.netspi.com/wp-content/uploads/2024/07/OpenGroupsandGoogleCloud-1.png)

## Escalating into Google Cloud

The following example assumes that the demo-user is a normal member organization user with no permissions in Google Cloud. This is confirmed by browsing to the Cloud Console and attempting to list Projects in the Project chooser.

![](https://www.netspi.com/wp-content/uploads/2024/07/OpenGroupsandGoogleCloud-2.png)

The demo-open-join Group does have permissions in Google Cloud and has been previously configured with open join settings (see the last screenshot in the previous section). This group is a standard group created via the Groups UI and has been granted the Storage Admin Role on the entire prj-demo project in GCP.

![](https://www.netspi.com/wp-content/uploads/2024/07/OpenGroupsandGoogleCloud-3.png)

The demo-user can join the demo-open-join group by clicking into the group’s settings and clicking on the “Join group” button. The normal member user has successfully joined the group.

![](https://www.netspi.com/wp-content/uploads/2024/07/OpenGroupsandGoogleCloud-4.png)

![](https://www.netspi.com/wp-content/uploads/2024/07/OpenGroupsandGoogleCloud-5.png)

The demo-user can then refresh their session to the Cloud Console after a few minutes and will see a new project. Digging further into the console, the user will also be able to see buckets. Since the Storage Admin role has been granted to the demo-open-join group, any user in this group inherits these permissions.

![](https://www.netspi.com/wp-content/uploads/2024/07/OpenGroupsandGoogleCloud-6.png)

![](https://www.netspi.com/wp-content/uploads/2024/07/OpenGroupsandGoogleCloud-7.png)

This is a very simple example, but it demonstrates the risk around groups with open join permissions when they are granted roles in Google Cloud. Not every scenario will be this straightforward and impact depends entirely on the role and the scope of the permissions granted to the group.

## Prevention and Remediation

The best way to prevent accidental role grants to open join groups is to always validate the group’s access settings and members before making a role assignment. NetSPI was able to grant roles in GCP to a group with open join permissions (“Entire organization – can join group”). The test Organization was using default configurations and there were no explicit guardrails in place that prevented this. Google does support Security Groups, which have some additional protections in place, but also allow open join permissions.

![](https://www.netspi.com/wp-content/uploads/2024/07/OpenGroupsandGoogleCloud-8-1024x984.png)

Google does provide some Group specific guardrails around Group visibility. [Hiding certain groups](https://support.google.com/a/answer/167097#visibility) from general members could be an effective way to prevent users from enumerating sensitive groups.

General recommendations for [Groups can be found here](https://support.google.com/a/answer/7587183?hl=en#Groups). Google Cloud also provides additional features for controlling IAM permissions via [IAM Deny policies](https://cloud.google.com/iam/docs/deny-overview) that may be useful for your organization.

While this issue has been classified as Intended Behavior, there is a risk for customer misconfiguration. Google’s Security Command Center in GCP has a check (Open group IAM member) that can find these scenarios. Google’s recommendations for remediating the issue can be [found here](https://cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#open_group_iam_member).

## Hunting and Detection

The following may be helpful to organizations that want to actively search or detect on Open join groups. Note that these opportunities are meant to provide a starting point and may not work as written for every organization’s use case. At a high level, the detection below will alert to existing open groups in the environment while the hunting opportunities offer a more broad approach using IAM and Group metadata.

### Detection Opportunity #1

**Data Source** : IAM Policy bindings creation  
**Detection Strategy** : Behavior  
**Detection Concept** : Detect when an IAM policy is created where the principal is an open group. The finding OPEN_GROUP_IAM_MEMBER exists in Security Command Center for this detection opportunity.
  
  
  state="ACTIVE" AND NOT mute="MUTED" AND category="OPEN_GROUP_IAM_MEMBER"

![](https://www.netspi.com/wp-content/uploads/2024/07/OpenGroupsandGoogleCloud-9.png)

**Detection Reasoning** : A member user of the Organization could join the open group and inherit any permissions granted to the group.  
**Known Detection Consideration** : Detection relies on the cadence of scanning in Security Command Center.

### Hunting Opportunity #1 – Identify permissions for any groups in GCP

**Data Source** : IAM Policy Metadata  
**Detection Strategy** : Behavior  
**Hunting Concept** : Review all IAM Policies where the principal is a group using Asset Inventory. Will include ALL groups. This data should be cross-referenced with Hunting Opp #2.  
Gcloud CLI command
  
  
  gcloud asset search-all-iam-policies \
  --scope='...' \
  --query='memberTypes:group'

Console command

![](https://www.netspi.com/wp-content/uploads/2024/07/OpenGroupsandGoogleCloud-10.png)

**Hunting Reasoning** : A member user of the Organization could join the open group and inherit any permissions granted to the group.

### Hunting Opportunity #2 – Identify any open groups

**Data Source** : Group Metadata  
**Detection Strategy** : Behavior  
**Hunting Concept** : Review all groups that have open join access, even those that are not assigned permissions in GCP.

  1. Go to the Groups dashboard in the Admin console.
  2. Click the Manage Columns option.
  3. Add a new column “Who can join the group”.
  4. Click Save.
  5. Review this column for the setting “Anyone in the organization can join”.

![](https://www.netspi.com/wp-content/uploads/2024/07/OpenGroupsandGoogleCloud-11.png)

**Hunting Reasoning** : A member user of the Organization could join the open group and inherit any permissions granted to the group.

# Coordinated Disclosure Timeline

NetSPI worked with Google on coordinated disclosure.

  * 12/11/2023 – Report submitted
  * 12/11/2023 – Report triaged and assigned
  * 12/12/2023 – Status changed to Won’t Fix (Infeasible)
  * 12/14/2023 – Status changed to Won’t Fix (Intended Behavior)
  * 12/28/2023 – Status changed to Assigned (reopened)
  * 01/03/2024 – Status changed to Won’t Fix (Intended Behavior)
  * 01/16/2024 – Status changed to In Progress (Accepted) (reopened). Type changed to Bug.
  * 01/18/2024 – Status changed to Won’t Fix (Intended Behavior)
  * 01/21/2024 – Coordinated Disclosure process begins
  * 03/15/2024 – Coordinated Disclosure process completed

Thanks to Karl Fosaaen, Nick Lynch, and Ben Lister for their review.

[![](https://www.netspi.com/wp-content/uploads/2024/07/073124_TECH_Google-Vulnerability-Disclosure_In-Blog.webp)](https://www.netspi.com/netspi-ptaas/cloud-penetration-testing/)

### Authors:

[ ![Headshot of Thomas Elling](https://www.netspi.com/wp-content/uploads/2024/04/Thomas-Elling-1.jpg) Thomas Elling Director, Cloud Pentesting ](/authors/telling)

## Explore More Blog Posts

[ ![](https://www.netspi.com/wp-content/uploads/2024/07/072924_TECH_GCPwn_Feature.webp) Cloud Pentesting Bypassing Microsoft Entra Conditional Access Policies via Nested App Authentication  June 22, 2026 Discover how attackers bypassed Microsoft Entra Conditional Access Policies using Nested App Authentication (NAA) flows in this technical vulnerability breakdown. Learn More ](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)[ ![](https://www.netspi.com/wp-content/uploads/2026/06/Feature-Image_Red-Plaid.jpg) Social Engineering I’m Just Asking Questions: Social Engineering as a Reporter  June 17, 2026 Dive into this real-world social engineering assessment where a fake anonymous tip and an adversary-in-the-middle framework tested the limits of an organization's security policies. Learn More ](https://www.netspi.com/blog/technical-blog/social-engineering/im-just-asking-questions-social-engineering-as-a-reporter/)[ ![](https://www.netspi.com/wp-content/uploads/2025/12/TB-Design-6_Feature-Image.png) CISO Perspectives Beyond the Hype: What Regulated Industries Need to Know Before Trusting AI Security Tooling  June 16, 2026 AI security tools can build an attack, but enterprise security teams in regulated industries need consistency, auditability, and predictable costs before they can trust one. Learn why the surrounding infrastructure is where most AI security vendors are still falling short. Learn More ](https://www.netspi.com/blog/executive-blog/ciso-perspectives/beyond-the-hype-what-regulated-industries-need-to-know-before-trusting-ai-security-tooling/)
