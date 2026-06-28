---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-19_awss-log4shell-hot-patch-vulnerable-to-container-escape-and-privilege-escalation.md
original_filename: 2022-04-19_awss-log4shell-hot-patch-vulnerable-to-container-escape-and-privilege-escalation.md
title: AWS's Log4Shell Hot Patch Vulnerable to Container Escape and Privilege Escalation
category: documents
detected_topics:
- command-injection
- cloud-security
- supply-chain
- sso
- access-control
- mfa
tags:
- imported
- documents
- command-injection
- cloud-security
- supply-chain
- sso
- access-control
- mfa
language: en
raw_sha256: ddb2a78e80e1543625427616c824e438d1d5c2fe6e013e0e0db362f93f9ccb79
text_sha256: e211c5946a00f6444b7093e0b4de5e7e6f5025a0c9dcd6c68cf5f4402d210592
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# AWS's Log4Shell Hot Patch Vulnerable to Container Escape and Privilege Escalation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-19_awss-log4shell-hot-patch-vulnerable-to-container-escape-and-privilege-escalation.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, supply-chain, sso, access-control, mfa
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `ddb2a78e80e1543625427616c824e438d1d5c2fe6e013e0e0db362f93f9ccb79`
- Text SHA256: `e211c5946a00f6444b7093e0b4de5e7e6f5025a0c9dcd6c68cf5f4402d210592`


## Content

---
title: "AWS's Log4Shell Hot Patch Vulnerable to Container Escape and Privilege Escalation"
url: "https://unit42.paloaltonetworks.com/aws-log4shell-hot-patch-vulnerabilities/"
final_url: "https://unit42.paloaltonetworks.com/aws-log4shell-hot-patch-vulnerabilities/"
authors: ["Unit 42 (@Unit42_Intel)"]
programs: ["AWS"]
bugs: ["Privilege escalation", "Container escape"]
publication_date: "2022-04-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2697
---

