---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-12_olx-reflected-xss-on-resend-code-link.md
original_filename: 2018-11-12_olx-reflected-xss-on-resend-code-link.md
title: OLX Reflected XSS on Resend Code link !!
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 14ac47af2282b5c243fcb71ac1f188be089ffccb5e2d56e1d2082301885a5e88
text_sha256: 2c20971cb65ca5db140141becc3de297cc878adcf2327db70193508eec1ab9ea
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# OLX Reflected XSS on Resend Code link !!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-12_olx-reflected-xss-on-resend-code-link.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `14ac47af2282b5c243fcb71ac1f188be089ffccb5e2d56e1d2082301885a5e88`
- Text SHA256: `2c20971cb65ca5db140141becc3de297cc878adcf2327db70193508eec1ab9ea`


## Content

---
title: "OLX Reflected XSS on Resend Code link !!"
page_title: "Security Blog"
url: "http://blog.h4rsh4d.com/2018/03/olx-reflected-xss-on-resend-code-link.html"
final_url: "http://blog.h4rsh4d.com/2018/03/olx-reflected-xss-on-resend-code-link.html"
authors: ["Harshad Gaikwad (@h4rsh4d)"]
programs: ["OLX"]
bugs: ["Reflected XSS"]
publication_date: "2018-11-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5596
---

* Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ March 17, 2018  ](http://blog.h4rsh4d.com/2018/03/olx-reflected-xss-on-resend-code-link.html "permanent link")

> > **OLX Reflected XSS on Resend Code link !!**  
>  **  
> ****  
> **  
> 
>> 
>> ****This is my first write up ! sharing is caring !! 😎****

This is not big finding , just one of my noob xss that i have found on OLX.in  
To change password , OLX firstly sends OTP to registered phone number and hold on for user to enter OTP number  
but on the same page they have provided the link which resend code (which get highlight after some seconds if user failed to enter the code)  
so i checked the request and response of that resend code functionality and its pretty sending mobile number and hash as parameter ph="phone number" & h="hash"  
I changed that default user "ph" value to victims number but no luck because of another parameter "h=xxxxxxxxxxxxxxxxxxxx" (hash) 😫  
  
So after that i decided to test for XSS on same functionality and found one ! ✌😜  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZdFAIdlemkMir5ZwwysuyoW2UE8w0FugOCdF3xwI8a-oK0Fiff25FHeTlufjNvdiPG6skLElKLRgpP5aakz49dJyivI3YKX3YSh4Z1Gu0XBdyfef5Kzv0UUWKe9KnlzpQxJwb53wOOM0/s640/XSS.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZdFAIdlemkMir5ZwwysuyoW2UE8w0FugOCdF3xwI8a-oK0Fiff25FHeTlufjNvdiPG6skLElKLRgpP5aakz49dJyivI3YKX3YSh4Z1Gu0XBdyfef5Kzv0UUWKe9KnlzpQxJwb53wOOM0/s1600/XSS.png)  
---  
OLX Reflected XSS  
  
  
I checked the context and entered payload in "ph" parameter ph=" onmouseover="alert(document.domain)  
  
  
Here is source code view :  
  
  
<div class="margintop10 marginbott10">  
<a href="#" class="not-active" id="sendAgain" data-phone=" " onmouseover="alert(document.domain)" >Resend code</a>  
</div>  
  
  
You can see "ph" parameter is passing his data to data-phone=" "onmouseover="alert(document.domain)  
  
Final payload : [https://www.olx.in/account/otpchangepassword/?ph=" onmouseover=" alert(document.domain)&h=xxxxxxxxxxxxxxxxxxx](https://www.olx.in/account/otpchangepassword/?ph=%22%20onmouseover=%22%20alert\(document.domain\)&h=xxxxxxxxxxxxxxxxxxx)  
  
Visited this crafted url and after some seconds when Resend Code link got active or highlight , hover mouse pointer on link and got XSS POPUP !!  
  
Here is video POC :  
  

  
  
  
OLX team have patched this vulnerability and gave me hall of fame !! 😊  
  
Thanks for Reading .. 💜💚  
  

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[shikama](https://www.blogger.com/profile/15892479843138259428)[1 November 2024 at 20:48](http://blog.h4rsh4d.com/2018/03/olx-reflected-xss-on-resend-code-link.html?showComment=1730519285252#c5289143620638426545)

GJ

Reply[Delete](https://www.blogger.com/comment/delete/2656914608170622406/5289143620638426545)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/2656914608170622406?po=1893862844893957661&hl=en-GB&saa=85391&origin=http://blog.h4rsh4d.com&skin=contempo)
