---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-02_how-i-found-stored-xss-on-your-domainredactedcom.md
original_filename: 2018-10-02_how-i-found-stored-xss-on-your-domainredactedcom.md
title: How i found Stored xss on your-domain.redacted.com
category: documents
detected_topics:
- xss
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: de822f340de12e1c91ad9f9ee1688e472d59ea8cbba4fe385ff4dbc51a97db00
text_sha256: ead16fc595f5ef2566bfbb473e7e7e96a30c10d9bf08a9d6df8abefd1a6441d0
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How i found Stored xss on your-domain.redacted.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-02_how-i-found-stored-xss-on-your-domainredactedcom.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `de822f340de12e1c91ad9f9ee1688e472d59ea8cbba4fe385ff4dbc51a97db00`
- Text SHA256: `ead16fc595f5ef2566bfbb473e7e7e96a30c10d9bf08a9d6df8abefd1a6441d0`


## Content

---
title: "How i found Stored xss on your-domain.redacted.com"
url: "https://rudr4sarkar.blogspot.com/2018/10/how-i-found-stored-xss-on-your.html"
final_url: "https://rudr4sarkar.blogspot.com/2018/10/how-i-found-stored-xss-on-your.html"
authors: ["Rudra Sarkar (@rudr4_sarkar)"]
bugs: ["XSS"]
publication_date: "2018-10-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5670
---

###  How i found Stored xss on your-domain.redacted.com 

[ October 02, 2018  ](https://rudr4sarkar.blogspot.com/2018/10/how-i-found-stored-xss-on-your.html "permanent link")

Hay,  
  
Today i am going to show how i found XSS on site your-domain.redacted.com who provide **Help Desk & Live Chat Software**.  
  
  
Now in the signup page i am trying to create a account with the payload in **Full name** but it showing error "**Invalid name on name** "  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1-SS7Fx45zsTllzaHXX_tP1tL6Di9tvzG0DiHc1n2u5K4pJt9UNmaEhPQ7soywspvF1nRw8l_2rfoPiVTJnK5cRh_-5USuXiGf58BQDWQEGLt0Qo3j-mRJvcLa8bUL8t4TnVJUwraIm91/s320/1.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1-SS7Fx45zsTllzaHXX_tP1tL6Di9tvzG0DiHc1n2u5K4pJt9UNmaEhPQ7soywspvF1nRw8l_2rfoPiVTJnK5cRh_-5USuXiGf58BQDWQEGLt0Qo3j-mRJvcLa8bUL8t4TnVJUwraIm91/s1600/1.PNG)  
---  
Signup page|  
  
  
then i filled it with my name and i finished signup. It redirect me to <https://your-domain.redacted.com/agent/index.php#GettingStarted;>  
  
Without checking other staffs i go to **Edit profile**  
  
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjcK9oAfHPY9V_TLdi2fq1x22I7V92T1NxKK_-OP4UeAg8jpxw6NQcTh-tX8Oi0Cz0o55d6pNllVrzItA4qOakQMAVXnd-Nsb8O3XpPVbQ5HpsdqRdiePt8u92929r6xIaxUegXoywIEzd/s320/2.PNG)  
---  
Setting page after signup|  
  
  
  

and here i can able add **XSS Payload** in Name field also in Alias field ( image bellow )  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJ3agJX0CALYLxYD4oiKofyI-xRJBhyV6W45lWTgJd4ZUdGZ8EBkMmzfi2k3rWGedOwdowpwwpLTsCdiGf7SGuoA8CPMr3mxSs0Kp1eKXb2dBsPt0lzYwb48e3nvZeEJBcttozp7darZM5/s320/3.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJ3agJX0CALYLxYD4oiKofyI-xRJBhyV6W45lWTgJd4ZUdGZ8EBkMmzfi2k3rWGedOwdowpwwpLTsCdiGf7SGuoA8CPMr3mxSs0Kp1eKXb2dBsPt0lzYwb48e3nvZeEJBcttozp7darZM5/s1600/3.PNG)  
---  
Setting Page  
  
After save this **Setting** when i back to my Dashboard nothing happen i mean no **PopUp**  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihsGpk8NJQegI3RG_vlvgS1RrztRCbdndH38uNyZqcEUtuiPcheYV5vmCg780jC6KH6q91FBcuAkdfsC7j9AEnu_M8mqCZq1ItZlCI57u9ZYIYNBRWfBshmVdPBXloQSvIrsjWYno76Tbc/s320/4.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihsGpk8NJQegI3RG_vlvgS1RrztRCbdndH38uNyZqcEUtuiPcheYV5vmCg780jC6KH6q91FBcuAkdfsC7j9AEnu_M8mqCZq1ItZlCI57u9ZYIYNBRWfBshmVdPBXloQSvIrsjWYno76Tbc/s1600/4.PNG)  
---  
Profile after added payload, No XSS|  
  
