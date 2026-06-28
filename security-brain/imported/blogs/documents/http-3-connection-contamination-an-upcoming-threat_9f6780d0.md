---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-19_http3-connection-contamination-an-upcoming-threat.md
original_filename: 2022-10-19_http3-connection-contamination-an-upcoming-threat.md
title: 'HTTP/3 connection contamination: an upcoming threat?'
category: documents
detected_topics:
- ssrf
- xss
- csrf
- saml
- sqli
- command-injection
tags:
- imported
- documents
- ssrf
- xss
- csrf
- saml
- sqli
- command-injection
language: en
raw_sha256: 9f6780d07584308cb10d115c123625462eb4cd7ec1dde493efa2e7f57fdc903b
text_sha256: 52fb227ec47e5c960423aa6f6c7678b7feaf78bad58e2ff5a532752f20417634
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# HTTP/3 connection contamination: an upcoming threat?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-19_http3-connection-contamination-an-upcoming-threat.md
- Source Type: markdown
- Detected Topics: ssrf, xss, csrf, saml, sqli, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `9f6780d07584308cb10d115c123625462eb4cd7ec1dde493efa2e7f57fdc903b`
- Text SHA256: `52fb227ec47e5c960423aa6f6c7678b7feaf78bad58e2ff5a532752f20417634`


## Content

---
title: "HTTP/3 connection contamination: an upcoming threat?"
page_title: "HTTP/3 connection contamination: an upcoming threat? | PortSwigger Research"
url: "https://portswigger.net/research/http-3-connection-contamination"
final_url: "https://portswigger.net/research/http-3-connection-contamination"
authors: ["James Kettle (@albinowax)"]
bugs: ["HTTP connection contamination"]
publication_date: "2022-10-19"
added_date: "2022-10-21"
source: "pentester.land/writeups.json"
original_index: 2017
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

