---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-14_write-up-1000-usd-in-5-minutes-xss-stored-in-outlookcom-ios-browsers.md
original_filename: 2019-03-14_write-up-1000-usd-in-5-minutes-xss-stored-in-outlookcom-ios-browsers.md
title: Write up – $1,000 usd in 5 minutes, xss stored in outlook.com (ios browsers)
category: documents
detected_topics:
- xss
- mobile-security
- command-injection
- path-traversal
tags:
- imported
- documents
- xss
- mobile-security
- command-injection
- path-traversal
language: en
raw_sha256: 86df759f23e79fcf84a3d555e603318da0f08c66c0c25094dacf1537abd04f59
text_sha256: 1686c3cbca7799c22943eed1cb868a51784e087acfb318c3a93eaeb7a50f1520
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Write up – $1,000 usd in 5 minutes, xss stored in outlook.com (ios browsers)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-14_write-up-1000-usd-in-5-minutes-xss-stored-in-outlookcom-ios-browsers.md
- Source Type: markdown
- Detected Topics: xss, mobile-security, command-injection, path-traversal
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `86df759f23e79fcf84a3d555e603318da0f08c66c0c25094dacf1537abd04f59`
- Text SHA256: `1686c3cbca7799c22943eed1cb868a51784e087acfb318c3a93eaeb7a50f1520`


## Content

---
title: "Write up – $1,000 usd in 5 minutes, xss stored in outlook.com (ios browsers)"
page_title: "$1,000 USD, XSS STORED IN OUTLOOK.COM (IOS BROWSERS) – @omespino"
url: "https://omespino.com/write-up-1000-usd-in-5-minutes-xss-stored-in-outlook-com-ios-browsers/"
final_url: "https://omespino.com/write-up-1000-usd-in-5-minutes-xss-stored-in-outlook-com-ios-browsers/"
authors: ["Omar Espino (@omespino)"]
programs: ["Microsoft"]
bugs: ["Stored XSS"]
bounty: "1,000"
publication_date: "2019-03-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5360
---

MOBILE$1,000 USD[March 2019](/write-up-1000-usd-in-5-minutes-xss-stored-in-outlook-com-ios-browsers/)

# $1,000 USD, XSS STORED IN OUTLOOK.COM (IOS BROWSERS)

**Introduction**  
Hi everyone It’s been a while since my last post but I’m back, I want to tell you a short story about the Microsoft bug bounty program and why you can always check the basic payloads because you will surprise that some times will work:

**SPOILER ALERT:** I highly recommend [Microsoft Bug Bounty Program](https://www.microsoft.com/en-us/msrc/bounty), in my experience their program is much better compared with another big companies programs

Title XSS Stored on outlook.com (iOS) via doc file.  
**Product / URL: ​** outlook.com iOS browser (Google chrome)Report sent via secure@microsoft.com

Hi ​Microsoft Security team.

I’ve found a XSS ​stored ​ in​ ​outlook.live.com ​in iOS ​ browsers via msoffice (ppt) file.

**POC**

1.- Create a msoffice document per example a power point presentation with an hyperlink pointing to the url address **“javascript:prompt(document.cookie)”** and save as “Powerpoint presentation 97-2003 Presentation”, Is very important save the doc as 97-2003, if you don’t save the document as this version the bug reproduction may not work.

![](/assets/images/2019/03/chrome_XSS_iOS_msoffice_doc_hyperlink-1024x628.webp)

2.- Login ​in​ to ​outlook.live.com ​(outlook email)​, upload to msoffice ppt file ​and send the file via email.

3.- ​ Login into ​outlook.live.com ​(outlook email)​ in Google chrome iOS browser, open the email with the special crafted document, click the attachment and then click download, after that the document ppt will render in Google chrome ​,​ ​then click the hyperlink and see the XSS (shows up the document.cookie). ​

Something important to highlight is: At this time you have a “magic” link that points directly to the ppt special crafted document. ​

​4​ .- Open the link directly ​in Chrome iOS browser, click the hyperlink, and ​ see​ the XSS(shows up ​again ​ the document.cookie) ​, ​ if you open the link in any iOS browser like Safari, Firefox, Chrome, Opera the XSS works, you just need to be logged in your ​outlook account, only works in iOS).

![](/assets/images/2019/03/chrome_XSS_iOS_msoffice_doc.webp)

**Impact**

Stored XSS allows an attacker to embed a malicious and arbitraries scripts into a vulnerable page, which is then executed when a victim views the page.

**Environment**

\- iPhone 6 – iOS v11.2.5.  
\- Safari Latest version  
\- Google Chrome Latest version  
\- My personal email account and all testing was sending emails to myself.

**Microsoft HOF (November 2018):  
**

<https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services?rtc=1>

![](/assets/images/2019/03/microsoft-hof-nov18-596x1024.webp)

**Report Timeline**  
21 Feb 2018: Sent the report to secure@microsoft.com  
21 Feb 2018: Got confirmation from Microsoft team and team begin the investigation  
23 Mar 2018: Microsft team ask for some details  
23 Mar 2018: Sent details to Microsoft team  
26 Jul 2018: Update from the team that the investigation was still in progress  
07 Nov 2018: Update from the team that saying that it appears that the submission qualifies for Bounty  
26 Nov 2018: Microsoft Reward paid through their payment system – [Profit]  
04 March 2019: Ask for disclose permission  
14 March 2019: Disclose permission granted from Microsoft team

well that’s it, share your thoughts, what do you think about how they handle that security issue? if you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.  

[](/write-up-google-bug-bounty-lfi-on-production-servers-in-redacted-google-com-13337-usd/)

[](/tutorial-universal-android-ssl-pinning-in-10-minutes-with-frida/)
