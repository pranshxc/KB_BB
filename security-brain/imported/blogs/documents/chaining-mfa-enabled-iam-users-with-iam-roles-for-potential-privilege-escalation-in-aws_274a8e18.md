---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-16_chaining-mfa-enabled-iam-users-with-iam-roles-for-potential-privilege-escalation.md
original_filename: 2022-06-16_chaining-mfa-enabled-iam-users-with-iam-roles-for-potential-privilege-escalation.md
title: Chaining MFA-Enabled IAM Users with IAM Roles for Potential Privilege Escalation
  in AWS
category: documents
detected_topics:
- cloud-security
- mfa
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- cloud-security
- mfa
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 274a8e1887d316c689fed625ac35b11ded075b23e108ee998bf10ffada2fb895
text_sha256: 4be8c56b64a6034969ea4f4d060bbd317a8bc336b3aca736ad4bcbb0a8736a3e
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining MFA-Enabled IAM Users with IAM Roles for Potential Privilege Escalation in AWS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-16_chaining-mfa-enabled-iam-users-with-iam-roles-for-potential-privilege-escalation.md
- Source Type: markdown
- Detected Topics: cloud-security, mfa, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `274a8e1887d316c689fed625ac35b11ded075b23e108ee998bf10ffada2fb895`
- Text SHA256: `4be8c56b64a6034969ea4f4d060bbd317a8bc336b3aca736ad4bcbb0a8736a3e`


## Content

---
title: "Chaining MFA-Enabled IAM Users with IAM Roles for Potential Privilege Escalation in AWS"
page_title: "Chaining MFA-Enabled IAM Users with IAM Roles for Potential Privilege Escalation in AWS | Praetorian"
url: "https://www.praetorian.com/blog/stsgetsessiontoken-role-chaining-in-aws/"
final_url: "https://www.praetorian.com/blog/stsgetsessiontoken-role-chaining-in-aws/"
authors: ["Jason Kao"]
programs: ["AWS"]
bugs: ["Privilege escalation"]
publication_date: "2022-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2542
---

Skip to content

**Meet Constantine – Find Mythos-level vulnerabilities in your code. It proves them, patches them, PRs them back. Autonomously.**

[ Download Datasheet ](/resources/constantine-datasheet/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

  * Platform  Close Platform Open Platform

#### [Praetorian Guard Platform](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Services  Close Services Open Services

#### [Penetration Testing Services](/penetration-testing/)

  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)
  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)

#### [Advanced Offensive Security](/advanced-penetration-testing/)

  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)
  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)

#### [Continuous Offensive Security](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Why Praetorian  Close Why Praetorian Open Why Praetorian

#### [Customer Case Studies](/customer-success-in-cybersecurity/)

  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)
  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)

#### Resources

  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)
  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)

#### Use Cases

  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)
  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)

  * About  Close About Open About

#### [About Praetorian](/praetorian-offensive-cybersecurity-company/)

  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)
  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)

