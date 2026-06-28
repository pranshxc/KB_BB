---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-08_bug-bounty-guest-post-local-file-read-via-stored-xss-in-the-opera-browser.md
original_filename: 2021-09-08_bug-bounty-guest-post-local-file-read-via-stored-xss-in-the-opera-browser.md
title: 'Bug Bounty Guest Post: Local File Read via Stored XSS in The Opera Browser'
category: blogs
detected_topics:
- xss
- command-injection
tags:
- imported
- blogs
- xss
- command-injection
language: en
raw_sha256: 48b92b932bd1b2bce72d4c53221b7c5a09e70abb0db459714b433bc35af67d2d
text_sha256: f6d2d353c0bae83270d2ca961f6bb23e140b34933556dc3342702c6522647de0
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Bounty Guest Post: Local File Read via Stored XSS in The Opera Browser

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-08_bug-bounty-guest-post-local-file-read-via-stored-xss-in-the-opera-browser.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `48b92b932bd1b2bce72d4c53221b7c5a09e70abb0db459714b433bc35af67d2d`
- Text SHA256: `f6d2d353c0bae83270d2ca961f6bb23e140b34933556dc3342702c6522647de0`


## Content

---
title: "Bug Bounty Guest Post: Local File Read via Stored XSS in The Opera Browser"
page_title: "Bug Bounty Guest Post: Local File Read via Stored XSS in The Opera Browser | Opera Security"
url: "https://blogs.opera.com/security/2021/09/bug-bounty-guest-post-local-file-read-via-stored-xss-in-the-opera-browser/"
final_url: "https://blogs.opera.com/security/2021/09/bug-bounty-guest-post-local-file-read-via-stored-xss-in-the-opera-browser/"
authors: ["Renwa (@RenwaX23)"]
programs: ["Opera"]
bugs: ["Stored XSS", "Local File Read"]
bounty: "4,000"
publication_date: "2021-09-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3335
---

