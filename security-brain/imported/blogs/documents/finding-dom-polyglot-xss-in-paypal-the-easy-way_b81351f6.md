---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-30_finding-dom-polyglot-xss-in-paypal-the-easy-way.md
original_filename: 2021-06-30_finding-dom-polyglot-xss-in-paypal-the-easy-way.md
title: Finding DOM Polyglot XSS in PayPal the Easy Way
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
raw_sha256: b81351f69c473e50e6bcc435f7bc334985612fdef6f31185d2a0ee2fca92591e
text_sha256: 8075d9a8c4dde687db7b745f7d5cbcf0b8a415aabae7f041879045ad449b1442
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Finding DOM Polyglot XSS in PayPal the Easy Way

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-30_finding-dom-polyglot-xss-in-paypal-the-easy-way.md
- Source Type: markdown
- Detected Topics: xss, ssrf, csrf, sqli, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `b81351f69c473e50e6bcc435f7bc334985612fdef6f31185d2a0ee2fca92591e`
- Text SHA256: `8075d9a8c4dde687db7b745f7d5cbcf0b8a415aabae7f041879045ad449b1442`


## Content

---
title: "Finding DOM Polyglot XSS in PayPal the Easy Way"
page_title: "Finding DOM Polyglot XSS in PayPal the Easy Way | PortSwigger Research"
url: "https://portswigger.net/research/finding-dom-polyglot-xss-in-paypal-the-easy-way"
final_url: "https://portswigger.net/research/finding-dom-polyglot-xss-in-paypal-the-easy-way"
authors: ["Gareth Heyes (@garethheyes)"]
programs: ["Paypal"]
bugs: ["DOM XSS", "CSP bypass"]
publication_date: "2021-06-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3532
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

