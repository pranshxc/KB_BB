---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-17_mitigating-rbac-based-privilege-escalation-in-popular-kubernetes-platforms.md
original_filename: 2022-05-17_mitigating-rbac-based-privilege-escalation-in-popular-kubernetes-platforms.md
title: Mitigating RBAC-Based Privilege Escalation in Popular Kubernetes Platforms
category: documents
detected_topics:
- access-control
- cloud-security
- supply-chain
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- access-control
- cloud-security
- supply-chain
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 19b7c2b5a1bc72dc084ad5601b8500cf5a99b40697380fe3ce2d11d853cf1328
text_sha256: 8e2d870bba603441c4f3ebc354a805c2e0ef473d1485f5c28e72ce31a7f3d520
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Mitigating RBAC-Based Privilege Escalation in Popular Kubernetes Platforms

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-17_mitigating-rbac-based-privilege-escalation-in-popular-kubernetes-platforms.md
- Source Type: markdown
- Detected Topics: access-control, cloud-security, supply-chain, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `19b7c2b5a1bc72dc084ad5601b8500cf5a99b40697380fe3ce2d11d853cf1328`
- Text SHA256: `8e2d870bba603441c4f3ebc354a805c2e0ef473d1485f5c28e72ce31a7f3d520`


## Content

---
title: "Mitigating RBAC-Based Privilege Escalation in Popular Kubernetes Platforms"
url: "https://unit42.paloaltonetworks.com/kubernetes-privilege-escalation/#post-126770-_5e5x5pdas37n"
final_url: "https://unit42.paloaltonetworks.com/kubernetes-privilege-escalation/#post-126770-_5e5x5pdas37n"
authors: ["Yuval Avrahami (@yuval_avrahami)", "Shaul Ben Hai"]
programs: ["Google", "AWS", "Microsoft", "Red Hat"]
bugs: ["Privilege escalation", "Broken Access Control", "Kubernetes"]
bounty: "13,022"
publication_date: "2022-05-17"
added_date: "2023-01-27"
source: "pentester.land/writeups.json"
original_index: 2635
---

