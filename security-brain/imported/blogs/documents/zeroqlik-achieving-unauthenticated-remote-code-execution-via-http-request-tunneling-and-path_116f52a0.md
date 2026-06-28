---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-31_zeroqlik-achieving-unauthenticated-remote-code-execution-via-http-request-tunnel.md
original_filename: 2023-08-31_zeroqlik-achieving-unauthenticated-remote-code-execution-via-http-request-tunnel.md
title: 'ZeroQlik: Achieving Unauthenticated Remote Code Execution via HTTP Request
  Tunneling and Path Traversal'
category: documents
detected_topics:
- sso
- command-injection
- path-traversal
- mfa
- api-security
- idor
tags:
- imported
- documents
- sso
- command-injection
- path-traversal
- mfa
- api-security
- idor
language: en
raw_sha256: 116f52a0e120083a1aab201f1885ab95d0461255c9a05c555b0aab7c12a76eef
text_sha256: fe4ba567be81dd91dceab07b5075c8ebd0da08ebce6c1b6d1595c5671149a1d2
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# ZeroQlik: Achieving Unauthenticated Remote Code Execution via HTTP Request Tunneling and Path Traversal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-31_zeroqlik-achieving-unauthenticated-remote-code-execution-via-http-request-tunnel.md
- Source Type: markdown
- Detected Topics: sso, command-injection, path-traversal, mfa, api-security, idor
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `116f52a0e120083a1aab201f1885ab95d0461255c9a05c555b0aab7c12a76eef`
- Text SHA256: `fe4ba567be81dd91dceab07b5075c8ebd0da08ebce6c1b6d1595c5671149a1d2`


## Content

---
title: "ZeroQlik: Achieving Unauthenticated Remote Code Execution via HTTP Request Tunneling and Path Traversal"
page_title: "ZeroQlik: Achieving Unauthenticated Remote Code Execution via HTTP Request Tunneling and Path Traversal | Praetorian"
url: "https://www.praetorian.com/blog/qlik-sense-technical-exploit/"
final_url: "https://www.praetorian.com/blog/qlik-sense-technical-exploit/"
authors: ["Adam Crosser"]
programs: ["Qlik"]
bugs: ["RCE", "Path traversal", "HTTP request tunneling", "HTTP request smuggling", "Security code review"]
publication_date: "2023-08-31"
added_date: "2023-09-05"
source: "pentester.land/writeups.json"
original_index: 819
---

Skip to content

**Meet Constantine – Find Mythos-level vulnerabilities in your code. It proves them, patches them, PRs them back. Autonomously.**

