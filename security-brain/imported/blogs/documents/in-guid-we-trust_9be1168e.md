---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-11_in-guid-we-trust.md
original_filename: 2022-10-11_in-guid-we-trust.md
title: In GUID We Trust
category: documents
detected_topics:
- command-injection
- password-reset
- api-security
- cloud-security
- sso
- idor
tags:
- imported
- documents
- command-injection
- password-reset
- api-security
- cloud-security
- sso
- idor
language: en
raw_sha256: 9be1168ead94b5021aef705dbd340dc05a56b58022dd51089102de3ab1c04748
text_sha256: b659e5d41e4c65b16e40eaa8b61e9badabdb64b29d39f76ec547c987625a0f7f
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# In GUID We Trust

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-11_in-guid-we-trust.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, api-security, cloud-security, sso, idor
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `9be1168ead94b5021aef705dbd340dc05a56b58022dd51089102de3ab1c04748`
- Text SHA256: `b659e5d41e4c65b16e40eaa8b61e9badabdb64b29d39f76ec547c987625a0f7f`


## Content

---
title: "In GUID We Trust"
url: "https://www.intruder.io/research/in-guid-we-trust"
final_url: "https://www.intruder.io/research/in-guid-we-trust"
authors: ["Daniel Thatcher (@_danielthatcher)"]
bugs: ["IDOR", "Password reset", "Race condition", "Account takeover"]
publication_date: "2022-10-11"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2060
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

# In GUID We Trust

![In GUID We Trust](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/634580968ca941acf32e6263_blog_post_banner.avif)

[![Daniel Thatcher ](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6569d36ffc2f9ec21b3f563c_Dan.T.avif)Daniel Thatcher Security Research Engineer](/author/daniel-thatcher)

Updated

February 15, 2024

Published

October 11, 2022

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f855045438548a4944e33_Brand.svg)![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8556a95b95be4c061fe0_Brand.svg)![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8564317c519dedb1d71e_Frame%203605.svg)

[![Daniel Thatcher ](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6569d36ffc2f9ec21b3f563c_Dan.T.avif)Daniel Thatcher Security Research Engineer](/author/daniel-thatcher)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

GUIDs (often called UUIDs) are widely used in modern web applications. However, seemingly very few penetration testers and bug bounty hunters are aware of the different versions of GUIDs and the security issues associated with using the wrong one.

In this blog post I'll walk through an account takeover issue from a recent penetration test where GUIDs were used as password reset tokens:

If you've already spotted the issue and think you know how to exploit it, then you may want to skip to the CTF section at the end, and have a look at the [tool](https://github.com/intruder-io/guidtool) I've released. Otherwise, read on.

## GUID Versions

There are two characters in every GUID which indicate some information about the GUID:
  
  
  bcd510ca-3357-_4_8d7-_8_e3f-1206b9c09632

The first of these is the version number, which can be found directly after the second hyphen. For example, the GUID shown above is a version 4 GUID.

