---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-05_angular-ing-for-authz-problematic-anti-patterns-in-single-sign-on-systems.md
original_filename: 2024-03-05_angular-ing-for-authz-problematic-anti-patterns-in-single-sign-on-systems.md
title: Angular-ing for AuthZ, Problematic anti-patterns in Single Sign On Systems
category: documents
detected_topics:
- api-security
- oauth
- access-control
- cloud-security
- sso
- jwt
tags:
- imported
- documents
- api-security
- oauth
- access-control
- cloud-security
- sso
- jwt
language: en
raw_sha256: aae03f6a58c9f9b6a780ccb1ecb791fcb9a4f2b0b90361a04f1098ac411bc963
text_sha256: b9d79155c8ab2c1686d5c9192fd99238f7be08161998b368762ca853fc91dac1
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Angular-ing for AuthZ, Problematic anti-patterns in Single Sign On Systems

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-05_angular-ing-for-authz-problematic-anti-patterns-in-single-sign-on-systems.md
- Source Type: markdown
- Detected Topics: api-security, oauth, access-control, cloud-security, sso, jwt
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `aae03f6a58c9f9b6a780ccb1ecb791fcb9a4f2b0b90361a04f1098ac411bc963`
- Text SHA256: `b9d79155c8ab2c1686d5c9192fd99238f7be08161998b368762ca853fc91dac1`


## Content

---
title: "Angular-ing for AuthZ, Problematic anti-patterns in Single Sign On Systems"
page_title: "Traceable - Blog: Angular-ing for AuthZ, Problematic anti-patterns in Single Sign On Systems"
url: "https://www.traceable.ai/blog-post/angular-ing-for-authz-problematic-anti-patterns-in-single-sign-on-systems"
final_url: "https://www.traceable.ai/blog-post/angular-ing-for-authz-problematic-anti-patterns-in-single-sign-on-systems"
authors: ["Traceable ASPEN"]
bugs: ["SSO", "Authentication bypass"]
publication_date: "2024-03-05"
added_date: "2024-09-18"
source: "pentester.land/writeups.json"
original_index: 393
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

[Security Research](/blog-tags/security-research)

[Traceable ASPEN](/blog-tags/traceable-aspen)

[API Security](/blog-tags/api-security)

# Angular-ing for AuthZ, Problematic anti-patterns in Single Sign On Systems

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/67128d07b7b4e6d53c2ec10b_Eaton%20Zveare.webp)

Eaton Zveare

|

March 5, 2024

![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/66a74645e5b1725146287674_facebook-icon-blue.avif)![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/66a746452229f98f5c0ef8fb_linkedin-icon-blue.avif)![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/66a748b1212f19f2deee7b12_X%20icon.avif)![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/66a74645e12ce6bc65b64b69_reddit-icon-blue.avif)![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/66a746451fb995fd83e467d9_formik-icon-blue.avif)

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/66a9fd278d7857247f64c0f2_66a3678333c13bbf2c43bb87_Aspen%2520Labs.webp)![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/66a9fd278d7857247f64c0f2_66a3678333c13bbf2c43bb87_Aspen%2520Labs.webp)

Authentication is one of the most crucial elements of any application. It is perhaps unsurprising that many choose to use Single Sign On (SSO) from Google, Microsoft, and others. Instead of managing an entire login flow, forgotten password flow and other authentication patterns, SSO offloads this workload to the SSO provider. While this has numerous advantages for development teams, these systems are built for third parties passing around tokens via APIs; if these tokens aren’t handled with care, the entire login system can be exploited.Using publicly available information and APIs, the ASPEN team identified a flaw in the SSO login flow of a Fortune 500 company in the health and wellbeing sector and promptly reported it. While this specific vulnerability has now been resolved and mitigated, it is important to recognize some of the flaws in login flows that could easily be replicated in other environments and applications.

## **Bypassing an SSO login flow**

