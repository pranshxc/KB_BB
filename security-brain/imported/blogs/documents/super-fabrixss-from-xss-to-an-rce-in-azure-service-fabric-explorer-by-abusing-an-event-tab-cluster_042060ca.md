---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-30_super-fabrixss-from-xss-to-an-rce-in-azure-service-fabric-explorer-by-abusing-an.md
original_filename: 2023-03-30_super-fabrixss-from-xss-to-an-rce-in-azure-service-fabric-explorer-by-abusing-an.md
title: 'Super FabriXss: From XSS to an RCE in Azure Service Fabric Explorer by Abusing
  an Event Tab Cluster Toggle (CVE-2023-23383)'
category: documents
detected_topics:
- xss
- cloud-security
- command-injection
- sso
- idor
- automation-abuse
tags:
- imported
- documents
- xss
- cloud-security
- command-injection
- sso
- idor
- automation-abuse
language: en
raw_sha256: 042060ca34943bb3ea6d44edb2c778faccf33d1ee9cc4a962d2c2fe5d877d6ec
text_sha256: e52df1e699bd6e3768d61d41afa4c25ac416285d15c1ca26c920dd04cf1a62fb
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Super FabriXss: From XSS to an RCE in Azure Service Fabric Explorer by Abusing an Event Tab Cluster Toggle (CVE-2023-23383)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-30_super-fabrixss-from-xss-to-an-rce-in-azure-service-fabric-explorer-by-abusing-an.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, command-injection, sso, idor, automation-abuse
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `042060ca34943bb3ea6d44edb2c778faccf33d1ee9cc4a962d2c2fe5d877d6ec`
- Text SHA256: `e52df1e699bd6e3768d61d41afa4c25ac416285d15c1ca26c920dd04cf1a62fb`


## Content

