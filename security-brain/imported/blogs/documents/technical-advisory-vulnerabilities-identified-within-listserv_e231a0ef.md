---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-18_technical-advisory-vulnerabilities-identified-within-listserv.md
original_filename: 2023-10-18_technical-advisory-vulnerabilities-identified-within-listserv.md
title: 'Technical Advisory: Vulnerabilities Identified within ListServ'
category: documents
detected_topics:
- xss
- csrf
- command-injection
- supply-chain
- sso
- idor
tags:
- imported
- documents
- xss
- csrf
- command-injection
- supply-chain
- sso
- idor
language: en
raw_sha256: e231a0ef6b284f9f6ae9841d2e769f0f567be9114551a18519a0eb73d9797c50
text_sha256: f85c12f0101154b83a18e535c60e00ef713ad550166261a68a29ee62467b0118
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Technical Advisory: Vulnerabilities Identified within ListServ

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-18_technical-advisory-vulnerabilities-identified-within-listserv.md
- Source Type: markdown
- Detected Topics: xss, csrf, command-injection, supply-chain, sso, idor
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `e231a0ef6b284f9f6ae9841d2e769f0f567be9114551a18519a0eb73d9797c50`
- Text SHA256: `f85c12f0101154b83a18e535c60e00ef713ad550166261a68a29ee62467b0118`


## Content

---
title: "Technical Advisory: Vulnerabilities Identified within ListServ"
page_title: "Technical Advisory: Vulnerabilities Identified within ListServ | Praetorian"
url: "https://www.praetorian.com/blog/vulnerabilities-within-listserv/"
final_url: "https://www.praetorian.com/blog/vulnerabilities-within-listserv/"
authors: ["Adam Crosser"]
programs: ["ListServ"]
bugs: ["CSRF", "Samesite cookie bypass", "Reflected XSS", "Stored XSS", "Unrestricted file upload", "DLL Hijacking", "Local Privilege Escalation", "Buffer Overflow", "Memory corruption"]
publication_date: "2023-10-18"
added_date: "2024-01-02"
source: "pentester.land/writeups.json"
original_index: 709
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

