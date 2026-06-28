---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-09_finding-azurescape-cross-account-container-takeover-in-azure-container-instances.md
original_filename: 2021-09-09_finding-azurescape-cross-account-container-takeover-in-azure-container-instances.md
title: Finding Azurescape – Cross-Account Container Takeover in Azure Container Instances
category: documents
detected_topics:
- command-injection
- cloud-security
- jwt
- access-control
- ssrf
- sso
tags:
- imported
- documents
- command-injection
- cloud-security
- jwt
- access-control
- ssrf
- sso
language: en
raw_sha256: 1fd194494ef475513893b05bb61fad67d56ccf2778a5d3e0fdf9079d2359f37c
text_sha256: 301813369f0a40672cc0b5d18e47a6b09fd2ac37004433fc817d85f5f197747b
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Finding Azurescape – Cross-Account Container Takeover in Azure Container Instances

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-09_finding-azurescape-cross-account-container-takeover-in-azure-container-instances.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, jwt, access-control, ssrf, sso
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `1fd194494ef475513893b05bb61fad67d56ccf2778a5d3e0fdf9079d2359f37c`
- Text SHA256: `301813369f0a40672cc0b5d18e47a6b09fd2ac37004433fc817d85f5f197747b`


## Content

---
title: "Finding Azurescape – Cross-Account Container Takeover in Azure Container Instances"
page_title: "Cross-Account Container Takeover in Azure Container Instances"
url: "https://unit42.paloaltonetworks.com/azure-container-instances/"
final_url: "https://unit42.paloaltonetworks.com/azure-container-instances/"
authors: ["Unit 42 (@Unit42_Intel)"]
programs: ["Microsoft"]
bugs: ["Container takeover", "Container escape", "Privilege escalation", "Cloud"]
publication_date: "2021-09-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3329
---

