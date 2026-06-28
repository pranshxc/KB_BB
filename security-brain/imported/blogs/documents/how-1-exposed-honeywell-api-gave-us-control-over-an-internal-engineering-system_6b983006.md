---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-19_how-1-exposed-honeywell-api-gave-us-control-over-an-internal-engineering-system.md
original_filename: 2024-08-19_how-1-exposed-honeywell-api-gave-us-control-over-an-internal-engineering-system.md
title: How 1 Exposed Honeywell API Gave us Control Over an Internal Engineering System
category: documents
detected_topics:
- oauth
- access-control
- api-security
- sso
- jwt
- command-injection
tags:
- imported
- documents
- oauth
- access-control
- api-security
- sso
- jwt
- command-injection
language: en
raw_sha256: 6b98300627ea557d2ec7eba67896bd344c084f39ca08cecc404ab488480e0f6c
text_sha256: 485786e1c961a2a8998684223a2c64d41acdc3ec6faf9d8949d5e890c0956d21
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# How 1 Exposed Honeywell API Gave us Control Over an Internal Engineering System

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-19_how-1-exposed-honeywell-api-gave-us-control-over-an-internal-engineering-system.md
- Source Type: markdown
- Detected Topics: oauth, access-control, api-security, sso, jwt, command-injection
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `6b98300627ea557d2ec7eba67896bd344c084f39ca08cecc404ab488480e0f6c`
- Text SHA256: `485786e1c961a2a8998684223a2c64d41acdc3ec6faf9d8949d5e890c0956d21`


## Content

---
title: "How 1 Exposed Honeywell API Gave us Control Over an Internal Engineering System"
page_title: "Traceable - Blog: How 1 Exposed Honeywell API Gave us Control Over an Internal Engineering System"
url: "https://www.traceable.ai/blog-post/how-1-exposed-honeywell-api-gave-us-control-over-an-internal-engineering-system"
final_url: "https://www.traceable.ai/blog-post/how-1-exposed-honeywell-api-gave-us-control-over-an-internal-engineering-system"
authors: ["Eaton Z. (@XeEaton)"]
programs: ["Honeywell"]
bugs: ["Missing authentication", "Information disclosure", "Broken authorization", "Account takeover"]
publication_date: "2024-08-19"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 60
---

[![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/680c06a5aaf7a245dffb6200_logo%20by%20harness%20\(1\).avif)](/)

[![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/680c06a5aaf7a245dffb6200_logo%20by%20harness%20\(1\).avif)](/)

![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/65df0e0e581868dbe90c39ed_left-arrow.webp)

Back

![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/65def06eb5f223637a3c7ff9_close.webp)

[Why Traceable](/why-traceable-api-security)

# Why Traceable

[Why Traceable](/why-traceable-api-security)[Our Customers](/customer-stories)[About Traceable](/company)[In the News](/press-coverage)[Request Demo](/request-a-demo)

# The Traceable Edge

Discover why Traceable is chosen by the world’s leading organizations

[Learn more![arrow](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/65d5eb6dce96d429b5077e75_arrow-right.png)](/request-a-demo)

Why Traceable

# Why Traceable

[Why Traceable](/why-traceable-api-security)[Our Customers](/customer-stories)[Our Partners](/partner)[About Traceable](/company)[In the News](/press-coverage)[Request Demo](/request-a-demo)

# Traceable AI API Security Platform

Unmatched API discovery and attack detection. API Threat hunting. Infinite scale.

Request a Demo![arrow](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/65d5eb6dce96d429b5077e75_arrow-right.png)

[Platform](/api-security-platform)

# Platform Features

[![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/680c0ad86cd2889174adaa54_api%20discovery%20\(1\).webp)Application & API Posture Management](/application-discovery-and-risk-assessment)[![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/680c0ad8ca434ffc50dc612a_api%20testing%20\(1\).png)Application & API Security Testing](/application-security-testing)[![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/680c0ad8d1276501ab956d8b_attack%20\(1\).png)Application & API Protection](/application-runtime-protection)

# Traceable AI API Security Platform

Unmatched API discovery and attack detection. API Threat hunting. Infinite scale.

[Request a Demo![arrow](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/65d5eb6dce96d429b5077e75_arrow-right.png)](/request-a-demo)

Platform

# Platform Features

