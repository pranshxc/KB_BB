---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-17_abusing-azure-hybrid-workers-for-privilege-escalation-part-1.md
original_filename: 2022-03-17_abusing-azure-hybrid-workers-for-privilege-escalation-part-1.md
title: Abusing Azure Hybrid Workers for Privilege Escalation – Part 1
category: documents
detected_topics:
- access-control
- cloud-security
- command-injection
- otp
- automation-abuse
- webhooks
tags:
- imported
- documents
- access-control
- cloud-security
- command-injection
- otp
- automation-abuse
- webhooks
language: en
raw_sha256: a9c44356711c99419ff1100d0fb308a45ca3a58204ab484f209f004bae950f33
text_sha256: d3bb5be409b88efa181ccf47d8e7fa21dd7462f070eecd11fb8d77839a7f27ca
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: true
---

# Abusing Azure Hybrid Workers for Privilege Escalation – Part 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-17_abusing-azure-hybrid-workers-for-privilege-escalation-part-1.md
- Source Type: markdown
- Detected Topics: access-control, cloud-security, command-injection, otp, automation-abuse, webhooks
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: True
- Raw SHA256: `a9c44356711c99419ff1100d0fb308a45ca3a58204ab484f209f004bae950f33`
- Text SHA256: `d3bb5be409b88efa181ccf47d8e7fa21dd7462f070eecd11fb8d77839a7f27ca`


## Content

---
title: "Abusing Azure Hybrid Workers for Privilege Escalation – Part 1"
page_title: "Abusing Azure Hybrid Workers for Privilege Escalation | NetSPI Blog"
url: "https://www.netspi.com/blog/technical/cloud-penetration-testing/abusing-azure-hybrid-workers-for-privilege-escalation/"
final_url: "https://www.netspi.com/blog/technical-blog/cloud-penetration-testing/abusing-azure-hybrid-workers-for-privilege-escalation/"
authors: ["Josh Magri (@passthehashbrwn)"]
programs: ["Microsoft (Azure)"]
bugs: ["Privilege escalation"]
publication_date: "2022-03-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2807
---