---
title: "Super FabriXss: From XSS to an RCE in Azure Service Fabric Explorer by Abusing an Event Tab Cluster Toggle (CVE-2023-23383)"
page_title: "Super FabriXss: Azure Vulnerability | Orca Security"
url: "https://orca.security/resources/blog/super-fabrixss-azure-vulnerability/"
final_url: "https://orca.security/resources/blog/super-fabrixss-azure-vulnerability/"
authors: ["Lidor Ben Shitrit"]
programs: ["Microsoft (Azure)"]
bugs: ["RCE", "XSS", "Cloud"]
publication_date: "2023-03-30"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1320
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![Super FabriXss: From XSS to an RCE in Azure Service Fabric Explorer by Abusing an Event Tab Cluster Toggle \(CVE-2023-23383\)](https://orca.security/wp-content/uploads/2023/03/Blog-graphic_Super-FabriXss_Cover-1.jpg?w=1044)

# Super FabriXss: From XSS to an RCE in Azure Service Fabric Explorer by Abusing an Event Tab Cluster Toggle (CVE-2023-23383)

[ ![Avatar of Lidor Ben Shitrit](https://orca.security/wp-content/uploads/2022/01/avatar-lidor-ben.png) Lidor Ben Shitrit  ](https://orca.security/resources/author/lidor-ben-shitrit/)

Published: Mar 30, 2023 

  * [ __](https://twitter.com/share?text=Super%20FabriXss%3A%20From%20XSS%20to%20an%20RCE%20in%20Azure%20Service%20Fabric%20Explorer%20by%20Abusing%20an%20Event%20Tab%20Cluster%20Toggle%20%28CVE-2023-23383%29&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsuper-fabrixss-azure-vulnerability%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsuper-fabrixss-azure-vulnerability%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsuper-fabrixss-azure-vulnerability%2F)
  * [ __](mailto:?Subject=Super FabriXss: From XSS to an RCE in Azure Service Fabric Explorer by Abusing an Event Tab Cluster Toggle \(CVE-2023-23383\)&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsuper-fabrixss-azure-vulnerability%2F)

Today, at BlueHat IL 2023, we proudly announced our discovery of a new vulnerability in Azure, which we’ve dubbed ‘Super FabriXss.’ In our presentation, we demonstrated how we were able to escalate a reflected XSS vulnerability in Azure Service Fabric Explorer to an unauthenticated Remote Code Execution by abusing the metrics tab and enabling a specific option in the console – the ‘Cluster Type’ toggle. For the full story, please read our blog post below.

Super FabriXss (CVE-2023-23383) is a dangerous Cross-Site Scripting (XSS) vulnerability discovered by the [Orca Research Pod](https://orca.security/about/orca-research-pod/) that affects Azure Service Fabric Explorer (SFX). This vulnerability enables unauthenticated remote attackers to execute code on a container hosted on a Service Fabric node.

Orca Security immediately reported the vulnerability to the Microsoft Security Response Center (MSRC), who investigated the issue and assigned it [CVE-2023-23383](https://nvd.nist.gov/vuln/detail/CVE-2023-23383) (CVSS 8.2) with ‘Important’ severity. Microsoft released a fix and included it in their March 2023 Patch Tuesday.

We would like to express our gratitude to Microsoft for the collaboration and prompt responses, as well as their diligent efforts in releasing a patch for the vulnerability.

In this blog post, we’ll explore the details of how we found Super FabriXss, the risks it poses, as well as provide recommendations on how to mitigate the vulnerability.

## Executive Summary

  * Orca Security found a dangerous Cross-Site Scripting (XSS) vulnerability in Azure Service Fabric Explorer (SFX) that we named ‘Super FabriXss’ and was assigned [CVE-2023-23383](https://nvd.nist.gov/vuln/detail/CVE-2023-23383) by Microsoft.
  * The Super FabriXss vulnerability enables remote attackers to leverage an XSS vulnerability to achieve remote code execution on a container hosted on a Service Fabric node without the need for authentication.
  * What started initially as a discovery of an XSS vulnerability that allowed a malicious script to be reflected off a web application, ended up being a full remote code execution (RCE) vulnerability after clicking on a crafted malicious URL and toggling the ‘Cluster’ Event Type setting under the Events tab.
  * Organizations using Service Fabric Explorer version 9.1.1436.9590**** or earlier are vulnerable to this CVE. Microsoft included a patch for this vulnerability in their March 2023 Patch Tuesday. If automatic updates are applied, no further action is needed.
  * This is the second XSS vulnerability Orca found in Azure Service Fabric Explorer. The first one was called [FabriXss](https://orca.security/resources/blog/fabrixss-vulnerability-azure-fabric-explorer/). Since the second one is much more dangerous, we decided to call it ‘Super FabriXss.’

## FabriXss? Sounds Familiar.

If the name ‘[FabriXss](https://orca.security/resources/blog/fabrixss-vulnerability-azure-fabric-explorer/)’ sounds familiar, it’s because this is the second XSS vulnerability that Orca discovered in Azure Service Fabric Explorer. However, unlike the first one, this vulnerability is much more dangerous. With Super FabriXss, a remote unauthenticated attacker can execute code on a container hosted on one of the Service Fabric nodes. This means that an attacker could potentially gain control of critical systems and cause significant damage.

## About the Super FabriXss Vulnerability

Orca uncovered a critical vulnerability in Azure Service Fabric Explorer that we were able to exploit by sending a crafted URL to any Azure Service Fabric user. The vulnerability arises from a vulnerable ‘Node Name’ parameter, which can be exploited to embed an iframe in the user’s context. This iframe then retrieves remote files from a server controlled by the attacker, eventually leading to the execution of a malicious PowerShell reverse shell. This attack chain can ultimately result in remote code execution on the container which is deployed to the cluster, potentially allowing an attacker to take control of critical systems.

**Discovery and Remediation Timeline:**

● Orca reported the vulnerability to MSRC via MSRC VDP on December 20, 2022

● MSRC started investigating the issue on December 31, 2022

● MSRC and Orca discussed the vulnerability and its impact on January 1, 2023

● MSRC and Orca discussed the case on February 8, 2023

● MSRC assigned CVE-2023-23383 to the vulnerability on March 14, 2023

● Fix was included in Microsoft March 2023 Patch Tuesday on March 14, 2023

## What is Azure Service Fabric Explorer?

[Microsoft Azure Service Fabric](https://azure.microsoft.com/en-us/products/service-fabric/) is a platform for distributed systems that enables the packaging, deployment, and management of stateless and stateful microservices and containers on a large scale. It is compatible with Windows and Linux operating systems, and can be deployed on any cloud, datacenter, or even on a personal laptop, spanning across geographic regions. 

Super FabriXss is a dangerous vulnerability that exists on Azure Service Fabric Explorer version **9.1.1436.9590** and earlier.

## Our Proof of Concept for the Super FabriXss Vulnerability

For the FabriXss vulnerability that we found a few months ago, both Linux and Windows Clusters were susceptible to Cross Site Scripting through exploitation of the ComposeNewDeployment function in the old dashboard. The SuperFabriXxs vulnerability however, only exists in the Windows Cluster. Below we describe the steps of the exploit.

### Step 1: Creating the Azure Service Fabric Cluster

We start by creating a new Azure Service Fabric with Windows Server 2016 with containers as our main cluster operation system. Once the cluster is ready, we can jump right into it and review the new (and patched) dashboard.

Similar to the previous Service Fabric Explorer (SFX) dashboard, which was patched in response to the FabriXss vulnerability CVE-2022-35829, the current dashboard is essentially the same. However, it differs in that we are no longer able to toggle between the old SFX and the new one.

![](https://orca.security/wp-content/uploads/2024/01/image-509.png?w=1168)

As we can see, there is no option to switch between the old UI and the current one –  

![](https://orca.security/wp-content/uploads/2024/01/image-510.png?w=1200)

Reviewing our Nodes list, we can see that we are currently running 6 Windows Nodes.

![](https://orca.security/wp-content/uploads/2024/01/image-511.png?w=629)

When you click on one of the Nodes in the dashboard, it takes you to an independent Node dashboard that contains information about that specific Node. This dashboard has three main tabs:

● **Essentials:** High-level overview of the Node’s current state and health.

● **Details** : More detailed information about the Node, such as its ID, load metrics, current state, and uptime status.

● **Events** : Displays various metrics related to the events that are being executed on the Node.

The Super FabriXss resides in the Events tab.

### Step 2: Observing Node Name Changes

We noticed that when the Node name is modified in the UI, it is reflected in the Node’s independent dashboard. This behavior allowed us to observe how the server handles non-existent and/or modified values for different variables.

![](https://orca.security/wp-content/uploads/2024/01/image-512.png?w=1196)

For example, we can demonstrate this by changing the name of the Node to OrcaPOC and refreshing the page. We can see that our Node is now called OrcaPOC, but no valid or existing information regarding the Node is provided. A blank space is shown next to the green health status, in contrast to the valid name shown in the previous screenshots.

![](https://orca.security/wp-content/uploads/2024/01/image-513.png?w=725)

So now that we know our name is being reflected, the next step would be to try to insert a common HTML Injection or Cross Site Scripting (XSS) payload such as –

![](https://orca.security/wp-content/uploads/2024/01/image-514.png?w=1200)

OK, so nothing unusual this far, the H1 tag was not rendered nor reflected in any unusual way. This can also be verified by reviewing the page elements:

![](https://orca.security/wp-content/uploads/2024/01/image-515.png?w=1200)

### Step 3: Toggling the Cluster Option

Switching between the different tabs reveals new capabilities that could have an effect on the Node’s newly inserted name, or may have no effect at all.

Clicking on the Events tab would show us the exact same output as we receive in the two other tabs, but what about the Node Metrics? What if an actual event would take place or was executed by the Node, how does the name reflect if at all?

![](https://orca.security/wp-content/uploads/2024/01/image-516.png?w=1038)

A single click on Event Types shows two different options: Cluster and Repair Tasks –

![](https://orca.security/wp-content/uploads/2024/01/image-517.png?w=893)

As we were testing and clicking on the two different options, we were surprised to find that clicking on ‘Cluster’ resulted in a new title being displayed as a large title, due to the effect of the <h1> tag in HTML.

![](https://orca.security/wp-content/uploads/2024/01/image-518.png?w=740)

That was an interesting output since it now set us on a new course that would ultimately lead to an RCE.

With one click to a crafted URL and enabling the Cluster Event Type under the Events tab, we triggered the rendered JS payload, generating a sequence of events that would result in a Remote Code Execution.

I’ll validate the same tag escape by providing a Javascript payload that triggers an alert box –

![](https://orca.security/wp-content/uploads/2024/01/image-519.png?w=1200)

I’ll encode the payload, and combine the final url –

![](https://orca.security/wp-content/uploads/2024/01/image-520.png?w=1200)

So now, when entering any authenticated user, whether it’s the Administrator or a Low-Priv user with the appropriate permission clicks on the URL, he could be guided to enable the Cluster Event Type under the Events tab – et voilà!

![](https://orca.security/wp-content/uploads/2024/01/image-521.png?w=1200)

In the screenshot below, it is evident that the <img> tag successfully bypassed the enclosing <div> tag, indicating that it can now be executed. This demonstrates how we managed to escape the <div> class.  

![](https://orca.security/wp-content/uploads/2024/01/image-522.png?w=550)

### Step 4: Leveraging the XSS to a RCE

After discovering the [FabriXss](https://orca.security/resources/blog/fabrixss-vulnerability-azure-fabric-explorer/) vulnerability, I realized that it might be possible to achieve a similar result by abusing XSS with the newly-found vulnerability. This involves embedding an iframe that allows the attacker to leverage the victim’s permissions to execute a desired action. However, we had a different goal this time: to gain execution command on a container hosted by one of the cluster’s nodes.

To achieve this, we had to identify a specific functionality of Service Fabric that we could exploit. After several tests and many hours of reading documentation, we eventually discovered a vulnerability that could allow us to achieve our objective.  

![](https://orca.security/wp-content/uploads/2024/01/image-523.png?w=1200)

The Start Compose Deployment Upgrade is sent via a POST request, and its purpose, as implied by its name, is to upgrade (i.e. overwrite) an existing Compose Deployment. It was as if a lightbulb had suddenly switched on in my mind, just like in a cartoon. Reviewing the mandatory Parameters, we can see that it requires a crucial parameter called _ComposeDeploymentUpgradeDescription.  
_

![](https://orca.security/wp-content/uploads/2024/01/image-524.png?w=1200)

In order to properly send the malicious payload, we need to understand what exactly the required properties are for the _ComposeDeploymentUpgradeDescription:_

![](https://orca.security/wp-content/uploads/2024/01/image-525.png?w=1115)

The key element that enables the attack scenario described is the ComposeFileContent. This object contains the specifications for the new deployment created by Docker Compose, which in turn is based on a Dockerfile. In this attack, the ComposeFileContent is modified to reference a new Docker image that is controlled by the attacker. 

The attacker creates this image using a Dockerfile that includes a CMD instruction, which will be executed when the image is built. The CMD instruction downloads a malicious .bat file that contains a PowerShell payload encoded in a specific way. This payload will then retrieve a second-stage remote file and execute it.

The purpose of this attack is to replace the legitimate Compose deployment (in this example, let’s assume it’s an IIS application) with the attacker’s container. Once the attack is successful, the attacker gains access to a custom container that has a Reverse Shell, which enables them to remotely execute commands and potentially take control of the entire cluster node where the container is hosted.

The following workflow diagram illustrates the process –

![](https://orca.security/wp-content/uploads/2024/01/image-526.png)

In the image above, an attack is demonstrated that involves sending a crafted URL to the

Service Fabric Administrator. This URL includes an iframe that uses a simple fetch request to trigger an upgrade of a Compose deployment, in this case for an IIS application. The upgrade process can be monitored in the Service Fabric dashboard, and once it is completed, the application will have a new name, such as “iisupgraded.”

There are two main phases to the attack:

1\. Once the iframe is embedded and the fetch request is triggered, the attacker’s code takes advantage of the upgrade process to overwrite the existing deployment with a new, malicious one. This new deployment includes a CMD instruction in its Dockerfile that will download a remote .bat file.

2\. Once the .bat file is downloaded, it is executed and in turn retrieves a second file that contains an encoded reverse shell. This reverse shell allows the attacker to gain remote access to the target system and potentially take control of the cluster node where the container is hosted.

It’s worth noting that this attack takes advantage of the Cluster Type Toggle options under the Events Tab in the Service Fabric platform that allows an attacker to overwrite an existing Compose deployment by triggering an upgrade with a specially crafted URL from XSS Vulnerability. By taking control of a legitimate application in this way, the attacker can then use it as a platform to launch further attacks or gain access to sensitive data or resources.

The full attack scenario can be observed in the following video:

**About Orca Security**

The [Orca Research Pod](https://orca.security/about/orca-research-pod/) has discovered several critical vulnerabilities in public cloud provider platforms and worked with cloud service providers to remediate them. We continue to explore cloud products and services to find vulnerabilities before any malicious actors do, to strengthen the Orca platform and help make the cloud a safer place for all organizations. 

Orca’s agentless [Cloud Security Platform ](https://orca.security/platform/)connects to your environment in minutes and provides 100% visibility into all your assets AWS, Azure, Google Cloud, and Kubernetes, automatically including new assets as they are added. Orca detects and prioritizes cloud risks across every layer of your cloud estate, including vulnerabilities, malware, misconfigurations, lateral movement risk, API risks, weak and leaked passwords, sensitive data at risk, and overly permissive identities.

  * [ __](https://twitter.com/share?text=Super%20FabriXss%3A%20From%20XSS%20to%20an%20RCE%20in%20Azure%20Service%20Fabric%20Explorer%20by%20Abusing%20an%20Event%20Tab%20Cluster%20Toggle%20%28CVE-2023-23383%29&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsuper-fabrixss-azure-vulnerability%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsuper-fabrixss-azure-vulnerability%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsuper-fabrixss-azure-vulnerability%2F)
  * [ __](mailto:?Subject=Super FabriXss: From XSS to an RCE in Azure Service Fabric Explorer by Abusing an Event Tab Cluster Toggle \(CVE-2023-23383\)&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fsuper-fabrixss-azure-vulnerability%2F)

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
