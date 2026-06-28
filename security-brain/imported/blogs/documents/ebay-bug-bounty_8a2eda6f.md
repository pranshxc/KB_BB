---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-06-06_ebay-bug-bounty.md
original_filename: 2014-06-06_ebay-bug-bounty.md
title: ebay bug bounty
category: documents
detected_topics:
- xss
- command-injection
- cloud-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- cloud-security
- supply-chain
language: en
raw_sha256: 8a2eda6f3564791f4baad6fb86bba69c20e3194773c58fad203da7bf604decfc
text_sha256: 19ce2a6361a0cd71635fc753fdceb77a1872cc0db04bdfeb1f55e6fb636206b1
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# ebay bug bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-06-06_ebay-bug-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `8a2eda6f3564791f4baad6fb86bba69c20e3194773c58fad203da7bf604decfc`
- Text SHA256: `19ce2a6361a0cd71635fc753fdceb77a1872cc0db04bdfeb1f55e6fb636206b1`


## Content

---
title: "ebay bug bounty"
page_title: "eBay Mobile Reflected XSS  Disclosure Writeup – The Hacker Blog"
url: "https://thehackerblog.com/ebay-mobile-reflected-xss-disclosure-writeup/index.html"
final_url: "https://thehackerblog.com/ebay-mobile-reflected-xss-disclosure-writeup/index.html"
authors: ["Matthew Bryant (@IAmMandatory)"]
programs: ["Ebay"]
bugs: ["Reflected XSS"]
publication_date: "2014-06-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6370
---

# eBay Mobile Reflected XSS Disclosure Writeup

Thought I’d write a post on my experience with eBay’s security submission team and also to keep an archive of my various bug submissions.

The vulnerability was reflected XSS due to improper sanitation of a user inputted parameter itemId in eBay mobile. Found it manually by just tampering inputs and watching the output.

# The XSS

![Yummy Cookies](/wp-content/uploads/2014/06/tempFileForShare.jpg)

Yummy Cookies 

[http://m.ebay.com/recfb?sid=adoramacamera&itemId=331087337021%22%20onclick%3D%22alert%28document.cookie%29](http://m.ebay.com/recfb?sid=adoramacamera&itemId=331087887021%22%20onclick%3D%22alert%28document.cookie%29)

Yep, it was really that simple, oddly enough. I reported it initially and got an automated response stating to not contact them with the bug status **for any reason** and that they would get back to me eventually.

So I waited…and waited…and waited. A few months later I felt that I had waited more than enough – I understand they are most likely busy but I contacted them. Turns out they had lost the message! Oops! After resubmitting the bug to them they added me to the eBay hall of fame promptly and everything was smooth from there.

Overall I’d say eBay was a very nice and straightforward company to report to. Even though they don’t run a proper bug bounty program the hall of fame is always cool for researchers ![:\)](https://thehackerblog.com/wp-includes/images/smilies/simple-smile.png)

For those looking to report vulnerabilities in eBay check out this link to submit: <http://ebay.com/securitycenter/Researchers.html>

The eBay hall of fame: <http://ebay.com/securitycenter/ResearchersAcknowledgement.html>

Until next time,

-mandatory

[cross site scripting ebay](/tags#cross site scripting ebay "Pages tagged cross site scripting ebay")[ebay bug bounty](/tags#ebay bug bounty "Pages tagged ebay bug bounty")[ebay mobile xss](/tags#ebay mobile xss "Pages tagged ebay mobile xss")[ebay security team](/tags#ebay security team "Pages tagged ebay security team")[ebay submission](/tags#ebay submission "Pages tagged ebay submission")[ebay xss](/tags#ebay xss "Pages tagged ebay xss")[hall of fame](/tags#hall of fame "Pages tagged hall of fame") Matthew Bryant (mandatory)

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=/ebay-mobile-reflected-xss-disclosure-writeup/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=/ebay-mobile-reflected-xss-disclosure-writeup/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=/ebay-mobile-reflected-xss-disclosure-writeup/ "Share on Google Plus")

[About the Author](https://thehackerblog.com)

### Matthew Bryant (mandatory)

![Matthew Bryant \(mandatory\)](/images/avatar.jpg)

Security researcher who needs to sleep more. Opinions expressed are solely my own and do not express the views or opinions of my employer.

  * [__](https://github.com/mandatoryprogrammer)
  * [__](https://www.linkedin.com/in/matthew-bryant-a9403289/)

[Follow @mandatoryprogrammer](https://github.com/mandatoryprogrammer)  
[Follow @IAmMandatory](https://twitter.com/IAmMandatory)

[Read More](/crossdomain-xml-proof-of-concept-tool/)

### ["Zero-Days" Without Incident - Compromising Angular via Expired npm Publisher Email Domains](/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/)

**NOTE:** *If you're just looking for the high level points, see the"[The TL;DR Summary & High-LevelPoints](#the-tldr-summary--high-level...… [Continue reading](/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/)

#### [Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass (~15.5 Million Affected)](/video-download-uxss-exploit-detailed/ "Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass \(~15.5 Million Affected\)")

Published on February 22, 2019

#### [Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions](/kicking-the-rims-a-guide-for-securely-writing-and-auditing-chrome-extensions/ "Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions")

Published on June 12, 2018