[![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/680c0ad86cd2889174adaa54_api%20discovery%20\(1\).webp)Application Discovery & Risk Assessment](/application-discovery-and-risk-assessment)[![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/680c0ad8ca434ffc50dc612a_api%20testing%20\(1\).png)Application Security Testing](/application-security-testing)[![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/680c0ad8d1276501ab956d8b_attack%20\(1\).png)Application Runtime Protection](/application-runtime-protection)

# Traceable AI API Security Platform

Unmatched API discovery and attack detection. API Threat hunting. Infinite scale.

[Request a Demo![arrow](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/65d5eb6dce96d429b5077e75_arrow-right.png)](/request-a-demo)

[Solutions](https://www.traceable.ai/api-protection)

# Solutions

[OWASP Top 10 Protection](/api-protection)[API Security Data Lake](/api-data-lake-context-aware-security)[Contextual Based API Security Testing](/api-security-testing)[Securing Gen-AI APIs](/securing-gen-ai-apis)

# Verticals

[Finance / Banking](/api-security-for-financial-services)[Government and Public Sector](/public-sector-api-security)[Health Care](/api-security-for-healthcare)

Solutions

# Solutions

[OWASP Top 10 Protection](/api-protection)[API Security Data Lake](/api-data-lake-context-aware-security)[Contextual Based API Security Testing](/api-security-testing)[Securing Gen-AI APIs](/gen-ai-api-security)

# Verticals

[Finance / Banking](/api-security-for-financial-services)[High Tech](/public-sector-api-security)[Government and Public Sector](/api-security-for-healthcare)Retail and eCommerce

[Resource Center](/resources)

# Resource Center

[Resources](/resources)[Case Studies](/customer-stories)[Whitepapers](/resources?resource+type_equal=%5B"Whitepaper"%5D)[Blog](/blog)[Customer Success and Support](https://support.traceable.ai/hc/en-us?_gl=1*1t7ghvv*_ga*MTg3NjI2MDgxNS4xNjUzNjE2MTEw*_ga_S88NRYW79H*MTcwOTc3NzA5Ni40My4xLjE3MDk3ODMwNDQuMC4wLjA.)

# What’s New

![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/65d4b091c7ef335eebad734a_Traceable-Practical-Guide-to-API-Security-Ebook-012021_Page_01%202.avif)

# Context-Aware API Security

The Imperative for Complete API Protection

[Read Whitepaper![arrow](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/65d5eb6dce96d429b5077e75_arrow-right.png)](/resources/lp/whitepaper-context-aware-api-security)

Resource Center

# Resource Center

[Resources](/resources)[Case Studies](/resource/case-study)[Whitepapers](/resource/whitepaper)[Blog](/blog)[Documentation](https://docs.traceable.ai/)[Customer Success and Support](https://support.traceable.ai/hc/en-us?_gl=1*1t7ghvv*_ga*MTg3NjI2MDgxNS4xNjUzNjE2MTEw*_ga_S88NRYW79H*MTcwOTc3NzA5Ni40My4xLjE3MDk3ODMwNDQuMC4wLjA.)

# What’s New

![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/65d4b091c7ef335eebad734a_Traceable-Practical-Guide-to-API-Security-Ebook-012021_Page_01%202.avif)

# Context-Aware API Security

The Imperative for Complete API Protection

[Read Whitepaper![arrow](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/65d5eb6dce96d429b5077e75_arrow-right.png)](/resources/lp/whitepaper-context-aware-api-security)

[ASPEN Labs](/aspen-labs)

[Sign In](https://auth.traceable.ai/login?state=hKFo2SA1MWpwOVlhYWhsQnBkbDdMVmY2RDZuY0xOZ2FRRXZnNaFupWxvZ2luo3RpZNkgY0g0VGloQVgxVEkxenB5anIta1Zfd19TSHg2YkVWa1GjY2lk2SB1czVrZGJueGNlM05oZUxiekxDeHVacVlJUVlnUWdtOA&client=us5kdbnxce3NheLbzLCxuZqYIQYgQgm8&protocol=oauth2&redirect_uri=https%3A%2F%2Fapp.traceable.ai%2Fcallback%3Fredirect%3Dhttps%3A%2F%2Fapp.traceable.ai%2F%3F_gl%3D1*1klse9q*_ga*MTg3NjI2MDgxNS4xNjUzNjE2MTEw*_ga_S88NRYW79H*MTcwOTc3NzA5Ni40My4xLjE3MDk3ODQzNTYuMC4wLjA.&scope=openid%20profile%20email&response_type=code)[Request a Demo](/request-a-demo)

[Traceable](https://www.traceable.ai/)

/

[Blog](/blog)

[Traceable ASPEN](/blog-tags/traceable-aspen)

[Security Research](/blog-tags/security-research)

[API Security](/blog-tags/api-security)

# How 1 Exposed Honeywell API Gave us Control Over an Internal Engineering System

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/67128d07b7b4e6d53c2ec10b_Eaton%20Zveare.webp)

Eaton Zveare

|

August 19, 2024

![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/66a74645e5b1725146287674_facebook-icon-blue.avif)![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/66a746452229f98f5c0ef8fb_linkedin-icon-blue.avif)![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/66a748b1212f19f2deee7b12_X%20icon.avif)![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/66a74645e12ce6bc65b64b69_reddit-icon-blue.avif)![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/66a746451fb995fd83e467d9_formik-icon-blue.avif)

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/66c3b7311d8b35894a1998b9_image%20\(4\).webp)![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/67aa062b7732527fcf5fe75c_66c3b7311d8b35894a1998b9_image%2520\(4\).webp)

Developers are increasingly turning to APIs as a mechanism to expose and consume data for their web applications. APIs enable users to rapidly develop their web applications while supporting many different user-agents, but properly implementing access control across all workflows can be challenging. This is especially true for large enterprise APIs that are subject to frequent updates and expansion. In the race to launch new products, and with limited developer resources, it can be challenging to truly prioritize security.

The time for API security is now. These simple API security problems are occurring in some of the world’s largest organizations. If your organization develops APIs, there is always a chance of a security flaw existing now or in the future. These problems are a key focus of our work here at Traceable and our goal is to detect these security flaws before they lead to data breaches or damage. Traceable ASPEN has discovered another case where just one insecure API endpoint was enough to take control over an entire application: Honeywell’s BEDQ system.

## **Honeywell BEDQ**

Honeywell has a lot of subdomains and we eventually stumbled upon the BEDQ website: <https://uopbedq.honeywell.com/>. BEDQ is an internal system used by Honeywell employees and partners to submit engineering project proposals. It stands for “Basic Engineering Design Questionnaire”. It is used by companies all over the world to submit information about their projects to Honeywell. It is particularly popular in the oil & gas industry.

The BEDQ website requires a Honeywell ID to log in. By going to a different Honeywell website, we could register one and then use the login here. Honeywell IDs can be registered by anyone and the BEDQ login page was the same for internal users and consumers. In cases like this, websites may not correctly differentiate between an internal employee and a customer who just registered to access a specific website. This is [similar to Mercedes-Benz](https://samcurry.net/web-hackers-vs-the-auto-industry/) where the employee/corporate login system is the same one that external independent service providers use.

## **The users API**

After logging into BEDQ, we were quickly shown a “401: Unauthorized” page. This was not surprising, and it was good to see that Honeywell had access controls in place for their internal websites. While we could not progress past this page, we could view the source code of the website. It is an Angular application and we dug into the code to see if there were any interesting APIs that might be exploitable. While most of the APIs were properly secured, there was one critical oversight: the users API did not require authentication. In other words, a simple HTTP GET request to the “/api/users/” endpoint would return a list of all users registered in the system:

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/66c352ca52e37d0cfa5668ba_AD_4nXcKnMClK5fHEUsusLV4-2_Z7nVkLjFn1stL80mh69r--uGLd4WK5vACeuoPfCHTBJW7oTli-Y7i4li1P0wzMa53IkUkug52fjfaxyDSoKD8P6cbX6nlfp8-1SkHIg5vxiGyCYLMlNZEm70LGH05sj9heUT6.png)

By exploring further we were able to chain this initial vulnerability with another. This is important when exploring the impact of security vulnerabilities, as attackers will always seek to pivot within a system or escalate their privileges. While exploring the “/api/users/” API we noticed two interesting facts:

  1. There was an old/unused test user.
  2. The API allowed a regular user to make a PUT request to update users other than their own. This is something that usually requires administrator privileges.

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/66c352ca49e5516c54390f2d_AD_4nXfF9eGQHxjOTmmSsP7adYF0CJsykuh4kCDBtsN0cpP7w2Ue-JBP_ZG2gSfYhQCGyozX9pg1pAbBziNLrfTStVhrZaHa8q4p0PR0KPTXHvjpQC6j80oGryxKSllG2KO_z5Lk5NWL7T5_q8EePgSJg5iXJxDp.png)

Putting these two findings together, we were able to update our user as an internal user with super administrator privileges.

## **Internal super admin access achieved**

With the user update done, the moment of truth was at hand: logging in again and seeing if we were granted access. Since our Honeywell ID’s email address was now in the BEDQ system, we believed the login would work since this is now a match. Our theory was correct - the login succeeded, and we were granted complete control over the entire system. This means we had full access to the projects of every company and all the sensitive information inside. We decided to stop here and quickly report our findings to Honeywell.

## **Reporting to Honeywell**

The Traceable ASPEN team reported to [Honeywell’s vulnerability disclosure program](https://www.honeywell.com/us/en/product-security). We also made sure to tell them about the changes to the test user so that they could restore it to its original state. The timeline is as follows:

  * **August 18, 2023:** Report sent.
  * **August 24, 2023:** Follow-up sent asking if they received the report. They responded same-day confirming they did.
  * **September 11, 2023:** We requested an update.
  * **September 15, 2023:** Honeywell confirms the vulnerability is resolved and asks for [hall-of-fame](https://www.honeywell.com/us/en/product-security#acknowledgments) credit information, which we provide.

Honeywell’s prompt response to our vulnerability report highlights their commitment to customer security. We appreciate their partnership in helping improve the security of their BEDQ application.

## **Lessons & takeaways**

This Vulnerability was caused by chaining two very common API vulnerabilities:

1: [Broken Authentication](https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/) is one of the most common API vulnerabilities that we come across. In this instance, even though nearly all APIs were authenticated and had access controls, it only took one unauthenticated Users API to bypass the security of the entire platform.

2: [Broken Function Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/) is an API vulnerability caused by inadequate authorization controls. A common scenario is when a function that should be limited to a privileged user is made available to a non-privileged user. In this application, the HTTP PUT method on the users API should be only available to an admin user. 

## **Recommendations**

  * Depending on the application stack, it is generally recommended to have a single gateway or reverse proxy to implement authentication and authorization. This ensures that over time, as new APIs are developed or existing ones are modified, they all continue to provide the standard access controls.
  * APIs and Users should be explicitly mapped to user roles and if a user accesses an API that requires a more privileged role, it should be blocked by a [403 - Forbidden](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403) error.
  * Interactive Application Security Testing (IAST) is a good mechanism to test APIs and find such vulnerabilities earlier in the SDLC before the application is deployed in the production. For example, a relevant test case would be to mutate HTTP requests and remove request headers one or multiple at a time to test authorization controls.

## **How Traceable can help**

Traceable's mission is to secure the world's APIs. Traceable Sonar offers advanced external attack surface discovery, so you know what's public, be it leaked credentials, misconfigurations or sensitive data. If you'd like to find out more, request a demo.

Download Blog Post

### The Inside Trace

Subscribe for expert insights on application security.

Thanks! Your subscription has been recorded.

[or subscribe to our RSS Feed![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/6654d6b8d5248bc99ee107a5_rss%20feed%20icon.svg)](/blog-post/rss.xml)

## Read more

[API Security Masterclass Recap: Your Guide to the OWASP API Top 10](/blog-post/api-security-masterclass-recap-owasp-api-top-10)

[The Prescription for Vulnerable Mobile Health Apps: Protect APIs](/blog-post/the-prescription-for-vulnerable-mobile-health-apps-protect-apis)

[Spring4shell vulnerability (CVE-2022-22965) enables Remote Code Execution when using the Spring Framework](/blog-post/spring4shell-vulnerability-cve-2022-22965-enables-remote-code-execution-when-using-the-spring-framework)

[Application Security in the Public Cloud Requires Shared Responsibility](/blog-post/application-security-in-the-public-cloud-requires-shared-responsibility)

## See Traceable in Action

Learn how to elevate your API security today.

[Get Started](/request-a-demo)

![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/660eea1da139dc8fe95e4734_tracables%20in%20action%20background%20img-min.avif)

## Read more

[![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/69e1ae561353b66869ac5245_67aa05fcafd787a4d03ff76e_66a9fd187b43ab524e87d192_66a9ef10c83ec334b420161e_API%252520Security%20\(1\).webp)](/blog-post/what-is-sensitive-data-exfiltration-api-security)

#### [Sensitive Data Exfiltration: The New Nemesis of API Security](/blog-post/what-is-sensitive-data-exfiltration-api-security)

[API Security](/blog/?blogs-category-name=API-Security)

[Foundations](/blog/?blogs-category-name=Foundations)

[![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/66da1d509b653b0e5191884b_Aspen%20Labs.webp)](/blog-post/jwts-under-the-microscope-how-attackers-exploit-authentication-and-authorization-weaknesses)

#### [JWTs Under the Microscope: How Attackers Exploit Authentication and Authorization WeaknessesJSON Web Tokens (JWTs) offer stateless authentication in modern web applications, but improper implementation can expose critical vulnerabilities. This analysis explores attack vectors across JWT components, revealing how small oversights can lead to significant security breaches like privilege escalation and unauthorized access.](/blog-post/jwts-under-the-microscope-how-attackers-exploit-authentication-and-authorization-weaknesses)

[Traceable ASPEN](/blog/?blogs-category-name=Traceable+ASPEN)

[![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/69e1ae561353b66869ac5245_67aa05fcafd787a4d03ff76e_66a9fd187b43ab524e87d192_66a9ef10c83ec334b420161e_API%252520Security%20\(1\).webp)](/blog-post/scary-thoughts-this-halloween-a-world-without-apis)

#### [Scary Thoughts This Halloween: A World Without APIs!](/blog-post/scary-thoughts-this-halloween-a-world-without-apis)

[API Security](/blog/?blogs-category-name=API-Security)

[View All Blogs](/blog)

![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/680c06a5aaf7a245dffb6200_logo%20by%20harness%20\(1\).avif)

[](https://twitter.com/traceableai)[](https://www.linkedin.com/company/traceable-ai/)[](https://www.youtube.com/channel/UCTfTAQ0W-Hx1nWIJhwCKGMw/)

WHY TRACEABLE

[Why Traceable](/why-traceable-api-security)[Our Customers](/customer-stories)[In the News](/press-coverage)[Request Demo](/request-a-demo)

[PLATFORM](/api-security-platform)

[Application & API Posture Management](/application-discovery-and-risk-assessment)[Application & API Security Testing](/application-security-testing)[Application & API Protection](/application-runtime-protection)

USE CASES

[API Discovery](/api-catalog-discovery)[Shift Left Security](/api-security-testing)[Sensitive Data Exfiltration](/sensitive-data-exfiltration)[Account Takeover](/digital-fraud-prevention-api-security)[Bot Mitigation](/digital-fraud-prevention-api-security)[Incident Response](/api-analytics)[Data Privacy and Compliance](/security-and-compliance)

RESOURCES

[Overview](/resources)[Related API Resources ](/tag/apis)[Blog](/blog)[Webinars](/resource/webinar)[Customer Peer Reviews](/peer-review)[Case Studies](/customer-stories)[White Paper](/resource/whitepaper)[Datasheets](/resource/data-sheet)[Learning Center](https://docs.traceable.ai/)[Customer Success & Support](https://support.traceable.ai/hc/en-us?_gl=1*1t7ghvv*_ga*MTg3NjI2MDgxNS4xNjUzNjE2MTEw*_ga_S88NRYW79H*MTcwOTc3NzA5Ni40My4xLjE3MDk3ODMwNDQuMC4wLjA)

COMPANY

[Sign In ](https://app.traceable.ai)[About Traceable](/company)[Careers](/careers)[Press](/all-press-coverage)[Press Kit](/press-kit)[Customer Support](https://support.traceable.ai/hc/en-us?_gl=1*1brytq8*_ga*MjcwODU1MTEuMTcwMDUxMjY1Mw..*_ga_S88NRYW79H*MTcwOTgyNTExNy42Ni4xLjE3MDk4MzI3MDEuMC4wLjA.)[Security and Compliance](/about/compliance)[Legal](/legal)[Privacy Policy](/privacy-policy)

© 2025 Harness Inc.

[Subscription Terms](/legal/website-terms-of-use)[Website Terms of Use](/legal/website-terms-of-use)[Privacy Statement](/legal/privacy)[Opt Out![Do Not Sell / Share My Personal Information](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/67ec5b57c54422e36e01a59f_privacyoptions.svg)](https://harness-privacy.relyance.ai/)

[Cookie Settings](javascript:void\(0\))

[](https://github.com/harness/drone)[](https://www.linkedin.com/company/harnessinc/)[](https://www.facebook.com/harnessinc/)[](https://www.instagram.com/harness.io/)[](https://twitter.com/harnessio)

© 2024 Harness Inc.
