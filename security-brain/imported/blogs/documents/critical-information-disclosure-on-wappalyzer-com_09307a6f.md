---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-03-24_critical-information-disclosure-on-wappalyzercom.md
original_filename: 2017-03-24_critical-information-disclosure-on-wappalyzercom.md
title: Critical information disclosure on Wappalyzer.com
category: documents
detected_topics:
- automation-abuse
- sqli
- command-injection
- path-traversal
- information-disclosure
- api-security
tags:
- imported
- documents
- automation-abuse
- sqli
- command-injection
- path-traversal
- information-disclosure
- api-security
language: en
raw_sha256: 09307a6f749dcd045c99beb4b8ea41c47adad101c653f83feaaa8267f6f0701e
text_sha256: 22f8ad9322f1b45b87972baee37b504c76a56100162b6dd6b1f1cc5a8a2b7abc
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Critical information disclosure on Wappalyzer.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-03-24_critical-information-disclosure-on-wappalyzercom.md
- Source Type: markdown
- Detected Topics: automation-abuse, sqli, command-injection, path-traversal, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `09307a6f749dcd045c99beb4b8ea41c47adad101c653f83feaaa8267f6f0701e`
- Text SHA256: `22f8ad9322f1b45b87972baee37b504c76a56100162b6dd6b1f1cc5a8a2b7abc`


## Content

---
title: "Critical information disclosure on Wappalyzer.com"
page_title: "Critical information disclosure on Wappalyzer.com | nc-lp.com"
url: "https://www.nc-lp.com/blog/critical-information-disclosure-on-wappalyzer-com"
final_url: "https://www.nc-lp.com/blog/critical-information-disclosure-on-wappalyzer-com"
authors: ["Davide Tampellini (@tampe125)"]
programs: ["Wappalyzer"]
bugs: ["Information disclosure"]
publication_date: "2017-03-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6205
---

# [Critical information disclosure on Wappalyzer.com](/blog/critical-information-disclosure-on-wappalyzer-com)

__24th Mar 2017 __[web scraping, ](/tag:web scraping) [full disclosure](/tag:full disclosure)

![](/images/1/3/0/e/0/130e0a785fa4c5084330b69928917545fd3245bc-01leakresize.jpeg)

While performing some online assesment, a critical information disclosure has been found on [Wappalyzer.com](https://www.wappalyzer.com). The vulnerability has been fixed, this is the full disclosure about the issue.

## What's Wappalyzer?

Wappalyzer is a nice swift tool used to identify technologies powering the website you are currently visiting. It has browser extensions both for Chrome and Firefox, you can review the full source code [on GitHub](https://github.com/AliasIO/Wappalyzer).  
I'm currently using it on a side project of mine, so I'm visiting their site quite often.  
Few weeks ago, Wappalyzer decided to monetize their large database and start selling the dataset. This was paired with a change in their site: a new graphic and new features were added.

## Recon never ends

At that time I was reading a very interesting article about [SQLi + XXE + File path traversal Deutsche Telekom](https://www.ibrahim-elsayed.com/?p=150), explaining how recon never ends. Usually vulnerabilities are triggered by small details, maybe in some test subdomain that no one is maintaining.  
I found it very inspiring and I decided to try its suggestions on a live site. 

First of all I used [SubBrute](https://github.com/TheRook/subbrute) to find some interesting subdomain. Since nothing showed up, I started using DirBuster.  
After some time running, I found something interesting: ![](/user/pages/01.blog/critical-information-disclosure-on-wappalyzer-com/wappalyzer_dirbuster_1.png)

Oh nice! An authentication required! Maybe I can try to bruteforce it for some weak passwords. However, I let it running, just in case there could be something else.

![](/user/pages/01.blog/critical-information-disclosure-on-wappalyzer-com/wappalyzer_dirbuster_results.png)

Wait, what? **admin** requires authentication, but **Admin** doesn't ?!  
Oh boy, this means that we have access to the administrative area?

![](/user/pages/01.blog/critical-information-disclosure-on-wappalyzer-com/wappalyzer_admin_resize.png)

The heavily redacted image shows the most recent orders and their value. The only visible email is my own personal address, used to run some tests.  
Links to order details are "protected", too; but switching the case of the folder does the trick.

![](/user/pages/01.blog/critical-information-disclosure-on-wappalyzer-com/wappalyzer_order_resize.png)

As you can see, in the details page I can change the status of my order. This means that I could just request a quote for the **all the available datasets** , then log in, change the status to **Complete** and then download everything free of charge. I didn't actually tried to perform such actions, since it could have disruptive results, but I think it's a plausible scenario.

## Conclusions

Once I confirmed the access to the admin area and the disclosure of private information, I immediately got in touch with Wappalyzer owners and they quickly fixed the issue in a couple of hours.

## Report timeline
  
  
  2017-03-20  Initial report to Wappalyzer  
  2017-03-20  Fix by the vendor  
  2017-03-24  Full disclosure

  * [ __](https://www.facebook.com/share.php?u=https://www.nc-lp.com/blog/critical-information-disclosure-on-wappalyzer-com)
  * [ __](https://twitter.com/home?status=Critical%20information%20disclosure%20on%20Wappalyzer.com-https://www.nc-lp.com/blog/critical-information-disclosure-on-wappalyzer-com)
  * [ __](https://digg.com/submit?url=https://www.nc-lp.com/blog/critical-information-disclosure-on-wappalyzer-com&title=Critical%20information%20disclosure%20on%20Wappalyzer.com)
  * [ __](https://reddit.com/submit?url=https://www.nc-lp.com/blog/critical-information-disclosure-on-wappalyzer-com&title=Critical%20information%20disclosure%20on%20Wappalyzer.com)
  * [ __](https://www.linkedin.com/shareArticle?mini=true&url=https://www.nc-lp.com/blog/critical-information-disclosure-on-wappalyzer-com&title=Critical%20information%20disclosure%20on%20Wappalyzer.com)

#### Related Posts

[ ![](/images/a/5/f/6/0/a5f6093850c06e908a01f91e67339981e1c46b29-hashtags.png) ](/blog/hashtag-scraper "Hashtag scraper")

[ ![](/images/3/3/b/6/4/33b64e08097efc2433b8fec1b6f3f0c21a4e52fd-1mongodb.png) ](/blog/mongodb-scraper "MongoDB Scraper")

[ ![](/images/0/0/f/d/0/00fd08cc0dd9c192af8da6bbf04af2a09dc1bd5f-1logcheck.jpeg) ](/blog/server-compromise-on-redacted-hosting "Server compromise on \[REDACTED\] hosting")

[ ![](/images/c/d/a/d/e/cdade270737723384430501c71ba52b38f9987e2-1drinkingfirehose.jpeg) ](/blog/how-to-crawl-the-web "How to crawl the web")

#### Comments:

[Blog Comments powered by Disqus.](http://disqus.com)

[__Newer Post](/blog/server-compromise-on-redacted-hosting) [Older Post __](/blog/build-a-custom-apt-module) [Home](https://www.nc-lp.com)
