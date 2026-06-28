---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-24_responsible-denial-of-service-with-web-cache-poisoning.md
original_filename: 2019-10-24_responsible-denial-of-service-with-web-cache-poisoning.md
title: Responsible denial of service with web cache poisoning
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
raw_sha256: 1925e15e0283c3675bcb52ba543d59c8d8e9217c3b93e27781e89c7cc169b4d9
text_sha256: f4bcafbbe4f5b3837f841a0899710b6d6f26bc1e81b60c2a6f57866cbafa3717
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Responsible denial of service with web cache poisoning

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-24_responsible-denial-of-service-with-web-cache-poisoning.md
- Source Type: markdown
- Detected Topics: ssrf, xss, csrf, sqli, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `1925e15e0283c3675bcb52ba543d59c8d8e9217c3b93e27781e89c7cc169b4d9`
- Text SHA256: `f4bcafbbe4f5b3837f841a0899710b6d6f26bc1e81b60c2a6f57866cbafa3717`


## Content

---
title: "Responsible denial of service with web cache poisoning"
page_title: "Responsible denial of service with web cache poisoning | PortSwigger Research"
url: "https://portswigger.net/research/responsible-denial-of-service-with-web-cache-poisoning"
final_url: "https://portswigger.net/research/responsible-denial-of-service-with-web-cache-poisoning"
authors: ["James Kettle (@albinowax)"]
programs: ["Tesla", "HackerOne", "Deliveroo", "Bitbucket", "Paypal", "Meta / Facebook", "Twitter"]
bugs: ["DoS", "Web cache poisoning", "CPDoS"]
bounty: "22,300"
publication_date: "2019-10-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4974
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

