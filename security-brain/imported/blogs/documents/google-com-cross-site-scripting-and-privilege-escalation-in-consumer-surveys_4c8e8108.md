---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-01-03_googlecom-cross-site-scripting-and-privilege-escalation-in-consumer-surveys.md
original_filename: 2013-01-03_googlecom-cross-site-scripting-and-privilege-escalation-in-consumer-surveys.md
title: Google.com cross site scripting and privilege escalation in Consumer Surveys
category: documents
detected_topics:
- access-control
- xss
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- access-control
- xss
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 4c8e8108db2ca1468946e230bc6c293dbd3c887fa8c41517fe4b1a3064a1a789
text_sha256: 2a046c6181aebc618bdeb947e9effca9e5825f782052c1b85ba2e684f15895c1
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Google.com cross site scripting and privilege escalation in Consumer Surveys

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-01-03_googlecom-cross-site-scripting-and-privilege-escalation-in-consumer-surveys.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `4c8e8108db2ca1468946e230bc6c293dbd3c887fa8c41517fe4b1a3064a1a789`
- Text SHA256: `2a046c6181aebc618bdeb947e9effca9e5825f782052c1b85ba2e684f15895c1`


## Content

---
title: "Google.com cross site scripting and privilege escalation in Consumer Surveys"
page_title: "Josip Franjković - archived security blog: Google.com cross site scripting and privilege escalation in Consumer Surveys"
url: "https://josipfranjkovic.blogspot.com/2013/01/googlecom-cross-site-scripting-and.html"
final_url: "https://josipfranjkovic.blogspot.com/2013/01/googlecom-cross-site-scripting-and.html"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Google"]
bugs: ["Stored XSS", "Broken authorization"]
publication_date: "2013-01-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6413
---

Hello,  
  
I have recently found a persistent cross site scripting and privilege escalation in [Google Consumer Surveys](//www.google.com/insights/consumersurveys/home). Here are proofs of concept for both vulnerabilities:  

**Cross site scripting (XSS)**

  
You can create a new Google Consumer Survey [here](//www.google.com/insights/consumersurveys/create). I have entered **" </script><script>alert(document.cookie)</script> **as name of my survey and clicked Continue. The JavaScript was executed. Now the problem was, how do I exploit this on other users?  
When creating a survey, there are four steps. Step 1,3 and 4 links could be used to exploit it on other users, while Step 2 (still) gives a 500 Internal server error if viewing other people's surveys (I do not know why, maybe you can find something there :)). Here are the 3 links (the survey is deleted).  
  

  * http://www.google.com/insights/consumersurveys/create?survey=c2mexgsedz4dc

  * http://www.google.com/insights/consumersurveys/create/questions/edit?survey=c2mexgsedz4dc

  * http://www.google.com/insights/consumersurveys/create/confirm?survey=c2mexgsedz4dc

Visiting any of those three links would execute the JavaScript in your browser.  
Screenshot:

  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNOAmFX8nDwHtLkPPM8x45Cj6djrDrCVaFBKxeLKIF_ritaaoGjD3Qwh9MPhKXmYpxcjHqc38_492OUYpUKCuMk3Tpebc2Pay4uamQi5wNFI2F75BpXJXGE2VZwCqnlwfU-vTpIeTEYZeO/s640/xss.png)  

  

  

**Privilege escalation**  
In the same service, you could delete anyone's Consumer Survey with a single POST request. Keep in mind that this is a [paid](//www.google.com/insights/consumersurveys/pricing) Google service.**  
**  
A POST request to this URL with following parameters:  
  
http://www.google.com/insights/consumersurveys/delete_survey  
  
POST parameters:  
survey=**c2mexgsedz4dc**  
&xsrf-token=[Your-XSRF-token]&action=delete  
  
You could change **survey** parameter to any valid survey, and it would get deleted.  
When trying to visit a deleted survey, 500 Internal Server Error would pop out, and you wouldn't be able to view it.  
  
Thank you Google Security team for quick response and fix!
