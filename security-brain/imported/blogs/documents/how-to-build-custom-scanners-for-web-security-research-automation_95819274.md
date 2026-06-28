---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-03_how-to-build-custom-scanners-for-web-security-research-automation.md
original_filename: 2023-10-03_how-to-build-custom-scanners-for-web-security-research-automation.md
title: How to build custom scanners for web security research automation
category: documents
detected_topics:
- ssrf
- xss
- race-condition
- csrf
- sso
- sqli
tags:
- imported
- documents
- ssrf
- xss
- race-condition
- csrf
- sso
- sqli
language: en
raw_sha256: 9581927493e2a3907ad55a162f20d82c536b8dc93d150249d32d573834f7263b
text_sha256: 699277962a2816adab0186c6be7b618b7a804ffa8910f115edf3a82178c2b686
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# How to build custom scanners for web security research automation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-03_how-to-build-custom-scanners-for-web-security-research-automation.md
- Source Type: markdown
- Detected Topics: ssrf, xss, race-condition, csrf, sso, sqli
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `9581927493e2a3907ad55a162f20d82c536b8dc93d150249d32d573834f7263b`
- Text SHA256: `699277962a2816adab0186c6be7b618b7a804ffa8910f115edf3a82178c2b686`


## Content

---
title: "How to build custom scanners for web security research automation"
page_title: "How to build custom scanners for web security research automation | PortSwigger Research"
url: "https://portswigger.net/research/how-to-build-custom-scanners-for-web-security-research-automation"
final_url: "https://portswigger.net/research/how-to-build-custom-scanners-for-web-security-research-automation"
authors: ["James Kettle (@albinowax)"]
bugs: ["Race condition"]
publication_date: "2023-10-03"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 727
---

[](/)

[Login](/users)

Products Solutions [Research](/research) [Academy](/web-security) Support Company

[Customers](/customers) [About](/about) [Blog](/blog) [Careers](/careers) [Legal](/legal) [Contact](/contact) [Resellers](/support/reseller-faqs)

[My account](/users/youraccount) [Customers](/customers) [About](/about) [Blog](/blog) [Careers](/careers) [Legal](/legal) [Contact](/contact) [Resellers](/support/reseller-faqs)

