---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-21_gaps-in-azure-service-fabrics-security-call-for-user-vigilance.md
original_filename: 2023-06-21_gaps-in-azure-service-fabrics-security-call-for-user-vigilance.md
title: Gaps in Azure Service Fabric’s Security Call for User Vigilance
category: documents
detected_topics:
- sso
- access-control
- ssrf
- xss
- command-injection
- rate-limit
tags:
- imported
- documents
- sso
- access-control
- ssrf
- xss
- command-injection
- rate-limit
language: en
raw_sha256: 1281941a1bfaff5b479915034e0962bc8e450d3498ef49e2fba2b8e7a4b1d2b1
text_sha256: e8d8128d6d1fba5526c3ecb5387ffb221093e1b6f8223f9c5b05e57b12ed51c4
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Gaps in Azure Service Fabric’s Security Call for User Vigilance

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-21_gaps-in-azure-service-fabrics-security-call-for-user-vigilance.md
- Source Type: markdown
- Detected Topics: sso, access-control, ssrf, xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `1281941a1bfaff5b479915034e0962bc8e450d3498ef49e2fba2b8e7a4b1d2b1`
- Text SHA256: `e8d8128d6d1fba5526c3ecb5387ffb221093e1b6f8223f9c5b05e57b12ed51c4`


## Content

---
title: "Gaps in Azure Service Fabric’s Security Call for User Vigilance"
page_title: "Gaps in Azure Service Fabric’s Security Call for User Vigilance | Trend Micro (US)"
url: "https://www.trendmicro.com/en_ae/research/23/f/gaps-in-azure-service-fabric-s-security-call-for-user-vigilance.html"
final_url: "https://www.trendmicro.com/en_us/research/23/f/gaps-in-azure-service-fabric-s-security-call-for-user-vigilance.html"
authors: ["David Fiser"]
bugs: ["Cloud", "Security misconfiguration"]
publication_date: "2023-06-21"
added_date: "2023-07-17"
source: "pentester.land/writeups.json"
original_index: 1020
---

Cloud

# Gaps in Azure Service Fabric’s Security Call for User Vigilance

In this blog post, we discuss different configuration scenarios that may lead to security issues with Azure Service Fabric, a distributed platform for deploying, managing, and scaling microservices and container applications. 

By: David Fiser Jun 21, 2023 Read time:  ( words) 

