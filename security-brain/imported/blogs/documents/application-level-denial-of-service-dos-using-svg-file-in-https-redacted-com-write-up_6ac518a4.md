---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-10_application-level-denial-of-service-dos-using-svg-file-in-httpsredactedcom-write.md
original_filename: 2019-08-10_application-level-denial-of-service-dos-using-svg-file-in-httpsredactedcom-write.md
title: Application Level Denial of Service [DoS] using SVG file in https://[REDACTED].com
  (Write Up)
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 6ac518a40cce3d01c4c9af938e2a8cc85b5c066966185c680160167d577e6c9a
text_sha256: 3b5ffaf60d06f150ee64ad7292b2560ea107fb355f465676c188633ae834abc1
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Application Level Denial of Service [DoS] using SVG file in https://[REDACTED].com (Write Up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-10_application-level-denial-of-service-dos-using-svg-file-in-httpsredactedcom-write.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `6ac518a40cce3d01c4c9af938e2a8cc85b5c066966185c680160167d577e6c9a`
- Text SHA256: `3b5ffaf60d06f150ee64ad7292b2560ea107fb355f465676c188633ae834abc1`


## Content

---
title: "Application Level Denial of Service [DoS] using SVG file in https://[REDACTED].com (Write Up)"
page_title: "Evan Ricafort | Blog: Application Level Denial of Service [DoS] using SVG file in https://[REDACTED].com (Write Up)"
url: "https://blog.evanricafort.com/2019/08/application-level-denial-of-service-dos.html"
final_url: "https://blog.evanricafort.com/2019/08/application-level-denial-of-service-dos.html"
authors: ["Evan Ricafort (@evanricafort)"]
bugs: ["Application-level DoS"]
bounty: "300"
publication_date: "2019-08-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5088
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXgwmtYCoBq6SFBJCPlpANLiFgDhVtrU9tI98ahAKjg77Ng3VIKtfDm0EKjEjd1ZwVmqSh892TTWMEdEWzuTcd8c65z6aLFh_A_YUhFUf8rnuKzNc38m_NZC77lIw2XFmTrhu9YFez/s640/Untitled+2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXgwmtYCoBq6SFBJCPlpANLiFgDhVtrU9tI98ahAKjg77Ng3VIKtfDm0EKjEjd1ZwVmqSh892TTWMEdEWzuTcd8c65z6aLFh_A_YUhFUf8rnuKzNc38m_NZC77lIw2XFmTrhu9YFez/s1600/Untitled+2.jpg)

  
A year ago I participated on this private program on Bugcrowd and found some good quality vulnerabilities which earns me a good amount of bounty and one of my favorite vulnerability was this Application Level DoS (Denial of Service) using a malicious SVG file. This is my first time reporting this kind of issue that time though I reported some SVG file related vulnerabilities but this one is new to me since it was a Denial of Service using the SVG and it makes me feel more excited about it before.  
  
So after my first report was rewarded by them which is a Stored XSS using SVG file, I continued digging down on the same area and luckily found this issue. What really makes this as one of my favorite vulnerability that I found is because I learned something new from the Triaged person who handle this report. I learned something new from him because of this report.  
  
So long story short, here's the report timeline and proof of concept.  
  
_**\--Proof of Concept--**_  
  
1\. Go to https://<REDATED> then login  
2\. Go to https://<REDATED>/<username>/primary-brand  
3\. Click the Edit button or turn ON the Edit button in the upper left conrner of the page  
4\. In the Images section upload the attach SVG file.  
5\. Open the upload SVG file and see the result.  
  
I have attached a GIF file for the whole demonstration of the bug, I hope you understand.  
  
Live Demo of my test: https://user-images.<REDATED>/<userid>/primary-brand/<filename>.svg  
  
Tested in Firefox which results into browser crash and Google Chrome which also results into browser crash.  
  
_**\--Timeline--**_  
  
Report Title: DoS using SVG file in https://<REDACTED>  
Reported: 17, February 2018 16:52:37 UTC  
Update (Triaged Staff): 21 Feb 2018 17:24:32 UTC  
  

> _Hello evanricafort,_  
>  _The crashing of your browser must have been because of out of memory bounds. Can you try to use Windbg to check why it crashed? It allows me to check if there is a break instruction exception. This is not reproducible in my Chrome, Safari, and Firefox in Mac thus I would like to check the output from Windbg to check if this is indeed a vulnerability._

My Update Response: 21 Feb 2018 18:04:50 UTC  
  

