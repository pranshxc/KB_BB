---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-14_microsoft-defender-for-cloud-management-port-exposure-confusion.md
original_filename: 2023-03-14_microsoft-defender-for-cloud-management-port-exposure-confusion.md
title: Microsoft Defender for Cloud Management Port Exposure Confusion
category: documents
detected_topics:
- cloud-security
- sso
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- cloud-security
- sso
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: a65096dd9cac6fb287e01112547a24522b9e6db7d127da29fd66d99c67f34a8b
text_sha256: 59f3ed20e5d8e99e3c7a68fbc4f98374930a09396586a738c66526bc08802ed9
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Defender for Cloud Management Port Exposure Confusion

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-14_microsoft-defender-for-cloud-management-port-exposure-confusion.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `a65096dd9cac6fb287e01112547a24522b9e6db7d127da29fd66d99c67f34a8b`
- Text SHA256: `59f3ed20e5d8e99e3c7a68fbc4f98374930a09396586a738c66526bc08802ed9`


## Content

---
title: "Microsoft Defender for Cloud Management Port Exposure Confusion"
page_title: "Microsoft Defender for Cloud Management Port Exposure Confusion | Rapid7 Blog"
url: "https://www.rapid7.com/blog/post/2023/03/14/microsoft-defender-for-cloud-management-port-exposure-confusion/"
final_url: "https://www.rapid7.com/blog/post/2023/03/14/microsoft-defender-for-cloud-management-port-exposure-confusion/"
authors: ["Aaron Sawitsky"]
programs: ["Microsoft"]
bugs: ["Cloud", "Security misconfiguration"]
publication_date: "2023-03-14"
added_date: "2023-03-15"
source: "pentester.land/writeups.json"
original_index: 1383
---

Prior to March 9, 2023, Microsoft Defender for Cloud incorrectly marked some Azure virtual machines as having secured management ports including SSH (port 22/TCP), RDP (port 3389/TCP) and WINRM (port 5985/TCP), when in fact one or more of these ports were exposed to the internet. This occured when the Network Security Group (NSG) associated with the virtual machine contained a rule that allowed access to one of these ports from the IPv4 range “0.0.0.0/0”. Defender for Cloud would only detect an open management port if the source in the port rule is set to the literal alias of “Any”. Although the CIDR-notated network of "/0" is often treated as synonymous with "Any," they are not equivalent in Defender for Cloud's logic.

Note that as of this writing, the same issue appears when using the IPv6 range “::/0” as a synonym for "any" and Microsoft has not yet fixed this version of the vulnerability.

## Product Description

