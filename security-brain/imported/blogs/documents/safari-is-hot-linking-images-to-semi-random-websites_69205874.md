---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-31_safari-is-hot-linking-images-to-semi-random-websites.md
original_filename: 2022-10-31_safari-is-hot-linking-images-to-semi-random-websites.md
title: Safari is hot-linking images to semi-random websites
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
raw_sha256: 69205874f4df7bbe62293d3d16be577421e2e3306a57feb53aa56f1bafdf9b63
text_sha256: 28909ffe8facc8cab5ceb301eb520d78a69dcaed32ce1805a04ed1a39102be8b
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Safari is hot-linking images to semi-random websites

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-31_safari-is-hot-linking-images-to-semi-random-websites.md
- Source Type: markdown
- Detected Topics: ssrf, xss, csrf, sqli, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `69205874f4df7bbe62293d3d16be577421e2e3306a57feb53aa56f1bafdf9b63`
- Text SHA256: `28909ffe8facc8cab5ceb301eb520d78a69dcaed32ce1805a04ed1a39102be8b`


## Content

---
title: "Safari is hot-linking images to semi-random websites"
page_title: "Safari is hot-linking images to semi-random websites | PortSwigger Research"
url: "https://portswigger.net/research/safari-is-hot-linking-images-to-semi-random-websites"
final_url: "https://portswigger.net/research/safari-is-hot-linking-images-to-semi-random-websites"
authors: ["Gareth Heyes (@garethheyes)"]
programs: ["Apple"]
bugs: ["Browser hacking", "XSS"]
publication_date: "2022-10-31"
added_date: "2022-11-01"
source: "pentester.land/writeups.json"
original_index: 1965
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

# Safari is hot-linking images to semi-random websites

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fsafari-is-hot-linking-images-to-semi-random-websites&text=Safari+is+hot-linking+images+to+semi-random+websites%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fsafari-is-hot-linking-images-to-semi-random-websites)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fsafari-is-hot-linking-images-to-semi-random-websites)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fsafari-is-hot-linking-images-to-semi-random-websites)
  * [ ](mailto:?subject=Safari+is+hot-linking+images+to+semi-random+websites&body=Safari+is+hot-linking+images+to+semi-random+websites%0A%0AEvery+image+is+potentially+a+URL+on+Safari%2C+thanks+to+over-enthusiastic+OCR+\(Optical+Character+Recognition\).+This+means+you+can+link+any+image+to+an+external+website+-+and+Safari+might+already+be+send%0A%0Ahttps://portswigger.net/research/safari-is-hot-linking-images-to-semi-random-websites)
  * [ ](/research/rss)

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

  * **Published:** Monday, 31 October 2022 at 14:58 UTC

  * **Updated:** Friday, 3 May 2024 at 08:12 UTC

  * 

![Graphic showing the quick look menu on the Amazon logo](/cms/images/76/df/bf6c-article-article.png)  

  

Every image is potentially a URL on Safari, thanks to over-enthusiastic OCR (Optical Character Recognition). This means you can link any image to an external website - and Safari might already be sending your users to unintended destinations.

This all started with the mysterious arrival of 'zon.com' on our company homepage. Ric (one of our designers) noticed some suspicious behaviour on our website. He came over to us, loaded our homepage on Safari and hovered over the Amazon logo. To our shock, it showed a link to "Zon.com". His first questions to us - "Have we been hacked? Why on earth is this URL showing on our homepage?!"

![Animation showing quick look menu with the Amazon logo](/cms/images/8e/78/9738-article-showing-zon.com.gif)

After some investigation with dev tools we didn't find anything out of the ordinary. So I loaded up Photoshop and made an image that had amazon.com in it. I loaded up Safari and hovered over the image, then a "quick look" menu popped up and gave a link to amazon.com!

This is a Safari feature, it attempts to parse URLs in images. What was happening was because the Amazon logo had an arrow underneath, it was breaking the OCR - this then resulted in the URL being parsed as Zon.com. This is complete madness. Any image you upload to any website can now embed a URL on Safari!

Naturally, we then started investigating what kind of URLs it would recognise. Normally I'd fuzz the URLs but this was quite difficult because you had to hover over the image and click a menu, which made fuzzing awkward. So, I decided to use Photoshop and do some manual testing. The first thing I tried was to see if protocols were recognised - it seemed to allow http and https, but not javascript or file. I then tested to see if it would allow query string parameters. Of course it did. So you could embed a [XSS](/web-security/cross-site-scripting) payload inside an image, and Safari would happily parse it and allow you to click it. Although JavaScript URLs didn't work, I started to look for ways to bypass this restriction.

The first thing I did was to try and make the JavaScript URL look like a protocol:

`javascript://alert(1).com`

This was parsed and the quick look menu showed, but didn't allow you to click the URL. I then tried to make the JS URL look more like a regular URL:

`http://javascript://hackvertor.co.uk`

This also failed, but then I tried this:

`http://javascript:1337//location.href=123`

That seemed to be clickable but I couldn't find the server message, and the URL bar was showing the JavaScript URL. What was happening? Safari was visiting a HTTP URL, but stripping the protocol which left the JavaScript protocol. That means when you refresh, the JavaScript URL will be activated. After many more attempts I optimised the payload:

![JavaScript URL image](/cms/images/09/d7/f5c9-article-javascript-url.png)

When you hover over the above image, Safari will allow you to click it in the quick look menu. When you've clicked the link you get a server error message, but hitting refresh will execute the JavaScript in the context of "safari-resource". There is a caveat however - you need to enable JavaScript in the "Smart search field" in the developer menu. Caveat aside though, this is still one crazy feature as I'm pretty sure you don't want any image to be able to embed JavaScript URLs or link to random websites!

![Animated GIF showing JavasCript injection](/cms/images/57/89/8027-article-showing-javascript-injection-from-image.gif)

Anyway, I'm off to register Zon.com.

[ Hot-linking ](/research/hot-linking) [ Safari ](/research/safari)

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
