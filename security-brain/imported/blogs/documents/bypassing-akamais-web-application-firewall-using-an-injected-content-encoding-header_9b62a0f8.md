---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-21_bypassing-akamais-web-application-firewall-using-an-injected-content-encoding-he.md
original_filename: 2023-02-21_bypassing-akamais-web-application-firewall-using-an-injected-content-encoding-he.md
title: Bypassing Akamai’s Web Application Firewall Using an Injected Content-Encoding
  Header
category: documents
detected_topics:
- xss
- sso
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- sso
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 9b62a0f898c660c2b409ee65e8547a54140e0a4eeaa239df3bc23bca5fbdc7e5
text_sha256: 390a9afcb2a1cbc7ad881026d40c37a56c9ebfa560d22ecbf9cf8a1a1a58ebe6
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Akamai’s Web Application Firewall Using an Injected Content-Encoding Header

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-21_bypassing-akamais-web-application-firewall-using-an-injected-content-encoding-he.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `9b62a0f898c660c2b409ee65e8547a54140e0a4eeaa239df3bc23bca5fbdc7e5`
- Text SHA256: `390a9afcb2a1cbc7ad881026d40c37a56c9ebfa560d22ecbf9cf8a1a1a58ebe6`


## Content

---
title: "Bypassing Akamai’s Web Application Firewall Using an Injected Content-Encoding Header"
page_title: "Bypassing Akamai's Web Application Firewall Using an Injected Content-Encoding Header | Praetorian"
url: "https://www.praetorian.com/blog/using-crlf-injection-to-bypass-akamai-web-app-firewall/"
final_url: "https://www.praetorian.com/blog/using-crlf-injection-to-bypass-akamai-web-app-firewall/"
authors: ["Adam Crosser"]
programs: ["Akamai"]
bugs: ["WAF bypass", "CRLF injection", "XSS"]
publication_date: "2023-02-21"
added_date: "2023-02-22"
source: "pentester.land/writeups.json"
original_index: 1506
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

  * [Labs](https://www.praetorian.com/category/labs/)

# Bypassing Akamai’s Web Application Firewall Using an Injected Content-Encoding Header

  * [Adam Crosser](https://www.praetorian.com/author/adam-crosser/)
  * [ February 21, 2023 ](https://www.praetorian.com/blog/2023/02/21/)

![](https://www.praetorian.com/wp-content/uploads/2024/06/Akamai1.png)

During a recent Chariot customer pilot we identified an interesting method to bypass the cross-site scripting (XSS) filtering functionality within the Akamai Web Application Firewall (WAF) solution. Chariot had identified a Carriage Return and Line Feed (CRLF) injection vulnerability during an automated scan, and we discovered the bypass during our exploitation phase. In this article, our goals are to explain some of the risks associated with CRLF injection as well as discuss the technique we leveraged to bypass the Akamai WAF filtering.

### Before We Get Started…

Please note that while we use example.com as the vulnerable application within this article, the site itself wasn’t actually vulnerable to CRLF injection. Instead, we have substituted example.com for the customer domain and redacted other potentially identifying information. This allows us to include details on technique without exposing any information that could be linked to the customer network environments. In some cases, we provide simulated screenshots to show what we would have observed when performing the attack, and have manually recreated the scenario using example.com to avoid exposing sensitive information.

We also do not intend for this article to single out Akamai in particular. Rather, we suspect that attackers could use similar bypass techniques against just about every web application firewall product on the market.

## What is a CRLF injection vulnerability?

First, let’s discuss a bit more about [ what a CRLF injection vulnerability is](https://www.invicti.com/blog/web-security/crlf-http-header/) and why it could be useful to an attacker. CRLF injection occurs when an application does not perform proper filtering and returns an HTTP response header that includes attacker-controlled user-input. This type of vulnerability allows an attacker to insert carriage return (abbreviated CR and often represented as ‘r’) and line feed (abbreviated LF and often represented as ‘n’) characters into the HTTP response body.

Figure 1 shows an example HTTP response in which the CRLF (‘rn’) character sequence both separates the HTTP headers and delineates between the HTTP headers and response body. In this case, we observe that the separator between the HTTP headers and body is simply a single line containing only the CRLF sequence.

![](https://www.praetorian.com/wp-content/uploads/2024/06/Akamai1.png)

_Figure 1: An example HTTP response from example.com that uses a CRLF sequence delineated between HTTP headers and the response body._

This HTTP protocol means that an attacker who can inject CRLF characters into the HTTP response body can in many cases end up controlling both HTTP headers and data within the HTTP response body. This issue can then lead to other vulnerabilities such as cross-site scripting and open redirection vulnerabilities. Additionally, other attack vectors can become viable, such as [ session fixation attacks](https://www.invicti.com/learn/session-fixation/) if the attacker can inject a Set-Cookie header within a HTTP response the victim system returns.

One of the most common root-causes of CRLF injection is when an HTTP header within a server’s response body reflects attacker-controlled input from an URL in a HTTP request.

## What did Chariot discover?

In this case, Chariot performed testing for CRLF injection vulnerabilities using the Nuclei scanning utility. Figure 2 shows an example request in the finding Chariot generated.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20914%20536'%3E%3C/svg%3E)

_Figure 2: An example CRLF injection vulnerability Chariot discovered automatically. Praetorian engineers manually adjusted the risk rating from low-risk to high-risk._

In this case, we observe that a HTTP request was sent to the victim server example.com running a HTTPS server on port 443/TCP. At this point, our managed services team performed manual verification of the issue before escalating to the customer.

We began by confirming the existence of the CRLF injection vulnerability. We used the URL [ https://example.com/%0ASet-Cookie:test=test](https://example.com/%0ASet-Cookie:test=test) to trigger the CRLF injection vulnerability. We included a %0A character to represent a newline character that reflects in the HTTP response the client received. It allowed us to inject a Set-Cookie header into the HTTP response, as Figure 3 shows. The “vulnerable header” field reflects the attacker-controlled user input.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20917%20373'%3E%3C/svg%3E)

_Figure 3: An example where CRLF injection allows us to inject a Set-Cookie header into the HTTP response body._

We observe two things of particular note from this response. The first is that the injected Set-Cookie header is not located directly after the vulnerable header despite our expectation that it would be after we injected a new-line after the vulnerable header. The second observation is that while we injected only a newline character (‘n’) after the vulnerable-header header, the response clearly contained a ‘rn’ character sequence (both a carriage return and line feed) after the vulnerable-header header.

Ultimately, this gets into the complex nature of modern web applications where an application must route multiple levels of requests. For example, imagine a scenario where we deploy a service within Kubernetes using Istio as a service mesh, exposed externally through a cloud-based load balancer, hosted behind an external web application firewall service, served through a content delivery network such as Akamai. In such a scenario, an external request made by a client could take the following path to hit an internal application or service running in Kubernetes:

  1. From client browser to [ https://example.com/](https://example.com/)
  2. Through content delivery network
  3. Web application firewall examination
  4. To external load balancer
  5. To internal Kubernetes load balancer
  6. To Istio sidecar running on pod in Kubernetes cluster
  7. Ending at the application service running on the Kubernetes pod

Each step presents an opportunity for an intermediary system to transform the ultimate HTTP response, which explains why headers can be reordered. Many systems also include flexible parsing logic to make them capable of handling responses that differ slightly from the RFC, so an intermediate system’s formal parsing also could transform the “n” injection to the “rn” injection we see in the example.

A reader might wonder why we didn’t include ‘rn’ so that our payload is compliant with the specification. Figure 4 demonstrates that the Akamai WAF actually blocks the ‘rn’ sequence when specified in a URL (in this case the URL encoded version of ‘rn’ is ‘%0d%0a’). Simply specifying ‘n’ bypasses the filter.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20913%20429'%3E%3C/svg%3E)

_Figure 4: Chariot automatically bypassed the Akamai WAF when testing for CRLF injection by specifying both ‘n’ and ‘rn’ as potential CRLF injection payloads. This allowed Chariot to bypass Akamai’s rule to detect testing for CRLF injection issues._

## An Initial Exploitation Attempt

After verifying the presence of the CRLF injection issue we attempted to exploit the vulnerability in a naive way by simply injecting the standard <script>alert(“XSS”)</script> payload into the response body. However, the Akamai WAF blocked this attempt based on the script payload tag within the GET parameter sent to the server. Figure 5 shows the response we received from Akamai as a result.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20913%20560'%3E%3C/svg%3E)

_Figure 5: An example response received from the Akamai WAF solution when we attempted to trigger a cross-site scripting issue using CRLF injection._

At this point we attempted several different common cross-site scripting payloads using standard Akamai WAF bypass techniques. We largely focused on modifying the cross-site scripting payload injected into the HTTP response body. This is the standard approach for attempting to bypass a WAF when exploiting a reflected cross-site scripting vulnerability.

## Researching the Content-Encoding Header

One simple option to bypass the web application firewall would be to continually modify our cross-site scripting payload until it bypasses the firewall’s signatures. However, we decided instead to bypass the WAF using the header injection primitive the CRLF injection vulnerability provided.

We hypothesized that we could inject a header using CRLF injection to specify that the HTTP response body was compressed. Next, we would compress the HTTP response payload injected into the response body. In this case, we didn’t need to modify the core XSS payload as we are simply relying on the compression to bypass the WAF rules used to inspect the GET malicious parameters specified in the request the application sends.

Our research indicated that the Content-Encoding header supported several different compression algorithms such as the gzip, compress, deflate, and br algorithms (see Figure 6 and Figure 7 [1]).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20909%20318'%3E%3C/svg%3E)

_Figure 6: An initial review of the Mozilla HTTP documentation revealed four different supported compression algorithms._

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20906%20634'%3E%3C/svg%3E)

_Figure 7: A section from the Mozilla documentation describing the four compression algorithms listed in Figure 6._

## Bypassing WAF Filtering Using Response Compression

Somewhat arbitrarily, we picked the deflate algorithm and injected a Content-Encoding header specifying it. We then injected a malicious compressed cross-site scripting payload that decompressed to <script>alert(“XSS”)</script> as shown in Figure 8.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20903%20641'%3E%3C/svg%3E)

_Figure 8: A HTTP response containing compressed data and residual header data from the split HTTP response._

Unfortunately, we can see that, while our compressed data is present, the response body also contains some headers from the modified request since we injected a new header and response body into an existing HTTP request. This is because we essentially specified that everything past a specific injection point should be considered as part of the HTTP request body, which included any headers that came after the injection point. Fortunately, the simple solution to this is to inject a malicious Content-Length header with which we can specify that only the compressed data should be interpreted as being part of the request body.

### Adding a Content-Length Header to the Payload

In this case, the compressed version of our cross-site scripting payload is twenty-six bytes, so we injected a Content-Length header specifying a length of twenty-six bytes. This means that everything coming after our compressed data is ignored, including the headers mentioned previously. Thus, the response body can be properly decompressed and rendered. Figure 9 shows the updated payload with the injected headers now including a Content-Length header and the compressed data in the response body.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20885%20404'%3E%3C/svg%3E)

_Figure 9: An updated payload including a Content-Length header so only the compressed data containing the XSS payload is considered to be part of the response body._

Figure 10 shows an example of what the executed payload would have looked like when triggered while targeting the victim system. Please note that example.com is simply being used as a placeholder for the targeted application so as to avoid including information on the client domain.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20886%20490'%3E%3C/svg%3E)

_Figure 10: An example screenshot showing what would have been observed on the targeted site. Please note example.com wasn’t impacted by a CRLF injection issue; this is just an example screenshot showing what execution of the payload looked like._

## How is this different from a traditional bypass technique?

You may be wondering how the technique we leverage in this article is different from other previously published bypass techniques that aim to bypass the cross-site scripting (XSS) functionality within the Akamai WAF.

Ordinarily, we wouldn’t write about a web application firewall bypass if it just used a standard bypass technique. However, the combination of chaining a CRLF injection issue to trigger cross-site scripting and bypassing a web application firewall by injecting compressed data into the response body is a novel approach. We are not aware of another article that discusses this method.

## Conclusion

In this article, we discussed the basic theory behind CRLF injection vulnerabilities and then moved into discussing web application firewall bypass techniques we leveraged during a customer pilot to demonstrate the risk of CRLF injection by leveraging these issues to perform cross-site scripting.

## References

[1] [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding)

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
