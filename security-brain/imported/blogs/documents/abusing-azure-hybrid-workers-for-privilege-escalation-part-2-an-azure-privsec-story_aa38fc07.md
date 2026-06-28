---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-14_abusing-azure-hybrid-workers-for-privilege-escalation-part-2-an-azure-privsec-st.md
original_filename: 2022-04-14_abusing-azure-hybrid-workers-for-privilege-escalation-part-2-an-azure-privsec-st.md
title: 'Abusing Azure Hybrid Workers for Privilege Escalation – Part 2: An Azure PrivSec
  Story'
category: documents
detected_topics:
- jwt
- access-control
- cloud-security
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- jwt
- access-control
- cloud-security
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: aa38fc072f1ea18a38fed0c1ab367b2881e3fa690a9ed80a50ca22f8847be3e2
text_sha256: ae3a319b8a2b46999fb4c530f4959fde4de791880f5564f040d8d103457466c9
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing Azure Hybrid Workers for Privilege Escalation – Part 2: An Azure PrivSec Story

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-14_abusing-azure-hybrid-workers-for-privilege-escalation-part-2-an-azure-privsec-st.md
- Source Type: markdown
- Detected Topics: jwt, access-control, cloud-security, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `aa38fc072f1ea18a38fed0c1ab367b2881e3fa690a9ed80a50ca22f8847be3e2`
- Text SHA256: `ae3a319b8a2b46999fb4c530f4959fde4de791880f5564f040d8d103457466c9`


## Content

---
title: "Abusing Azure Hybrid Workers for Privilege Escalation – Part 2: An Azure PrivSec Story"
page_title: "Abusing Azure Hybrid Workers for Privilege Escalation | NetSPI"
url: "https://www.netspi.com/blog/technical/cloud-penetration-testing/abusing-azure-hybrid-workers-part-2/"
final_url: "https://www.netspi.com/blog/technical-blog/cloud-penetration-testing/abusing-azure-hybrid-workers-part-2/"
authors: ["Josh Magri (@passthehashbrwn)"]
programs: ["Microsoft"]
bugs: ["Privilege escalation"]
bounty: "10,000"
publication_date: "2022-04-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2712
---

