---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-15_detecting-server-side-prototype-pollution.md
original_filename: 2023-02-15_detecting-server-side-prototype-pollution.md
title: Detecting Server-Side Prototype Pollution
category: documents
detected_topics:
- command-injection
- api-security
- cloud-security
- sso
- xss
- automation-abuse
tags:
- imported
- documents
- command-injection
- api-security
- cloud-security
- sso
- xss
- automation-abuse
language: en
raw_sha256: 3a4cebf0bc514f05346f5fb16dbb2bc511ded7a478a349905685560e5f2b2caf
text_sha256: 12829c38b7c994ee9c2fe18486e976f344d240a1b6df822a27fd1c76ac616d12
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Detecting Server-Side Prototype Pollution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-15_detecting-server-side-prototype-pollution.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, cloud-security, sso, xss, automation-abuse
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `3a4cebf0bc514f05346f5fb16dbb2bc511ded7a478a349905685560e5f2b2caf`
- Text SHA256: `12829c38b7c994ee9c2fe18486e976f344d240a1b6df822a27fd1c76ac616d12`


## Content

---
title: "Detecting Server-Side Prototype Pollution"
url: "https://www.intruder.io/research/server-side-prototype-pollution"
final_url: "https://www.intruder.io/research/server-side-prototype-pollution"
authors: ["Daniel Thatcher (@_danielthatcher)"]
bugs: ["Server-side prototype pollution"]
publication_date: "2023-02-15"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1522
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

# Detecting Server-Side Prototype Pollution

![Detecting Server-Side Prototype Pollution](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/63ecf9671b745240e0a16c36_blog-header.avif)

[![Daniel Thatcher ](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6569d36ffc2f9ec21b3f563c_Dan.T.avif)Daniel Thatcher Security Research Engineer](/author/daniel-thatcher)

Updated

December 1, 2023

Published

February 15, 2023

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f855045438548a4944e33_Brand.svg)![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8556a95b95be4c061fe0_Brand.svg)![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8564317c519dedb1d71e_Frame%203605.svg)

[![Daniel Thatcher ](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6569d36ffc2f9ec21b3f563c_Dan.T.avif)Daniel Thatcher Security Research Engineer](/author/daniel-thatcher)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Prototype pollution bugs have been a feature in many CTFs in recent years, and real-world examples in open-source applications have led to impactful exploits such as remote code execution and denial-of-service. The discovery of these bugs has long relied on access to source code, with no safe black-box detection techniques being widely used.