# Technical Advisory: Vulnerabilities Identified within ListServ

  * [Adam Crosser](https://www.praetorian.com/author/adam-crosser/)
  * [ October 18, 2023 ](https://www.praetorian.com/blog/2023/10/18/)

![](https://www.praetorian.com/wp-content/uploads/2024/06/Vulnerability-Research-at-Praetorian-Labs.png)

## Overview

In an effort to safeguard our customers, we perform proactive vulnerability research with the goal of identifying zero-day vulnerabilities that are likely to impact the security of leading organizations. Our ultimate goal when performing our research is to identify unauthenticated remote code execution vulnerabilities which could be reliably exploited across a wide variety of targets without any user-interaction required within the exploit chain (this generally rules out cross-site scripting and cross-site request forgery vulnerabilities). In this article, we discuss our findings from reviewing ListServ, an email mailing list management application. Unfortunately, in this case, ListServ was unresponsive to the security issues we reported to them. At this point, the 90 day disclosure timeline has passed so we have decided to publish the technical details of these vulnerabilities. There are currently no patches available for these security issues. 

### Why target the ListServ application?

We decided to focus on the ListServ application because one of our Chariot customers uses it along with a variety of government agencies, universities, and non-government research institutions that may be the target of certain advanced threat actors. We also observed that, while previous researchers had discovered some stack-based buffer overflow issues [in ListServ in the early 2000s](https://www.cvedetails.com/vulnerability-list/vendor_id-69/product_id-109/Lsoft-Listserv.html), few new vulnerabilities had been reported in the application. Few recent CVEs combined with the relatively old technology stack associated with the application made it a potentially interesting target for remote code execution vulnerabilities. 

### Summary of Vulnerabilities Identified

We identified several vulnerabilities that an attacker could exploit to compromise privileged administrative accounts and achieve remote code execution. They involve chaining cross-site scripting and CSRF vulnerabilities with a stack-based buffer overflow vulnerability within an administrative component of the ListServ application. An attacker could then combine these with a stack-based buffer overflow vulnerability in an administrative component of the ListServ application to achieve remote code execution. The diagram in Figure 1 shows an attack chain diagram representing the vulnerabilities we identified and how an attacker could chain them together for remote code execution.  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20723%201043'%3E%3C/svg%3E) _Figure 1: An attack chain diagram showing how multiple vulnerabilities in the ListServ application could be chained together to achieve remote code execution or local privilege escalation._

## Exploring ListServ Application Architecture

ListServ is an interesting application in that it has essentially grown up with the modern internet. The first version of ListServ was released in 1986 ([for context the first web browser wasn’t released until 1990](https://www.mozilla.org/en-US/firefox/browsers/browser-history/)). As a result, ListServ exposes both a web interface alongside its original email-based management interface. A review of externally facing ListServ applications revealed that the application is primarily leveraged by government agencies, universities, and research institutions. The application offers several options for administration, including the ability to manage the application over SMB named pipes, through an email-based interface, and through a web interface. The web interface consists of a CGI application binary (WA.exe) that runs a component which communicates with a backend process called LSV.exe. The communication between WA.exe and LSV.exe uses a command-based language that end-users can also leverage via email to perform actions within the application. The LSV service listens on a localhost TCP port that the WA process connects to in order to send commands using the LSV service. Ultimately, a large portion of the application’s logic is implemented within the LSV service with the WA application simply translating actions sent by the user’s web browser to commands that are then executed by the LSV service. During our initial inspection of the ListServ application’s architecture we identified several interesting items which spiked our attention. The first was, as shown in Figure 2, noticing that the core backend components of the application (such as LSV.exe) all ran as the NT AUTHORITYSYSTEM user account. Additionally, we observed an SMB-based mechanism that we could leverage to manage the application using the same command-based language as the email-based management component (see Figure 3).  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20709%20286'%3E%3C/svg%3E) _Figure 2: A process tree showing the LSV.exe executable running as NT AUTHORITYSYSTEM and several sub-processes used when multiple SMTP servers are configured for sending outgoing messages._ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20715%20255'%3E%3C/svg%3E) _Figure 3: We observed some interesting functionality exposed by the ListServ application which allowed for the application to be managed over SMB named pipes. We thought this might be an interesting potential attack surface for vulnerabilities._ We also observed that common exploit mitigations associated with core application components such as WA.exe and LSV.exe were disabled, including ASLR, SafeSEH, and Control Flow Guard, asFigure 4 shows. This in particular piqued our interest in researching potential memory corruption vulnerabilities present within the application. _ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20709%20383'%3E%3C/svg%3E) _ _Figure 4: An initial inspection of the core application binaries lsv.exe and wa.exe indicated that exploit mitigations such as ASLR, SafeSEH, and Control Flow Guard were not enabled on the core application binaries._ After performing an initial enumeration of the application’s architecture and the available attack surface, we began reverse engineering the wa.exe component, a CGI binary written in C which the developers used to implement the web application component of ListServ. 

### Local Privilege Escalation via DLL Hijacking

During the initial installation of the ListServ application we observed that the installation directory defaulted to C:LISTSERV .We knew from previous experience with [exploiting writable system path vulnerabilities for privilege escalation](https://praetstaging.wpengine.com/blog/red-team-local-privilege-escalation-writable-system-path-privilege-escalation-part-1/) that this was likely to result in local privilege escalation due to an inherited DACL applied to folders created directory under the C: drive. Figure 5 shows an image of the ListServ installer with the default path set to C:LISTSERV.  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20681%20490'%3E%3C/svg%3E) _Figure 5: The installer for the ListServ indicating the default path of C:LISTSERV used for the installation of the application._ We confirmed that the C:LISTSERV folder inherited the weak DACL upon installation, which made the entire LISTSERV installation directory writable by unprivileged users (see Figure 6 and Figure 7). ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20444'%3E%3C/svg%3E) _Figure 6: Praetorian examined the inherited DACLs applied to the C:LISTSERV directory from the DACLs inherited from the C: directory._ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20747%20463'%3E%3C/svg%3E) _Figure 7: Praetorian examined a DACL inherited from the C: directory specifying that a user could create files and folders within the C:LISTSERV directory and inherited subdirectories._ We observed that the LSV.exe service would attempt to load dbghelp.dll from its current working directory of C:LISTSERVMAIN upon startup. To exploit this vulnerability we created a malicious DLL (shown in Figure 8) that includes exports that LSV.exe expected when loading dbghelp.dll.  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20439'%3E%3C/svg%3E) _Figure 8: An example proof of concept payload that we could leverage to perform privilege escalation by adding a new user named attacker with local administrator privileges._ Next, we copied the malicious payload to C:LISTSERVMAINdbghelp.dll (see Figure 9). _ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20679%20337'%3E%3C/svg%3E) _ _Figure 9: We leveraged an unprivileged user account to copy a malicious DLL file into the ListServ installation directory renamed to dbghelp.dll._ Upon a restart of the ListServ application we observed that our malicious version of dbghelp.dll had loaded and a new administrative user named attacker existed on the system, as shown in Figure 10. _ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20415'%3E%3C/svg%3E) _ _Figure 10: We observed that our malicious DLL file was loaded by the LSV.exe process upon startup and a new administrative user account named attacker existed on the system._

### Cookie-Based Reflected Cross-Site Scripting

During the beginning of our reverse engineering process we identified several debugging endpoints which could be leveraged to display session cookies, the application version, and other information such as the query string. We observed that while the application properly encoded the response when printing query string data within the DEBUG-SHOW-QS endpoint, it failed to properly sanitize HTTP cookies displayed when invoking the DEBUG-SHOW-COOKIE endpoint, as shown in Figure 11. ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20379'%3E%3C/svg%3E) _Figure 11: A reflected cross-site scripting vulnerability we identified when enumerating application endpoints accessible by unauthenticated users._ When we are performing vulnerability research, we often find cross-site scripting and other issues we aren’t necessarily looking for. While the issues themselves are not often critical or high risk, we still report them to help improve the overall security posture of the application. A reasonable reaction in this scenario would be to dismiss this vulnerability as being entirely theoretical. However, Chariot had actually previously performed automated fuzzing and identified several reflected cross-site scripting issues in the parent domain that would have made this issue exploitable by a real-world attacker against the particular Chariot customer we identified as running the ListServ application. In this scenario, an attacker with a cross-site scripting vulnerability on example.com could [configure a cookie containing an XSS payload scoped to *.example.com](https://www.thoughtco.com/javascript-by-example-2037272) and then redirect the victim to listserv.example.com/scripts/wa.exe?DEBUG-SHOW-COOKIE to trigger a reflected cross-site scripting vulnerability on listserv.example.com. Figure 12 shows the expected output when invoking the DEBUG-SHOW-COOKIE endpoint.  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20299'%3E%3C/svg%3E) _Figure 12: An example showing the output of the endpoint under normal conditions._ Then, in Figure 13, we can see the cross-site scripting payload execution with a cookie containing a cross-site scripting vulnerability.  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20292'%3E%3C/svg%3E) _Figure 13: An example where leveraging a cookie containing a cross-site scripting payload resulted in a reflected cross-site scripting vulnerability in the ListServ application._

### Cross Site Request Forgery in Admin Components

An analysis of the WA application indicated that upon processing a request the application determined if it received a GET or POST request. It then saved the parameters specified in either the query string or the request body into the same buffer. Figure 14 shows the logic executed within the main function where parameters are written into the same buffer regardless of if they originated from a POST body parameter or a GET query string parameter.  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20694%20280'%3E%3C/svg%3E) _F_ _igure 14: An analysis of the WA CGI binary indicated that the GET query string and POST data were stored within the same data buffer used to process requests sent by end-users._ We also observed that the switchboard function routed user requests to the appropriate functionality within the application. The previously read data buffer containing parameters from the query string or the POST request body is then processed by the switchboard function, as shown in Figure 15. The implication of this behavior is that GET and POST requests become interchangeable so an attacker can substitute what would normally be a POST request with a GET request while placing the parameters in the query string instead of the POST request body.  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20685%20242'%3E%3C/svg%3E) _Figure 15: The switchboard function was invoked by the main function using the data buffer that was previously populated with the query string or POST request body data._ We also analyzed the session cookie we received after logging into the application, and the SameSite value was not configured within the Set-Cookie header. In most cases, modern browsers will apply the Lax security setting to cookies when they are issued without a SameSite value configured. Figure 16 shows the settings applied to the WALOGIN session cookie upon authenticating to the application. We observed that the application does not leverage CSRF tokens to prevent CSRF attacks as shown in Figure 17. _![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20284'%3E%3C/svg%3E)_ _Figure 16: An analysis of the cookie options configured when the user authenticates to the application indicates the SameSite value was not explicitly configured by the application._ _![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20674%20490'%3E%3C/svg%3E)_ _Figure 17: A POST request sent by the user’s browser to reconfigure options within the ListServ administration panel. We observed that there were no CSRF tokens or headers leveraged to prevent CSRF attacks._

##### Methods of Bypassing the SameSite = Lax Security Setting

The combination of the interchangeability of GET and POST requests, the lack of CSRF security tokens, and the same SameSite = Lax setting being applied to session cookies, provides two potential exploitation scenarios: 

  1. Exploitation by Substituting POST with GET Requests: An attacker could exploit the fact that POST and GET requests are interchangeable due to the logic mentioned previously to perform a CSRF attack using GET requests against an endpoint that a POST request normally would invoke. The PortSwigger Web Academy documents this technique in an article titled “Bypassing SameSite Cookie Restrictions” under a subsection titled [Bypassing SameSite Lax Restrictions Using GET Requests](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions#bypassing-samesite-lax-restrictions-using-get-requests). This is the technique we use for exploitation within this article.
  2. Exploiting Vulnerable Adjacent Subdomains: Another potential exploitation vector when the SameSite security setting is set to “Lax” is to leverage vulnerable adjacent subdomains which the system considers as being part of the same-site even though they are within different origins. The Portswigger Web Academy explains [the differences between a site and an origin](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions#what-s-the-difference-between-a-site-and-an-origin) in their article on “Bypassing SameSite Cookie Restrictions.” The article then goes on to explain how the [SameSite restrictions can be bypassed using vulnerable sibling domains](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions#bypassing-samesite-restrictions-via-vulnerable-sibling-domains).

We can exploit the behavior we observed previously where GET and POST requests are interchangeable to bypass the SameSite “Lax” security setting and perform a CSRF attack to promote an attacker-controlled user account to the POSTMASTER role. Figure 18 shows an example exploit payload that attempts to perform a CSRF attack using a cross-origin POST request.  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20652%20313'%3E%3C/svg%3E) _Figure 18: An exploit for the CSRF vulnerability leveraging a POST request would fail because of the SameSite “Lax” security setting enforced by default by modern browsers._ If we examine Figure 19, we observe that the cross-origin POST request sent by the CSRF payload does not contain the user’s session cookie.  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20622%20508'%3E%3C/svg%3E) _Figure 19: Attempting to exploit the CSRF vulnerability leveraging a POST request failed due to the “Lax” SameSite security setting configured on the WALOGIN session token._ In Figure 20 we can see an exploit payload that leverages a GET request instead of a POST request to invoke the same application functionality. _![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20664%20323'%3E%3C/svg%3E)_ _Figure 20: A successful attempt to exploit the CSRF vulnerability by leveraging the ability to invoke the same functionality leveraging a GET request instead of a POST request to bypass the SameSite cookie restrictions imposed by the “Lax” security setting._ Triggering this payload generates a GET request, which as we see in Figure 21 includes a session cookie. ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20666%20324'%3E%3C/svg%3E) _Figure 21: The CSRF vulnerability was successfully exploited by leveraging a GET request instead of a POST request to bypass the SameSite “Lax” security restrictions imposed by the browser._ Finally, Figure 22 shows the result of successfully exploiting this vulnerability: the attacker user account now exists as an administrative (POSTMASTER) user within the application. _ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20375'%3E%3C/svg%3E) _ _Figure 22: The[[email protected]](/cdn-cgi/l/email-protection) user account was added as a POSTMASTER (i.e. Administrative) user within the ListServ application._

### Arbitrary File Upload and Stored Cross Site Scripting

During our analysis of the WA.exe application binary we identified an endpoint that we couldn’t map back to a component within the frontend interface. This function, “redirect_for_upload_applet”, worked in conjunction with a Java applet that, while still shipped with the application, didn’t appear to be in use within the frontend of the application anymore. We observed that the “redirect_for_upload_applet” function was invoked after the application performed parsing of the parameters passed to the CGI binary as shown in Figure 23.  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20230'%3E%3C/svg%3E) _Figure 23: The redirect_for_upload_applet function is invoked from the main function after parsing of parameters passed to the WA application._ The redirect_for_upload_applet function leverages parameter F to construct a filename that the attacker can partially control. The application then writes the user-controlled input specified in the query string to that file. Figure 24 shows the relevant code from the redirect_for_upload_applet function. Unfortunately from an attacker’s perspective, the wafopen function properly prevents directory traversal attacks and the .qs extension applied to the filename prevents an attacker from having full control over the file extension. While an attacker could leverage alternative data streams to fully control the extension, this then prevents them from controlling the contents of the underlying file. We attempted various methods of bypassing the appending of .qs to the extension without success such as by specifying null bytes or CRLF characters within file names. ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20633%20266'%3E%3C/svg%3E) _Figure 24: The redirect_for_upload_applet function leverages an attacker-controlled parameter when generating the filename to be written to disk. Attacker controlled data is then written to the newly created file._ The curl command that follows can trigger the file upload issue on a vulnerable system. This command results in a file named “XSS.html.qs” being created within the “archives/upload” directory. “curl -v -X $’POST’ –data-binary $’P1=<script>alert(“XSS”)</script>&F=XSS.html&U=XSS’ <http://192.168.6.62/cgi-bin/wa>_“_ We observe the output of the command in Figure 25 and note the Content-Type header is set to “text/html” despite the extension being “.qs” when Apache is configured as the web server for the ListServ application. This appears to occur only when the filename includes “.html.”. ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20663%20336'%3E%3C/svg%3E) _Figure 25: An example curl command sent to an instance of the ListServ application to upload a file named XSS.html.qs containing a cross-site scripting payload to the application server._ In Figure 26 we can see the execution of the corresponding JavaScript code in the victim’s browser when accessing “archives/upload/XSS.html.qs” on the ListServ site.  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20338'%3E%3C/svg%3E) _Figure 26: An example payload uploaded to a test system resulting in the execution of a cross-site scripting payload within the victim’s browser._

### Stack Based Overflow Vulnerability

Another methodology we leverage when performing vulnerability research is a more bottom-up focused approach to testing an application. For example, if an application leverages dangerous function calls such as sprintf in a CGI application or ObjectInputStream.readObject in the case of an enterprise Java application we will perform an analysis of these dangerous sinks in an attempt to map them to input sources that are attacker controlled. In this case, we reviewed the sprintf calls made within the LSV.exe and WA.exe applications and found an instance where an environment variable was being read and passed directly to the sprintf function without a corresponding length check (see Figure 27).  ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20654%20303'%3E%3C/svg%3E) _Figure 27: Praetorian observed that the lsv.exe application read from the SMTP_HOSTNAME environment variable and then passed the obtained value to the sprintf function which wrote to a fixed stack-based buffer of 512 bytes._ We observed that the SMTP_HOSTNAME environment variable was configurable within the administrative component of the ListServ application. This highlights one of the downsides of the bottom-up approaches to vulnerability research as it can result in vulnerabilities that are exploitable, but require privileged access to the application to exploit. We reconfigured the SMTP_HOSTNAME environment variable to contain a long-string of A characters (see Figure 28) and observed that the program stack was corrupted the next time the ListServ application attempted to send an email, as shown in Figure 29. ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20665%20472'%3E%3C/svg%3E) _Figure 28: Praetorian modified the SMTP_HOSTNAME variable to include a long string of A characters._ ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20669%20473'%3E%3C/svg%3E) _Figure 29: A stack trace indicating the return address on the stack was corrupted as a result of the buffer overflow vulnerability._ However, we decided not to move ahead with developing a full blown proof-of-concept exploit for this particular issue. Several factors made this vulnerability less than ideal from an operational perspective, including the following: 

  1. Exploitation of the vulnerability requires modifying the SMTP settings within the ListServ application, which could interfere with the core email-sending functionality of the application.
  2. The vulnerability is only triggered after a restart of the ListServ application, which is not possible to do from the primary user interface.
  3. A failed exploit attempt after triggering the stack-based overflow vulnerability effectively bricks the LSV service indefinitely until the attacker’s malicious change to the SMTP_HOSTNAME variable is reverted.

This vulnerability is a great example of why [attackers only exploit a small percentage of real-world vulnerabilities](https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities#:~:text=Known%20exploited%20vulnerabilities%20should%20be,by%20attackers%20in%20the%20wild.). Often, valid vulnerabilities also are logistically difficult to exploit in the context of a real-world operation and thus attackers follow the path of least resistance and leverage alternative vectors to gain access. 

## Conclusion

In an effort to safeguard our customers, we perform proactive vulnerability research with the goal of identifying zero-day vulnerabilities that are likely to impact the security of leading organizations. In this case, while we didn’t meet our target objective of identifying a pre-authentication remote code execution vulnerability that we could exploit reliably (without requiring user-interaction), we were able to identify several serious issues within the application that, when combined with user-interaction, would allow for remote code execution. Unfortunately, ListServ was unresponsive to the security issues reported by Praetorian so no patches are currently available for these issues. Praetorian recommends that users of ListServ consider migrating to another application as the vendor doesn’t appear to be performing proper maintenance of the application. If you’d like to learn more about the Chariot offensive security platform, please don’t hesitate to [contact us](/contact-us) to schedule a demo. 

## Vulnerability Disclosure Timeline

The following is the disclosure timeline outlining the communication with ListServ by Praetorian in an attempt to responsibly disclose these security vulnerabilities: 

  * July 18th, 2023 – Praetorian made an initial contact with ListServ’s support email address to verify it was the appropriate email address to report security issues given the lack of documented reporting channels. ListServ responded on the same day that this was the appropriate channel for reporting security issues.
  * July 19th, 2023 – Praetorian provided writeups documenting the five discovered vulnerabilities to ListServ support. ListServ support responded on the same day indicating that they were conducting internal discussions regarding the technical details of these vulnerabilities.
  * July 21st, 2023 – ListServ requested information on the ListServ version Praetorian used for testing. Praetorian provided information on the version we used, which was the latest version available on the ListServ website. ListServ responded indicating that they are still discussing these issues internally.
  * August 17th, 2023 – Praetorian followed up with ListServ as there had been no further communication with ListServ since July 21st, 2023. ListServ responded that they were still discussing the issues internally.
  * September 11th, 2023 – Praetorian followed up again with ListServ indicating that it had been 55 days since the initial disclosure and indicated that we planned to disclose these issues at the 90 day mark if they had not been remediated by that point. ListServ replied indicating that the issue had been escalated to their development team.
  * September 27th, 2023 – Praetorian followed up again with ListServ indicating that it had been roughly 70 days since the initial disclosure and reiterated that we plan to release technical details at the 90 day mark. ListServ responded they were still waiting to hear back from their development team.
  * October 10th, 2023 – Praetorian followed up again indicating that we planned to release the blog post detailing the vulnerabilities on October 16th, 2023. Praetorian did not receive a response from ListServ.
  * October 18th, 2023 – Praetorian released the technical blog post with no patch available from ListServ.

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
