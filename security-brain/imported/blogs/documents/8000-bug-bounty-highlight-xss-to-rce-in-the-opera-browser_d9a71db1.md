---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-24_8000-bug-bounty-highlight-xss-to-rce-in-the-opera-browser.md
original_filename: 2021-09-24_8000-bug-bounty-highlight-xss-to-rce-in-the-opera-browser.md
title: '$8,000 Bug Bounty Highlight: XSS to RCE in the Opera Browser'
category: documents
detected_topics:
- command-injection
- xss
- path-traversal
tags:
- imported
- documents
- command-injection
- xss
- path-traversal
language: en
raw_sha256: d9a71db159d3a4a414e26f7930d845dec8b3fe2b773609379589ed73f9a17461
text_sha256: 1908ae0cfa65265bbfd25ef1c4a9476d04bc7a698d20809299e1f7097bb278f4
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# $8,000 Bug Bounty Highlight: XSS to RCE in the Opera Browser

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-24_8000-bug-bounty-highlight-xss-to-rce-in-the-opera-browser.md
- Source Type: markdown
- Detected Topics: command-injection, xss, path-traversal
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `d9a71db159d3a4a414e26f7930d845dec8b3fe2b773609379589ed73f9a17461`
- Text SHA256: `1908ae0cfa65265bbfd25ef1c4a9476d04bc7a698d20809299e1f7097bb278f4`


## Content

---
title: "$8,000 Bug Bounty Highlight: XSS to RCE in the Opera Browser"
page_title: "$8,000 Bug Bounty Highlight: XSS to RCE in the Opera Browser | Opera Security"
url: "https://blogs.opera.com/security/2021/09/8000-bug-bounty-highlight-xss-to-rce-in-the-opera-browser"
final_url: "https://blogs.opera.com/security/2021/09/8000-bug-bounty-highlight-xss-to-rce-in-the-opera-browser/"
authors: ["Renwa (@RenwaX23)"]
programs: ["Opera"]
bugs: ["XSS", "RCE"]
bounty: "8,000"
publication_date: "2021-09-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3288
---

[Research](https://blogs.opera.com/security/category/research/)

# $8,000 Bug Bounty Highlight: XSS to RCE in the Opera Browser

Share

  * [![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_facebook.da73949178f1431aa6845a440149477e.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fblogs.opera.com%2Fsecurity%2F2021%2F09%2F8000-bug-bounty-highlight-xss-to-rce-in-the-opera-browser%2F)
  * [![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_twitter.2d56c3ce28cf4b8b0c903daaa279cdec.svg)](https://twitter.com/intent/tweet?text=$8,000%20Bug%20Bounty%20Highlight:%20XSS%20to%20RCE%20in%20the%20Opera%20Browser&url=https%3A%2F%2Fblogs.opera.com%2Fsecurity%2F2021%2F09%2F8000-bug-bounty-highlight-xss-to-rce-in-the-opera-browser%2F&via=wpvkp)
  * [![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_linkedin.6432d0e754bc197e2aeb64c38fcf2e23.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fblogs.opera.com%2Fsecurity%2F2021%2F09%2F8000-bug-bounty-highlight-xss-to-rce-in-the-opera-browser%2F&title=$8,000%20Bug%20Bounty%20Highlight:%20XSS%20to%20RCE%20in%20the%20Opera%20Browser)
  * ![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_copy-link.c83a9d420f922d3fde784398f6d5b79c.png)

![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/img-placeholder.e3550a73cbe5432de9d7de613fbf1e1a.jpg)

September 24th, 2021

_Continuing from his[previous post](https://blogs.opera.com/security/2021/09/bug-bounty-guest-post-local-file-read-via-stored-xss-in-the-opera-browser/), Bug Bounty Hunter [Renwa](https://twitter.com/RenwaX23) writes about the second vulnerability he submitted to [Opera’s Private Bug Bounty Programme](https://security.opera.com/bug-bounty/): a Remote Code Execution in Opera’s My Flow Feature. What follows is his write-up and experience._ _The described vulnerability of course has been fixed immediately after reporting._

One of the cooler features of the Opera Browser is _**My Flow**_ , which is basically a shared space between your computer and your phone, allowing you to share links, images, and videos with yourself. To connect, you just scan a QR code, and then you can send things between devices.

![](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2021/09/1525218633095-d6c9feef-075c-4e81-9701-22a296592e53-image.png)

Using the developer tools in Opera, I found that the My Flow interface is loaded from the domain _web.flow.opera.com_ , which is just a normal HTML page, and which allows me to view its code and components.

Looking at the page’s source code, I found that the page communicated with a browser extension, but from my browser’s extension list in _**opera://extensions/**_ , nothing appeared. After some research, I found that it is actually a hidden browser extension, which could be displayed by opening Opera using a special flag, **–show-component-extension-options**. After opening the browser with that flag, I found the extension called _**Opera Touch Background**_ , and was able to view its source code.

Going back to the web.flow.opera.com page, I began looking for XSS vulnerabilities. What caught my eye was this code:

`const html = e.dataTransfer.getData('text/html');  
const src = html.match(//);  
if (src && src[1]) {  
const parser = document.createElement("span");  
parser.innerHTML = src[1];  
}`

This functionality is for drag-and-drop; when a user drops an image onto the page, the code creates an element with its innerHTML element set as the location of the image. However, there are two problems with this:

  1. In browsers, it is possible to set the dataTransfer to any arbitrary value.
  2. In browsers, if you create a new element and set its innerHTML to an <img> tag, it will still be loaded in the background.

This means that the following will cause an alert box, despite no image being loaded on the screen:

`const parser = document.createElement("span");  
parser.innerHTML = '<img src=x onerror=alert(1)>';`

With all of this in mind, I created a small proof-of-concept XSS. To show how easy it was to cause the XSS, I created a webpage which, once you began dragging an image, would redirect to the web.flow.opera.com page after a couple seconds. This meant that a user would only need to begin dragging an image, and then simply let go of the mouse, for the XSS to happen.

![](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2021/09/ezgif-1-9b114c3d83bb-1.gif)

However, I wanted to show a greater impact, so I began looking at what the Opera Touch Background extension actually did. As it turns out, it has higher privileges and access to native functions, such as **_opr.operaTouchPrivate_** , which is a collection of functions developed for use with the My Flow application. Looking at the available functions, two cases caught my eye: _**SEND_FILE**_ and _**OPEN_FILE**_.

The SEND_FILE function retrieves information about a file provided by the user and uploads it to My Flow; it also saves the file to the user’s computer in _Downloads/MyFlow_. The OPEN_FILE is used for image files for My Flow, but while testing I noticed that you can open any type of file, not just images.

With these two functionalities, we can now have an arbitrary file write, and open, on the targeted computer. To create a real scenario I created a proof-of-concept which would first create a file _**exploit.bat**_ containing _**calc**_ , and then secondly, open the file — which would cause it to be executed, opening the Windows calculator:

`operaTouchBackground.port.postMessage({  
type: "SEND_FILE",  
name: 'exploit.bat',  
content: 'calc',  
file_type: 'image/png'  
});  
  
operaTouchBackground.port.postMessage({  
type: 'OPEN_FILE',  
localFileName: 'exploit.bat'  
});`

Finally, with a convincing user interface for the single click (dragging) needed to activate the exploit, I demonstrated how the simple XSS could be turned into remote code execution for users of the My Flow system.

The vulnerability was fixed within a few days, and a bounty was awarded around three weeks later.

Thanks for reading!  
– [Renwa](https://twitter.com/RenwaX23)

Bounty: $8,000 USD.

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
