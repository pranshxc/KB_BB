---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-24_how-the-sysall-loophole-allowed-us-to-penetrate-gke-clusters-in-production.md
original_filename: 2024-01-24_how-the-sysall-loophole-allowed-us-to-penetrate-gke-clusters-in-production.md
title: How the Sys:All Loophole Allowed Us To Penetrate GKE Clusters in Production
category: documents
detected_topics:
- cloud-security
- access-control
- oauth
- sso
- jwt
- xss
tags:
- imported
- documents
- cloud-security
- access-control
- oauth
- sso
- jwt
- xss
language: en
raw_sha256: f9320fcf14471a0f24111da942cb9e1718f88a5a665faca3fa23de18983804fb
text_sha256: 1f0d4c7061b3a233ed82cda2d13bd3490fb44528175e3752936cfeb6dbb2391a
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# How the Sys:All Loophole Allowed Us To Penetrate GKE Clusters in Production

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-24_how-the-sysall-loophole-allowed-us-to-penetrate-gke-clusters-in-production.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, oauth, sso, jwt, xss
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `f9320fcf14471a0f24111da942cb9e1718f88a5a665faca3fa23de18983804fb`
- Text SHA256: `1f0d4c7061b3a233ed82cda2d13bd3490fb44528175e3752936cfeb6dbb2391a`


## Content

