---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-28_fabricscape-escaping-service-fabric-and-taking-over-the-cluster.md
original_filename: 2022-06-28_fabricscape-escaping-service-fabric-and-taking-over-the-cluster.md
title: 'FabricScape: Escaping Service Fabric and Taking Over the Cluster'
category: documents
detected_topics:
- cloud-security
- command-injection
- api-security
- sso
- access-control
- otp
tags:
- imported
- documents
- cloud-security
- command-injection
- api-security
- sso
- access-control
- otp
language: en
raw_sha256: 13cf85c8d44a0af1a3f08c9126d2d025100ab944ce821480e1929622ebd6faf6
text_sha256: 65bbc68f414200b0b7e6d726dfcae8c8cb6745bbdbfc984258eb77ae33074500
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# FabricScape: Escaping Service Fabric and Taking Over the Cluster

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-28_fabricscape-escaping-service-fabric-and-taking-over-the-cluster.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, api-security, sso, access-control, otp
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `13cf85c8d44a0af1a3f08c9126d2d025100ab944ce821480e1929622ebd6faf6`
- Text SHA256: `65bbc68f414200b0b7e6d726dfcae8c8cb6745bbdbfc984258eb77ae33074500`


## Content

---
title: "FabricScape: Escaping Service Fabric and Taking Over the Cluster"
url: "https://unit42.paloaltonetworks.com/fabricscape-cve-2022-30137/"
final_url: "https://unit42.paloaltonetworks.com/fabricscape-cve-2022-30137/"
authors: ["Unit 42 (@Unit42_Intel)"]
programs: ["Microsoft"]
bugs: ["Container escape", "Local Privilege Escalation", "Cross-tenant vulnerability"]
publication_date: "2022-06-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2506
---

