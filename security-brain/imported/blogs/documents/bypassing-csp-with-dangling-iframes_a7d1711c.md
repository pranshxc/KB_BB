---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-14_bypassing-csp-with-dangling-iframes.md
original_filename: 2022-06-14_bypassing-csp-with-dangling-iframes.md
title: Bypassing CSP with dangling iframes
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
raw_sha256: a7d1711c145f364ebb613e94cf35d9df82a8341df9033c737d766cdc26bb587c
text_sha256: 16cef8bc9cad3c2dd00ad2f2db0b489295a4608f0338f9d65a9118f87a8ba483
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing CSP with dangling iframes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-14_bypassing-csp-with-dangling-iframes.md
- Source Type: markdown
- Detected Topics: xss, ssrf, csrf, sqli, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `a7d1711c145f364ebb613e94cf35d9df82a8341df9033c737d766cdc26bb587c`
- Text SHA256: `16cef8bc9cad3c2dd00ad2f2db0b489295a4608f0338f9d65a9118f87a8ba483`


## Content

---
title: "Bypassing CSP with dangling iframes"
page_title: "Bypassing CSP with dangling iframes | PortSwigger Research"
url: "https://portswigger.net/research/bypassing-csp-with-dangling-iframes"
final_url: "https://portswigger.net/research/bypassing-csp-with-dangling-iframes"
authors: ["Gareth Heyes (@garethheyes)"]
programs: ["Google", "Mozilla"]
bugs: ["CSP bypass"]
publication_date: "2022-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2558
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

# Bypassing CSP with dangling iframes

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-with-dangling-iframes&text=Bypassing+CSP+with+dangling+iframes%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-with-dangling-iframes)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-with-dangling-iframes)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fbypassing-csp-with-dangling-iframes)
  * [ ](mailto:?subject=Bypassing+CSP+with+dangling+iframes&body=Bypassing+CSP+with+dangling+iframes%0A%0AIntroduction+Our+Web+Security+Academy+has+a+topic+on+dangling+markup+injection+-+a+technique+for+exploiting+sites+protected+by+CSP.+But+something+interesting+happened+when+we+came+to+update+to+Chrome+%0A%0Ahttps://portswigger.net/research/bypassing-csp-with-dangling-iframes)
  * [ ](/research/rss)

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

  * **Published:** Tuesday, 14 June 2022 at 14:00 UTC

  * **Updated:** Tuesday, 14 June 2022 at 14:00 UTC

  * 

![Showing iframe screenshots dangling from strings](/cms/images/9e/5b/c853-article-dangling-markup-iframes-article.jpg)

## Introduction

Our Web Security Academy has a topic on [dangling markup injection](https://portswigger.net/web-security/cross-site-scripting/dangling-markup) \- a technique for exploiting sites protected by [CSP](https://portswigger.net/web-security/cross-site-scripting/content-security-policy). But something interesting happened when we came to update to Chrome 97 - because one of our interactive labs mysteriously stopped working. When we originally made this lab, Chrome prevented dangling markup-based attacks by looking for raw whitespace followed by "<" characters - but forgot to prevent background attributes (as discovered by [Masato Kinugawa](https://twitter.com/kinugawamasato)). 

Unfortunately, from Chrome 97 this technique no longer worked, so I was tasked to try and find an alternative. I tried many different attributes and CSS-based animations to delay assignments to try and bypass this protection. They all failed - it appears the force is strong with [Mike West](https://twitter.com/mikewest), who authored this change.

I took a step back and analysed the [CSP](/web-security/cross-site-scripting/content-security-policy):

`default-src 'self';object-src 'none'; style-src 'self'; script-src 'self'; img-src *;`

This looks watertight, right (apart from the img-src)? What if I told you that you could remove the 'img-src' directive and yet still conduct a [dangling markup](/web-security/cross-site-scripting/dangling-markup) attack without a click? Let's see how ...

## Cross domain iframe issues

First I fired up the [Hackability inspector](https://portswigger-labs.net/hackability/inspector/) which is a security-focussed enumerator I coded a while back and began to dissect the inner workings of iframes. The Inspector is convenient for testing multiple domains for cross-domain leaks. I added the [first iframe](https://portswigger-labs.net/hackability/inspector/?input=%3Ciframe%20src=%22https://subdomain1.portswigger-labs.net/hackability/inspector/%22%20id=x%20width=1000%20height=1000%3E) and inside that instance, I added another iframe:

`<iframe name=test>`

Then from the parent, I inspected the cross domain window with the following input:

`x.contentWindow`

To my surprise, the Inspector showed the name of the iframe as "test" - what was going on here? Well, the Inspector has a few known properties it tries - with "test" being one of them. But this then means that a cross-domain iframe can discover the iframe name attribute. I did a few tests and it appears that you can't enumerate the iframe for the name of the frame, but you can use typeof to determine if the name exists or not. For example you can ask yes/no questions on the name attribute of any cross-domain iframe:

`if(typeof x.contentWindow.myWinName === 'object') {  
//window name exists  
} else {  
//window name doesn't exist  
}`

This is good, but doesn't really help me bypass the CSP; it's no use trying to brute force a [CSRF](/web-security/csrf) token asking yes / no questions. Inspecting various properties of the cross-domain iframe, I tried changing the values - changing the location of the iframe to about:blank. To my surprise, even though this was cross-domain, Chrome allowed it: 

`x.contentWindow[0].location='about:blank'`

Not only that, but the full window was able to be enumerated, and I was able to access `location.ancesterOrigins` \- which leaked an external domain. But what I was really interested in was the window.name and if it could be read. Sure enough, the window name was readable and writable - and you could even execute JavaScript regardless of the parent page's CSP. What appears to happen is that when you assign it to about:blank the ownership of the iframe changes to the domain that set it.

Finally, here's the exploit that solved the lab:

`<script>  
function cspBypass(win) {  
win[0].location = 'about:blank';  
setTimeout(()=>alert(win[0].name), 500);  
}  
</script>  
<iframe src="//subdomain1.portswigger-labs.net/bypassing-csp-with-dangling-iframes/target.php?email=%22><iframe name=%27" onload="cspBypass(this.contentWindow)"></iframe>`

[Proof of concept](https://portswigger-labs.net/bypassing-csp-with-dangling-iframes/attacker.php)

## Conclusion

CSP treats about:blank URLs as the same origin - however when an attacker sets a cross domain iframe to about:blank, it becomes readable by an attacker and is definitely not the same origin. The Chrome mitigations for dangling markup attacks prevent some attacks, but by abusing browser quirks, it's possible to sidestep those mitigations and gain access to cross domain information via an injection - even with JavaScript disabled in your CSP.

## Timeline

2022-02-10 08:55 AM GMT - Reported bug to Google  
2022-02-10 09:38 AM GMT - Reported to Mozilla  
2022-06-14 15:00 PM GMT - Published this post

[ csp ](/research/csp) [ dangling markup ](/research/dangling-markup)

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
