---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-10_gsuite-hangouts-chat-5k-idor.md
original_filename: 2018-07-10_gsuite-hangouts-chat-5k-idor.md
title: Gsuite Hangouts Chat 5k IDOR
category: documents
detected_topics:
- idor
- access-control
- xss
- command-injection
- mfa
- otp
tags:
- imported
- documents
- idor
- access-control
- xss
- command-injection
- mfa
- otp
language: en
raw_sha256: f1f3f0bc105d9b5dd0d1a535acd782fa8fe96b7a9dce85eaf5793377fef665f9
text_sha256: 9d021c2961f3ce483501012b84b077ddcd2c3bd18ed0ade1ce1a25f90c8ef2da
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: true
---

# Gsuite Hangouts Chat 5k IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-10_gsuite-hangouts-chat-5k-idor.md
- Source Type: markdown
- Detected Topics: idor, access-control, xss, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: True
- Raw SHA256: `f1f3f0bc105d9b5dd0d1a535acd782fa8fe96b7a9dce85eaf5793377fef665f9`
- Text SHA256: `9d021c2961f3ce483501012b84b077ddcd2c3bd18ed0ade1ce1a25f90c8ef2da`


## Content

---
title: "Gsuite Hangouts Chat 5k IDOR"
url: "https://secreltyhiddenwriteups.blogspot.com/2018/07/gsuite-hangouts-chat-5k-idor.html"
final_url: "https://secreltyhiddenwriteups.blogspot.com/2018/07/gsuite-hangouts-chat-5k-idor.html"
authors: ["Cam (@SecretlyHidden1)"]
programs: ["Google"]
bugs: ["IDOR"]
bounty: "5,000"
publication_date: "2018-07-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5812
---

###  Gsuite Hangouts Chat 5k IDOR 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

\-  [ July 10, 2018  ](https://secreltyhiddenwriteups.blogspot.com/2018/07/gsuite-hangouts-chat-5k-idor.html "permanent link")

Hello everyone, So as most of you should see the Google VRP has started doing a bug of the week promotion. One of my submissions has been selected for this week so here we are.  
  
This is a write up about a IDOR I found back in March affecting chat.google.com.  
  
Back in March after scrolling through twitter I noticed Google Chat was trending. Immediately I thought it was a new product being pushed and started to read some of the posts about it. After looking into it the product was a new team collaboration chat room for gsuite customers and their users to message each other in. Just like most bug hunters when you see a new product being rolled out its time to go and test it.  
  
I then setup my gsuite account and went to chat.google.com. Now this was a chat area and as a result of this xss was the first thing I was testing. I did not find anything related to that but maybe someone else did ;).  
  
Since it was a new feature though I was pretty determined it had to have something so I launched up burp suite and started examining all the requests coming through.  
  
After looking for some time I noticed that on these chat rooms users can add webhooks for bots, delete them, edit them etc. These bot webhooks allow bots that are connected to the chat room to send messages to the room, read messages if the user @ the bot etc. The bot implementation could be read here https://developers.google.com/hangouts/chat/how-tos/bots-develop  
  
Now when deleting a webhook for example on burp suite this was the request that ran  
  
POST /_/DynamiteWebUi/mutate?ds.extension=115617448&f.sid=-8125538407103612547&hl=en&soc-app=534&soc-platform=1&soc-device=1&_reqid=10551185&rt=c HTTP/1.1  
Host: [chat.google.com](http://chat.google.com/)  
Connection: close  
Content-Length: 225  
X-Same-Domain: 1  
Origin: [https://chat.google.com](https://chat.google.com/)  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36  
Content-Type: application/x-www-form-urlencoded;charset=UTF-8  
X-Client-Data: ***REDACTED-SUSPECT-TOKEN***Accept: */*  
Referer: <https://chat.google.com/>  
Accept-Encoding: gzip, deflate  
Accept-Language: en,en-GB;q=0.9  
Cookie: 1P_JAR=2018-2-28-19; HSID=Abx0Xo43JAoofqOKS; SSID=ARXCoaFb-TH2GqLPQ; APISID=Q3MACqZWeAe8kt-_/AKx7734WMwG2uVZH1; SAPISID=nqYEUnsiTn_6uKOn/AdH--sbzTfjsz9cnv; NID=124=SoBxeZUELNfhi9f7mrBzcSGnZ1w8uYFn-kBYBWik5236veI2YfT78wwxQanT6_Y0OOb_HERtBK_N1MWrKXCucmVfry6GINfq8o2adBLGkErshu6inrVfM4UckgHMcEEeT9_IB93gaOMboXWYS5_9QkIecg; SID=0wVQgy4t9V79MSxExAlhwQm__pNVCp758iCRdNqh4Wi2X1A-pjQd6T3iwB-rckAX5n1xzQ.; OTZ=4292347_76_76_104100_72_446760; SIDCC=AAiTGe_-r1x0cGo-MPMgd4BrnKTQWiPe90Jw9u5LvH_***REDACTED-SUSPECT-TOKEN***f.req=%5B%22af.maf%22%2C%5B%5B%22af.add%22%2C115617448%2C%5B%7B%22115617448%22%3A%5B%5B%22space%2FAAAAbkEmhbA%22%2C%22AAAAbkEmhbA%22%2C2%5D%2C%22test3322xx%22%5D%7D%5D%5D%5D%5D&at=AJwI_LDFWIAMSGUjX3mVuYZZbn-n%3A1519845183375&  
  
Now if you look closely at the bottom of that request you should see a f.req= %5B%22af.maf%22%2C%5B%5B%22af.add%22%2C115617448%2C%5B%7B%22115617448%22%3A%5B%5B%22space%2FAAAAbkEmhbA%22%2C%22AAAAbkEmhbA%22%2C2%5D%2C%22test3322xx%22%5D%7D%5D%5D%5D%5D&  
  
If you are a diverse bug hunter the steps should be coming together here ;)  
  
You will see two types of IDs in that request  
  
First one is  
  
115617448  
  
Second one is  
  
AAAAbkEmhbA  
  
The first ID is the ID of the actual bot webhook. The second ID was the ID of the chatroom.  
  
All you had to then was simply swap the IDs with another bot webhook for example and you would delete it in this case. The whole bot webhook area was not correctly checking if you had authorization to do any actions for it though.  
  
So you could have deleted, edited, or even added your own bot webhook to anyone's chatroom and send messages etc with it.  
  
Thanks for reading and hope you enjoyed it. My twitter is linked at the top of the page if you have any other questions. 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps
