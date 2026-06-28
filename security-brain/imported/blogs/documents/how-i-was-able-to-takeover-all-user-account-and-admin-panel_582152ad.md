---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-28_how-i-was-able-to-takeover-all-user-account-and-admin-panel.md
original_filename: 2018-12-28_how-i-was-able-to-takeover-all-user-account-and-admin-panel.md
title: How I Was Able To Takeover All User Account And Admin Panel
category: documents
detected_topics:
- sso
- idor
- command-injection
- path-traversal
- automation-abuse
tags:
- imported
- documents
- sso
- idor
- command-injection
- path-traversal
- automation-abuse
language: en
raw_sha256: 582152ad9db6e3cb00ca01b0e68ffa3451999e10879a4ca741e7db9731e7805c
text_sha256: 16cf35c9e1f0e9ceb86e39d5114e972a650d26de17af3f57f05bfb62bfadc1a1
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I Was Able To Takeover All User Account And Admin Panel

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-28_how-i-was-able-to-takeover-all-user-account-and-admin-panel.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, path-traversal, automation-abuse
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `582152ad9db6e3cb00ca01b0e68ffa3451999e10879a4ca741e7db9731e7805c`
- Text SHA256: `16cf35c9e1f0e9ceb86e39d5114e972a650d26de17af3f57f05bfb62bfadc1a1`


## Content

---
title: "How I Was Able To Takeover All User Account And Admin Panel"
page_title: "How I Was Able To Takeover All User Account And Admin Panel - ADDICTIVE HACKERS"
url: "https://addictivehackers.blogspot.com/2018/12/how-i-was-able-to-takeover-all-user.html"
final_url: "https://addictivehackers.blogspot.com/2018/12/how-i-was-able-to-takeover-all-user.html"
authors: ["Dipak kumar Das (@d1pakdas)"]
bugs: ["IDOR", "Account takeover"]
bounty: "1,500"
publication_date: "2018-12-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5501
---

