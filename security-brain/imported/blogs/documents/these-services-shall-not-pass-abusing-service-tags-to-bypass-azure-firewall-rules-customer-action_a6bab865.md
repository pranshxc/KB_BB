---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-03_these-services-shall-not-pass-abusing-service-tags-to-bypass-azure-firewall-rule.md
original_filename: 2024-06-03_these-services-shall-not-pass-abusing-service-tags-to-bypass-azure-firewall-rule.md
title: 'These Services Shall Not Pass: Abusing Service Tags to Bypass Azure Firewall
  Rules (Customer Action Required)'
category: documents
detected_topics:
- ssrf
- cloud-security
- access-control
- sso
- command-injection
- automation-abuse
tags:
- imported
- documents
- ssrf
- cloud-security
- access-control
- sso
- command-injection
- automation-abuse
language: en
raw_sha256: a6bab86507ae8d34b42faa60971774fa3c0bcba9b236dc4fea9b4954e0149b25
text_sha256: 2bcba8855560bf7ed12a50c798804cef45ac6d0a2465e5c517e411b9a0ef67e1
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# These Services Shall Not Pass: Abusing Service Tags to Bypass Azure Firewall Rules (Customer Action Required)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-03_these-services-shall-not-pass-abusing-service-tags-to-bypass-azure-firewall-rule.md
- Source Type: markdown
- Detected Topics: ssrf, cloud-security, access-control, sso, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `a6bab86507ae8d34b42faa60971774fa3c0bcba9b236dc4fea9b4954e0149b25`
- Text SHA256: `2bcba8855560bf7ed12a50c798804cef45ac6d0a2465e5c517e411b9a0ef67e1`


## Content

---
title: "These Services Shall Not Pass: Abusing Service Tags to Bypass Azure Firewall Rules (Customer Action Required)"
page_title: "Abusing Service Tags to Bypass Azure Firewall Rule"
url: "https://www.tenable.com/blog/these-services-shall-not-pass-abusing-service-tags-to-bypass-azure-firewall-rules-customer"
final_url: "https://www.tenable.com/blog/these-services-shall-not-pass-abusing-service-tags-to-bypass-azure-firewall-rules-customer"
authors: ["Liv Matan (@terminatorLM)"]
programs: ["Microsoft (Azure)"]
bugs: ["Cloud", "WAF bypass", "SSRF"]
publication_date: "2024-06-03"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 262
---

#  These Services Shall Not Pass: Abusing Service Tags to Bypass Azure Firewall Rules (Customer Action Required)

[![Liv Matan](/sites/default/files/pictures/2024-03/Liv-Matan.jpg) ]()

