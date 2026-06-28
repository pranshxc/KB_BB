---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-13_azure-hdinsight-riddled-with-xss-vulnerabilities-via-apache-services.md
original_filename: 2023-09-13_azure-hdinsight-riddled-with-xss-vulnerabilities-via-apache-services.md
title: Azure HDInsight Riddled With XSS Vulnerabilities via Apache Services
category: documents
detected_topics:
- xss
- cloud-security
- command-injection
- idor
- access-control
- automation-abuse
tags:
- imported
- documents
- xss
- cloud-security
- command-injection
- idor
- access-control
- automation-abuse
language: en
raw_sha256: ba26d59320c8c34748554698055a1e045d68ad32d208e02d2c67a2c2ecb6e203
text_sha256: 970a11959bccc8819249da8cef2cc8bc1ff14141755c8d97ebf2ac92d8f4dcb1
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Azure HDInsight Riddled With XSS Vulnerabilities via Apache Services

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-13_azure-hdinsight-riddled-with-xss-vulnerabilities-via-apache-services.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, command-injection, idor, access-control, automation-abuse
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `ba26d59320c8c34748554698055a1e045d68ad32d208e02d2c67a2c2ecb6e203`
- Text SHA256: `970a11959bccc8819249da8cef2cc8bc1ff14141755c8d97ebf2ac92d8f4dcb1`


## Content

