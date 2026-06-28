---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-05_bypassing-csp-with-policy-injection.md
original_filename: 2019-06-05_bypassing-csp-with-policy-injection.md
title: Bypassing CSP with policy injection
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
raw_sha256: 368daebcd21a808c5d7dfeee8f87e1afef7b834cff6f8e5802431f5e157d7c66
text_sha256: a10f7d35271d5da3d3ac216cd74198d56006f181ea226d54d023e67cfa5f9032
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing CSP with policy injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-05_bypassing-csp-with-policy-injection.md
- Source Type: markdown
- Detected Topics: xss, ssrf, csrf, sqli, command-injection, path-traversal
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `368daebcd21a808c5d7dfeee8f87e1afef7b834cff6f8e5802431f5e157d7c66`
- Text SHA256: `a10f7d35271d5da3d3ac216cd74198d56006f181ea226d54d023e67cfa5f9032`


## Content

---
title: "Bypassing CSP with policy injection"
page_title: "Bypassing CSP with policy injection | PortSwigger Research"
url: "https://portswigger.net/blog/bypassing-csp-with-policy-injection"
final_url: "https://portswigger.net/research/bypassing-csp-with-policy-injection"
authors: ["Gareth Heyes (@garethheyes)"]
programs: ["Paypal"]
bugs: ["CSP bypass"]
bounty: "900"
publication_date: "2019-06-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5230
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

# Bypassing CSP with policy injection

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-with-policy-injection&text=Bypassing+CSP+with+policy+injection%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-with-policy-injection)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-with-policy-injection)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-with-policy-injection)
  * [ ](mailto:?subject=Bypassing+CSP+with+policy+injection&body=Bypassing+CSP+with+policy+injection%0A%0AWhilst+testing+PayPal+looking+for+ways+to+bypass+CSP+and+mixed+content+protection+I+found+an+interesting+behaviour.+PayPal+was+putting+a+GET+parameter+called+token+inside+the+report-uri+directive+of+t%0A%0Ahttps://portswigger.net/research/bypassing-csp-with-policy-injection)
  * [ ](/research/rss)

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

  * **Published:** Wednesday, 5 June 2019 at 13:10 UTC

  * **Updated:** Friday, 4 September 2020 at 14:31 UTC

  * 

![CSP policy injection](/cms/images/80/75/c2f7cdcc2432-article-csp_policy_injection_article.png)  

Whilst testing PayPal looking for ways to bypass [CSP](/web-security/cross-site-scripting/content-security-policy) and mixed content protection I found an interesting behaviour. PayPal was putting a GET parameter called token inside the report-uri directive of their CSP. I found that by changing the token parameter it was possible to inject directives into the policy. Most browsers simply skip over invalid CSP directives, but Edge behaves differently. If it encounters invalid syntax, Edge will drop the entire policy! I fuzzed Edge to find ways of breaking the CSP with as few characters as possible, and found you could simply use a semi-colon and an underscore. So if you loaded the following URL:

https://www.paypal.com/webapps/xoonboarding?values=etc&**token=SOMETOKEN;_**

You would be served this CSP header:

`Content-Security-Policy: default-src 'self' https://*.paypal.com https://*.paypal.com:* https://*.paypalobjects.com 'unsafe-eval';connect-src 'self' https://*.paypal.com https://nexus.ensighten.com https://*.paypalobjects.com;frame-src 'self' https://*.paypal.com https://*.paypalobjects.com https://*.cardinalcommerce.com;script-src https://*.paypal.com https://*.paypalobjects.com 'unsafe-inline' 'unsafe-eval';style-src 'self' https://*.paypal.com https://*.paypalobjects.com 'unsafe-inline';img-src https: data:;object-src 'none'; report-uri /webapps/xoonboarding/api/log/csp?**token=SOMETOKEN;_**`

And Edge would drop the entire policy.  

To see it in action I created a simple PoC:  

[Edge CSP bypass using policy injection](http://portswigger-labs.net/edge_csp_injection_xndhfye721/?x=;_&y=%3Cscript%3Ealert\(1\)%3C/script%3E)

Of course hardly anyone uses Edge, so then I thought about Chrome. Since Chrome ignores invalid directives and our injection happens at the end of the policy, I needed a way to override a directive. I found a recently proposed directive called "[script-src-elem](https://w3c.github.io/webappsec-csp/#directive-script-src-elem)". This directive allows you to control just script blocks and was created so that you can allow event handlers but block script elements for example: 

`Content-Security-Policy: script-src-elem 'none'; script-src-attr 'unsafe-inline'`

`<script>alert("This will be blocked")</script>  
<a href="#" onclick="alert('This will be allowed')">test</a>`

The interesting thing about this directive is that it will overwrite existing script-src directives! So you can use it to bypass CSP provided you have policy injection. Here is a PoC that works on Chrome:

[Chrome CSP bypass using policy injection  
](http://portswigger-labs.net/edge_csp_injection_xndhfye721/?x=%3Bscript-src-elem+*&y=%3Cscript+src=%22http://subdomain1.portswigger-labs.net/xss/xss.js%22%3E%3C/script%3E)

PayPal awarded me $900 for this bug which I thought was quite generous for a mitigation bypass.

Visit our Web Security Academy to [learn more about cross-site scripting (XSS)](https://portswigger.net/web-security/cross-site-scripting)

[ csp ](/research/csp)

[Back to all articles](/research/articles)

## Related Research

### [ Using form hijacking to bypass CSP 05 March 2024 Using form hijacking to bypass CSP ](/research/using-form-hijacking-to-bypass-csp) ### [ Bypassing CSP via DOM clobbering 05 June 2023 Bypassing CSP via DOM clobbering ](/research/bypassing-csp-via-dom-clobbering) ### [ Ambushed by AngularJS: a hidden CSP bypass in Piwik PRO 28 April 2023 Ambushed by AngularJS: a hidden CSP bypass in Piwik PRO ](/research/ambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro) ### [ Stealing passwords from infosec Mastodon - without bypassing CSP 15 November 2022 Stealing passwords from infosec Mastodon - without bypassing CSP ](/research/stealing-passwords-from-infosec-mastodon-without-bypassing-csp)

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
