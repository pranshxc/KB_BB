---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-01_using-hackability-to-uncover-a-chrome-infoleak.md
original_filename: 2022-09-01_using-hackability-to-uncover-a-chrome-infoleak.md
title: Using Hackability to uncover a Chrome infoleak
category: documents
detected_topics:
- xss
- ssrf
- csrf
- oauth
- sqli
- command-injection
tags:
- imported
- documents
- xss
- ssrf
- csrf
- oauth
- sqli
- command-injection
language: en
raw_sha256: fe15889406bcfd15de9459f3f9811b2f8e8f21106d35fec489ec7e591565349f
text_sha256: 9e027b7107c213d7eb54fc79f67d7e21e3c2b1c15e0f23aa59dc369032f3e684
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Using Hackability to uncover a Chrome infoleak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-01_using-hackability-to-uncover-a-chrome-infoleak.md
- Source Type: markdown
- Detected Topics: xss, ssrf, csrf, oauth, sqli, command-injection
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `fe15889406bcfd15de9459f3f9811b2f8e8f21106d35fec489ec7e591565349f`
- Text SHA256: `9e027b7107c213d7eb54fc79f67d7e21e3c2b1c15e0f23aa59dc369032f3e684`


## Content

---
title: "Using Hackability to uncover a Chrome infoleak"
page_title: "Using Hackability to uncover a Chrome infoleak | PortSwigger Research"
url: "https://portswigger.net/research/using-hackability-to-uncover-a-chrome-infoleak"
final_url: "https://portswigger.net/research/using-hackability-to-uncover-a-chrome-infoleak"
authors: ["Gareth Heyes (@garethheyes)"]
programs: ["Google"]
bugs: ["SOP bypass"]
bounty: "2,000"
publication_date: "2022-09-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2230
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

# Using Hackability to uncover a Chrome infoleak

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fusing-hackability-to-uncover-a-chrome-infoleak&text=Using+Hackability+to+uncover+a+Chrome+infoleak%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fusing-hackability-to-uncover-a-chrome-infoleak)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fusing-hackability-to-uncover-a-chrome-infoleak)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fusing-hackability-to-uncover-a-chrome-infoleak)
  * [ ](mailto:?subject=Using+Hackability+to+uncover+a+Chrome+infoleak&body=Using+Hackability+to+uncover+a+Chrome+infoleak%0A%0AI%27ve+been+hacking+browsers+for+over+15+years+and+one+of+the+challenges+I+set+myself+was+to+find+a+SOP+bypass+or+info+leak+in+every+major+browser.+Chrome+was+the+last+browser+standing%E2%80%A6until+now.+This+p%0A%0Ahttps://portswigger.net/research/using-hackability-to-uncover-a-chrome-infoleak)
  * [ ](/research/rss)

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

  * **Published:** Thursday, 1 September 2022 at 13:00 UTC

  * **Updated:** Thursday, 1 September 2022 at 13:32 UTC

  * 

![An illustration showing nested iframes with the inner most frame showing arrows outwards](/cms/images/4c/fd/41fd-article-uncover_a_chrome_infoleak_blog-article.jpg)

I've been hacking browsers for over 15 years and one of the challenges I set myself was to find a [SOP](/web-security/cors/same-origin-policy) bypass or info leak in every major browser. Chrome was the last browser standing…until now. This post will walk you through how I exploited a flaw that had been buried for nearly 5 years.

It all started when one of our Academy labs on [dangling markup](https://portswigger.net/web-security/cross-site-scripting/dangling-markup) injection stopped working. I've blogged about this previously which led to a [CSP bypass](https://portswigger.net/research/bypassing-csp-with-dangling-iframes). The technique involves setting an iframe location to about:blank which enables you to read the name property of the cross domain window. Normally you wouldn't be allowed to do this because cross domain windows are protected by [Same Origin Policy (SOP)](https://portswigger.net/web-security/cors/same-origin-policy). SOP is a browser feature that prevents different websites from reading data off each other, for example facebook.com from reading data from google.com.

Bypassing [CSP](/web-security/cross-site-scripting/content-security-policy) was great but I thought there could be more vulnerabilities to find as lots of properties were being leaked when the about:blank location was set. The first step was to use my [Hackability Inspector](https://portswigger-labs.net/hackability/inspector/?html=%3Ciframe%20src=%22//subdomain1.portswigger-labs.net/hackability/inspector?html=%3Ciframe%20src=/%3E%22%20id=x%3E) \- a security-focused enumerator. I added an iframe to a different domain which also contained another iframe. Next, in the main inspector window I set the location of the subframe on the cross domain window:

`[x.contentWindow[0].location='about:blank';](https://portswigger-labs.net/hackability/inspector/?input=x.contentWindow\[0\].location=%27about:blank%27;undefined&html=%3Ciframe%20src=%22//subdomain1.portswigger-labs.net/hackability/inspector?html=%3Ciframe%20src=/%3E%22%20id=x%3E)`

Then once I had set the location I inspected the cross domain window, I changed the input of the main inspector window to inspect the cross domain iframe window and hit return:

`x.contentWindow[0]`

![A screenshot showing inspection of a iframe cross origin window](/cms/images/9e/ec/8810-article-screenshot-of-inspector-investigating-iframe.png)

Look at all those properties! There must be some data leaking somewhere. I scrolled down the list of properties but there were too many. So I started filtering by properties I knew contained interesting information. I found I could access the document object:

`x.contentWIndow[0].document`

I continued filtering for known properties like document.URL which was set to "about:blank" obviously no good. Then I remembered the baseURI property and filtered for it and to my delight it contained cross domain information:

![A screenshot showing document.baseURI leaking a cross origin URL](/cms/images/08/c1/65f5-article-screenshot-of-infoleak.png)

This property contained information about the full URL and you could get that from a different subdomain. Imagine attachments.example.com could read the entire URL of [oauth](/web-security/oauth).example.com and steal OAuth tokens provided they have at least one iframe and was frameable. I confirmed that if the external URL was modified with hash or query string parameters they could be read from the different subdomain and decided to report it to Google.

Google investigated the issue after I'd simplified my proof of concept and found the baseURI problem was known since 2017:

` // TODO(tkent): Referring to ParentDocument() is not correct. See  
// [crbug.com/751329](https://bugs.chromium.org/p/chromium/issues/detail?id=751329).  
if (Document* parent = ParentDocument())  
return parent->BaseURL();`

The baseURI property was reporting an incorrect URL but nobody had managed to demonstrate a security vulnerability until now. Using a framed page with an existing iframe I could use this bug to obtain cross domain information. Google awarded me $2000 for this vulnerability.

[Proof of concept](https://subdomain2.portswigger-labs.net/chrome-infoleak-sWpsDfkg9102/)

### Conclusion

This issue demonstrates that minor bugs such as incorrectly assigned properties can be chained together with existing techniques to expose cross domain information. When enumerating it's a good idea to look for properties that contain external URLs as they can lead to cross domain [information disclosure](/web-security/information-disclosure).

### Timeline

2022-06-16 9:37 AM GMT+1 - Reported to Google  
2022-07-08 7:15 PM GMT+1 - Google patches issue  
2022-08-18 - Google awards $2000 bounty for this issue  
2022-08-30 - Chrome released  
2022-09-01 14:00 PM GMT - Blog post published

[ Browser hacking ](/research/browser-hacking) [ Infoleak ](/research/infoleak) [ SOP ](/research/sop) [ browser security ](/research/browser-security)

[Back to all articles](/research/articles)

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