[Home](https://addictivehackers.blogspot.com/)

[BUGBOUNTY](https://addictivehackers.blogspot.com/search/label/BUGBOUNTY)

[Bypass](https://addictivehackers.blogspot.com/search/label/Bypass)

#  How I Was Able To Takeover All User Account And Admin Panel 

Bug bounty writeup, account takeover, poc

Dipak Kumar Das

[ ](https://www.blogger.com/profile/04926341088648339962)

  
Hi everyone, This is my last write-up of 2018, so 6 months ago I got the invite from a Hackerone private program, the program has a huge scope, so currently I am focused on that single program. Found a subdomain let say abc.example.com (As it a private program so we will be using example.com instead of the original domain)  
  
So let's start  
  
The vulnerability was a pretty straightforward [IDOR](https://www.owasp.org/index.php/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet)  
  
So, the website uses sso for authentication, after successful authentication its redirect back the subdomain abc.example.com  
  
after exploring the functionality, I found its a very basic site where no option to edit your own account even, many static pages and some third party links.  
  
so after that, I navigate to the https://abc.example.com/robots.txt and found lots of hidden directories are there, like /admin, /user  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiB0T9Jq8MuSuTvpFTudgP-0HHBSQactPbZEey9MS2RxE1cpM5FFsFZAgoVgPEiu221Z8vhNB9bKCgZOZ5TixNF3jDqXDdoTE7cZC6r3EhOhA5E7ZuzNLWHsBGLYA8C5zJ8ULCUHEVucVI/s400/Screenshot_9.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiB0T9Jq8MuSuTvpFTudgP-0HHBSQactPbZEey9MS2RxE1cpM5FFsFZAgoVgPEiu221Z8vhNB9bKCgZOZ5TixNF3jDqXDdoTE7cZC6r3EhOhA5E7ZuzNLWHsBGLYA8C5zJ8ULCUHEVucVI/s1600/Screenshot_9.png)

  
so quickly I navigate to the directory /user it redirected me to https://abc.example.com/user/16397/edit  
that page provides functionality like change password, change email id, change address, add an address  
Next, I just change the value to 16390, then it's redirected me to the user edit option of the user which associated with 16390 userid  
  
Then I created another test account to verify the issue, I am successfully able to change password and email of the user  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7m8L5_GxjPEgfpKtqcRwQqhnM-ZZ2eImlzmmhAShyphenhyphenInsdo2Z_hk3upkqIJGEqN_lH5Y2JLmjF_JXAs-wU4eYaBZhTHMDy_PnBxiRXNRSUua2R21DT2p_n-thAs2BEV3PHzjSvIUUZKUQ/s1600/Screenshot_10.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7m8L5_GxjPEgfpKtqcRwQqhnM-ZZ2eImlzmmhAShyphenhyphenInsdo2Z_hk3upkqIJGEqN_lH5Y2JLmjF_JXAs-wU4eYaBZhTHMDy_PnBxiRXNRSUua2R21DT2p_n-thAs2BEV3PHzjSvIUUZKUQ/s1600/Screenshot_10.png)

  
  
Then I thought to give a try for admin panel takeover, so iIvisited to https://abc.example.com/user/1/edit  
  
its redirected to me to the portal admin panel where i can change admin password email  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkJLLmDQFBO-WKlQ3G5T_QVF17yXVC_6q2I0mGu1KT1OLhcMGVvr76Y775t8GsTWusBDKLsI1Y2pWG7VTqKYRXmWTjIAkKKv2NmN6dXkRRqBCNO8kiHEQCAU_YYw2rKnYRKqqMKW-fFGM/s1600/Screenshot_11.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkJLLmDQFBO-WKlQ3G5T_QVF17yXVC_6q2I0mGu1KT1OLhcMGVvr76Y775t8GsTWusBDKLsI1Y2pWG7VTqKYRXmWTjIAkKKv2NmN6dXkRRqBCNO8kiHEQCAU_YYw2rKnYRKqqMKW-fFGM/s1600/Screenshot_11.png)

So at that point ,i can able to takeover all user account by changing the userid value as all are sequential and admin panel too .  
  

[![](https://media.giphy.com/media/26AHszU183LU0wa6A/giphy.gif)](https://media.giphy.com/media/26AHszU183LU0wa6A/giphy.gif)

  
After 4 days they fixed the issue and got a nice bounty and bonus , that helped me to fullfill my last 2018 goal.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTdtKrIZaiIFx1hF3o_6nCyzymcJfVNLL8SoOxY71Ckfs8zuyLc9J4sx_IIi59r9uI7rTTzWDUo1Mh-v2ts0PI3VgEdab2u77Bhl2Ygh1DRDCbaGCv23tC53_qWd4VIXC_P0uzLzMLLbg/s640/Screenshot_12.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTdtKrIZaiIFx1hF3o_6nCyzymcJfVNLL8SoOxY71Ckfs8zuyLc9J4sx_IIi59r9uI7rTTzWDUo1Mh-v2ts0PI3VgEdab2u77Bhl2Ygh1DRDCbaGCv23tC53_qWd4VIXC_P0uzLzMLLbg/s1600/Screenshot_12.png)

  
  
Thanks for reading, any suggestion feedback are welcome  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

[ Previous](https://addictivehackers.blogspot.com/2018/08/a-tale-of-two-simple-account-takeover.html) [ Next ](https://addictivehackers.blogspot.com/2019/08/from-github-recon-to-account-takeover.html)

[ ](https://www.blogger.com/blog/settings/2133657112119240765 "Settings")[](https://www.blogger.com/blog/comments/2133657112119240765 "Comments")[](https://www.blogger.com/feeds/2133657112119240765/archive "Backup content")[](https://www.blogger.com/blog/stats/week/2133657112119240765 "7-days blog stats")[](https://www.blogger.com/blog/posts/2133657112119240765 "Dashboard")[](https://www.blogger.com/blog/post/edit/2133657112119240765/219758674805951953 "Edit post")

## 

## 

[#BUGBOUNTY](https://addictivehackers.blogspot.com/search/label/BUGBOUNTY) [#Bypass](https://addictivehackers.blogspot.com/search/label/Bypass) [#IDOR](https://addictivehackers.blogspot.com/search/label/IDOR)

[ ](https://www.facebook.com/sharer.php?u=https://addictivehackers.blogspot.com/2018/12/how-i-was-able-to-takeover-all-user.html) [ ](https://api.whatsapp.com/send?text=https://addictivehackers.blogspot.com/2018/12/how-i-was-able-to-takeover-all-user.html) [ ](https://twitter.com/share?url=https://addictivehackers.blogspot.com/2018/12/how-i-was-able-to-takeover-all-user.html)
