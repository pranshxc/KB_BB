---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-20_cracking-recaptcha-turbo-intruder-style.md
original_filename: 2019-11-20_cracking-recaptcha-turbo-intruder-style.md
title: Cracking reCAPTCHA, Turbo Intruder style
category: documents
detected_topics:
- ssrf
- xss
- path-traversal
- automation-abuse
- race-condition
- csrf
tags:
- imported
- documents
- ssrf
- xss
- path-traversal
- automation-abuse
- race-condition
- csrf
language: en
raw_sha256: b195c34c6d9df5c442cad5e01638503fad9c1983167063d1e08a533ec1c056bf
text_sha256: 98441bce6eff793dcc4f06ab1f3ffeadd86a0a93765a0dca512c2d5d74b2776f
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Cracking reCAPTCHA, Turbo Intruder style

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-20_cracking-recaptcha-turbo-intruder-style.md
- Source Type: markdown
- Detected Topics: ssrf, xss, path-traversal, automation-abuse, race-condition, csrf
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `b195c34c6d9df5c442cad5e01638503fad9c1983167063d1e08a533ec1c056bf`
- Text SHA256: `98441bce6eff793dcc4f06ab1f3ffeadd86a0a93765a0dca512c2d5d74b2776f`


## Content

---
title: "Cracking reCAPTCHA, Turbo Intruder style"
page_title: "Cracking reCAPTCHA, Turbo Intruder style | PortSwigger Research"
url: "https://portswigger.net/research/cracking-recaptcha-turbo-intruder-style"
final_url: "https://portswigger.net/research/cracking-recaptcha-turbo-intruder-style"
authors: ["James Kettle (@albinowax)"]
programs: ["Google"]
bugs: ["Captcha bypass", "Race condition"]
publication_date: "2019-11-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4927
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

