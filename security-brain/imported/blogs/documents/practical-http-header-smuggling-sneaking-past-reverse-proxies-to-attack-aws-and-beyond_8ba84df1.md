---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-10_practical-http-header-smuggling-sneaking-past-reverse-proxies-to-attack-aws-and-.md
original_filename: 2021-11-10_practical-http-header-smuggling-sneaking-past-reverse-proxies-to-attack-aws-and-.md
title: 'Practical HTTP Header Smuggling: Sneaking Past Reverse Proxies to Attack AWS
  and Beyond'
category: documents
detected_topics:
- rate-limit
- api-security
- cloud-security
- access-control
- xss
- command-injection
tags:
- imported
- documents
- rate-limit
- api-security
- cloud-security
- access-control
- xss
- command-injection
language: en
raw_sha256: 8ba84df169ef711419d4acf0dd9c6d1a421b20d6452f2d6f63e755cbde07a733
text_sha256: 487c7e9c54ab2f71f0de5ec582811ec9cefb89bdd0bec054d0b332b5c43f70f6
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Practical HTTP Header Smuggling: Sneaking Past Reverse Proxies to Attack AWS and Beyond

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-10_practical-http-header-smuggling-sneaking-past-reverse-proxies-to-attack-aws-and-.md
- Source Type: markdown
- Detected Topics: rate-limit, api-security, cloud-security, access-control, xss, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `8ba84df169ef711419d4acf0dd9c6d1a421b20d6452f2d6f63e755cbde07a733`
- Text SHA256: `487c7e9c54ab2f71f0de5ec582811ec9cefb89bdd0bec054d0b332b5c43f70f6`


## Content

---
title: "Practical HTTP Header Smuggling: Sneaking Past Reverse Proxies to Attack AWS and Beyond"
url: "https://www.intruder.io/research/practical-http-header-smuggling"
final_url: "https://www.intruder.io/research/practical-http-header-smuggling"
authors: ["Daniel Thatcher (@_danielthatcher)"]
bugs: ["HTTP Header Smuggling", "HTTP request smuggling"]
publication_date: "2021-11-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3184
---

[![Intruder logo](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/64931cbdee18510b47f41730_Logo.svg)](/)

  * Platform

  * [AI PentestingThe depth of a pentest, on-demand](/platform/ai-pentesting)
  * [Cloud SecurityDaily config checks](/platform/cloud-security)
  * [Attack Surface ManagementDetect changes and hidden assets](/platform/attack-surface-management)
  * [GregAI Security AnalystAct faster](/platform/ai-security-analyst)
  * [Vulnerability ManagementScan, prioritize, remediate](/platform/vulnerability-management)
  * [IntegrationsCompliance and workflow management![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/68bf47477497d547db8ce5ad_integrations.svg)](/platform/integrations)

  * Solutions  

  * [External ScanningInfrastructure security](/use-cases/external-vulnerability-scanning)
  * [Attack Surface MonitoringRespond to changes](/use-cases/attack-surface-monitoring)
  * [DASTSecure web apps](/use-cases/dast)
  * [Website Security140k+ checks](/use-cases/website-security)
  * [Risk Based PrioritizationNo more alert fatigue](/use-cases/risk-based-vulnerability-management)
  * [API SecurityTest your APIs](/use-cases/api-security)
  * [Asset DiscoveryReveal unknown targets](/use-cases/asset-discovery)
  * [Emerging Threat DetectionCheck and act fast](/use-cases/emerging-threat-scanning)
  * [CSPMDaily cloud config checks](/use-cases/cspm)
  * [ComplianceSOC 2, ISO, HIPAA, DORA](/use-cases/compliance)
  * [Cyber Hygiene ReportingDemonstrate progress](/use-cases/vulnerability-management-reporting)
  * [Container Image ScanningAutomated discovery and scanning](/use-cases/container-image-scanning)
  * [Secrets DetectionPrevent leaked credentials](/use-cases/secrets-detection)
  * [Internal ScanningSecure employee devices](/use-cases/internal-vulnerability-scanning)
  * [Case Studies](/success-stories)

  * [Pricing](/pricing)
  * Resources