#### [Join Praetorian](/careers/#job-opening)

  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)
  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)

  * [ Platform Demo  ](/praetorian-guard-demo/)

  * [ Contact Us  ](/contact-us/)

  * [Cloud Security](https://www.praetorian.com/category/cloud-security/)

# Chaining MFA-Enabled IAM Users with IAM Roles for Potential Privilege Escalation in AWS

  * [Jason Kao](https://www.praetorian.com/author/jason-kao/)
  * [ June 16, 2022 ](https://www.praetorian.com/blog/2022/06/16/)

![](https://www.praetorian.com/wp-content/uploads/2024/06/amazon-aws.png)

## Overview

In AWS, [sts:AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) is an action within AWS’s Security Token Service that allows existing IAM principals to access AWS resources to which they may not already have access. For example, Role A can assume Role B and then use Role B’s privileges to access AWS resources. Common use cases include assuming a role within the same AWS Account, gaining cross-account access to interact with workloads in different AWS Accounts, or providing centralized access to security or operations teams.

Multiple sts:AssumeRole calls can be linked to chain roles. For example, if Role A can assume Role B and Role B can assume Role C, someone with access to Role A could gain the permissions to Role C by [role chaining](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) sts:AssumeRole calls together. This is a privilege escalation path that malicious actors can abuse and that security teams frequently overlook.

In this blog post, we will be discussing one specific role chaining path that begins with an IAM User with MFA. While researching this privilege escalation path, Praetorian noted inconsistencies with documentation and permissions related to sts:GetSessionToken and Policy Simulator and reported those to AWS Security. Due to the inconsistencies with AWS documentation and Policy Simulator, it is possible for AWS customers to misconfigure security controls and overlook AWS IAM users with privilege escalation paths potentially gained via role chaining. 

### Timeline

  * May 2022: Praetorian reported these issues to AWS Security.
  * May 2022: AWS updated documentation to clarify sts:GetSessionToken.
  * Planned: AWS is planning to update IAM Policy Simulator for both sts:GetSessionToken and sts:GetCallerIdentity.

## Technical Walkthrough

### AWS & Multi-Factor Authentication 

AWS recommends configuring [multi-factor authentication](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) (MFA) to help protect AWS resources. In AWS, security teams can enable MFA for IAM Users or the AWS account root user. 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20437%20315'%3E%3C/svg%3E)

_Figure 1: MFA prompt within AWS._

### Validating MFA on an IAM User

AWS IAM policies support multiple MFA conditions including the following:

  * aws:MultiFactorAuthPresent for existence
  * aws:MultiFactorAuthAge for duration

These MFA Conditions validate the presence of MFA on AWS API and CLI actions. The conditions apply to a couple places in this role chaining example:

  * [Directly](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage.html) on the IAM User’s permissions. An example IAM policy snippet is shown in Figure 2.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20314'%3E%3C/svg%3E)

_Figure 2: Source code requiring MFA on a user’s permissions._

  * On a role’s trust policy, checked during the sts:AssumeRole call. For an example trust policy, see Figure 3. 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20441%20244'%3E%3C/svg%3E)

_Figure 3: A role’s trust policy requiring MFA._

### Temporary Security Credentials vs Long-Term Credentials

Authenticating to AWS can result in [temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) or long-term credentials. The type of credential used in AWS has an impact on MFA. AWS has designed MFA protection to only apply to temporary security credentials. Additionally, [MFA-protected API access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) cannot be used either with AWS account root user credentials or U2F security keys. 

With IAM Users, the IAM Access Key and Secret Access Key are long-term credentials and do not have the aws:MultiFactorAuthPresent condition key available. However, while using the AWS Management Console AWS generates temporary security credentials for an IAM User and thus the aws:MultiFactorAuthPresent condition key is available. However, when using the AWS CLI or API in conjunction with an IAM Access Key and Secret Access Key, the aws:MultiFactorAuthPresent condition key is not present in the request due to Access Keys and Secret Access Keys being long-term credentials. In that scenario the user must make another call to generate temporary credentials.

### Acquiring Temporary Security Credentials for an IAM User

In AWS, there are two distinct methods for generating temporary security credentials.

  * sts:GetSessionToken

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20584%20142'%3E%3C/svg%3E)

_Figure 4: Generating temporary security credentials via sts:GetSessionToken._

Note: stsGetSessionToken is similar to [sts:GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html) where the call cannot be controlled by IAM policies. This means that sts:GetSessionToken cannot be denied by an explicit deny and that an IAM user will always be able to call sts:GetSessionToken provided the call is properly formed.

  * sts:AssumeRole

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20587%20174'%3E%3C/svg%3E)

_Figure 5: Generating temporary security credentials via sts:AssumeRole._

Thus, if MFA has been setup for the IAM User, then we can chain roles to an IAM User with MFA by one of the following two processes:

  1. Use the User’s Access Key and Secret Access Key.
  2. Call sts:AssumeRole into Role B with the corresponding MFA device and code.
  3. Use the credentials from the above command to sts:AssumeRole into Role C.

or

  1. Use the User’s Access Key and Secret Access Key.
  2. Call sts:GetSessionToken with the corresponding MFA device and code.
  3. Use the credentials from the above command to sts:AssumeRole into Role B.
  4. Use the credentials from the above command to sts:AssumeRole into Role C.

### Inconsistencies 

#### **AWS Documentation**

Praetorian noticed inconsistent documentation regarding the usage and permission model of sts:GetSessionToken across AWS documentation (as seen in Figure 6). This could lead to application teams misunderstanding and misconfiguring sts:GetSessionToken permissions. In one scenario, Praetorian observed a team unaware of the ability of a MFA-enabled IAM User to chain roles together via CLI and of how sts:GetSessionToken could not be denied via IAM Policy.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20314'%3E%3C/svg%3E)

_Figure 6: Former AWS reference material for sts:GetSessionToken, which AWS has since clarified following our discussions._

One example of clear documentation is the note regarding how IAM Policies interact with the sts:GetCallerIdentity, another sts call that cannot be controlled by IAM Policies (as seen in Figure 7). 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20532%20165'%3E%3C/svg%3E)

_Figure 7: AWS reference material for sts:GetCallerIdentity._

Praetorian worked with AWS to add a similar note to the sts:GetSessionToken documentation (as seen in Figure 8).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20303'%3E%3C/svg%3E)

_Figure 8: Current AWS reference material for sts:GetSessionToken, which AWS clarified following our discussions._

#### **AWS Policy Simulator**

Praetorian often uses the AWS Policy Simulator to test and validate IAM Permissions. While validating the usage of sts:GetSessionToken and sts:AssumeRole, Praetorian noticed that due to inconsistent documentation around sts:GetSessionToken and the way no attached IAM policy can explicitly deny it, the ability to chain an IAM User with MFA to multiple roles could be misunderstood and misconfigured. 

Additionally, Praetorian noticed inconsistent results from the usage of IAM Policy Simulator for sts:GetSessionToken and sts:GetCallerIdentity. The IAM Policy Simulator results for both depend on the IAM policies passed to the simulator (see Figure 8), but they both should always return a permission allowed result. AWS is working on fixing IAM Policy Simulator for both sts:GetCallerIdentity and sts:GetSessionToken.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20519%20268'%3E%3C/svg%3E)

_Figure 9: Incorrect permission result for sts:GetSessionToken and sts:GetCallerIdentity._

## Conclusion

Praetorian and [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) both recommend pivoting away from IAM Users and long-term credentials in favor of IAM Roles and other short-term credentials. If an organization must use IAM Users, Praetorian recommends ensuring remediation of role chaining and other privilege escalation paths.

Note: Praetorian has reached out to AWS Security to report inconsistencies with documentation and behavior of sts:GetSessionToken. Praetorian would like to thank AWS Security for their prompt response, updates, and assistance.

## About the Authors

![Jason Kao](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Jason Kao](https://www.praetorian.com/author/jason-kao/)

Jason is in the Cloud Security Engineering practice, where he works with customers to secure and understand their cloud environments at scale.

[ ](https://www.linkedin.com/in/kaojason/)

## Catch the Latest

Catch our latest exploits, news, articles, and events.

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 19, 2026

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

## [GhostPack Necromancy: Reforging C# Tools with WasmForge](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[ Read More ](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 17, 2026

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

## [FreeBSoD: Leveraging Language Models to Find and Exploit Kernel Bugs (Part 1 of 2)](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[ Read More ](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

  * [Uncategorized](https://www.praetorian.com/category/uncategorized/)

  * June 16, 2026

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## [Sharing is Caring: SMB Secret Scanning with Sulla](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

[ Read More ](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## Ready to Discuss Your Next Continuous Threat Exposure Management Initiative?

Praetorian’s Offense Security Experts are Ready to Answer Your Questions

[ Get Started ](/contact-us/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

##### [Praetorian Guard Platform](https://www.praetorian.com/guard)

  * [ Continuous Threat Exposure Management ](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [ Attack Surface Management ](https://www.praetorian.com/guard/attack-surface-management/)
  * [ Vulnerability Management ](/chariot/vulnerability-management/)
  * [ Cyber Threat Intelligence ](/chariot/threat-intelligence/)
  * [ Continuous Penetration Testing ](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [ Breach and Attack Simulation ](https://www.praetorian.com/guard/breach-attack-simulation/)

##### Professional Services

  * [ AI/ML Penetration Testing ](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [ Application Penetration Testing ](/services/application-penetration-testing/)
  * [ Assumed Breached Exercise ](/services/assumed-breached-exercise/)
  * [ Attack Path Mapping ](https://www.praetorian.com/resources/attack-path-mapping/)
  * [ Automotive Penetration Testing ](/services/automotive-penetration-testing/#)
  * [ CI/CD Security Engagement ](/services/ci-cd-security-engagement/)
  * [ Cloud Penetration Testing ](/services/cloud-penetration-testing/)
  * [ IoT Penetration Testing ](/services/iot-penetration-testing/)
  * [ Network Penetration Testing ](/services/network-penetration-testing/)
  * [ NIST CSF Benchmark ](/services/nist-csf-benchmark/)
  * [ Purple Team ](/services/purple-team/)
  * [ Red Team ](/services/red-team/)

##### Use Cases

  * [ Bug Bounty Cost Reduction ](/services/bug-bounty-cost-reduction/)
  * [ FDA Testing and Monitoring ](/services/fda-testing-monitoring/)
  * [ Mergers and Acquisitions ](/services/mergers-acquisitions/)
  * [ Ransomware Prevention ](/services/ransomware-prevention/)
  * [ Rogue IT Identification ](/services/rogue-it-identification/)
  * [ Tool and Vendor Consolidation ](/services/tool-vendor-consolidation/)
  * [ Vendor Risk Management ](https://www.praetorian.com/services/vendor-risk-management/)

##### Company

  * [ About Us ](https://www.praetorian.com/about-us/)
  * [ Leadership Team ](https://www.praetorian.com/leadership-team/)
  * [ Press Releases ](/news/press-release/)
  * [ In the News ](/news/news)
  * [ Contact Us ](https://www.praetorian.com/contact-us/)
  * [ Resource Library ](https://www.praetorian.com/resources/)
  * [ Security Blog ](/blog/)
  * [ People Ops Blog ](/people-ops/)
  * [ Careers ](https://www.praetorian.com/careers/)
  * [ Culture ](https://www.praetorian.com/work-at-praetorian/)
  * [ Survival Kit ](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)

### Subscribe to our Newsletter

Catch our latest exploits, news, articles, and events.

[Privacy Policy](/privacy-policy/) | [Responsible Disclosure Policy](/responsible-disclosure-policy/) | [Terms of Service](/terms-of-service/) | [Terms and Conditions](/terms/)

Copyright © 2025. All Rights Reserved.

[ Linkedin-in ](https://www.linkedin.com/company/praetorian/) [ X-twitter ](https://twitter.com/praetorianlabs) [ Facebook-f ](https://www.facebook.com/praetorianlabs) [ Github ](https://github.com/praetorian-inc) [ Youtube ](https://www.youtube.com/user/PraetorianLabs)