---
title: "How the Sys:All Loophole Allowed Us To Penetrate GKE Clusters in Production"
page_title: "Real-World Examples of Sys:All GKE Risk | Orca Security"
url: "https://orca.security/resources/research-pod/sys-all-google-kubernetes-engine-risk-example/"
final_url: "https://orca.security/resources/research-pod/sys-all-google-kubernetes-engine-risk-example/"
authors: ["Roi Nisimi (@roinisimi)", "Ofir Yakobi"]
programs: ["Google (GKE)"]
bugs: ["Kubernetes", "Cloud", "Privilege escalation"]
publication_date: "2024-01-24"
added_date: "2024-01-25"
source: "pentester.land/writeups.json"
original_index: 504
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![How the Sys:All Loophole Allowed Us To Penetrate GKE Clusters in Production](https://orca.security/wp-content/uploads/2024/01/sys-all-real-world-blog-1980.png?w=1044)

# How the Sys:All Loophole Allowed Us To Penetrate GKE Clusters in Production

[ ![Avatar of Ofir Yakobi](https://orca.security/wp-content/uploads/2024/01/cropped-Ofir-Yakobi-100x100.jpg) Ofir Yakobi  ](https://orca.security/resources/author/ofiryakobi/)

Published: Jan 24, 2024 

  * [ __](https://twitter.com/share?text=How%20the%20Sys%3AAll%20Loophole%20Allowed%20Us%20To%20Penetrate%20GKE%20Clusters%20in%20Production&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk-example%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk-example%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk-example%2F)
  * [ __](mailto:?Subject=How the Sys:All Loophole Allowed Us To Penetrate GKE Clusters in Production&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk-example%2F)

Following our discovery of a critical loophole in Google Kubernetes Engine (GKE) dubbed [Sys:All](https://orca.security/resources/blog/sys-all-google-kubernetes-engine-risk/), we decided to conduct research into the real-world impacts of this issue. Our initial probe already revealed over a thousand vulnerable GKE clusters due to admins configuring RBAC bindings making the system:authenticated group overprivileged, which could potentially allow any Google account holder to access and control these clusters.

GKE, unlike other major Kubernetes services offered by CSPs such as AWS and Azure, defaults to using standard IAM for cluster authentication and authorization. This approach enables some access to the Kubernetes API server using any Google credentials, thereby including all Google users, including those outside of the organization, in GKE’s system:authenticated group. Since the scope of this group is easily misunderstood, administrators can unknowingly assign too many privileges and leave the GKE cluster wide open.

In this article, we delve into how widespread this issue actually is. Through a series of scans on publicly available GKE clusters, we uncovered a spectrum of data exposures with real-world consequences for numerous organizations. We will discuss the nature of these exposures and the range of sensitive information that could be compromised. Our story will show tangible examples of exploitation paths, and give practical recommendations for securing GKE clusters against these threats.

[Attend Threat Briefing](https://www.brighttalk.com/webcast/18490/605535?bt_tok=%7B%7Blead.Id%7D%7D&utm_source=OrcaSecurity&utm_medium=brighttalk&utm_campaign=605535)

## Executive Summary:

  * We discovered numerous organizations with significant misconfigurations of their system:authenticated groups across various GKE clusters, that make them vulnerable to the [Sys:All loophole](https://orca.security/resources/blog/sys-all-google-kubernetes-engine-risk/) discovered by Orca.
  * These misconfigurations led to the exposure of various sensitive data types, including JWT tokens, GCP API keys, AWS keys, Google OAuth credentials, and private keys.
  * A notable example involved a publicly traded company where this misconfiguration resulted in extensive unauthorized access, potentially leading to system-wide security breaches.
  * This study highlights the critical need for stringent security protocols in cloud environments to prevent similar occurrences.
  * A [Threat Briefing](https://www.brighttalk.com/webcast/18490/605535?bt_tok=%7B%7Blead.Id%7D%7D&utm_source=OrcaSecurity&utm_medium=brighttalk&utm_campaign=605535) detailing how an attacker could abuse this GKE security loophole, as well as recommendations on how to protect your clusters, will be held on January 26th at 11 am Pacific Time.

## Technical Exploitation Overview

Our research embarked on a journey to assess how many GKE clusters were exposed to the Sys:All loophole, inspecting clusters from a known CIDR range. We specifically targeted clusters that had custom roles assigned to the system:authenticated group. Our scans identified over a thousand clusters with varying degrees of exposure due to these custom role assignments.

To probe these clusters, we developed a python script that utilized a generic Google authentication token (obtained through the [OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)), accessible to any Google user. The script was designed to [interact with the Kubernetes API](https://orca.security/platform/container-and-kubernetes-security/) of these clusters, aiming to extract a wealth of potentially sensitive information. We targeted data points such as configuration maps (configmaps), Kubernetes secrets, service account details, and other critical operational data. Furthermore, our approach included attempts to associate these clusters with their respective organizations, thus uncovering the broader impact of these misconfigurations and their owners.

We then ran Orca Secret-Detector on the retrieved data to identify and match known secret patterns and regexes that could allow further lateral movement within the organization’s environment.

  
This part was crucial in understanding the real implications of these security misconfigurations, particularly in the context of potential exploitation by unauthorized entities. Through this comprehensive technical examination, we gained deepened insights into the prevalence and severity of security shortcomings within these GKE clusters.

## How We Accessed GKE Clusters of a NASDAQ Listed Company

Our investigations led us to a stark discovery of a NASDAQ listed company’s exploitable GKE clusters. A seemingly innocuous misconfiguration in the system:authenticated group had far-reaching implications, such as allowing list and pull images from the company’s container registries and providing open access to AWS credentials stored within a cluster’s configmap (alongside other sensitive data found). With these credentials, we gained access to S3 buckets containing multiple sensitive information and logs that, upon further analysis, revealed system admin credentials and multiple valuable endpoints including RabbitMQ, Elastic, authentication server and internal system – **all with administrator access**.

Here’s a step-by-step account of how this misconfiguration enabled us to move laterally within the company’s digital infrastructure:

  1. **Initial Access** : The misconfigured GKE clusters allowed cluster admin permissions to the system:authenticated group, allowing us (with any Google user account) to query multiple valuable resources using the Kubernetes API, including the ConfigMap resources and investigate it.  
  
It is important to note that Google blocks the binding of the system:authenticated group to the cluster-admin role in newer GKE versions (1.28 and up). We would like to emphasize that even though this is an improvement, it still leaves many other roles and permissions (other than cluster-admin) that can be assigned to the system:authenticated group.

![](https://orca.security/wp-content/uploads/2024/01/image3_9edb98.png?w=1200)

  2. **AWS Credential Exposure** : Embedded within a bash script we found an AWS access key and secret with broad S3 permissions. This highlighted a serious breach in security practices, leading to the exposure of multiple credentials and sensitive data.

  3. **Bucket Content Examination** : Using the exposed AWS credentials, we could list and download the contents of several S3 buckets. Among these were log files with detailed operational data.
  4. **Sensitive Information Discovery** : The logs contained administrator credentials for various systems, including an **internal platform** used by their customers. Critically, URLs to important internal services such as ElasticSearch and RabbitMQ were also found, accompanied by superuser privileges.

![](https://orca.security/wp-content/uploads/2024/01/image4_6adb34.png) ![](https://orca.security/wp-content/uploads/2024/01/image1_9f255f.png?w=1200)

  5. **Potential for Further Lateral Movement** : With admin credentials and service URLs in hand, a malicious actor could potentially access these systems, extract or manipulate sensitive data, disrupt services, or even move further into the network.

After responsibly disclosing these findings to the affected company, we collaborated with them to address the vulnerabilities. This involved tightening IAM roles and permissions, securing S3 buckets, and implementing better practices around ConfigMaps. As the secrets were embedded within bash scripts as part of the Kubernetes configmaps, we advised and assisted in establishing better practices. This involved removing sensitive data from scripts, using more secure methods for managing secrets, and ensuring that configmaps were not accessible to unauthorized users.

By addressing these areas, the company was able to significantly reduce the risk of similar vulnerabilities in the future, enhancing the overall security of their cloud infrastructure.

## Findings from Other Exposed GKE Clusters

In our broader more general examination of GKE clusters, we uncovered a variety of sensitive data exposure across multiple organizations, highlighting the extensive nature of these issues:

  * **Exposure of GCP API Keys and Service Account JSONs** : We frequently came across GCP API keys and service account authentication JSON files left exposed. These elements are crucial for accessing GCP resources, and their exposure represents a significant security threat.
  * **Discovery of Private Keys** : Our scans also revealed private keys within these clusters. Such keys are essential for securing communications and data access, making their exposure a major security risk.
  * **Access to Container Registries** : We found numerous instances where credentials for various container registries were accessible. This allowed us to pull and run container images locally, a capability that could be abused to introduce malicious elements into containerized applications.

![](https://orca.security/wp-content/uploads/2024/01/image2_55b9a1.png?w=1200)

  * **Access to Critical Services** : Our findings included unauthorized access to Grafana dashboards, RabbitMQ message brokers, and ElasticSearch clusters in different organizations. Each of these services play a critical role in operational monitoring, messaging, and data management, respectively. Gaining access to these services could lead to significant data breaches and operational disruptions.

![](https://orca.security/wp-content/uploads/2024/01/image7_1f0f63.png?w=1200) ![](https://orca.security/wp-content/uploads/2024/01/image5_e77f9b.png?w=850) ![](https://orca.security/wp-content/uploads/2024/01/image6_126e29.png?w=1200)

Where possible, we notified the owners of the vulnerable GKE clusters, but it’s not always possible to identify who owns the cluster. Therefore we urge organizations to follow the recommendations presented below.

The cumulative findings from our research painted a concerning picture of the widespread nature of security lapses in cloud environments. From critical access keys to operational data and infrastructure oversight, the diversity and depth of the data exposed underscore the urgent need for robust security measures and [continuous monitoring](https://orca.security/platform/) in cloud environments.

## Recommendations

This story is a real-world testament to the importance of rigorous security configurations. For GKE users, it’s vital to review cluster permissions, especially default groups such as system:authenticated. Organizations must ensure that only necessary permissions are granted following the [Principle of Least Privilege (PolP)](https://orca.security/platform/cloud-infrastructure-entitlement-management-ciem/), and that regular audits are conducted to prevent such oversights.

Google has blocked the binding of the system:authenticated group to the cluster-admin role in newer GKE versions ([version 1.28 and up](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-003)). However, it’s important to note that this still leaves many other roles and permissions that can be assigned to the group. This means that in addition to upgrading to GKE version 1.28 or higher, the main way to block this attack vector is to strictly follow the [principle of least privilege](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-003). 

More specifically, the Orca Platform now also alerts to overprivileged System:Authenticated groups, in addition to the above mentioned issues we found in many cloud environments.

![The Orca Platform warns when the GKE system:authenticated group allows too much access](https://orca.security/wp-content/uploads/2024/01/image8.jpg?w=1200)

_The Orca Platform warns when the GKE system:authenticated group allows too much access_

## Orca is Here to Help

As cloud technologies grow more complex, the potential for misconfigurations grows. But with diligence and proper security practices, these risks can be mitigated. The [Orca Research Pod](https://orca.security/about/orca-research-pod/) will continue to research and share our findings to contribute to safer cloud ecosystems. 

If you are ready to take your cloud security to the next level, schedule a personal demo with [one of our experts](https://orca.security/demo/) to see how we can help strengthen your cloud environment.

  * [ __](https://twitter.com/share?text=How%20the%20Sys%3AAll%20Loophole%20Allowed%20Us%20To%20Penetrate%20GKE%20Clusters%20in%20Production&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk-example%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk-example%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk-example%2F)
  * [ __](mailto:?Subject=How the Sys:All Loophole Allowed Us To Penetrate GKE Clusters in Production&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsys-all-google-kubernetes-engine-risk-example%2F)

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
