---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-12_unauthenticated-access-to-gcp-dataproc-can-lead-to-data-leak.md
original_filename: 2023-12-12_unauthenticated-access-to-gcp-dataproc-can-lead-to-data-leak.md
title: Unauthenticated Access to GCP Dataproc Can Lead to Data Leak
category: documents
detected_topics:
- cloud-security
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- cloud-security
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 26f33bca4d63bc4ad61483f8f486828faa18bf3ee23d12e3677d9de81f8f010f
text_sha256: ed95bce4f5c8d09e1933eb0c1627198f63ded521383a546ddc8cdc78edc6483d
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated Access to GCP Dataproc Can Lead to Data Leak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-12_unauthenticated-access-to-gcp-dataproc-can-lead-to-data-leak.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `26f33bca4d63bc4ad61483f8f486828faa18bf3ee23d12e3677d9de81f8f010f`
- Text SHA256: `ed95bce4f5c8d09e1933eb0c1627198f63ded521383a546ddc8cdc78edc6483d`


## Content

---
title: "Unauthenticated Access to GCP Dataproc Can Lead to Data Leak"
page_title: "Unauthenticated Access to GCP Dataproc Can Lead to Data Leak | Orca Security"
url: "https://orca.security/resources/blog/unauthenticated-access-to-google-cloud-dataproc/"
final_url: "https://orca.security/resources/blog/unauthenticated-access-to-google-cloud-dataproc/"
authors: ["Roi Nisimi (@roinisimi)"]
programs: ["Google (GCP)"]
bugs: ["Cloud", "Data leak", "Post-exploitation"]
publication_date: "2023-12-12"
added_date: "2024-01-29"
source: "pentester.land/writeups.json"
original_index: 633
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![Unauthenticated Access to GCP Dataproc Can Lead to Data Leak](https://orca.security/wp-content/uploads/2023/12/Blog-Data-Proc-B-1980px-min.jpg?w=1044)

# Unauthenticated Access to GCP Dataproc Can Lead to Data Leak

[ ![Avatar of Roi Nisimi](https://orca.security/wp-content/uploads/2023/01/roi-nisimi_avatar.png) Roi Nisimi  ](https://orca.security/resources/author/roi-nisimi/)

Published: Dec 12, 2023 

  * [ __](https://twitter.com/share?text=Unauthenticated%20Access%20to%20GCP%20Dataproc%20Can%20Lead%20to%20Data%20Leak&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Funauthenticated-access-to-google-cloud-dataproc%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Funauthenticated-access-to-google-cloud-dataproc%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Funauthenticated-access-to-google-cloud-dataproc%2F)
  * [ __](mailto:?Subject=Unauthenticated Access to GCP Dataproc Can Lead to Data Leak&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Funauthenticated-access-to-google-cloud-dataproc%2F)

The [Orca Research Pod](https://orca.security/about/orca-research-pod/) has made an important discovery that puts Google Cloud Dataproc clusters at risk for data theft, manipulation or loss. This is due to a lack of security controls of the underlying Open Source Software (OSS) managed solution which allows an attacker with knowledge of the Dataproc IP address to access it without any authentication.

Even though Google’s Dataproc [documentation](https://cloud.google.com/dataproc/docs/concepts/accessing/cluster-web-interfaces) highlights this potential security risk and suggests to avoid open firewall rules on a public network, they don’t take into account the risk of an attacker already having an initial foothold on a Compute Engine instance – which would give them unauthenticated access to GCP Dataproc as well.

Orca Security immediately reported the findings to the Google Security Team who labeled the attack flow an ‘Abuse Risk’. However, at the time of this writing, this design flaw has not been fixed. To avoid exposure, it’s up to organizations themselves to ensure that their GCP Dataproc clusters are not configured in a way that makes them vulnerable. 

In light of this, and due to the potential severity of such an attack, Orca decided to highlight this issue and help organizations increase their security posture to protect against this risk. In this blog, we give a detailed breakdown of the attack flow and provide recommendations on how organizations can minimize this risk. 

[Attend Orca’s ‘Ask the Experts’ to Learn More](https://try.orca.security/ask-the-experts.html)

## Executive Summary:

  * Orca Security discovered a potential abuse risk of GCP Dataproc clusters which allows a threat actor to impact sensitive data on the Apache Hadoop Distributed File System (HDFS) when a Compute Engine cluster is part of a public-facing virtual private cloud (VPC), or when the VPC is shared with other Compute Engine instances.
  * GCP includes a default VPC named ‘default’, which doesn’t allow inbound connections on ports other than 22 and 3389, but allows inbound connections from all ports on the internal subnet. This means that sharing a default VPC subnet with both Dataproc clusters and Compute Engine instances could expose a serious security threat which could lead to data corruption or theft.
  * Based on Orca Platform scans, 20% of organizations who use Dataproc have at least one cluster deployed on the default subnet VPC, which means that there’s a considerable chance it is served on the same internal address along with other Compute Engine servers and therefore makes it vulnerable.
  * After reporting the findings, the Google Security team labeled the attack flow as an ‘Abuse Risk’. However, at the time of writing, the design flaw has not been fixed.
  * To help organizations mitigate exposure to the issue, the Orca Cloud Security Platform alerts customers when any Dataproc clusters are misconfigured and vulnerable to this exploitation, along with providing remediation steps and code so that these instances can be remediated quickly.
  * To learn more about this threat, join our [Orca Live ‘Ask the Experts’ ](https://try.orca.security/ask-the-experts.html)on December 14th at 9 am PT, where Roi Nisimi, the Orca threat researcher who discovered the attack path, will be explaining more about how an attacker could gain access to data on a GCP Dataproc server. Roi will also be providing recommendations on how to avoid and mitigate vulnerable configurations.

## What is Google Cloud Dataproc?

Google Cloud [Dataproc](https://cloud.google.com/dataproc/docs/concepts/overview) is a managed cloud service that allows you to run Apache Spark and Apache Hadoop clusters easily and efficiently. It’s designed to handle large-scale data processing and analytics workloads. Hadoop is used for distributed storage and batch processing, while Spark is used for in-memory data processing and analytics.

## The Abuse Risk Overview

The GCP Dataproc threat exploits the following two shortcomings: Lack of security controls in Apache Hadoop’s web interfaces, and the common tendency to keep default settings when creating resources. Together, they enable a dangerous attack scenario which allows an adversary to access any data on the Apache Hadoop Distributed File System (HDFS).

There are two available web interfaces on the master node for every deployed Dataproc cluster: YARN ResourceManager on port 8088 and HDFS NameNode on port 9870. Both are critical to the operation of the entire cluster, and yet both **don’t** require authentication. The more intriguing one is HDFS, since it is the main storage system of the entire cluster. We can see the two ports mentioned above are served for all addresses. Which means to fully access them, the one single prerequisite is internet access. So one, not properly segmented cluster, can cause great damage.

![](https://orca.security/wp-content/uploads/2024/01/image-4.png) ![](https://orca.security/wp-content/uploads/2024/01/image-5.png?w=1200)_HDFS_** _NameNode_** _on port 9870_ ![](https://orca.security/wp-content/uploads/2024/01/image-6.png?w=1200)_YARN_** _ResourceManager_** _on port 8088_

## The GCP Dataproc Attack Flow

Having an internet-facing, Remote Code Execution (RCE) vulnerable Compute Engine instance is not far fetched. As the famous quote goes, “shit happens”, and sometimes we can’t control it, but we should always try to minimize risk as much as possible.

With that being said, the potential attack path we’ll describe in this blog is fairly simple. 

![](https://orca.security/wp-content/uploads/2024/01/image-7.png)

Assuming a vulnerable internet-facing Compute Engine is running in an organization’s cloud environment, it can be fully compromised by an external attacker. Once the attacker can execute commands on the VM instance, they can scan for the same ports described above and hope for the best. If a Dataproc cluster has been deployed on the same VPC, this could turn out to be disastrous, giving the attacker full access to the unauthenticated unauthorized services.

![](https://orca.security/wp-content/uploads/2024/01/image-8.png)

The attacker can now tunnel through the compromised machine to access both web interfaces. They can use the YARN endpoint to create applications, submit jobs and perform Cloud Storage operations, as described [here](https://cloud.google.com/dataproc/docs/concepts/accessing/cluster-web-interfaces#allowed_yarn_resourcemanager_rest_apis). Or worse, they can use the HDFS endpoint to browse through the storage file system and obtain full access to sensitive data.

![](https://orca.security/wp-content/uploads/2024/01/image-9.png?w=1200)

This attack flow isn’t limited to a vulnerable Compute Engine. Any deployed workload, such as [Cloud Run](https://cloud.google.com/run?hl=en) or [AppEngine](https://cloud.google.com/appengine?hl=en), on the same VPC network as the Hadoop’s master node can lead to the HDFS data. If possessed, it can serve attackers the same way that is described above.

## Recommendations

Below, we list a number of best practices that organizations can follow to decrease their risk of these types of threats, as well as very specific alerting by the Orca Platform when it detects vulnerable configurations.

### Network Segmentation

In general, it’s always important to be aware of the default settings, and not just accept them as they are. Decide which settings best suit your organization’s needs and security requirements, and which don’t. In the context of Dataproc, we recommend creating a dedicated VPC network and configuring the firewall rules as needed, prior to deploying any new clusters. Then, to limit lateral movement and avoid one cluster’s security issue affecting all others, deploy independent clusters in different subnets of the same VPC. Also, avoid deploying any other service on these dedicated networks, other than the required cluster components.

### Vulnerability Management 

With consistent vulnerability and patch management, organizations can minimize the possibility of a bad actor entering their cloud environment. Being able to view all vulnerable assets throughout all cloud accounts is a huge advantage that aids in the process of not only eliminating this attack flow scenario, but also many others. Using a [vulnerability management](https://orca.security/platform/vulnerability-management/) platform such as Orca, is essential to ensure that any vulnerabilities are detected and remediated, and unpatched servers and applications are brought to your attention.

### Be Alerted to GCP Dataproc Misconfigurations

After making this discovery, the Orca Platform now identifies Dataproc clusters that are misconfigured and deployed on a default VPC. To mitigate this issue, security teams can edit the firewall rules accordingly, or migrate their cluster to a different VPC.

![](https://orca.security/wp-content/uploads/2024/01/image-10.png?w=1200)_Orca detects a vulnerable Dataproc clusters and provides remediation steps and code_

## Key Takeaways

The origin of this security issue is a non security-oriented OSS project. It is very common in cloud computing, among all other vendors, to abstract the complexity and manage the setup of a popular Open Source project. The cloud vendor adjusts the project to the best of its abilities, usually to allow integration with other cloud resources, but the core will usually stay the same. And if the core is missing security controls, users should be extremely careful.

Most likely there will be no authentication added to the web-interfaces mentioned above. Google warns in its documentation about the risk, but sometimes it can be overlooked or not well understood. It’s within the [shared responsibility](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) model to know and understand the risk and not misuse services in a way that endangers your organization’s crown jewels.

## About the Orca Cloud Security Platform

Orca’s agentless-first Cloud Security Platform connects to your environment in minutes and provides 100% visibility into all your assets on AWS, Azure, Google Cloud, Alibaba Cloud, Oracle Cloud, and Kubernetes, automatically including new assets as they are added. Orca detects and prioritizes cloud risks across every layer of your cloud estate, including vulnerabilities, malware, misconfigurations, lateral movement risk, API risks, weak and leaked passwords, sensitive data at risk, and overly permissive identities.  
To learn more about this risk and how to protect against it, join our [Orca Live ‘Ask the Experts’](https://try.orca.security/ask-the-experts.html) on December 14th at 9 am PT.

  * [ __](https://twitter.com/share?text=Unauthenticated%20Access%20to%20GCP%20Dataproc%20Can%20Lead%20to%20Data%20Leak&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Funauthenticated-access-to-google-cloud-dataproc%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Funauthenticated-access-to-google-cloud-dataproc%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Funauthenticated-access-to-google-cloud-dataproc%2F)
  * [ __](mailto:?Subject=Unauthenticated Access to GCP Dataproc Can Lead to Data Leak&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Funauthenticated-access-to-google-cloud-dataproc%2F)

## Related articles

[ ![Risk-based Vulnerability Management](https://orca.security/wp-content/uploads/2025/02/orca-blog-risk-prioritization-featured.png?w=750) ](/resources/blog/risk-based-vulnerability-management/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Product Info

##  [Risk-Based Vulnerability Management for the Cloud: A 2026 Guide](/resources/blog/risk-based-vulnerability-management/ "Risk-Based Vulnerability Management for the Cloud: A 2026 Guide")

Jun 26, 2026 

[ ![Digital illustration of a data center cross-section showing an adversarial path indicated by glowing red arrows originating from a breached, orange-lit server rack and moving laterally toward a secured, cyan-lit server enclosure with a locked terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-private-cloud-security-1.png?w=750) ](/resources/blog/private-cloud-security/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [Private Cloud Security: Top Risks and Best Practices (2026)](/resources/blog/private-cloud-security/ "Private Cloud Security: Top Risks and Best Practices \(2026\)")

Jun 26, 2026 

[ ![Digital illustration of a central AI microchip on a cloudy background, processing threats from the left—such as a cracked message bubble and a bug icon—and outputting cybersecurity solutions on the right, including prioritized alert windows and a remediation code terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-what-is-generative-ai-in-cybersecurity-1.png?w=750) ](/resources/blog/what-is-generative-ai-in-cybersecurity/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [What Is Generative AI in Cybersecurity?](/resources/blog/what-is-generative-ai-in-cybersecurity/ "What Is Generative AI in Cybersecurity?")

Jun 25, 2026 

### Stay in the loop

Keep up to date with everything you need to know about cloud security and our latest research

By submitting my email address I agree to the use of my personal data in accordance with Orca Security [ Privacy Policy](https://orca.security/privacy-policy/).
