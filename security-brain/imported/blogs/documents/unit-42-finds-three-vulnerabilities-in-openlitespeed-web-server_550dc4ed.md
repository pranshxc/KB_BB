---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-10_unit-42-finds-three-vulnerabilities-in-openlitespeed-web-server.md
original_filename: 2022-11-10_unit-42-finds-three-vulnerabilities-in-openlitespeed-web-server.md
title: Unit 42 Finds Three Vulnerabilities in OpenLiteSpeed Web Server
category: documents
detected_topics:
- command-injection
- cloud-security
- path-traversal
- sso
- access-control
- rate-limit
tags:
- imported
- documents
- command-injection
- cloud-security
- path-traversal
- sso
- access-control
- rate-limit
language: en
raw_sha256: 550dc4eda6a3c7a1dadeb5233a969267d32fae4f03de08c6510fdcd744c55950
text_sha256: 23ac1458b2da1fd769dd916bc72a43478fad363fba32f270b205e1130b333991
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Unit 42 Finds Three Vulnerabilities in OpenLiteSpeed Web Server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-10_unit-42-finds-three-vulnerabilities-in-openlitespeed-web-server.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, path-traversal, sso, access-control, rate-limit
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `550dc4eda6a3c7a1dadeb5233a969267d32fae4f03de08c6510fdcd744c55950`
- Text SHA256: `23ac1458b2da1fd769dd916bc72a43478fad363fba32f270b205e1130b333991`


## Content

---
title: "Unit 42 Finds Three Vulnerabilities in OpenLiteSpeed Web Server"
url: "https://unit42.paloaltonetworks.com/openlitespeed-vulnerabilities/"
final_url: "https://unit42.paloaltonetworks.com/openlitespeed-vulnerabilities/"
authors: ["Artur Avetisyan (@3v1LMonk3y)"]
programs: ["LiteSpeed"]
bugs: ["RCE", "OS command injection", "Path traversal", "Local Privilege Escalation"]
publication_date: "2022-11-10"
added_date: "2022-11-17"
source: "pentester.land/writeups.json"
original_index: 1928
---