[ ![Burp Suite DAST](/content/images/svg/icons/enterprise.svg) **Burp Suite DAST** The enterprise-enabled dynamic web vulnerability scanner. ](/burp/enterprise) [ ![Burp Suite Professional](/content/images/svg/icons/professional.svg) **Burp Suite Professional** The world's #1 web penetration testing toolkit. ](/burp/pro) [ ![Burp Suite Community Edition](/content/images/svg/icons/community.svg) **Burp Suite Community Edition** The best manual tools to start web security testing. ](/burp/communitydownload) [View all product editions](/burp)

[ **Burp Scanner** Burp Suite's web vulnerability scanner ![Burp Suite's web vulnerability scanner'](/mega-nav/images/burp-suite-scanner.jpg) ](/burp/vulnerability-scanner)

[ **Attack surface visibility** Improve security posture, prioritize manual testing, free up time. ](/solutions/attack-surface-visibility) [ **CI-driven scanning** More proactive security - find and fix vulnerabilities earlier. ](/solutions/ci-driven-scanning) [ **Application security testing** See how our software enables the world to secure the web. ](/solutions) [ **DevSecOps** Catch critical bugs; ship more secure software, more quickly. ](/solutions/devsecops) [ **Penetration testing** Accelerate penetration testing - find more bugs, more quickly. ](/solutions/penetration-testing) [ **Automated scanning** Scale dynamic scanning. Reduce risk. Save time/money. ](/solutions/automated-security-testing) [ **Bug bounty hunting** Level up your hacking and earn more bug bounties. ](/solutions/bug-bounty-hunting) [ **Compliance** Enhance security monitoring to comply with confidence. ](/solutions/compliance)

[View all solutions](/solutions)

[ **Product comparison** What's the difference between Pro and DAST? ![Burp Suite Professional vs Burp Suite DAST](/mega-nav/images/burp-suite.jpg) ](/burp/dast/resources/dast-vs-professional)

[ **Support Center** Get help and advice from our experts on all things Burp. ](/support) [ **Documentation** Tutorials and guides for Burp Suite. ](/burp/documentation) [ **Get Started - Professional** Get started with Burp Suite Professional. ](/burp/documentation/desktop/getting-started) [ **Get Started - DAST** Get started with Burp Suite DAST. ](/burp/documentation/dast/getting-started) [ **Downloads** Download the latest version of Burp Suite. ](/burp/releases)

[Visit the Support Center](/support)

[ **Downloads** Download the latest version of Burp Suite. ![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg) ](/burp/releases)

Articles

  * [Overview](/research)
  * Core Topics

[Black Hat](/research/black-hat) [XSS](/research/cross-site-scripting-research) [Request Smuggling](/research/request-smuggling) [Template Injection](/research/template-injection) [Top 10 Hacking Techniques](/research/top-10-web-hacking-techniques)

  * [Articles](/research/articles)
  * Meet the Researchers

[James Kettle](/research/james-kettle) [Gareth Heyes](/research/gareth-heyes) [Zakhar Fedotkin](/research/zakhar-fedotkin)

  * [Talks](/research/talks)
  * [ RSS  ](/research/rss)

# How to build custom scanners for web security research automation

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhow-to-build-custom-scanners-for-web-security-research-automation&text=How+to+build+custom+scanners+for+web+security+research+automation%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhow-to-build-custom-scanners-for-web-security-research-automation)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhow-to-build-custom-scanners-for-web-security-research-automation)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhow-to-build-custom-scanners-for-web-security-research-automation)
  * [ ](mailto:?subject=How+to+build+custom+scanners+for+web+security+research+automation&body=How+to+build+custom+scanners+for+web+security+research+automation%0A%0AIn+this+post%2C+I%27ll+share+my+approach+to+developing+custom+automation+to+aid+research+into+under-appreciated+attack+classes+and+\(hopefully\)+push+the+boundaries+of+web+security.+As+a+worked+example%2C+I%27l%0A%0Ahttps://portswigger.net/research/how-to-build-custom-scanners-for-web-security-research-automation)
  * [ ](/research/rss)

![James Kettle](/content/images/profiles/callout_james_kettle_112px.png)

### [James Kettle](/research/james-kettle)

Director of Research

[@albinowax](https://twitter.com/albinowax)

  * **Published:** Tuesday, 3 October 2023 at 13:34 UTC

  * **Updated:** Thursday, 1 August 2024 at 08:26 UTC

  * 

![](/cms/images/be/7d/784e-article-black-box_automation_blog.png)  

In this post, I'll share my approach to developing custom automation to aid research into under-appreciated attack classes and (hopefully) push the boundaries of web security. 

As a worked example, I'll build on my research from [Smashing the state machine: the true potential of web race conditions](https://portswigger.net/research/smashing-the-state-machine). If you haven't already seen it, the [DEFCON recording of this presentation](https://www.youtube.com/watch?v=tKJzsaB1ZvI&list=PLoX0sUafNGbEkK0ai5P_DB2HDnljRAJyZ) is now available and probably worth a watch.

#### Identify the opportunity

Do you think it's possible to create a scanner that can automatically detect web [race conditions](/web-security/race-conditions)? I initially dismissed the idea, as the race conditions I found required triggering complex, multi-step authenticated interactions with websites and spotting subtle side-effects.

Over the course of this research, I noticed that race conditions often occur in clusters. They bubble up from shaky libraries and frameworks, so if you spot one in a website it's likely that others lurk nearby. This meant that automated detection of race conditions might be valuable even if the detected races were themselves harmless.

I decided that this idea was worth exploring based on my familiarity with the topic, novel tooling in the form of the single-packet attack, and a test-bed that meant I could try out the concept in a day or two.

#### Avoid over-committing

When attempting to automate something tricky, a common pitfall is to try to automate too much and ultimately fail to achieve anything useful. To avoid this, I like to examine my manual testing methodology and identify the smallest, earliest step that I could plausibly automate. Here's the manual testing process I use for race conditions:

![](/cms/images/c3/96/d22c-article-methodology.png)  

Since the 'predict' phase is just about efficiency, we can skip this and simply try to automate the 'probe' phase. The goal of this phase is to use a batch of concurrent requests to trigger an 'anomaly' and prove that an endpoint might have a sub-state. 

#### Embrace the unexpected

I wrote code to send a request ten times sequentially, then resend it ten times in under 1ms using the single-packet attack. I anticipated that on a race-prone website, the concurrent requests might trigger a 50X error response. 

At this point I could have improved efficiency and reduced false positives by only targeting dynamic-looking endpoints, and only reporting responses with 50X codes. However, the best research discoveries often come from unexpected outcomes. This means that it's important to avoid writing your expectations into the code. I deliberately left room for unexpected outcomes by testing all observed requests regardless of what they were for, and reporting any difference in status-code. 

When it comes to research I'd rather have false positives than false negatives.

#### Make iteration easy

This approach inevitably results in a flood of false positives at the start, so it's crucial that making iterative improvements is painless.

I implemented this in a Burp Suite extension, and as a testbed I used a project file containing the homepage and resources from around ~30,000 websites with bug bounty programs. For more details on this setup, check out [Cracking the lens](https://portswigger.net/research/cracking-the-lens-targeting-https-hidden-attack-surface).

For a full run, I just select all the requests in the proxy, right click, and launch the scan. It prioritises shorter domains so results on high-profile targets tend to turn up quickly.

#### Automate your triage

I typically manually triage a small portion of the findings, then analyse my triage process and automate it. While processing the results I found myself:

  * Ignoring findings where crucial requests just timed out
  * Ignoring findings with 429 status codes as these are just rate-limits
  * Ignoring findings with 502/503 as these indicate back-end timeouts
  * Trying extra sequential requests after the concurrent batch
  * Adding cache-busters to filter out cache behaviour 

Implementing this filter process in my scan-check and re-running it left me with a number of promising findings:

  * Assorted curious 50X and 307 codes
  * A webserver that issues a cryptic '501 Not Implemented' response claiming it doesn't support GET requests when you use the single-packet attack. 
  * A website that triggers a server-side request to a back-end system for SSO purposes. The single-packet attack overloaded the back-end and triggered an error message disclosing the full URL.
  * Another server which intermittently issued a 400 Bad Request response when hit with synchronised requests. This is curious because it suggests that there may be a race condition in their request parsing, which might enable a desync attack. 

Unfortunately none of these left me with a clear route forward other than in-depth manual investigation, which I didn't have time for before the conference I was targeting (Nullcon Goa).

#### Abuse gadgets

What I needed was an approach that would detect behaviour that was obviously dangerous. But what dangerous race-condition can you directly detect from a site's homepage? Well, now and then I've seen reports of applications and caches getting mixed up and either sending responses to the wrong people, or serving up raw memory. The most notorious example of this is, of course, [Cloudbleed](https://portswigger.net/research/top-10-web-hacking-techniques-of-2017#5).

How can we tell if we've received a response intended for someone else? As a human it's easy, and an LLM could probably tell at the price of terrible performance, but it's a tricky question for crude, regex-level automation. 

This is where gadgets come in. Gadgets are helpful features present on some websites that make vulnerability detection easier. We can lean on gadgets to quickly and easily explore whether a concept is worth investing more time in. Relying on gadgets for vulnerability detection will cause a lot of false negatives, but during the early stages of research it's worth the trade-off for development speed.

Quite a few websites embed data about the user's request in order to expose it to client-side JavaScript. This typically includes the user's IP address, and request properties like the URL and User-Agent. On sites containing this type of gadget I could detect race-infoleak vulnerabilities by placing a unique 'canary' parameter in every request, then analysing each response to see if it contained a canary from a different request.

This approach initially flagged a lot of websites, but most of them just had cache-poisoning via an [unkeyed query string](https://portswigger.net/research/web-cache-entanglement). 

After filtering out the cache poisoning and other 'canary storage' behaviour via some more code tweaks, some genuine findings remained. The best example was a certain website where thanks to a race condition, you could obtain the URLs that live users were accessing simply by repeatedly fetching the homepage:

`window.PAGE_STATE={…{"params":{"utm_souce":"bing",…`

This was perfect for Nullcon; I knocked together a couple of slides and released the scan-checks in [Backslash Powered Scanner](https://portswigger.net/research/backslash-powered-scanning-hunting-unknown-vulnerability-classes). You can install it via the BApp store, and [peruse the code on Github](https://github.com/PortSwigger/backslash-powered-scanner).

#### Wrapping up

As we've seen, research-oriented scanning is quite different to building a normal scanner so please be careful when cross-applying this advice to other use-cases.

If you'd like to try your hand at custom automation, the [new BChecks feature](https://portswigger.net/blog/bchecks-houston-we-have-a-solution) in Burp Suite is designed to make this extra accessible. 

If you found this useful, you might also enjoy the presentation [Hunting evasive vulnerabilities: finding flaws that others miss](https://www.youtube.com/watch?v=skbKjO8ahCI) where I take a look at research automation from a different angle.

In my next post I'll continue the race condition theme and look beyond HTTP/2 to explore which other protocols support the single-packet attack.

[ automation ](/research/automation) [ race condition ](/research/race-condition) [ How to research ](/research/how-to-research)

[Back to all articles](/research/articles)

## Related Research

### [ WebSocket Turbo Intruder: Unearthing the WebSocket Goldmine 17 September 2025 WebSocket Turbo Intruder: Unearthing the WebSocket Goldmine ](/research/websocket-turbo-intruder-unearthing-the-websocket-goldmine) ### [ The single-packet attack: making remote race-conditions 'local' 18 October 2023 The single-packet attack: making remote race-conditions 'local' ](/research/the-single-packet-attack-making-remote-race-conditions-local) ### [ Smashing the state machine the true potential of web race conditions 09 August 2023 Smashing the state machine the true potential of web race conditions ](/research/smashing-the-state-machine) ### [ How I choose a security research topic 14 June 2023 How I choose a security research topic ](/research/how-i-choose-a-security-research-topic)

Burp Suite

[Web vulnerability scanner](/burp/vulnerability-scanner) [Burp Suite Editions](/burp) [Release Notes](/burp/releases)

Vulnerabilities

[Cross-site scripting (XSS)](/web-security/cross-site-scripting) [SQL injection](/web-security/sql-injection) [Cross-site request forgery](/web-security/csrf) [XML external entity injection](/web-security/xxe) [Directory traversal](/web-security/file-path-traversal) [Server-side request forgery](/web-security/ssrf)

Customers

[Organizations](/organizations) [Testers](/testers) [Developers](/developers)

Company

[About](/about) [Careers](/careers) [Contact](/about/contact) [Legal](/legal) [Privacy Notice](/privacy) [Modern Slavery Statement](/modern-slavery-statement)

Insights

[Web Security Academy](/web-security) [Blog](/blog) [Research](/research) [Engineering](/engineering)

[![PortSwigger Logo](/content/images/logos/portswigger-logo.svg)](/) [ Follow us](https://twitter.com/Burp_Suite)

© 2026 PortSwigger Ltd.