[ Download Datasheet ](/resources/constantine-datasheet/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

  * Platform  Close Platform Open Platform

#### [Praetorian Guard Platform](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Services  Close Services Open Services

#### [Penetration Testing Services](/penetration-testing/)

  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)
  * [LLM Penetration Testing](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [Application Penetration Testing](https://www.praetorian.com/services/application-penetration-testing/)
  * [Automotive Penetration Testing](https://www.praetorian.com/services/automotive-penetration-testing/)
  * [Cloud Penetration Testing](https://www.praetorian.com/services/cloud-penetration-testing/)
  * [IoT Penetration Testing](https://www.praetorian.com/services/iot-penetration-testing/)
  * [Network Penetration Testing](https://www.praetorian.com/services/network-penetration-testing/)

#### [Advanced Offensive Security](/advanced-penetration-testing/)

  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)
  * [Assumed Breached](https://www.praetorian.com/services/assumed-breached-exercise/)
  * [Attack Path Mapping](https://www.praetorian.com/guard/attack-path-mapping/)
  * [CI/CD Attack Chains](https://www.praetorian.com/services/ci-cd-security-engagement/)
  * [Purple Team](https://www.praetorian.com/services/purple-team/)
  * [Red Team](https://www.praetorian.com/services/red-team/)

#### [Continuous Offensive Security](/guard/)

  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)
  * [Adversarial Exposure Validation](https://www.praetorian.com/guard/breach-attack-simulation/)
  * [Attack Surface Management](https://www.praetorian.com/guard/attack-surface-management/)
  * [Continuous Penetration Testing](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [Continuous Threat Exposure Management](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [Cyber Threat Intelligence](https://www.praetorian.com/guard/threat-intelligence/)
  * [Unified Vulnerability Management](https://www.praetorian.com/guard/vulnerability-management/)

  * Why Praetorian  Close Why Praetorian Open Why Praetorian

#### [Customer Case Studies](/customer-success-in-cybersecurity/)

  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)
  * [21st Century Fox](https://www.praetorian.com/customer-success-in-cybersecurity/21st-century-fox/)
  * [Cushman & Wakefield](https://www.praetorian.com/customer-success-in-cybersecurity/cushman-wakefield/)
  * [Bookings Holdings](https://www.praetorian.com/customer-success-in-cybersecurity/cybersecurity-partnership-bookings-holdings/)
  * [Nielsen](https://www.praetorian.com/customer-success-in-cybersecurity/nielsen/)
  * [OpenTable](https://www.praetorian.com/customer-success-in-cybersecurity/open-table/)
  * [Priceline](https://www.praetorian.com/customer-success-in-cybersecurity/priceline/)
  * [Samsung](https://www.praetorian.com/customer-success-in-cybersecurity/samsung-electronics/)
  * [X](https://www.praetorian.com/customer-success-in-cybersecurity/x-twitter/)
  * [Zoom](https://www.praetorian.com/customer-success-in-cybersecurity/zoom-2/)
  * [See All Customers](https://www.praetorian.com/customer-success-in-cybersecurity/)

#### Resources

  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)
  * [Security Blog](https://www.praetorian.com/blog/)
  * [Resource Library](https://www.praetorian.com/resources/)
  * [Security 101](/security-101/)
  * [Labs](https://www.praetorian.com/praetorian-labs/)
  * [GitHub](https://github.com/praetorian-inc/)
  * [MITRE ATT&CK](https://www.praetorian.com/mitre-attack/)
  * [Speaking and Events](https://www.praetorian.com/speaking-and-events/)
  * [Warlocks](https://wherewarlocksstayuplate.com/)

#### Use Cases

  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)
  * [ASM for Healthcare](https://www.praetorian.com/guard/attack-surface-management-healthcare/)
  * [Bug Bounty Cost Reduction](https://www.praetorian.com/services/bug-bounty-cost-reduction/)
  * [FDA Testing and Monitoring](https://www.praetorian.com/services/fda-testing-monitoring/)
  * [Mergers and Acquisitions](https://www.praetorian.com/services/mergers-acquisitions/)
  * [Ransomware Prevention](https://www.praetorian.com/services/ransomware-prevention/)
  * [Rogue IT Identification](https://www.praetorian.com/services/rogue-it-identification/)
  * [Tool and Vendor Consolidation](https://www.praetorian.com/services/tool-vendor-consolidation/)
  * [Vendor Risk Management](https://www.praetorian.com/services/vendor-risk-management/)

  * About  Close About Open About

#### [About Praetorian](/praetorian-offensive-cybersecurity-company/)

  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)
  * [Overview](https://www.praetorian.com/about-us/)
  * [In the News](/news/news/)
  * [Press Releases](/news/press-release/)
  * [Contact Us](https://www.praetorian.com/contact-us/)

#### [Join Praetorian](/careers/#job-opening)

  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)
  * [Culture](https://www.praetorian.com/work-at-praetorian/)
  * [People Ops Blog](/people-ops/)
  * [New Hire Survival Guide](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)
  * [Tech Challenges​](https://www.praetorian.com/challenges/)
  * [Job Postings](https://www.praetorian.com/careers/#job-opening)

  * [ Platform Demo  ](/praetorian-guard-demo/)

  * [ Contact Us  ](/contact-us/)

  * [Labs](https://www.praetorian.com/category/labs/), [Uncategorized](https://www.praetorian.com/category/uncategorized/)

# ZeroQlik: Achieving Unauthenticated Remote Code Execution via HTTP Request Tunneling and Path Traversal

  * [Adam Crosser](https://www.praetorian.com/author/adam-crosser/)
  * [ August 31, 2023 ](https://www.praetorian.com/blog/2023/08/31/)

![](https://www.praetorian.com/wp-content/uploads/2024/06/ZeroQlik-1.png)

## Overview

In an effort to safeguard our customers, we perform proactive vulnerability research with the goal of identifying zero-day vulnerabilities that are likely to impact the security of leading organizations. Recently, we decided to take a look at Qlik Sense Enterprise, a data analytics solution similar to Tableau. The recent [exploitation of vulnerabilities in the GoAnywhere and MoveIT MFT applications by the cl0p ransomware gang](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a) highlights the need for proactive vulnerability research focused on finding critical issues before attackers can identify and exploit them.

During our research into the application we identified an HTTP request tunneling vulnerability which allowed an attacker to bypass security controls implemented by a frontend proxy service and impersonate a privileged service account to a backend service. These vulnerabilities provided an attacker the ability to perform administrative actions including remote code execution through the execution of external tasks and adding a new administrative user to the Qlik Sense Enterprise application. These vulnerabilities have been assigned CVE-2023-41265 (HTTP Tunneling Vulnerability in Qlik Sense Enterprise for Windows) and CVE-2023-41266 (Path Traversal in Qlik Sense Enterprise for Windows).

We begin the article with a brief discussion of the architecture of the Qlik Sense application architecture, then explain our methodology and how we identified the vulnerability, discuss some of the issues we had with exploiting the issue, and conclude with some additional notes and recommendations.

### Why Research Qlik Sense?

Our primary interest in Qlik Sense came from its use by Chariot customers, the large number of instances on Shodan (around six thousand externally facing instances), and the high value nature of the software given its usage for data analytics. Because organizations use Qlik Sense for data analytics, we hypothesized that they most likely would provide the application with both database credentials and internal network access to corporate environments. This combination of factors made it a high value target for research purposes.

## Qlik Sense Architecture Overview

We began our research by becoming familiar with the basic architecture of the Qlik Sense application. Our primary focus was to understand the application’s exposed pre-authentication attack surface. We then focused on identifying issues that we could exploit for remote code execution without any prior authentication. Figure 1 shows [a simplified architecture diagram of the Qlik Sense application](https://data-flair.training/blogs/qlik-sense-architecture/).

![](https://www.praetorian.com/wp-content/uploads/2024/06/ZeroQlik-1.png)

_Figure 1: A simplified architecture diagram of a single-node deployment of the Qlik Sense application._

As Figure 1 shows, a Proxy service routes all external requests from the user to various backend components. These components implement various pieces of functionality and are written in a variety of programming languages like NodeJS and C#. Our research showed that the attack surface of the Qlik Sense application from an unauthenticated user perspective was quite small and unauthenticated users in the default configuration weren’t typically allowed to do much more than login. However, on Shodan we did identify several instances of the application that had an optional anonymous access mode enabled, which allowed for viewing some limited data.

During our initial enumeration of the application’s attack surface we leveraged Shodan to identify externally facing instances of the application. Doing so helped us determine what ports and services are commonly exposed externally. Our research indicated, as shown in Figure 2, that the overwhelming majority of identified instances only exposed port 443/TCP externally.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20376'%3E%3C/svg%3E)

_Figure 2: Our analysis using data from Shodan indicated that real world Qlik Sense deployments mostly just exposed the HTTPS port externally._

After reviewing the architecture and attack surface of the application we concluded that, because of a relatively minimal attack surface within externally-facing deployments, we should focus on the authorization and authentication logic the proxy service implements. Bypassing the proxy service would unlock a substantial attack surface and provide more potential routes to remote code execution.

## Identifying the Vulnerabilities

### Initial Source Code Review

The proxy service was written in C#, which made analysis fairly straightforward. We began by decompiling the proxy service and performing a code review of the authentication and request routing logic. One piece of functionality that stood out to us was the logic for forwarding requests to backend services. As Figure 3 shows, the function ForwardPostData first checked for the Content-Length header before checking for the Transfer-Encoding header. We knew, however, that the HTTP specification ([RFC2616](https://www.ietf.org/rfc/rfc2616.txt)) states that a “message must not include both a Content-Length header field and a non-identity transfer-coding. If a message does include a non-identity transfer-encoding, the Content-Length MUST be ignored.”

We thought this code snippet looked quite risky as the proxy service is forwarding the message body based on the Content-Length header, but any application which conforms to the RFC2616 specification will leverage the Transfer-Encoding field when determining message length. This misalignment could potentially result in an [HTTP request tunneling vulnerability](https://portswigger.net/web-security/request-smuggling/advanced/request-tunnelling).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20644%20236'%3E%3C/svg%3E)

_Figure 3: An initial review of the proxy source code indicated that the proxy service leveraged the Content-Length header first before the Transfer-Encoding header which differs from the stated behavior in the HTTP specification._

We leveraged a debugger to examine requests generated by the proxy and sent to backend services. We observed that the proxy injected these headers into requests forwarded to backend services. We also observed that the proxy would block requests containing these headers. Figure 4 shows the header blacklisting mechanism in action. Figure 5 shows a request with the X-Qlik-* headers injected by the proxy into requests forwarded to backend services.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20347'%3E%3C/svg%3E)

_Figure 4: We observed that a blacklist was leveraged to prevent certain headers such as the X-Qlik-User header from being sent by the end-user in a request forwarded by the proxy service to a backend service._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20320'%3E%3C/svg%3E)

_Figure 5: We observed that the proxy inserted the blacklisted headers into requests forwarded to backend services such as the X-Qlik-User header leveraged to specify the user associated with the request._

Another important point to note is that the authentication between the proxy and internal services involves certificates for both client and server authentication. However, after the proxy authenticates to the backend service the system trusts all requests over that communications channel, including any headers. An attacker that is able to bypass the header blacklisting mechanism could therefore impersonate arbitrary users and perform privileged actions when communicating with backend services.

### Mapping Request Routing to Backend Services

The next step in our analysis involved mapping out how the proxy routed requests to [various backend services exposed through the proxy](https://help.qlik.com/en-US/sense-admin/May2023/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Deploy_QSEoW/Ports.htm). We leveraged the dnSpy debugger and set a breakpoint on the HttpChannelHandler.ForwardRequest function (see Figure 6). Figure 7 shows some of the requests and their corresponding backend services, which the path in the request dictated. The list in Figure 7 is by no means exhaustive.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20313'%3E%3C/svg%3E)

_Figure 6: We attached a debugger to the proxy service and set a breakpoint on the HttpChannelHandler.ForwardRequest function. We observed authentication requests being forwarded to a service running on port 4244._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20644%20191'%3E%3C/svg%3E)

_Figure 7: A non-exhaustive list of some of the routes we identified leveraging the dnSpy debugger to monitor where requests were being routed to various backend services based on their associated request path._

### Testing for Request Tunneling Issues

At this point, we knew that the proxy service would route requests to backend services based on the Content-Length header while forwarding both the Content-Length and Transfer-Encoding headers to backend services. In order for the request tunneling attack to work we needed to meet the following preconditions:

  1. The backend service should not drop requests containing both a Content-Length and a Transfer-Encoding header within the same message.
  2. The backend service should use the Transfer-Encoding header when both the Content-Length and Transfer-Encoding headers are specified in a request routed to the backend.
  3. Assuming the following two preconditions are met, the backend service should process the request body so that it would identify multiple requests sent over the same connection.

We performed testing against the broker service and the repository service to determine how they would each respond to specially crafted requests containing both a Content-Length and a Transfer-Encoding header. Figure 8 shows the request sent to the broker service and the corresponding response. We determined that this is because the NodeJS HTTP server appears to drop requests when both of these headers are present based on a[ Github discussion we identified](https://github.com/nodejs/http-parser/issues/517).

Please note that we performed the testing in this section by directly communicating with the backend services. This allowed us to determine the behavior of the services when they received various types of requests forwarded by the proxy. It also made testing much easier than if we had attempted fully blind testing of the application by routing requests through the proxy.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20456'%3E%3C/svg%3E)

_Figure 8: We observed that requests sent to the broker service containing both a Content-Length and a Transfer-Encoding header resulted in a 400 bad request message being generated by the broker service._

Next, we performed testing against the repository service and, at first, it seemed to leverage the Content-Length to process the request headers instead of the Transfer-Encoding header. Figure 9 shows the initial single response we received to our smuggled request attempt.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20540'%3E%3C/svg%3E)

_Figure 9: We observed that requests to the repository service appeared to only process the first request while ignoring the second request we sent to the application._

We also attempted to trigger the parsing of multiple messages within a single request within the repository service by triggering various POST handlers within the REST API. We hypothesized here that the application potentially wasn’t consuming the body of GET requests we sent.

We first attempted to trigger the issue by invoking an endpoint which expected JSON data within the body of the POST request. This failed since the application returned a 500 internal server error and closed the connection without processing any further messages (see Figure 10). However, after we switched to targeting an endpoint which didn’t expect any parameters within the body of the POST request we were able to successfully trigger the issue and received multiple responses back from the repository service as shown in Figure 11.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20570'%3E%3C/svg%3E)

_Figure 10: We attempted to trigger the request tunneling on the repository service by leveraging a POST request handler and this failed as we didn’t specify the appropriate parameters in the request body._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20766'%3E%3C/svg%3E)

_Figure 11: We successfully triggered the processing of multiple requests within the same message by targeting the /qrs/internal/management/apilogcontext/disable endpoint which didn’t expect any parameters within the body of the POST request._

## Developing an Initial Exploit

After confirming the existence of the request tunneling issue we developed an initial proof of concept exploit that added a new administrative user account to the Qlik Sense application. We sent the request in Figure 12 to the application and succeeded in creating a new administrative user account named praetorian on the system.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20635'%3E%3C/svg%3E)

_Figure 12: An example diagram showing how the proxy views the boundary between requests (red) versus how the repository service views the boundary between requests (blue)._

### Identifying a Primitive for Code Execution

At this point, we had the ability to impersonate a privileged service account giving us full access to invoke any APIs the repository service exposed. We performed a review of the REST APIs exposed through the repository service and [identified the /qrs/externalprogramtask endpoint](https://community.qlik.com/t5/Official-Support-Articles/How-to-create-an-external-program-task-in-Qlik-Sense-with-a/ta-p/1713044), which allowed for execution of arbitrary commands with arbitrary arguments as shown in Figure 13 and Figure 14.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20449'%3E%3C/svg%3E)

_Figure 13: After reviewing the documentation for the repository service API we observed there was a REST endpoint which could be leveraged to execute arbitrary commands by creating an external program task._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20253'%3E%3C/svg%3E)

_Figure 14: We also observed functionality existed in the frontend interface to create external program tasks within the management console._

### Leveraging Request Tunneling for Command Execution

We then developed a proof of concept request that would trigger the creation of an external program task using the request tunneling issue to impersonate the internal sa_repository service account user, as Figure 15 shows. Figure 16 shows that the request successfully created the task, and Figure 17 shows the resulting evil.txt file in the Windows temp directory.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20657'%3E%3C/svg%3E)

_Figure 15: An example request smuggled to the repository service used to impersonate the sa_repository service account and create an external program task to execute attacker-controlled commands._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20284'%3E%3C/svg%3E)

_Figure 16: The request smuggling issue was leveraged to create an external program task named “Evil Task” which created a file named evil.txt in the Windows temp directory._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20431'%3E%3C/svg%3E)

_Figure 17: We observed that the queued external program task was executed successfully resulting in the creation of a file named evil.txt in the Windows temp directory._

### Achieving Unauthenticated Request Tunneling

At this point we had the ability to obtain administrative privileges within the Qlik Sense application under a default installation if we had a valid session within the application. However, we were unable to invoke the /qrs/internal/management/apilogcontext/disable endpoint without a valid session cookie, Figure 18 and Figure 19 show. We needed an authentication bypass to exploit the request tunneling vulnerability as a fully unauthenticated attacker without a valid session token.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20207'%3E%3C/svg%3E)

_Figure 18: We attempted to invoke the /qrs/internal/management/apilogcontext/disable endpoint without a valid session cookie._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20328'%3E%3C/svg%3E)

_Figure 19: We received a 403 forbidden response when attempting to exploit the /qrs/internal/management/apilogcontext/disable endpoint without a valid session._

After performing some additional research we identified a method to bypass the authentication requirements imposed by the proxy service and invoke the /qrs/internal/management/apilogcontext/disable endpoint within the repository service. Through trial and error we determined that the proxy would allow through any request beginning in “/resources/qmc/fonts/” and ending in “.ttf”. Figure 20 shows the request we used to bypass authentication requirements enforced by the proxy. Figure 21 shows the response from the backend indicating successful routing of the request to the targeted REST endpoint.

We also observed that the proxy service didn’t appear to normalize paths within requests before analyzing them and forwarding them to backend services. This meant that we could provide the proxy with a path that began and ended with the expected path for loading a font, but that on the backend resolved to an internal REST endpoint we wished to invoke to trigger the request smuggling issue.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20644%20485'%3E%3C/svg%3E)

_Figure 20: We observed that attempts to load fonts from the repository service were allowed without a valid session cookie._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20641%20293'%3E%3C/svg%3E)

_Figure 21: The response received from the server in response to the request sent in Figure 20 indicated that we successfully accessed the repository service while bypassing the normal authentication requirements._

## Automating the Exploitation Process

We then automated the exploitation process and developed a utility named zeroqlik with which an attacker can compromise a target system running Qlik Sense. The utility uses the request tunneling and path traversal vulnerabilities. The video below demonstrates the zeroqlik utility facilitating remote code execution:

<https://www.praetorian.com/wp-content/uploads/2024/07/ZeroQlik-POC-Video.mp4>

## Verifying Remediation Using Nuclei

We created a Nuclei template to check for vulnerable versions of Qlik Sense Enterprise. The template works by attempting to trigger the CVE-2023-41266 authentication bypass vulnerability. However, because one security update fixes both CVE-2023-41265 and CVE-2023-41266, we don’t need to check for the presence of CVE-2023-41265 if we can confirm the existence of CVE-2023-41266. We have published this template to the [praetorian-inc/zeroqlik-detect repository.](https://github.com/praetorian-inc/zeroqlik-detect) We have also [submitted a pull request to ProjectDiscovery](https://github.com/projectdiscovery/nuclei-templates/pull/8125?) to integrate this template into the nuclei-templates repository.

Operators can use the following command to test an instance of Qlik Sense Enterprise for the vulnerability. Operators also can provide a list of hosts, rather than a single host, to Nuclei to test multiple potentially impacted Qlik Sense Enterprise instances. Figure 22 shows an example output from the Nuclei utility when the instance is vulnerable and Figure 23 shows an example output from Nuclei when the instance is not vulnerable
  
  
  echo https://ip:443/ | nuclei -t <path-to-template>/zeroqlik-vulnerability.yaml

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20226'%3E%3C/svg%3E)

_Figure 22: An example output from the Nuclei scanner when the targeted instance is vulnerable to CVE-2023-41265 and CVE-2023-41266._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20267'%3E%3C/svg%3E)

_Figure 23: An example output from the Nuclei scanner when the targeted instance is not vulnerable to CVE-2023-41265 and CVE-2023-41266._

## Verifying Remediation Using Curl

Users can check for the existence of CVE-2023-41265 and CVE-2023-41266 with the following simple curl command.
  
  
  curl -H "X-Qlik-Xrfkey: 1333333333333337" -H "Host: localhost" -v -k --path-as-is https://ip/resources/qmc/fonts/../../../qrs/ReloadTask?xrfkey=1333333333333337&filter=.ttf

Figure 24 shows the expected response when an instance is vulnerable. The system will return an HTTP 400 response code with a message in the response body indicating that the filter provided to the /qrs/ReloadTask endpoint is invalid (“The comparison expression does not consist of three elements: .ttf”). Figure 25 shows the expected response from a patched instance of the application where the system returns an HTTP 302 redirect to an authentication page.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20553'%3E%3C/svg%3E)

_Figure 24: The expected response received from an unpatched instance of Qlik Sense Enterprise._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20644%20481'%3E%3C/svg%3E)

_Figure 25: The expected response received from a properly patched instance of Qlik Sense Enterprise._

## A Note on Load Balancers

In some cases, load balancers or other systems sitting in front of the Qlik Sense instance could hinder an attacker from performing HTTP request tunneling using CVE-2023-41265. These load balancers forward requests properly using the Transfer-Encoding header first and thus would break the specially formatted request sent to the proxy to trigger the request tunneling issue. In our lab environment, we configured an example vulnerable instance of Qlik Sense behind an Amazon Elastic Load Balancer (ELB). Our remote code execution exploit failed due to the load balancer breaking the HTTP request tunneling payload. We don’t recommend that organizations leverage this behavior instead of patching CVE-2023-41265. We only wanted to make note of this as it can, in some cases, explain why the exploit isn’t working correctly against a system that otherwise appears vulnerable.

Our testing in our lab environment indicated that the HTTP request tunneling payload we leveraged in this article did not work properly when the vulnerable instance was behind an Elastic Load Balancer (ELB) in AWS. However, we still were able to exploit CVE-2023-41266 as the presence of a load balancer would not impact the path traversal issue we mentioned previously. An attacker could potentially modify the payload to successfully exploit CVE-2023-41265 in instances where Qlik Sense resides behind an Elastic Load Balancer. The core point in this case is simply that load balancers and other devices that process requests and route requests before hitting the vulnerable Qlik Sense Enterprise instance could complicate exploitation of the vulnerability.

## Potential Indicators of Compromise

Organizations can leverage two particularly useful indicators of compromise e to detect exploitation. The first is the proxy audit logs which could include evidence of the path traversal exploit for CVE-2023-41266. The second is a review of the processes spawned by the Scheduler service which we leveraged previously in our exploit to execute arbitrary commands using external program tasks.

### Proxy Audit Logs

The proxy writes audit access logs to the C:ProgramDataQlikSenseLogProxyAudit directory. The local file is an audit log of the format $HOSTNAME_AuditSecurity_Proxy (e.g. IP-AC1FB18B_AuditSecurity_Proxy). Following is an example entry from an exploitation attempt. We observe here that the user is authenticated as anonymous and that the path begins with /resources/ and ends in .ttf, .woff, .otf, or .eot with a ../../../ directory traversal sequence being leveraged within the request path. [1]
  
  
  /resources/qmc/fonts/../../../qrs/reloadtask?xrfkey=1333333333333337&filter=.ttf Login 0 User authenticated. User 'NONEanonymousfdcd2a6f-5b78-46db-8a8a-d8ad5b550530' used authentication method 'anonymous'

### Scheduler Service-Spawned Processes

Organizations also might find reviewing processes spawned by Scheduler.exe to be useful in helping identify suspicious processes that may be associated with exploitation. An attacker is likely to leverage the external program task functionality during the course of an exploit to execute malicious code as we showed previously. When a user executes an external program task the Scheduler.exe service (i.e. C:Program FilesQlikSenseSchedulerscheduler.exe) is responsible for launching the target process. In Figure 26 we have an example where Scheduler.exe created a malicious external program task as a result of us exploiting CVE-2023-41265 and CVE-2023-41266.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20105'%3E%3C/svg%3E)

_Figure 26: An example where an attacker created an external program task to run a PowerShell one-liner on the impacted system._

In our example exploit we leverage an external program task to run a PowerShell one-liner that reaches out to a remote server. We observe that Scheduler.exe spawns a malicious PowerShell process which then executes a one-liner to execute a malicious payload on the system. Figure 27 and Figure 28 show additional details associated with the spawning of a malicious external program task. We recommend that impacted organizations concerned about exploitation of this issue review historical data process execution logs associated with Scheduler.exe to identify potential malicious external program tasks.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20239'%3E%3C/svg%3E)

_Figure 27: The full path of the Scheduler.exe service from the event observed previously in ProcMon._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20651%20243'%3E%3C/svg%3E)

_Figure 28: An example PowerShell one-liner executed using an external program task._

## Qlik Sense NTLM Authentication Endpoints

We also observed during the course of our research that Qlik Sense, by default, will expose an NTLM authentication endpoint at /internal_windows_authentication/?targetId=$GUID, which attackers could use for password spraying or enumeration of information on the target organization’s internal Active Directory domain. We updated our [NTLMRecon](https://github.com/praetorian-inc/NTLMRecon) utility to support discovery of this endpoint and leveraged it to confirm that externally facing Qlik Sense instances we identified were largely domain joined and connected to the internal Active Directory environments of the target organizations.

We also observed that many externally facing instances of Qlik Sense that leveraged single sign-on with an external identity provider by default also still exposed the NTLM authentication endpoint if an attacker browsed directly to the /internal_windows_authentication/?targetId=$GUID path. While this isn’t a security vulnerability itself, some organizations are likely to assume that multi-factor authentication protects their externally facing Qlik Sense instance while in actuality an attacker could bypass the MFA by directory browsing to the NTLM authentication endpoint in the default setting. While this is not directly relevant to the vulnerability, it represents an interesting piece of related attack surface that a red team could target during an engagement.

## Conclusion

Praetorian performs proactive vulnerability research to identify vulnerabilities in commonly used software applications. As part of our research into Qlik Sense Enterprise we identified two vulnerabilities which when combined lead to unauthenticated remote code execution.

The best defense is a proactive one. Understanding your attack surface better and taking proactive steps to reduce exposures and better assess the impact of new vulnerabilities is a critical step of this process. If you’d like to know how the Chariot offensive security platform can help you stay one step ahead of attackers, please don’t hesitate to [contact us](https://www.praetorian.com/chariot-registration/) for a demo.

[1] With thanks to Michael McKinley and Tony Latteri at Raymond James for their observations on the file extensions this vulnerability affects.

## About the Authors

![Adam Crosser](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Adam Crosser](https://www.praetorian.com/author/adam-crosser/)

Adam is an operator on the red team at Praetorian. He is currently focused on conducting red team operations and capabilities development.

[ ](https://www.linkedin.com/in/adam-crosser-366263265)

## Catch the Latest

Catch our latest exploits, news, articles, and events.

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 19, 2026

[](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

## [GhostPack Necromancy: Reforging C# Tools with WasmForge](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[ Read More ](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/)

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

  * [Offensive Security](https://www.praetorian.com/category/offensive-security/), [Vulnerability Research](https://www.praetorian.com/category/vulnerability-research/)

  * June 17, 2026

[](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

## [FreeBSoD: Leveraging Language Models to Find and Exploit Kernel Bugs (Part 1 of 2)](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[ Read More ](https://www.praetorian.com/blog/ai-vulnerability-research-freebsd-kernel/)

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

  * [Uncategorized](https://www.praetorian.com/category/uncategorized/)

  * June 16, 2026

[](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## [Sharing is Caring: SMB Secret Scanning with Sulla](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

[ Read More ](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/)

## Ready to Discuss Your Next Continuous Threat Exposure Management Initiative?

Praetorian’s Offense Security Experts are Ready to Answer Your Questions

[ Get Started ](/contact-us/)

[ ![Praetorian](https://www.praetorian.com/wp-content/uploads/2025/10/praetorian-logo-final-white.svg) ](https://www.praetorian.com)

##### [Praetorian Guard Platform](https://www.praetorian.com/guard)

  * [ Continuous Threat Exposure Management ](https://www.praetorian.com/guard/continuous-threat-exposure-management/)
  * [ Attack Surface Management ](https://www.praetorian.com/guard/attack-surface-management/)
  * [ Vulnerability Management ](/chariot/vulnerability-management/)
  * [ Cyber Threat Intelligence ](/chariot/threat-intelligence/)
  * [ Continuous Penetration Testing ](https://www.praetorian.com/guard/continuous-penetration-testing/)
  * [ Breach and Attack Simulation ](https://www.praetorian.com/guard/breach-attack-simulation/)

##### Professional Services

  * [ AI/ML Penetration Testing ](https://www.praetorian.com/services/ai-ml-penetration-testing/)
  * [ Application Penetration Testing ](/services/application-penetration-testing/)
  * [ Assumed Breached Exercise ](/services/assumed-breached-exercise/)
  * [ Attack Path Mapping ](https://www.praetorian.com/resources/attack-path-mapping/)
  * [ Automotive Penetration Testing ](/services/automotive-penetration-testing/#)
  * [ CI/CD Security Engagement ](/services/ci-cd-security-engagement/)
  * [ Cloud Penetration Testing ](/services/cloud-penetration-testing/)
  * [ IoT Penetration Testing ](/services/iot-penetration-testing/)
  * [ Network Penetration Testing ](/services/network-penetration-testing/)
  * [ NIST CSF Benchmark ](/services/nist-csf-benchmark/)
  * [ Purple Team ](/services/purple-team/)
  * [ Red Team ](/services/red-team/)

##### Use Cases

  * [ Bug Bounty Cost Reduction ](/services/bug-bounty-cost-reduction/)
  * [ FDA Testing and Monitoring ](/services/fda-testing-monitoring/)
  * [ Mergers and Acquisitions ](/services/mergers-acquisitions/)
  * [ Ransomware Prevention ](/services/ransomware-prevention/)
  * [ Rogue IT Identification ](/services/rogue-it-identification/)
  * [ Tool and Vendor Consolidation ](/services/tool-vendor-consolidation/)
  * [ Vendor Risk Management ](https://www.praetorian.com/services/vendor-risk-management/)

##### Company

  * [ About Us ](https://www.praetorian.com/about-us/)
  * [ Leadership Team ](https://www.praetorian.com/leadership-team/)
  * [ Press Releases ](/news/press-release/)
  * [ In the News ](/news/news)
  * [ Contact Us ](https://www.praetorian.com/contact-us/)
  * [ Resource Library ](https://www.praetorian.com/resources/)
  * [ Security Blog ](/blog/)
  * [ People Ops Blog ](/people-ops/)
  * [ Careers ](https://www.praetorian.com/careers/)
  * [ Culture ](https://www.praetorian.com/work-at-praetorian/)
  * [ Survival Kit ](/wp-content/uploads/2024/11/Praetorian-Survival-Guide.pdf)

### Subscribe to our Newsletter

Catch our latest exploits, news, articles, and events.

[Privacy Policy](/privacy-policy/) | [Responsible Disclosure Policy](/responsible-disclosure-policy/) | [Terms of Service](/terms-of-service/) | [Terms and Conditions](/terms/)

Copyright © 2025. All Rights Reserved.

[ Linkedin-in ](https://www.linkedin.com/company/praetorian/) [ X-twitter ](https://twitter.com/praetorianlabs) [ Facebook-f ](https://www.facebook.com/praetorianlabs) [ Github ](https://github.com/praetorian-inc) [ Youtube ](https://www.youtube.com/user/PraetorianLabs)