> _not really familiar with windbg but I tried it with my firefox browser and this is what I got_  
>  _Microsoft (R) Windows Debugger Version 10.0.16299.91 AMD64  
>  Copyright (c) Microsoft Corporation. All rights reserved._  
>  _*** wait with pending attach  
>  Symbol search path is: srv*  
>  Executable search path is:  
>  ModLoad: 00007ff6`6ca80000 00007ff6`6caf7000 C:\Program Files\Mozilla Firefox\firefox.exe  
>  ModLoad: 00007ff9`bb8b0000 00007ff9`bba71000 C:\Windows\SYSTEM32\ntdll.dll  
>  ModLoad: 00007ff9`bb070000 00007ff9`bb11d000 C:\Windows\system32\KERNEL32.DLL  
>  ModLoad: 00007ff9`b89c0000 00007ff9`b8ba8000 C:\Windows\system32\KERNELBASE.dll  
>  ModLoad: 00007ff9`b97b0000 00007ff9`b9857000 C:\Windows\system32\ADVAPI32.dll  
>  ModLoad: 00007ff9`b9280000 00007ff9`b931d000 C:\Windows\system32\msvcrt.dll  
>  ModLoad: 00007ff9`ac2e0000 00007ff9`ac305000 C:\Program Files\Mozilla Firefox\mozglue.dll  
>  ModLoad: 00007ff9`bb310000 00007ff9`bb36b000 C:\Windows\system32\sechost.dll  
>  ModLoad: 00007ff9`b8cb0000 00007ff9`b8dcd000 C:\Windows\system32\RPCRT4.dll  
>  ModLoad: 00007ff9`b4610000 00007ff9`b461a000 C:\Windows\SYSTEM32\VERSION.dll  
>  ModLoad: 00007ff9`aa550000 00007ff9`aa5ee000 C:\Program Files\Mozilla Firefox\MSVCP140.dll  
>  ModLoad: 00007ff9`ac400000 00007ff9`ac417000 C:\Program Files\Mozilla Firefox\VCRUNTIME140.dll  
>  ModLoad: 00007ff9`b7170000 00007ff9`b7264000 C:\Windows\SYSTEM32\ucrtbase.dll  
>  ModLoad: 00007ff9`b79d0000 00007ff9`b79db000 C:\Windows\SYSTEM32\CRYPTBASE.DLL  
>  ModLoad: 00007ff9`b8890000 00007ff9`b88fa000 C:\Windows\system32\bcryptPrimitives.dll  
>  ModLoad: 000001b2`46430000 000001b2`46434000 C:\Program Files\Mozilla Firefox\api-ms-win-crt-runtime-l1-1-0.dll  
>  ModLoad: 000001b2`46440000 000001b2`46444000 C:\Program Files\Mozilla Firefox\api-ms-win-crt-string-l1-1-0.dll  
>  ModLoad: 000001b2`46450000 000001b2`46453000 C:\Program Files\Mozilla Firefox\api-ms-win-crt-heap-l1-1-0.dll  
>  ModLoad: 000001b2`46460000 000001b2`46464000 C:\Program Files\Mozilla Firefox\api-ms-win-crt-stdio-l1-1-0.dll  
>  ModLoad: 000001b2`46470000 000001b2`46474000 C:\Program Files\Mozilla Firefox\api-ms-win-crt-convert-l1-1-0.dll  
>  ModLoad: 000001b2`46480000 000001b2`46483000 C:\Program Files\Mozilla Firefox\api-ms-win-crt-locale-l1-1-0.dll  
>  ModLoad: 000001b2`46490000 000001b2`46495000 C:\Program Files\Mozilla Firefox\api-ms-win-crt-math-l1-1-0.dll  
>  ModLoad: 000001b2`464a0000 000001b2`464a5000 C:\Program Files\Mozilla Firefox\api-ms-win-crt-multibyte-l1-1-0.dll  
>  ModLoad: 000001b2`464c0000 000001b2`464c3000 C:\Program Files\Mozilla Firefox\api-ms-win-crt-time-l1-1-0.dll  
>  ModLoad: 000001b2`464d0000 000001b2`464d3000 C:\Program Files\Mozilla Firefox\api-ms-win-crt-filesystem-l1-1-0.dll_

  

> _.............................................._

  

> _**ModLoad: 00007ff9`b0400000 00007ff9`b0674000 C:\Windows\WinSxS\amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.10586.839_none_a2ddba30a539a2ae\comctl32.dll  
>  (2a84.2b90): Break instruction exception - code 80000003 (first chance)  
>  ntdll!DbgBreakPoint:  
>  00007ff9`bb958860 cc int 3**_

Follow-up Update (Triaged Staff): 23 Feb 2018 16:16:43 UTC  
  

> _Hello Evan,  
>  
>  Based on the breakpoint, it did crash from your end:  
>  
> ModLoad: 00007ff9b0400000 00007ff9b0674000 C:\Windows\WinSxS\amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.10586.839_none_a2ddba30a539a2ae\comctl32.dll  
> (2a84.2b90): Break instruction exception - code 80000003 (first chance)  
> ntdll!DbgBreakPoint:  
> 00007ff9`bb958860 cc int 3  
>  
> Windbg allows us to check if there is a DoS or if it has overwritten the EIP / instruction pointer, etc. In this case, it tells us that a crash has actually occurred. Since this is reproducible from your end and not for all users, I am marking this issue as P3. _

  
Closed: 06 Jul 2018 20:28:52 UTC (Won't fix)  

> _Thank you for your help in making`<REDACTED>` safer. The application will be sunset very soon and development has ceased. Therefore we are closing the reported issue as **WON'T FIX**. _

Reward: $300 + 10 Kudos points  
_****_  
So I hope you enjoy this write up and have a great day everyone!  
  

**_"Opportunities don't happen. You create them."_**

_― Chris Grosser_