[Technical](/blog/technical-blog/#post-container) / Cloud Pentesting 

# Abusing Azure Hybrid Workers for Privilege Escalation – Part 2: An Azure PrivEsc Story

April 14, 2022

### [Josh Magri](/authors/josh-magri/)

  * [](https://www.facebook.com/sharer/sharer.php?u=https://www.netspi.com/blog/technical-blog/cloud-pentesting/abusing-azure-hybrid-workers-part-2/)
  * [](https://twitter.com/intent/tweet?text=Abusing Azure Hybrid Workers for Privilege Escalation – Part 2: An Azure PrivEsc Story&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/abusing-azure-hybrid-workers-part-2/)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.netspi.com/blog/technical-blog/cloud-pentesting/abusing-azure-hybrid-workers-part-2/&title=Abusing Azure Hybrid Workers for Privilege Escalation – Part 2: An Azure PrivEsc Story)

![Abusing Azure Hybrid Workers for Privilege Escalation – Part 2: An Azure PrivEsc Story](https://www.netspi.com/wp-content/uploads/2024/03/Blog-Feature-Images-07.webp)

The NetSPI team recently discovered a set of issues that allows any Azure user with the Subscription Reader role to dump saved credentials and certificates from Automation Accounts. In cases where Run As accounts were used, this allowed for a Reader to Contributor privilege escalation path.

This is part two of a two-part blog series. [In part one](https://www.netspi.com/blog/technical/cloud-penetration-testing/abusing-azure-hybrid-workers-for-privilege-escalation/), we walked through a privilege escalation scenario by abusing Azure hybrid workers. In this blog, we’ll dig a little deeper and explain how we utilized an undocumented internal API to poll information about the Automation Account (Runbooks, Credentials, Jobs).

Note: The scope of this bug is limited to a subscription. A subscription Reader account is necessary to exploit this bug, and it is not a cross-tenant issue.

### Background: Azure Hybrid Worker Groups

The genesis of this research stemmed from studying any potential abuse mechanisms from how Azure Automation handled authenticating Hybrid Worker nodes.

Azure Automation’s core feature is Runbooks, which are pieces of code that can be run on Azure’s Infrastructure or customer-owned Azure Virtual Machines (VMs). These are often used to run scheduled tasks or manage Azure resources. To accomplish this, the runbooks must be authenticated, which can be accomplished through several methods. 

Users can store credentials in Automation Accounts (AA) and access them via Runbooks. Automation Accounts can also use Run As accounts to create a Service Principal that will be used for authentication via a certificate stored in the Automation Account. 

The third option is using Managed Identities, which is what Microsoft is [pushing users towards](https://docs.microsoft.com/en-us/azure/automation/automation-security-guidelines). Managed Identities allow the user to obtain a token at runtime to authenticate and eliminate the issue of stored credentials. The Get-AzPasswords script from the MicroBurst project supports dumping all three kinds of authentication, so long as you have Contributor access. 

Normally, a Runbook is executed in a sandbox on Azure’s infrastructure. However, this comes with certain constraints, namely processing power and execution time. Any long running or resource intensive code may be ill-suited to run in this manner. 

To bridge this gap, Azure offers Hybrid Worker Groups (HWG). HWGs offer users the ability to run Runbooks on their own Azure Virtual Machines, so they can run on more powerful machines for longer. 

Normally, this is accomplished by deploying a Virtual Machine Extension to the desired Virtual Machine to register the Virtual Machine as a HWG node. Then, the user can execute Runbooks on those Hybrid Worker nodes. 

There are also two types of HWGs: User and System. System HWGs are used for Update Management and don’t have the necessary permissions for what we’re interested in, so we’ll be focusing on User HWGs.

### The First Set of Issues: Compromising Credentials

We began our research with a registered Hybrid Worker node. When you execute a runbook on the host, the HybridWorkerService process spawns the Orchestrator.Sandbox process. The command line for the latter is as follows.

![](https://www.netspi.com/wp-content/uploads/041422_Automation-Account-Hybrid-Workers-Part-2-Blog_1.png)

Next, we focused on MSISecret. At first glance, it appears that the Hybrid Worker node must be able to use this to request an MSI token externally. After reversing the binary, this turned out to be true. 

Every Automation Account has a “Job Runtime Data Service” endpoint, or JRDS, which Hybrid Workers use to poll for jobs and request credentials. You can see the JRDS URL supplied in the command line above. Below is what the full path to request a token looks like in the binary. 

![](https://www.netspi.com/wp-content/uploads/041422_Automation-Account-Hybrid-Workers-Part-2-Blog_2.png)

And here you can see this in action.

![](https://www.netspi.com/wp-content/uploads/041422_Automation-Account-Hybrid-Workers-Part-2-Blog_3.png) ![](https://www.netspi.com/wp-content/uploads/041422_Automation-Account-Hybrid-Workers-Part-2-Blog_4.png)

You can only get that MSI secret after receiving a job from the JRDS endpoint. This can be achieved by polling the /sandboxes endpoint. HWGs handle jobs in a first-come-first-serve fashion, so whichever node polls the endpoint first starts first. By default, nodes will poll every 60 seconds so if polled constantly, then we should almost always beat out the other nodes and get a job with a secret. However, this only works if Runbooks jobs are actively being run through the HWG.

Since we’re able to request Managed Identity tokens, it would make sense that we can request other forms of authentication. A quick grep through of the decompiled binary makes this apparent, and a quick request to these endpoints will yield results. 

![](https://www.netspi.com/wp-content/uploads/041422_Automation-Account-Hybrid-Workers-Part-2-Blog_5.png)

The JSON Web Token (JWT) in these requests is for the System Assigned MI of the Virtual Machine, not a management token for Azure.

![](https://www.netspi.com/wp-content/uploads/041422_Automation-Account-Hybrid-Workers-Part-2-Blog_6.png)

Requesting all certificates:

![](https://www.netspi.com/wp-content/uploads/041422_Automation-Account-Hybrid-Workers-Part-2-Blog_7.png)

We were satisfied with these findings. We figured that this represented an escalation path from Virtual Machine Contributor to Subscription Contributor if Hybrid Worker nodes were in use and reported our findings to Microsoft.

### Escalating Our Findings

After we had submitted our report, we found a recently [published blog](https://azsec.azurewebsites.net/2021/11/09/laterally-move-by-abusing-log-analytics-agent-and-automation-hybrid-worker/) that detailed some of these same ideas, though their thesis was obtaining lateral movement after an administrator pushed a certificate to the Virtual Machine. The author also demonstrated that you could register a new Hybrid Worker node to an Automation Account using the Automation Account key and Log Analytics Workspace key. We wondered if we could abuse this route to escalate the severity of our previous findings.

To read Automation Account keys, a user only needs the Reader role. To exploit this, we hacked up some source code from Microsoft’s Desired State Configuration (DSC) repository.

The repository contained some scripts that are used to register a new Hybrid Worker node, so we bypassed some environment checks and created users/groups that are expected to exist. The registration process looks like this: 

  1. Generate a new self-signed certificate or use an existing one
  2. Create a payload with some details: HWG name, IP address, certificate thumbprint, etc.
  3. Sign the payload with the AA key
  4. Send a PUT request to the AA with all the above info 

This also does not require Hybrid Worker Groups to already be in use; we can supply an arbitrary group name and it will be created. After registering, we can use the certificate and key generated during this process to access the same endpoints that we identified earlier. You also don’t need a Log Analytics workspace key to register because not all AAs are linked to a workspace. 

From start to finish, this exploit works as follows: 

  1. Attacker with Reader access reads the victim Automation Account key
  2. Attacker uses this key to register their own Virtual Machine in their own tenant as a Hybrid Worker node
  3. Attacker can dump any credentials or certificates from the victim AA and use them to authenticate 

We reported this issue to MSRC in a separate report. Below is the timeline for this case: 

  * October 25, 2021: Initial report submitted 
  * December 13, 2021: Second report submitted with details of full privilege escalation 
  * December 31, 2021: $10k bounty awarded 
  * March 14, 2022: Patch is applied 

### Microsoft’s Response to the Azure Automation Account Vulnerabilities

After reporting our findings, Microsoft identified the Azure Automation customers vulnerable to this exploit and notified them through the Azure portal. A fix has been rolled out to all customers.

Additionally, Microsoft has updated their documentation with [mitigation steps](https://docs.microsoft.com/en-us/azure/automation/automation-role-based-access-control#reader-role-access-permissions) for customers. They’ve updated the Reader role so that it no longer has the ListKeys permission on Automation Accounts and can no longer fetch Automation Account keys. They recommend that customers switch to custom roles if they need a Reader to fetch the Automation Account keys.

Microsoft has also provided the following guidance for deploying Hybrid Workers:

_Microsoft recommends installing Hybrid workers using the[Hybrid Runbook Worker Virtual Machine extension](https://docs.microsoft.com/en-us/azure/automation/extension-based-hybrid-runbook-worker-install?tabs=windows)_  _– without using the automation account keys – for registration of hybrid worker. Microsoft recommends this platform as it leverages a secure Azure AD based authentication mechanism and centralizes the control and management of identities and other resource credentials. Refer to_[ _the security best practices for Hybrid worker role._](https://docs.microsoft.com/en-us/azure/automation/automation-security-guidelines#securing-hybrid-runbook-worker-role)

### Conclusion

This issue allowed any user who could read Automation Account keys to extract any credentials or certificates from the affected Automation Account. This issue was not particularly technical or difficult to exploit, and only abused the intended methods for registration and credential retrieval. 

This is a good reminder that even low privileged role assignments such as Reader can have unintended consequences in your cloud environment. 

_Want to learn more about cloud penetration testing? Explore our_[ _Azure cloud penetration testing service_](https://www.netspi.com/security-testing/azure-penetration-testing) _._

## Explore More Blog Posts

[ ![](https://www.netspi.com/wp-content/uploads/2024/07/072924_TECH_GCPwn_Feature.webp) Cloud Pentesting Bypassing Microsoft Entra Conditional Access Policies via Nested App Authentication  June 22, 2026 Discover how attackers bypassed Microsoft Entra Conditional Access Policies using Nested App Authentication (NAA) flows in this technical vulnerability breakdown. Learn More ](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)[ ![](https://www.netspi.com/wp-content/uploads/2026/06/Feature-Image_Red-Plaid.jpg) Social Engineering I’m Just Asking Questions: Social Engineering as a Reporter  June 17, 2026 Dive into this real-world social engineering assessment where a fake anonymous tip and an adversary-in-the-middle framework tested the limits of an organization's security policies. Learn More ](https://www.netspi.com/blog/technical-blog/social-engineering/im-just-asking-questions-social-engineering-as-a-reporter/)[ ![](https://www.netspi.com/wp-content/uploads/2025/12/TB-Design-6_Feature-Image.png) CISO Perspectives Beyond the Hype: What Regulated Industries Need to Know Before Trusting AI Security Tooling  June 16, 2026 AI security tools can build an attack, but enterprise security teams in regulated industries need consistency, auditability, and predictable costs before they can trust one. Learn why the surrounding infrastructure is where most AI security vendors are still falling short. Learn More ](https://www.netspi.com/blog/executive-blog/ciso-perspectives/beyond-the-hype-what-regulated-industries-need-to-know-before-trusting-ai-security-tooling/)
