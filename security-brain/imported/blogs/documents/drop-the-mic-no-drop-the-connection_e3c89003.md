---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-29_drop-the-mic-no-drop-the-connection.md
original_filename: 2019-12-29_drop-the-mic-no-drop-the-connection.md
title: Drop the mic?! no! Drop the connection ;)
category: documents
detected_topics:
- xss
- command-injection
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- supply-chain
language: en
raw_sha256: e3c890035a14a0c66574da6dd42a8b22f9d5f77a68ba560eb020bd56e0135d34
text_sha256: 9c3a33bc74171cc39e9961d82061c80ddac77d843a0467b9c73e02d0a602c571
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Drop the mic?! no! Drop the connection ;)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-29_drop-the-mic-no-drop-the-connection.md
- Source Type: markdown
- Detected Topics: xss, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `e3c890035a14a0c66574da6dd42a8b22f9d5f77a68ba560eb020bd56e0135d34`
- Text SHA256: `9c3a33bc74171cc39e9961d82061c80ddac77d843a0467b9c73e02d0a602c571`


## Content

---
title: "Drop the mic?! no! Drop the connection ;)"
page_title: "Security blog by Sasi Levi: Drop the mic?! no! Drop the connection ;)"
url: "https://sasi2103.blogspot.com/2019/12/drop-mic-no-drop-connection.html"
final_url: "https://sasi2103.blogspot.com/2019/12/drop-mic-no-drop-connection.html"
authors: ["Sasi Levi (@sasi2103)"]
programs: ["Google"]
bugs: ["DOM XSS"]
publication_date: "2019-12-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4858
---

Hello all!!!  
  
Its been a long time since I blogged about my finding, so today I'm going to post about one of my XSS on Google and one of the tricks I use to find such bugs.  
  
Let's begin, I have a trick, which you probably know or not ;), that I'm using during my tests.  
The trick is to drop the request via burp suite and see what page I'll get. (Many researchers turn off WIFI).  
Usually, you'll end up with an error from burp suite that the request was canceled by the user, but in many cases, you'll get an error page from the site. (I need to write an extender for it!).  
  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4DHMsybh7Wn0kTRPMJ2SeETpJa-3HBwkHkwXigNEoT41mwHgZIJtr8Bi0Sz1PKLNBpmbsCoBHbT2c9PX6CUkPcF70LiF0crg3NUDlT8Kr72BHsoCfH4ZEjy7tatb1VBmWK2utIyr674/s200/Screen+Shot+2019-12-29+at+19.33.25.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4DHMsybh7Wn0kTRPMJ2SeETpJa-3HBwkHkwXigNEoT41mwHgZIJtr8Bi0Sz1PKLNBpmbsCoBHbT2c9PX6CUkPcF70LiF0crg3NUDlT8Kr72BHsoCfH4ZEjy7tatb1VBmWK2utIyr674/s1600/Screen+Shot+2019-12-29+at+19.33.25.png)  
---  
Survey error page  
  
  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLn3VabdvzZMwWwmP2ws1dSeRS_PP8rRNPkuM7kSoSiB_ibtt91i837FWTNpmosxZsgQf7swQlEHNIDgQsQm1-oHJhCAb4aY3ZJUSnOdBpWeEl14okok7lDN0E_zQ-KdCexSqulw_zepA/s200/Screen+Shot+2019-12-29+at+19.33.42.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLn3VabdvzZMwWwmP2ws1dSeRS_PP8rRNPkuM7kSoSiB_ibtt91i837FWTNpmosxZsgQf7swQlEHNIDgQsQm1-oHJhCAb4aY3ZJUSnOdBpWeEl14okok7lDN0E_zQ-KdCexSqulw_zepA/s1600/Screen+Shot+2019-12-29+at+19.33.42.png)  
---  
Burp Suite error  
  
  
  
  
  
  
I usually return to Google subdomains million times to see if there's a new change, new JS files or just to look around and see if I missed something.  
I went back to survey.google.com, which lets any user create a survey, to see if I can find bugs that I didn't find in my previous visits.  
  
After a few hours, I decided to check my trick, so here is what I did:  
  
  

1\. Login to [https://surveys.google.com/your-surveys](https://surveys.google.com/your-surveys)  
2\. Turn on your burp-suite.  
3\. Click on the 3 dots on your right and then delete.  
4\. Drop the request by burp-suite and then drop it again, total of 2 requests should be dropped.  
5\. You'll see in the browser new page with "TRY AGAIN" and "GET HELP" links.  
6\. The "TRY AGAIN" href is "javascript:window.location.href=window.location.href".  
7\. Set the URL to be [https://surveys.google.com/your-surveys?#](https://surveys.google.com/your-surveys?#)"><img src=y onerror=confirm(1)>  
8\. Chrome auditor will block your request.

  

As you can see the DOM XSS was blocked by the Chrome auditor which is enough to report to Google.

  

Happy holidays,  
Sasi
