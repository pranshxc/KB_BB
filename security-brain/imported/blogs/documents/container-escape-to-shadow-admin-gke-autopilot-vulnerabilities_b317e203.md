---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-08_container-escape-to-shadow-admin-gke-autopilot-vulnerabilities.md
original_filename: 2022-03-08_container-escape-to-shadow-admin-gke-autopilot-vulnerabilities.md
title: 'Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities'
category: documents
detected_topics:
- cloud-security
- command-injection
- access-control
- otp
- supply-chain
- sso
tags:
- imported
- documents
- cloud-security
- command-injection
- access-control
- otp
- supply-chain
- sso
language: en
raw_sha256: b317e2032df6549599a0d412f1127c4eada34e8f156ad55e08cc889879f4ce54
text_sha256: ddb1cf68706912184810cbded741106ccad7b1c83dd6496ca115392d5f6f7995
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-08_container-escape-to-shadow-admin-gke-autopilot-vulnerabilities.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, access-control, otp, supply-chain, sso
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `b317e2032df6549599a0d412f1127c4eada34e8f156ad55e08cc889879f4ce54`
- Text SHA256: `ddb1cf68706912184810cbded741106ccad7b1c83dd6496ca115392d5f6f7995`


## Content

---
title: "Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities"
url: "https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/"
final_url: "https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/"
authors: ["Unit 42 (@Unit42_Intel)"]
programs: ["Google"]
bugs: ["Privilege escalation", "Container escape", "Kubernetes"]
publication_date: "2022-03-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2843
---

