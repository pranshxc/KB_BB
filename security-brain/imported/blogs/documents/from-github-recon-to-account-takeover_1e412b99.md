---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-24_from-github-recon-to-account-takeover.md
original_filename: 2019-08-24_from-github-recon-to-account-takeover.md
title: From Github Recon To Account Takeover
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- mobile-security
language: en
raw_sha256: 1e412b992e90ad33e98fbd3bd32993df50ea72442446c8f3d2765ec83631ca7e
text_sha256: 232b7a7fba1868c8797b59522a11f7dd9923c76c713ef8c2b5e2992293e50938
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# From Github Recon To Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-24_from-github-recon-to-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `1e412b992e90ad33e98fbd3bd32993df50ea72442446c8f3d2765ec83631ca7e`
- Text SHA256: `232b7a7fba1868c8797b59522a11f7dd9923c76c713ef8c2b5e2992293e50938`


## Content

---
title: "From Github Recon To Account Takeover"
page_title: "From Github Recon To Account Takeover - ADDICTIVE HACKERS"
url: "https://addictivehackers.blogspot.com/2019/08/from-github-recon-to-account-takeover.html"
final_url: "https://addictivehackers.blogspot.com/2019/08/from-github-recon-to-account-takeover.html"
authors: ["Dipak kumar Das (@d1pakdas)"]
bugs: ["Information disclosure", "Account takeover"]
publication_date: "2019-08-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5065
---

[Home](https://addictivehackers.blogspot.com/)

[authentication](https://addictivehackers.blogspot.com/search/label/authentication)

[BUGBOUNTY](https://addictivehackers.blogspot.com/search/label/BUGBOUNTY)

#  From Github Recon To Account Takeover 

Git gub recon, bug bounty

Dipak Kumar Das

[ ](https://www.blogger.com/profile/04926341088648339962)

Hi everyone , after a long time I am doing a write-up on GitHub recon which leads to full account takeover . Few days ago I got a private invite where the in-scope target is only the mobile app.  
  
As its a private program we will take it as Example App . So I gone through all endpoint and functionality of the application , i didn't find anything critical. So I thought to give a try to their GitHub.  
  
If you want to learn how to do GitHub recon there is a detailed [tutorial](https://www.youtube.com/watch?v=l0YsEk_59fQ) by [Th3G3nt3lman](https://twitter.com/Th3G3nt3lman)  
  
  
So i started my search with the keyword **passwd** , i got 3-5 result  
  
after going through all file i got a valid password in file called config.properties  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYdXqpyjYJtmByK7XokwzIlWhqW4svp4arV3j-uxU6t62F6WijU1ZCfNE58zcicF1Ea8e30lB_kaJm4hWC7c6SUbtTe0wiO2o8hm48fdUcalR0LBlJoZDIvZRz498Rm_qYjShLL_geKuw/s640/Screenshot_145.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYdXqpyjYJtmByK7XokwzIlWhqW4svp4arV3j-uxU6t62F6WijU1ZCfNE58zcicF1Ea8e30lB_kaJm4hWC7c6SUbtTe0wiO2o8hm48fdUcalR0LBlJoZDIvZRz498Rm_qYjShLL_geKuw/s1600/Screenshot_145.png)

  
So that app using OTP based authentication and i got the credential for the third party service , which they are using for the SMS.  
  
Using those credential I logged into the SMS provider portal , there is a section call SMS delivery where all SMS delivery report are stored along with the Phone number and the text sent to that number.  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuUJh9QsNFxfj4XUKxt1rKQz8gz6Tpdax376lq6axraxGmCkh2EUjGe0nloGAtXS-1B65MhT_FT5vP48tcIJ34DgZQugMPvKYaMGbjsm4bijlljMmeTb7_1_5qJb3OCdyk60bOCCm8FuE/s640/6wPYotSY.png+large.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuUJh9QsNFxfj4XUKxt1rKQz8gz6Tpdax376lq6axraxGmCkh2EUjGe0nloGAtXS-1B65MhT_FT5vP48tcIJ34DgZQugMPvKYaMGbjsm4bijlljMmeTb7_1_5qJb3OCdyk60bOCCm8FuE/s1600/6wPYotSY.png+large.png)

  
So now i have all registered users mobile number and OTP delivery report along with OTP  
  
  
So i just request for OTP and from the delivery report got the valid OTP and loggedin to any user's account 😎  
  

[![](https://media.giphy.com/media/iNqNlmBrb7iQ4gsmVo/giphy.gif)](https://media.giphy.com/media/iNqNlmBrb7iQ4gsmVo/giphy.gif)

  
Hope you guys like it , share your feedback in commen.  
  
  
  
  

[ Previous](https://addictivehackers.blogspot.com/2018/12/how-i-was-able-to-takeover-all-user.html) [ Next ](https://addictivehackers.blogspot.com/2020/06/buying-gift-can-cost-you-your-pii-data.html)

[ ](https://www.blogger.com/blog/settings/2133657112119240765 "Settings")[](https://www.blogger.com/blog/comments/2133657112119240765 "Comments")[](https://www.blogger.com/feeds/2133657112119240765/archive "Backup content")[](https://www.blogger.com/blog/stats/week/2133657112119240765 "7-days blog stats")[](https://www.blogger.com/blog/posts/2133657112119240765 "Dashboard")[](https://www.blogger.com/blog/post/edit/2133657112119240765/9045206553579211038 "Edit post")

## 

## 

[#authentication](https://addictivehackers.blogspot.com/search/label/authentication) [#BUGBOUNTY](https://addictivehackers.blogspot.com/search/label/BUGBOUNTY) [#Bypass](https://addictivehackers.blogspot.com/search/label/Bypass)

[ ](https://www.facebook.com/sharer.php?u=https://addictivehackers.blogspot.com/2019/08/from-github-recon-to-account-takeover.html) [ ](https://api.whatsapp.com/send?text=https://addictivehackers.blogspot.com/2019/08/from-github-recon-to-account-takeover.html) [ ](https://twitter.com/share?url=https://addictivehackers.blogspot.com/2019/08/from-github-recon-to-account-takeover.html)