[ ![Share](/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

Besides being known for deployment of containerized applications, many also know Kubernetes for container orchestration. However, it’s not the only platform that offers this service in the market. In this blog post, we will focus on Service Fabric, an orchestrator developed by Microsoft and available as a service inside the Azure cloud. As with our previous [posts on Kubernetes](https://www.trendmicro.com/vinfo/tmr/?/us/security/news/virtualization-and-cloud/the-basics-of-keeping-your-kubernetes-cluster-secure-part-1), we will look into different configuration scenarios that may lead to security issues with this service.

Azure Service Fabric is a distributed platform for deploying, managing, and scaling microservices and container applications. It is available for Windows and Linux platforms, providing multiple options for application deployment. Azure offers two types of Service Fabric services: managed and not managed. Service Fabric’s managed service puts the responsibility for the configuration and maintenance of nodes on the cloud service provider. With a traditional cluster, the user must maintain the nodes on their own; they are responsible for its proper configuration and deployment settings.

Service Fabric uses virtual machines (VMs) as cluster nodes that are running Docker as a container engine, together with Service Fabric-related services (Figure 1). The deployed applications are executed inside a container. In this entry, we will focus on the implementation of Service Fabric on the Linux operating system, Ubuntu 18.04.

![](/content/dam/trendmicro/global/en/research/23/f/gaps-in-azure-service-fabric%E2%80%99s-security-call-for-user-vigilance/ServiceFabricSecurity-Figure1.png)  
Figure 1. A simplified diagram of Service Fabric’s cluster deployment

Creating a Service Fabric cluster (Figure 2) requires a username and password, among other fields. These credentials are used to access a node.

![](/content/dam/trendmicro/global/en/research/23/f/gaps-in-azure-service-fabric%E2%80%99s-security-call-for-user-vigilance/ServiceFabricSecurity-Figure2.png)  
Figure 2. Cluster creation step

#### Deploying applications

A script generated using [Service Fabric’s official command-line interface (CLI)](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-cli) is used for application deployment. The configuration itself is saved inside _ServiceManifest_ and _ApplicationManifest_ XML files. This could include a repository of credentials for getting data like container images, port exposure settings, and isolation modes (Figure 3). 

![](/content/dam/trendmicro/global/en/research/23/f/gaps-in-azure-service-fabric%E2%80%99s-security-call-for-user-vigilance/ServiceFabricSecurity-Figure3.png)  
Figure 3. Registry credentials within the container deployment configuration

#### Client certificate

To establish communication with the cluster, a user must authenticate using a client certificate that is generated for the cluster. This certificate is used for accessing the dashboard and deploying CLI applications. It is essential to ensure confidentiality of this certificate, as its exposure would compromise the full cluster.

To model threat scenarios, we simulated a user code vulnerability that compromises the container and spawns a reverse shell. This can be considered a simulation of lateral movement that potential attackers could perform. Following a security mindset with [Zero Trust](https://www.trendmicro.com/vinfo/tmr/?/us/security/definition/zero-trust) policies and an Assume Breach paradigm, we should emphasize quoted paragraph from [Azure’s documentation](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-best-practices-security):

“ _A Service Fabric cluster is single tenant by design and hosted applications are considered trusted. Applications are, therefore, granted access to the Service Fabric runtime, which manifests in different forms, some of which are: environment variables pointing to file paths on the host corresponding to application and Fabric files, host paths mounted with write access onto container workloads, an inter-process communication endpoint which accepts application-specific requests, and the client certificate which Fabric expects the application to use to authenticate itself.”_

This, of course, contradicts the Assume Breach paradigm. The presence of sensitive information was confirmed: During our container environment analysis, we noticed the presence of several read-only mounts containing readable information about the cluster, one of which included credentials used to log into the container registry (Figure 4).

![](/content/dam/trendmicro/global/en/research/23/f/gaps-in-azure-service-fabric%E2%80%99s-security-call-for-user-vigilance/ServiceFabricSecurity-Figure4.png) Figure 4. Container registry credentials that were among the information leaked when using process isolation

Notably, the selected isolation used for container deployment was the default process isolation and no mitigation policies were applied, as we were relying on minimal default settings. This credentials leak would provide us with access to the linked private container repository; it would enable us to pull all of the container images present, or update the packages and compromise services. Hence, this scenario will be dependent [on user roles and permissions settings](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-roles?tabs=azure-cli) within the linked container registry.

After these initial findings, we switched our focus to the available network, as our container had internet access by default. Further exploration revealed that we had network access to the node, allowing us to perform a port scan on it (Figure 5).

![](/content/dam/trendmicro/global/en/research/23/f/gaps-in-azure-service-fabric%E2%80%99s-security-call-for-user-vigilance/ServiceFabricSecurity-Figure5.png)  
Figure 5. List of open ports on the Service Fabric node

We could see that Secure Shell (SSH) port 22 is open, running at the node of our compromised container simulation. The SSH was configured to accept public key and password authentication. The set username and password were the same as the credentials we previously used for cluster creation, allowing us to log in to the cluster node with root permission.

In a real-world scenario, an attacker would likely not know our password. However, because default password authentication is used, they would still be able to run brute-force and dictionary attacks to try to guess the password. At this stage, we would expect that key pair authentication is allowed on the node only. As the user is responsible for managing the cluster, we recommend setting this manually by accessing the node.

This functionality allowed us to access the node from the container, and after further investigation, we found out the Docker is used as a container engine and the default network mode is _set to the host_ (Figure 6).

![](/content/dam/trendmicro/global/en/research/23/f/gaps-in-azure-service-fabric%E2%80%99s-security-call-for-user-vigilance/ServiceFabricSecurity-Figure6.png)  
Figure 6. Container settings inspection

According to official [Docker documentation](https://docs.docker.com/network/host/): _“If you use the host network mode for a container, that container’s network stack is not isolated from the Docker host (the container shares the host’s networking namespace), and the container does not get its own IP-address allocated.”_

This has implications from a security perspective, as sharing the IP address with the host, together with non-restrictive firewall settings, makes the node (10.0.0.4) reachable from container by default. The node itself contains sensitive cluster information, such as the _cluster certificate that allows us to get control over the whole cluster_ (Figure 7).__

![](/content/dam/trendmicro/global/en/research/23/f/gaps-in-azure-service-fabric%E2%80%99s-security-call-for-user-vigilance/ServiceFabricSecurity-Figure7.png)  
Figure 7. Cluster-related certificates found on the node

#### Mitigation and security hardening

Mitigating attacks and limiting the attack vectors of bad actors are the foundations of securing IT systems, so encrypting communication and forcing authorization for accessing sensitive content are a must. However, as our research has shown, applications can be poorly configured and default deployments may not be inherently secure by default. Knowing this, users should be especially careful when securing application deployments.

Fortunately, Service Fabric allows us to address some of these issues using appropriate policies, which are defined within the _ApplicationManifest_ file _._ For instance, setting _ServiceFabricRuntimeAcessPolicy_ with the attribute _RemoveServiceFabricRuntimeAccess_ to ‘true’**** removes the _/mnt/sfroot/_ mount from the deployed application container; this prevents sensitive information that’s stored there from leaking in the event of compromise.

On the other hand, we were unable to use networking policies to limit network access to the node from the container. It is worth mentioning that some of the settings are also not available on Linux hosts, as shown in Figure 8.

![](/content/dam/trendmicro/global/en/research/23/f/gaps-in-azure-service-fabric%E2%80%99s-security-call-for-user-vigilance/ServiceFabricSecurity-Figure8.png)  
Figure 8. Example of a setting not supported in Linux

We were also unable to set Hyper-V process isolation for containers running on Linux hosts. Our most significant finding, in which we demonstrated how we were able to guess credentials and gain access to the node, may be mitigated by manually configuring public key cryptography access only and generating appropriate key pairs.

Given these facts, we began to explore scenarios with more serious implications, such as container escape. We evaluated the possibility of:

  * Exploiting unpatched container engine vulnerabilities (like [CVE-2019-5736](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736))
  * Exploiting unpatched Service Fabric vulnerabilities (like [CVE-2022-30137](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30137))
  * Exploiting isolation vulnerabilities, like:
  * Kernel vulnerabilities, in case of process isolation
  * Hypervisor vulnerabilities, in case of virtualization
  * Exploiting a misconfiguration or a design flaw

As most of our options seemed unlikely, and given the previous access to the node, we switched our focus to analysis of the node. This led to our [discovery](https://www.zerodayinitiative.com/advisories/ZDI-23-002/) of [CVE-2023-21531](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21531), allowing us to gain cluster access from a container.

#### Conclusion

Users should realize that their usage of cloud services doesn’t delegate security fully to their cloud service provider (CSP): Depending on the service, some configuration is necessary on the user’s end, leaving room for misconfigurations and unprotected deployments. Security comes with a price that doesn’t end with paying for CSPs; it also calls for a proactive security mindset and enforcing security practices, such as:

  * Follow the [CSP’s recommendations](/en_us/research/23/c/azure-serverless-security-risks.html) for securing environments and projects
  * Follow [the principle of least privilege](https://www.trendmicro.com/vinfo/tmr/?/us/security/news/virtualization-and-cloud/using-custom-containers-in-serverless-environments-for-better-security) for containers and applications
  * Configuring based on the Assume Preach paradigm to minimize the impact of potential breach

Following best practices that are specific to [Service Fabric](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-best-practices-security) and [container registries](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-best-practices) will help mitigate any emerging security issues. However, some applications might not be designed with Zero Trust policies in mind, so additional manual configuration and security hardening from the user may be required.

Tags

[Latest News](/en_us/research.html?category=trend-micro-research:article-type/latest-news) | [Cloud](/en_us/research.html?category=trend-micro-research:environments/cloud) | [Research](/en_us/research.html?category=trend-micro-research:article-type/research) | [Articles, News, Reports](/en_us/research.html?category=trend-micro-research:medium/article)

###  Authors 

  * David Fiser

Threat Researcher

[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ From Langflow to Monero: Inside CVE-2026-33017 Cryptominer ](/en_us/research/26/f/from-langflow-to-monero-inside-cve-2026-33017-cryptominer.html)
  * [ PeopleSoft PeopleTools Pre-Authentication RCE: A PSIGW SSRF Chain That Executes Inside the JVM ](/en_us/research/26/f/PeopleTools.html)
  * [ Router Roulette: Cybercriminals and Nation-States Sharing Compromised Networks ](/en_us/research/24/e/router-roulette.html)

[ See all articles ](/en_us/research.html)

[ ](/en_us/research.html)
