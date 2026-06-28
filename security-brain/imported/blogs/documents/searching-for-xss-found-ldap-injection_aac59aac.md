---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-05_searching-for-xss-found-ldap-injection.md
original_filename: 2018-06-05_searching-for-xss-found-ldap-injection.md
title: Searching for XSS found LDAP injection
category: documents
detected_topics:
- sqli
- xss
- command-injection
- otp
- csrf
- supply-chain
tags:
- imported
- documents
- sqli
- xss
- command-injection
- otp
- csrf
- supply-chain
language: en
raw_sha256: aac59aacf0352f9b2126c2f20dfe6b890f237cca4f67cd970f2a6fbcf4ef146d
text_sha256: 8eec567d527b393d9ff0111a57ef7116d01a113d05585247fc365da1bcf6aaaf
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Searching for XSS found LDAP injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-05_searching-for-xss-found-ldap-injection.md
- Source Type: markdown
- Detected Topics: sqli, xss, command-injection, otp, csrf, supply-chain
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `aac59aacf0352f9b2126c2f20dfe6b890f237cca4f67cd970f2a6fbcf4ef146d`
- Text SHA256: `8eec567d527b393d9ff0111a57ef7116d01a113d05585247fc365da1bcf6aaaf`


## Content

---
title: "Searching for XSS found LDAP injection"
page_title: "Searching for XSS found LDAP injection | nc-lp.com"
url: "https://www.nc-lp.com/blog/searching-for-xss-found-ldap-injection"
final_url: "https://www.nc-lp.com/blog/searching-for-xss-found-ldap-injection"
authors: ["Davide Tampellini (@tampe125)"]
bugs: ["LDAP injection"]
publication_date: "2018-06-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5853
---

# [Searching for XSS found LDAP injection](/blog/searching-for-xss-found-ldap-injection)

__5th Jun 2018 __[vulnerability](/tag:vulnerability)

![](/images/a/3/a/7/0/a3a7081cb186b52c9414da52fe47afeb7e1c6c8b-1ldap.jpeg)

While searching for bugs on target website, I decided to check if it was vulnerable to blind XSS.  
It turns out that the system was vulnerable to LDAP injection. 

## Context

Some time ago I was assessing a website for vulnerabilities and I was reviewing all the possible endpoints.  
While surfing, I encountered a registration form to the service, it was pretty packed with fields and it seemed your account needed to be valuated and activated by a human.  
Usually registering to websites is a trivial test: if the website is built with a CMS, the workflow is pretty secure, otherwise there are chances to find some trivial SQL injections.  
However, this time I tried to exploit some side-channel vulnerabilities: if someone needs to review my data, maybe I can inject something into their backend and extract some data?

## Blind XSS

That "something" is [a blind XSS payload](https://www.acunetix.com/blog/articles/blind-xss/), where the payload is not executed directly on target website, but rather on another interface (for example admin backend).  
Detecting blind XSS is a little more complicated than regular onces, since you don't know when (and if) the payload would be executed. A great online tool is [XSS hunter](https://xsshunter.com/), that allows you to setup a test subdomain that will collect a lot of info once the vulnerability is triggered. 

So, I grabbed one of the default payloads, put into the fields and... bummer 

![](/user/pages/01.blog/searching-for-xss-found-ldap-injection/dotnet_waf.png)

## Built-in WAF and elusion

Ok, it seems that there's some kind of protection in place.  
After some reading, it seems that's the default WAF for .NET applications. However, when there are default settings there are known workarounds, too.  
Searching on Internet, I found [this article](https://markitzeroday.com/xss/asp.tag2017/10/14/asp.net-request-validation-bypass.html) about some tags being allowed even if the WAF is turned on.  
Long story short, tag `<%tag` is allowed, which could cause isseus with IE9. Ok, it's quite old, but maybe it's my lucky day? 

I put the payload into the form and... wait what? 

![](/user/pages/01.blog/searching-for-xss-found-ldap-injection/ldap_error.png)

## LDAP injection

Looking for the error code `0x80005000` and the error text `An invalid directory pathname was passed` I learnt that they are related to an LDAP error.  
This means that the server was taking user input with filtering it and trying to create a new user inside the LDAP server. 

Oh Boy! 

Exploiting LDAP injections is tricky, since they are ultra-blind and they aren't so common, I had to take back from the shelf my copy of _The WebApplication Hacker's Handbook_ to refresh my memory.  
Luckly the error page was enough for a valid POC, so I reported it back.

## Conclusions

If I had to sum up the whole experience in one phrase, I'd chose **Expect the unexpected**.  
Additionally, that's another reminder that you should never ever trust user input, even if there are protections in place.

  * [ __](https://www.facebook.com/share.php?u=https://www.nc-lp.com/blog/searching-for-xss-found-ldap-injection)
  * [ __](https://twitter.com/home?status=Searching%20for%20XSS%20found%20LDAP%20injection-https://www.nc-lp.com/blog/searching-for-xss-found-ldap-injection)
  * [ __](https://digg.com/submit?url=https://www.nc-lp.com/blog/searching-for-xss-found-ldap-injection&title=Searching%20for%20XSS%20found%20LDAP%20injection)
  * [ __](https://reddit.com/submit?url=https://www.nc-lp.com/blog/searching-for-xss-found-ldap-injection&title=Searching%20for%20XSS%20found%20LDAP%20injection)
  * [ __](https://www.linkedin.com/shareArticle?mini=true&url=https://www.nc-lp.com/blog/searching-for-xss-found-ldap-injection&title=Searching%20for%20XSS%20found%20LDAP%20injection)

#### Related Posts

[ ![](/images/6/0/9/e/c/609ecfabeea47a2d5085105dd3f41ae24e484005-1magento.jpeg) ](/blog/having-fun-with-magento-supee-8788 "Having fun with Magento SUPEE-8788")

[ ![](/images/3/6/a/6/a/36a6ad6376f3082b985dd9810dbad83a7e4b0579-1steal.jpeg) ](/blog/csrf-token-steal-in-joomla "CSRF token steal in Joomla")

[ ![](/images/e/f/2/8/1/ef281260aa21c29f9ed2adb30b4b3b1845d2e1f8-1manualblindsqli.jpeg) ](/blog/manually-craft-blind-sql-injections "Manually craft blind SQL injections")

[ ![](/images/4/c/0/5/7/4c057dbe535df86e0fd53af6ecb7ccf5f174f3f9-1pharasimage.jpeg) ](/blog/disguise-phar-packages-as-images "Disguise PHAR packages as images")

#### Comments:

[Blog Comments powered by Disqus.](http://disqus.com)

[__Newer Post](/blog/manually-craft-blind-sql-injections) [Older Post __](/blog/csrf-token-steal-in-joomla) [Home](https://www.nc-lp.com)
