---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-28_ambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro.md
original_filename: 2023-04-28_ambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro.md
title: 'Ambushed by AngularJS: a hidden CSP bypass in Piwik PRO'
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
raw_sha256: 845b4b67f412d441018e62df6fa233bfc98efd82b32e4e0390e30a9145dae39e
text_sha256: 3c6a00ef30e23c76062defec44287426844a1ff2014f81d1de917db51c3f47ed
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Ambushed by AngularJS: a hidden CSP bypass in Piwik PRO

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-28_ambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro.md
- Source Type: markdown
- Detected Topics: xss, ssrf, csrf, sqli, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `845b4b67f412d441018e62df6fa233bfc98efd82b32e4e0390e30a9145dae39e`
- Text SHA256: `3c6a00ef30e23c76062defec44287426844a1ff2014f81d1de917db51c3f47ed`


## Content

---
title: "Ambushed by AngularJS: a hidden CSP bypass in Piwik PRO"
page_title: "Ambushed by AngularJS: a hidden CSP bypass in Piwik PRO | PortSwigger Research"
url: "https://portswigger.net/research/ambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro"
final_url: "https://portswigger.net/research/ambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro"
authors: ["Gareth Heyes (@garethheyes)"]
programs: ["PortSwigger", "Piwik"]
bugs: ["CSP bypass"]
publication_date: "2023-04-28"
added_date: "2023-04-29"
source: "pentester.land/writeups.json"
original_index: 1213
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