There are five possible values for this version detailed in the [RFC](https://datatracker.ietf.org/doc/html/rfc4122#section-4.2.2):

**Version 0**

Only seen in the nil GUID ("00000000-0000-0000-0000-000000000000").

**Version 1**

The GUID is generated in a predictable manner based on:

  * The current time
  * A randomly generated "clock sequence" which remains constant between GUIDs during the uptime of the generating system
  * A "node ID", which is generated based on the system's MAC address if it is available

**Version 3**

The GUID is generated using an MD5 hash of a provided name and namespace.

**Version 4**

The GUID is randomly generated.

**Version 5**

The GUID is generated using a SHA1 hash of a provided name and namespace.

‍

If you only take one thing away from this blog post, it should be to always look at a GUIDs version and become mildly concerned when it isn't 4. Once you start doing this, you can become very quick at spotting the version, and it almost becomes subconscious.

While these versions are defined in the standard, some applications will just encode 128 bits of random data as hex and add hyphens in the right places to generate GUIDs rather than following the RFC. All rules about how the GUIDs are generated will go out the window in these situations, but you should be able to spot them easily as the version number will change between GUIDs.

## Attacking Password Reset Functionality

If you look at the link from the start of this post you might now be able to spot the issue:
  
  
  https://example.com/reset?token=3fcf5140-47ca-_1_1ec-9755-c75cdea7a1c7

This link contains a version 1 GUID, which is generated using predictable data. To attack this functionality, we want to issue a password reset request for another user, and then predict the GUID that was included in the link emailed to that user. For this, we need to know the approximate time the GUID was generated, as well as the node ID and clock sequence of the generating system. I've released a [small tool](https://github.com/intruder-io/guidtool) to print information about version 1 GUIDs and generate them to help with this process.

We begin attacking this functionality by issuing a password reset request for an account we own, and then inspecting the GUID sent to us in the password reset link:

The timestamp is represented as the number of 100-nanosecond intervals since midnight UTC on 15 October 1582 (the date of Gregorian reform to the Christian calendar according to the RFC), because this is clearly how any rational person represents time. It's uncommon for systems to use this level of precision when generating GUIDS however, so usually the last four digits of the timestamp are zero, indicating that we're measuring time to the nearest millisecond. It's important to take note of this level of precision, as it drastically affects the number of GUIDs we need to guess.

We now generate a password reset request for our victim's account and take note of the server time when this was generated. If the server returns the "Date" header, then this is easy. Otherwise, we'll have to work it out based on your local time, and the timestamp encoded in the GUIDs sent in your password reset links.

guidtool will extract the node ID and clock sequence from a sample GUID you provide, so we just need to give it a sample GUID from one of our password reset links, the estimated time the GUID was generated to the nearest second, and the precision we want in our timestamps:

The "-p" parameter provides the precision using the number of 100-nanosecond intervals between timestamps. The easy way to work out the value of this is to copy the number of zeros you see at the end of the timestamp when you ran "guidtool -i <guid>" with a one before them.

The output here is every possible GUID the server could have generated during the one second before and one second after our specified time . If our estimate of when the victim's password reset link was generated is within one second of the actual value, then their token will be in this output.

All we need to do now is to submit the password reset using every GUID from this output, and when we use the one that's in the victim's password reset link, we will change their password and gain access to their account.

The issue of predictable tokens is of course not limited to password reset functionality, though I hope this example effectively shows the danger of using an insecure GUID version in applications.

## CTF

I've created a little CTF challenge to show this issue, which can be found here:

<http://gooey.intrud.es>

There are two flags – the first should be straightforward to find once you've read and understood this blog post, while the second is designed to be a harder follow-up for when you've found the first flag.

## One Last Thing: Race Conditions and Version 1 GUIDs

Most GUID libraries will try not to generate the same version 1 GUID twice. If the library generates timestamps to the nearest millisecond and is asked to generate two GUIDs within the same millisecond, it will typically add 1 to the timestamp of the second GUID:

This may come in useful in some situations when attacking version 1 GUIDs. You can try generate a GUID you can see and a GUID you can't see within the same millisecond. If the GUID you can see has a 1 added to the timestamp, it is very likely that the GUID you can't see will be the same, but without the 1 added to the timestamp.

I haven't come across a scenario where this approach is required, but if you find one I'd be interested to hear about it. You can find me at [@_danielthatcher](https://twitter.com/_danielthatcher) on Twitter if you'd like to share.

‍

## Other research articles

[![Detecting Server-Side Prototype Pollution](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/63ecf9671b745240e0a16c36_blog-header.avif)Detecting Server-Side Prototype PollutionPrototype pollution bugs have been a feature in many CTFs in recent years, and real-world examples in open-source applications have led to impactful exploits such as remote code execution and denial-of-service. The discovery of these bugs has long relied on access to source code, with no safe black-box detection techniques being widely used.Daniel Thatcher February 15, 2023](/research/server-side-prototype-pollution)

[![In GUID We Trust](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/634580968ca941acf32e6263_blog_post_banner.avif)In GUID We TrustGUIDs (often called UUIDs) are widely used in modern web applications. However, seemingly very few penetration testers and bug bounty hunters are aware of the different versions of GUIDs and the security issues associated with using the wrong one.Daniel Thatcher October 11, 2022](/research/in-guid-we-trust)

[![Shadow IT Isn’t Invisible - It’s Expanding Your Attack Surface. Here’s Proof](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/68a5f1dcbfefcd9580f0c30c_Shadow%20IT%20blog%20header.jpg)Shadow IT Isn’t Invisible - It’s Expanding Your Attack Surface. Here’s ProofIntruder’s security team used CT log queries to find millions of exposed hosts - then found a wide range of Shadow IT exposures attackers can exploit. See real-world Shadow IT risks and what they mean for your attack surface.Benjamin MarrAugust 20, 2025](/research/shadow-it-risks)

## Sign up for your free 14-day trial

[Try for free](https://portal.intruder.io/free_trial)

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/678e7f3d291be28e461ce216_74b8b3edcebfb1003b2f3fe2483d1a6a_Feature%3DOverview-2.svg)