The ASPEN team initially identified this Angular application with SSO after performing subdomain reconnaissance on a well-known large healthcare brand. Angular websites are a goldmine for API research since these websites typically offer a highly interactive JavaScript front end that then calls REST API endpoints. A typical login flow would be:

  1. It would check for a logged in user (via Microsoft SSO) and redirect to the SSO page if there is not.
  2. It would call the Microsoft Graph API to retrieve the user’s information. In particular, it wanted the email address.
  3. The email address was used in a user search API to retrieve the user’s information. This included data like name, access role, and regions the user is allowed to access.
  1. This API (and all others) on the website used API key authentication, and that key was present in the client-side JavaScript.
  4. The login data is saved to session storage. The _role_ and _region_ are used later to control and present data.

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/667fa6c071414a358ee7c12d_image2.png)

We conducted research to find the best way to gain entry into the app with as little modification as possible. The user search API works by sending an email address, so we attempted to locate potentially valid company emails on LinkedIn and Google. We tried various emails and even some wildcard patterns. Nothing was successful in getting the API to reveal user information until a value of “all” was used. When that was used, it returned all the user information in the system:

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/667fa6c071414a358ee7c13b_image4.webp)

We now know all the valid user emails and with this, we were ready to make changes to the Angular code.

## **Angular code modifications**

The goal of our modifications was to trick the app into thinking that the SSO login succeeded, and set the logged in email to one that is known to be a Global Admin. The app had to be modified 3 different ways:First, a few changes had to be made to the login function to trick it into thinking a valid user is logged in:

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/667fa6c071414a358ee7c137_image5.png)

Second, there was an issue where some pages would redirect to SSO login, despite the user having the proper access role. The easiest way to fix and allow access to all pages was to simply short-circuit the Angular [_canActivate_](https://angular.io/api/router/CanActivate) function and return true in all cases:

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/667fa6c071414a358ee7c128_image6.png)

Finally, we modified the Microsoft Angular Authentication Library’s [_activateHelper_](https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/90629381de88e0bb391c3cb658b9ec2923806993/lib/msal-angular/src/msal.guard.ts#L122) function to trick it into thinking an account is logged in. This stopped another case of being redirected to the SSO login:

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/667fa6c071414a358ee7c131_image3.png)

Once all that was done, we had Global Admin access to the entire app and could access the records of **7½ million users** :

![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/667fa6c071414a358ee7c134_image1.webp)

## **Reporting to the company**

The Traceable ASPEN team put together a report and sent it through the company’s vulnerability disclosure program. The timeline is as follows:

  * **September 18, 2023:** Report sent. 12 minutes later, the company responded confirming they received the report.
  * **September 20, 2023:** The company confirmed the issue was valid and are working on fixing it. At this point the entire website had been taken offline, so the issue was essentially contained.

As seen from the timeline, the company's response to our report was exemplary. Often it takes weeks, if not months, to get an acknowledgement and remediation done. This was one of our best experiences engaging with a vulnerability disclosure team, and we believe that they are a great model for efficiency and others should strive for a similar response. We shared this blog with the company prior to publication for their approval. On their request, we have redacted their name.

## **Lessons & takeaways**

The Traceable ASPEN team was able to identify this API security vulnerability before it could have been abused. Our recommendations for similar SSO Angular applications are:

  1. Stop and think before including any API keys in your code. Think about what could happen if you published the key for the world to see. If you must include them, make sure they are narrowly scoped to specific operations they are needed for. Remember that these keys provide long-term access to data. For APIs meant to be accessed by logged in users, API key authentication is not a good fit.
  2. Fully implement SSO login tokens and login. In this case, instead of using the OAuth token, they used API keys. All the company’s APIs should have used this SSO access token to authenticate instead of an API key. It is also important to check what permissions the user has and properly deny access to API resources the user is not allowed to use.
  3. Check to make sure that admin APIs are well protected. The user search API with the “email=all” query option seems to be an admin API, but it was accessible by a user API key. This is what is called a [BFLA (Broken Function Level Authorization)](https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/) vulnerability. Make sure all APIs implement proper access controls to avoid introducing backdoors into your websites.

## **How Traceable can help**