Both myself and PortSwigger’s [Gareth Heyes](https://infosec.exchange/@gaz) have independently spent time looking into developing safe black-box detection techniques to open up prototype pollution as a more commonly identified bug class. We’ve ended up taking different approaches to the problem, so if you haven’t already read [Gareth's post](https://portswigger.net/research/server-side-prototype-pollution) I would highly recommend it.

Prototype pollution is a vulnerability found in JavaScript applications which allows attackers to effectively add accessible properties to all objects, which can often lead to remote code execution or a denial-of-service. Olivier Arteau's NorthSec [talk](https://www.youtube.com/watch?v=LUsiFV3dsK8) and accompanying [paper](https://github.com/HoLyVieR/prototype-pollution-nsec18/blob/master/paper/JavaScript_prototype_pollution_attack_in_NodeJS.pdf) provide a great introduction to prototype pollution for those not already familiar with it. This post doesn't require a deep understanding of prototype pollution - if you can understand what's going on in the following code block then you understand enough to keep reading:
  
  
  > obj = { a: 1 }
  { a: 1 }
  > obj.b
  undefined
  > {}.__proto__.b = 2
  2
  > obj.b
  2

## Detection

### Gunship CTF Challenge

The detection technique relies on a common coding pattern found in many applications. This coding pattern can be seen in the "Gunship" CTF challenge from the Hack the Box 2020 University CTF:

The "/api/submit" endpoint uses the "unflatten" function to convert the JSON in the request body to the "artist" object, then accesses the "name" property of this object. The "unflatten" function is imported from an old version of the "flat" library, which is vulnerable to prototype pollution.

The first step of the detection is to find a required parameter. For our purposes, we define this as a parameter which changes the application’s response when it is omitted. We can see a sample request and response using the expected input:

By removing the "name" parameter we get a different response:

This error occurs because the application attempts to access the non-existent "name" property of the "artist" object. If we can now trigger prototype pollution to add the "name" property to every object with a value of "test", we should no longer see the error from the above request.

The way to do this is to cycle through many payloads which are likely to trigger prototype pollution in the application to add the "name" parameter to the prototype. After sending each of these payloads, we can resend the request with the missing "name" parameter to see if we have been successful and the response has changed. In this case, the following payload will trigger the vulnerability:

After we have sent this request, we get the following response from our request with the missing "name" parameter:

This response is different from when we previously omitted the name parameter, and matches the one we saw when we provided a value of "test" for the name parameter. This indicates that we have managed to successfully trigger prototype pollution.

### Kibana

This technique is not just limited to simple CTF challenges. For example, it can also be used to detect Michał Bentkowski's [CVE-2019-7609](https://research.securitum.com/prototype-pollution-rce-kibana-cve-2019-7609/) in Kibana. Browsing an instance of Kibana 6.5.4 we can generate the following base request and response:

If we remove the "interval" parameter from this request we can see that we trigger a different response containing an error:

This indicates that the "interval" parameter is required. Now, we send the payload described by Michał Bentkowski to trigger prototype pollution to add the "interval" parameter to the JavaScript prototype with a value of "auto":

Now, we resend our previous request with the missing "interval" parameter and note that we get a different response:

This response matches the one received from our initial request containing the "interval" parameter, suggesting that we have successfully exploited prototype pollution to add this parameter to the prototype.

## Limitations

While this technique can work, it is not without its limitations. The most obvious is that it relies on developers converting user input to a JavaScript object. In my experience this is common, but it's by no means universal.

This technique can also be dangerous when used against the wrong application. The following request exploiting Olivier Arteau's bug in GhostCMS to add a meaningless parameter to the prototype initially seems like it may be harmless:

However, after sending this request, all requests to the homepage of the application are met with an error. While causing a complete denial-of-service with a single request certainly shows impact, it should be avoided on live applications.

I have demonstrated this technique against single instances of applications, but if an application is doing any form of load balancing which routes your requests to multiple application servers then detection becomes slightly more complex. You may have polluted the prototype on one of these application servers, but your next request may be sent to a different application server which doesn't have a polluted prototype. This problem can be solved by sending many requests with the missing parameter to ensure that one of them is routed to the same application server as the request containing the payload.

## Comparison to Gareth’s Techniques

At this point you may be wondering which techniques to use to detect prototype pollution vulnerabilities. The answer is to almost always use [Gareth's techniques](https://portswigger.net/research/server-side-prototype-pollution). Gareth's techniques don't rely on developers using specific coding patterns, so are going to detect prototype pollution vulnerabilities in a wider range of applications. I would also consider his techniques safer since you will end up attempting to add only a specific set of properties to the prototype.

There may be some edge cases where the technique described in this post comes in useful. I hope that it may also be useful to someone else in further researching prototype pollution. If you have any questions or find anything interesting, please feel free to message me at [@_danielthatcher](https://twitter.com/_danielthatcher) on Twitter, though please bear in mind that I'm checking Twitter quite infrequently these days so please don't be offended if I take a little while to respond.

‍

## Other research articles

[![How We’re Using AI to Write Vulnerability Checks \(and Where It Falls Short\)](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/68c2eb250f406e07d6693871_Agentic%20AI%20Header%20Image%20Design.jpg)How We’re Using AI to Write Vulnerability Checks (and Where It Falls Short)Intruder’s security team is experimenting with agentic AI to accelerate vulnerability checks. Discover what’s working, what isn’t, and why AI isn’t the silver bullet it’s made out to be.Benjamin MarrSeptember 11, 2025](/research/the-state-of-agentic-ai-in-vulnerability-management)

[![From enterprise chatbots to gooner caves: exposed AI infrastructure is rampant](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/69c65f5be3fdb1d002c176a3_%5Bblog%5D%20From%20Enterprise%20ChatBots%20To%20Gooner%20Caves%2C%20Scanning%20The%20Internet%20For%20Exposed%20LLM%20Infra.avif)From enterprise chatbots to gooner caves: exposed AI infrastructure is rampantWe scanned 1 million AI services and found widespread misconfigurations, exposed credentials, and unauthenticated APIs. AI infrastructure security is falling dangerously behind.Benjamin MarrMarch 27, 2026](/research/from-enterprise-chatbots-to-gooner-caves-exposed-ai-infrastructure-is-rampant)

[![In GUID We Trust](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/634580968ca941acf32e6263_blog_post_banner.avif)In GUID We TrustGUIDs (often called UUIDs) are widely used in modern web applications. However, seemingly very few penetration testers and bug bounty hunters are aware of the different versions of GUIDs and the security issues associated with using the wrong one.Daniel Thatcher October 11, 2022](/research/in-guid-we-trust)

## Sign up for your free 14-day trial

[Try for free](https://portal.intruder.io/free_trial)

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/678e7f3d291be28e461ce216_74b8b3edcebfb1003b2f3fe2483d1a6a_Feature%3DOverview-2.svg)