English

  * [English](https://unit42.paloaltonetworks.com/azure-container-instances/)
  * [Japanese](https://unit42.paloaltonetworks.com/ja/azure-container-instances/)

  * [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")

[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)

# Finding Azurescape – Cross-Account Container Takeover in Azure Container Instances

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 14 min read 

Related Products

[![Prisma Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Cloud](https://unit42.paloaltonetworks.com/product-category/prisma-cloud/ "Prisma Cloud")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
  * [Yuval Avrahami](https://unit42.paloaltonetworks.com/author/yuval-avrahami/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:September 9, 2021

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
  * [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
  * [Azure](https://unit42.paloaltonetworks.com/tag/azure/)
  * [Azurescape](https://unit42.paloaltonetworks.com/tag/azurescape/)
  * [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/)
  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/)
  * [CVE-2018-1002102](https://unit42.paloaltonetworks.com/tag/cve-2018-1002102/)
  * [CVE-2019-5736](https://unit42.paloaltonetworks.com/tag/cve-2019-5736/)
  * [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/)
  * [RunC](https://unit42.paloaltonetworks.com/tag/runc/)

  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/azure-container-instances/?pdf=download&lg=en&_wpnonce=007ee71b73 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/azure-container-instances/?pdf=print&lg=en&_wpnonce=007ee71b73 "Click here to print")

Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Finding%20Azurescape%20–%20Cross-Account%20Container%20Takeover%20in%20Azure%20Container%20Instances&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fazure-container-instances%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fazure-container-instances%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fazure-container-instances%2F&title=Finding%20Azurescape%20–%20Cross-Account%20Container%20Takeover%20in%20Azure%20Container%20Instances "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fazure-container-instances%2F&text=Finding%20Azurescape%20–%20Cross-Account%20Container%20Takeover%20in%20Azure%20Container%20Instances "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fazure-container-instances%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Finding%20Azurescape%20–%20Cross-Account%20Container%20Takeover%20in%20Azure%20Container%20Instances%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fazure-container-instances%2F "Share in Mastodon")

## **Executive Summary**

[Azure Container Instances](https://azure.microsoft.com/en-us/services/container-instances/) (ACI) is Azure's Container-as-a-Service (CaaS) offering, enabling customers to run containers on Azure without managing the underlying servers. Unit 42 researchers recently identified and disclosed critical security issues in ACI to Microsoft. A malicious Azure user could have exploited these issues to execute code on other users' containers, steal customer secrets and images deployed to the platform, and possibly abuse ACI's infrastructure for cryptomining. Researchers named the vulnerability **Azurescape – the first cross-account container takeover in the public cloud**.

Azurescape allowed malicious users to compromise the multitenant [Kubernetes](https://kubernetes.io/) clusters hosting ACI, establishing full control over other users' containers. This post covers the research process, presents an analysis of the issue and suggests best practices for securing Kubernetes, with a focus on multitenancy, that could help prevent similar attacks.

Microsoft patched ACI shortly after our disclosure. Unit 42 has no knowledge of Azurescape exploited in the wild. As a precautionary measure, if you run containers on ACI, we recommend revoking any privileged credentials that were deployed to the platform before Aug. 31, 2021, and checking their access logs for irregularities.

For a high-level overview of Azurescape, please refer to our corporate blog, “[What You Need to Know About Azurescape](https://www.paloaltonetworks.com/blog/2021/09/azurescape).”

## **Background on Azure Container Instances**

Azure Container Instances (ACI) was [released](https://azure.microsoft.com/en-us/blog/announcing-azure-container-instances/) in July 2017 and was the first Container-as-a-Service (CaaS) offering by a major cloud provider. With ACI, customers can deploy containers to Azure without managing the underlying infrastructure. ACI takes care of scaling, request routing and scheduling, providing a serverless experience for containers.

Azure’s website described ACI by saying, "Develop apps fast without managing virtual machines or having to learn new tools – it's just your application, in a container, running in the cloud."

Internally, ACI is built on multitenant clusters that host customer containers. Originally those were Kubernetes clusters, but over the past year, Microsoft started hosting ACI on Service Fabric Clusters as well. The issues presented here affect ACI on Kubernetes, and the rest of the post will only reference that architecture. According to our tests, in which we deployed several thousand containers to the platform, at the time of disclosure Kubernetes hosted around 37% of newly created containers in ACI.

Figure 1. ACI hosted on multitenant Kubernetes clusters.

In multitenant environments like ACI, you need to enforce a strong boundary between tenants. In ACI, that boundary is the node virtual machine. Each customer container runs in a Kubernetes pod on a dedicated, single-tenant node. This Kubernetes multitenancy approach is often called node-per-tenant.

## **Azurescape Attack Scenario**

ACI is built to defend against malicious neighbors. Since practically anyone can deploy a container to the platform, ACI must ensure that malicious containers cannot disrupt, leak information, execute code or otherwise affect other customers' containers. These are often called cross-account or cross-tenant attacks.

Figure 2. Cross-account attack scenario.

The following sections cover our research into cross-account attacks in ACI. We identified a cross-tenant attack through which a malicious Azure customer could escape their container, acquire a privileged Kubernetes service account token and take over the Kubernetes [api-server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver), thus establishing complete control over the multitenant cluster and all customer containers running within it.

## **Escaping Our Container**

CaaS offerings are notoriously hard to look into. Users are only exposed to their container environment, and access to the local network is disabled through firewalls. To better understand how CaaS platforms run our containers, we created WhoC. [WhoC](https://github.com/twistlock/whoc) is a container image that reads the container runtime executing it. It's based on a rarely discussed design flaw in Linux containers allowing them to read the underlying host's container runtime. The idea is quite similar to [the infamous](https://unit42.paloaltonetworks.com/breaking-docker-via-runc-explaining-cve-2019-5736/) [CVE-2019-5736](https://nvd.nist.gov/vuln/detail/CVE-2019-5736), except that instead of overwriting the host's runtime, you read it.

By deploying WhoC to ACI, we were able to retrieve the container runtime used in the platform. Unsurprisingly, we found [runC](https://github.com/opencontainers/runc), the industry standard container runtime. What caught us off guard was the version, as shown in Figure 3.

Figure 3. Container runtime used in ACI.

RunC v1.0.0-rc2 was released on Oct. 1, 2016, and was vulnerable to at least two container breakout CVEs. Back in 2019, we analyzed one of these vulnerabilities, CVE-2019-5736. Our blog post, “[Breaking out of Docker via runC – Explaining CVE-2019-5736](https://unit42.paloaltonetworks.com/breaking-docker-via-runc-explaining-cve-2019-5736/),” shared our analysis and a proof-of-concept (PoC) exploit for it.

Once we discovered the presence of this old version of runC in ACI, we took the PoC container image developed then, polished it and deployed it to ACI. We successfully broke out of our container and gained a [reverse shell](https://docs.paloaltonetworks.com/prisma/prisma-cloud/20-12/prisma-cloud-compute-edition-admin/runtime_defense/incident_types/reverse_shell.html) running as root on the underlying host, which turned out to be a Kubernetes node.

Figure 4. Exploiting CVE-2019-5736 to escape our ACI container.

While we escaped our container, we were still within the tenant boundary – the node VM. CaaS platforms are designed to withstand sophisticated attackers who possess kernel vulnerabilities enabling privilege escalation and container breakout. A malicious container breaking out is a somewhat expected threat, tolerated through node-level isolation.

Figure 5. Out of the container, still inside our dedicated node.

## **Scouting the Node Environment**

Looking around the node, we could verify our container was the only customer container. Using the [Kubelet](https://kubernetes.io/docs/concepts/overview/components/#kubelet) credentials, we listed the pods and nodes in the cluster. The cluster hosted around 100 customer pods and had about 120 nodes. Each customer was assigned a Kubernetes namespace where their pod ran; ours was caas-d98056cf86924d0fad1159XXXXXXXXXX.

We saw that the node's Kubelet allowed anonymous access, so we tried to access Kubelets on neighboring nodes. All attempted requests to access neighboring nodes timed out, probably due to a firewall configuration that prevented communication between worker nodes.

Nodes had a reference to the cluster name in a kubernetes.azure.com/cluster label, with the following format: CAAS-PROD-<LOCATION>-LINUX-<ID>.

Figure 6. Cluster name.

We deployed a few breakout containers which landed on different Kubernetes clusters. Each cluster was found to have a unique cluster ID ranging between 1-125, indicating that each location (e.g. Western Europe) hosted a few dozen clusters.

### Kubernetes 1-days

Next, we examined the cluster's Kubernetes version.

Figure 7. ACI Kubernetes version.

ACI was hosted on clusters running either Kubernetes v1.8.4, v1.9.10 or v1.10.9. These versions were released between November 2017 and October 2018 and are vulnerable to multiple publicly known vulnerabilities. Running older Kubernetes versions is considered bad practice, but it doesn't necessarily entail a security issue within ACI. If no past issues are exploitable from the context of a malicious node, then there's no security impact.

We started going over past Kubernetes issues, searching for ones that would allow our compromised node to escalate privileges or gain access to other nodes. We identified one that looked promising – [CVE-2018-1002102](https://github.com/kubernetes/kubernetes/issues/85867).

### Kubernetes CVE-2018-1002102

The [api-server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver) occasionally reaches out to [Kubelets](https://kubernetes.io/docs/concepts/overview/components/#kubelet). For example, when servicing a kubectl exec <pod> <cmd> command, the api-server will defer the request to the appropriate Kubelet's /exec endpoint.

CVE-2018-1002102 marks a security issue in how the api-server communicated with Kubelets – it would accept redirects. By redirecting the api-server's requests to another node's Kubelet, a malicious Kubelet can spread in the cluster. Figure 8 shows the basic flow of the vulnerability:

Figure 8. CVE-2018-1002102 flow.

The prerequisites for exploitation are:

  1. A vulnerable api-server version: ✓
  2. A compromised node: ✓
  3. A way to make the api-server contact the compromised node. For example, this can be accomplished by issuing a kubectl exec to a pod on the compromised node: **?**

As it turns out, ACI also fulfilled the third prerequisite. ACI supports executing commands on uploaded containers via the az container exec [command](https://docs.microsoft.com/en-us/cli/azure/container?view&#61;azure-cli-latest#az_container_exec), which mirrors kubectl exec.

az container exec --name <my-container> \--exec-command <command>

We proceeded to create a custom Kubelet image that exploits CVE-2018-1002102, redirecting incoming exec requests to pods on other nodes. To maximize impact, we configured it to target the api-server pod, and finally, ran az container exec my-ctr --exec-command /bin/bash, with the expectation of establishing a shell on the api-server container. The command just failed.

After some debugging, we noticed the redirection operation only works if the target container is hosted on the same node. This effectively nullifies the attack, since we can't spread to other nodes. Examining the [patch](https://github.com/kubernetes/kubernetes/pull/66516) for CVE-2018-1002102, this was actually the fix for the vulnerability. At this point, something didn't add up. We had already verified the api-server version was vulnerable to CVE-2018-1002102, and we didn't understand why it appeared to include the fix.

Reexamining the exec requests arriving at the node helped shed some light on what was going on. We expected the requests to arrive from the api-server IP, as illustrated in Figure 8. Surprisingly, the requests originated from a pod dubbed the 'bridge' running in the default namespace.

Figure 9. Kubelet connections during an `az container exec` session.

We discovered that ACI moved the handling of exec requests from the api-server to a custom service. This was probably implemented by routing az container exec commands to the bridge pod instead of to the api-server.

Figure 10. Bridge pods handle execs in ACI.

The bridge image tag was master_20201125.1, indicating it was updated after CVE-2018-1002102. Judging from its recent build time and its refusal to redirect exec requests, it appears that CVE-2018-1002102's patch was ported to the bridge. Microsoft deserves credit for noticing a vulnerability affects their custom bridge pod and patching accordingly. Nicely done!

It's worth mentioning that CVE-2018-1002102 can also be exploited in other cases, for instance, when a client asks a malicious Kubelet to retrieve container logs (e.g. kubectl logs). This is actually relevant for ACI, where this functionality is implemented via the az container logs [command](https://docs.microsoft.com/en-us/cli/azure/container?view=azure-cli-latest#az_container_logs). But as with exec requests, ACI deferred the handling of log retrieval to a dedicated pod appropriately named log-fetch. And as with the bridge pod, a fix for CVE-2018-1002102 was also ported to the log-fetch pod, preventing exploitation.

## **Escalating to Cluster Admin**

CVE-2018-1002102 was off the table, but we did notice something odd while debugging the exploit. The exec requests arriving at the node included an Authorization header carrying a Kubernetes service account token, as shown in Figure 11.

Figure 11. Bridge sends 'exec' request with service account token.

Finding a token here was surprising. As mentioned earlier, Kubelets in the cluster were configured to allow anonymous access, so there was no need for requests to authenticate via a token. Perhaps this was a relic of an older implementation.

Kubernetes service account tokens are unencrypted JSON Web Tokens (JWTs), so they're [decodable](https://jwt.io/). As seen below, the received token is a service account token for the 'bridge' service account. This makes sense given the request originated from the bridge pod.

Figure 12. Bridge service account token, decoded.

If you run Kubernetes, be careful to whom you send your service account tokens: Anyone who receives a token is free to use it and masquerade as its owner. Token thieves are likely to be very interested in the permissions of their stolen tokens. The api-server exposes two APIs that allow clients to query for their permissions, SelfSubjectAccessReview and SelfSubjectRulesReview. And kubectl provides kubectl auth can-i as a convenient way of accessing these APIs.

Here are the privileges of the 'bridge' token in the default namespace:

Figure 13. Bridge token permissions – default namespace.

Looking at other namespaces, the permissions are consistent, indicating they're cluster-wide (as opposed to namespace-scoped). Below are the token's permissions in the kube-system namespace. Try to identify a permission that would allow us to spread in the multitenant cluster:

Figure 14. Bridge token permissions – kube-system namespace.

Seasoned Kubernetes security folks may have identified the pods/exec privilege, indicating that the token can be used to execute commands on any pod in the cluster – including the api-server pod! Figure 15 shows the token opening a shell on the api-server container:

Figure 15. Using the bridge's token to pop a shell on the api-server.

**We just completed a dangerous cross-account attack. With code execution on the api-server, we're now cluster admins with full control over the multitenant cluster and all customer containers within it.**

## Azurescape Attack Summary

Let's summarize the steps through which a malicious Azure customer could have gained administrative privileges over multitenant Kubernetes clusters hosting ACI:

  1. Deploy an image exploiting CVE-2019-5736 to ACI. The malicious image breaks out upon execution and establishes code execution on the underlying node.
  2. On the node, monitor traffic on the Kubelet port, port 10250, and wait for a request that includes a JWT token in the Authorization header.
  3. Issue az container exec to run a command on the uploaded container. The bridge pod will now send an exec request to the Kubelet on the compromised node.
  4. On the node, extract the bridge token from the request's Authorization header and use it to pop a shell on the api-server.

The attack is demonstrated in the following video:  
  
Video 1: From malicious container to full cluster admin.

## **Impact of the Attack**

A malicious Azure user could have compromised the multitenant Kubernetes clusters hosting ACI. As cluster administrator, an attacker could execute commands in other customer containers, exfiltrate secrets and private images deployed to the platform, or deploy cryptominers. A sophisticated adversary would further investigate the detection mechanisms protecting ACI to try to avoid getting caught.

## **The Fix**

We responsibly disclosed all the above findings to Microsoft. Consequently Microsoft released a patch to ACI. The bridge pod no longer sends its service account token to nodes when issuing exec requests, preventing the reported cross-tenant attack.

## **Another Route to Admin – Bridge SSRF**

After reporting the token issue, we wanted to make sure there aren't other ways to escalate to cluster admin. After extensive research, we were able to identify such a way. At this point Microsoft reduced the share of ACI containers running on Kubernetes; only around 10% of regions defaulted to Kubernetes clusters. That being said, some features were only supported on Kubernetes, for example [gitRepo volumes](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-volume-gitrepo). If an ACI container used such features, it was deployed on a Kubernetes cluster. Other features meant containers were likely to land on Kubernetes. That was the case for containers in private [virtual networks](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-vnet).

The second issue we discovered was a server-side request forgery (SSRF) vulnerability in the bridge pod.

When a bridge pod services an az container exec <ctr> <cmd> command, it sends a request to the appropriate Kubelet's /exec endpoint. The bridge constructs the request according to the [API specification of the Kubelet's /exec endpoint](https://github.com/kubernetes/kubernetes/blob/8088b3e67d3f917a94b4ac530579c22cd7688fe6/pkg/kubelet/server/server.go#L421), resulting in the following URL:

https://<nodeIP>:10250/exec/<customer-namespace>/<customer-pod>/<customer-ctr>?command=<url-encoded-cmd>&error=1&input=1&output=1&tty=1

The bridge must somehow fill in the missing parameters enclosed in <>. As it turns out, the value of <nodeIP> is retrieved from the customer pod's status.hostIP field. That was quite interesting to discover, since nodes are authorized to update the status of their pods (in order, for example, to update their pod's status.state field to Running, Terminated, etc).

We tried changing our pod's status.hostIP field using the compromised node's credentials. It worked, but after a second or two the api-server corrected the hostIP field to its original value. Although the change didn't persist, nothing prevented us from repeatedly updating this field.

We wrote a small script that repeatedly updates our pods' status, and used it to set the status.hostIP field to 1.1.1.1. We then issued an az container exec command. The command failed, verifying the bridge sent the exec request to 1.1.1.1 instead of the real node IP. We started thinking about which specially crafted hostIP could trick the bridge into executing a command on other pods.

Simply setting the pod's status.hostIP to another node's IP wouldn’t have achieved anything. Kubelets only accept requests that point to a container they host. Even if the bridge sends the exec request to another Kubelet's IP, the URL will still point to our namespace, pod name and container name.

We then realized the api-server doesn't actually verify that the status.hostIP value is a valid IP, and would accept any string – including URL components. After a few attempts, we came up with a hostIP value that would trick the bridge into executing a command on the api-server container, instead of our container:

<apiserver-nodeIP>:10250/exec/kube-system/<apiserver-pod>/<apiserver-container>?command=<url-encoded-command>&error=1&input=1&output=1&tty=1#

This hostIP value will cause the bridge to send the exec request to the following URL:

https://**< apiserver-nodeIP>:10250/exec/kube-system/<apiserver-pod-name>/<apiserver-ctr>?command=<url-encoded-command>&error=1&input=1&output=1&tty=1#**:10250/exec/<customer-namespace>/<customer-pod-name>/<customer-ctr-name>?command=<command>&error=1&input=1&output=1&tty=1

The # suffix ensures the rest of the URL is treated as a [URI fragment](https://en.wikipedia.org/wiki/URI_fragment) and is effectively ignored. We set our pod's status.hostIP to this value and issued a command via az container exec. The attack worked! Instead of a shell to our container, we were presented with a shell to the api-server container. The full attack can be seen in the following video:

Video 2: Tricking the bridge into opening a shell on the api-server.

The impact here is exactly the same as with the previous attack – full administrative control over the multitenant cluster. We reported this issue to MSRC as well, resulting in a patch to ACI. The bridge now verifies that a pod's status.hostIP field is a valid IP before sending an exec request.

## **Conclusion**

Cross-account vulnerabilities are often described as a "nightmare" scenario for the public cloud. Azurescape is evidence that they're more real than we'd like to think. Cloud providers invest heavily in securing their platforms, but it's inevitable that unknown zero-day vulnerabilities would exist and put customers at risk. Cloud users should take a defense-in-depth approach to cloud security to ensure breaches are contained and detected, whether the threat is from the outside or from the platform itself.

As part of the commitment of Palo Alto Networks to advancing public cloud security, we actively invest in public cloud research that includes advanced threat modeling and vulnerability testing of cloud platforms and related technologies. We hope such research can illustrate how cross-account attacks may look in the wild, which can translate into suitable mitigations and detection mechanisms.

We'd like to thank Microsoft’s MSRC for quickly patching the reported issues and professionally handling the disclosure process, as well as for the bounty rewards. Cooperative penetration testing and bug bounty programs help secure the cloud services we all rely on.

### Preventing Similar Attacks on Kubernetes Environments

From the perspective of a Kubernetes defender, several best practices, mitigations and policies can help prevent or detect features of similar attacks:

  * Keep your cluster infrastructure up to date and prioritize patches by severity and context.
  * Refrain from sending privileged service accounts tokens to anyone but the api-server. If a recipient is compromised, an attacker can masquerade as the token owner.
  * Enable [BoundServiceAccountTokenVolume](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#bound-service-account-token-volume). This recently graduated feature gate ensures token expiration is bound to its pod. When a pod terminates, its token is no longer valid, minimizing the impact of token theft.
  * Deploy policy enforcers to monitor and prevent suspicious activity in your clusters. Configure them to alert on service accounts or nodes that query the SelfSubjectAccessReview or SelfSubjectRulesReview APIs for their permissions. [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) customers can download a [relevant rule template](https://github.com/twistlock/sample-code/blob/master/opa-rego-policies/suspicious-selfsubjectreview.rego) and enforce it via the built-in [admission control for Kubernetes](https://docs.paloaltonetworks.com/prisma/prisma-cloud/21-04/prisma-cloud-compute-edition-admin/access_control/open_policy_agent.html). We recommend setting the rule to Alert. Others can rely on open-source tools such as OPA Gatekeeper.

To expand on the last point, we see adversaries actively abusing the SelfSubjectReview APIs to inspect the privileges of stolen Kubernetes credentials. Daniel Prizmant, a fellow researcher, recently observed the [Siloscape](https://unit42.paloaltonetworks.com/siloscape/) malware leveraging these APIs to retrieve the permissions of the node it compromised, and then using them to determine whether to continue its campaign against the cluster. We reported this behaviour to MITRE, and it will be included in the next release of [ATT&CK for Containers](https://attack.mitre.org/matrices/enterprise/containers/) as the Permission Group Discovery technique.

Secure multitenancy in Kubernetes is challenging, even for cloud providers. Hosting services, cloud providers and CI/CD services implementing multitenancy on Kubernetes should consider the following when designing their platforms:

  * Refrain from exposing cluster credentials within the tenant boundary. Malicious tenants may abuse these credentials to fuel further escalation or collect information on other tenants and the platform itself.
  * Assume a malicious tenant will break out of its container/sandbox. Think from an attacker's perspective – What could be the objectives? What would be the first moves? Implement detection mechanisms accordingly. Detection schemes should be considered a requirement in hostile multitenant environments, necessary to combat advanced persistent threats (APTs) and zero-day vulnerabilities.
  * Even if a node is compromised, it shouldn't be able to move laterally and compromise other nodes. Ensure nodes are least privileged by enabling the [NodeRestiction](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#noderestriction) admission controller. Set up firewall rules to prevent communication between nodes hosting customer containers.

## Additional Resources

  * [What You Need to Know About Azurescape](https://www.paloaltonetworks.com/blog/2021/09/azurescape)
  * [Coordinated disclosure of vulnerability in Azure Container Instances Service](https://msrc-blog.microsoft.com/2021/09/08/coordinated-disclosure-of-vulnerability-in-azure-container-instances-service/)
  * [Azurescape: What to Know About the Microsoft ACI Vulnerability](https://register.paloaltonetworks.com/azurescapemircosoftmci)
  * [Azure Container Instances ](https://azure.microsoft.com/en-us/services/container-instances/)
  * [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
  * [Breaking out of Docker via runC – Explaining CVE-2019-5736](https://unit42.paloaltonetworks.com/breaking-docker-via-runc-explaining-cve-2019-5736/)
  * [Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments](https://unit42.paloaltonetworks.com/siloscape/)

Back to top

### Tags

  * [Azure](https://unit42.paloaltonetworks.com/tag/azure/ "Azure")
  * [Azurescape](https://unit42.paloaltonetworks.com/tag/azurescape/ "Azurescape")
  * [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/ "Cloud Security")
  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")
  * [CVE-2018-1002102](https://unit42.paloaltonetworks.com/tag/cve-2018-1002102/ "CVE-2018-1002102")
  * [CVE-2019-5736](https://unit42.paloaltonetworks.com/tag/cve-2019-5736/ "CVE-2019-5736")
  * [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/ "Kubernetes")
  * [RunC](https://unit42.paloaltonetworks.com/tag/runc/ "runC")

[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Threat Brief: CVE-2021-26084 ](https://unit42.paloaltonetworks.com/cve-2021-26084/ "Threat Brief: CVE-2021-26084")

### Table of Contents

  * 

### Related Articles

  * [ Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/ "article - table of contents")
  * [ Essential Data Sources for Detection Beyond the Endpoint ](https://unit42.paloaltonetworks.com/detection-beyond-the-endpoint/ "article - table of contents")
  * [ Understanding Current Threats to Kubernetes Environments ](https://unit42.paloaltonetworks.com/modern-kubernetes-threats/ "article - table of contents")

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
