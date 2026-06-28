---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-10_2fa-verification-bypass-in-shapeshift-shapeshiftcom-write-up.md
original_filename: 2021-05-10_2fa-verification-bypass-in-shapeshift-shapeshiftcom-write-up.md
title: 2FA Verification Bypass in Shapeshift [shapeshift.com] (Write Up)
category: documents
detected_topics:
- mfa
- command-injection
- api-security
tags:
- imported
- documents
- mfa
- command-injection
- api-security
language: en
raw_sha256: 12c546d435353cfcd9daff48f87180b59041342b305666e7e35505b606626c78
text_sha256: f0261a010433a2d4a23e75615eee364de660163860fef8d37bcc96ec7f683528
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# 2FA Verification Bypass in Shapeshift [shapeshift.com] (Write Up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-10_2fa-verification-bypass-in-shapeshift-shapeshiftcom-write-up.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `12c546d435353cfcd9daff48f87180b59041342b305666e7e35505b606626c78`
- Text SHA256: `f0261a010433a2d4a23e75615eee364de660163860fef8d37bcc96ec7f683528`


## Content

---
title: "2FA Verification Bypass in Shapeshift [shapeshift.com] (Write Up)"
page_title: "Evan Ricafort | Blog: 2FA Verification Bypass in Shapeshift [shapeshift.com] (Write Up)"
url: "https://blog.evanricafort.com/2021/05/2fa-verification-bypass-in-shapeshift.html"
final_url: "https://blog.evanricafort.com/2021/05/2fa-verification-bypass-in-shapeshift.html"
authors: ["Evan Ricafort (@evanricafort)"]
programs: ["Shapeshift"]
bugs: ["2FA / MFA bypass"]
publication_date: "2021-05-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3663
---

Hello Readers!

  

Morning of Sunday 18th of April after playing video game I decided to make a quick hunt on one of the bug bounty program that I found on Google. So I fired up some of my favorite recon tools to gather information from the website and while the tools are doing their things I registered my email on the website to test on the login and reset password page. After few checks on the login page I decided to enable the 2FA verification on my account to check if there is an issue on the 2FA feature and fortunately found an interesting one.  
  
So long story short I found a 2FA verification bypass on Shapeshift which allow me access an account with 2FA enabled without giving the correct 2FA code during the login procedure. The vulnerability is easy to reproduce, A simple tampering of one of the value of the parameters in the 2FA verification request able me to bypass the feature due to lack of authentication of the app.

So below is the proof of concept of the issue. 

  

 _**\--Proof of Concept--**_

  

  

  

**_\--Timeline--_**

**_  
_**

Reported: April 18, 2021

>  _Dear Evan,_
> 
> _  
> _
> 
> _Thank you for reaching out to the ShapeShift security team! Unfortunately, we haven’t yet been able to confirm this issue. Would you be willing to double check that 2FA Verification Bypass Vulnerability truly exists?_
> 
> _  
> _
> 
> _Thank you again. It’s people like you who make the Internet a safer place!_
> 
> _  
> _
> 
> _​​_
> 
>  _ShapeShift Security Team_

  

  

I submitted another video PoC for the re-test and ended up getting duplicate, I don't know why.

  

Final Response: April 19, 2021

>  _Dear Evan,_
> 
> _  
> _
> 
> _Thank you sending more videos. We checked this issue and the security team already been made aware of this issue by another researcher. For your reference, here is the tracking number for this issue: VULN- <XXXX>._
> 
> _  
> _
> 
> _We are currently working with that researcher to resolve the issue._
> 
> _  
> _
> 
> _Thanks for taking the time to report a vulnerability to ShapeShift. It’s because of researchers like you that the web is a little bit safer._
> 
> _  
> _
> 
> _Have a wonderful day!_
> 
> _​​_
> 
>  _ShapeShift Security Team_

  

I hope you enjoy this write up.

Stay safe everyone!

  

_**“Many people lose the small joys in the hope for the big happiness.”**_

 _― Pearl S. Buck_