[Research](https://blogs.opera.com/security/category/research/)

# Bug Bounty Guest Post: Local File Read via Stored XSS in The Opera Browser

Share

  * [![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_facebook.da73949178f1431aa6845a440149477e.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fblogs.opera.com%2Fsecurity%2F2021%2F09%2Fbug-bounty-guest-post-local-file-read-via-stored-xss-in-the-opera-browser%2F)
  * [![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_twitter.2d56c3ce28cf4b8b0c903daaa279cdec.svg)](https://twitter.com/intent/tweet?text=Bug%20Bounty%20Guest%20Post:%20Local%20File%20Read%20via%20Stored%20XSS%20in%20The%20Opera%20Browser&url=https%3A%2F%2Fblogs.opera.com%2Fsecurity%2F2021%2F09%2Fbug-bounty-guest-post-local-file-read-via-stored-xss-in-the-opera-browser%2F&via=wpvkp)
  * [![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_linkedin.6432d0e754bc197e2aeb64c38fcf2e23.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fblogs.opera.com%2Fsecurity%2F2021%2F09%2Fbug-bounty-guest-post-local-file-read-via-stored-xss-in-the-opera-browser%2F&title=Bug%20Bounty%20Guest%20Post:%20Local%20File%20Read%20via%20Stored%20XSS%20in%20The%20Opera%20Browser)
  * ![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_copy-link.c83a9d420f922d3fde784398f6d5b79c.png)

![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/img-placeholder.e3550a73cbe5432de9d7de613fbf1e1a.jpg)

September 8th, 2021

_Opera manages a[Bug Bounty program](https://bugcrowd.com/opera) where researchers can report vulnerabilities in Opera’s software and be rewarded for it. For high-quality reports, we like to invite researchers to write about their findings.  
  
In this post, Opera’s Security Team has invited Bug Bounty Hunter [Renwa](https://twitter.com/RenwaX23) to write about a recent vulnerability that he reported, which was subsequently fixed and a $4,000 USD reward given. What follows is his write-up and experience._

I like testing the security of browsers. So when I found out that Opera offers bounties for finding vulnerabilities in its browser, I started looking. This post outlines one of the vulnerabilities I found: the potential for a webpage to retrieve screenshots of local files from users.

![](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2021/08/Screen20Shot202021-07-2720at2012.51.5120AM.png)A pin on my Opera Pinboard.

Given that Opera is Chromium-based, the first thing I did was download a fresh version of the Opera Browser, and look at the new features they had added. One of those features is called Opera Pinboards. It’s basically a note/bookmark saver which can be shared with other users, to which you can add text, images, and links.

The URI for this service is <https://pinboard.opera.com/>. When opening this page in Opera, however, I was redirected to _**opera:pinboards**_. The _opera:_ scheme is a special location in Opera, similar to Chrome’s _**chrome:**_ , and has special permissions which normal pages don’t have. By using a web proxy, I found that when adding a new link as a pin to my pinboard, a request is made to _**pinboard.opera-api.com**_ as so:

POST /v1/items HTTP/2  
Host: pinboard.opera-api.com  
Content-Type: application/json  
  
{“items”:[{“pos”:{“x”:6,”y”:1},”title”:{“v”:”Hello”},”desc”:{“v”:”Check my cool website”},”video”:false,”link”:{“href”:”https://renwax23.github.io/X/”,”title”:”it’s me”}}]} 

The URI inside the tag is parsed by the browser, and sent to the pinboard API, before being added to the local version in opera:pinboards.

My idea was that, if I could add a pin to opera:pinboards that link to a javascript URI, I could perform cross-site scripting (XSS) from within the privileged scheme. After performing many tests, I found that pinning the URI _**javascript:@opera.com**_ was possible, and it showed up in my pinboard as a clickable link! Thus, we have XSS!

After many more tries, I eventually came up with the payload _**javascript:’@opera.com/’;alert(1)**_ , which, upon clicking within my pinboard, caused a popup. However, there was a small problem: the tag within the pinboard interface used the attribute _**target=_blank**_ , which meant that any link clicked on the page would open in a new window, and wouldn’t execute javascript within the page. Luckily, there’s a small trick for that: if you **Command (Ctrl) + Click** or **Middle-Click** the link, the code runs successfully.

![](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2021/08/Screen20Shot202021-07-2720at201.04.1320AM-1-edited.jpg)

With simple XSS on the opera:pinboards page, I wanted to show a greater impact than just simply causing a popup when clicking on a link — because who cares about that?

As mentioned, the opera: scheme has more permissions than normal webpages: it also has access to some native function calls, and allows for the viewing of other tabs, bypassing the browser’s same-origin policy (SOP). It also allows for the loading of the _**file:**_ scheme, which can be used to view local files. However, it didn’t allow all native functions to be used, which would allow complete control and access to other tabs (e.g. injecting javascript which would copy the whole page’s contents and send it to my server).

Putting all of this information together, I made a script that would do the following:

  1. Create a new tab using the native function _**chrome.tabs.create**_. In this case, the new tab opened _**file:///etc/passwd**_.
  2. Create a screenshot of the opened tab using the same function which Opera Pinboards uses to create thumbnails for pins, _**opr.pinboardPrivate.getThumbnail**_.
  3. Send the screenshot, in a base64-encoded PNG, to my server, which I could then view.

Creating a new pinboard that imported the script to execute all of these steps, I added a new pin which, when clicked, sent a screenshot of my stolen /etc/passwd file. I sent video proof of concept to Opera via their BugCrowd page.

After reporting the bug, I received a great response from the Opera Bug Bounty Council, and the bug was fixed within one day, with a reward paid out about one month later.

Thanks For Reading!  
— [Renwa](https://twitter.com/RenwaX23)

Bounty: $4,000 USD.

[ ![](https://secure.gravatar.com/avatar/1bc5da9caf0d55cabcd2a1b02829c7e38d344f0eb5a29824736d5da7a2f71adb?s=120&d=mm&r=g) Opera Team ](https://blogs.opera.com/security/author/operateam/)

[bug bounty](https://blogs.opera.com/security/tag/bug-bounty/)

* * *

### User comments

![You deserve a</br>better browser](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/image-sidebar.829f600e58c0e4206501da0863c92aa1.png)

### You deserve abetter browser

Faster, safer and smarter than default browsers. Fully-featured for privacy, security, and so much more.

[ Download now ](https://www.opera.com/download)

* * *

[![How does Opera make money? An explainer on monetization](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2026/06/How-does-Opera-make-money-monetization-explainer.png)](https://blogs.opera.com/security/2026/06/how-does-opera-make-money-monetization-explainer/)

[Privacy](https://blogs.opera.com/security/category/privacy/)

##  [How does Opera make money? An explainer on monetization](https://blogs.opera.com/security/2026/06/how-does-opera-make-money-monetization-explainer/ "Permanent Link to How does Opera make money? An explainer on monetization")

June 22nd, 2026

[![](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2023/06/Opera-Security-Updates-Green.png)](https://blogs.opera.com/security/2026/06/update-your-browser-security-fix-for-chrome-zero-day-cve-2026-11645/)

[News, ](https://blogs.opera.com/security/category/news/)[Security](https://blogs.opera.com/security/category/security/)

##  [Update your browser: Security fix for Chrome zero-day CVE-2026-11645](https://blogs.opera.com/security/2026/06/update-your-browser-security-fix-for-chrome-zero-day-cve-2026-11645/ "Permanent Link to Update your browser: Security fix for Chrome zero-day CVE-2026-11645")

June 11th, 2026

[![Is Opera's VPN safe?](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2024/09/opera-free-vpn-no-log-audit-wide.jpg)](https://blogs.opera.com/security/2026/05/opera-vpn-is-safe/)

[Security](https://blogs.opera.com/security/category/security/)

##  [Why browsing with Opera’s VPN is safer](https://blogs.opera.com/security/2026/05/opera-vpn-is-safe/ "Permanent Link to Why browsing with Opera’s VPN is safer")

May 29th, 2026

[![Inside the role of Opera's Head of Security](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2026/05/Opera-Head-of-Security.png)](https://blogs.opera.com/security/2026/05/meet-opera-head-of-security/)

[Security](https://blogs.opera.com/security/category/security/)

##  [How we keep Opera users and products safe: Inside the role of Head of Security](https://blogs.opera.com/security/2026/05/meet-opera-head-of-security/ "Permanent Link to How we keep Opera users and products safe: Inside the role of Head of Security")

May 8th, 2026

[![Opera Security team helps make the web safer through responsible disclosure](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2026/04/Opera-Security-responsible-disclosure.png)](https://blogs.opera.com/security/2026/04/opera-security-responsible-disclosure-osslsigncode-quill/)

[Security](https://blogs.opera.com/security/category/security/)

##  [How Opera’s Security team helps make the web safer through responsible disclosure](https://blogs.opera.com/security/2026/04/opera-security-responsible-disclosure-osslsigncode-quill/ "Permanent Link to How Opera’s Security team helps make the web safer through responsible disclosure")

April 17th, 2026

[![](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2023/06/Opera-Security-Updates-Green.png)](https://blogs.opera.com/security/2026/04/update-your-browser-security-fix-for-chrome-zero-day-cve-2026-5281/)

[News, ](https://blogs.opera.com/security/category/news/)[Security](https://blogs.opera.com/security/category/security/)

##  [Update your browser: Security fix for Chrome zero-day CVE-2026-5281](https://blogs.opera.com/security/2026/04/update-your-browser-security-fix-for-chrome-zero-day-cve-2026-5281/ "Permanent Link to Update your browser: Security fix for Chrome zero-day CVE-2026-5281")

April 4th, 2026

![control](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/arrow-left.171ab59fa709a3915488a44fbe586dba.svg) ![control](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/arrow-right.22d48607ea14d7ce2603010ffc20d31d.svg)

* * *

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Sign up for our Newsletter and get the latest news from Opera

Join the mailing list for regular updates on AI and Opera

Your name

Your email

I agree to receive regular updates about Opera via electronic means (including email).

Sign up 

*Required fields

[Please check our Privacy Policy to see how we process data.](https://legal.opera.com/privacy/)

[ ![Opera](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/logo.e807fcd39b532b698412c37cd8017781.png) ](https://www.opera.com/)

# You deserve a better browser

Opera's free VPN, Ad blocker, and Flow file sharing. Just a few of the must-have features built into Opera for faster, smoother and distraction-free browsing designed to improve your online experience.

[ Download now ](https://www.opera.com/download)
