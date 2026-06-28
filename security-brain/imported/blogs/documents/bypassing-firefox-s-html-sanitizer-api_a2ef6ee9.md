---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-29_bypassing-firefoxs-html-sanitizer-api.md
original_filename: 2022-06-29_bypassing-firefoxs-html-sanitizer-api.md
title: Bypassing Firefox's HTML Sanitizer API
category: documents
detected_topics:
- ssrf
- xss
- csrf
- sqli
- command-injection
- file-upload
tags:
- imported
- documents
- ssrf
- xss
- csrf
- sqli
- command-injection
- file-upload
language: en
raw_sha256: a2ef6ee9a2f02aa8379654726ae83fef31f28169c0de3906bcf62e6ce835f2c2
text_sha256: 983e269da7e83d2c46d74987887322a9b21deed962538523d61345e4d5d3fd17
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Firefox's HTML Sanitizer API

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-29_bypassing-firefoxs-html-sanitizer-api.md
- Source Type: markdown
- Detected Topics: ssrf, xss, csrf, sqli, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `a2ef6ee9a2f02aa8379654726ae83fef31f28169c0de3906bcf62e6ce835f2c2`
- Text SHA256: `983e269da7e83d2c46d74987887322a9b21deed962538523d61345e4d5d3fd17`


## Content

---
title: "Bypassing Firefox's HTML Sanitizer API"
page_title: "Bypassing Firefox's HTML Sanitizer API | PortSwigger Research"
url: "https://portswigger.net/research/bypassing-firefoxs-html-sanitizer-api"
final_url: "https://portswigger.net/research/bypassing-firefoxs-html-sanitizer-api"
authors: ["Gareth Heyes (@garethheyes)"]
programs: ["Mozilla"]
bugs: ["XSS"]
publication_date: "2022-06-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2497
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

# Bypassing Firefox's HTML Sanitizer API

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-firefoxs-html-sanitizer-api&text=Bypassing+Firefox%27s+HTML+Sanitizer+API%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-firefoxs-html-sanitizer-api)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-firefoxs-html-sanitizer-api)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-firefoxs-html-sanitizer-api)
  * [ ](mailto:?subject=Bypassing+Firefox%27s+HTML+Sanitizer+API&body=Bypassing+Firefox%27s+HTML+Sanitizer+API%0A%0AThe+HTML+Sanitizer+is+a+great+new+API+that+allows+web+developers+to+filter+untrusted+HTML+natively+in+the+browser+rather+than+use+a+JavaScript+library+such+as+DOM+Purify.+Microsoft+created+a+similar+A%0A%0Ahttps://portswigger.net/research/bypassing-firefoxs-html-sanitizer-api)
  * [ ](/research/rss)

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

  * **Published:** Wednesday, 29 June 2022 at 14:00 UTC

  * **Updated:** Monday, 4 July 2022 at 07:46 UTC

  * 

![A picture of code flowing through a filter](/cms/images/91/4b/e6a7-article-firefox_html_sanitizer_blog_article.png)

The [HTML Sanitizer](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Sanitizer_API) is a great new API that allows web developers to filter untrusted HTML natively in the browser rather than use a JavaScript library such as [DOM Purify](https://github.com/cure53/DOMPurify). Microsoft created a similar API called toStaticHTML in 2008 for Internet Explorer but it was [riddled](https://web.archive.org/web/20101025032152/http://archives.neohapsis.com/archives/fulldisclosure/2010-08/0179.html) with [holes](https://blog.watchfire.com/wfblog/2012/07/tostatichtml-the-second-encounter-cve-2012-1858-html-sanitizing-information-disclosure-introduction-t.html) and wasn't widely adopted or standardised. Hopefully the Sanitizer will have more success. 

The advantages of using a native browser feature are obvious; if the browser is used to filter HTML then it can use its own parsers to ensure the untrusted HTML is filtered consistently. 

However, there can be a disagreement in what the Sanitizer thinks is safe compared to the actual reality of the filtered HTML. One such example is with SVG "use" elements; we've [shown in the past that "use" elements can be used to execute arbitrary JavaScript](https://portswigger.net/research/new-xss-vectors) by using data URLs. 

The Sanitizer prevents these attacks by blocking SVG imports using both data URLs and relative URLs. However, it allowed SVG imports from absolute URLs, provided they were the same origin. This means if the target site allowed a file upload of an SVG file and protected it by forcing a download using Content-Disposition: attachment, it would still be possible to execute arbitrary JavaScript. 

`<svg><use href="//portswigger-labs.net/use_element/upload.php#x"/></svg>`

[Proof of concept](https://portswigger-labs.net/xss/xss.php?x=%3Csvg%3E%3Cuse%20href=%22//portswigger-labs.net/use_element/upload.php%23x%22/%3E%3C/svg%3E)

Here's the result of the untrusted HTML being filtered incorrectly by the Sanitizer:

Input:

`<svg><use href="//portswigger-labs.net/use_element/upload.php#x" />`

Output:

`<div><svg><use href="//portswigger-labs.net/use_element/upload.php#x"></use></svg></div>`

### Conclusion

Browser APIs for sanitizing HTML are a good idea as the browser is in a better position to filter the HTML correctly however this doesn't mean they are a foolproof mechanism to prevent malicious HTML from sneaking past. As with any filter, a feature like this requires a large amount of testing to ensure correct filtering of malicious HTML.

### Note

Please note this is an experimental API and isn't widely supported yet.

### Timeline

2022-02-25 09:42 PST - Reported bug to Mozilla  
2022-04-29 15:03 PDT - Fixed  
2022-06-28 - Firefox 102.0 released  
2022-06-29 15:00 PM GMT - Published this post

[ XSS ](/research/cross-site-scripting-research) [ filter ](/research/filter) [ firefox ](/research/firefox)

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
