---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-12-25_waze-arbitrary-file-upload.md
original_filename: 2013-12-25_waze-arbitrary-file-upload.md
title: Waze arbitrary file upload
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- api-security
language: en
raw_sha256: bfc994aad4bc0f6c1e57bfb0a61249a18b852a535e4ac27e6b3cebdd1fd99551
text_sha256: d4854440cfdfb38f7c70551d71f1b950aeabdbefb81c2e1884546081b670a3be
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Waze arbitrary file upload

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-12-25_waze-arbitrary-file-upload.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `bfc994aad4bc0f6c1e57bfb0a61249a18b852a535e4ac27e6b3cebdd1fd99551`
- Text SHA256: `d4854440cfdfb38f7c70551d71f1b950aeabdbefb81c2e1884546081b670a3be`


## Content

---
title: "Waze arbitrary file upload"
page_title: "Shashank's Security Blog: waze arbitrary file upload"
url: "http://blog.shashank.co/2013/12/waze-arbitrary-file-upload.html"
final_url: "https://blog.shashank.co/2013/12/waze-arbitrary-file-upload.html"
authors: ["Shashank (@cyberboyIndia)"]
programs: ["Google (Waze)"]
bugs: ["Unrestricted file upload", "XSS"]
bounty: "100"
publication_date: "2013-12-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6382
---

**Waze** is one of the world's largest community-based traffic and navigation app which was acquired by Google on  _June 11, 2013._ And Google opens up responsible disclosure for their acquired websites. So I thought of trying my hands over it.  

  

While I was scrolling around the pages, I found the Waze wiki which allowed users to upload files :]

  

When I tried uploading a PHP file, the response was 

  

**Files of the MIME type "application/x-php" are not allowed to be uploaded**

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpLruEfZT_-RH4WA4t0Vmek9OPldIBLoNfKGuBtiAv1D5HowLylXQgcVGX0NnDwjCbq1gF-LTk-Ifey5Sw1poWtrDP11dRF2hA14sNZDDgY2FduAXPz2ajLTkTM7m6hbWa8QbLLMImHUaP/s400/waze2.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpLruEfZT_-RH4WA4t0Vmek9OPldIBLoNfKGuBtiAv1D5HowLylXQgcVGX0NnDwjCbq1gF-LTk-Ifey5Sw1poWtrDP11dRF2hA14sNZDDgY2FduAXPz2ajLTkTM7m6hbWa8QbLLMImHUaP/s1600/waze2.PNG)

  

Well, so the website is filtering files type by checking the MIME type. So no use of uploading arbitrary files by extension spoofing ... HMMMMMM

  

  

Then again, something struck my mind. What more MIME types are filtered?? 

So I tried uploading an SWF file. BINGOOOOO!!!!!

  

SWF files are not filtered >:)  
  
So what bad I can do ??

  

Aaahhaahhh, execute an XSS with a vulnerable SWF file ;-)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjs28mbnaeqPNhpFYLtAPGCwiA6OpReFx5XNVaPyQae4orSu91gO50h75IsQiDBdcn2GHmKtKrtEYCeTOgj7ntdEgEX_RQN6q-I2qEx3wUZV4zINeK75cVnQtD9BHjMqiCIM81jNzoZzTsO/s400/wazexss.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjs28mbnaeqPNhpFYLtAPGCwiA6OpReFx5XNVaPyQae4orSu91gO50h75IsQiDBdcn2GHmKtKrtEYCeTOgj7ntdEgEX_RQN6q-I2qEx3wUZV4zINeK75cVnQtD9BHjMqiCIM81jNzoZzTsO/s1600/wazexss.PNG)

  

Aweee yeahhh!!  
  
Now they have fixed the bug :)  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQmXc2ns4iY62n7NoAdlyTgqSQf-eovThAnNFEESknPIhzhXEpETphNATaibbylXRiWcB_9RGPD_6lIc4FhbMRsBs7v6bNHH1IuUpvGax6FStzwP9SDtgPErwcgShyBzUPPZeFh5NSA-hU/s400/wazefix.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQmXc2ns4iY62n7NoAdlyTgqSQf-eovThAnNFEESknPIhzhXEpETphNATaibbylXRiWcB_9RGPD_6lIc4FhbMRsBs7v6bNHH1IuUpvGax6FStzwP9SDtgPErwcgShyBzUPPZeFh5NSA-hU/s1600/wazefix.PNG)

  
  
And they sent a 100$ reward for this :D, and my name will be listed in their reward hall of fame :)  
  
[http://www.google.co.in/about/appsecurity/hall-of-fame/reward/](https://www.google.co.in/about/appsecurity/hall-of-fame/reward/)  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitYInBcl-lsG_qVDFaEKwcJw2d0a87_f3wTlYuDqJ02hs_Pq-IqrOBYctDWtXWO4SPju9BM2TXe_tyaillqhC3oO47fTGSYwbEB4vdQd239zZB8K-sYd-saul0680xDYKofKDoTbH3ZUih/s400/reward.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitYInBcl-lsG_qVDFaEKwcJw2d0a87_f3wTlYuDqJ02hs_Pq-IqrOBYctDWtXWO4SPju9BM2TXe_tyaillqhC3oO47fTGSYwbEB4vdQd239zZB8K-sYd-saul0680xDYKofKDoTbH3ZUih/s1600/reward.PNG)

  
  
CHEERS  
Shashank (@cyberboyIndia)