# Ambushed by AngularJS: a hidden CSP bypass in Piwik PRO

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro&text=Ambushed+by+AngularJS%3A+a+hidden+CSP+bypass+in+Piwik+PRO%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro)
  * [ ](mailto:?subject=Ambushed+by+AngularJS%3A+a+hidden+CSP+bypass+in+Piwik+PRO&body=Ambushed+by+AngularJS%3A+a+hidden+CSP+bypass+in+Piwik+PRO%0A%0AAny+individual+website+component+can+undermine+the+security+of+the+entire+site%2C+and+analytics+platforms+are+no+exception.+With+this+in+mind%2C+we+decided+to+do+a+quick+audit+of+Piwik+PRO+to+make+sure+it%0A%0Ahttps://portswigger.net/research/ambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro)
  * [ ](/research/rss)

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

  * **Published:** Friday, 28 April 2023 at 12:00 UTC

  * **Updated:** Friday, 28 April 2023 at 12:31 UTC

  * 

![A picture of AngularJS style tribes people surrounding an CSP bypass vector in a pit](/cms/images/25/8d/ed5e-article-ambushed_by_angularjs_final_blog-article_copy_7.png)  

Any individual website component can undermine the security of the entire site, and analytics platforms are no exception. With this in mind, we decided to do a quick audit of Piwik PRO to make sure it was safe to deploy on portswigger.net.

I decided to look for client-side issues like [DOM XSS](/web-security/cross-site-scripting/dom-based) \- I focussed on this because we were introducing new script resources and therefore the most likely vector would be a DOM XSS vulnerability. The first thing I did was browse the site with [DOM Invader](https://portswigger.net/burp/documentation/desktop/tools/dom-invader) enabled and try injecting canaries - this yielded no results, which was good news. Next, I changed the DOM Invader canary to a blank value which enabled me to see all the sinks being used regardless of whether the canary was present or not. This is super useful for spotting stuff like document.write() and sure enough, there was a document.write call and various innerHTML assignments. I got a stack trace and inspected the document.write() call and noticed there was a debug flag… That led me to my next question - what does this do?

I added the flag to the URL and low and behold, an analytics debugger appeared. I tested that the document.write call wasn't vulnerable to XSS and then I pondered my next question: how was this debugger constructed? I started inspecting the debugger using devtools and immediately noticed an "ng-app" event. Jackpot, this is my [old friend AngularJS](https://portswigger.net/research/xss-without-html-client-side-template-injection-with-angularjs).

You might be wondering why I hit the jackpot. This is because [AngularJS](/web-security/cross-site-scripting/contexts/client-side-template-injection) has well known [script gadgets](https://www.blackhat.com/docs/us-17/thursday/us-17-Lekies-Dont-Trust-The-DOM-Bypassing-XSS-Mitigations-Via-Script-Gadgets.pdf) that can be used to bypass [Content Security Policy](/web-security/cross-site-scripting/content-security-policy) ([CSP](https://portswigger.net/web-security/cross-site-scripting/content-security-policy)). A script gadget is some JavaScript code, usually from a library, that adds additional functionality to HTML or JavaScript. You can then use this gadget to bypass [CSP](/web-security/cross-site-scripting/content-security-policy), since the gadget already has JavaScript execution and is allowed by the policy. A good example of this is ng-focus in AngularJS - this event lets you execute a browser focus event but because ng-focus is non-standard it will be allowed by the CSP and executed by AngularJS itself. 

Once you have identified that you have a AngularJS gadget there are two possible outcomes. You can either perform [client-side template injection](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection) (CSTI), or you have a CSP bypass. CSTI wasn't possible because it requires a HTML injection vulnerability in order to inject the script resources. This left a CSP bypass, which is important to fix because if your site has a HTML injection vulnerability then you can use the CSP bypass to escalate to XSS. I've done this in the past to find [XSS in PayPal](https://portswigger.net/research/finding-dom-polyglot-xss-in-paypal-the-easy-way).

On further inspection, the debugger seemed to use an iframe and loaded various script resources that were allowed by our CSP. I consulted our [XSS cheat](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#angularjs-csp-bypasses) sheet to see the various CSP bypasses for AngularJS. I picked the first one and entered the following into the console:

`document.body.innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>  
<script src=https://ps.containers.piwik.pro/container-debugger/vendor.js></script>  
<script src=https://ps.containers.piwik.pro/container-debugger/scripts.js></script>  
<script src=https://ps.containers.piwik.pro/container-debugger/templates.cache.js></script>  
<input autofocus ng-focus=$event.composedPath()|orderBy:'[].constructor.from([1],alert)'>  
</div>  
">``

Sure enough, this bypassed CSP completely. Because the scripts were allow listed, an attacker could inject AngularJS directives and a ng-focus event using composedPath() to get the window object in an array. The orderBy filter, which traverses that array and the scope of executing code, then eventually becomes the window object and Array.from() is used to call the alert function indirectly - this then bypasses CSP. We reported this issue to Piwik and they updated their CSP deployment instructions to address this vulnerability. They [fixed it](https://github.com/PiwikPRO/PPMS-PublicDocs/pull/984/files) by tightening the CSP to allow list a specific JavaScript file rather than the whole domain. They also used nonces for certain scripts, as this prevented an attacker from injecting their own AngularJS script resources.

This is now live - if you find something we missed please report it to [PortSwigger's](https://hackerone.com/portswigger) and [Piwik PRO's](https://piwik.pro/bug-bounty-program/) bug bounty programs.

## Timeline

2nd Mar 2023, 10:51 - Reported CSP bypass to Piwik  
2nd Mar 2023, 11:20 - Acknowledged by Piwik  
3rd Mar 2023, 13:09 - Vulnerability confirmed  
7th Mar 2023, 12:24 - CSP [deployment instructions](https://developers.piwik.pro/en/latest/tag_manager/content_security_policy.html) updated to fix vulnerability  
28th April 2023, 13:00 - Blog post released

[ csp ](/research/csp) [ angularjs ](/research/angularjs)

[Back to all articles](/research/articles)

## Related Research

### [ Using form hijacking to bypass CSP 05 March 2024 Using form hijacking to bypass CSP ](/research/using-form-hijacking-to-bypass-csp) ### [ Bypassing CSP via DOM clobbering 05 June 2023 Bypassing CSP via DOM clobbering ](/research/bypassing-csp-via-dom-clobbering) ### [ Stealing passwords from infosec Mastodon - without bypassing CSP 15 November 2022 Stealing passwords from infosec Mastodon - without bypassing CSP ](/research/stealing-passwords-from-infosec-mastodon-without-bypassing-csp) ### [ Bypassing CSP with dangling iframes 14 June 2022 Bypassing CSP with dangling iframes ](/research/bypassing-csp-with-dangling-iframes)

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