[Traceable ASPEN](https://traceable.ai/blog-post/traceable-aspen-leading-the-charge-in-api-security-research) provides vendor neutral and threat driven research in API security, investigating the latest breaches with world leading expertise and analysis. We believe in securing the world’s APIs with actionable insights from across the industry. We are offensively minded, defensively driven, and focused on your protection. Get the ASPEN advantage, join the biggest names in finance and software and secure your most valuable API assets with Traceable’s complete API security platform. From attack surface discovery, advanced mitigation and blocking to threat intelligence, see how we can transform your API security across the API lifecycle and [request a demo today](https://traceable.ai/request-a-demo).

Download Blog Post

### The Inside Trace

Subscribe for expert insights on application security.

Thanks! Your subscription has been recorded.

[or subscribe to our RSS Feed![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/6654d6b8d5248bc99ee107a5_rss%20feed%20icon.svg)](/blog-post/rss.xml)

## Read more

[Traceable API Security Platform Updates - September 2023](/blog-post/traceable-api-security-platform-updates-september-2023)

[Cybersecurity Roundup for January 2023: API Attacks Front and Center](/blog-post/cybersecurity-roundup-for-january-2023-api-attacks-front-and-center)

[My Journey With Traceable Begins](/blog-post/my-journey-with-traceable-begins)

[The Imperative of API Ownership: A Nexus of Development and API Security](/blog-post/the-imperative-of-api-ownership-a-nexus-of-development-and-api-security)

## See Traceable in Action

Learn how to elevate your API security today.

[Get Started](/request-a-demo)

![](https://cdn.prod.website-files.com/65c483f725156eae6eed4056/660eea1da139dc8fe95e4734_tracables%20in%20action%20background%20img-min.avif)

## Read more

[![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/66c3b7311d8b35894a1998b9_image%20\(4\).webp)](/blog-post/how-1-exposed-honeywell-api-gave-us-control-over-an-internal-engineering-system)

#### [How 1 Exposed Honeywell API Gave us Control Over an Internal Engineering SystemAPIs are crucial for web apps but pose security risks. Traceable uncovered a critical flaw in Honeywell's BEDQ system, highlighting the need for strong API security.](/blog-post/how-1-exposed-honeywell-api-gave-us-control-over-an-internal-engineering-system)

[Traceable ASPEN](/blog/?blogs-category-name=Traceable+ASPEN)

[Security Research](/blog/?blogs-category-name=Security+Research)

[API Security](/blog/?blogs-category-name=API-Security)

[![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/66a37e7de4f9d94bd21abb50_66a36784f02d40282e761d99_Fraud.webp)](/blog-post/the-regulators-are-coming-for-your-washing-machine-app)

#### [The Regulators Are Coming for Your Washing Machine AppDiscover how the PSTI Act 2022 and 2023 regulations shape IoT security, impacting manufacturers with new compliance standards and necessary steps for adherence.](/blog-post/the-regulators-are-coming-for-your-washing-machine-app)

[Breach Analysis](/blog/?blogs-category-name=Breach+Analysis)

[Security Research](/blog/?blogs-category-name=Security+Research)

[![](https://cdn.prod.website-files.com/65c5190e5dd9c9f6dde799df/66da1d509b653b0e5191884b_Aspen%20Labs.webp)](/blog-post/albeast-a-simple-misconfiguration-to-a-complete-authentication-bypass)

#### [ALBeast: a simple misconfiguration to a complete authentication bypassThe ALBeast vulnerability represents a critical security flaw in AWS Application Load Balancer (ALB) authentication implementation that could lead to complete authentication bypass. This vulnerability, affecting over 15,000 applications, stems from improper validation of AWS-specific header claims and misconfigured security groups, allowing attackers to forge authentication tokens and impersonate legitimate users. The issue highlights the importance of proper JWT validation and security group configuration in AWS ALB implementations.](/blog-post/albeast-a-simple-misconfiguration-to-a-complete-authentication-bypass)

[Traceable ASPEN](/blog/?blogs-category-name=Traceable+ASPEN)

[Security Research](/blog/?blogs-category-name=Security+Research)

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