[Technical](/blog/technical-blog/#post-container) / Cloud Pentesting 

# Abusing Azure Hybrid Workers for Privilege Escalation – Part 1

March 17, 2022

### [Karl Fosaaen](/authors/karl-fosaaen/)

  * [](https://www.facebook.com/sharer/sharer.php?u=https://www.netspi.com/blog/technical-blog/cloud-pentesting/abusing-azure-hybrid-workers-for-privilege-escalation/)
  * [](https://twitter.com/intent/tweet?text=Abusing Azure Hybrid Workers for Privilege Escalation – Part 1&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/abusing-azure-hybrid-workers-for-privilege-escalation/)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/abusing-azure-hybrid-workers-for-privilege-escalation/&title=Abusing Azure Hybrid Workers for Privilege Escalation – Part 1)

![Abusing Azure Hybrid Workers for Privilege Escalation – Part 1](https://www.netspi.com/wp-content/uploads/2024/03/Blog-Feature-Images-01.webp)

On the NetSPI blog, we often focus on [Azure Automation Accounts](https://www.netspi.com/blog/technical/cloud-penetration-testing/maintaining-azure-persistence-via-automation-accounts/). They offer a fair amount of attack surface area during [cloud penetration tests](https://www.netspi.com/security-testing/cloud-penetration-testing) and are a great source for privilege escalation opportunities. 

During one of our recent Azure penetration testing assessments, we ran into an environment that was using [Automation Account Hybrid Workers](https://docs.microsoft.com/en-us/azure/automation/automation-hybrid-runbook-worker) to run automation runbooks on virtual machines. Hybrid Workers are an alternative to the traditional Azure Automation Account container environment for runbook execution. Outside of the “normal” runbook execution environment, automation runbooks need access to additional credentials to interact with Azure resources. This can lead to a potential privilege escalation scenario that we will cover in this blog.

### TL;DR

Azure Hybrid Workers can be configured to use Automation Account “Run as” accounts, which can expose the credentials to anyone with local administrator access to the Hybrid Worker. Since “Run as” accounts are typically subscription contributors, this can lead to privilege escalation from multiple Azure Role-Based Access Control (RBAC) roles.

### What are Azure Hybrid Workers?

For those that need more computing resources (CPU, RAM, Disk, Time) to run their Automation Account runbooks, there is an option to add Hybrid Workers to an Automation Account. These Hybrid Workers can be Azure Virtual Machines (VMs) or [Arc-enabled servers](https://docs.microsoft.com/en-us/azure/azure-arc/servers/overview), and they allow for additional computing flexibility over the normal [limitations](https://docs.microsoft.com/en-us/azure/automation/automation-runbook-execution) of the Automation Account hosted environment. Typically, I’ve seen Hybrid Workers as Windows-based Azure VMs, as that’s the easiest way to integrate with the Automation Account runbooks. 

![Add Hybrid Workers to an Automation Account](https://www.netspi.com/wp-content/uploads/031722_Abusing-Azure-Hybrid-Workers-Pt1-Blog_1.png)

In this article, we’re going to focus on instances where the Hybrid Workers are Windows VMs in Azure. They’re the most common configuration that we run into, and the Linux VMs in Azure can’t be configured to use the “Run as” certificates, which are the target of this blog.

The easiest way to identify Automation Accounts that use Hybrid Workers is to look at the “Hybrid worker groups” section of an Automation Account in the portal. We will be focusing on the “User” groups, versus the “System” groups for this post. 

![The easiest way to identify Automation Accounts that use Hybrid Workers is to look at the “Hybrid worker groups” section of an Automation Account in the portal.](https://www.netspi.com/wp-content/uploads/031722_Abusing-Azure-Hybrid-Workers-Pt1-Blog_2.png)

Additionally, you can use the Az PowerShell cmdlets to identify the Hybrid Worker groups, or you can enumerate the VMs that have the “HybridWorkerExtension” VM extension installed. I’ve found this last method is the most reliable for finding potentially vulnerable VMs to attack.

**Additional Azure Automation Accounts Research:**

  * [Get-AzurePasswords: Exporting Azure RunAs Certificates for Persistence](https://www.netspi.com/blog/technical/cloud-penetration-testing/exporting-azure-runas-certificates/)
  * [Using Azure Automation Accounts to Access Key Vaults](https://www.netspi.com/blog/technical/cloud-penetration-testing/azure-automation-accounts-key-stores/)
  * [Escalating Azure Privileges with the Log Analytics Contributor Role](https://www.netspi.com/blog/technical/cloud-penetration-testing/escalating-azure-privileges-with-the-log-analystics-contributor-role/)
  * [CVE-2021-42306 CredManifest: App Registration Certificates Stored in Azure Active Directory](https://www.netspi.com/blog/technical/cloud-penetration-testing/azure-cloud-vulnerability-credmanifest/)

### Running Jobs on the Workers

To run jobs on the Hybrid Worker group, you can modify the “Run settings” in any of your runbook execution options (Schedules, Webhook, Test Pane) to “Run on” the Hybrid Worker group.

![To run jobs on the Hybrid Worker group, you can modify the “Run settings” in any of your runbook execution options \(Schedules, Webhook, Test Pane\) to “Run on” the Hybrid Worker group.](https://www.netspi.com/wp-content/uploads/031722_Abusing-Azure-Hybrid-Workers-Pt1-Blog_3.png)

When the runbook code is executed on the Hybrid Worker, it is run as the “NT AUTHORITYSYSTEM” account in Windows, or “root” in Linux. If an Azure AD user has a role (Automation Contributor) with Automation Account permissions, and no VM permissions, this could allow them to gain privileged access to VMs.

We will go over this in greater detail in part two of this blog, but Hybrid Workers utilize an undocumented internal API to poll for information about the Automation Account (Runbooks, Credentials, Jobs). As part of this, the Hybrid Workers are not supposed to have direct access to the certificates that are used as part of the traditional “Run As” process. As you will see in the following blog, this isn’t totally true.

To make up for the lack of immediate access to the “Run as” credentials, [Microsoft recommends](https://docs.microsoft.com/en-us/azure/automation/automation-hrw-run-runbooks#runas-script) exporting the “Run as” certificate from the Automation Account and installing it on each Hybrid Worker in the group of workers. Once installed, the “Run as” credential can then be referenced by the runbook, to authenticate as the app registration.

If you have access to an Automation Account, keep an eye out for any lingering “Export-RunAsCertificateToHybridWorker” runbooks that may indicate the usage of the “Run as” certificates on the Hybrid Workers.

![If you have access to an Automation Account, keep an eye out for any lingering “Export-RunAsCertificateToHybridWorker” runbooks that may indicate the usage of the “Run as” certificates on the Hybrid Workers.](https://www.netspi.com/wp-content/uploads/031722_Abusing-Azure-Hybrid-Workers-Pt1-Blog_4.png)

The issue with installing these “Run As” certificates on the Hybrid Workers is that anyone with local administrator access to the Hybrid Worker can extract the credential and use it to authenticate as the “Run as” account. Given that “Run as” accounts are typically configured with the Contributor role at the subscription scope, this could result in privilege escalation.

### Extracting “Run As” Credentials from Hybrid Workers

We have two different ways of accessing Windows VMs in Azure, direct authentication (Local or Domain accounts) and platform level command execution (VM Run Command in Azure). Since there are a million different ways that someone could gain access to credentials with local administrator rights, we won’t be covering standard Windows authentication. Instead, we will briefly cover the multiple Azure RBAC roles that allow for various ways of command execution on Azure VMs.

**Affected Roles:**

  * [Virtual Machine Contributor](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-contributor)
  * Run Command Rights
  * VM Extension Rights
  * [Virtual Machine Administrator Login](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-administrator-login)
  * “Log in to a virtual machine with Windows administrator or Linux root user privileges”
  * [Log Analytics Contributor](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#log-analytics-contributor)
  * VM Extension Rights
  * [Previously covered in this blog](https://www.netspi.com/blog/technical/cloud-penetration-testing/escalating-azure-privileges-with-the-log-analystics-contributor-role/)
  * [Virtual Machine User Login](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-user-login)
  * May have rights to login and access the “Run as” PFX file left over in C:WindowsTemp
  * [Azure Connected Machine Onboarding](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-connected-machine-onboarding)
  * Can add new ARC machines, [which may get the “Run as” ](https://azsec.azurewebsites.net/2021/11/09/laterally-move-by-abusing-log-analytics-agent-and-automation-hybrid-worker/)  
[certificate installed](https://azsec.azurewebsites.net/2021/11/09/laterally-move-by-abusing-log-analytics-agent-and-automation-hybrid-worker/)
  * [Azure Connected Machine Resource Administrator](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-connected-machine-resource-administrator)
  * Can add new ARC machines, [which may get the “Run as” ](https://azsec.azurewebsites.net/2021/11/09/laterally-move-by-abusing-log-analytics-agent-and-automation-hybrid-worker/)  
[certificate installed](https://azsec.azurewebsites.net/2021/11/09/laterally-move-by-abusing-log-analytics-agent-and-automation-hybrid-worker/)
  * Azure ARC Extension Rights

Where noted above (VM Extension Rights), the VM Extension command execution method comes from the following NetSPI blog: [Attacking Azure with Custom Script Extensions](https://www.netspi.com/blog/technical/cloud-penetration-testing/attacking-azure-with-custom-script-extensions/).

Since the above roles are not the full Contributor role on the subscription, it is possible for someone with one of the above roles to extract the “Run as” credentials from the VM (see below) to escalate to a subscription Contributor. This is a somewhat similar escalation path to the one that we previously called out for the [Log Analytics Contributor role](https://www.netspi.com/blog/technical/cloud-penetration-testing/escalating-azure-privileges-with-the-log-analystics-contributor-role/).

#### Exporting the Certificate from the Worker

As a local administrator on the Hybrid Worker VM, it’s fairly simple to export the certificate. With Remote Desktop Protocol (RDP) access, we can just manually go into the certificate manager (certmgr), find the “Run as” certificate, and export it to a pfx file.

![With Remote Desktop Protocol \(RDP\) access, we can just manually go into the certificate manager \(certmgr\), find the “Run as” certificate, and export it to a pfx file.](https://www.netspi.com/wp-content/uploads/031722_Abusing-Azure-Hybrid-Workers-Pt1-Blog_5.png)

At this point we can copy the file from the Hybrid Worker to use for authentication on another system. Since this is a bit tedious to do at scale, we’ve automated the whole process with a PowerShell script.

#### Automating the Process

The following script is in the [MicroBurst repository](https://github.com/NetSPI/MicroBurst) under the “Az” folder:

<https://github.com/NetSPI/MicroBurst/blob/master/Az/Invoke-AzHybridWorkerExtraction.ps1>

This script will enumerate any running Windows virtual machines configured with the Hybrid Worker extension and will then run commands on the VMs (via Invoke-AzVMRunCommand) to export the available private certificates. Assuming the Hybrid Worker is only configured with one exportable private certificate, this will return the certificate as a Base64 string in the run command output.
  
  
  PS C:temphybrid> Invoke-AzHybridWorkerExtraction -Verbose
  VERBOSE: Logged In as kfosaaen@notarealdomain.com
  VERBOSE: Getting a list of Hybrid Worker VMs
  VERBOSE: 	Running extraction script on the HWTest virtual machine
  VERBOSE:  Looking for the attached App Registration... This may take a while in larger environments
  VERBOSE:  Writing the AuthAs script
  VERBOSE:  Use the C:tempHybridWorkersAuthAsNetSPI_tester_[REDACTED].ps1 script to authenticate as the NetSPI_sQ[REDACTED]g= App Registration
  VERBOSE: 	Script Execution on HWTest Completed
  VERBOSE: Run as Credential Dumping Activities Have Completed
  

The script will then write this Base64 certificate data to a file and use the resulting certificate thumbprint to match against App Registration credentials in Azure AD. This will allow the script to find the App Registration Client ID that is needed to authenticate with the exported certificate.

Finally, this will create an “AuthAs” script (noted in the output) that can be used to authenticate as the “Run as” account, with the exported private certificate.
  
  
  PS C:temphybrid> ls | select Name, Length
  Name  Length
  ----  ------
  AuthAsNetSPI_tester_[Redacted_Sub_ID].ps1  1018
  NetSPI_tester_[Redacted_Sub_ID].pfx  2615
  

This script can be run with any RBAC role that has VM “Run Command” rights on the Hybrid Workers to extract out the “Run as” credentials.

#### Authenticating as the “Run As” Account

Now that we have the certificate, we can use the generated script to authenticate to the subscription as the “Run As” account. This is very similar to what we do with exporting credentials in the Get-AzPasswords function, so this may look familiar.
  
  
  PS C:temphybrid> .AuthAsNetSPI_tester_[Redacted_Sub_ID].ps1
  PSParentPath: Microsoft.PowerShell.SecurityCertificate::LocalMachineMy
  Thumbprint  Subject
  ----------  -------
  BDD023EC342FE04CC1C0613499F9FF63111631BB  DC=NetSPI_tester_[Redacted_Sub_ID]
  
  Environments : {[AzureChinaCloud, AzureChinaCloud], [AzureCloud, AzureCloud], [AzureGermanCloud, AzureGermanCloud], [AzureUSGovernment, AzureUSGovernment]}
  Context  : Microsoft.Azure.Commands.Profile.Models.Core.PSAzureContext
  
  PS C:temphybrid> (Get-AzContext).Account  
  Id  : 52[REDACTED]57
  Type  : ServicePrincipal
  Tenants  : {47[REDACTED]35}
  Credential  :
  TenantMap  : {}
  CertificateThumbprint : ***REDACTED-SUSPECT-TOKEN***  ExtendedProperties  : {[Subscriptions, d4[REDACTED]b2], [Tenants, 47[REDACTED]35], [CertificateThumbprint, BDD023EC342FE04CC1C0613499F9FF63111631BB]}
  

#### Alternative Options

Finally, any user with the ability to run commands as “NT AUTHORITYSYSTEM” on the Hybrid Workers is also able to assume the authenticated Azure context that results from authenticating (Connect-AzAccount) to Azure while running a job as a Hybrid Worker. 

This would result in users being able to run Az PowerShell module functions as the “Run as” account via the Azure “Run command” and “Extension” features that are available to many of the roles listed above. Assuming the “Connect-AzAccount” function was previously used with a runbook, an attacker could just use the run command feature to run other Az module functions with the “Run as” context.

Additionally, since the certificate is installed on the VM, a user could just use the certificate to directly authenticate from the Hybrid Worker, if there was no active login context.

### Summary

In conjunction with the issues outlined in part two of this blog, we submitted our findings to MSRC.

Since this issue ultimately relies on an Azure administrator giving a user access to specific VMs (the Hybrid Workers), it’s considered a user misconfiguration issue. Microsoft has updated [their documentation](https://docs.microsoft.com/en-us/azure/automation/automation-hrw-run-runbooks#runas-script) to reflect the potential impact of installing the “Run as” certificate on the VMs. Additionally, you could also modify the certificate installation process to mark the certificates as “non-exportable” to help protect them.

![Note: Microsoft has updated their documentation to reflect the potential impact of installing the “Run as” certificate on the VMs.](https://www.netspi.com/wp-content/uploads/031722_Abusing-Azure-Hybrid-Workers-Pt1-Blog_6.png)

We would recommend against using “Run as” accounts for Automation Accounts and instead switch to using managed identities on the Hybrid Worker VMs.

Stay tuned to the [NetSPI technical blog](https://www.netspi.com/blog/technical/) for the second half of this series that will outline how we were able to use a Reader role account to extract credentials and certificates from Automation Accounts. In subscriptions where Run As accounts were in use, this resulted in a Reader to Contributor privilege escalation.

### Prior Work

While we were working on these blogs, the Azsec blog put out the “[Laterally move by abusing Log Analytics Agent and Automation Hybrid worker](https://azsec.azurewebsites.net/2021/11/09/laterally-move-by-abusing-log-analytics-agent-and-automation-hybrid-worker/)” post that outlines some similar techniques to what we’ve outlined above. Read the post to see how they make use of Log Analytics to gain access to the Hybrid Worker groups.

## Explore More Blog Posts

[ ![](https://www.netspi.com/wp-content/uploads/2024/07/072924_TECH_GCPwn_Feature.webp) Cloud Pentesting Bypassing Microsoft Entra Conditional Access Policies via Nested App Authentication  June 22, 2026 Discover how attackers bypassed Microsoft Entra Conditional Access Policies using Nested App Authentication (NAA) flows in this technical vulnerability breakdown. Learn More ](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)[ ![](https://www.netspi.com/wp-content/uploads/2026/06/Feature-Image_Red-Plaid.jpg) Social Engineering I’m Just Asking Questions: Social Engineering as a Reporter  June 17, 2026 Dive into this real-world social engineering assessment where a fake anonymous tip and an adversary-in-the-middle framework tested the limits of an organization's security policies. Learn More ](https://www.netspi.com/blog/technical-blog/social-engineering/im-just-asking-questions-social-engineering-as-a-reporter/)[ ![](https://www.netspi.com/wp-content/uploads/2025/12/TB-Design-6_Feature-Image.png) CISO Perspectives Beyond the Hype: What Regulated Industries Need to Know Before Trusting AI Security Tooling  June 16, 2026 AI security tools can build an attack, but enterprise security teams in regulated industries need consistency, auditability, and predictable costs before they can trust one. Learn why the surrounding infrastructure is where most AI security vendors are still falling short. Learn More ](https://www.netspi.com/blog/executive-blog/ciso-perspectives/beyond-the-hype-what-regulated-industries-need-to-know-before-trusting-ai-security-tooling/)
