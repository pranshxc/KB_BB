---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-12-19_imgur-xss.md
original_filename: 2013-12-19_imgur-xss.md
title: Imgur xss
category: documents
detected_topics:
- xss
- jwt
- command-injection
tags:
- imported
- documents
- xss
- jwt
- command-injection
language: en
raw_sha256: 46376ea0b63cd53a4cbf7c5b3858d8902539c275772da6040bc2bb1790215d89
text_sha256: bbf9d37e14851c88cd699dbc61a4d9351e46d55ba3570c51cd56b46be672f550
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Imgur xss

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-12-19_imgur-xss.md
- Source Type: markdown
- Detected Topics: xss, jwt, command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `46376ea0b63cd53a4cbf7c5b3858d8902539c275772da6040bc2bb1790215d89`
- Text SHA256: `bbf9d37e14851c88cd699dbc61a4d9351e46d55ba3570c51cd56b46be672f550`


## Content

---
title: "Imgur xss"
page_title: "Shashank's Security Blog: Imgur xss"
url: "http://blog.shashank.co/2013/12/imgur-xss.html"
final_url: "https://blog.shashank.co/2013/12/imgur-xss.html"
authors: ["Shashank (@cyberboyIndia)"]
programs: ["Imgur"]
bugs: ["XSS"]
publication_date: "2013-12-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6383
---

Imgur is an online image hosting service founded by Alan Schaaf in 2009 in Athens, Ohio. Imgur describes itself as "the home to the web's most popular image content, curated in real-time by a dedicated community through commenting, voting and sharing.  
I spotted a cross-site scripting vulnerability in <http://imgur.com/> on 6 FEB 2013.  
_  
__  
_  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirKdXeKyim4IvqznE_qpFz_kodB91Beg5vq1m6HJza6SMUY6Zwv8zkYs0L5ysNu6ONQBvgtGgrIRomOUrg3BbcwAUW4e-sunhubSEU3PUh0DprEQFqRIrPQnxdprtVvwtO27v5QlYx_fFH/s400/imgurxss.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirKdXeKyim4IvqznE_qpFz_kodB91Beg5vq1m6HJza6SMUY6Zwv8zkYs0L5ysNu6ONQBvgtGgrIRomOUrg3BbcwAUW4e-sunhubSEU3PUh0DprEQFqRIrPQnxdprtVvwtO27v5QlYx_fFH/s1600/imgurxss.PNG)

  

I reported the issue to them on the very day I found it and the same day they replied. After 2-3 days the bug was fixed.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGYCqiMR0C4mcOGJA2d5_0RxcBIFauMsRMXJavcPlJws023bn7iTIYFTp4u_yPlgN46yoRqj980W_PRm7ba238Oq_GD5nFMnxzeQFnl2_3T_dJt8OJ36MEx9fTH5i-6tC61117KFkTVxKY/s400/imgur.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGYCqiMR0C4mcOGJA2d5_0RxcBIFauMsRMXJavcPlJws023bn7iTIYFTp4u_yPlgN46yoRqj980W_PRm7ba238Oq_GD5nFMnxzeQFnl2_3T_dJt8OJ36MEx9fTH5i-6tC61117KFkTVxKY/s1600/imgur.PNG)

  
  
Cheers :)  
Shashank