# Finding DOM Polyglot XSS in PayPal the Easy Way

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Ffinding-dom-polyglot-xss-in-paypal-the-easy-way&text=Finding+DOM+Polyglot+XSS+in+PayPal+the+Easy+Way%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Ffinding-dom-polyglot-xss-in-paypal-the-easy-way)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Ffinding-dom-polyglot-xss-in-paypal-the-easy-way)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Ffinding-dom-polyglot-xss-in-paypal-the-easy-way)
  * [ ](mailto:?subject=Finding+DOM+Polyglot+XSS+in+PayPal+the+Easy+Way&body=Finding+DOM+Polyglot+XSS+in+PayPal+the+Easy+Way%0A%0AIntroduction+Finding+DOM+XSS+can+be+tricky+when+it%27s+buried+in+thousands+of+lines+of+code.+We+recently+developed+DOM+Invader+to+help+tackle+this+using+a+combined+dynamic%2Bmanual+approach+to+vulnerabili%0A%0Ahttps://portswigger.net/research/finding-dom-polyglot-xss-in-paypal-the-easy-way)
  * [ ](/research/rss)

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

  * **Published:** Wednesday, 30 June 2021 at 16:47 UTC

  * **Updated:** Wednesday, 7 September 2022 at 09:04 UTC

  * 

![Shows a phone and open pad locks](/cms/images/94/b5/ee02-article-dom_invader_pp_page_article_image.png)  

## Introduction

Finding [DOM XSS](/web-security/cross-site-scripting/dom-based) can be tricky when it's buried in thousands of lines of code. We recently developed [DOM Invader](https://portswigger.net/blog/introducing-dom-invader) to help tackle this using a combined dynamic+manual approach to vulnerability discovery, and promptly found an interesting polyglot DOM XSS affecting PayPal. In this post, we'll take you through the discovery journey, and also show how to use unintended script gadgets to bypass an allow list based [CSP](/web-security/cross-site-scripting/content-security-policy).

First, we used Burp's embedded browser to navigate the site and inject the canary to see which sources and sinks were used on each of the pages. When we encountered some interesting sinks, we would then send probes of characters such as <>'" along with the canary and inspect the sink to see if they were allowed. It didn't take us long to find a page that was reflecting our probes in an insecure way. Normally this would be difficult as the reflection is invisible, but with DOM Invader it was easy.

![DOM Invader's Augmented DOM showing a sink on PayPal](/cms/images/c4/26/5c88-article-image1-resized.png)  

As you can see in the screenshot above our canary is being reflected inside an id attribute. If we send a double quote we can see how the value reaches the sink. But when sending a double quote, the screen goes blank. However, if we escape the double quote, then the site will not break and we can see it reaches the sink:

![DOM Invader's Augmented DOM showing an unescaped double quote](/cms/images/09/11/563c-article-image2-resized.png)

In HTML, backslash has no effect on the double quote - so we appear to have an XSS vulnerability. We need to confirm this though by injecting other characters which will cause JavaScript to execute. After multiple probes at this vulnerability, we noticed that the value injected had to be a valid CSS selector. So we came up with the following vector:

`burpdomxss input[value='\">\<iframe srcdoc=&lt;script&gt;alert(document.domain)&llt;/script&gt;>\"']`

This didn't work initially because of the CSP - but when we disabled this in Burp, we got the alert. We then reported this to PayPal on HackerOne, along with the instructions to disable CSP. To our surprise, we got the response from a HackerOne triager that: 

> After review, there doesn’t seem to be any security risk and/or security impact as a result of the behavior you are describing.

So apparently you need a CSP bypass to report XSS on PayPal assets. We didn't agree with this assessment and other companies like Google will reward you for XSS without a CSP bypass. But this is PortSwigger, and we don't stop there. We then began to look for ways to bypass PayPal's policy.

## Bypassing CSP on PayPal

First we studied the CSP and noticed a few weak parts. In the script-src directive they were allowing certain domains like *.paypalobjects.com and *.paypal.com. They also included the 'unsafe-eval' directive which would allow the use of eval, the Function constructor and other JavaScript execution sinks:

`base-uri 'self' https://*.paypal.com; connect-src 'self' https://*.paypal.com https://*.paypalobjects.com https://*.google-analytics.com https://nexus.ensighten.com https://*.algolianet.com https://*.algolia.net https://insights.algolia.io https://*.qualtrics.com; default-src 'self' https://*.paypal.com https://*.paypalobjects.com; form-action 'self' https://*.paypal.com; frame-src 'self' https://*.paypal.com https://*.paypalobjects.com https://www.youtube-nocookie.com https://*.qualtrics.com https://*.paypal-support.com; img-src 'self' https: data:; object-src 'none'; script-src 'nonce-RGYH2N1hP59U4+QwLcOaI5GgHbP19yxg1MEmKXc883wiDeAj' 'self' https://*.paypal.com https://*.paypalobjects.com 'unsafe-inline' 'unsafe-eval'; style-src 'self' block-all-mixed-content;; report-uri https://www.paypal.com/csplog/api/log/csp`

Looking at the policy, the allow list and 'unsafe-eval' were probably the best targets to bypass the CSP. So we added those domains in the Burp Suite scope. You can use regexes in the scope which is super handy. Our scope looked like this:

`^(?:.*[.]paypal(?:objects)?.com)$`

Burp allows you to pick specific protocols in the scope - and because the policy had the 'block-all-mixed-content' directive, we only selected the HTTPS protocol.

After studying the CSP, we opened the embedded browser in Burp and began browsing the site manually - in order to pick the targets which had a lot of JavaScript assets. Once we had collected a lot of proxy history, we then used Burp's superb search functionality to find older JavaScript libraries. Conveniently, Burp allows you to search only in scope items - so we checked that box - allowing us to find assets that would bypass the CSP.

We started with searches for [AngularJS](/web-security/cross-site-scripting/contexts/client-side-template-injection), as it's pretty easy to create a CSP bypass with that. There were references to Angular but not AngularJS - and the JavaScript files we tried didn't seem to load Angular or cause exceptions. So we moved on to Bootstrap and did searches in request headers and the response body. A few instances of Bootstrap came up, and we found an older version (3.4.1). 

Next we looked into Bootstrap gadgets. There were a few XSS issues on GitHub, but these affected versions 3.4.0. We looked at the Bootstrap code for a while, looking for jQuery usage but were unable to find suitable gadgets.

Rather than find gadgets in libraries, we thought about PayPal gadgets. What if PayPal had some insecure JavaScript that we could exploit? This time, instead of searching for a specific library, we searched for part of a path where libraries were hosted (such as "/c979c6f780cc5b37d2dc068f15894/js/lib/"). In the search results, we noticed a file called youtube.js and immediately spotted an obvious DOM XSS hole in it:

`../' + $(this).attr("data-id") + '.jpg"...`

This file was using jQuery, so all we needed to do was include jQuery and youtube.js, exploit the vulnerability, and we had a CSP bypass. Looking at the youtube.js file we saw that it used a CSS selector to find the YouTube player element:

`...$(".youtube-player").each(function() {... `

So we needed to inject an element with a class of "youtube-player" and a data-id attribute that contained our jQuery XSS vector. Once we had the basis of our generic PayPal CSP bypass, all we had to do was combine it with the original injection. First we injected an iframe with a srcdoc attribute. This was because we wanted to inject an external script - but because this was a DOM based vulnerability, scripts won't execute. But with srcdoc they will:

`input[value='\">\<iframe srcdoc=`

Notice that we need to ensure it's a valid selector by escaping double quotes, and assigning single quotes for the value part of the selector. Then we can inject our scripts, which point to jQuery and the YouTube gadget: 

`&lt;script/src=https://www.paypalobjects.com/web/res/28f/c979c6f780cc5b37d2dc068f15894/js/lib/jquery-2.2.4.min.js&gt;&lt;/script&gt;&lt;script/src=https://www.paypalobjects.com/web/res/28f/c979c6f780cc5b37d2dc068f15894/js/lib/youtube.js&gt;&lt;/script&gt;`

Notice that we have to HTML encode the vector - because we don't want it to close the srcdoc attribute with a > character. We avoid using spaces for the same reason. Then we use the YouTube gadget to inject a script, which jQuery converts and executes. Again we need to HTML encode the vector, give it the correct class name, and use the data-id attribute to inject our vector. Notice that we use an encoded single quote to avoid the attribute from breaking. We have to double HTML encode the double quote, because the srcdoc will decode the HTML, and the data-id attribute will decode when it's rendered in the iframe - so double encoding makes sure the quote is there when it injects into the YouTube gadget. Finally, we clean up by using a single line comment to ensure the script ignores anything after the inject - finishing the CSS selector with a double quote and single quote:

`<div/class=youtube-player data-id=&apos;&amp;quot;&gt;&lt;script&gt;alert(document.domain)//&apos;&gt;>\"']`

The final proof of concept can be found here:

[Proof of concept](https://developer.paypal.com/docs/archive/?countries=burpdomxss%20input%5Bvalue=%27%5c%22%3E%5c%3Ciframe%20srcdoc=%26lt%3Bscript/src=https://www.paypalobjects.com/web/res/28f/c979c6f780cc5b37d2dc068f15894/js/lib/jquery-2.2.4.min.js%26gt%3B%26lt%3B/script%26gt%3B%26lt%3Bscript/src=https://www.paypalobjects.com/web/res/28f/c979c6f780cc5b37d2dc068f15894/js/lib/youtube.js%26gt%3B%26lt%3B/script%26gt%3B%26lt%3Bdiv/class=youtube-player%26%23x20%3Bdata-id=%26apos%3B%26amp%3Bquot%3B%26gt%3B%26lt%3Bscript%26gt%3Balert%28document.domain%29%2f%2f%26apos%3B%26gt%3B%3E%5c%22%27%5D)

Here is a screenshot of the PoC in all its glory:

![PayPal proof of concept DOM based XSS found with DOM Invader](/cms/images/83/0d/afe8-article-image3-resized.png)

This is pretty cool - a complete CSP bypass on all of PayPal - but is it needed? Well, as we've seen, jQuery is CSP's nemesis. It converts scripts, and will happily execute them with policies, using the 'unsafe-eval' directive. Looking at the original XSS hole, it appears to be a jQuery selector. We can therefore inject a script, and it will be converted by jQuery - so a separate CSP bypass isn't required. Therefore, we can simplify the injection to the following:

`input[value='\">\<script>alert(1)//>\"']`

[Proof on concept with smaller vector](https://developer.paypal.com/docs/archive/?countries=burpdomxss%20input%5Bvalue=%27%5c%22%3E%5c%3Cscript%3Ealert%281%29%2f%2f%3E%5c%22%27%5D)

## Conclusion

Allow list policies are definitely not secure - especially when you have a multitude of scripts/libraries that can be abused. Fixing XSS even when user input is typically not expected can help prevent unintentional script gadgets. 

You should never rely solely on a CSP to protect you from XSS. While it's part of your defence, it's not the only barrier available. If you run a bug bounty program we recommend you fix XSS regardless of a CSP. If you don't use [DOM Invader](https://portswigger.net/blog/introducing-dom-invader), you'll miss out on serious XSS vulnerabilities in your application.

[ XSS ](/research/cross-site-scripting-research) [ polyglot ](/research/polyglot) [ csp ](/research/csp)

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
