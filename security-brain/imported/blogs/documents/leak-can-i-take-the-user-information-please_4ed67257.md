---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-29_leak-can-i-take-the-user-information-please.md
original_filename: 2019-10-29_leak-can-i-take-the-user-information-please.md
title: '[Leak] Can I take the user information, please?!!'
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
- mobile-security
language: en
raw_sha256: 4ed67257fd6599c3730471bfb5ed7d492bb9d17bb49d50750dc1f12f213d6212
text_sha256: 5832fe2a143488e160ce5bdd0c3aad5ade02c07598b1e7137c65fe71310725b6
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# [Leak] Can I take the user information, please?!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-29_leak-can-i-take-the-user-information-please.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `4ed67257fd6599c3730471bfb5ed7d492bb9d17bb49d50750dc1f12f213d6212`
- Text SHA256: `5832fe2a143488e160ce5bdd0c3aad5ade02c07598b1e7137c65fe71310725b6`


## Content

---
title: "[Leak] Can I take the user information, please?!!"
url: "https://flex0geek.blogspot.com/2019/10/leak-can-i-take-user-information-please.html"
final_url: "https://flex0geek.blogspot.com/2019/10/leak-can-i-take-user-information-please.html"
authors: ["Mohamed Sayed (@FlEx0Geek)"]
bugs: ["Information disclosure"]
publication_date: "2019-10-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4968
---

###  [Leak] Can I take the user information, please?!! 

on  [ October 29, 2019  ](https://flex0geek.blogspot.com/2019/10/leak-can-i-take-user-information-please.html "permanent link")

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEim2kZzTAGG4YcIomLYiugXHU8SRWkYfnl6Z-lhvdrIQcBsMifemtWYHpoH0x22IJhI_u61ABrtHJ_PZovgsiGVpZjCemECdZlMDOL_ovtgCGMtWGsaX3IPYihgr-WoE8n-UhtNj8p6758/s640/s.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEim2kZzTAGG4YcIomLYiugXHU8SRWkYfnl6Z-lhvdrIQcBsMifemtWYHpoH0x22IJhI_u61ABrtHJ_PZovgsiGVpZjCemECdZlMDOL_ovtgCGMtWGsaX3IPYihgr-WoE8n-UhtNj8p6758/s1600/s.jpg)

  
Hi again it's me :P, I found a cool bug on a private program I wanna share with you.  
  
Like every time I start testing on a target I opened my Burp Suite and start visit every link and send a requests to the website to collect the endpoints, and paths and when I try to add a user on my account I write test on the name and I found that the page send an automatic request to an endpoint to check if this username available or not the endpoint form is  
  
https://target.com/api/user/endpoint_name?q=  
  
the value of username which you write on the input field will be added to the q parameter and the server will send a post request to the endpoint the problem here is the response which gives me a lot of information about this username like email, phone number, UUID, company's information, and a lot of other information almost all of the account information except password, it was cool for me but it's not very cool because I should get the username to get this information I continue testing and get some endpoints I found a very coooooooooool thing another parameter on the same endpoint which is size you give it a size of output information what this means? if my output is 1000 I just wanna see 10 outputs now I will use this parameter like that size=10 it will show just 10 outputs, not all 1000 what is the cool thing here? the cool thing is when I set the q parameter empty and give the endpoint a size it will respond with users' information too if I give the size parameter a value 100 the endpoint will response with 100 users information like I said before almost all information of the account, it was a cool bug I like it so much :P, so if I used this link to get the information  
  
https://target.com/api/user/endpoint_name?q=&size=100  
  
  
in the end, I hope this is good for you and thanks for reading my topic, Goodbye.  
  

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/07730471447607815411)[November 9, 2019 at 9:18 PM](https://flex0geek.blogspot.com/2019/10/leak-can-i-take-user-information-please.html?showComment=1573363136349#c1635243281564320469)

hi. my name is mehdi. i read write-up in CTF write-up.  
it is very good. you are professional. well done. may you help me.  
my job is penetration tester but i am not professional. i have knowledge in information security and web security and mobile security. i want become professional in bug-bounty. please help me.  

Reply[Delete](https://www.blogger.com/comment/delete/7853305107519134332/1635243281564320469)

Replies

  1. ![](//4.bp.blogspot.com/-RCluX9M2Ul8/Zi-EQwWbd4I/AAAAAAAAZuo/Xr6trR6LS2kIHwQgZQSbr6Yd3o_KeUsvwCK4BGAYYCw/s35/IMG_8527.jpg)

[Mohamed Sayed (Flex)](https://www.blogger.com/profile/04130844926048047329)[April 4, 2020 at 1:12 AM](https://flex0geek.blogspot.com/2019/10/leak-can-i-take-user-information-please.html?showComment=1585987936407#c6446557357025763968)

you can talk with me here https://www.facebook.com/flex0geek

[Delete](https://www.blogger.com/comment/delete/7853305107519134332/6446557357025763968)

Replies

Reply

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/7853305107519134332?po=6435327416368145168&hl=en&saa=85391&origin=https://flex0geek.blogspot.com&skin=emporio)