Microsoft Defender for Cloud is a cloud security posture management (CSPM) solution that provides several security capabilities, including the ability to detect misconfigurations in Azure and multi-cloud environments. Defender for Cloud is described in detail at the [vendor's website](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction).

Security groups are a concept that exists in both Azure and Amazon Web Services (AWS) cloud environments. Similar to a firewall, a security group allows you to create rules that limit what IP addresses/ranges can access which ports on one or more virtual machines in the cloud environment.

## Credit

This issue was discovered by Aaron Sawitsky, Senior Manager for Cloud Product Integrations at Rapid7. It is being disclosed in accordance with [Rapid7's vulnerability disclosure policy](/security/disclosure/).

## Exploitation

If an Azure Virtual Machine is associated with a Network Security Group with “management ports” such as RDP (Remote Desktop Protocol on port 3389/TCP) or SSH (Secure Shell protocol on port 22/TCP) exposed to the "Any" pseudo-class for "Source," Microsoft Defender for Cloud will create a security recommendation to highlight that the management port is open to the internet, which allows an administrator to easily recognize that there is a virtual machine in their environment with one or more over-exposed server management ports.

However, prior to March 9th, if the Network Security Group was instead configured such that a “management port” like RDP or SSH was exposed to “0.0.0.0/0,” as a source (which is the entire IPv4 range of all possible addresses) no security recommendation was created and the configuration was incorrectly marked as “Healthy.”

The effect is demonstrated in the screenshots below:

![image1.png](https://www.rapid7.com/cdn/images/blt8b34b6cc039692d3/683de30e6b437ba51f4fa6d5/image1.png) ![image2.jpg](https://www.rapid7.com/cdn/images/blt02f236d7bf24e638/683de339ca9dfcf667526742/image2.jpg)

Because of this network scope confusion, Azure users can easily and accidentally expose management ports to the entire internet and evade detection by Defender for Cloud.

We suspect that other Defender for Cloud features that check for the "any-ness" of ingress tests are similarly affected, but we have not comprehensively tested for other manifestations of this issue.

## Impact

We can imagine two cases where this unexpected behavior in Defender for Cloud could be useful for attackers. First, it's likely that administrators are unaware of any practical semantic difference between "Any" and "0.0.0.0/0" or “::/0” since these terms are often used interchangeably in other networking products, most notably, as when configuring AWS Security Groups. As a result, this misconfiguration could be accidentally applied by a legitimate administrator, but remain undetected by the person or process responsible for monitoring Defender for Cloud security recommendations. This is the most likely scenario most administrators will face.

More maliciously, an attacker who has already compromised a virtual Azure-hosted machine could leverage this confusion to avoid post-exploit detection by the Defender for Cloud. This makes repeated, post-exploit access from several different sources much easier for more sophisticated attackers. In this case, the "attacker" will often be an insider who is merely subverting their own IT security organization for ostensibly virtuous, just-get-it-done reasons, such as testing a configuration in production, but forgetting to re-limit the exposure.

Note that more exotic combinations of subnets could be used to achieve the same effect; for example, an administrator could define "0.0.0.0/1" and "128.0.0.1/1" which would have exactly the same effect as one "0.0.0.0/0" source rule. Or, even more cleverly, define a set of subnets that adds up to "almost any," which would be good enough for a thoughtful attacker to ensure continued, un-alerted exposure. However, this kind of configuration is extremely unlikely to be implemented by accident (as described in the first case), and thus, is almost certainly beyond the reasonable scope of the Defender for Cloud use case. After all, Defender for Cloud is designed to catch common misconfigurations, and not necessarily an intentionally confusing configuration.

## Remediation

Since Defender for Cloud is a cloud-based solution, users should not have to do anything special to enjoy the benefits of Microsoft's update. With that said, customers should remember that the update has not resolved the issue when using the IPV6 range ::/0 as a synonym for “any.” As a result, customers should search their Azure environments for any Security Groups configured to allow ingress from a source of “::/0” and seriously consider reconfiguring these rules to be more restrictive. In addition, customers should regularly subject their cloud infrastructure to auditing and penetration tests to verify that their CSPM is actually catching common misconfigurations. We have already validated that this issue does not impact Rapid7’s InsightCloudSec CSPM solution. In addition, Defender for Cloud customers who have previously used the "/0" CIDR notation in their security group rules should review access logs to ensure that malicious actors were not evading the presumed detection capabilities provided by Defender for Cloud.

## Disclosure Timeline

January 2023: Issue discovered by Rapid7 cloud security researcher [Aaron Sawitsky](https://www.linkedin.com/in/aaronsawitsky/)  
Wed, Jan 11, 2023: Initial disclosure to Microsoft  
Thu, Jan 12, 2023: Details explained further and validated by the vendor  
Mon, Feb 6, 2023: Fix planned by the vendor  
Thu, Mar 9, 2023: Fix for "0.0.0.0/0" confirmed by Rapid7  
Tue, Mar 14, 2023: This disclosure

[![LinkedIn](/linkedin-logo.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2023%2F03%2F14%2Fmicrosoft-defender-for-cloud-management-port-exposure-confusion&title=Microsoft%20Defender%20for%20Cloud%20Management%20Port%20Exposure%20Confusion)[![Facebook](/facebook-logo.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2023%2F03%2F14%2Fmicrosoft-defender-for-cloud-management-port-exposure-confusion)[![X](/x-logo.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2023%2F03%2F14%2Fmicrosoft-defender-for-cloud-management-port-exposure-confusion&text=Microsoft%20Defender%20for%20Cloud%20Management%20Port%20Exposure%20Confusion)[![Bluesky](/bluesky-dark-logo.svg)](https://bsky.app/intent/compose?text=Microsoft%20Defender%20for%20Cloud%20Management%20Port%20Exposure%20Confusion%20https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2023%2F03%2F14%2Fmicrosoft-defender-for-cloud-management-port-exposure-confusion)

#### Article Tags

  * [Vulnerability Disclosure](/blog/tag/vulnerability-disclosure/)
  * [Cloud Security](/blog/tag/cloud-security/)

[![Tod Beardsley](/_next/image/?url=https%3A%2F%2Fwww.rapid7.com%2Fcdn%2Fimages%2Fblt6cf094a2ceec5340%2F68404474afd14d7c456286fa%2FTod-Beardsley.jpg&w=256&q=75)Tod BeardsleyAuthor Posts](/blog/author/tod-beardsley/)
