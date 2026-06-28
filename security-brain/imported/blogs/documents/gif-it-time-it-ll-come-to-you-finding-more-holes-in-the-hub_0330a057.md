---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-10-01_gif-it-time-itll-come-to-you-finding-more-holes-in-the-hub.md
original_filename: 2016-10-01_gif-it-time-itll-come-to-you-finding-more-holes-in-the-hub.md
title: gif it time it'll come to you - Finding More Holes in The Hub
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 0330a057cf973b8cd68e7f7ffac71baf93ef4e4ccfcde9f6a8f7daf235f5eaad
text_sha256: f768e2791fdf5b9c55476ebb11b00c1a1821bb6d253cefcbd53f728ca5b9785c
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# gif it time it'll come to you - Finding More Holes in The Hub

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-10-01_gif-it-time-itll-come-to-you-finding-more-holes-in-the-hub.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `0330a057cf973b8cd68e7f7ffac71baf93ef4e4ccfcde9f6a8f7daf235f5eaad`
- Text SHA256: `f768e2791fdf5b9c55476ebb11b00c1a1821bb6d253cefcbd53f728ca5b9785c`


## Content

---
title: "gif it time it'll come to you - Finding More Holes in The Hub"
url: "https://blog.zsec.uk/gif-time-pornhub/"
final_url: "https://blog.zsec.uk/gif-time-pornhub/"
authors: ["Andy Gill (@ZephrFish)"]
programs: ["PornHub"]
bugs: ["XSS"]
publication_date: "2016-10-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6253
---

[bugbounty](https://blog.zsec.uk/tag/bugbounty/)

# gif it time it'll come to you - Finding More Holes in The Hub

[ ![Andy Gill](/content/images/size/w100/2017/10/ZSIcon.png) Andy Gill ](/author/andy/)

01 Oct 2016 · 3 min read

![gif it time it'll come to you - Finding More Holes in The Hub](/content/images/size/w1000/2016/10/2016_05_12-Pornhub-Hacking-ILL_homepage-3-292656989.png)

Contents

Following suit of stored cross site scripting vulnerabilities this post will talk about another issue I found in Pornhub. Unfortunately someone found before me and as a result this bug was a duplicate. However, this is my write-up of it and how it was possible, how it worked and the madness of it!

Finding cross-site scripting vulnerabilities ain't easy and this finding was no different, as you'll see below the discovery method is pretty obscure and likely something people don't usually look for/at.

Difficulty: **Medium**  
Risk: **High**  
Affected URLs: **pornhub.com**  
Report Link: Closed as _**Duplicate**_  
Date Closed: 15th June, 2016  
Date Reported: 15th June , 2016

The issue resided within the gif generation functionality of the site, whereby an attacker could create a malicious GIF that would result in execution of malicious JavaScript via a data URI.

The gif generation functionality is located at `http://www.pornhub.com/gifgenerator` warning this is likely **NSFW**. **[You have been warned!].**

For those of you who do not know, this is what the gif generation tool looks like, simply select a video URL and it will generate a GIF of that video. To find and create the exploit GIF I was able to do the following.  
![Gif Generator](https://blog.zsec.uk/content/images/2016/09/Step1--GifSelect.png)  
Insert a random video into the create gif tool, then trap the request in burp suite or another proxy for manipulating requests. Enter any title, tags. Turn on intercept within proxy to catch the request before it gets sent to the server.

I was able to modify the title content and replace with a malicious payload:

`0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWmVwaHJGaXNoJyk8L3NjcmlwdD4="http-equiv="refresh"test=""`

By forwarding this back to the server, this should then save the image title as our payload. From here, when the GIF is visited the User's browser is directed to the data URI which is decoded to the output below and rendered in their browser.

Essentially this is a base64 string of `<script>alert("ZephrFish")</script>` An alert box has been used to demonstrate this. However, this attack will accept any javascript in the form of a data URI. The reason this attack worked was due to the way the application processed the gif title. When the gif is uploaded it would attempt to inject the title into a `twitter:meta` tag which is pre-loaded on every page the gif was displayed meaning that the attack is launched as soon as the page started to render! The offending tag can be seen in the code snippet below:

`<meta name="twitter:title" content="0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWmVwaHJGaXNoJyk8L3NjcmlwdD4="http-equiv="refresh"test=""">`

As can clearly be seen the base64 content was successfully injected into the tag and as a result was rendered when the page loaded:  
![Preload](https://blog.zsec.uk/content/images/2016/10/step1_pre-launch.jpg)

![MoneyShot](https://blog.zsec.uk/content/images/2016/10/phloadlaunch.png)

This issue has since been patched however it was a fun and interesting vulnerability to exploit through the stages and report back to Pornhub. As the original report has not been publicly disclosed on hackerone I had to request permission from Pornhub to write about this:

![AccessGranted](https://blog.zsec.uk/content/images/2016/10/permission.png)

Thanks for reading, feel free to [Follow me](https://twitter.com/ZephrFish?ref=blog.zsec.uk) on twitter or tweet me

Share [ ](https://twitter.com/intent/tweet?text=gif%20it%20time%20it'll%20come%20to%20you%20-%20Finding%20More%20Holes%20in%20The%20Hub&url=https://blog.zsec.uk/gif-time-pornhub/) [ ](https://www.linkedin.com/sharing/share-offsite/?url=https://blog.zsec.uk/gif-time-pornhub/)

[bugbounty](/tag/bugbounty/) [pornhub](/tag/pornhub/) [learning](/tag/learning/) [xss](/tag/xss/)