**** Then i am start looking into source code what actually happening.After scrolling source code suddenly my eyes stuck into a **JS** code  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnD_FBzXkrf66NPmnQKTDJGyxdY8mz5RNq1qySK3ewDWzjEzrbMGrBqEaTn4-zsC0sZDtK8DLtnHkiGZH54I1HC8W3cTwMJ2AhNEd4D3q_uHXUmYxWCwajlEKkL5NhjBzEvZOFicqcavsV/s320/5.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnD_FBzXkrf66NPmnQKTDJGyxdY8mz5RNq1qySK3ewDWzjEzrbMGrBqEaTn4-zsC0sZDtK8DLtnHkiGZH54I1HC8W3cTwMJ2AhNEd4D3q_uHXUmYxWCwajlEKkL5NhjBzEvZOFicqcavsV/s1600/5.PNG)  
---  
before bypass  
Oh boy! </script> blocking the <script> here so again i get my ass back into **Edit Setting** then i filled **Name** with xss payload  
  
Payload: </script><script>alert(document.domain);</script>  
  
Then i save it, and back to my Dashboard and tada! XSS Executing success.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidj5-BLLGincp79dTHpnHEVFl57oecjVoPW8MKI4kLupMugC8oraGC_8WaYCR8lqnB_tFWj854KSv3OaHzNjGUYOGRACm5wQ9b21DgIqH8Y_4GJqhuLdsr0admrTWTLrCMRBlAM7LGW2F6/s320/6.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidj5-BLLGincp79dTHpnHEVFl57oecjVoPW8MKI4kLupMugC8oraGC_8WaYCR8lqnB_tFWj854KSv3OaHzNjGUYOGRACm5wQ9b21DgIqH8Y_4GJqhuLdsr0admrTWTLrCMRBlAM7LGW2F6/s1600/6.PNG)  
---  
XSS Popup  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYWBWd-NqR4m9o7SEsjfNF7TXj5aBf4DTws9wq5DnHeX5QistsKANK3JymR0xn7r93DxAAd6ky-IXnrkLedxsYHXgDcbPb1UF-v7ps3aFA-8gLW9IxQS822ZEhjuV7aPPMUCAORiZ_2ZqM/s320/7.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYWBWd-NqR4m9o7SEsjfNF7TXj5aBf4DTws9wq5DnHeX5QistsKANK3JymR0xn7r93DxAAd6ky-IXnrkLedxsYHXgDcbPb1UF-v7ps3aFA-8gLW9IxQS822ZEhjuV7aPPMUCAORiZ_2ZqM/s1600/7.PNG)  
---  
After added new payload|  
  
  
[![](https://66.media.tumblr.com/181e1649ea2ff6e24ad6cd555c65d323/tumblr_ndkawbkxst1rbybp4o1_400.gif)](https://66.media.tumblr.com/181e1649ea2ff6e24ad6cd555c65d323/tumblr_ndkawbkxst1rbybp4o1_400.gif)  
---  
I start dancing like this 😂😂  
**Status:**  
**\------------------**  
30-09-2018 - Reported to the team  
02-10-2018 - Issue Resolved ( No Bounty No HoF 😂 )****

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Labels

[Bug Bounty](https://rudr4sarkar.blogspot.com/search/label/Bug%20Bounty) [Cross-site scripting](https://rudr4sarkar.blogspot.com/search/label/Cross-site%20scripting) [Stored xss](https://rudr4sarkar.blogspot.com/search/label/Stored%20xss) [xss](https://rudr4sarkar.blogspot.com/search/label/xss)

Labels: [Bug Bounty](https://rudr4sarkar.blogspot.com/search/label/Bug%20Bounty) [Cross-site scripting](https://rudr4sarkar.blogspot.com/search/label/Cross-site%20scripting) [Stored xss](https://rudr4sarkar.blogspot.com/search/label/Stored%20xss) [xss](https://rudr4sarkar.blogspot.com/search/label/xss)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//resources.blogblog.com/img/blank.gif)

Anonymous[April 11, 2022 at 4:56 PM](https://rudr4sarkar.blogspot.com/2018/10/how-i-found-stored-xss-on-your.html?showComment=1649721401516#c8109174740857474322)

Merkur Gold Strike Safety Razor - FEBCASINO  
Merkur's Gold [casinosites.one](https://casinosites.one/) Strike Safety Razor, [febcasino.com](https://febcasino.com/) Merkur <https://febcasino.com/review/merit-casino/> Platinum [메이피로출장마사지](https://www.mapyro.com/) Edge Plated Finish, [토토](https://tricktactoe.com/) German, Gold-Plated, Satin Chrome Finish. Merkur has a more aggressive looking,

Reply[Delete](https://www.blogger.com/comment/delete/1586848109216065596/8109174740857474322)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/1586848109216065596?po=6288492912918528301&hl=en&saa=85391&origin=https://rudr4sarkar.blogspot.com&skin=notable)