# Cracking reCAPTCHA, Turbo Intruder style

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fcracking-recaptcha-turbo-intruder-style&text=Cracking+reCAPTCHA%2C+Turbo+Intruder+style%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fcracking-recaptcha-turbo-intruder-style)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fcracking-recaptcha-turbo-intruder-style)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fcracking-recaptcha-turbo-intruder-style)
  * [ ](mailto:?subject=Cracking+reCAPTCHA%2C+Turbo+Intruder+style&body=Cracking+reCAPTCHA%2C+Turbo+Intruder+style%0A%0ATired+of+proving+you%27re+not+a+robot%3F+In+this+post%2C+I%27ll+show+how+you+can+partially+bypass+Google+reCAPTCHA+by+using+a+new+Turbo+Intruder+feature+to+trigger+a+race+condition.+This+vulnerability+was+rep%0A%0Ahttps://portswigger.net/research/cracking-recaptcha-turbo-intruder-style)
  * [ ](/research/rss)

![James Kettle](/content/images/profiles/callout_james_kettle_112px.png)

### [James Kettle](/research/james-kettle)

Director of Research

[@albinowax](https://twitter.com/albinowax)

  * **Published:** Wednesday, 20 November 2019 at 14:59 UTC

  * **Updated:** Wednesday, 20 November 2019 at 15:33 UTC

  * 

![](/cms/images/26/95/f16a82675f84-article-recaptcha_article.png)  

Tired of proving you're not a robot? In this post, I'll show how you can partially bypass [Google reCAPTCHA](https://www.google.com/recaptcha) by using a new Turbo Intruder feature to trigger a race condition. This vulnerability was reported to Google 8 months ago but they declined to fix it, leaving the patching burden on individual websites. As a case study, I'll target Reddit.  

### Background

While researching [HTTP Desync Attacks](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn), I found I needed to send a group of HTTP requests within a tiny time window, to minimize the chance of someone else's request landing in the middle of my attack and interfering. I turned to [Turbo Intruder](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack), which uses a custom HTTP stack built from scratch with speed in mind. However, Turbo Intruder was originally designed for total request throughput (requests per second), rather than making requests arrive simultaneously.

### Last-byte synchronization

To address this, I added support for last-byte synchronization, where Turbo first sends the whole of every request except the last byte, then, when they're all ready, 'releases' each request by sending the last byte. This helps minimize the effect of network congestion and latency on our attempt to get multiple requests processed simultaneously. I'm not sure who invented this technique - I first saw it years ago being used to improve timing attack accuracy - but it certainly works.

To use this feature, just add a 'gate' argument when queuing your requests, and then invoke engine.openGate when you're ready to send them

`engine.queue(request, gate='race1')  
engine.queue(request, gate='race1')  
engine.openGate('race1')`

For further details, check out the [example script](https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/race.py).

While developing this strategy I [wrote a benchmark](https://github.com/PortSwigger/turbo-intruder/tree/master/resources/examples/race-benchmark.py) to ensure it was actually having the desired effect. This repeatedly sent a batch of five requests over consumer-grade broadband to a public website and measured how close together the first and second requests hit the server.

Using the basic five-thread approach caused an average difference of 2.7ms (0.0027 seconds). Ensuring every TCP connection was fully established before sending any requests reduced that window to 1.4ms, and the last-byte technique squeezed it to a tiny 0.7ms - making it roughly twice as effective at triggering [race conditions](/web-security/race-conditions). 

I also added support for [per-chunk callbacks](https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/partialReadCallback.py), for when you have a race condition that requires reading information from the server mid-attack like in [LFI with PHPInfo Assistance](https://insomniasec.com/downloads/publications/LFI%20With%20PHPInfo%20Assistance.pdf).

### Racing reCAPTCHA

Shortly after this, I was asked to do a security audit of PortSwigger's self-registration feature, which we were introducing just ahead of the [Web Security Academy](https://portswigger.net/web-security) launch.

Users are supposed to be limited to registering one account per email address, which makes registration a potential target for a Time-of-check Time-of-use ([TOCTOU](https://cwe.mitre.org/data/definitions/367.html)) exploit. But there was a catch - the form was protected with reCAPTCHA, and everyone knows you can only use a valid reCAPTCHA solution once, right? Well, I tried anyway and it turned out you can use it a few times if you go fast enough.

This is particularly surprising thanks to the design of reCAPTCHA, where users don't directly connect to the server that validates the solution token. When you perform this attack, you're actually forcing the target website to trigger the race condition on your behalf:

`Turbo Intruder <-> Target Website <-> Google reCAPTCHA`

I considered giving this a fancy label like 'second order race condition'. However, in this age of reverse proxies and load-balancer chains most race conditions are 'second order' to some extent.

### Uncoordinated Disclosure

After finding the vulnerability, we immediately deployed a workaround to patch it on our website and reported the issue to Google, with a proof of concept showing the Target Website <-> Google reCAPTCHA race condition. [In the past](https://www.skeletonscribe.net/2016/08/reviewing-bug-bounties-hackers.html) I've had numerous great experiences with Google's security team, but this time was fated to be different.

Google requested a video, and when asked why the proof of concept wasn't sufficient replied "_Please share a video Poc as we need the same while contacting the relevant team._ "

This wasn't a great sign, but I eventually provided a video, and restated that I found this vulnerability on a live website. Google then politely declared the issue was imaginary, saying they "_don't think this attack is plausible in the wild_ " due to "_latency between the 3rd party server, the attacker and us, while also taking into account the 3rd party's server's workload and concurrency_ ". 

Rather than waste further time and energy arguing with Google about a moderate severity finding, I opted for public disclosure. This vulnerability affects almost all websites using reCAPTCHA - for my example target I chose Reddit as it's a well known target for spammers, and the account-registration process is reCAPTCHA protected. Reddit kindly agreed I could publish a video of the attack in action:

Video tags are not supported by your browser.

The obvious impact is that you can now register three times as many spam accounts for each solved captcha, potentially tripling your spam-rate. This could easily be chained with mechanical turk style services.

The second, more interesting implication is that on other sites this may enable exploitation of race conditions in thread-unsafe code that's protected by reCAPTCHA - for example, posting reviews or voting.

Hopefully this post will help persuade someone at Google that this attack is actually plausible, and should be fixed. Till then, if you're using reCAPTCHA, you'll need to manually secure it by locking/synchronising on the g-recaptcha-response token. Depending on your own application architecture this may be impossible, and you'll have to wait for Google to fix it.

[ race condition ](/research/race-condition) [ turbo intruder ](/research/turbo-intruder)

[Back to all articles](/research/articles)

## Related Research

### [ Introducing HTTP Anomaly Rank 11 November 2025 Introducing HTTP Anomaly Rank ](/research/introducing-http-anomaly-rank) ### [ WebSocket Turbo Intruder: Unearthing the WebSocket Goldmine 17 September 2025 WebSocket Turbo Intruder: Unearthing the WebSocket Goldmine ](/research/websocket-turbo-intruder-unearthing-the-websocket-goldmine) ### [ The single-packet attack: making remote race-conditions 'local' 18 October 2023 The single-packet attack: making remote race-conditions 'local' ](/research/the-single-packet-attack-making-remote-race-conditions-local) ### [ How to build custom scanners for web security research automation 03 October 2023 How to build custom scanners for web security research automation ](/research/how-to-build-custom-scanners-for-web-security-research-automation)

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