# Responsible denial of service with web cache poisoning

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fresponsible-denial-of-service-with-web-cache-poisoning&text=Responsible+denial+of+service+with+web+cache+poisoning%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fresponsible-denial-of-service-with-web-cache-poisoning)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fresponsible-denial-of-service-with-web-cache-poisoning)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fresponsible-denial-of-service-with-web-cache-poisoning)
  * [ ](mailto:?subject=Responsible+denial+of+service+with+web+cache+poisoning&body=Responsible+denial+of+service+with+web+cache+poisoning%0A%0AIn+this+post%2C+I%27ll+tell+the+story+of+how+I+came+to+love+denial+of+service+attacks%2C+and+show+you+how+to+use+web+cache+poisoning+to+take+down+websites+with+a+single+request+while+earning+bug+bounties+al%0A%0Ahttps://portswigger.net/research/responsible-denial-of-service-with-web-cache-poisoning)
  * [ ](/research/rss)

![James Kettle](/content/images/profiles/callout_james_kettle_112px.png)

### [James Kettle](/research/james-kettle)

Director of Research

[@albinowax](https://twitter.com/albinowax)

  * **Published:** Thursday, 24 October 2019 at 12:13 UTC

  * **Updated:** Thursday, 14 November 2019 at 14:52 UTC

  * 
![](/cms/images/1d/a3/78f2eb8c05c6-article-responsible_denial_of_service_with_web_cache_poisoning_article.png)

In this post, I'll tell the story of how I came to love denial of service attacks, and show you how to use [web cache poisoning](/web-security/web-cache-poisoning) to take down websites with a single request while earning bug bounties along the way.

Denial of Service (DoS) attacks have a poor reputation. Historically, DoS used to be trivial - you could knock most sites offline using script-kiddie friendly tools like slowloris.pl. DoS attacks are also often conflated with DDoS attacks, which are near-impossible to truly fix. A line was drawn between a site being 'hacked', and merely being (D)DoS'd. As a result many hackers, myself included, regarded DoS vulnerabilities as lame. Of course 'availability' sits in the CIA triad and therefore CVSS, but that's just another reason why CVSS sucks, right? This was my perspective until a series of events spanning a year changed it.

While I was researching web cache poisoning, I noticed that you could use it for single-request, persistent DoS attacks, but didn't pay much attention until I found I could take out chunks of Tesla's website due to a WAF returning a cacheable "you have been blocked" page whenever it saw the text 'burpcollaborator.net' in a request: 

`GET /en_GB/roadster?dontpoisoneveryone=1 HTTP/1.1  
Host: www.tesla.com  
Any-Header: burpcollaborator.net  
  
HTTP/1.1 403 Forbidden  
  
Access Denied. Please contact waf@tesla.com`

For efficiency reasons the cache key only includes the highlighted values, so anyone who subsequently tried to access that URL would get a cache hit and receive the Access Denied response. The 'dontpoisoneveryone' parameter is crucial to proving that the attack is possible without actually causing site downtime. For a in-depth explanation of this technique, please refer to [Practical Web Cache Poisoning](https://portswigger.net/blog/practical-web-cache-poisoning).

This was a curious variation on a standard header-based attack, and would make a great example for my presentation, so I tentatively reported it and unexpectedly received a token $300 bounty.

Later on, after discovering, reporting, and publishing a critical cache poisoning exploit chain for Drupal, I realised www.hackerone.com was using Drupal all along - but they'd already applied the patch. While attempting to bypass the patch, I noticed the `X-Forwarded-Port` header could be used to persistently [poison a redirect](https://hackerone.com/reports/409370) with an invalid port, causing a timeout for everyone trying to access their site:

`GET /index.php?dontpoisoneveryone=1 HTTP/1.1  
Host: www.hackerone.com  
X-Forwarded-Port: 123  
  
HTTP/1.1 302 Found  
Location: https://www.hackerone.com:123/  
`

Video tags are not supported by your browser.  

I reported this mostly out of annoyance at missing my chance to apply the Drupal exploit, and received a surprising $2,500 bounty.

Shortly afterward, I was contacted by academic researchers Hoai Viet Nguyen and Luigi Lo Iacono who asked my advice on their foray into using web cache poisoning for DoS attacks. I offered some technical advice then politely suggested that denial of service attacks wasn't a topic worthy of serious research, but they wisely ignored me and kept on going.

Then, on Christmas eve, Deliveroo contacted me because someone had taken down their website with cache poisoning and due to some confusion they thought I was responsible.

Finally, while attempting a HTTP Desync attack on a target I can't name, I happened to use Burp Repeater's 'Paste URL as request' function, which creates a HTTP request from a URL and takes its `User-Agent` from the venerable Internet Explorer 9. This accidentally overwrote the cached page with a 'Please update your browser' response. I reported this, and received a eye-opening $7,500, which was actually more than I got for the desync attack.

At this point I'd earned over $10,000 by accidentally finding DoS vulnerabilities, and could no longer ignore the niggling idea that maybe some companies do care about DoS. In retrospect, this looks like a solid example of my [research-breadcrumb theory](https://portswigger.net/research/so-you-want-to-be-a-web-security-researcher#invent) in action. I dusted off [Param Miner](https://github.com/PortSwigger/param-miner), tuned the cache-poisoning detection to make it more sensitive if you toggle the 'twitchy cache poison' option, and set out to earn some bounties. Here are a few highlights:

On https://bitbucket.org, you could use `X-Forwarded-SSL` header to overwrite certain pages with a response saying 'Contradictory scheme headers', and also use `Transfer-Encoding` to overwrite arbitrary pages. This earned a $1,800 bounty:

![](/cms/images/0c/c2/2823560b957f-article-image_\(1\).png)

On https://paypal.com/, you could break core functionality by using an invalid `Transfer-Encoding` header to replace crucial JavaScript files from www.paypalobjects.com with the message '501 Not Implemented'. They patched this and [awarded a top-tier $9,700 bounty](https://hackerone.com/reports/622122).

My colleague Gareth Heyes spotted that you can DoS instagram for people using old browsers or a proxy, by using `Accept_Encoding: br` to force a brotli-encoded response. `Accept-Encoding` was in the cache key, but using an underscore made the cache miss it. This earned $500, doubled to $1,000 as it was donated.

Finally, you can deny access to core Twitter JavaScript files loaded from abs.twimg.com and ton.twimg.com by using the header `Range: bytes=cow` to cause a 400 response. They decided not to patch or pay out for this, so you can (carefully) use it for practise if you want. 

Other successful attacks used the `Accept`, `Upgrade`, `[Origin](https://nathandavison.com/blog/corsing-a-denial-of-service-via-cache-poisoning)`, and `Max-Forwards` headers. 

Most bug-bounty policies have text discouraging DoS attacks. However, if you look closely you'll see some of them actually forbid launching DoS attacks, rather than forbidding reporting DoS vulnerabilities. Web cache poisoning has a rare property in that it's often possible to make a proof of concept without actually launching an attack, provided you use a cache-buster.

That said, quite a few programs do have a blanket exclusion on reporting DoS vulnerabilities. I'd suggest that sufficiently mature programs think about their business requirements, and perhaps tweak their wording to merely exclude 'volumetric DoS' or 'computational DoS' reports.

Finally, the academic research mentioned earlier was actually published earlier this week - you can read it at <https://cpdos.org/>

[ web cache poisoning ](/research/web-cache-poisoning)

[Back to all articles](/research/articles)

## Related Research

### [ Gotta cache 'em all: bending the rules of web cache exploitation 08 August 2024 Gotta cache 'em all: bending the rules of web cache exploitation ](/research/gotta-cache-em-all) ### [ Web Cache Entanglement 05 August 2020 Web Cache Entanglement ](/research/web-cache-entanglement) ### [ Bypassing Web Cache Poisoning Countermeasures 05 October 2018 Bypassing Web Cache Poisoning Countermeasures ](/research/bypassing-web-cache-poisoning-countermeasures) ### [ Practical Web Cache Poisoning Redefining 'unexploitable' 09 August 2018 Practical Web Cache Poisoning Redefining 'unexploitable' ](/research/practical-web-cache-poisoning)

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