# HTTP/3 connection contamination: an upcoming threat?

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhttp-3-connection-contamination&text=HTTP%2F3+connection+contamination%3A+an+upcoming+threat%3F%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhttp-3-connection-contamination)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhttp-3-connection-contamination)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fhttp-3-connection-contamination)
  * [ ](mailto:?subject=HTTP%2F3+connection+contamination%3A+an+upcoming+threat%3F&body=HTTP%2F3+connection+contamination%3A+an+upcoming+threat%3F%0A%0AI+recently+documented+a+dangerous+reverse-proxy+behaviour+called+first-request+routing%2C+which+enables+host-header+attacks+on+back-end+systems.+In+this+post%2C+I%27ll+show+how+first-request+routing+also+en%0A%0Ahttps://portswigger.net/research/http-3-connection-contamination)
  * [ ](/research/rss)

![James Kettle](/content/images/profiles/callout_james_kettle_112px.png)

### [James Kettle](/research/james-kettle)

Director of Research

[@albinowax](https://twitter.com/albinowax)

  * **Published:** Wednesday, 19 October 2022 at 13:28 UTC

  * **Updated:** Wednesday, 2 November 2022 at 14:49 UTC

  * 

I [recently documented](https://portswigger.net/research/browser-powered-desync-attacks#anomalies) a dangerous reverse-proxy behaviour called first-request routing, which enables [host-header attacks](https://portswigger.net/web-security/host-header) on back-end systems. In this post, I'll show how first-request routing also enables a client-side, browser-based attack called HTTP connection contamination. This technique works on systems running HTTP/2, and is likely to become a greater threat with the advent of HTTP/3. The video above is a five minute presentation explaining this threat from a high level, and the rest of this post covers the full technical details. 

Web browsers have a shiny feature called [HTTP connection coalescing](https://daniel.haxx.se/blog/2016/08/18/http2-connection-coalescing), which lets them reuse a single HTTP/2+ connection for requests going to different websites, provided that the sites resolve to the same IP address and use a TLS certificate valid for both hostnames.

First-request routing is a dangerous reverse-proxy behaviour where the proxy analyses the first request on a connection to work out which back-end end to route it to, and then sends all subsequent requests on that connection to the same back-end.

Connection coalescing and first-request routing do not play well together. For example, imagine secure.example.com and wordpress.example.com are both sat behind a reverse proxy using a certificate valid for *.example.com:

`$ nslookup wordpress.example.com  
52.16.179.7 // reverse proxy that supports HTTP/2 and does first-request routing  
  
$ nslookup secure.example.com  
52.16.179.7 // same reverse proxy  
  
$ openssl s_client -connect x.portswigger-labs.net:443  
subject=/CN=*.example.com // wildcard TLS certificate  
`

If a browser tries to send a request to wordpress.example.com followed by secure.example.com, browser connection coalescing will force both requests down a single connection to the front-end. First-request routing will result in the request to secure.example.com incorrectly being routed to the WordPress back-end. This means that if you find [XSS](/web-security/cross-site-scripting) on wordpress.example.com, you can use it to compromise secure.example.com!

`// create HTTP/2+ connection  
fetch('https://wordpress.example.com/', {credentials: 'include'})  
  
// connection coalescing will force this down the same connection...  
// ...leading to the front-end misrouting it to WordPress  
// the browser thinks our injected JS is coming from secure.example.com  
// exposing saved passwords, cookies, etc.  
location='https://secure.example.com/plugin/x?q=<script>stealPasswords()'`

You can explore connection coalescing for yourself by using the Timing graph under the Network tab in Chrome's developer tools (or using WireShark if you're a masochist). Issue request pairs using fetch() and see if the graph shows time spent on 'Initial connection' for the second request, and if the Connection ID column matches:

`fetch('//sub1.hackxor.net/', {mode: 'no-cors', credentials: 'include'}).then(()=>{ fetch('//sub2.hackxor.net/', {mode: 'no-cors', credentials: 'include'}) })`

![](/cms/images/d7/ca/b7cf-article-screenshot_2022-10-17_at_15.17.28.png)

I haven't invested the time required to explore this threat in depth or scan for it in the wild as I believe it's currently rare for two reasons. Firstly, first-request routing is relatively uncommon and HTTP/2's implementation complexity means there's only a small pool of unique HTTP/2 servers relative to HTTP/1.1. Secondly, connection coalescing means HTTP/2 servers performing first-request routing may intermittently break for genuine visitors, so the owners may end up fixing the vulnerability without attacker encouragement. 

That said, it's not all bad news for attackers. HTTP/3 proposes [removing the requirement for an IP address match](https://www.rfc-editor.org/rfc/rfc9114.html#name-connection-reuse), which will expose everyone with a front-end that uses first-request routing and has a certificate valid for multiple hosts.

This also creates a second risk which isn't related to first-request routing - it means a compromised server with a wildcard certificate no longer requires an MITM to exploit. In effect, this greatly increases the pool of malicious actors who could profit from it.

To avoid these risks before they become a reality, ensure your reverse proxies don't perform first-request routing. You can test for this manually in Repeater by enabling HTTP/1 and HTTP/2 connection reuse, and also scan for it using the 'Connection-State' attack in [HTTP Request Smuggler](https://github.com/PortSwigger/http-request-smuggler). Also, be aware that while wildcard TLS certificates have never been ideal, HTTP/3 means a compromised server with a wildcard certificate can now be used to attack sibling domains without an active MITM.

These new threats continue the ongoing trend of web infrastructure descending into a heavily intertwined mess where a weakness in any individual site has numerous non-obvious knock-on effects on the security of the overall system. It'll be interesting to see how these risks play out in practice. 

[Back to all articles](/research/articles)

## Related Research

### [ 05 February 2026 ](/research/top-10-web-hacking-techniques-of-2025) ### [ 06 January 2026 ](/research/top-10-web-hacking-techniques-of-2025-nominations-open) ### [ The Fragile Lock: Novel Bypasses For SAML Authentication  10 December 2025 The Fragile Lock: Novel Bypasses For SAML Authentication ](/research/the-fragile-lock) ### [ Introducing HTTP Anomaly Rank 11 November 2025 Introducing HTTP Anomaly Rank ](/research/introducing-http-anomaly-rank)

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