By [Liv Matan](/profile/liv-matan)

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.tenable.com%2Fblog%2Fthese-services-shall-not-pass-abusing-service-tags-to-bypass-azure-firewall-rules-customer&title=These%20Services%20Shall%20Not%20Pass%3A%20Abusing%20Service%20Tags%20to%20Bypass%20Azure%20Firewall%20Rules%20%28Customer%20Action%20Required%29) [ ](https://www.reddit.com/submit?url=https%3A%2F%2Fwww.tenable.com%2Fblog%2Fthese-services-shall-not-pass-abusing-service-tags-to-bypass-azure-firewall-rules-customer&title=These%20Services%20Shall%20Not%20Pass%3A%20Abusing%20Service%20Tags%20to%20Bypass%20Azure%20Firewall%20Rules%20%28Customer%20Action%20Required%29) [ ](https://twitter.com/intent/tweet?urlhttps%3A%2F%2Fwww.tenable.com%2Fblog%2Fthese-services-shall-not-pass-abusing-service-tags-to-bypass-azure-firewall-rules-customer&text=These%20Services%20Shall%20Not%20Pass%3A%20Abusing%20Service%20Tags%20to%20Bypass%20Azure%20Firewall%20Rules%20%28Customer%20Action%20Required%29) Subscribe 

![An image of a lit explosive device on top of lines of code](/sites/default/files/images/articles/Abusing%20Service%20Tags%20to%20Bypass%20Azure%20Firewall%20Rules.jpg)

Azure customers whose firewall rules rely on Azure Service Tags, pay attention: You could be at risk due to a vulnerability discovered by Tenable Research. Here’s what you need to know to determine if you’re affected, and if so, what you should do right away to protect your Azure environment from attackers.

Tenable Research has discovered a vulnerability in Azure that allows an attacker to bypass firewall rules based on Azure [Service Tags](https://learn.microsoft.com/en-us/azure/virtual-network/service-tags-overview) by forging requests from trusted services. Customers who rely on these firewall rules for security are at risk from this vulnerability. They should take immediate action to mitigate the issue and ensure they are protected by robust layers of authentication and authorization.

The vulnerability was discovered initially in the Azure Application Insights service, but we and the Microsoft Security Response Center (MSRC) eventually found that it affects more than 10 other Azure services. In each case, attackers would be able to access other internal and private Azure services.

![Diagram reveals how hacker could access internal private network of victim](/sites/default/files/inline/images/Diagram%20shows%20how%20attackers%20would%20be%20able%20to%20access%20other%20internal%20and%20private%20Azure%20services_0.gif)

In Tenable Research’s communication with MSRC about this vulnerability, MSRC explained that Azure Service Tags have security limitations and also updated their documentation to reflect those.

“Service Tags are not sufficient to secure traffic to a customer's origin without considering the nature of the service and the traffic it may send. It is always the best practice to implement authentication/authorization for traffic rather than relying on firewall rules alone,” reads one of the messages MSRC sent to Tenable Research.

## The vulnerability

Multiple services in Azure allow the customer to craft web requests. Some even allow users to add headers to the request and to change HTTP methods. This is part of the intended functionality of these services. For example, since the Azure Application Insight Availability Tests Feature tests the availability of applications deployed by clients, clients require full control of the request to create a functional test.

However, this functionality may open the door for a malicious actor to achieve an impact similar to that of a server-side request forgery (SSRF) vulnerability. SSRF allows an attacker to cause a server-side application to make requests to an unintended location, whether internal or external, allowing the attacker, among other options, to reach/expose resources that were previously unreachable.

When a service grants users the option to control server-side requests, and the service is associated with Azure Service Tags, things can get risky if the customer does not have additional layers of protection.

## Impact

This vulnerability enables an attacker to control server-side requests, thus impersonating trusted Azure services. This enables the attacker to bypass network controls based on Service Tags, which are often used to prevent public access to Azure customers’ internal assets, data, and services.

## Coordinated Disclosure

January 24, 2024 - Tenable discloses to vendor. Automated acknowledgment.

January 31, 2024 - MSRC confirms the behavior as an “Elevation of Privilege” with severity “Important” and awarded a bounty.

February 2, 2024 - MSRC devises a comprehensive fix plan along with a timeline for implementation.

February 26, 2024 - MSRC decides to address the issue via a comprehensive documentation update and addresses more variants of the vulnerability.

March 6, 2024 - Coordinated disclosure in May is agreed upon.

April 30, 2024 - Tenable provides a blog draft to MSRC.

April 30 - May 10, 2024 - Tenable coordinates with MSRC to incorporate technical comments.

June 3, 2024 - Coordinated disclosure.

## What are Azure Service Tags?

Per the documentation, which has since been updated by Microsoft, Azure Service Tags simplify network isolation within Azure by grouping specific Azure services IP ranges. These tags can be used to define network security rules and apply these rules consistently across multiple Azure resources. Essentially, Azure Service Tags provide a convenient way to manage access controls, such as firewall rules or network security group (NSG) configurations.

![Example of Azure Service Tags](/sites/default/files/inline/images/Azure%20service%20tags%20examples.png) Azure Service Tags (Source: [Microsoft](https://learn.microsoft.com/en-us/azure/virtual-network/service-tags-overview))

For example, if I as a customer want to allow network access to my private [Azure API Management Service](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts), and only from the service itself, or another service I use in Azure, I can do it in two ways as long as these services have associated Service Tags:

  1. I can specify the IP ranges of the services I want to allow.
  2. I can use a service tag of the associated service, the “ApiManagement” service tag, to only allow my API Management services to access my API Management.

The second option is more convenient, so it’s safe to assume many – maybe most – customers will choose it. Nonetheless, both options can put customers at risk from the vulnerability we’re describing.

## Technical details - Azure Application Insights example

Azure Application Insights is a monitoring and analytics service that helps developers detect, diagnose, and understand issues affecting their web applications and services in real-time.

Azure Application Insights has a service tag associated with it named “ApplicationInsightsAvailability”.

The Application Insights Availability feature allows you to create availability tests for your application or machine. 

When creating a new test using Azure Application Insights with the intention of using it for an internal network application or machine, Azure [advises](https://learn.microsoft.com/en-us/azure/azure-monitor/app/availability-private-test) customers to use a Service Tag to only allow the Application Insights Availability service to monitor and access your internal application or machine through port 80 or 443:

![ Azure advises customers to use a Service Tag to only allow the Application Insights Availability service to monitor and access your internal application or machine through port 80 or 443](/sites/default/files/inline/images/Azure%20advises%20customers%20to%20use%20a%20Service%20Tag%20to%20only%20allow%20the%20Application%20Insights%20Availability%20service.png)

A naive user will follow the advice, and apply the “ApplicationInsightsAvailability” Service Tag to his private asset in the asset’s Azure network configuration while aiming to achieve network isolation. Behind the scenes, [a set of IPs associated with the Application Insights Availability](https://www.microsoft.com/en-us/download/details.aspx?id=56519) agent are allowed.

The interesting part is the combination of the Service Tag usage and the service’s feature that allows users to control server-side requests:

Attackers can abuse the "availability test" of the "classic test" or a "standard test" functionality. Both functionalities support custom headers and HTTP method change. Attackers can send requests using the availability tests feature of the Application Insights Availability service. Through this, they can access the internal services of cross-tenant victims who blindly trust the Application Insights Availability Service Tag in their firewall rule. Attackers can leverage this to access internal APIs that are now exposed in the victim's service, since the exposed ports are 80/443, which usually host web assets.

Attackers can add custom headers, change methods and customize their HTTP requests however they want.

## Proof of concept

Below we outline the steps an attacker would take to exploit this vulnerability on Azure App Services.

Let us say that a user is deploying an internal Azure App Service, that user wants their App Service to utilize the capabilities of Azure Application Insights, but still remain isolated. The user attempts to accomplish this by applying access restrictions to only allow the ApplicationInsightsAvailability Service tag:

![Box reveals example of applying access restrictions to only allow the ApplicationInsightsAvailability Service tag](/sites/default/files/inline/images/The%20user%20attempts%20to%20accomplish%20this%20by%20applying%20access%20restrictions%20to%20only%20allow%20the%20Application%20Insights%20Availability%20Service%20tag.png)

An attacker tries to access the internal App Service and gets a forbidden response:

![An attacker tries to access the internal App Service and gets a forbidden response](/sites/default/files/inline/images/An%20attacker%20tries%20to%20access%20the%20internal%20App%20Service%20and%20gets%20a%20forbidden%20response.png)

An attacker abuses the described vulnerability in the Application Insights availability tests feature to impersonate the Application Insights service and successfully accesses the victim's internal App service. The attacker can also view the response and add custom headers, which are available through the "standard test" feature:

![An attacker abuses the described vulnerability in the Application Insights availability tests feature to impersonate the Application Insights service and successfully accesses the victim's internal App service](/sites/default/files/inline/images/The%20attacker%20can%20also%20view%20the%20response%20and%20add%20custom%20headers%2C%20which%20are%20available%20through%20the%20standard%20test%20feature.png)

![The attacker can also view the response and add custom headers, which are available through the "standard test" feature](/sites/default/files/inline/images/Example%20of%20how%20the%20attacker%20can%20view%20the%20response%20and%20add%20custom%20headers.jpg)

## Affected services - Variants of the vulnerability 

After analyzing the security and the trustworthiness of Azure Service Tags through the Application Insights service, and reporting our findings to MSRC, we and MSRC found more variants of the issue in more than 10 Azure services.

We appreciate MSRC’s commitment and work on this matter. Capabilities and risks vary for each service. Those include:

  * Azure Application Insights
  * Azure DevOps
  * Azure Machine Learning
  * Azure Logic Apps
  * Azure Container Registry
  * Azure Load Testing
  * Azure API Management
  * Azure Data Factory
  * Azure Action Group
  * Azure AI Video Indexer
  * Azure Chaos Studio

The common denominator in these various scenarios is this dangerous combination: a service that has an associated Service Tag and also allows users to control server-side requests. 

## How to defend against these attacks

First, analyze the network rules in your Azure environment on each associated service, search for the use of Service Tags, and filter the affected services. For the affected services, assume these assets are public.

To defend these assets, add authentication and authorization layers to these. Just as MSRC advised:

“Service Tags are not sufficient to secure traffic to a customer's origin without considering the nature of the service and the traffic it may send. It is always the best practice to implement authentication/authorization for traffic rather than relying on firewall rules alone.”

Second, when configuring Azure services’ network rules, bear in mind that Service Tags are not a watertight way to secure traffic to your private service. By ensuring that strong network authentication is maintained, users can defend themselves with an additional and crucial layer of security. In that case, even an attacker leveraging the vulnerability to reach the target endpoint would have great trouble exploiting that access. 

The Azure services we listed in this blog are vulnerable. We advise approaching even other services not listed on this blog with a healthy dose of skepticism as well and check whether a service has the dangerous combination described in this blog.

**To read more vulnerability discovery posts like this from the Tenable Cloud Security Research team, please visit**[**here**](https://www.tenable.com/blog/search?field_blog_section_tid=1801&combine=)**.**

## Author

## Learn more

[![Liv Matan](/sites/default/files/pictures/2024-03/Liv-Matan.jpg) ]()

### [Liv Matan](/profile/liv-matan)

##### Senior Security Researcher, Tenable

Liv is a Senior Security Researcher at Tenable, specializing in cloud, application and web security. As a bug bounty hunter, Liv has found vulnerabilities in popular software platforms, including Azure, Google Cloud, AWS, Facebook and GitLab. Liv was recognized by Microsoft as a Most Valuable Securi... 

[Read more](/profile/liv-matan)

## Learn more

## Related articles

AI Security

![Don't confuse asset inventory with exposure management image](/sites/default/files/images/articles/Exposure%20Management%20Academy_20250313_03_22%20%281%29.png)

Mar 16 2026

#### Don't confuse asset inventory with exposure management

By [Nathan Dyer](/profile/nathan-dyer)

[ ](/blog/asset-inventory-discovery-tools-vs-exposure-management)

Research

![Tenable Discovers Critical Vulnerabilities in SimpleHelp Tool: CVE-2025-36727… image](/sites/default/files/images/articles/Critical%20Security%20Issues%20Identified%20in%20SimpleHelp%20Tool.jpeg)

Oct 16 2025

#### Tenable Discovers Critical Vulnerabilities in SimpleHelp Tool: CVE-2025-36727…

By [Derrie Sutton](/profile/derrie-sutton)

[ ](/blog/tenable-discovers-critical-vulnerabilities-in-simplehelp-tool-cve-2025-36727-and-cve-2025)

Cybersecurity Snapshot

![Cybersecurity Snapshot: Cyber Platforms Are CISOs' BFFs, Study Says, as OpenSSF… image](/sites/default/files/images/articles/Cyber%20Platforms%20Are%20CISOs%20BFFs.png)

Sep 19 2025

#### Cybersecurity Snapshot: Cyber Platforms Are CISOs' BFFs, Study Says, as OpenSSF…

By [Juan Perez](/profile/juan-perez)

[ ](/blog/cybersecurity-snapshot-cisos-embrace-integrated-security-platforms-to-reduce-tool-sprawl-save-costs-9-19-2025)

  * Attack Surface Management
  * Cloud
  * Threat Intelligence
  * Threat Management
  * Vulnerability Management
