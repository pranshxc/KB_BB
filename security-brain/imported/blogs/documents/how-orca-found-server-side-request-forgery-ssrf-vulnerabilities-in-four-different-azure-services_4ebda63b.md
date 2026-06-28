---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-17_how-orca-found-server-side-request-forgery-ssrf-vulnerabilities-in-four-differen.md
original_filename: 2023-01-17_how-orca-found-server-side-request-forgery-ssrf-vulnerabilities-in-four-differen.md
title: How Orca Found Server-Side Request Forgery (SSRF) Vulnerabilities in Four Different
  Azure Services
category: documents
detected_topics:
- cloud-security
- ssrf
- idor
- command-injection
- otp
- api-security
tags:
- imported
- documents
- cloud-security
- ssrf
- idor
- command-injection
- otp
- api-security
language: en
raw_sha256: 4ebda63b6f6e4672aa779c647520bbd850d9bc06f8146278fdc732eb053f2f2f
text_sha256: 871741f1ed69706606195bf7454011f0a10847b243193da9245f3790f08e4342
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# How Orca Found Server-Side Request Forgery (SSRF) Vulnerabilities in Four Different Azure Services

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-17_how-orca-found-server-side-request-forgery-ssrf-vulnerabilities-in-four-differen.md
- Source Type: markdown
- Detected Topics: cloud-security, ssrf, idor, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `4ebda63b6f6e4672aa779c647520bbd850d9bc06f8146278fdc732eb053f2f2f`
- Text SHA256: `871741f1ed69706606195bf7454011f0a10847b243193da9245f3790f08e4342`


## Content