English

  * [English](https://unit42.paloaltonetworks.com/aws-log4shell-hot-patch-vulnerabilities/)
  * [Japanese](https://unit42.paloaltonetworks.com/ja/aws-log4shell-hot-patch-vulnerabilities/)

  * [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")

[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)

# AWS's Log4Shell Hot Patch Vulnerable to Container Escape and Privilege Escalation

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 7 min read 

Related Products

[![Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Next-Generation Firewall icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Next-Generation Firewall](https://unit42.paloaltonetworks.com/product-category/next-generation-firewall/ "Next-Generation Firewall")[![Prisma Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Cloud](https://unit42.paloaltonetworks.com/product-category/prisma-cloud/ "Prisma Cloud")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
  * [Yuval Avrahami](https://unit42.paloaltonetworks.com/author/yuval-avrahami/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:April 19, 2022

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
  * [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
  * [Apache Log4j](https://unit42.paloaltonetworks.com/tag/apache-log4j/)
  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/)
  * [Container escape](https://unit42.paloaltonetworks.com/tag/container-escape/)
  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/)
  * [CVE-2021-3100](https://unit42.paloaltonetworks.com/tag/cve-2021-3100/)
  * [CVE-2021-3101](https://unit42.paloaltonetworks.com/tag/cve-2021-3101/)
  * [CVE-2021-44228](https://unit42.paloaltonetworks.com/tag/cve-2021-44228/)
  * [CVE-2022-0070](https://unit42.paloaltonetworks.com/tag/cve-2022-0070/)
  * [CVE-2022-0071](https://unit42.paloaltonetworks.com/tag/cve-2022-0071/)
  * [Log4j](https://unit42.paloaltonetworks.com/tag/log4j/)
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/)

  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/aws-log4shell-hot-patch-vulnerabilities/?pdf=download&lg=en&_wpnonce=007ee71b73 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/aws-log4shell-hot-patch-vulnerabilities/?pdf=print&lg=en&_wpnonce=007ee71b73 "Click here to print")

Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=AWS's%20Log4Shell%20Hot%20Patch%20Vulnerable%20to%20Container%20Escape%20and%20Privilege%20Escalation&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Faws-log4shell-hot-patch-vulnerabilities%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Faws-log4shell-hot-patch-vulnerabilities%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Faws-log4shell-hot-patch-vulnerabilities%2F&title=AWS's%20Log4Shell%20Hot%20Patch%20Vulnerable%20to%20Container%20Escape%20and%20Privilege%20Escalation "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Faws-log4shell-hot-patch-vulnerabilities%2F&text=AWS's%20Log4Shell%20Hot%20Patch%20Vulnerable%20to%20Container%20Escape%20and%20Privilege%20Escalation "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Faws-log4shell-hot-patch-vulnerabilities%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=AWS's%20Log4Shell%20Hot%20Patch%20Vulnerable%20to%20Container%20Escape%20and%20Privilege%20Escalation%20https%3A%2F%2Funit42.paloaltonetworks.com%2Faws-log4shell-hot-patch-vulnerabilities%2F "Share in Mastodon")

## **Executive Summary**

Following [Log4Shell](https://unit42.paloaltonetworks.com/apache-log4j-vulnerability-cve-2021-44228/), AWS released several [hot patch solutions](https://alas.aws.amazon.com/announcements/2021-001.html) that monitor for vulnerable Java applications and Java [containers](https://aws.amazon.com/blogs/containers/advice-on-mitigating-the-apache-log4j-security-issue-for-eks-ecs-and-fargate-customers/) and patch them on the fly. Each solution suits a different environment, covering standalone servers, Kubernetes clusters, Elastic Container Service (ECS) clusters and Fargate. The hot patches aren't exclusive to AWS environments and can be installed onto any cloud or on-premises environment.

Unit 42 researchers identified severe security issues within these patching solutions and partnered with AWS to remediate them. After installing the patch service to a server or cluster, every container in that environment can exploit it to take over its underlying host. For example, if you [installed the hot patch to a Kubernetes cluster](https://github.com/aws-samples/kubernetes-log4j-cve-2021-44228-node-agent), every container in your cluster can now escape until you either disable the hot patch or upgrade to the fixed version. Aside from containers, unprivileged processes can also exploit the patch to escalate privileges and gain root code execution.

Containers can escape regardless of whether they run Java applications, or whether their underlying host runs [Bottlerocket](https://aws.amazon.com/bottlerocket/), AWS's hardened Linux distribution for containers. Containers running with [user namespaces](https://docs.docker.com/engine/security/userns-remap/) or as a non-root user are affected as well. Unit 42 assigned CVE-2021-3100, CVE-2021-3101, CVE-2022-0070 and CVE-2022-0071 to track the vulnerabilities.

AWS released a fixed version for each hot patch solution on April 19:

  1. Version 1.1-16 of the log4j-cve-2021-44228-hotpatch [package](https://alas.aws.amazon.com/announcements/2021-001.html), which bundles the hot patch service.
  2. Version 1.1-16 of the kubernetes-log4j-cve-2021-44228-node-agent [Daemonset](https://github.com/aws-samples/kubernetes-log4j-cve-2021-44228-node-agent), which installs the updated package.
  3. Version 1.02 of [Hotdog](https://github.com/bottlerocket-os/hotdog), a hot patch solution for Bottlerocket hosts based on Open Container Initiative (OCI) hooks.

Unit 42 advises anyone who installed any of these hot patches to upgrade to a fixed version. Note that starting from Dec. 17, 2021, JDK packages (Java installations) on Amazon Linux [automatically installed](https://alas.aws.amazon.com/announcements/2021-001.html) the log4j-cve-2021-44228-hotpatch package. Alternatively, users who are confident their applications are patched against Log4Shell can disable the hot patch service following the instructions in the Mitigations section below.

[Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) detects the hot patch package and will alert on hosts running a vulnerable version.

CVEs Assigned | CVE-2021-3100, CVE-2021-3101, CVE-2022-0070, CVE-2022-0071  
---|---  
Related Unit 42 topics | [Container escape](https://unit42.paloaltonetworks.com/tag/containers/), [privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/), [cloud](https://unit42.paloaltonetworks.com/category/cloud/), [Apache log4j](https://unit42.paloaltonetworks.com/tag/apache-log4j-2/)  
  
## **Overview of AWS Log4Shell Hot Patches**

Log4Shell proved itself as one of the worst vulnerabilities of recent times. To help users combat the issue at scale, AWS open-sourced several hot patch solutions, each covering a different environment. Hot patching is the process of injecting a fix to a vulnerable running application. It's meant to serve as a short-term solution until a new, fixed version of the application can be deployed.

AWS released three hot patching solutions that detect processes and containers running vulnerable Java applications and patch them on the fly:

  1. A [hot patch service](https://alas.aws.amazon.com/announcements/2021-001.html) bundled in an RPM package. Starting from Dec. 17, 2021, this service is automatically installed with Amazon Linux JDK (Java) packages. Fargate customers could've asked for this service to be installed on the hosts running their containers.
  2. A [hot patch Daemonset](https://github.com/aws-samples/kubernetes-log4j-cve-2021-44228-node-agent) for Kubernetes clusters, which installs the aforementioned hot patch service on all nodes.
  3. [Hotdog](https://github.com/bottlerocket-os/hotdog), a hot patch solution bundled as a set of OCI hooks. Hotdog is primarily intended for Bottlerocket hosts.

These solutions cover most compute environments, from Kubernetes clusters to ECS clusters, Fargate containers and standalone servers. They aren't exclusive to AWS environments, and can be installed onto other cloud environments or on-premises.

Unit 42 researchers discovered these patches can be exploited for container escape and privilege escalation. After any one of the patches is installed to a host or cluster, new containers can exploit the patch to escape and compromise their underlying host. On hosts that installed either the hot patch service or the hot patch Daemonset, existing containers can escape as well. Aside from containers, unprivileged processes can also exploit the patch service to escalate privileges and gain root code execution. AWS has now mitigated these vulnerabilities and released a fix for each solution.

## **Root Cause Analysis**

AWS's hot patch solutions continuously search for Java processes and patch them against Log4Shell on the fly. Any process running a binary named “java“ – inside or outside of a container – is considered a candidate for the hot patch.

To patch Java processes inside containers, the hot patch solutions invoke certain container binaries. For example, they run the container's "java" binary twice: once to retrieve the Java version, and again to inject the hot patch. The issue was that they invoked container binaries without properly containerizing them. That is, the new processes would run without the limitations normally applied to container processes.

For example, the "java" binary was invoked in the container namespaces via the [nsenter](https://man7.org/linux/man-pages/man1/nsenter.1.html) command (excluding the user namespace). But aside from that, it was spawned with all [Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html), and without the [isolation technologies that normally confine containers](https://opensource.com/article/21/8/container-linux-technology), such as [seccomp](https://man7.org/linux/man-pages/man2/seccomp.2.html) and [cgroups](https://man7.org/linux/man-pages/man7/cgroups.7.html). It also ran as the root user regardless of the container's user.

A malicious container therefore could have included a malicious binary named “java” to trick the installed hot patch solution into invoking it with elevated privileges. The malicious “java” process could then abuse its elevated privileges to escape the container and take over the underlying host. The fixed hot patch solutions now properly containerize container binaires before running them.

Aside from containers, the hot patch service also patched host processes in a similar manner. A malicious unprivileged process could have created and run a malicious binary named "java" to trick the hot patch service into executing it with elevated privileges. The fixed hot patch service now spawns “java” binaries with the same privileges as the Java process being patched.

## **Container Escape Demo**

To verify the vulnerability is exploitable, we built a proof of concept (PoC) container image. When deployed to a cluster or VM that runs a vulnerable version of a hot patch solution, the container exploits the vulnerabilities to escape and gain root code execution on the underlying host. It then sends a [reverse shell](https://docs.paloaltonetworks.com/prisma/prisma-cloud/20-12/prisma-cloud-compute-edition-admin/runtime_defense/incident_types/reverse_shell.html) to an attacker-controlled server.

In the demo video below, a user installed the hot patch Daemonset to an EKS cluster. The demo then simulates a supply chain attack by showing what happens when the user inadvertently runs a malicious container image that exploits the hot patch.

_Video 1. CVE-2021-3100 exploit demo._

While the demo showcases a supply chain attack, existing containers that were compromised (e.g. by a network payload) can also exploit the issues to escape and take over their underlying host. We've decided not to share the exploit's implementation details at this time to prevent malicious parties from weaponizing it.

## **Impact**

Given the urgency surrounding Log4Shell, users may have deployed hot patches at scale, inadvertently putting container environments at risk. Even after Java applications were patched against Log4Shell, users may have kept the hot patch running for defense-in-depth as there isn't a strong incentive to remove it.

Containers are often used as a security boundary between applications running on the same machine. A container escape allows an attacker to extend a campaign beyond a single application and compromise neighboring services. In Kubernetes clusters, a single container escape is unfortunately sometimes enough to take over the entire cluster.

The issues are exploitable regardless of the container configuration, so even environments that enable advanced isolation techniques like running containers in [user namespaces](https://docs.docker.com/engine/security/userns-remap/) or as a non-root user are affected.

Aside from containers, unprivileged processes could have also exploited the vulnerabilities to escalate privileges and gain full control over their underlying server.

## **Mitigations**

AWS released a fix for each hot patch solution. Once a host runs a fixed version, container escape and privilege escalation are no longer possible.

  1. In Kubernetes clusters, you can install the fixed hot patch version by deploying the [latest Daemonset](https://github.com/aws-samples/kubernetes-log4j-cve-2021-44228-node-agent) provided by AWS. Note that only deleting the hot patch Daemonset doesn't remove the hot patch service from your nodes. **Updated April 25** : Currently, there isn't a fixed Daemonset version for Debian-based hosts (Debian and Ubuntu). See this [GitHub thread](https://github.com/aws-samples/kubernetes-log4j-cve-2021-44228-node-agent/commit/cacdf35d40a3f1da84dac6aae9e807ac1b2c9d4f#commitcomment-72082620) for more details. **Updated May 5** : A fixed Daemonset version for Debian-based hosts was released. Note that the fixed version for the Debian log4j-cve-2021-44228-hotpatch package is **1.1.17**.
  2. On standalone hosts, you can upgrade by running yum update log4j-cve-2021-44228-hotpatch.
  3. Hotdog users need to upgrade to the [latest version](https://github.com/bottlerocket-os/hotdog/releases).

Alternatively, if you're confident that your environment is patched against Log4Shell, you can disable the hot patch service on a host by running sudo touch /etc/log4j-cve-2021-44228-hotpatch.kill. To disable Hotdog, run apiclient set oci-hooks.log4j-hotpatch-enabled=false.

Prisma Cloud customers can identify affected hosts under the Vulnerabilities tab. The platform detects the hot patch packages and alerts customers on VMs running a vulnerable version. To search for the vulnerabilities, use the Amazon Linux Security Advisories (ALAS) IDs associated with them: ALAS-2021-1554, ALAS-2021-1732, ALAS-2022-1580 and ALAS-2022-1773.

Figure 1. Prisma Cloud detects and alerts on vulnerable log4j-cve-2021-44228-hotpatch versions.

Palo Alto Networks [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud), [Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr) and [Next-Generation Firewalls](https://www.paloaltonetworks.com/network-security/next-generation-firewall) (NGFWs) can detect follow-on attacker activities and disrupt command and control communications like the reverse shell used in the demo.

## **Safely Interacting With Containers**

CVE-2021-3100, CVE-2021-3101, CVE-2022-0070 and CVE-2022-0071 add to a long list of container escape vulnerabilities that arise from a host process directly interacting with a running container. Simple tasks like copying files or spawning a new containerized process can have surprising outcomes when the container is malicious.

If you're building software around containers, defer to an established container runtime like [runc](https://github.com/opencontainers/runc) for operations involving a container's processes or filesystem. Although they have also had their share of vulnerabilities, container runtimes are by far the most vetted and mature programs for safely interacting with containers.

## **Conclusion**

Given the urgency surrounding Log4Shell, users may have deployed hot patches at scale, inadvertently putting container environments at risk. We encourage users to upgrade to the fixed hot patch version as soon as possible. Multitenant container environments and clusters running untrusted images are especially at risk.

If you're still patching against Log4Shell, prioritize that effort first. While the presented issues can lead to severe attacks against container environments, Log4Shell has rightfully earned its spot as one of the worst vulnerabilities of all time and is still being actively exploited.

We'd like to thank AWS for their partnership and coordination in remediating this vulnerability efficiently. As Log4Shell exploitation peaked, AWS's hot patch helped the community stop countless attacks. With these vulnerabilities fixed, it's now possible to use the hot patch to address Log4Shell while also keeping container environments secure.

## **Additional Resources**

  * [Unit 42 analysis of Log4Shell ](https://unit42.paloaltonetworks.com/apache-log4j-vulnerability-cve-2021-44228/)
  * [AWS advice on mitigating Log4Shell in container enviroments](https://aws.amazon.com/blogs/containers/advice-on-mitigating-the-apache-log4j-security-issue-for-eks-ecs-and-fargate-customers/)
  * [Prisma Cloud Mitigations for Log4Shell](https://www.paloaltonetworks.com/blog/prisma-cloud/log-4-shell-vulnerability/)

## **Disclosure Timeline**

  * **Dec. 14:** AWS releases hot patch package with support for containers.
  * **Dec. 20** : Unit 42 researchers identify the issue.
  * **Dec. 21** : Advisory sent to AWS.
  * **Dec. 22** : AWS acknowledges the issue.
  * **Dec. 23** : AWS releases fixes and advisories for affected components.
  * **Dec. 27** : Unit 42 reports bypasses for the initial fixes to AWS.
  * **Feb. 9** : Unit 42 researchers meet with AWS security to discuss fixes.
  * **April 1** : AWS shares fixed versions for Unit 42 review.
  * **April 4** : Unit 42 points out a few remaining issues.
  * **April 19** : AWS releases final fixes and advisories; Unit 42 discloses the vulnerabilities publicly.

_Updated May 5, 2022, at 11:10 a.m. PT._

Back to top

### Tags

  * [Apache Log4j](https://unit42.paloaltonetworks.com/tag/apache-log4j/ "Apache Log4j")
  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [Container escape](https://unit42.paloaltonetworks.com/tag/container-escape/ "container escape")
  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")
  * [CVE-2021-3100](https://unit42.paloaltonetworks.com/tag/cve-2021-3100/ "CVE-2021-3100")
  * [CVE-2021-3101](https://unit42.paloaltonetworks.com/tag/cve-2021-3101/ "CVE-2021-3101")
  * [CVE-2021-44228](https://unit42.paloaltonetworks.com/tag/cve-2021-44228/ "CVE-2021-44228")
  * [CVE-2022-0070](https://unit42.paloaltonetworks.com/tag/cve-2022-0070/ "CVE-2022-0070")
  * [CVE-2022-0071](https://unit42.paloaltonetworks.com/tag/cve-2022-0071/ "CVE-2022-0071")
  * [Log4j](https://unit42.paloaltonetworks.com/tag/log4j/ "log4j")
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")

[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Gaining Visibility Within Container Clusters ](https://unit42.paloaltonetworks.com/visibility-k8s-clusters/ "Gaining Visibility Within Container Clusters")

### Table of Contents

  * 

### Related Articles

  * [ The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "article - table of contents")
  * [ Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/ "article - table of contents")
  * [ Cracks in the Bedrock: Agent God Mode ](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/ "article - table of contents")

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