Free Tools

  * [cvemonVulnerability intel](https://cvemon.intruder.io/)
  * [ AutoswaggerCheck for API auth flaws](https://github.com/intruder-io/autoswagger)
  * [ AWASP Top TenOWASP, but with evidence](https://awasp.org/)

Security

  * [ Security ResearchInsights from our experts](/research)
  * [ BlogGuides & insights](/blog)
  * [ Cyber GlossaryLearn the lingo](/glossary)

Customers

  * [Help CenterFAQs & tutorials](https://help.intruder.io/en/?_gl=1*9iuogt*_ga*MTQwOTAxMDU5NC4xNjgyNTk3MDI0*_ga_ME4CJVYS32*MTY4NjU0NDQ1MS4xOS4wLjE2ODY1NDQ0NTEuNjAuMC4w)
  * [ Developer HubAPIs & integrations](https://developers.intruder.io/docs/welcome)
  * [ Trust CenterSecurity & compliance](https://trust.intruder.io/)

  * Company

  * [About IntruderHistory and mission](/about-us)
  * [PressNews and interviews](/press)
  * [Partner ProgramBecome a reseller](/partners)
  * [CareersWork with us](https://careers.intruder.io/?_gl=1*1nmt3bk*_ga*MTQwOTAxMDU5NC4xNjgyNTk3MDI0*_ga_ME4CJVYS32*MTY4NzI0OTQ3NS4yOC4xLjE2ODcyNDk0NzYuNTkuMC4w)
  * [ContactGet in touch](/contact)

[BOOK A DEMO](/get-demo)[Try free](https://portal.intruder.io/free_trial?__hstc=17958374.b73aa9ab7ef5c36b66105c3ccda231eb.1733843293400.1733843293400.1733843293400.1&__hssc=17958374.1.1733843293400&__hsfp=51185828)[Log in](https://accounts.intruder.io/login?__hstc=17958374.745348f99aa3f380087c4ff0668fb314.1734654557436.1734654557436.1734654557436.1&__hssc=17958374.1.1734654557436&__hsfp=51185828)

[Log in](https://accounts.intruder.io/login?__hstc=17958374.745348f99aa3f380087c4ff0668fb314.1734654557436.1734654557436.1734654557436.1&__hssc=17958374.1.1734654557436&__hsfp=51185828)[Try for free](https://portal.intruder.io/free_trial?__hstc=17958374.b73aa9ab7ef5c36b66105c3ccda231eb.1733843293400.1733843293400.1733843293400.1&__hssc=17958374.1.1733843293400&__hsfp=51185828)[BOOK A DEMO](/get-demo)

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f89fada52ff5ffd531bf5_clouds_centre.svg)

[![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8b9557aa5dcce0cdf59a_Icon%20\(2\).svg)Back to more research](/research)

# Practical HTTP Header Smuggling: Sneaking Past Reverse Proxies to Attack AWS and Beyond

![Practical HTTP Header Smuggling: Sneaking Past Reverse Proxies to Attack AWS and Beyond](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/61dd9339d05701c9830b35ef_smugglers.avif)

[![Daniel Thatcher ](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6569d36ffc2f9ec21b3f563c_Dan.T.avif)Daniel Thatcher Security Research Engineer](/author/daniel-thatcher)

Updated

October 11, 2022

Published

November 10, 2021

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f855045438548a4944e33_Brand.svg)![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8556a95b95be4c061fe0_Brand.svg)![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8564317c519dedb1d71e_Frame%203605.svg)

[![Daniel Thatcher ](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6569d36ffc2f9ec21b3f563c_Dan.T.avif)Daniel Thatcher Security Research Engineer](/author/daniel-thatcher)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Modern web applications typically rely on chains of multiple servers, which forward HTTP requests to one another. The attack surface created by this forwarding is increasingly receiving more attention, including the recent popularisation of [cache](https://portswigger.net/research/practical-web-cache-poisoning) [poisoning ](https://portswigger.net/research/web-cache-entanglement)and [request](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn) [smuggling ](https://i.blackhat.com/USA-20/Wednesday/us-20-Klein-HTTP-Request-Smuggling-In-2020-New-Variants-New-Defenses-And-New-Challenges-wp.pdf)vulnerabilities. Much of this exploration, especially recent request smuggling research, has developed new ways to hide HTTP request headers from some servers in the chain while keeping them visible to others – a technique known as "header smuggling". This paper presents a new technique for identifying header smuggling and demonstrates how header smuggling can lead to cache poisoning, IP restriction bypasses, and request smuggling.

## Background

A chain of HTTP servers used by a web application can often be modelled as consisting of two components:

  * A "front-end" server which directly handles requests from users. These servers typically handle caching and load balancing, or act as web application firewalls (WAFs).
  * A "back-end" server which the front-end server forwards requests to. This is where the application's server-side code runs.

![](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/61dd9339d05701fd000b35ea_image001%20\(1\).jpg)

This model is often a simplification of reality. There may be multiple front-end and back-end servers, and front-end and back-end servers are often themselves chains of multiple servers. However, this model is sufficient to understand and develop the attacks presented in this article, as well as most of the recent research into attacking chains of servers.

Back-end servers often rely on front-end servers providing accurate information in the HTTP request headers, such as the client's IP address in the "X-Forwarded-For" header, or the length of the request body in the "Content-Length" header. To provide this information accurately, front-end servers must filter out the values of these headers provided by the client, which are untrusted and cannot be relied upon to be accurate.

Using header smuggling, it is possible to bypass this filtering and send information to the back-end server which it treats as trusted. I will show how this led to bypassing of IP restrictions in [AWS API Gateway](https://aws.amazon.com/api-gateway/), as well as an easily exploitable cache poisoning issue. I will then discuss how the methodology used to find these vulnerabilities can also be adapted to safely detect request smuggling based on multiple "Content-Length" headers (CL.CL request smuggling) in black-box scenarios.

## Methodology

The method developed by this research to identify header smuggling vulnerabilities determines whether a "mutation" can be applied to a header to allow it to be snuck through to a back-end server without being recognised or processed by a front-end server. A mutation is simply an obfuscation of a header. The following examples are mutated versions of the "Content-Length" header:

This method relies on the fact that most web servers will return an error when sent a request with an invalid "Content-Length" header:

**_Request_**

** _Response_**

The methodology also relies on comparing the responses when valid and invalid values are sent in both the regular and a mutated form of the "Content-Length" header. We start by sending valid and invalid values in a regular "Content-Length" header to the target:

**_Request_**

** _Response_**

‍

** _Request_**

** _Response_**

Since including a junk value in the "Content-Length" header causes a difference in response, we can infer that at least 1 server in the chain is parsing this header.

This server chain allows headers to be smuggled through to the back-end by appending characters after a space in the header name. So, when we substitute "Content-Length" with "Content-Length abcd" in the requests and send the requests again, we get the following results:

**_Request_**

** _Response_**

‍

** _Request_**

** _Response_**

There are three important things to note here when comparing the responses from the regular and the mutated "Content-Length" headers. The first is that an invalid value in each header causes a different response than a valid one does. This indicates that at least one server in the chain is parsing each of these headers as a "Content-Length" header.

Secondly, the same response is returned when a valid value is included in each header:

**_Request_**

** _Response_**

‍

** _Request_**

** _Response_**

This shows that the presence of the mutated header has not prevented either server from parsing the request as normal. This check is important to ensure that the mutation hasn't invalidated the request entirely.

The final important thing to notice is that an invalid value in each header causes different responses in the mutated header compared to the regular one:

**_Request_**

** _Response_**

‍

** _Request_**

** _Response_**

This suggests that the errors are likely originating from different servers in the chain. In other words, a front-end server is not parsing our mutated "Content-Length" header as though it is the regular "Content-Length" header, while the back-end server is – we have header smuggling.

## Examples

### Bypassing Restrictions

#### **AWS API Gateway IP Restrictions**

While scanning across bug bounty programs, I noticed that APIs created using AWS API Gateway allowed header smuggling by appending characters to the header name after a space – for example by changing "X-My-Header: test" to "X-My-Header abcd: test". I also noticed that the "X-Forwarded-For" header was being stripped and rewritten by a front-end server.

API Gateway allows you to limit API access to certain IP addresses by using a [resource policy](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-resource-policy-access/) such as the following:

This policy limits access to only accept requests from the IP address 1.2.3.4 (which I unfortunately don't own) and the private range 10.0.0.0/8. Requests originating from other IP addresses are met with an error:

**_Request_**

** _Response_**

Unsurprisingly, simply adding the "X-Forwarded-For" header to a request was no match for AWS' security controls:

**_Request_**

** _Response_**

However, when applying a mutation which allows header smuggling to this header, access was granted:

**_Request_**

** _Response_**

This allows IP restrictions to be bypassed, but in practical situations it might be hard to pull off. Addresses from private ranges are obvious guesses, but if those are not allowed then it might be hard to guess an IP address which has been granted access. However, one of the most important things I've learnt is to senselessly try stupid things:

**_Request_**

** _Response_**

It turned out that adding the header "X-Forwarded-For abcd: z" to requests allowed IP restrictions from AWS resource policies to be bypassed in API gateway.

#### AWS Cognito Rate Limiting

I discovered a similar, but very minor, bug in [AWS Cognito](https://aws.amazon.com/cognito/) during a penetration test. Cognito is an authentication provider which you can integrate into your applications to help handle authentication.

After five requests to the “ConfirmForgotPassword” or “ForgotPassword” targets in a short period of time, my IP address was temporarily blocked. However, adding "X-Forwarded-For:[0x0b]z" to the request allowed 5 more requests to be made. Unfortunately, it wasn't possible to cycle different values or valid IP addresses in this header keep gaining five more attempts, meaning the impact of this bug is minimal. However, it still acts as a nice example of how header smuggling can be used to bypass rate limiting.

### Cache Poisoning

AWS promptly fixed the IP restriction bypass after I reported it to them. When retesting, I noticed that I could still smuggle headers through to the back-end server using the same mutation, leading me to wonder if there were any other interesting headers worth trying.

There are probably some headers that API gateway uses internally which would be interesting, but I was unable to identify any of these. What did stand out as interesting was the "Host" header, and I started to wonder what would happen if I tried to sneak this header through to back-end servers.

I setup two APIs using API Gateway – one "victim" API and one "attacker" API:

**_Request_**

** _Response_**

‍

** _Request_**

** _Response_**

The interesting behaviour appeared when including a mutated "Host" header alongside a regular "Host" header:

**_Request_**

** _Response_**

API gateway was returning the response from the API specified in the mutated "Host" header. This is in contrast to the behaviour of most web servers, which will not view the mutated "Host" header as a "Host" header and instead take the host from the regular "Host" header. This becomes interesting when such a server is acting as a cache in front of API gateway, as it will cache the result of the above request as though it was a request for "victim.i.long.lat", even though the response is from the "attacker.i.long.lat" API.

![](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/61dd9339d05701b03f0b35eb_image002%20\(1\).jpg)

To demonstrate this, I setup [CloudFront](https://aws.amazon.com/cloudfront/) in front of API Gateway with the "AllViewer" request policy, which causes all headers to be forwarded. Sending the above request, and then requesting "https://victim.i.long.lat/a" shows that the response from the attacker's API has been stored in the cache for the victim's API:

**_Request_**

** _Response_**

‍

** _Request_**

** _Response_**

This cache poisoning is rather easy to exploit as an attacker can setup their own API and return arbitrary content for any path. This allows them to completely overwrite any entry in the victim's cache, effectively allowing them to completely control the content of the victim's API.

### Request Smuggling

#### Amit Klein's Bug

At Black Hat USA 2020 Amit Klein presented a request smuggling based on 2 "Content-Length" headers ("CL.CL" request smuggling). The bug could be triggered when [Squid ](http://www.squid-cache.org/)was used as a reverse proxy in front of the [Abyss web server](https://aprelium.com/abyssws/) using the following requests sent in the same connection:

![](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/61dd9339d0570111670b35ee_Image%201.JPG)

The first request, shown in green, contains two "Content-Length" headers – 1 mutated and the other unmutated. Squid will only parse the unmutated header, and will take the length of the first request's body to be 33 bytes, which is shown in blue. Squid then takes the second request to be the one shown in red – a "GET" request to "/doesntexist".

Abyss on the other hand will parse both the mutated and unmutated "Content-Length" headers, and takes the values of 0 bytes from the mutated header. It therefore thinks that the second request is the one which starts in blue – a "GET" request to "/a.html".

![](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/61dd9339d057011c950b35ed_image003%20\(1\).jpg)

The total effect of this is that Abyss responds with the content for "/a.html", and Squid caches this response for the path "/doesntexist", giving cache poisoning.

#### Methodology Background

Klein's research is particularly interesting as it showed that CL.CL request smuggling exists in modern systems, despite it being a bug that felt almost too simple. Klein worked in a white box scenario to find this vulnerability, though I set out to find a methodology which could detect CL.CL request smuggling in black box scenarios.¹

James Kettle's research which popularised request smuggling presented a simple methodology for safely detecting request smuggling based on a "Content-Length" and a "Transfer-Encoding" header ("CL.TE" and "TE.CL" request smuggling) using timeouts. This methodology attempts to cause the back-end to expect more content than is forwarded by the front-end to trigger a timeout from the back-end. By scanning for CL.TE request smuggling first, it's possible to minimise the risk of affecting other users' requests when testing a vulnerable system.

An attempt to do the same with CL.CL request smuggling might look similar to the following:

Against a vulnerable system where the front-end reads the unmutated "Content-Length" header and the back-end reads the mutated version, this will usually cause a timeout. Though in the case of the Squid and Abyss setup, no timeout will be caused as Abyss does not wait for the body to be sent before replying to the "POST" request.

The danger comes when this request is sent to a vulnerable system where the front-end reads the mutated header, and the back-end reads the unmutated version. The front-end server will forward the "z" body, which the back-end server will believe to be the start of the next request. The socket has then been poisoned, and there is a high chance of another user's request failing due to the backend server seeing the request method as, for example, "zGET"². 

If we don't know which "Content-Length" header the front-end server is going to parse, we have a 50% chance of causing a timeout in a vulnerable system, and a 50% chance of poisoning the socket, potentially causing another user's request to fail.

#### Methodology

The methodology used to detect header smuggling can be modified slightly to create a safe CL.CL request smuggling detection methodology. The following example shows how this modified methodology can be used to detect Klein's bug in Squid and Abyss.

First, send a "baseline" request to the target system with the pair of "Content-Length" headers which are being tested:

**_Request_**

** _Response_**

The next step is to send the same request two times more - once with a junk value in each "Content-Length" header:

**_Request_**

** _Response_**

‍

** _Request_**

** _Response_**

Comparing the 3 responses, we notice that:

  * Both the requests containing junk values triggered responses which are different from the baseline response. This indicates that the value of each header is being parsed by at least 1 server.
  * The responses to the requests containing junk values are different. This suggests that the errors are coming from different servers, and therefore different servers in the chain are parsing the different versions of the "Content-Length" header.

These conditions indicate potential CL.CL request smuggling. When moving beyond this point with the investigation it is important to know which header the front-end server is parsing to minimise the chance of poisoning the socket and affecting other users.

This can be achieved by sending a request with a single, unmutated "Content-Length" header, and observing the resulting error:

**_Request_**

** _Response_**

As the front-end server is almost certainly parsing the "Content-Length" header in this request, the resulting error is likely generated by the front-end server. By comparing this error to the ones generated earlier in the process, we see that it is the same error generated when the headers "Content-Length: z" and "Content-Length abcd: 0" are sent in the same request. Hence, the front-end server is parsing the unmutated "Content-Length" header, and the back-end server the mutated one³. 

These requests only indicate a potential request smuggling vulnerability, though it is far from certain. For example, many servers will process both forms of the "Content-Length" header, but throw an error when they have different values, making request smuggling impossible.

To continue the investigation, timeouts can be a good next step to confirm the behaviour. However, these are not always reliable, and sometimes exploitation attempts will be required.

#### Exploitation with Turbo Intruder

The exploitation steps from this point are very similar to those used by Kettle in his research. They largely rely on [Turbo Intruder](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack) scripts which send 1 request to poison the socket, quickly followed by multiple benign requests with the hope that one of these requests is poisoned.

I've created a modified version of one of Kettle's Turbo Intruder scripts which attempts to exploit CL.CL request smuggling to cause a 404 error, which you can find [here](https://gist.github.com/DanielIntruder/ddd773e95ad78895cedb064401a938fa). This is often the simplest way to confirm request smuggling. A similar script which attempts to trigger cache poisoning can be found [here](https://gist.github.com/DanielIntruder/e235ab83d095bde25219e0d4f178087d).

These scripts are configured to run against my lab environment using Squid and Abyss, though can easily be modified to target other systems using other mutations. You may find them a useful starting point when trying to exploit CL.CL request smuggling in other systems.

## Tooling

Once a mutation which allows header smuggling has been identified, the next step is to find an interesting header to sneak through to the back-end. Sometimes you may know a header you wish try, however, there is often no obvious choice. To assist with this second case, as well as to help find mutations which lead to header smuggling, I am releasing a fork of James Kettle's [Param Miner Burp Suite extension](https://github.com/PortSwigger/param-miner), which can be found [here](https://github.com/intruder-io/param-miner). _‍_

 _Update: these changes have now been merged into_[ _Param Miner_](https://github.com/PortSwigger/param-miner) _, and you can play with the new functionality by downloading Param Miner from the BApp store._

This fork adds two new pieces of functionality. The first is a scan which uses the methodology I've described to identify mutations which lead to header smuggling. The second is an option when guessing headers which will cause the extension to automatically identify header smuggling mutations, and then also guess headers using these mutations.

## Defences

Defending against these types of bugs can be somewhat complicated as they rely on differences in implementations between web servers, rather than a specific flaw in 1 web server. One of the main defences is to scan your systems with the fork of Param Miner released as part of this research to try and identify any vulnerabilities.

Front-end servers should avoid forwarding weirdly formatted headers. This is the approach being taken by AWS with API gateway – including writing tests to validate this behaviour. This also prevented [Cloudflare](https://www.cloudflare.com/) from being used in the cache poisoning example, as they do not forward any headers with a space in the name.

There is a concept known as "[Postel's Law](https://devopedia.org/postel-s-law)" which states that you should "be liberal in what you accept, and conservative in what you send" when dealing with protocols such as HTTP. While the idea of being liberal in parsing HTTP requests may be beneficial to front-end servers, which receive requests from a multitude of different clients which each contain their own quirks, some setups may allow back-end servers to be stricter. If the front-end server filters or normalises a request before it is forwarded, the back-end server should not be exposed to quirks form a wide range of clients. Instead, handling of these quirks can be entrusted entirely to the front-end server, and the back-end server only has to accept requests from one client – the front-end server.

## Conclusion

While often considered to be just a tool for request smuggling, header smuggling can produce interesting behaviours and vulnerabilities when considered in its own right. The methodology and tooling developed for this research makes identifying header smuggling and resulting vulnerabilities easier. This research has shown how header smuggling can be used to bypass restrictions and to achieve cache poisoning, though there are likely many more vulnerabilities waiting to be found. 

I have also demonstrated a methodology for safely identifying CL.CL request smuggling in black-box scenarios, and released Turbo Intruder scripts to aid in exploiting CL.CL request smuggling.

## Thanks

I would like to thank the AWS security team, and in particular Dan Urson, for their response to the vulnerabilities found during this research. The disclosure process has been incredibly smooth, and they've worked very fast to resolve the vulnerabilities considering the scale of their infrastructure.

## Footnotes

1\. Trying to detect CL.CL request smuggling was the origin of this research project.

2\. Some scanning with zgrab suggests that this risk can be minimised, though not completely eliminated, by making the body a CRLF which most web servers will discard from the start of a request.

3\. You may notice that this logic can be used to make timeout-based detections safe for CL.CL request smuggling. As some vulnerable setups, including the Squid and Abyss setup, will not produce a timeout, I chose to use the purely error-based approach presented here.

‍

## Other research articles

[![Broken Authorization in APIs: Introducing Autoswagger](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6894aca6c10c23d043d1231d_Autoswagger.jpg)Broken Authorization in APIs: Introducing AutoswaggerAPIs power modern apps but often expose critical data, and mistakes in their design can be shockingly easy to exploit. Intruder’s research found that the same simple authorization flaws behind the 2022 Optus breach are still alarmingly widespread today. To help tackle this, Intruder built a free tool - Autoswagger - available on GitHub.Daniel AndrewJuly 22, 2025](/research/broken-authorization-apis-autoswagger)

[![Shadow IT Isn’t Invisible - It’s Expanding Your Attack Surface. Here’s Proof](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/68a5f1dcbfefcd9580f0c30c_Shadow%20IT%20blog%20header.jpg)Shadow IT Isn’t Invisible - It’s Expanding Your Attack Surface. Here’s ProofIntruder’s security team used CT log queries to find millions of exposed hosts - then found a wide range of Shadow IT exposures attackers can exploit. See real-world Shadow IT risks and what they mean for your attack surface.Benjamin MarrAugust 20, 2025](/research/shadow-it-risks)

[![Path Traversal and Code Execution in CSLA.NET \(CVE-2024-28698\)](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6699343aa6692b92e8724f39_Exposure-Management-thumbnail.avif)Path Traversal and Code Execution in CSLA.NET (CVE-2024-28698)CSLA.NET is a framework that helps structure business logic for .NET applications into re-usable objects, and share those objects between systems. During a penetration test last year, we discovered an interesting path traversal vulnerability affecting applications using this framework. Read on for a technical explanation of how this vulnerability works. Sam PizzeyJuly 19, 2024](/research/path-traversal-and-code-execution-in-csla-net-cve-2024-28698)

## Sign up for your free 14-day trial

[Try for free](https://portal.intruder.io/free_trial)

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/678e7f3d291be28e461ce216_74b8b3edcebfb1003b2f3fe2483d1a6a_Feature%3DOverview-2.svg)
