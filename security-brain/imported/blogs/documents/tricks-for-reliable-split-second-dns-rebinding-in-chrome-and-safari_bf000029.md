---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-06_tricks-for-reliable-split-second-dns-rebinding-in-chrome-and-safari.md
original_filename: 2023-12-06_tricks-for-reliable-split-second-dns-rebinding-in-chrome-and-safari.md
title: Tricks for Reliable Split-Second DNS Rebinding in Chrome and Safari
category: documents
detected_topics:
- command-injection
- api-security
- cloud-security
- sso
- ssrf
- xss
tags:
- imported
- documents
- command-injection
- api-security
- cloud-security
- sso
- ssrf
- xss
language: en
raw_sha256: bf000029b2c87953e275f4d919224b3146578b2df233465dbce5fb3cc0773cef
text_sha256: 6246f25f1b3421586872b90461da0e32745541de8026189067c2fa45a5c44247
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Tricks for Reliable Split-Second DNS Rebinding in Chrome and Safari

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-06_tricks-for-reliable-split-second-dns-rebinding-in-chrome-and-safari.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, cloud-security, sso, ssrf, xss
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `bf000029b2c87953e275f4d919224b3146578b2df233465dbce5fb3cc0773cef`
- Text SHA256: `6246f25f1b3421586872b90461da0e32745541de8026189067c2fa45a5c44247`


## Content

---
title: "Tricks for Reliable Split-Second DNS Rebinding in Chrome and Safari"
url: "https://www.intruder.io/research/split-second-dns-rebinding-in-chrome-and-safari"
final_url: "https://www.intruder.io/research/split-second-dns-rebinding-in-chrome-and-safari"
authors: ["Daniel Thatcher (@_danielthatcher)"]
programs: ["Google (Chrome)", "Apple (Safari)"]
bugs: ["DNS rebinding"]
publication_date: "2023-12-06"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 647
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

# Tricks for Reliable Split-Second DNS Rebinding in Chrome and Safari

![Tricks for Reliable Split-Second DNS Rebinding in Chrome and Safari](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/656ef8ebb535ad68279407d5_hack_ourselves_pt2.avif)

[![Daniel Thatcher ](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6569d36ffc2f9ec21b3f563c_Dan.T.avif)Daniel Thatcher Security Research Engineer](/author/daniel-thatcher)

Updated

January 12, 2024

Published

December 6, 2023

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f855045438548a4944e33_Brand.svg)![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8556a95b95be4c061fe0_Brand.svg)![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8564317c519dedb1d71e_Frame%203605.svg)