English

  * [English](https://unit42.paloaltonetworks.com/kubernetes-privilege-escalation/)
  * [Japanese](https://unit42.paloaltonetworks.com/ja/kubernetes-privilege-escalation/)

  * [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Learning Hub](https://unit42.paloaltonetworks.com/category/learning-hub/ "Learning Hub")

[Learning Hub](https://unit42.paloaltonetworks.com/category/learning-hub/)

# Mitigating RBAC-Based Privilege Escalation in Popular Kubernetes Platforms

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 9 min read 

Related Products

[![Prisma Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Cloud](https://unit42.paloaltonetworks.com/product-category/prisma-cloud/ "Prisma Cloud")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
  * [Yuval Avrahami](https://unit42.paloaltonetworks.com/author/yuval-avrahami/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:January 27, 2023

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
  * [Learning Hub](https://unit42.paloaltonetworks.com/category/learning-hub/)
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
  * [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/)
  * [Container escape](https://unit42.paloaltonetworks.com/tag/container-escape/)
  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/)
  * [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/)
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/)

  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/kubernetes-privilege-escalation/?pdf=download&lg=en&_wpnonce=007ee71b73 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/kubernetes-privilege-escalation/?pdf=print&lg=en&_wpnonce=007ee71b73 "Click here to print")

Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Mitigating%20RBAC-Based%20Privilege%20Escalation%20in%20Popular%20Kubernetes%20Platforms&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fkubernetes-privilege-escalation%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fkubernetes-privilege-escalation%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fkubernetes-privilege-escalation%2F&title=Mitigating%20RBAC-Based%20Privilege%20Escalation%20in%20Popular%20Kubernetes%20Platforms "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fkubernetes-privilege-escalation%2F&text=Mitigating%20RBAC-Based%20Privilege%20Escalation%20in%20Popular%20Kubernetes%20Platforms "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fkubernetes-privilege-escalation%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Mitigating%20RBAC-Based%20Privilege%20Escalation%20in%20Popular%20Kubernetes%20Platforms%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fkubernetes-privilege-escalation%2F "Share in Mastodon")

## Executive Summary

Prisma Cloud and Unit 42 recently released a [report examining the use of powerful credentials](https://www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms) in popular Kubernetes platforms, which found most platforms install privileged infrastructure components that could be abused for privilege escalation. We're happy to share that, as of today, all platforms mentioned in our report have addressed built-in node-to-admin privilege escalation. However, it’s possible third party add-ons might reintroduce the issue.

In the research we presented at [KubeCon EU and BlackHat USA](https://www.youtube.com/watch?v=PGsJ4QTlKlQ), we found that in half the platforms, any container escape had previously allowed for a full cluster compromise because all nodes hosted admin-equivalent credentials. Most of the platforms mentioned in our report made their infrastructure unprivileged by default, while one did so through an optional add-on.

Stripping permissions is often complex, and we recognize fixing this is no small matter. We'd like to thank Azure Kubernetes Service (AKS), AWS Elastic Kubernetes Service (EKS), Google Kubernetes Engine (GKE), RedHat OpenShift Container Platform, Antrea and Calico for working to harden their access control.

We provide a short recap of our research and look into the different mitigations the platforms implemented to address privilege escalation and powerful permissions in Kubernetes. If you're interested in evaluating your own cluster's Role Based Access Control (RBAC) posture, try [rbac-police](https://github.com/PaloAltoNetworks/rbac-police), our open-source RBAC analyzer for Kubernetes.

[Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) users can catch Kubernetes misconfigurations like excessive RBAC permissions before they're deployed to the cluster via the [Cloud Code Security](https://www.paloaltonetworks.com/prisma/cloud/cloud-code-security) (CCS) module. In the runtime phase, users can rely on the built-in [admission controller for Kubernetes](https://docs.paloaltonetworks.com/prisma/prisma-cloud/21-04/prisma-cloud-compute-edition-admin/access_control/open_policy_agent) to enforce policies that alert on suspicious activity in their clusters, including Kubernetes privilege escalation.

**Related Unit 42 Topics** | [Privilege Escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/), [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/), [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/), [Containers](https://unit42.paloaltonetworks.com/tag/containers/), [Container Escape](https://unit42.paloaltonetworks.com/tag/container-escape/)  
---|---  
  
## **Recap: Powerful Permissions Everywhere**

Kubernetes managed services, distributions and add-ons install a set of system pods into our cluster to manage its infrastructure and enable core functions such as networking, DNS and logging. Commonly, these pods are deployed via [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) that distribute them onto every node in the cluster.

If those DaemonSets' permissions are loosely granted, they could inadvertently spread powerful credentials throughout the cluster. This could be abused for privilege escalation, as shown in Figure 1.

Figure 1. An attacker who escaped a container exploits the credentials of a powerful DaemonSet to spread in the cluster.

To understand the prevalence of powerful DaemonSets, we analyzed popular Kubernetes platforms—managed services, distributions and container network interfaces (CNIs)—to identify privileged infrastructure components. We found that**most platforms ran powerful DaemonSets** , installing privileged credentials onto every node in the cluster.

As shown in Figure 2, in half the platforms, those credentials were admin-equivalent, allowing a single container escape to compromise the entire cluster.

Figure 2. Percentage of platforms where a container escape allowed a complete cluster takeover.

We believe powerful DaemonSets became common for three main reasons:

  1. **Historically, Kubernetes clusters weren't secured by default**.  
In environments where crucial components like Kubelets allowed unauthenticated access, maintaining a least-privileged RBAC posture wasn't a priority. The infrastructure built then set a precedent for powerful DaemonSets.
  2. **Some Kubernetes permissions are simply too broad**.  
This means they authorize a large set of operations. Often, granting a service account the ability to perform a necessary but sensitive operation implicitly authorizes it to perform other, potentially harmful operations. RBAC is not a great model for many of these use cases, and an attribute-based access control model that matches some attribute of the principal to some attribute of the resource would often make more sense.
  3. **Certain** **permissions appear benign, but are in fact quite powerful**.  
If someone believes a permission is harmless, they won't have second thoughts about granting it. For example, the ability to update the status of pods implicitly allows deleting pods that are part of ReplicaSets.

## Mitigation

After identifying a powerful DaemonSet, we reached out to the relevant platform and started a discussion on mitigation. The response was extremely positive – the teams understood the issue and wanted to resolve it. Mitigations were developed, tested and deployed in recent months. And as of today, all of the privilege escalation attacks we identified are resolved.

Thanks to the work done by the different platforms, the Kubernetes landscape is a safer one, where nodes aren't admins by default. In the following sections, we'll highlight the different approaches platforms took to address powerful DaemonSets in their offerings.

## **Strip Permissions**

The simplest way to address a risky permission is to remove it. A number of platforms identified certain risky permissions that weren't explicitly necessary, and they removed them. Some permissions were made safe by scoping them down to certain [resourceNames](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-resources) or subresources.

For example, Cilium found that the “delete pods” permission wasn't explicitly necessary for their DaemonSet to operate correctly, and they [removed it](https://github.com/cilium/cilium/pull/19053). Openshift was able to [strip the "update nodes" permission](https://github.com/openshift/cluster-network-operator/pull/1350) from their software-defined network (sdn) DaemonSet, because the function that relied on it could be replaced with an unprivileged implementation.

## Restrict via Admission Control

A common use case for DaemonSets is local node management, where each DaemonSet pod manages its local node. Unfortunately, Kubernetes doesn't support scoping down a DaemonSet pod's permissions to its local node. Thus every pod in the DaemonSet must be authorized to manage all nodes, not just its local one. This allows attackers who take over a node to abuse the credentials of the local DaemonSet pod to compromise other nodes and spread in the cluster.

Both AKS and EKS ran a DaemonSet that had pods that needed to update their local node. Unfortunately, the only way built in to Kubernetes to grant this permission was to permit every pod in the DaemonSet to update every node in the cluster.

An attacker who compromised a node could abuse the DaemonSet's token to [taint](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) other nodes, allowing it to steal pods. This attack is carried out in three steps, illustrated in Figure 3.

  1. Add a NoSchedule taint to every node in the cluster beside the compromised one, making the compromised node the only available node in the cluster.
  2. Add a NoExecute taint to the node hosting the target pod to force Kubernetes to evict it and delete its pods.
  3. Kubernetes recreates the target pod, and can now only schedule it on the one available node in the cluster, which is the compromised node.

Figure 3. Abusing a DaemonSet's “update nodes” permission to manipulate taints in order to steal pods.

The DaemonSets on EKS and AKS needed the “update nodes” permission, so simply removing it wasn't a valid solution. Instead, both platforms were able to mitigate the attack using custom [validating admission webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#what-are-admission-webhooks).

### EKS - Restrict by Operation

In EKS, the aws-node DaemonSet needed to update certain node attributes, but not taints. So if an aws-node pod unexpectedly attempts to taint a node, it's likely an attack. The EKS team implemented a validating admission webhook that intercepts node update requests, and blocks attempts to manipulate taints that are issued by the aws-node service account. You can see this in action in Figure 4, below.

Figure 4. EKS prevents the aws-node pod from tainting nodes.

### AKS - Restrict by Target

AKS had a slightly more difficult situation to contend with. Their cloud-node-manager DaemonSet does taint nodes, so blocking taints altogether wasn't a valid option.

To be exact, each cloud-node-manager only needed to taint its hosting node. AKS used that to mitigate the attack. They wrote a validating admission webhook that intercepts node update requests, and identifies which cloud-node-manager pod issued the request.

If a cloud-node-manager pod attempts to update a node that isn't its hosting one, the request is denied. As shown in Figure 5, if an attacker attempts to abuse a cloud-node-manager pod's credentials, they are denied.

Figure 5. AKS prevents the cloud-node-manager pod from tainting other nodes.

To function correctly, this admission webhook must know which pod issued the request, not only which service account. This is possible thanks to a recent Kubernetes enhancement, [bound service account tokens](https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1205-bound-service-account-tokens/README.md#summary).

In the past, a token only referenced the service account it represents. Now, a pod's service account token also includes a claim that specifies the pod the token was issued for. Admission controllers can use that claim to identify which pod a request originated from.

This webhook nicely demonstrates how bound tokens enable node-local authorization for DaemonSet pods. It's possible that in the future, Kubernetes would have built-in support for that functionality, without the need for a custom admission webhook.

## **Move Privileged Functionality Elsewhere**

To carry out privileged tasks, someone in the cluster needs to possess powerful credentials. Because DaemonSets' credentials are widely distributed, they're not the best fit for carrying out privileged tasks. Several platforms addressed powerful DaemonSets by having control plane controllers or non-DaemonSet pods carry out privileged tasks instead. DaemonSets' powerful permission could then be removed.

For example, in GKE clusters running Dataplane v2 the anted DaemonSet was authorized to update pods and nodes for certain tasks. These permissions are risky, and could also be abused for a number of privilege escalation attacks. By having the control plane take care of pod and node updates, GKE was able to remove these powerful permissions from the anted DaemonSet.

## **Recommendations**

Even when the underlying Kubernetes infrastructure is configured to maintain appropriate privilege boundaries, add-ons and applications that are misconfigured with excessive permissions can still re-introduce the same attack paths to a cluster. Below are best practices for hardening your cluster's RBAC posture and preventing intracluster privilege escalation.

  * Follow the principle of least-privilege. Only grant explicitly required permissions. When possible, scope down permissions to specific namespaces, resources names, or subresources.
  * Add guardrails to your Kubernetes Infrastructure-as-Code (IaC) continuous integration/continuous delivery (CI/CD) pipelines. This will prevent developers from unintentionally granting powerful permissions to service accounts. [Checkov](https://www.checkov.io/), an open-source IaC scanner, [supports a number of Kubernetes checks](https://docs.bridgecrew.io/docs/ensure-roles-and-clusterroles-that-grant-permissions-to-bind-rolebindings-or-clusterrolebindings-are-minimized) that alert on excessive RBAC permissions, as shown below in Figure 6.
  * Routinely review your RBAC posture. This allows you to identify potential threats and overly powerful identities. Ensure powerful permissions aren't granted to less trusted or publicly exposed pods. Consider using automated tools like [rbac-police](https://github.com/PaloAltoNetworks/rbac-police).
  * Refrain from assigning tasks requiring privileged credentials to DaemonSets. Control plane controllers or deployments are preferable in this instance.
  * Separate resources and workloads requiring different trust levels into different namespaces.
  * Use [admission control](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#admission-webhooks) to implement fine grained authorization for permissions that cannot be expressed in RBAC. When possible, implement a safe operation allowlist to block unexpected and malicious requests from powerful service accounts.
  * Isolate powerful pods on separate nodes from untrusted or publicly-exposed ones using scheduling constraints like [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/), [NodeAffinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) rules, or [PodAntiAfinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#types-of-inter-pod-affinity-and-anti-affinity) rules.

Figure 6: Checkov alerts on a ClusterRole configured with powerful permissions.

Your cluster’s threat model should be taken into account when implementing industry best practices. Kubernetes is a platform for building platforms, meaning a cluster's threat model varies heavily depending on its architecture. The above guidelines tackle intracluster privilege escalation.

If you're building clusters with different trust levels, intracluster privilege is a major threat. Below are a few examples for clusters hosting different trust levels:

  * Multitenant clusters hosting possibly malicious tenants/workloads
  * Running different teams on a single cluster
  * Deploying multiple applications across a large cluster

On the other hand, if you're running small clusters that are each dedicated to a single application, then it makes more sense to invest in segregating those clusters from one another and from external services. When the cluster doesn't host different trust levels, preventing privilege escalation inside it shouldn't be a top priority. That being said, **detecting** privilege escalation attacks can still help identify breaches.

## **Conclusion**

Maintaining a secure RBAC posture in Kubernetes is complex, both for platforms and users. When leading platforms enforce hardened defaults, it's easier for Kubenetes users to adopt secure architectures.

We'd like to thank each of the platforms mentioned in this blog for taking the difficult problem of unprivileged infrastructure head on, and coming up with creative implementations to solve it.

We recommend Kubernetes users and platforms automate the detection of RBAC misconfigurations in their CI/CD pipelines through tools like [Checkov](https://www.checkov.io/) and [rbac-police](https://github.com/PaloAltoNetworks/rbac-police). For managed services, even when an infrastructure component requires risky permissions, a validating admission webhook might be able to prevent misuse.

See our report, [Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms](https://www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms), for more information. [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) users are encouraged to read the report's "Prisma Cloud" section to learn how Prisma's [Kubernetes IaC scanning capabilities](https://www.paloaltonetworks.com/prisma/cloud/cloud-code-security) and the built-in [admission controller for Kubernetes](https://docs.paloaltonetworks.com/prisma/prisma-cloud/21-04/prisma-cloud-compute-edition-admin/access_control/open_policy_agent) can tackle the challenges of securing Kubernetes identities.

## **Additional Resources**

  * [Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms](https://www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms)
  * [Trampoline Pods: Node to Admin PrivEsc Built Into Popular K8s Platforms](https://www.youtube.com/watch?v=PGsJ4QTlKlQ)
  * [Privileged pod escalations in Kubernetes and GKE](https://security.googleblog.com/2022/05/privileged-pod-escalations-in.html)
  * [Checkov](https://www.checkov.io/)
  * [rbac-police](https://github.com/PaloAltoNetworks/rbac-police)

Back to top

### Tags

  * [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/ "Cloud Security")
  * [Container escape](https://unit42.paloaltonetworks.com/tag/container-escape/ "container escape")
  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")
  * [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/ "Kubernetes")
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")

[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Chinese PlugX Malware Hidden in Your USB Devices? ](https://unit42.paloaltonetworks.com/plugx-variants-in-usbs/ "Chinese PlugX Malware Hidden in Your USB Devices?")

### Table of Contents

  * 

### Related Articles

  * [ The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "article - table of contents")
  * [ Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/ "article - table of contents")
  * [ Essential Data Sources for Detection Beyond the Endpoint ](https://unit42.paloaltonetworks.com/detection-beyond-the-endpoint/ "article - table of contents")

## Related Threat Research Resources

![Pictorial representation of CL-STA-1062 targeting energy and government sectors in Southeast Asia. An artistic depiction of a digital workspace featuring an open laptop with a red virus on the screen, indicating malware.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/03_Malware_Category_1920x900-5-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 25, 2026 #### [CL-STA-1062 Targets Southeast Asian Governments and Critical Infrastructure ](https://unit42.paloaltonetworks.com/cl-sta-1062-tinyrct-backdoor/)

  * [Backdoor](https://unit42.paloaltonetworks.com/tag/backdoor/ "backdoor")
  * [CL-STA-1062](https://unit42.paloaltonetworks.com/tag/cl-sta-1062/ "CL-STA-1062")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cl-sta-1062-tinyrct-backdoor/ "CL-STA-1062 Targets Southeast Asian Governments and Critical Infrastructure")

![Pictorial representation of OpenClaw's skill marketplace and AI supply chain risk. A bustling city street at dusk, filled with silhouettes of pedestrians. The scene is illuminated by glowing lights from buildings and a warm, golden sky, creating a vibrant, almost dream-like atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/AdobeStock_768915868-1-786x410.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 23, 2026 #### [OpenClaw’s Skill Marketplace and the Emerging AI Supply Chain Threat ](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/)

  * [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")
  * [ClawHavoc](https://unit42.paloaltonetworks.com/tag/clawhavoc/ "ClawHavoc")
  * [ClawHub](https://unit42.paloaltonetworks.com/tag/clawhub/ "ClawHub")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/ "OpenClaw’s Skill Marketplace and the Emerging AI Supply Chain Threat")

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

![Pictorial representation of integrity verification for AI Agent supply chains. A swirling, colorful digital pattern on a dark background resembling a vortex. Bright dots and lines in shades of blue, pink, and purple create a dynamic, futuristic effect.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/AdobeStock_429594706-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 11, 2026 #### [Trust No Skill: Integrity Verification for AI Agent Supply Chains ](https://unit42.paloaltonetworks.com/ai-agent-supply-chain-risks/)

  * [AI agents](https://unit42.paloaltonetworks.com/tag/ai-agents/ "AI agents")
  * [Credential exfiltration](https://unit42.paloaltonetworks.com/tag/credential-exfiltration/ "credential exfiltration")
  * [LLMs](https://unit42.paloaltonetworks.com/tag/llms/ "LLMs")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-agent-supply-chain-risks/ "Trust No Skill: Integrity Verification for AI Agent Supply Chains")

![Pictorial representation of Cloud Logging services for defense evasion. A vibrant digital illustration depicting a glowing, neon blue cloud symbol positioned over a circuit board landscape. The cloud symbolizes cloud computing technology, and the landscape features intricate electronic circuits with glowing lines and nodes, suggesting high-tech data transfer and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/11_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 9, 2026 #### [Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/ "cloud logging")
  * [Defense evasion](https://unit42.paloaltonetworks.com/tag/defense-evasion/ "defense evasion")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/ "Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility")

![Pictorial representation of FlutterBridge. Digital screen with a warning sign reading "Malware." The background features lines of computer code and graphics, creating a sense of cybersecurity threat.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/07_Malware_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 2, 2026 #### [Operation FlutterBridge: macOS Malvertising Campaign Spreads New FlutterShell Backdoor ](https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/)

  * [CL-CRI-1089](https://unit42.paloaltonetworks.com/tag/cl-cri-1089/ "CL-CRI-1089")
  * [MacOS](https://unit42.paloaltonetworks.com/tag/macos/ "macOS")
  * [Malvertising](https://unit42.paloaltonetworks.com/tag/malvertising/ "malvertising")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/ "Operation FlutterBridge: macOS Malvertising Campaign Spreads New FlutterShell Backdoor")

![Pictorial representation of a woman standing in a server room holding a laptop that projects a digital code overlay.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/06_Security-Technology_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/) May 28, 2026 #### [2026 World Cup: Discussing The World’s Biggest Game’s Attack Surface ](https://unit42.paloaltonetworks.com/fifa-world-cup-attack-surface/)

  * [Fiddling Scorpius](https://unit42.paloaltonetworks.com/tag/fiddling-scorpius/ "Fiddling Scorpius")
  * [Fighting Ursa](https://unit42.paloaltonetworks.com/tag/fighting-ursa/ "Fighting Ursa")
  * [Muddled Libra](https://unit42.paloaltonetworks.com/tag/muddled-libra/ "Muddled Libra")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/fifa-world-cup-attack-surface/ "2026 World Cup: Discussing The World’s Biggest Game’s Attack Surface")

![Pictorial representation of ROADtools framework in the cloud. An Asian man wearing glasses sits in front of a computer screen. Reflecting in the glasses are lines indicating analysis. Bright blue city lights illuminate the rest of the image.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/10_Cloud_cybersecurity_research_Overview_1920x900-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) May 22, 2026 #### [Paved With Intent: ROADtools and Nation-State Tactics in the Cloud ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)

  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/ "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud")

![Pictorial representation of TamperedChef clusters. Hands typing on a laptop keyboard with colorful lines of binary code and digital information flowing from the screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/07_Security-Technology_Category_1505x922-718x440.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) May 20, 2026 #### [Tracking TamperedChef Clusters via Certificate and Code Reuse ](https://unit42.paloaltonetworks.com/tracking-tampered-chef-clusters/)

  * [Adware](https://unit42.paloaltonetworks.com/tag/adware/ "Adware")
  * [Appsuite PDF](https://unit42.paloaltonetworks.com/tag/appsuite-pdf/ "Appsuite PDF")
  * [Certificates](https://unit42.paloaltonetworks.com/tag/certificates/ "certificates")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/tracking-tampered-chef-clusters/ "Tracking TamperedChef Clusters via Certificate and Code Reuse")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image]()
