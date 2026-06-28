---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-16_stealing-cookies-to-login-in-any-account.md
original_filename: 2019-06-16_stealing-cookies-to-login-in-any-account.md
title: Stealing Cookies to Login in any Account
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 7015f1773dc885770c33eafba95557daa611f91a51cfe4c63f2f3c03a38f9504
text_sha256: 37da8143739ae6d0af070e275456ef9ec217eeda685532f90420cdddf446e711
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing Cookies to Login in any Account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-16_stealing-cookies-to-login-in-any-account.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `7015f1773dc885770c33eafba95557daa611f91a51cfe4c63f2f3c03a38f9504`
- Text SHA256: `37da8143739ae6d0af070e275456ef9ec217eeda685532f90420cdddf446e711`


## Content

---
title: "Stealing Cookies to Login in any Account"
url: "https://medium.com/@osamaavvan/stealing-cookies-to-login-in-any-account-52ca33df0318"
authors: ["Osama Avvan (@osamaavvan)"]
bugs: ["Cookie theft"]
bounty: "900"
publication_date: "2019-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5211
scraped_via: "browseros"
---

# Stealing Cookies to Login in any Account

Stealing Cookies to Login in any Account
Osama Avvan
Follow
3 min read
·
Jun 16, 2019

149

2

Hi,

So this is my first write up, This write up is about how I was able to get into other users account, by stealing their cookies. It was a private program on bugcrowd, let’s just say the program was named Redact.

I created my account on one of the domains of the program https://passport.redact.com, after that, I open up another domain which was https://redact.com.cn and I was automatically logged in without creating an account on that domain as it was using the https://passport.redact.com account to authenticate users, so either create an account or use the https://passport.redact.com account. So as I was playing in the browser console to get something interesting at https://redact.com.cn I typed the Program name in console Redact and I got something RedactId, it was a javascript Object with user information like user Id and email so now I tried to find the JS file from which this object was created and luckily I got that file.

Get Osama Avvan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So after reading that file source code, I got my eyes on a function which was requesting logged in user cookies from the server and was sending that cookie to a subdomain https://reg.redact.com.cn to get user Id and email, the complete URL was like this https://reg.redact.com.cn/auth/setcookie?cookie=usercookie&domain=redact.com.cn

Press enter or click to view image in full size

So now I downloaded that file and modified the source code to log the user cookie in console instead of sending it to https://reg.redact.com.cn and uploaded that modified file on my server and I was hoping that it should log the cookies in the console.

Press enter or click to view image in full size

and it worked the whole URL with cookie was logged in my server console, now it was time to test that am I able to log in my account using that cookie.

Press enter or click to view image in full size

So when I opened this URL in the incognito window I got a response like this sum=sum+1, so to confirm if I was able to login in the account I opened up https://redact.com.cn and yes I was logged in my account.

So now in order to log into other users account I just have to send them this URL of the modified js file on my server, and their cookies will be stored on my server.

It was a weird bug and it was hard to explain to the Program that how it was exploited, but the wait was worth it.

Press enter or click to view image in full size

Thank You for Reading.