English

  * [English](https://unit42.paloaltonetworks.com/openlitespeed-vulnerabilities/)
  * [Japanese](https://unit42.paloaltonetworks.com/ja/openlitespeed-vulnerabilities/)

  * [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/ "Vulnerabilities")

[Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)

# Unit 42 Finds Three Vulnerabilities in OpenLiteSpeed Web Server

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 5 min read 

Related Products

[![Advanced Threat Prevention icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced Threat Prevention](https://unit42.paloaltonetworks.com/product-category/advanced-threat-prevention/ "Advanced Threat Prevention")[![Next-Generation Firewall icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Next-Generation Firewall](https://unit42.paloaltonetworks.com/product-category/next-generation-firewall/ "Next-Generation Firewall")[![Prisma Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Cloud](https://unit42.paloaltonetworks.com/product-category/prisma-cloud/ "Prisma Cloud")[![Prisma Cloud WAAS icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Cloud WAAS](https://unit42.paloaltonetworks.com/product-category/prisma-cloud-waas/ "Prisma Cloud WAAS")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
  * [Artur Avetisyan](https://unit42.paloaltonetworks.com/author/artur-avetisyan/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:November 10, 2022

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
  * [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/)
  * [CVE-2022-0072](https://unit42.paloaltonetworks.com/tag/cve-2022-0072/)
  * [CVE-2022-0073](https://unit42.paloaltonetworks.com/tag/cve-2022-0073/)
  * [CVE-2022-0074](https://unit42.paloaltonetworks.com/tag/cve-2022-0074/)
  * [Exploit](https://unit42.paloaltonetworks.com/tag/exploit/)
  * [Openlitespeed](https://unit42.paloaltonetworks.com/tag/openlitespeed/)
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/)
  * [Remote Code Execution](https://unit42.paloaltonetworks.com/tag/remote-code-execution/)
  * [Web server](https://unit42.paloaltonetworks.com/tag/web-server/)

  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/openlitespeed-vulnerabilities/?pdf=download&lg=en&_wpnonce=007ee71b73 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/openlitespeed-vulnerabilities/?pdf=print&lg=en&_wpnonce=007ee71b73 "Click here to print")

Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Unit%2042%20Finds%20Three%20Vulnerabilities%20in%20OpenLiteSpeed%20Web%20Server&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fopenlitespeed-vulnerabilities%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fopenlitespeed-vulnerabilities%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fopenlitespeed-vulnerabilities%2F&title=Unit%2042%20Finds%20Three%20Vulnerabilities%20in%20OpenLiteSpeed%20Web%20Server "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fopenlitespeed-vulnerabilities%2F&text=Unit%2042%20Finds%20Three%20Vulnerabilities%20in%20OpenLiteSpeed%20Web%20Server "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fopenlitespeed-vulnerabilities%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Unit%2042%20Finds%20Three%20Vulnerabilities%20in%20OpenLiteSpeed%20Web%20Server%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fopenlitespeed-vulnerabilities%2F "Share in Mastodon")

## Executive Summary

The Unit 42 research team has researched and discovered three different vulnerabilities in the open source [OpenLiteSpeed Web Server](https://github.com/litespeedtech/openlitespeed). These vulnerabilities also affect the enterprise version, [LiteSpeed Web Server](https://www.litespeedtech.com/). By chaining and exploiting the vulnerabilities, adversaries could compromise the web server and gain fully privileged remote code execution. The vulnerabilities discovered include:

  1. Remote Code Execution ([CVE-2022-0073](https://www.cve.org/CVERecord?id=CVE-2022-0073)) rated High severity (CVSS 8.8)
  2. Privilege Escalation ([CVE-2022-0074](https://www.cve.org/CVERecord?id=CVE-2022-0074)) rated High severity (CVSS 8.8)
  3. Directory Traversal ([CVE-2022-0072](https://www.cve.org/CVERecord?id=CVE-2022-0072)) rated Medium severity (CVSS 5.8)

[OpenLiteSpeed](https://openlitespeed.org/) is the [Open Source edition](https://www.litespeedtech.com/open-source/openlitespeed) of [LiteSpeed Web Server Enterprise](https://www.litespeedtech.com/products/litespeed-web-server), which is developed and maintained by LiteSpeed Technologies. LiteSpeed Web Server is ranked the sixth most popular web server. Analysis from Palo Alto Networks [Cortex Xpanse](https://www.paloaltonetworks.com/cortex/cortex-xpanse) and [Shodan](https://www.shodan.io/) reveals that LiteSpeed serves roughly 2% of all Web Server applications, with nearly 1.9 million unique servers globally.

Unit 42 responsibly disclosed the vulnerabilities to LiteSpeed Technologies with suggested remediation on Oct. 4, 2022. LiteSpeed Technologies swiftly released a patch version ([v1.7.16.1](https://github.com/litespeedtech/openlitespeed/tree/v1.7.16.1)) on Oct. 18, 2022, to mitigate the reported vulnerabilities.

Organizations using OpenLiteSpeed versions 1.5.11 up to 1.7.16 and LiteSpeed versions 5.4.6 up to 6.0.11 are advised to update their software to the latest matching release – v1.7.16.1 and [6.0.12](https://store.litespeedtech.com/store/index.php?rp=/announcements/451).

Palo Alto Networks customers using [Prisma Cloud WAAS](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/waas) or [Next-Generation Firewalls](https://www.paloaltonetworks.com/network-security/next-generation-firewall) with [Advanced ](https://www.paloaltonetworks.com/network-security/advanced-threat-prevention)[Threat Prevention](https://www.paloaltonetworks.com/products/secure-the-network/subscriptions/threat-prevention) receive protection from these vulnerabilities by new rules and signatures that block the attack.

Related Unit 42 Topics | [Containers](https://unit42.paloaltonetworks.com/tag/containers/)  
---|---  
  
## Background

LiteSpeed is a performance-focused web server. According to our findings there are 1.9 million internet facing LiteSpeed Server instances online.

As part of our initiative to contribute to the community to improve security and increase security awareness, we decided to audit OpenLiteSpeed, which is the open source version of the LiteSpeed Web Server.

We tried to imitate the actions of an adversary and engaged in research with the intention of finding vulnerabilities and disclosing them to the vendor. This research has resulted in finding three vulnerabilities that affect both the enterprise and open source solutions. These could be chained and exploited by an adversary who has the credentials for the admin dashboard, in order to gain privileged code execution on vulnerable components.

## Remote Code Execution

_This vulnerability has been assigned the CVE ID of_[ _CVE-2022-0073_](https://www.cve.org/CVERecord?id=CVE-2022-0073) _._

At the first stage of the attack, we tried to gain remote code execution and found that the OpenLiteSpeed Web Server admin dashboard is vulnerable to a command injection vulnerability. A threat actor who managed to gain the credentials to the dashboard, whether by brute force attacks or social engineering, could exploit the vulnerability in order to execute code on the server.

The vulnerability exists in the External App Command field, which allows users to specify a command that will be executed when the server starts.

This functionality is considered dangerous and therefore mitigations for abusing it were implemented. We managed to bypass the mitigations and abuse this functionality to download and execute a malicious file on the server with the privileges of the user [nobody](https://en.wikipedia.org/wiki/Nobody_\(username\)), which is an unprivileged user that traditionally exists in Linux machines.

## Privilege Escalation

_This vulnerability has been assigned the CVE ID of_[ _CVE-2022-0074_](https://www.cve.org/CVERecord?id=CVE-2022-0074) _._

After gaining code execution on the server we wanted to take it a step further and escalate our privileges from nobody to root.

While exploring the OpenLiteSpeed Docker image as nobody, we found a misconfiguration in the PATH environment variable that could be exploited into a privilege escalation using the CWE [untrusted search path](https://cwe.mitre.org/data/definitions/426.html).

When executing a binary with a relative path, the operating system will look at the PATH variable, which contains a list of directories. It will then search for that binary in the listed folders, in the same order that the directories are presented.

The issue in this case was that the second directory in PATH was /usr/local/bin, which is a directory that the user nobody controls.

This leads to a situation where an attacker could execute code as an unprivileged user (such as nobody) to place a malicious file and disguise it as a legitimate binary in /usr/local/bin, with the intention for it to be executed by highly privileged processes because it is in the second directory on the PATH environment variable.

We were able to exploit this by abusing the script entrypoint.sh as shown in Figure 1, which runs as root and executes the binary grep repeatedly.

Figure 1. Entrypoint.sh script showing vulnerable usage of the grep command.

By chaining these vulnerabilities, we were able to gain remote code execution and escalate our privileges to root, as shown in Figure 2.

Figure 2. Proof of successful exploitation.

This vulnerability requires the controlled user to have write permissions to /usr/local/bin, which is usually not the case by default. In the OpenLiteSpeed docker container, this directory is writable by the user nobody by default.

## Directory Traversal

_This vulnerability has been assigned the CVE ID of_[ _CVE-2022-0072_](https://www.cve.org/CVERecord?id=CVE-2022-0072) _._

The last issue we found was a directory traversal vulnerability that could allow an attacker to bypass security measures and access forbidden files. An attacker that compromised the server could create a secret backdoor and exploit the vulnerability to access it.

When browsing in LiteSpeed, the server will make sure that clients only access endpoints that should be visible to them. It does so by verifying that the requested URL does not contain characters that will result in a directory traversal and thus allow them to access forbidden endpoints.

This verification is done by two regular expressions, on lines [2060](https://github.com/litespeedtech/openlitespeed/blob/v1.7.16/src/main/httpserver.cpp#L2060) and [2061](https://github.com/litespeedtech/openlitespeed/blob/v1.7.16/src/main/httpserver.cpp#L2061). We managed to bypass those regular expression verifications, and we were able to access paths that we were not able to access initially.

Exploitation of this vulnerability allows adversaries to access any file in the web root directory, but it is limited only to that directory.

## Mitigations

Unit 42 responsibly disclosed the vulnerabilities to LiteSpeed Technologies with suggested remediation on Oct. 4, 2022. LiteSpeed Technologies has released a patch version [v1.7.16.1](https://github.com/litespeedtech/openlitespeed/tree/v1.7.16.1) for OpenLiteSpeed and[ 6.0.12](https://store.litespeedtech.com/store/index.php?rp=/announcements/451) for LiteSpeed, which addresses the disclosed vulnerabilities.

The command injection mitigation regex that we previously mentioned was [changed](https://github.com/litespeedtech/openlitespeed/blob/v1.7.16.1/dist/admin/html.open/lib/CValidation.php#L565) to include binaries such as curl, fetch and wget to prevent downloading external scripts to mitigate [CVE-2022-0073](https://www.cve.org/CVERecord?id=CVE-2022-0073).

The rewrite condition regexes previously mentioned were [changed](https://github.com/litespeedtech/openlitespeed/blob/v1.7.16.1/src/main/httpserver.cpp#L2060-L2061) in order to mitigate [CVE-2022-0072](https://www.cve.org/CVERecord?id=CVE-2022-0072).

The [ols-dockerfiles](https://github.com/litespeedtech/ols-dockerfiles) repository was [patched](https://github.com/litespeedtech/ols-dockerfiles/blob/master/template/Dockerfile#L29) as well, to set the PATH variable with the user nobody’s controlled path positioned last, preventing binary execution hijacking to mitigate [CVE-2022-0074](https://www.cve.org/CVERecord?id=CVE-2022-0074).

## Conclusion

Web technologies, including web servers, have come a long way in the last few decades. They have become much more secure, but vulnerabilities are still being found as technologies are still evolving at a rapid pace.

As part of the commitment of Palo Alto Networks to advancing cloud security, we actively invest in the public cloud and web application research that includes advanced threat modeling and vulnerability testing of cloud platforms, web servers and related technologies

Palo Alto Networks customers receive protection from this kind of attack through the following products and services:

  1. [Prisma Cloud WAAS](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/waas) customers received a virtual patch designated to mitigate this threat, and they remain protected until patches are applied to vulnerable assets.
  2. [Next-Generation Firewalls](https://www.paloaltonetworks.com/network-security/next-generation-firewall) with [Advanced ](https://www.paloaltonetworks.com/network-security/advanced-threat-prevention)[Threat Prevention](https://www.paloaltonetworks.com/products/secure-the-network/subscriptions/threat-prevention) signatures 93190 and 93191 can block the aforementioned attacks.

We'd like to thank LiteSpeed Technologies for quickly responding and patching the reported issues, and professionally handling the disclosure process.

Palo Alto Networks has shared these findings, including file samples and indicators of compromise, with our fellow Cyber Threat Alliance members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://cyberthreatalliance.org/).

_Updated Nov. 15, 2022, to adjust authorship to focus on the discoverer of the vulnerabilities._

Back to top

### Tags

  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")
  * [CVE-2022-0072](https://unit42.paloaltonetworks.com/tag/cve-2022-0072/ "CVE-2022-0072")
  * [CVE-2022-0073](https://unit42.paloaltonetworks.com/tag/cve-2022-0073/ "CVE-2022-0073")
  * [CVE-2022-0074](https://unit42.paloaltonetworks.com/tag/cve-2022-0074/ "CVE-2022-0074")
  * [Exploit](https://unit42.paloaltonetworks.com/tag/exploit/ "exploit")
  * [Openlitespeed](https://unit42.paloaltonetworks.com/tag/openlitespeed/ "openlitespeed")
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")
  * [Remote Code Execution](https://unit42.paloaltonetworks.com/tag/remote-code-execution/ "Remote Code Execution")
  * [Web server](https://unit42.paloaltonetworks.com/tag/web-server/ "web server")

[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Cobalt Strike Analysis and Tutorial: Identifying Beacon Team Servers in the Wild ](https://unit42.paloaltonetworks.com/cobalt-strike-team-server/ "Cobalt Strike Analysis and Tutorial: Identifying Beacon Team Servers in the Wild")

### Table of Contents

  * 

### Related Articles

  * [ The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "article - table of contents")
  * [ Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution ](https://unit42.paloaltonetworks.com/captive-portal-zero-day/ "article - table of contents")
  * [ Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/ "article - table of contents")

## Related Resources

![Pictorial representation of bucket hijacking technique for cloud data exfiltration. Digital illustration of Europe map highlighting network connections and nodes, depicted as glowing points and lines on a dark blue background, emphasizing major cities and connectivity across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/09_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 22, 2026 #### [The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/)

  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [Bucket hijacking](https://unit42.paloaltonetworks.com/tag/bucket-hijacking/ "bucket hijacking")
  * [Cloud data exfiltration](https://unit42.paloaltonetworks.com/tag/cloud-data-exfiltration/ "cloud data exfiltration")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration")

![Pictorial representation of Vertex AI model uploads. Close-up view of a digital wall displaying various glowing icons, representing a high-tech network interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/AdobeStock_1270203474-1-786x354.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 16, 2026 #### [Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/)

  * [Bucket squatting](https://unit42.paloaltonetworks.com/tag/bucket-squatting/ "bucket squatting")
  * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
  * [Joblib](https://unit42.paloaltonetworks.com/tag/joblib/ "joblib")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/ "Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE")

![Pictorial representation of Cloud Logging services for defense evasion. A vibrant digital illustration depicting a glowing, neon blue cloud symbol positioned over a circuit board landscape. The cloud symbolizes cloud computing technology, and the landscape features intricate electronic circuits with glowing lines and nodes, suggesting high-tech data transfer and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/11_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 9, 2026 #### [Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/ "cloud logging")
  * [Defense evasion](https://unit42.paloaltonetworks.com/tag/defense-evasion/ "defense evasion")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/ "Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility")

![Pictorial representation of PAN-OS CVE-2026-0257. A vibrant city skyline at night, with tall skyscrapers and glowing digital beams extending into the sky, suggesting advanced technology and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/07_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) June 9, 2026 #### [Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257 ](https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/)

  * [CVE-2026-0257](https://unit42.paloaltonetworks.com/tag/cve-2026-0257/ "CVE-2026-0257")
  * [Vulnerability](https://unit42.paloaltonetworks.com/tag/vulnerability/ "vulnerability")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/ "Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257")

![Pictorial representation of ROADtools framework in the cloud. An Asian man wearing glasses sits in front of a computer screen. Reflecting in the glasses are lines indicating analysis. Bright blue city lights illuminate the rest of the image.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/10_Cloud_cybersecurity_research_Overview_1920x900-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) May 22, 2026 #### [Paved With Intent: ROADtools and Nation-State Tactics in the Cloud ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)

  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/ "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud")

![Pictorial representation of CVE-2026-30300. Digital illustration of a map of North America with interconnected glowing lines and dots symbolizing network connections across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/06_Vulnerabilities_1920x900-3-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) May 6, 2026 #### [Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution ](https://unit42.paloaltonetworks.com/captive-portal-zero-day/)

  * [CVE-2026-0300](https://unit42.paloaltonetworks.com/tag/cve-2026-0300/ "CVE-2026-0300")
  * [EarthWorm](https://unit42.paloaltonetworks.com/tag/earthworm/ "EarthWorm")
  * [PAN-OS](https://unit42.paloaltonetworks.com/tag/pan-os/ "PAN-OS")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/captive-portal-zero-day/ "Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution")

![Pictorial representation of a severe Linux vulnerability. Close-up of a woman wearing glasses and focusing intently on a computer screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/05_Vulnerabilities_1920x900-2-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) May 5, 2026 #### [Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/)

  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")
  * [CVE-2026-31431](https://unit42.paloaltonetworks.com/tag/cve-2026-31431/ "CVE-2026-31431")
  * [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/ "Kubernetes")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/ "Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years")

![Pictorial representation of autonomous AI attack in cloud environments. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/12_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 23, 2026 #### [Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/)

  * [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
  * [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
  * [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System")

![Pictorial representation of CVE-2023-33538. Abstract image of a glowing red Wi-Fi symbol on a circuit board, with intricate patterns and a futuristic appearance.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/04_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 16, 2026 #### [A Deep Dive Into Attempted Exploitation of CVE-2023-33538 ](https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/)

  * [Botnet](https://unit42.paloaltonetworks.com/tag/botnet/ "botnet")
  * [Command injection](https://unit42.paloaltonetworks.com/tag/command-injection/ "Command injection")
  * [CVE-2023-33538](https://unit42.paloaltonetworks.com/tag/cve-2023-33538/ "CVE-2023-33538")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/ "A Deep Dive Into Attempted Exploitation of CVE-2023-33538")

![Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) March 23, 2026 #### [Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication/)

  * [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
  * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
  * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image]()