English

  * [English](https://unit42.paloaltonetworks.com/fabricscape-cve-2022-30137/)
  * [Japanese](https://unit42.paloaltonetworks.com/ja/fabricscape-cve-2022-30137/)

  * [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/ "Vulnerabilities")

[Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)

# FabricScape: Escaping Service Fabric and Taking Over the Cluster

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 10 min read 

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
  * [Aviv Sasson](https://unit42.paloaltonetworks.com/author/aviv-sasson/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:June 28, 2022

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
  * [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
  * [Azure](https://unit42.paloaltonetworks.com/tag/azure/)
  * [Container escape](https://unit42.paloaltonetworks.com/tag/container-escape/)
  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/)
  * [Fabricscape](https://unit42.paloaltonetworks.com/tag/fabricscape/)
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/)
  * [Service Fabric](https://unit42.paloaltonetworks.com/tag/service-fabric/)

  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/fabricscape-cve-2022-30137/?pdf=download&lg=en&_wpnonce=007ee71b73 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/fabricscape-cve-2022-30137/?pdf=print&lg=en&_wpnonce=007ee71b73 "Click here to print")

Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=FabricScape:%20Escaping%20Service%20Fabric%20and%20Taking%20Over%20the%20Cluster&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Ffabricscape-cve-2022-30137%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Ffabricscape-cve-2022-30137%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Ffabricscape-cve-2022-30137%2F&title=FabricScape:%20Escaping%20Service%20Fabric%20and%20Taking%20Over%20the%20Cluster "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Ffabricscape-cve-2022-30137%2F&text=FabricScape:%20Escaping%20Service%20Fabric%20and%20Taking%20Over%20the%20Cluster "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Ffabricscape-cve-2022-30137%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=FabricScape:%20Escaping%20Service%20Fabric%20and%20Taking%20Over%20the%20Cluster%20https%3A%2F%2Funit42.paloaltonetworks.com%2Ffabricscape-cve-2022-30137%2F "Share in Mastodon")

## Executive Summary

Unit 42 researchers identified FabricScape (CVE-2022-30137), a vulnerability of important severity in Microsoft’s [Service Fabric](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-overview) – commonly used with Azure – that allows Linux containers to escalate their privileges in order to gain root privileges on the node, and then compromise all of the nodes in the cluster. The vulnerability could be exploited on containers that are configured to have [runtime access](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-best-practices-security#removeservicefabricruntimeaccess), which is granted by default to every container.

Service Fabric hosts more than 1 million applications and runs millions of cores daily, [according to Microsoft](https://azure.microsoft.com/en-us/blog/azure-service-fabric-at-microsoft-build-2018/). It powers many Azure offerings, including [Azure Service Fabric](https://azure.microsoft.com/en-us/services/service-fabric/), [Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/database/) and [Azure CosmosDB](https://azure.microsoft.com/en-us/services/cosmos-db/), as well as other Microsoft products including [Cortana](https://www.microsoft.com/en-us/cortana) and [Microsoft Power BI](https://powerbi.microsoft.com/en-us/).

Using a container under our control to simulate a compromised workload, we were able to exploit the vulnerability on [Azure Service Fabric](https://azure.microsoft.com/en-us/services/service-fabric/), which is an Azure offering that deploys private Service Fabric clusters in the cloud. A few other exploitation attempts on Azure's offerings that are powered by managed multi tenant Service Fabric clusters have failed as Microsoft disables runtime access on containers of those offerings.

We worked closely with Microsoft (MSRC) to remediate the issue, which was fully fixed on June 14, 2022. Microsoft released a patch to Azure Service Fabric that has already mitigated the issue in Linux clusters, and also updated internal production environments of offerings and products that are powered by Service Fabric.

We advise customers running Azure Service Fabric without automatic updates enabled to upgrade their Linux clusters to the most recent Service Fabric release. Customers whose Linux clusters are automatically updated do not need to take further action.

Both Microsoft and Palo Alto Networks recommend avoiding execution of untrusted applications in Service Fabric. See [Service Fabric documentation](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-best-practices-security#hosting-untrusted-applications-in-a-service-fabric-cluster) for more information.

While we're not aware of any attacks in the wild that have successfully exploited this vulnerability, we want to urge organizations to take immediate action to identify whether their environments are vulnerable and quickly implement patches if they are.

Related Unit 42 Topics | [Containers](https://unit42.paloaltonetworks.com/tag/containers/)  
---|---  
  
## Service Fabric Overview

Service Fabric is an application hosting platform that supports different forms of packaging and managing services, including, but not limited to containers.

Microsoft had previously published documentation that Service Fabric is being used in many core Azure services:

Figure 1. A partial list of services powered by Service Fabric (as of 2019).

In 2016, in light of Service Fabric's success in internal environments, Microsoft released Azure Service Fabric as a platform as a service, allowing customers to create and manage their own dedicated Service Fabric clusters in Azure Cloud. It’s widely used by enterprises across a variety of sectors including [government](https://customers.microsoft.com/en-us/story/alaskadotpf-government-azure-iot), media, [automotive](https://news.microsoft.com/transform/bmw-launches-new-digital-mobility-experience-based-on-the-open-mobility-cloud-using-microsoft-azure/), [fashion](https://customers.microsoft.com/en-us/story/asos-retail-and-consumer-goods-azure), [transportation](https://customers.microsoft.com/en-us/story/alaska-airlines-travel-transportation-azure) and multinational conglomerates.

## Service Fabric Architecture

A general understanding of the basic architecture of Service Fabric is required in order to understand the full impact of FabricScape, so we’ll start with a quick overview of Service Fabric architecture.

A Service Fabric cluster consists of many nodes as each one runs a container engine that executes the desired containerized applications, just like Kubernetes. It supports Linux and Windows nodes and uses Docker on both while supporting [Hyper-V isolation mode](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container) in Windows nodes for maximum isolation. When deploying an application into a Service Fabric cluster, Service Fabric will deploy the application as containers according to the application manifest.

Under the hood every node runs multiple components, allowing multiple nodes to work in synergy and form a reliable and distributed cluster. There is almost no public documentation about these components, but Microsoft released Service Fabric version 6.4 [source code](https://github.com/microsoft/service-fabric) in 2018, and that allowed the public to read the code and understand the components' purposes and operations.

Figure 2. Service Fabric Linux node example.

## The Vulnerability

Service Fabric supports deploying applications as containers, and during each container initialization, a new log directory is created and mounted into each container with read and write permission. All of those directories are centralized in one path on every node. For example, in Azure Service Fabric offering, those directories are at /mnt/sfroot/log/Containers.

One of Service Fabric's components is the Data Collection Agent (DCA). Among other things, it is responsible for collecting the logs from those directories to be processed later. In order to access the directories, it needs high privileges and therefore runs as root on every node.

At the same time, it handles files that could be modified by containers. Thus, exploiting a vulnerability in the agent's mechanism that handles these files could result in a container escape and gaining root on the node. This could happen, for example, if the user runs a malicious container or package, or if a container is taken over by an attacker.

By digging into DCA's old source code, we noticed a potential race-conditioned [arbitrary write](https://cwe.mitre.org/data/definitions/123.html) in the function GetIndex (PersistedIndex.cs:48).

This function reads a file, checks that the content is in the expected format, modifies some of the content and overwrites the file with the new content.

In order to do so, it uses two sub-functions:

  * LoadFromFile – reads the file.
  * SaveToFile – writes the new data to the file.

Figure 3. GetIndex function.

This functionality results in a [symlink race](https://en.wikipedia.org/wiki/Symlink_race). An attacker in a compromised container could place malicious content in the file that LoadFromFile reads. While it continues to parse the file, the attacker could overwrite the file with a symlink to a desirable path so that later SaveToFile will follow the symlink and write the malicious content to that path.

As DCA runs as root on the node file system, it will follow the symlink and overwrite files in the node file system.

## Exploitation of CVE-2022-30137

In order to exploit the issue, an attacker needs to trigger DCA to run the vulnerable function on a file that it controls. DCA monitors the creation of specific filenames in the log directories we mentioned above, and executes different functionality for each file. One of those files is ProcessContainerLog.txt.

Figure 4. ProcessContainerLog documentation in the code.

When DCA identifies that this file was created, it executes a function that eventually runs GetIndex numerous times on paths inside the log directory, which the container can modify.

Figure 5. Monitoring ProcessContainerLog.

This means that a malicious container could trigger the execution of GetIndex on a file that it controls and try to beat the race condition in order to overwrite any path on the node filesystem.

In order to beat it consistently, we changed the malicious file to weigh 10 MB, so that it will take LoadFromFile a considerable amount of time to parse it, giving us sufficient time to overwrite it with a symlink and beat the race every single time.

At this point, we were able to exploit GetIndex from the context of the container and overwrite any file on the node.

While this behavior can be observed on both Linux containers and Windows containers, it is only exploitable in Linux containers because in Windows containers unprivileged actors cannot create symlinks in that environment.

From now on, we will focus on the exploitation of a Linux node (Ubuntu 18.04) in order to gain code execution on the node.

## Gaining Code Execution on the Node

Gaining code execution on a machine using a privileged arbitrary write vulnerability is a trivial task that can be accomplished using many techniques such as [adding malicious ssh keys](https://attack.mitre.org/techniques/T1098/004/), [adding a malicious user](https://attack.mitre.org/techniques/T1098/) or installing a [backdoor by overwriting benign binaries](https://attack.mitre.org/techniques/T1036/).

None of these techniques is applicable in this case since the write primitive to the node filesystem is weak because of two reasons:

  1. GetIndex modifies internal Service Fabric files and therefore verifies that the file (payload content) is in the right internal format before continuing to SaveToFile.
  2. The overwritten file on the node file system doesn't have execution permissions.

Figure 6. Example of the internal format.

After some digging, we figured out that the format is very similar to the format of files that contain environment variables.

Figure 7. Malicious file example.

We choose to use [/etc/environment](https://man7.org/linux/man-pages/man7/environ.7.html) for the exploitation as it contains environment variables specifying the basic environment variables for new shells but can be used by other programs. After some research, we found out that every executed job in the Linux task scheduler ([cron](https://en.wikipedia.org/wiki/Cron)) imports this file, and luckily, there is a job that is executed every minute by root on every node, meaning we could inject malicious environment variables into new processes that run as root on the node.

After digging deeper, we found that having jobs on the scheduler is not necessary for exploitation since cron executes an internal hourly job as root, which could be exploited.

Figure 8. The cron job that is executed every minute.

In order to gain code execution, we used a technique called [dynamic linker hijacking](https://attack.mitre.org/techniques/T1574/006/). We abused the LD_PRELOAD environment variable. During the initialization of a new process, the [linker](https://en.wikipedia.org/wiki/Linker_\(computing\)) loads the shared object that this variable points to, and with that, we inject shared objects to the privileged cron jobs on the node.

We wrote a dummy shared object with a function that initiates a reverse shell and added a [construction attribute](https://gcc.gnu.org/onlinedocs/gcc-4.7.0/gcc/Function-Attributes.html) so that when the shared object is loaded, it will initiate a reverse shell automatically. We compiled the shared object and copied it to the log directory in the container so that we could point LD_PRELOAD to the object path.

One minute after exploitation, we got a reverse shell in the context of root on the node.

Figure 9. Exploitation flow.

We tested this exploitation successfully on the Azure Service Fabric offering using the latest version available at that time (8.2.1124.1), on both Ubuntu 16.04 and 18.04. We were able to beat the race condition consistently and successfully break out and execute code on the node every single time.

## Cluster Takeover

Microsoft provides users an easy way to manage and interact with their Service Fabric clusters by using the [sfctl](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-cli) CLI tool.

Figure 10. Sfctl subcommands.

In order to interact and manage a cluster, users need to provide sfctl two arguments:

  1. The cluster endpoint address.
  2. A private certificate.

When executing a command, sfctl sends requests to a REST API in the cluster and uses the certificate for authentication. This API can perform [many functionalities](https://docs.microsoft.com/en-us/rest/api/servicefabric/sfclient-index) and provides a way to manage the cluster remotely. It listens on port 19080 by default in the Azure Service Fabric offering and is open to the internet so that users would be able to access it.

Figure 11. Selecting a cluster using sfctl.

Besides the API, this endpoint has a graphical interface that can be accessed by browsers if the private certificate is applied. This interface is called [Service Fabric Explorer](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-visualizing-your-cluster), and it is used as a graphical way to manage and analyze the cluster.

Figure 12. Service Fabric Explorer index page.

After gaining root privileges on the node by exploiting CVE-2022-30137, we explored the file system and found the directory /var/lib/waagent/ contains sensitive files, including the certificate that controls the whole cluster.

By applying the compromised certificate, we were able to authenticate to any of the REST API endpoints (and the load balancer) and send requests to trigger functionalities in the cluster.

We were able to use the certificate to run sfctl and manage the cluster, or even browse to the Service Fabric Explorer.

Figure 13. Testing the compromised certificate.

## Broader Impact of FabricScape

Microsoft does not publicly disclose what offerings are powered by Service Fabric but does provide a partial list as shown in Figure 1.

This means that if a malicious actor gains control over a container in Service Fabric, it would be possible to compromise the whole cluster as demonstrated above.

## Limitations

A Service Fabric cluster is single-tenant by design, and hosted applications are considered trusted. They are therefore able to access the Service Fabric runtime data by default. This access allows the applications to read data regarding their Service Fabric environment and write logs to specific locations. In order to exploit FabricScape, the compromised container must have runtime access because that is necessary for the logs directory to be accessible. If developers consider their applications as untrusted or if the cluster is multitenant, this access can be disabled for each application on the cluster separately by modifying each application manifest and setting [RemoveServiceFabricRuntimeAccess](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-best-practices-security#hosting-untrusted-applications-in-a-service-fabric-cluster) to true.

Other than our successful exploitation in Azure Service Fabric, we tested Azure Container Instances, Azure PostgreSQL and Azure Functions. All of these services can be deployed in a serverless plan and are powered by multitenant Service Fabric clusters.

We could not exploit FabricScape over those services since Azure disabled the runtime access on those services.

## Disclosure and Mitigations

We disclosed the vulnerability, including a full operational exploit, to Microsoft on Jan. 30, 2022.

Microsoft [released](https://github.com/microsoft/service-fabric/blob/master/release_notes/Service_Fabric_ReleaseNotes_90CU1.md) a fix for the issue on June 14, 2022.

We advise that customers running Azure Service Fabric without automatic updates enabled should upgrade their Linux clusters to the most recent Service Fabric release. Customers whose Linux clusters are automatically updated do not need to take further action.

Customers that use other Azure offerings that are based on managed Service Fabric clusters are safe as Microsoft has updated its software.

## Conclusion

As the trend of migrating to the cloud grows exponentially, the cloud ecosystem adapts and reinvents itself constantly to keep up with demand by developing new technologies.

As part of a Palo Alto Networks commitment to improving public cloud security, we actively invest in researching such technologies and report issues to the vendors in order to keep customers and users safe.

Back to top

### Tags

  * [Azure](https://unit42.paloaltonetworks.com/tag/azure/ "Azure")
  * [Container escape](https://unit42.paloaltonetworks.com/tag/container-escape/ "container escape")
  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")
  * [Fabricscape](https://unit42.paloaltonetworks.com/tag/fabricscape/ "fabricscape")
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")
  * [Service Fabric](https://unit42.paloaltonetworks.com/tag/service-fabric/ "Service Fabric")

[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: There Is More Than One Way to Sleep: Dive Deep Into the Implementations of API Hammering by Various Malware Families ](https://unit42.paloaltonetworks.com/api-hammering-malware-families/ "There Is More Than One Way to Sleep: Dive Deep Into the Implementations of API Hammering by Various Malware Families")

### Table of Contents

  * 

### Related Articles

  * [ The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "article - table of contents")
  * [ Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/ "article - table of contents")
  * [ Cracks in the Bedrock: Agent God Mode ](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/ "article - table of contents")

## Related Vulnerabilities Resources

![Pictorial representation of PAN-OS CVE-2026-0257. A vibrant city skyline at night, with tall skyscrapers and glowing digital beams extending into the sky, suggesting advanced technology and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/07_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) June 9, 2026 #### [Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257 ](https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/)

  * [CVE-2026-0257](https://unit42.paloaltonetworks.com/tag/cve-2026-0257/ "CVE-2026-0257")
  * [Vulnerability](https://unit42.paloaltonetworks.com/tag/vulnerability/ "vulnerability")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/ "Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257")

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

![Pictorial representation of CVE-2023-33538. Abstract image of a glowing red Wi-Fi symbol on a circuit board, with intricate patterns and a futuristic appearance.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/04_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 16, 2026 #### [A Deep Dive Into Attempted Exploitation of CVE-2023-33538 ](https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/)

  * [Botnet](https://unit42.paloaltonetworks.com/tag/botnet/ "botnet")
  * [Command injection](https://unit42.paloaltonetworks.com/tag/command-injection/ "Command injection")
  * [CVE-2023-33538](https://unit42.paloaltonetworks.com/tag/cve-2023-33538/ "CVE-2023-33538")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/ "A Deep Dive Into Attempted Exploitation of CVE-2023-33538")

![Pictorial representation of BeyondTrust vulnerability CVE-2026-1731. Digital art depicting a stylized mountain range with vibrant blue and red hues. The peaks are accentuated by glowing particles and an abstract, starry backdrop, creating a futuristic landscape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/14_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) February 19, 2026 #### [VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability (CVE-2026-1731) ](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/)

  * [Bash](https://unit42.paloaltonetworks.com/tag/bash/ "bash")
  * [CVE-2026-1731](https://unit42.paloaltonetworks.com/tag/cve-2026-1731/ "CVE-2026-1731")
  * [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/ "VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability \(CVE-2026-1731\)")

![](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/AdobeStock_1020436911-786x440.jpeg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) February 17, 2026 #### [Critical Vulnerabilities in Ivanti EPMM Exploited ](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/)

  * [CVE-2026-1281](https://unit42.paloaltonetworks.com/tag/cve-2026-1281/ "CVE-2026-1281")
  * [CVE-2026-1340](https://unit42.paloaltonetworks.com/tag/cve-2026-1340/ "CVE-2026-1340")
  * [Ivanti](https://unit42.paloaltonetworks.com/tag/ivanti/ "Ivanti")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/ "Critical Vulnerabilities in Ivanti EPMM Exploited")

![Pictorial representation of CVE-2025-0921. Digital illustration of a map of North America with interconnected glowing lines and dots symbolizing network connections across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/06_Vulnerabilities_1920x900-2-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 30, 2026 #### [Privileged File System Vulnerability Present in a SCADA System ](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/)

  * [CVE-2025-0921](https://unit42.paloaltonetworks.com/tag/cve-2025-0921/ "CVE-2025-0921")
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")
  * [SCADA](https://unit42.paloaltonetworks.com/tag/scada/ "SCADA")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/ "Privileged File System Vulnerability Present in a SCADA System")

![Pictorial representation of MongoBleed, CVE-2025-14847. Digital image featuring a glowing padlock icon superimposed on a background of streaming blue binary code, symbolizing cybersecurity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/AdobeStock_233494953-786x429.jpeg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) January 13, 2026 #### [Threat Brief: MongoDB Vulnerability (CVE-2025-14847) ](https://unit42.paloaltonetworks.com/mongobleed-cve-2025-14847/)

  * [CVE-2025-14847](https://unit42.paloaltonetworks.com/tag/cve-2025-14847/ "CVE-2025-14847")
  * [MongoDB](https://unit42.paloaltonetworks.com/tag/mongodb/ "MongoDB")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/mongobleed-cve-2025-14847/ "Threat Brief: MongoDB Vulnerability \(CVE-2025-14847\)")

![Pictorial representation of remote code execution in AI and machine learning libraries. Close-up of a woman wearing glasses and focusing intently on a computer screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/05_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 13, 2026 #### [Remote Code Execution With Modern AI/ML Formats and Libraries ](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/)

  * [Apple](https://unit42.paloaltonetworks.com/tag/apple/ "Apple")
  * [CVE-2025-23304](https://unit42.paloaltonetworks.com/tag/cve-2025-23304/ "CVE-2025-23304")
  * [CVE-2026-22584](https://unit42.paloaltonetworks.com/tag/cve-2026-22584/ "CVE-2026-22584")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/ "Remote Code Execution With Modern AI/ML Formats and Libraries")

![Pictorial representation of CVE-2025-55182 \(React\) and CVE-2025-66478 \(Next.js\). Close-up of a digital display on electronic equipment with illuminated text reading "SYSTEM HACKED" in red, set against a blurred background of blue and red lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/12/02_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) December 12, 2025 #### [Exploitation of Critical Vulnerability in React Server Components (Updated December 12) ](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/)

  * [Cobalt Strike](https://unit42.paloaltonetworks.com/tag/cobalt-strike/ "Cobalt Strike")
  * [CVE-2025-55182](https://unit42.paloaltonetworks.com/tag/cve-2025-55182/ "CVE-2025-55182")
  * [CVE-2025-66478](https://unit42.paloaltonetworks.com/tag/cve-2025-66478/ "CVE-2025-66478")

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/ "Exploitation of Critical Vulnerability in React Server Components \(Updated December 12\)")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image]()