English

  * [English](https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/)
  * [Japanese](https://unit42.paloaltonetworks.com/ja/gke-autopilot-vulnerabilities/)

  * [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")

[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)

# Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 13 min read 

Related Products

[![Prisma Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Cloud](https://unit42.paloaltonetworks.com/product-category/prisma-cloud/ "Prisma Cloud")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
  * [Yuval Avrahami](https://unit42.paloaltonetworks.com/author/yuval-avrahami/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:March 8, 2022

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
  * [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/)

  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/?pdf=download&lg=en&_wpnonce=007ee71b73 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/?pdf=print&lg=en&_wpnonce=007ee71b73 "Click here to print")

Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Container%20Escape%20to%20Shadow%20Admin:%20GKE%20Autopilot%20Vulnerabilities&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fgke-autopilot-vulnerabilities%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgke-autopilot-vulnerabilities%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgke-autopilot-vulnerabilities%2F&title=Container%20Escape%20to%20Shadow%20Admin:%20GKE%20Autopilot%20Vulnerabilities "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgke-autopilot-vulnerabilities%2F&text=Container%20Escape%20to%20Shadow%20Admin:%20GKE%20Autopilot%20Vulnerabilities "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgke-autopilot-vulnerabilities%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Container%20Escape%20to%20Shadow%20Admin:%20GKE%20Autopilot%20Vulnerabilities%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fgke-autopilot-vulnerabilities%2F "Share in Mastodon")

## **Executive Summary**

In February 2021, Google announced [Autopilot](https://cloud.google.com/blog/products/containers-kubernetes/introducing-gke-autopilot), a new mode of operation in [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE). With Autopilot, Google provides a "hands-off" Kubernetes experience, managing cluster infrastructure for the customer. The platform automatically provisions and removes nodes based on resource consumption and enforces secure Kubernetes best practices out of the box.

In June 2021, Unit 42 researchers disclosed several vulnerabilities and attack techniques in GKE Autopilot to Google. Users able to create a pod could have abused these to (1) escape their pod and compromise the underlying node, (2) escalate privileges and become full cluster administrators, and (3) covertly persist administrative access through backdoors that are completely invisible to cluster operators.

An attacker who obtained an initial foothold on an Autopilot cluster, for example, through a compromised developer's account, could have exploited these issues to escalate privileges and become a "shadow administrator," with the ability to covertly exfiltrate secrets, deploy malware or cryptominers and disrupt workloads.

Following our disclosure, Google fixed the reported issues, deploying patches universally across GKE. All Autopilot clusters are now protected.

This blog provides a technical analysis of the issues, as well as mitigations for preventing similar attacks against Kubernetes and GKE environments. For a high-level overview of the issues, please refer to our blog on the Palo Alto Networks site, [Unit 42 Discloses Newly Discovered Vulnerabilities in GKE Autopilot](https://www.paloaltonetworks.com/blog/2022/03/gke-autopilot-vulnerabilities).

Palo Alto Networks customers receive protections from the issues discussed below through the Kubernetes admission control and auditing features of [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud).

Affected Product | Google Kubernetes Engine (GKE) Autopilot  
---|---  
Related Unit 42 Topics | [Container Escape](https://unit42.paloaltonetworks.com/tag/containers/), [Cloud](https://unit42.paloaltonetworks.com/category/cloud/)  
  
## **Background on GKE Autopilot**

Autopilot is a new mode of operation in GKE, providing what Google describes as a "hands-off" Kubernetes experience. In GKE Standard, customers manage their cluster infrastructure and pay per node. With GKE Autopilot, Google takes care of cluster infrastructure, and customers only pay for their running pods. This allows customers to focus on their applications, cutting operational costs.

In a nutshell, managed cluster infrastructure means Google automatically:

  1. Provisions and adjusts the number of nodes according to your pods' resource consumption.
  2. Enforces a built-in policy to ensure the cluster adheres to secure best practices and can be safely managed by Google.

Below is a simplified diagram of Autopilot's architecture. Components unique to Autopilot are colored in green and shown with a number corresponding to their role from the list above. Unlike GKE Standard, where nodes are visible as Compute Engine VMs, Autopilot nodes are completely managed by Google, thus colored in green.

Figure 1. GKE Autopilot architecture.

As seen in Figure 1, two components enforce Autopilot's policy. First is an [OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs/) validating admission webhook, an open-source project widely used for policy enforcement in Kubernetes. The second is a proprietary Kubernetes authorization mode named GKEAutopilot, which Google implemented by modifying the Kubernetes source code.

The built-in policy serves two [purposes](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#limits): (a) prevent users from accessing cluster components managed by Google, like nodes; and (b) uphold secure Kubernetes best practices. For example, Autopilot forbids running privileged containers, fulfilling both (a) and (b).

Figure 2. Autopilot's built-in policy prevents privileged containers (Gatekeeper).

Autopilot's policy goes beyond preventing container escapes. Figures 3, 4, and 5 highlight a few interesting examples. [GKE's documentation](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#limits) lists every limit enforced by the policy.

Figure 3. The kube-system namespace is managed, customers are limited to read-only access. Figure 4. Users cannot list or create mutating admission webhooks. Figure 5. External IP services are denied to protect against CVE-2020-8554.

Reading the error messages in the Figures above, you can see that Gatekeeper prevented the operations in Figures 2 and 5, while the GKEAutopilot authorization mode prevented the operations in Figures 3 and 4.

## **Attack Surfaces Unique to GKE Autopilot**

Autopilot's built-in policy blocks several exploitation paths out of the box, providing better security posture compared to standard Kubernetes or GKE Standard. That being said, it also creates attack surfaces unique to Autopilot:

  1. Administrators may rely on Autopilot's policy to prevent risky configurations. If attackers can somehow circumvent that policy, they may escalate privileges via methods customers expect to be blocked, like deploying a privileged container.
  2. Autopilot administrators aren't fully privileged, restricted by the built-in policy from accessing nodes and certain privileged Kubernetes APIs. If attackers can bypass Autopilot's policy, they may gain higher privileges than administrators, opening the door for invisible backdoors.

The following sections present vulnerabilities, privilege escalation techniques and persistence methods we identified that fall under these attack surfaces. Chained together, they allow a restricted user who can create a pod to (1) compromise nodes, (2) escalate privileges to an unrestricted cluster administrator and (3) install invisible and persistent backdoors to the cluster.

## **Masquerading as Allowlisted Workloads to Compromise Nodes**

Our research began at the [following paragraph](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#:~:text=Our%20intent%20is%20to%20prevent%20unintended%20access%20to%20the%20node%20virtual%20machine.%20We%20accept%20submissions%20to%20that%20effect%20through%20the%20Google%20Vulnerability%20Reward%20Program%20\(VRP\)) in Autopilot's documentation:

"Our intent is to prevent unintended access to the node virtual machine. We accept submissions to that effect through the Google Vulnerability Reward Program (VRP)..."

This seemed like an interesting challenge, and so we created an Autopilot cluster and started looking around. Autopilot installed OPA Gatekeeper onto the cluster along with several policies (called “constraints” in Gatekeeper terminology) in charge of preventing risky configurations like privileged containers. The cluster also had a [Custom Resource Definition](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) (CRD) that seemed interesting, named allowlistedworkloads.

Figure 6. Autopilot installs a Custom Resource Definition (CRD) named allowlistedworkloads

As shown earlier in Figure 2, Autopilot forbids pod configurations that could allow container escapes. To support add-ons that require some level of node access, Autopilot created a notion of allow-listed workloads. If a container matches an allow-listed workload, it's permitted to use the privileged features specified in the allowlistedworkload configuration. In June, the only allow-listed workloads were Datadog agents.

Figure 7. Datadog agent allowlistedworkload

Below is the allow-listed workload configuration for one of the Datadog agents that caught our attention. If a container specifies the listed command and image, it's allowed to mount the listed host paths in read-only volumes.

Figure 8. One of the allowlistworkloadconfiguration examples for Datadog agents.

The issue here is insufficient verification. Only checking the command and image isn't enough to ensure the container runs Datadog code. Using the following PodSpec, a container can masquerade as the Datadog agent while running attacker-controlled code, and abuse the exposed host volumes to break out.

Figure 9. Masquerading as the Datadog agent.

In the video below, a malicious user deploys a pod masquerading as the Datadog agent. The pod takes over its underlying node through the following steps:

  1. Abuse the mounted containerd socket to create a privileged container that mounts the host filesystem.
  2. Have that privileged container install a systemd service that spawns a reverse shell from the node to an attacker-controlled machine.

_Video 1. Masquerading as an allowlistedworkload to compromise the underlying node._

## **Impact of Node Compromise**

An attacker who can create a pod may exploit this issue to create malicious containers that escape and take over their underlying nodes. Autopilot users expect the platform to prevent this kind of attack, and will be caught off-guard.

Node compromise opens up the following attack vectors:

  1. The attacker immediately gains control over neighboring pods and their service account tokens, potentially escalating privileges and spreading to other [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).
  2. The attacker can query the node's [instance metadata endpoint](https://cloud.google.com/compute/docs/metadata/overview) for an access token. By default, this token provides read access to cloud storage in the customer's project.
  3. Since Autopilot administrators cannot access nodes, attackers may abuse this issue to install covert malware or cryptominers on them. However, Autopilot automatically scales nodes, so ensuring malware persists isn't straightforward.
  4. The attacker gains access to the underlying Kubelet credentials, allowing visibility to nearly all cluster objects.

Finally, because Autopilot only bills per running pods, crafty users could have abused this issue to cut some costs, running some workloads directly on nodes. We advise reducing bills in more legitimate ways.

## **Escalating to Unrestricted Administrators**

Following the trajectory of a motivated intruder, we looked for reliable methods of escalating this container escape into a full cluster takeover. By compromising a node, attackers can steal the service account tokens of neighboring pods. Naturally, it would make sense to target nodes hosting pods with powerful service accounts. These may be pods deployed by the user, or more interestingly, system pods deployed natively in all Autopilot clusters.

After examining the built-in policy, we discovered that **Autopilot completely exempts kube-system service accounts**. This made kube-system pods the most interesting targets, as stolen tokens could be used freely without worrying about the policy.

Figure 10. Autopilot's policy exempts kube-system service accounts in line 3.

To search for powerful pods in Autopilot, we created [sa-hunter](https://github.com/twistlock/sa-hunter), a Python tool that maps pods' service accounts to their Kubernetes permissions (i.e. roles and clusterroles). Existing tools link service accounts to their permissions, but don't show whether any pods actually use a given service account. Figure 11 shows an example output of sa-hunter:

Figure 11. sa-hunter output, linking running pods to their permissions.

sa-hunter found two powerful kube-system pods installed by default: stackdriver-metadata-agent-cluster-level and metrics-server. Both pods can update existing deployments, as shown in Figure 12. This privilege may appear innocent at first glance, but it is enough to escalate to full cluster admin. Interestingly, these pods are also deployed by default in GKE Standard, **making the following privilege escalation technique relevant to all GKE clusters, Standard and Autopilot**.

Figure 12. Privileged role assigned to the metrics-server pod can update deployments.

After taking over a node hosting either the stackdriver-metadata-agent-cluster-level or metrics-server pod, an attacker can harvest their service account token from the node filesystem. Armed with that token, the attacker can attain the privileges of any service account in the cluster with three simple steps:

  1. Update an existing deployment's service account to the target service account. There are a number of preinstalled deployments, any one of which can be used for this step.
  2. Add a malicious container to that deployment.
  3. Have that malicious container retrieve the target service account token mounted in the container at /run/secrets/kubernetes.io/serviceaccount/token.

Figure 13. Abusing deployment update privileges to obtain any service account's token.

For this to be a meaningful privilege escalation, the attacker would need to target a powerful service account. The kube-system namespace offers a number of preinstalled, extremely powerful service accounts to choose from. The clusterrole-aggregation-controller (CRAC) service account is probably the leading candidate, as it can add arbitrary permissions to existing cluster roles.

Figure 14. The clusterrole-aggregation-controller service account can escalate cluster roles.

After using the technique illustrated in Figure 13 to obtain CRAC's token, the attacker can update the cluster role binded to CRAC to possess all privileges. At this point, the attacker is effectively cluster admin, and is also exempt from Autopilot's policy (as seen in Figure 10).

Figure 15. The clusterrole-aggregation-controller's token can add admin privileges to itself.

Rewinding, if the attacker wants to chain this privilege escalation technique with the container escape discussed earlier, he needs to somehow schedule his breakout pod on a node hosting either the stackdriver-metadata-agent-cluster-level or metrics-server pod. Although Autopilot rejects pods that have nodeSelectors, it does permit the simplest form of node assignment — the [nodeName](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodename) field.

The nodeName field assures the breakout pod will land on the target node as long as it has adequate resources for another pod. Even if there's no room on the target node, the attacker still has a couple of options. He can either (1) watch the target node and wait for a pod to be deleted; or (2) create pods to trigger a node scale up, tricking Autopilot's autoscaler into redistributing workloads so that a powerful pod ends up on an emptier node.

## **Full Chain: Invisible Backdoors via Mutating Admission Webhooks**

Video 2 shows the full attack chain, combining the container escape with the privilege escalation route built into GKE. Following exploitation, the attacker has higher privileges than Autopilot administrators, as he's exempt from the built-in policy (as seen in Figure 10). **This level of access can be abused to install invisible and persistent backdoors** in the form of [mutating admission webhooks](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook).

Mutating admission webhooks receive any objects created or updated in the cluster, including pods and secrets. If that's not scary enough, these webhooks can also arbitrarily mutate any received object, making them a ridiculously powerful backdoor. As shown earlier in Figure 4, Autopilot administrators cannot list mutating admission webhooks, and thus will never see this backdoor.

Figure 16. Becoming a shadow administrator through an invisible mutating admission webhook.

_Video 2. Escalating from pod creation to an unrestricted administrator and an invisible backdoor_.

Figure 17. A malicious mutating admission webhook installed by abusing the reported issues. Note that seeing the backdoor required the unrestricted admin token acquired in the attack.

## **Full Chain: Impact**

Before the fixes, attackers could have exploited the presented issues to transform a limited breach into a full cluster takeover on any Autopilot cluster. Using webhooks that are invisible to users, attackers can covertly persist their administrative access, effectively becoming "shadow administrators." At that point, they could have covertly exfiltrated secrets, deployed malware or cryptominers, and disrupted workloads.

## **Other Issues**

During our research we found two additional issues that allow node compromise, but with lower impact. The first involves two service account names in the default namespace that were exempt from Autopilot's policy: csi-attacher and otelsvc. If an attacker gained control over the default namespace, it would have been possible to create these service accounts to bypass the built-in policy. The attacker could then create privileged pods to compromise nodes, and use the discussed privilege escalation technique to take over the entire cluster.

The second attack exploited [CVE-2020-8554](https://unit42.paloaltonetworks.com/cve-2020-8554/) through Load Balancer services to compromise nodes, but required admin privileges to exploit. The attack scenario here is an attacker who has already compromised an Autopilot cluster and is looking to bypass the built-in policy to establish a covert backdoor.

## **Fixes and Mitigations**

Following our advisory and over the course of the last several months, Google deployed numerous fixes and mitigations to GKE Autopilot. These prevent the reported attack and harden the platform against similar exploits.

  1. Cluster administrators can now list, view and even create mutating admission webhooks, preventing their abuse as invisible backdoors.
  2. Google hardened the verification process of allowlistedworkloads.
  3. Policy enforcement moved from OPA Gatekeeper to Google's policy controller, allowing customers to deploy their own Gatekeeper instance. Customers can now enforce their own policy on top of the built-in one. As defense-in-depth and to mitigate possible future issues, we recommend deploying the same policies you would have deployed to GKE standard.
  4. The built-in policy is no longer visible.
  5. The csi-attacher and otelsvc service accounts are no longer exempt from Autopilot's policy.
  6. Google [open-sourced a policy for OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/noupdateserviceaccount) that restricts the powerful kube-system pods abused in the attack. The policy prevents these pods from assigning a new service account to an existing pod. See GKE's [hardening guide](https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_self_modify) for more information.

We highly recommend reading [Google's official advisory](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-009), which describes the issues from Google's perspective and lists their mitigations.

## **Preventing Similar Attacks on Kubernetes Environments**

The presented attack can be classified as a Kubernetes privilege escalation, where an attacker with limited access obtains broader permissions over a cluster. This kind of follow-on attacker activity must start from an initial breach: a malicious image in your cluster supply chain, a vulnerable publicly exposed service, stolen credentials or an insider threat. Securing your cluster's software supply chain, identities and external perimeter can reduce the chances of such breaches occurring in your clusters.

Sophisticated attackers may still find creative ways to infiltrate clusters. Proactively solving common misconfigurations, like Kubelets that allow unauthenticated access, can significantly reduce the internal attack surface available to an intruder. Security controls such as NetworkPolicies and PodSecurityStandards further restrict and demoralize malicious actors.

In the presented attack chain, the attacker only had to compromise one node to take over the entire cluster. The underlying issue wasn't the node's permissions, but those of the powerful pods it hosted, which included the ability to update deployments. This permission and others may appear somehow restricted at first glance, but are equivalent to cluster admin.

**Powerful pods are still common in production clusters** : natively installed by the underlying Kubernetes platform or introduced through popular open-source add-ons. If a node hosting a powerful pod is compromised, the attacker can easily harvest the pod's powerful service account token to spread in the cluster.

Tackling powerful pods is complex, mostly because their permissions may be rightfully needed. The first step is detection — identifying whether powerful pods exist in your cluster. We hope [sa-hunter](https://github.com/twistlock/sa-hunter) can help with that, and we plan to release additional tools that focus on automating detection of powerful pods.

If you identified powerful pods in your cluster, we recommend taking one of the approaches below:

  1. If you manage the powerful pod, consider whether it's possible to strip unnecessary privileges from its service account, or scope them to specific namespaces or resource names.
  2. If these pods are part of an external solution, reach out to the relevant cloud provider or project to pursue reducing the pod's privileges. If the pod is deployed by a managed Kubernetes service, it may be possible for them to replace it with a control plane controller.
  3. Some Kubernetes permissions are too broad, meaning the pod in question may not require access to the dangerous operations its permissions expose. In that case, it may be possible to implement a policy (e.g. via OPA Gatekeeper) that prevents the pod from performing certain dangerous operations, or even better, restricts the pod to a set of allowed and expected operations.
  4. Use [Taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/), [NodeAffinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) or [PodAntiAffinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) rules to isolate powerful pods from untrusted or publicly exposed ones, ensuring they don't run on the same node.

As an example for the third approach, the following Rego policy can stop the presented privilege escalation attack. The attack abused system pods who can update deployments to replace the service account of an existing deployment to a powerful one. Inspecting the source code of these powerful pods revealed they don't need the ability to change the service account of deployments they update. The policy below capitalizes on that and forbids these pods from unexpectedly updating deployments' service accounts. [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) users on GKE are encouraged to import this policy as an [admission rule](https://docs.paloaltonetworks.com/prisma/prisma-cloud/21-04/prisma-cloud-compute-edition-admin/access_control/open_policy_agent.html#:~:text=Prisma%20Cloud%20provides%20a%20dynamic,to%20Defender%2C%20which%20enforces%20them.) set on Alert.

match[{"msg": msg}] { input.request.object.kind == "Deployment" request_by_powerful_dep_update_sa(input.request.userInfo.username) old_spec := input.request.oldObject.spec.template.spec new_spec := input.request.object.spec.template.spec new_service_account := is_updating_the_service_account(old_spec, new_spec) msg := sprintf("SA '%v' may be compromised, it unexpectedly tried to replace the serviceaccount of 'deployment/%v:%v' to '%v'", [input.request.userInfo.username, input.request.object.metadata.namespace, input.request.object.metadata.name, new_service_account]) } request_by_powerful_dep_update_sa(username) { # metrics-server pod on GKE username == "system:serviceaccount:kube-system:metrics-server" } { # stackdriver pod on older GKE clusters username == "system:serviceaccount:kube-system:metadata-agent" } is_updating_the_service_account(oldspec, newspec) = new_service_account { oldspec.serviceAccountName != newspec.serviceAccountName new_service_account := newspec.serviceAccountName } { not has_key(oldspec, "serviceAccountName") new_service_account := newspec.serviceAccountName } has_key(obj, k) { _ = obj[k] }

1234567891011121314151617181920212223242526 | match[{"msg": msg}] { input.request.object.kind == "Deployment" request_by_powerful_dep_update_sa(input.request.userInfo.username) old_spec := input.request.oldObject.spec.template.spec new_spec := input.request.object.spec.template.spec new_service_account := is_updating_the_service_account(old_spec, new_spec) msg := sprintf("SA '%v' may be compromised, it unexpectedly tried to replace the serviceaccount of 'deployment/%v:%v' to '%v'", [input.request.userInfo.username, input.request.object.metadata.namespace, input.request.object.metadata.name, new_service_account])} request_by_powerful_dep_update_sa(username) { # metrics-server pod on GKE username == "system:serviceaccount:kube-system:metrics-server"} { # stackdriver pod on older GKE clusters username == "system:serviceaccount:kube-system:metadata-agent"} is_updating_the_service_account(oldspec, newspec) = new_service_account { oldspec.serviceAccountName != newspec.serviceAccountName new_service_account := newspec.serviceAccountName} { not has_key(oldspec, "serviceAccountName") new_service_account := newspec.serviceAccountName} has_key(obj, k) { _ = obj[k]}  
---|---  
  
## **Conclusion**

As organizations migrate to Kubernetes, attackers follow suit. Recent malware samples like [Silocape](https://unit42.paloaltonetworks.com/siloscape/) indicate adversaries are evolving beyond simple techniques into advanced Kubernetes tailored attacks. Against sophisticated attackers, solely securing the cluster's perimeter may not be enough. We encourage defenders to adopt policy and audit engines that enable detection and prevention of follow-on, "stage 2" attacker activities, and we hope this research can highlight how those may look. [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) customers are encouraged to enable our Kubernetes [admission control](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/access_control/open_policy_agent.html) and [auditing](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/audit/kubernetes_auditing.html) features aimed at tackling this threat.

We'd like to thank Google for their cooperation in resolving these issues, the bounty reward and their [wonderful policy](https://bughunters.google.com/about/rules/6625378258649088#:~:text=We%20understand%20that%20some%20of%20you%20are%20not%20interested%20in%20money.%20We%20offer%20the%20option%20to%20donate%20your%20reward%20to%20an%20established%20charity.%20If%20you%20do%20so%2C%20we%20will%20double%20your%20donation%20-%20subject%20to%20our%20discretion.%20Any%20rewards%20that%20are%20unclaimed%20after%2012%20months%20will%20be%20donated%20to%20a%20charity%20of%20our%20choosing.) that doubles bounties donated to charity.

Palo Alto Networks has shared these findings, including file samples and indicators of compromise, with our fellow Cyber Threat Alliance members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org/).

### **Additional Resources**

  * [GKE Autopilot documentation](https://www.google.com/search?q=gke+autotpilot&oq=gke+autotpilot&aqs=chrome..69i57.1414j0j7&sourceid=chrome&ie=UTF-8)
  * [sa-hunter](https://github.com/twistlock/sa-hunter)
  * [Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments](https://unit42.paloaltonetworks.com/siloscape/)
  * [Protecting Against an Unfixed Kubernetes Man-in-the-Middle Vulnerability (CVE-2020-8554)](https://unit42.paloaltonetworks.com/cve-2020-8554/)

Back to top

### Tags

  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")

[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: New Linux Vulnerability CVE-2022-0492 Affecting Cgroups: Can Containers Escape? ](https://unit42.paloaltonetworks.com/cve-2022-0492-cgroups/ "New Linux Vulnerability CVE-2022-0492 Affecting Cgroups: Can Containers Escape?")

### Table of Contents

  * 

### Related Articles

  * [ Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/ "article - table of contents")
  * [ Understanding Current Threats to Kubernetes Environments ](https://unit42.paloaltonetworks.com/modern-kubernetes-threats/ "article - table of contents")
  * [ Cloud Threats on the Rise: Alert Trends Show Intensified Attacker Focus on IAM, Exfiltration ](https://unit42.paloaltonetworks.com/2025-cloud-security-alert-trends/ "article - table of contents")

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