---
title: "How Orca Found Server-Side Request Forgery (SSRF) Vulnerabilities in Four Different Azure Services"
page_title: "How Orca Found SSRF Vulnerabilities in 4 Azure Services"
url: "https://orca.security/resources/blog/ssrf-vulnerabilities-in-four-azure-services/"
final_url: "https://orca.security/resources/blog/ssrf-vulnerabilities-in-four-azure-services/"
authors: ["Lidor Ben Shitrit"]
programs: ["Microsoft (Azure)"]
bugs: ["SSRF", "Cloud"]
publication_date: "2023-01-17"
added_date: "2023-01-18"
source: "pentester.land/writeups.json"
original_index: 1662
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![How Orca Found Server-Side Request Forgery \(SSRF\) Vulnerabilities in Four Different Azure Services](https://orca.security/wp-content/uploads/2023/01/Blog-graphic_Server-Side-Request-Forgery_Cover.jpg?w=1044)

# How Orca Found Server-Side Request Forgery (SSRF) Vulnerabilities in Four Different Azure Services

[ ![Avatar of Lidor Ben Shitrit](https://orca.security/wp-content/uploads/2022/01/avatar-lidor-ben.png) Lidor Ben Shitrit  ](https://orca.security/resources/author/lidor-ben-shitrit/)

Published: Jan 17, 2023 

  * [ __](https://twitter.com/share?text=How%20Orca%20Found%20Server-Side%20Request%20Forgery%20%28SSRF%29%20Vulnerabilities%20in%20Four%20Different%20Azure%20Services&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fssrf-vulnerabilities-in-four-azure-services%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fssrf-vulnerabilities-in-four-azure-services%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fssrf-vulnerabilities-in-four-azure-services%2F)
  * [ __](mailto:?Subject=How Orca Found Server-Side Request Forgery \(SSRF\) Vulnerabilities in Four Different Azure Services&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fssrf-vulnerabilities-in-four-azure-services%2F)

As part of the [Orca Research Pod](https://orca.security/about/orca-research-pod/) efforts, we regularly research various cloud provider services and capabilities to help our customers keep their assets safe and secure in the cloud. During our research into several Azure services, we found four instances where different services were vulnerable to a Server Side Request Forgery (SSRF) attack. Alarmingly, two of the vulnerabilities did not require authentication, meaning that they could be exploited without even having an Azure account. 

SSRF attacks can be particularly dangerous since a successful execution can result in an attacker accessing or modifying internal resources as well as submitting data to external sources. 

As soon as we discovered the vulnerabilities, we reached out to the [Microsoft Security Response Center (MSRC)](https://www.microsoft.com/en-us/msrc), who promptly fixed the reported issues. Microsoft has confirmed that the vulnerabilities have been remediated, which is why we are now disclosing the details of the vulnerabilities we found. 

In this blog, we will describe how we found each of these SSRF vulnerabilities and were able to take advantage of these flaws to access various internal endpoints in some of the Azure Services.

## Executive Summary

  * In total we found four Azure services vulnerable to SSRF: Azure API Management, Azure Functions, Azure Machine Learning and Azure Digital Twins.
  * We managed to exploit two vulnerabilities _without requiring any authentication_ on the service (Azure Functions and Azure Digital Twins), allowing us to send requests in the name of the server without even having an Azure account.
  * The discovered Azure SSRF vulnerabilities allowed an attacker to scan local ports, find new services, endpoints, and files – providing valuable information on possibly vulnerable servers and services to exploit for initial entry and the location of potential information to target. 
  * [SSRF vulnerabilities](https://orca.security/resources/blog/oracle-server-side-request-forgery-ssrf-attack-metadata/) are particularly dangerous since if attackers are able to access the host’s IMDS (Cloud Instance Metadata Service), this exposes detailed information on instances, including hostname, security group, MAC address and user-data, potentially allowing attackers to retrieve tokens, move to another host, and execute code (RCE).
  * Thanks to various SSRF mitigations that Microsoft put in place, such as the environment variable (X-IDENTITY-HEADER), we did not manage to reach any IMDS endpoints. However, even without the ability to access IMDS services, there was still a lot of potential damage an attacker could achieve, as described above.
  * After flagging the vulnerabilities to Microsoft, they were swiftly mitigated. 
  * The most notable aspect of these discoveries is arguably the number of SSRF vulnerabilities we were able to find with only minimal effort (including another SSRF vulnerability we found last year in [Oracle Cloud Services](https://orca.security/resources/blog/oracle-server-side-request-forgery-ssrf-attack-metadata/)), indicating just how prevalent they are and the risk they pose in cloud environments.

## About the Four SSRF Vulnerabilities

Below we have provided an overview and timeline of the vulnerabilities we found in the four different Azure services.

| **Affected Service**| **Severity**| **Unauthenticated**| **Date reported**| **Status**  
---|---|---|---|---|---  
SSRF #1| [Azure Digital Twins](https://orca.security/resources/blog/ssrf-vulnerabilities-azure-digital-twins/)| Important| Yes| October 8, 2022| Fixed (October 17, 2022)  
SSRF #2| [Azure Functions App](https://orca.security/resources/blog/ssrf-vulnerabilities-azure-functions-app/)| Important| Yes| November 12, 2022| Fixed (December 9, 2022)  
SSRF #3| [Azure API Management](https://orca.security/resources/blog/ssrf-vulnerabilities-azure-api-management/)| Important| No| November 12, 2022| Fixed (November 16, 2022)  
SSRF #4| [Azure Machine Learning](https://orca.security/resources/blog/ssrf-vulnerabilities-azure-machine-learning/)| Low| No| December 2, 2022| Fixed(December 20, 2022)  
  
## What is a Server-Side Request Forgery (SSRF)? 

A Server-Side Request Forgery (SSRF) is a [web security vulnerability](https://orca.security/resource/research-pod/anatomy-identity-and-access-management-cyber-attack-aws/) that allows an attacker to abuse a server-side application and make requests to read or update internal resources as well as submit data to external sources. 

There are three main types of Server-Side Request Forgery (SSRF) attacks:

  * **Blind SSRF:** This type of SSRF attack occurs when an attacker can manipulate a server to make requests, but they do not receive the response from the server. This makes it difficult to determine if the attack was successful.
  * **Semi-Blind SSRF** : This type of SSRF attack is similar to Blind SSRF, but the attacker is able to see some of the response from the server, such as the status code or response headers. This can allow the attacker to gather limited information about the target system.
  * **Non-Blind SSRF (or Full SSRF)** : This type of SSRF attack occurs when an attacker can manipulate a server to make requests and receive the full response from the server. This allows the attacker to gather more information about the target system and potentially launch further attacks.

All four SSRF vulnerabilities we discovered belong to the third category which is _Full SSRF_ (aka _Non-blind SSRF_. To give you an idea of how exploitable these vulnerabilities are, Non-blind SSRF flaws can be leveraged in many different ways, including SSRF via XXE, SSRF via SVG file, SSRF via Proxy, SSRF via PDF Rendering, SSRF via vulnerable query string in the URL and many more.

It is important to note that no matter the type of SSRF attack, each SSRF vulnerability can be used to gain unauthorized access to sensitive information or launch further attacks against a target. Therefore, it is important for organizations to [properly secure their servers and networks](https://orca.security/resources/blog/cloud-vulnerability-management-strategies/) to prevent these types of attacks.

### How does a Server-Side Request Forgery (SSRF) attack work?

In the diagram below, we show the different communication flows between the attacker, the vulnerable server and a web server in an SSRF attack.

![](https://orca.security/wp-content/uploads/2024/01/image-305.png)

  1. The first arrow represents the initial request being sent from the attacker to the vulnerable server. This request is crafted by the attacker in an attempt to exploit a Server-Side Request Forgery (SSRF) vulnerability on the vulnerable server.
  2. The second arrow represents the vulnerable server forwarding the request to a web server. This occurs because the vulnerable server is able to make requests to external servers due to the SSRF vulnerability.
  3. The third arrow represents the response from the web server being sent back to the vulnerable server.
  4. The fourth and final arrow represents the response from the vulnerable server sent back to the attacker. This response includes any information that the attacker was able to retrieve from the web server through the exploitation of the SSRF vulnerability.

## The Four Azure Server-Side Request Forgery (SSRF) Vulnerabilities Found by Orca

For each of the vulnerabilities, I describe how we discovered it and the potential damage it would have allowed an attacker to cause.

1\. [Unauthenticated SSRF on Azure Digital Twins Explorer](https://orca.security/resources/blog/ssrf-vulnerabilities-azure-digital-twins/)  
2\. [Unauthenticated SSRF on Azure Functions](https://orca.security/resources/blog/ssrf-vulnerabilities-azure-functions-app/)  
3\. [Authenticated SSRF on Azure API Management Service](https://orca.security/resources/blog/ssrf-vulnerabilities-azure-api-management/)  
4\. [Authenticated SSRF on Azure Machine Learning Service](https://orca.security/resources/blog/ssrf-vulnerabilities-azure-machine-learning/)

## Note on Microsoft Azure SSRF Mitigations

In 2020, Microsoft implemented several measures to mitigate the impact of SSRF attacks on its Azure platform.

One such measure was the introduction of requirements for accessing the [instance metadata service (IMDS) endpoint](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/instance-metadata-service?tabs=linux). To prevent unintended or unwanted redirection of IMDS requests, Microsoft now requires that such requests:

  * Contain the header “Metadata: true”
  * Do not contain an “X-Forwarded-For” header

In addition, Microsoft has implemented an “[Identity Header](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity?tabs=portal%2Chttp#rest-endpoint-reference)” for the App Service and Azure Functions. These services provide an internally accessible REST endpoint for token retrieval that can be accessed by apps with a managed identity using a standard HTTP GET request. To make this endpoint available, apps must define two environment variables:

  * IDENTITY_ENDPOINT: the URL to the local token service
  * IDENTITY_HEADER: a header used to help mitigate SSRF attacks. The value is rotated by the platform.

By implementing these measures, Microsoft has significantly reduced the potential damage of SSRF attacks on its Azure platform.

## Final Thoughts

Generally speaking, finding an SSRF vulnerability can be very rewarding for a remote attacker. The simple fact that by abusing such a vulnerability, attackers can reach internal endpoints and services, and even potentially reach a sensitive endpoint such as the IMDS of the server – could be devastating for the organization (see the infamous [2019 Capital One attack](https://securityboulevard.com/2020/12/understanding-the-2019-capital-one-attack/)).

But it’s not just limited to the IMDS – SSRF can also allow an attacker to access local ports on the vulnerable server, potentially leading to further compromise of the system. For example, we were able to access local endpoints in various services.

So how can organizations protect themselves against this type of attack? The key is to ensure that all input is properly validated, and that servers are configured to only allow necessary inbound and outbound traffic. In addition, by [keeping your cloud environment secure](https://orca.security/platform/) – for instance by enforcing proper cloud security hygiene, adhering to the principle of least privilege, patching vulnerabilities and avoiding misconfigurations – you can further limit the damage an attacker can achieve. 

## About Orca Security

The Orca Cloud Security Platform identifies, prioritizes, and remediates risks and compliance issues across your cloud estate spanning AWS, Azure, Google Cloud, Alibaba Cloud, and Kubernetes. Instead of layering multiple siloed tools together or deploying cumbersome agents, Orca delivers complete cloud security in a single platform. Sign up for a complimentary [cloud risk assessment](https://orca.security/lp/cloud-security-risk-assessment/) or [request a demo](https://orca.security/demo/) to get started today.

  * [ __](https://twitter.com/share?text=How%20Orca%20Found%20Server-Side%20Request%20Forgery%20%28SSRF%29%20Vulnerabilities%20in%20Four%20Different%20Azure%20Services&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fssrf-vulnerabilities-in-four-azure-services%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fssrf-vulnerabilities-in-four-azure-services%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fssrf-vulnerabilities-in-four-azure-services%2F)
  * [ __](mailto:?Subject=How Orca Found Server-Side Request Forgery \(SSRF\) Vulnerabilities in Four Different Azure Services&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fssrf-vulnerabilities-in-four-azure-services%2F)

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