---
title: "Azure HDInsight Riddled With XSS Vulnerabilities via Apache Services"
page_title: "XSS Vulnerabilities in Azure HDInsight | Orca Security"
url: "https://orca.security/resources/blog/cross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight/"
final_url: "https://orca.security/resources/blog/cross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight/"
authors: ["Lidor Ben Shitrit"]
programs: ["Microsoft (Azure HDInsight)"]
bugs: ["Stored XSS", "Reflected XSS"]
publication_date: "2023-09-13"
added_date: "2023-09-19"
source: "pentester.land/writeups.json"
original_index: 783
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![Azure HDInsight Riddled With XSS Vulnerabilities via Apache Services](https://orca.security/wp-content/uploads/2023/09/Blog-graphic_XSS-Vulnerabilities-Azure_Cover.jpg?w=1044)

# Azure HDInsight Riddled With XSS Vulnerabilities via Apache Services

[ ![Avatar of Lidor Ben Shitrit](https://orca.security/wp-content/uploads/2022/01/avatar-lidor-ben.png) Lidor Ben Shitrit  ](https://orca.security/resources/author/lidor-ben-shitrit/)

Published: Sep 13, 2023 

  * [ __](https://twitter.com/share?text=Azure%20HDInsight%20Riddled%20With%20XSS%20Vulnerabilities%20via%20Apache%20Services&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fcross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fcross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fcross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight%2F)
  * [ __](mailto:?Subject=Azure HDInsight Riddled With XSS Vulnerabilities via Apache Services&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fcross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight%2F)

The Orca Research Pod recently discovered a total of 8 important Cross-Site Scripting (XSS) vulnerabilities within various Apache services on Azure HDInsight, a widely used managed service for open-source analytics. The identified vulnerabilities consisted of 6 Stored XSS and 2 Reflected XSS vulnerabilities, each of which could be exploited to perform unauthorized actions, varying from data access to session hijacking and delivering malicious payloads.

Orca uncovered the vulnerabilities by manipulating variables, exploiting functions, and meticulously testing possible security loopholes. Upon the discovery, we immediately informed the Microsoft Service Response Center (MSRC), who were able to reproduce the issues and prioritize their remediation. All 8 XSS vulnerabilities were fixed in the August 8th [HDInsight Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster).

In this blog, we’ll describe how we discovered the vulnerabilities and what their impact could have been on Azure HDInsight users, as well as how organizations can protect against these types of XSS vulnerabilities.

## Executive Summary

  * Orca discovered 8 important Cross-Site Scripting (XSS) vulnerabilities in Apache services, including Apache Hadoop, Spark, and Kafka, all operating under the umbrella of Azure HDInsight.
  * 6 were Stored XSS vulnerabilities and 2 were Reflected XSS vulnerabilities. 
  * All XSS vulnerabilities posed significant security risks to data integrity and user privacy in the vulnerable Apache services, including session hijacking and delivering malicious payloads, putting any user of the Apache services at risk, including Apache Hadoop, Spark, and Oozie.
  * Upon discovering the vulnerabilities, Orca promptly reported them to the MSRC team who immediately prioritized the cases. Orca and Microsoft then conducted several meetings to reproduce and remediate all issues.
  * Microsoft fixed all vulnerabilities in their [Patch Tuesday ](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-release-notes)on August 8, 2023.
  * XSS vulnerabilities can be dangerous but are nevertheless quite common. Recent examples are the [Jenkins stored XSS](https://www.jenkins.io/security/advisory/2023-07-26/), [Zimbra XSS](https://nvd.nist.gov/vuln/detail/CVE-2023-37580), and [Azure Bastion and Azure Container Registry XSS](https://orca.security/resources/blog/examining-two-xss-vulnerabilities-in-azure-services/) vulnerabilities.
  * The fact that we found 8 important XSS vulnerabilities in Azure HDInsight via Apache Services in just a matter of days, calls into question the security of the service.
  * Organizations can reduce their risk of XSS attacks by applying best practices, such as implementing a Content Security Policy (CSP), performing input validation and output encoding, and adhering to the principle of least privilege.

## About the 8 XSS Vulnerabilities in Azure HDInsight

Below we have included an overview of the eight vulnerabilities that were found in Azure HDInsight. To protect against these vulnerabilities, organizations must apply Microsoft’s [August 2023 security update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster).

| **Name**| **Severity**| **XSS Type**| **Impact**| **CVE**| **Status**  
---|---|---|---|---|---|---  
#1| Azure HDInsight/Apache Ambari Stored XSS in Background Operations| Important| Stored XSS| Spoofing| [CVE-2023-36881](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-36881)| Fixed in August 8th [Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster)  
#2| Azure HDInsight/Apache Ambari Stored XSS via Managed Notifications| Important| Stored XSS| Spoofing| [CVE-2023-36881](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-36881)| Fixed in August 8th [Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster)  
#3| Azure HDInsight/Apache Ambari Stored XSS in YARN Queue Manager| Important| Stored XSS| Spoofing| [CVE-2023-36881](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-36881)| Fixed in August 8th [Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster)  
#4| Azure HDInsight/Jupyter Notebooks Code Execution via Stored XSS| Important| Stored XSS| Spoofing| [CVE-2023-35394](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-35394)| Fixed in August 8th [Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster)  
#5| Azure HDInsight/Apache Hadoop Reflected XSS via endpoint manipulation| Important| Reflected XSS| Spoofing| [CVE-2023-38188](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-38188)| Fixed in August 8th [Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster)  
#6| Azure HDInsight/Apache Hive 2 Reflected XSS via endpoint manipulation| Important| Reflected XSS| Spoofing| [CVE-2023-35393](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-35393)| Fixed in August 8th [Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster)  
#7| Azure HDInsight/Apache Ambari Stored XSS in YARN Configurations| Important| Stored XSS| Spoofing| [CVE-2023-36881](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-36881)| Fixed in August 8th [Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster)  
#8| Azure HDInsight/Apache Oozie Web Console Stored XSS via Custom Filter| Important| Stored XSS| Spoofing| [CVE-2023-36877](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-36877)| Fixed in August 8th [Security Update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster)  
  
## What is Azure HDInsight?

[Azure HDInsight](https://azure.microsoft.com/en-us/products/hdinsight) is a fully managed, open-source analytics service provided by Microsoft for processing big data workloads in a scalable and flexible way. It’s essentially a cloud-based service that simplifies the management, processing, and analysis of big data by offering a number of data processing frameworks like Apache Hadoop, Apache Spark, Apache Kafka, and others.

HDInsight supports a wide range of data processing tasks with open-source frameworks such as Apache Hadoop for batch processing, Apache Spark for in-memory processing, Apache HBase for NoSQL data, Apache Storm and Kafka for real-time processing, and Machine Learning with R Server.

HDInsight can be integrated with other Azure services. For example, you can store and manage data using Azure Data Lake Storage or Azure Blob Storage. Similarly, it can be integrated with Azure Data Factory for ETL operations, Azure Synapse Analytics for warehousing, or Power BI for visualization.

## What is Cross-Site Scripting (XSS)?

Cross-Site Scripting (XSS) occurs when an attacker injects malicious scripts into a trusted website, which are then executed by unsuspecting users’ browsers. This can lead to unauthorized access, data theft, and even complete compromise of the affected system. Recent examples are the [Jenkins stored XSS](https://www.jenkins.io/security/advisory/2023-07-26/), [Zimbra XSS](https://nvd.nist.gov/vuln/detail/CVE-2023-37580), and [Azure Bastion and Azure Container Registry XSS](https://orca.security/resources/blog/examining-two-xss-vulnerabilities-in-azure-services/) vulnerabilities.

All 8 XSS vulnerabilities discovered in various platforms and components in Azure HDInsight primarily resulted from the lack of proper input sanitization. This omission allowed malicious characters to be rendered once the dashboard was loaded, demonstrating inadequate output encoding that fails to neutralize these characters when rendered. Other factors also contributed, but the central issue lies in the absence of appropriate measures to sanitize inputs.

These weaknesses collectively allow an attacker to inject and execute malicious scripts when the stored data is retrieved and displayed to users. This goes for both Stored XSS and Reflected XSS Cases.

## Stored XSS Versus Reflected XSS Vulnerabilities

Two common types of XSS vulnerabilities are Reflected XSS and Stored XSS. The main difference between them are their execution mechanisms.

  * **Reflected XSS** : This type of attack occurs when a malicious script is inserted into a URL and is immediately reflected back to the user, executing only for those who click the specifically crafted link. 
  * **Stored XSS** : on the other hand, is when the malicious script is saved on the server and executed for any user viewing the affected page. The primary difference lies in the delivery: Reflected XSS targets individual requests, while Stored XSS is embedded in a web page and affects all users accessing it.

## How We Discovered 8 XSS vulnerabilities in Just a Few Days

Our initial encounter with XSS in Azure HDInsight was straightforward. We discovered that the Apache Ambari Background operations had multiple parameters that, by default, could be modified. After identifying this primary stored XSS vulnerability, we expanded our investigation. Using various techniques, we subsequently pinpointed seven more similar vulnerabilities.

Leveraging hands-on manipulation combined with in-depth exploration of the text rendering engine, we were able to discover 8 XSS vulnerabilities in total, each of which required a unique approach to exploit. By promptly documenting and reporting these findings to MSRC, Microsoft was able to fix all the XSS vulnerabilities in their [August 2023 security update](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-upgrade-cluster).

![](https://fast.wistia.com/embed/medias/2dsx4wgqi1/swatch)

_POC of how the XSS vulnerabilities could be exploited_

Utilizing BurpSuite, we were able to craft and send specially tailored requests to bypass the Apache Ambari dashboard’s native filters and sanitize problematic characters commonly known to prevent XSS. 

This involved encoding payloads and exploiting weak or misconfigured input validation, allowing us to manipulate user input in a manner that the server would process and render as part of the HTML. Through an automated software testing method known as fuzzing (Using the Intruder tool in Burpsuite), we systematically explored various permutations of both standard and non-standard XSS payloads, targeting different input fields and then observed how the application handled them. 

By careful inspection of HTTP responses and analyzing the Document Object Model (DOM), we were able to identify where the application was improperly escaping or sanitizing the user-supplied input. 

We traced the execution flow to uncover how the payloads were processed and manifested within the user’s browser. 

### #1. Azure HDInsight/Apache Ambari Stored XSS in Background Operations

The first XSS that we found in Azure HDInsight was in Apache Ambari Background operations, where we managed to modify default parameters by editing various values. Due to a special characters filter that was included in the dashboard, we weren’t able to modify the Background Operations parameters directly to a malicious XSS payload, but we got round this by first modifying them to a valid value, and then resending the request via Burpsuite.

Workflow:

  1. Create a new HDInsight Service on Azure Portal.
  2. Select the Interactive Query cluster type and set the version.
  3. Access the public endpoint of the service.  
Navigate to Services and select HDFS.
  4. Click on the Run Service Check option in Background Operations.
  5. Inspect the request made during this process.  
Modify the request to inject a simple HTML.
  6. Observe that the injected code is reflected and rendered.
  7. Proceed to inject a stored XSS payload which will be subsequently executed.

### #2. Azure HDInsight/Apache Ambari Stored XSS via Managed Notification

Stored XSS is found in the Managed Notifications component of Azure HDInsight’s Apache Ambari. The vulnerability occurs when manipulating alert notifications.

Workflow:

  1. Navigate to the dashboard and select Alerts.
  2. Click on ACTIONS and then Managed Notifications.
  3. Create a new email notification with a sample name.
  4. Capture the request and inspect the returned status.
  5. Attempt to inject an HTML payload when creating a new alert.
  6. Upon deletion, a confirmation box displays the name of the alert.
  7. Inject a stored XSS payload and observe it being executed.

![](https://orca.security/wp-content/uploads/2024/01/image-61.png) ![](https://orca.security/wp-content/uploads/2024/01/image-62.png)

### #3. Azure HDInsight/Apache Ambari Stored XSS in YARN Queue Manager

The YARN Queue Manager in Azure HDInsight’s Apache Ambari for the HBase cluster type is susceptible to a stored XSS. The vulnerability is present in the Access Control functions.

Workflow:

  1. Navigate to the dashboard and select the YARN Queue Manager view.
  2. Select the root queue.
  3. Navigate to the Access Control and Status sections.
  4. Change the Administrator Queue to Custom and focus on Groups.
  5. Observe the limitations in this field due to comma-separation.
  6. Inject a simple HTML payload to verify the vulnerability.
  7. Inject a crafted malicious XSS payload and save to see it being automatically executed.  
  

### #4. Azure HDInsight/Jupyter Notebooks Code Execution via Stored XSS

Azure HDInsight’s Jupyter Notebook service is vulnerable to a stored XSS which can be further exploited to achieve remote code execution. The vulnerability stems from bypassing the Caja compiler.

Workflow:

  1. Set up the Spark cluster and navigate to the Jupyter Notebook service.
  2. Create a new PySpark3 Notebook and test with sample code.
  3. Examine the actions, requests, and WebSocket communications triggered during execution.
  4. Test the Markdown feature in Jupyter and observe how the Caja compiler sanitizes JS code.
  5. Use a specific method to bypass the Caja sanitization process.
  6. Craft a malicious payload with a remote JS file evil.js.
  7. The evil.js file establishes a WebSocket communication and sends a reverse shell as a code payload.
  8. Set up a remote server to host the evil.js file and wait for an incoming reverse shell.  

### #5. Azure HDInsight/Apache Hadoop Reflected XSS via Endpoint Manipulation

A reflected XSS vulnerability is present in Apache Hadoop’s ResourceManager UI within Azure HDInsight. By altering the container endpoint and port, an XSS can be executed.

Workflow:

  1. Access YARN from the dashboard inside the Hadoop Cluster.
  2. Select Node and then the red-highlighted Node link.
  3. Observe the container endpoint and port.
  4. Alter the path by removing the host and port.
  5. Change the entire path, observing the DNS callback for the default port (30060).
  6. Set up a Python server to listen on port 30060.
  7. Observe the execution of the XSS.  

### #6. Azure HDInsight/Apache Hive 2 Reflected XSS via Endpoint Manipulation

Apache Hive 2 within Azure HDInsight suffers from a reflected XSS vulnerability. By modifying the container endpoint and hosting a malicious file, an XSS can be executed.

Workflow:

  1. Click on the Public Endpoint after creating the HDInsight service.
  2. Access Hive Service from the dashboard.
  3. Click on Hive Interactive UI to see Running Instances.
  4. Click on the Container ID to view the container endpoint and port.
  5. Modify the Host (port cannot be changed) to point to your Collaborator.
  6. Set up a Python server to listen on port 15002.
  7. Host an xss.html file on the Python server.
  8. Modify the URL to execute the malicious file, executing the XSS.  

### #7. Azure HDInsight/Apache Ambari Stored XSS in YARN Configurations

A stored XSS vulnerability resides within Apache Ambari’s YARN Queue Manager in Azure HDInsight. By injecting JS code into specific YARN configurations, a stored XSS is executed upon refreshing the queues.

Workflow:

  1. Access YARN Queue Manager.
  2. Set Node Locality Delay to 2 and click Save and Refresh Queues.
  3. Review the modifications in Burp.
  4. Experiment with different variables to find the injectable one (yarn.scheduler.capacity.resource-calculator).
  5. Modify the value and send a saveAndRefresh request.
  6. Refresh the queues; the next visit to the page will execute the Stored XSS.  
  

### #8. Azure HDInsight/Apache Oozie Web Console Stored XSS via Custom Filter

The Apache Oozie Web Console in Azure HDInsight allows stored XSS via custom filter manipulation. By injecting HTML and then JS XSS payloads, a stored XSS can be set up to execute repeatedly.

Workflow:

  1. Access the Dashboard and select Oozie.
  2. Click on the relevant Active Oozie Web UI.
  3. Navigate to Custom filter.
  4. Click on the Custom Filter Button.
  5. Test HTML injection using an H1 tag.
  6. Refresh the page, and validate that the tag is rendered.
  7. Move to a JS XSS payload, and inject it.
  8. Observe the payload being executed.
  9. From this point, the payload will execute as a Stored XSS.

## How Can Organizations Reduce Exposure to XSS Vulnerabilities?

Even though these XSS vulnerabilities have now been fixed by Microsoft, it’s still important to implement robust security practices to minimize the risk of further XSS vulnerabilities. 

Below we list our recommendations to protect against XSS:

  1. **Input Validation:** Validate user inputs against expected formats, data types, and ranges. This mitigates the risk of script injection.
  2. **Output Encoding:** Use output encoding (HTML, JavaScript, and URL encoding) to ensure that user-generated data is properly sanitized before being displayed in web pages.
  3. **Content Security Policy (CSP):** Implement CSP to add an extra layer of security that can restrict the execution of scripts and minimize the potential impact of any XSS vulnerabilities.
  4. **Use Frameworks and Libraries** : Utilize modern web frameworks and libraries that incorporate security features by default. These frameworks often include mechanisms to prevent XSS vulnerabilities, such as automatic output encoding.
  5. **Apply the principle of least privilege** : By giving users and processes only the permissions required for their specific tasks, you limit the potential attack surface for an attacker to exploit. This means that even if an attacker manages to inject malicious scripts through an XSS vulnerability, they will have limited access to sensitive data and functionality due to the [principle of least privilege](https://orca.security/platform/cloud-infrastructure-entitlement-management-ciem/).

![](https://orca.security/wp-content/uploads/2024/01/image-63.png?w=1176)

_The Orca Platform helps security teams apply the least privilege principle across their accounts_

## About Orca Security

Orca’s agentless [cloud security platform](https://orca.security/platform/) connects to your environment in minutes and provides full visibility of all your assets on AWS, Azure, Google Cloud, Kubernetes, and more. Orca detects, prioritizes, and helps remediate cloud risks across every layer of your cloud estate, including vulnerabilities, malware, misconfigurations, lateral movement risk, API risks, sensitive data at risk, weak and leaked passwords, and overly permissive identities.

  * [ __](https://twitter.com/share?text=Azure%20HDInsight%20Riddled%20With%20XSS%20Vulnerabilities%20via%20Apache%20Services&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fcross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fcross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fcross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight%2F)
  * [ __](mailto:?Subject=Azure HDInsight Riddled With XSS Vulnerabilities via Apache Services&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fcross-site-scripting-vulnerabilities-in-apache-services-azure-hd-insight%2F)

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
