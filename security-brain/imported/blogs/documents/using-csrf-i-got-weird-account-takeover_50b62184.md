---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-05_using-csrf-i-got-weird-account-takeover.md
original_filename: 2020-02-05_using-csrf-i-got-weird-account-takeover.md
title: Using CSRF I Got Weird Account Takeover
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- csrf
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- csrf
- api-security
- cloud-security
language: en
raw_sha256: 50b62184e036b92dfd0183611f2585aadda34faced216b16eeb2bbdf5fab7e42
text_sha256: 357aadc32cf85d82bfe7492b58ae6e52bfec92e90cd7eb587ed0b952cef43bb1
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Using CSRF I Got Weird Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-05_using-csrf-i-got-weird-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, csrf, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `50b62184e036b92dfd0183611f2585aadda34faced216b16eeb2bbdf5fab7e42`
- Text SHA256: `357aadc32cf85d82bfe7492b58ae6e52bfec92e90cd7eb587ed0b952cef43bb1`


## Content

---
title: "Using CSRF I Got Weird Account Takeover"
url: "https://flex0geek.blogspot.com/2020/02/using-csrf-i-got-weird-account-takeover.html"
final_url: "https://flex0geek.blogspot.com/2020/02/using-csrf-i-got-weird-account-takeover.html"
authors: ["Mohamed Sayed (@FlEx0Geek)"]
bugs: ["CSRF", "Account takeover"]
publication_date: "2020-02-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4788
---

###  Using CSRF I Got Weird Account Takeover 

on  [ February 05, 2020  ](https://flex0geek.blogspot.com/2020/02/using-csrf-i-got-weird-account-takeover.html "permanent link")

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjI2UdcCT_i7Gs5gTvBprBOuJxngmHbbifXBKk8rTO-wEMAqsOW9tUafkBAeG3DXZaVBr5j4D2qspwD7t3e_XVzk4ZIC0B6zxxJfwDo8W9yrqifkO-wuyTocw-JaLPMLKaOD0WeYL5jyVs/s640/csrf-cross-site-request-forgery.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjI2UdcCT_i7Gs5gTvBprBOuJxngmHbbifXBKk8rTO-wEMAqsOW9tUafkBAeG3DXZaVBr5j4D2qspwD7t3e_XVzk4ZIC0B6zxxJfwDo8W9yrqifkO-wuyTocw-JaLPMLKaOD0WeYL5jyVs/s1600/csrf-cross-site-request-forgery.jpg)

  
Hi guys, I'm back again this bug was interesting and weird let's start.  
  
let's refer to the target's name as (target.com) I start to test the domain like what I do in my testing, I used sublist3r to enumerate the subdomains, in one of these subdomains I start to test the password reset function I sent a request to my email to change the password, i opened the link and sent the request to change the password but i used my Burp to see the request and it looks like that  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5BWqWpD44Q9A8Lt1qnvyA4XzFevAWswAmrY1Q9SuNlJgK_h5VFb4hiVgK_mCkDRor99WWzYShu8CUHC1is6nuAzZH0ciN7LevU3wZR-LrK39txhrcleC2ZBV_7ttLD8E7SLD0tY9mztg/s640/Screen+Shot+2020-02-05+at+2.26.33+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5BWqWpD44Q9A8Lt1qnvyA4XzFevAWswAmrY1Q9SuNlJgK_h5VFb4hiVgK_mCkDRor99WWzYShu8CUHC1is6nuAzZH0ciN7LevU3wZR-LrK39txhrcleC2ZBV_7ttLD8E7SLD0tY9mztg/s1600/Screen+Shot+2020-02-05+at+2.26.33+PM.png)

  
there is a token for CSRF I tested this token and deleted it but the change happens, that means there is no filtring for this token there is a CSRF bug here and there is another thing the token of reset password not in the request not in the cookies or in the body so i think it's in the sessions and how i knew that? I test the function of reset password I sent another link to my account and i sent the same request but it returns 403, I opened the new reset link bug didn't use it and I go back to my burp and sent the request again and it works and I changed the password with outsend the request from the browser, I understand the function when the user opens the link there is a session will open and will add the token on it and there is something like value to chack like (change=1) if it (1) the server will change the password which comes from the same session if it (0) it will return 403 this what I understand from test the function so now if the user opened the link and didn't use the token it will not be expired and we can use the CSRF bug in this time and we will gain account takeover in this case.  
  
I liked this bug so I published it, but the subdomain was out-of-scope and I didn't notice it XD.  
  
Goodbye.

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXnkUT2DrFCknlAwOigyXr5kUtUhs4dSTneNNfTvkYEVHIz4Dn1_Cv4jMBjmih14FJRLedn53xd2GdJlhUwCP19epPHm2Bz1zNfauVRPn0VpPyCFTCldo4b2oEf_wV6SM/s45-c/Copy+of+DSC_0025+copy.jpg)

[احمد الماكى](https://draft.blogger.com/profile/05485690178068092467)[February 24, 2020 at 6:37 PM](https://flex0geek.blogspot.com/2020/02/using-csrf-i-got-weird-account-takeover.html?showComment=1582598231751#c69050333393060920)

hey dude ! can i talk with you private this is my profile https://www.facebook.com/profile.php?id=100009760126088

Reply[Delete](https://draft.blogger.com/comment/delete/7853305107519134332/69050333393060920)

Replies

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://draft.blogger.com/profile/01480295653485742161)[February 20, 2022 at 1:06 AM](https://flex0geek.blogspot.com/2020/02/using-csrf-i-got-weird-account-takeover.html?showComment=1645347991539#c7017981922028857240)

هو هنا مكنش بيت  
check  
الباسوورد الحالية ايه؟

Reply[Delete](https://draft.blogger.com/comment/delete/7853305107519134332/7017981922028857240)

Replies

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Hossam Hussein](https://draft.blogger.com/profile/03933817559138154323)[April 17, 2025 at 4:43 AM](https://flex0geek.blogspot.com/2020/02/using-csrf-i-got-weird-account-takeover.html?showComment=1744890186415#c7204164254108022342)

لا لان Function المستخدمه هنا Reset Password يعني هو ميعرفش Password اصلا.  

[Delete](https://draft.blogger.com/comment/delete/7853305107519134332/7204164254108022342)

Replies

Reply

Reply

Add comment

Load more...

#### Post a Comment

[](https://draft.blogger.com/comment/frame/7853305107519134332?po=4571886727085920598&hl=en&saa=85391&origin=https://flex0geek.blogspot.com&skin=emporio)