[![Daniel Thatcher ](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6569d36ffc2f9ec21b3f563c_Dan.T.avif)Daniel Thatcher Security Research Engineer](/author/daniel-thatcher)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

 _This is the second post in a two-part series on DNS rebinding._[_The first post_](http://www.intruder.io/research/we-hacked-ourselves-with-dns-rebinding) _covered a real-world exploit using DNS rebinding against our own product. In this post, I introduce new techniques for achieving reliable, split-second DNS rebinding in Chrome, Edge, and Safari when IPv6 is available, as well as a technique for bypassing the local network restrictions applied to the fetch API in Chromium-based browsers. This post assumes you have a basic understanding of DNS rebinding, as covered in the previous post._

DNS rebinding in browsers has traditionally been seen as a way for attackers to access internal network services by tricking victims into loading a malicious website, but with many modern web applications now driving headless browsers for part of their functionality, it's become a [useful tool](https://youtu.be/o-tL9ULF0KI?t=1157) for attacking web applications. In the previous post, I covered an example of this using perhaps the simplest method for rebinding. In that scenario, I had the luxury of a long time for the exploit to run, but this is unlikely to be the case on many web applications, where faster techniques are necessary.

# Slow Caches

Simple DNS rebinding techniques rely on returning different DNS records for successive lookups of the same hostname. For these attacks, the minimum time taken is the time between two successive DNS lookups being performed by the browser. This can sometimes be sped up by flushing the browser cache - generating a large number of DNS lookups to fill up the available cache space, and causing older entries to be discarded before they’ve expired - to cause the browser to perform a second lookup of the same hostname sooner.

When this works, it will still take somewhere in the order of 10 seconds, and often this technique won't work because of intermediate caches which can’t be cleared as easily as the browser’s cache. For example, during testing I found that on a freshly created Ubuntu EC2 instance I would only be able to get a different response for the same domain every 5 minutes due to the cache of _systemd-resolve_. On a VPN, I’ve seen DNS responses being cached for a minimum 30 minutes on the default resolver. It will often be a struggle to get users to keep a page open for this long to allow you to pull off a DNS rebinding exploit, let alone a headless browser being driven as part of a web application.

To speed up exploits, in 2010 Craig Heffner [presented](https://www.youtube.com/watch?v=VAaqABpjiUQ) the idea of performing DNS rebinding by replying with multiple A records for the same domain in the same response, a technique which was used by Gerald Doussot and Roger Meyer in [singularity](https://github.com/nccgroup/singularity) in 2019. The 2 records returned are the IP address of a public, attacker-controlled server and the (usually private) IP address of the target server.

The attack will only work if the browser attempts to communicate with the public server first and loads the attacker's malicious page. The attacker's web server then starts blocking traffic from the victim's browser, causing the browser to fall back to sending all future requests to the target server. In this case, JavaScript in the attacker's page will be able to send requests to the target IP address under the same origin.

‍

![](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/656ef9f5ad62e8b7c799895b_7t_agx3oKkMAatQ7KRe2yjtDkapPZNlS-cn9pcqoCdCYWS245BxRWu50eGY2j-V-rgn3Nm-6-srx9MeqNPOOcuRiZZaNlGe81f3Ah3OjJX_rBiwPr-_66_XNCBZfVw5g1fVk_uaUAKlOOS3Hd6M8GPs.avif)

‍

This technique does bypass the caching problem as the browser only has to perform one DNS lookup, though during my testing all the major browsers would consistently attempt to communicate to private IP addresses before public ones, meaning these techniques didn’t work. While I don't believe this behaviour is intended as a protection against DNS rebinding (I even got confirmation of this from one of the Chrome developers when informing them of my findings), it is effective at stopping this technique.

This new behaviour led me to research new techniques which can be used to achieve split-second DNS rebinding in Safari and Chromium-based browsers. The key to these techniques is finding new ways to make browsers initially use a public IP then switch to using a private IP when loading a website. Opening up Wireshark, I noticed that while loading websites in modern browsers, both an A and a AAAA query are sent. I started investigating whether this behaviour could be used to reliably perform DNS rebinding.

# Attacking Safari: Delaying DNS Responses

When you load a web page in Safari on a host with access to the internet over IPv6, A and AAAA DNS queries are sent for IPv4 and IPv6 addresses respectively. Safari will prioritise private IP addresses over public ones when multiple IP addresses are returned.

The interesting behaviour which allows for fast DNS rebinding in Safari occurs when either the A or AAAA response is delayed. In this case, Safari doesn't wait for all DNS responses, but instead sends HTTP requests as soon as the first DNS response is received. When the delayed DNS response is received, the IP addresses in this response are added to the pool of IP addresses that Safari can use for future requests to the domain.

This means that if the first DNS response is for a public IP address, and the delayed DNS response is for a private IP address, Safari will send the first requests to the public IP address until the delayed DNS response is received, at which point it will start sending requests to the private IP address.

‍

![](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/656efa8d5a4073db0042558d_SwKhlXyrBhRcE7_Jr-nzYS5BvW22EftGK3JnOR5bRWB4k6SeuEg-aRhRbQ6koyoCiXFIj0cMjPw3P6byy8TxLaUP_PnvPdI-v_Aqexo2unKZTKgdPCcxj_-Q52IeCxsEXktI-MCrpSgMEUkQ7T3HtYk.avif)

This provides a simple method for achieving DNS rebinding in Safari using a custom DNS server which handles queries for _*.r.intrud.es_ :

  1. Make the target browser load _http://safari.r.intrud.es_ , triggering A and AAAA lookups for _safari.r.intrud.es_.
  2. Have the DNS server return a AAAA record instantly, containing the IPv6 address of an attacker-controlled web server on the internet. Do not return the A response yet.
  3. Safari will make the first request to the attacker's web server once it has received the AAAA response. From the attacker’s web server, return a page with JavaScript to repeatedly request _http://safari.r.intrud.es/secret.txt_.
  4. Send the A response from the DNS server containing the IP address of the target server on the local network.
  5. Safari will now send the requests for _http://safari.r.intrud.es/secret.txt_ to the target server on the local network. The responses of these requests can be read by the page loaded from the attacker’s server without violating the same-origin policy.

To achieve this, I've written a small DNS server which can be used to delay DNS responses with command-line arguments. In practice, I found that delaying the A response by 100ms was almost always enough, though a delay of 200ms or more can be used to make the technique even more reliable. This server, as well as instructions for setting it up, can be found [here](https://github.com/intruder-io/dns-delay-server).

The PHP script I've used to exploit this will redirect the user to a random subdomain of r.intrud.es to avoid intermediate caches interfering with the exploit. It also includes the JavaScript directly in the page to avoid another resource load. You can find the code used [here](https://github.com/intruder-io/dns-delay-server/tree/main/safari-exploit).

Here's a video of this script in action, retrieving the contents of a file from a local web server:

I've tested in Safari and Brave on iOS, and found that this same technique will work to access services on the internal network.

# Attacking Chrome: Using AAAA Prioritisation

Chrome will prioritise loading pages on the local network over pages on the internet, but it gives more priority to loading pages over IPv6 instead of IPv4 when available. So the priority is:

  1. Local IPv6 (Highest Priority)
  2. Public IPv6
  3. Local IPv4
  4. Public IPv4 (Lowest Priority)

The key part here is that Chrome will prioritise a public IPv6 address over a private IPv4 address. Further, when Chrome knows multiple IP addresses for a domain, it will try a different IP address as soon as the server at one resets the connection.

![](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/656efa8dd44e3f1b22c2d234_OhJOu5UgU-O2KfTTtlOxv2F3gQ2pMEsTiTFvwy43yCx1fbTccvYyDfITnNnOEwiEpJFdaObjNwUJ5wLGUc7_ezv3tHvIqjvTdt0vnPolq9wvrMZg7voG-HeGdsLnq3Rv96wvxW7sdPNbv_Njbek5_xc.avif)

This gives a plan for fast DNS rebinding against Chrome:

  1. Load _http://chrome.r.intrud.es_ which will trigger A and AAAA lookups for _chrome.r.intrud.es_.
  2. Have the DNS server return an A record pointing to the target web server on the local network, and a AAAA record pointing to an attacker-controlled web server on the public internet.
  3. Chrome will prioritise the IPv6 address, and make the first request to load the page from the attacker controlled web-server, which returns JavaScript to repeatedly make requests to _http://chrome.r.intrud.es/secret.txt_.
  4. Shut down the attacker-controlled server so that all connections are reset. Chrome will now make all requests to the target server on the local network.
  5. Have the loaded page make requests to _http://chrome.r.intrud.es/secret.txt_. The responses to these requests can be read without violating the same-origin policy.

‍

This plan almost worked. The JavaScript on the page loaded from the internet attempted to make requests to the target on the local network, but these requests were blocked with the following error in the console:
  
  
  Access to fetch at 'http://chrome.r.intrud.es/secret.txt' from origin 'http://chrome.r.intrud.es' has been blocked by CORS policy: The request client is not a secure context and the resource is in more-private address space `local`.
  

This error occurs because Chrome partially implements the protections outlined in the [Private Network Access (PNA)](https://wicg.github.io/private-network-access/) specification.

## Bypassing Private Network Access

The PNA protections block pages loaded over plain HTTP from the public internet from making requests to the private networks. In Chrome, these protections are implemented for fetch requests, but aren’t yet implemented for iFrames. The incomplete implementation, along with DNS rebinding, allows the PNA restrictions on fetch requests to be bypassed.

We can repeat the exploit through to step 4 above, where the public web server has been shut off and all requests to _http://chrome.r.intrud.es_ are now directed to the target server on the local network. The loaded top page can’t make requests to the local network as it was loaded over HTTP from the public internet, but we can load _http://chrome.r.intrud.es_ in an iFrame. The page in this iFrame will be loaded from the target web server. As this server is on the local network, the page loaded in the iFrame is allowed to make requests to the local network.

The page in the iFrame is also under the same origin as the top page, which allows the top page to fully control the DOM of the framed page. This includes injecting scripts which make fetch requests into the framed page. These scripts can be used to access the target web server and exfiltrate data just as they would be able to from the top page if PNA wasn't implemented at all.

‍

![](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/656efa8d4b415f19ef581a3d_nEEXVEUe0aAtb0uCCybo32Gn1BBE4mferHk-57Qfv0naRGY8Brv58cq7teXot7gdOwJXtrF0blJCmGQKsMibJJARLS7s3is4CvCAlcusRafDLiSnM0fT3eKSiFrrQUYJLl4i3370uEhVWPBRccBkqnQ.avif)

‍

So, putting this all together we end up with a complete plan:

  1. Load _http://chrome.r.intrud.es_ which will trigger A and AAAA lookups for _chrome.r.intrud.es_.
  2. Have the DNS server return an A record pointing to the target web server on the local network, and a AAAA record pointing to an attacker-controlled web server on the public internet.
  3. Chrome will make the first request to load the top page from the attacker’s web-server, which returns a page to execute the following steps.
  4. Shut down the attacker-controlled server so that all connection attempts are reset. Chrome will now make all requests to the target server on the local network.
  5. Load _http://chrome.r.intrud.es_ in an iFrame.
  6. From the top page, inject a script into the framed page to request _http://chrome.r.intrud.es/secret.txt_ and send the response to the attacker's web server.

This works to achieve split-second DNS rebinding in Chrome:

To help achieve this exploit, I wrote a small web server which will stop when it receives a request to _/block_. You can find the source code and instructions for running it [here](https://github.com/intruder-io/rebind-server).

When attacking automated browsers, you'll often want to include an iFrame in the page which takes some time to load. This stops the browser considering the page fully loaded until that iFrame has loaded, and ensures that the exploit script has enough time to run. The following demo shows this exploit being used to extract credentials from the AWS metadata service when gowitness is used to take a screenshot of a malicious website from an EC2 with IPv6 enabled:

Or, for a scenario more likely to be found in a web application, headless Chromium being used to convert a web page to a PDF:

This bypass of Chrome's PNA restrictions was reported to the Chrome team through their issue tracker. They determined that it wasn't a security issue since the PNA restrictions are still in the process of being implemented.

# Summary

DNS rebinding can be a useful weapon in your arsenal for attacking web applications. In the first post in this series, I tried to show how rebinding exploits against web applications can be achievable without much complexity. In this post, I’ve provided tools and techniques to build reliable exploits against web applications driving automated browsers, even if they only load pages for a short time. I hope you now feel well-equipped to start using DNS rebinding in exploits against the applications you test.

‍

## Other research articles

[![Shadow IT Isn’t Invisible - It’s Expanding Your Attack Surface. Here’s Proof](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/68a5f1dcbfefcd9580f0c30c_Shadow%20IT%20blog%20header.jpg)Shadow IT Isn’t Invisible - It’s Expanding Your Attack Surface. Here’s ProofIntruder’s security team used CT log queries to find millions of exposed hosts - then found a wide range of Shadow IT exposures attackers can exploit. See real-world Shadow IT risks and what they mean for your attack surface.Benjamin MarrAugust 20, 2025](/research/shadow-it-risks)

[![Practical HTTP Header Smuggling: Sneaking Past Reverse Proxies to Attack AWS and Beyond](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/61dd9339d05701c9830b35ef_smugglers.avif)Practical HTTP Header Smuggling: Sneaking Past Reverse Proxies to Attack AWS and BeyondModern web applications typically rely on chains of multiple servers, which forward HTTP requests to one another. The attack surface created by this forwarding is increasingly receiving more attention, including the recent popularisation of cache poisoning...Daniel Thatcher November 10, 2021](/research/practical-http-header-smuggling)

[![Detecting Server-Side Prototype Pollution](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/63ecf9671b745240e0a16c36_blog-header.avif)Detecting Server-Side Prototype PollutionPrototype pollution bugs have been a feature in many CTFs in recent years, and real-world examples in open-source applications have led to impactful exploits such as remote code execution and denial-of-service. The discovery of these bugs has long relied on access to source code, with no safe black-box detection techniques being widely used.Daniel Thatcher February 15, 2023](/research/server-side-prototype-pollution)

## Sign up for your free 14-day trial

[Try for free](https://portal.intruder.io/free_trial)

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/678e7f3d291be28e461ce216_74b8b3edcebfb1003b2f3fe2483d1a6a_Feature%3DOverview-2.svg)
