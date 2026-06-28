---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-23_filesatck-upload-advisory-summary.md
original_filename: 2022-06-23_filesatck-upload-advisory-summary.md
title: Filesatck Upload Advisory Summary
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- information-disclosure
- api-security
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- information-disclosure
- api-security
language: en
raw_sha256: 491dfd7265da80272358993bcaf354525b2210d2fdf2349a2538f54a0187c949
text_sha256: 68a98b695c0313ee2391659d23ad255c093732587d8a3a493a5bd2be766b621a
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Filesatck Upload Advisory Summary

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-23_filesatck-upload-advisory-summary.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `491dfd7265da80272358993bcaf354525b2210d2fdf2349a2538f54a0187c949`
- Text SHA256: `68a98b695c0313ee2391659d23ad255c093732587d8a3a493a5bd2be766b621a`


## Content

---
title: "Filesatck Upload Advisory Summary"
page_title: "FileStack Upload Application Low Severity Vulnerability… | Bishop Fox"
url: "https://bishopfox.com/blog/filestack-upload-advisory"
final_url: "https://bishopfox.com/blog/filestack-upload-advisory"
authors: ["Carlos Yanez"]
programs: ["Filestack"]
bugs: ["XSS"]
publication_date: "2022-06-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2525
---

Share

[ ](https://www.facebook.com/share.php?u=https://bishopfox.com/blog/filestack-upload-advisory&amp;utm_medium=social&amp;utm_source=facebook) [ ](https://twitter.com/intent/tweet?url=https://bishopfox.com/blog/filestack-upload-advisory&utm_medium=social&utm_source=twitter&source=tweetbutton&text=) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://bishopfox.com/blog/filestack-upload-advisory&utm_medium=social&utm_source=linkedin) [ ](/feeds/advisories.rss)

## FILESTACK UPLOAD ADVISORY SUMMARY

The following document describes identified vulnerabilities in the FileStack Upload application.

### Product Vendor

FileStack

### Product Description

FileStack is a simple file uploader and powerful APIs to upload, transform & deliver any file into your app. The project’s official website is [www.filestack.com](http://www.filestack.com). The affected version was tested on January 31, 2022.

### Vulnerabilities List

One vulnerability was identified within the FileStack application:

  * Cross-site Scripting (XSS)

This vulnerability is described in the following sections.

### Affected Version

2022

### Summary of Findings

The FileStack Upload application is affected by a cross-site scripting (XSS) vulnerability  
that allows an attacker to upload SVG files with JavaScript code inside them.

### Impact

This enables JavaScript to be executed in the cdn.filestackcontent.com subdomain context and in any domain that loads the image as SVG.

### Solution

  * Display FileStack SVG images using <img> tags only.
  * Include a strong CSP if loading the image as SVG.
  * Use sandboxing if an <iframe> tag is used.
  * Strip JavaScript code from the SVG before loading.

## VULNERABILITIES

FileStack Version 2022

### Cross-site Scripting (XSS)

The FileStack Upload application is affected by a cross-site scripting (XSS) vulnerability that allows an attacker to upload SVG files with JavaScript code inside them. This enables JavaScript to be executed in the cdn.filestackcontent.com subdomain context and in any domain that loads the image as SVG.

### Vulnerability Details

_Vulnerability Type_ : Cross-site Scripting (XSS)

_Access Vector_ : ☒ Remote, ☐ Local, ☐ Physical, ☐ Context dependent, ☐ Other (if other, please specify)

_Impact_ : ☐ Code execution, ☐ Denial of service, ☒ Escalation of privileges, ☒ Information disclosure, ☐ Other (if other, please specify)

_Security Risk_ : ☐ Critical, ☐ High, ☐ Medium, ☒ Low

_Vulnerability_ : CWE-79

The FileStack Upload application is affected by a cross-site scripting (XSS) vulnerability that allows an attacker to upload SVG files with JavaScript code inside them. This enables JavaScript to be executed in the cdn.filestackcontent.com subdomain context.

To demonstrate this issue, an SVG image was crafted to include JavaScript, as shown below:
  
  
  <?xml version="1.0" standalone="no"?>
  <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
  <svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
  <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
  <script type="text/javascript">
  alert(document.domain);
  </script>
  </svg>
  

**FIGURE 1** \- JavaScript payload within SVG image

The image was then uploaded to FileStack and the resulting URL was visited in a browser to execute the JavaScript payload: `https://cdn.filestackcontent.com/DgR2ShASQvWDwOQbVxOt`

Upon detonation of the JavaScript payload, an alert box was displayed:  

![JavaScript alert box showing malicious JavaScript executed successfully.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/JavaScript-alert-box.png)

**FIGURE 2** \- JavaScript alert box

As shown above, the malicious JavaScript executed successfully. Although the payload was unable to escalate privileges within the [https://cdn.filesstackcontent....](https://cdn.filesstackcontent.com) domain, future changes to the application may introduce new vulnerabilities that could allow for escalation outside of the current domain.

## CREDITS

  * Carlos Yanez, Security Consultant III, Bishop Fox ([[email protected]](/cdn-cgi/l/email-protection#781b0119161d02381a110b1017081e1700561b1715))

## TIMELINE  

  * 01/28/2022: Initial discovery
  * 01/31/2022: Contact with vendor
  * 03/10/2022: Vendor did not respond on security channel. Forwarded to support team
  * 03/14/2022: Support reports SVG uploads is intended functionality, no comment on vulnerability
  * 03/14/2022: Clarification on vulnerability acknowledgement is requested by BishopFox
  * 04/11/2022: Second clarification on vulnerability acknowledgement is requested by BishopFox
  * 05/06/2022: Support restates SVG upload is intended functionality, no comment on vulnerability
  * 06/232022: Vulnerability publicly disclosed

* * *

![Headshot BF Carlos Yanez](https://assets.bishopfox.com/prod-1437/Images/author-photos/Headshot_BF-CarlosYanez.jpg)

By Carlos Yanez 

Carlos Yanez (CISSP, OSWE, OSCP, GWAPT, CNVP, eMAPT, MCPT) is a Senior Security Consultant at Bishop Fox. His focus areas include web and desktop [application assessments](https://bishopfox.com/services/penetration-testing-services/application-penetration-testing), [source code review](https://bishopfox.com/services/penetration-testing-services/secure-code-review), [cloud penetration tests](https://bishopfox.com/services/penetration-testing-services/cloud-penetration-testing), [product security reviews](https://bishopfox.com/services/penetration-testing-services/product-security-review), as well as [mobile devices penetration tests](https://bishopfox.com/services/penetration-testing-services/mobile-application-assessment). Prior to joining Bishop Fox, he worked on multiple e-commerce platforms as a Penetration Tester and spent years as a Web Developer and Systems Administrator. When AFK, he enjoys spending time with family and friends, lockpicking, and playing guitar.

[ More by Carlos Yanez  ](https://bishopfox.com/authors/carlos-yanez)

![](/static/assets/images/backgrounds/lander-header-bg-black-lines.svg)

Subscribe to our blog

Be first to learn about latest tools, advisories, and findings.

Thank You! You have been subscribed.
