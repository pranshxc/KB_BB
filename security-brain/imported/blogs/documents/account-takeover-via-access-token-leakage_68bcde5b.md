---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-19_account-takeover-via-access-token-leakage.md
original_filename: 2021-08-19_account-takeover-via-access-token-leakage.md
title: Account Takeover via Access Token Leakage
category: documents
detected_topics:
- idor
- ssrf
- xss
- command-injection
- file-upload
- otp
tags:
- imported
- documents
- idor
- ssrf
- xss
- command-injection
- file-upload
- otp
language: en
raw_sha256: 68bcde5b47043ca07030bdbc115c78569c2174003601fda65110522f6901bd24
text_sha256: 3705b2178014079b7d77e3e00bdef96c6e7a47792f229dfe3bea7b03a09d4cc0
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: true
---

# Account Takeover via Access Token Leakage

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-19_account-takeover-via-access-token-leakage.md
- Source Type: markdown
- Detected Topics: idor, ssrf, xss, command-injection, file-upload, otp
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: True
- Raw SHA256: `68bcde5b47043ca07030bdbc115c78569c2174003601fda65110522f6901bd24`
- Text SHA256: `3705b2178014079b7d77e3e00bdef96c6e7a47792f229dfe3bea7b03a09d4cc0`


## Content

---
title: "Account Takeover via Access Token Leakage"
url: "https://tuhin1729.medium.com/account-takeover-via-access-token-leakage-687276953408"
authors: ["Tuhin Bose (@tuhin1729_)"]
bugs: ["IDOR", "Information disclosure", "Account takeover"]
publication_date: "2021-08-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3408
scraped_via: "browseros"
---

# Account Takeover via Access Token Leakage

Top highlight

Account Takeover via Access Token Leakage
Tuhin Bose
Follow
3 min read
·
Aug 19, 2021

257

Hello guys! My name is Tuhin Bose (@tuhin1729). I am a cyber security researcher and bug bounty hunter. In this write-up, I am going to share one of my interesting findings. So without wasting time, let’s start:

tuhin1729
Introduction:

Basically the target was a marketing automation website where you can automate your marketing stuffs efficiently. Let's call it target.com. I have already found more than 10 bugs on the target and earned $$$$ from there.

Now while testing the profile update feature, I came across with this interesting request:

PUT /api/account/general-info/ HTTP/1.1
Host: services.target.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://bo.target.com/
Content-Type: application/json
accessToken: ***REDACTED-SUSPECT-TOKEN***Content-Length: 213
Origin: https://bo.target.com
DNT: 1
Connection: close
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
{"company":"DSPH","domain":"https://darksocietypenetration.com","cellphone":"+91-83xxxxxx36","companySize":"2","businessSector":20,"logo":{"height":0,"base64":"","square":true,"width":0}}

They are using accessToken header for changing the profile details (For other authenticated actions, there is no such header). I quickly changed the value of accessToken header with my 2nd account and my 2nd account’s details were changed. I tried to add the accessToken header in other authenticated requests and it got successful and 2nd account’s details were changed. While doing more research on this, I have discovered that the value of accessToken is static i.e. accessToken is same even after logout. That means, if somehow I can get the accessToken of victim, I would be able to takeover his complete account. But the value of accessToken header is non-guessable so I thought to find a way to get victim’s accessToken. But at that time, I was unable to do so. After 3 – 4 days of hunting, I forgot about that and started hunting on other functionalities.

Getting Victim’s accessToken

In the website, under email marketing, there is a section where we can make our own email templates. While testing that feature, I tried to upload an image file in the email. There are 2 ways to do so either from my device or via an image url. I tried some DoS, SSRF, XSS and file upload tricks. But it seems that they have a strong file type validation. Also they are fetching the image from client side so SSRF is not possible. Now when I tried to use my burp collaborator’s link to see the request, I noticed an interesting thing:

Press enter or click to view image in full size
tuhin1729

Then accessToken is getting leaked in the Referrer header via the token parameter.

Get Tuhin Bose’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So what would be the attacking scenario?

Attacking Scenario
Victim is creating a manual template.
Victim adds an image to his template from 3rd party website.
The 3rd party website owner (or employees) gets victim’s access token (from their logs) and can able to takeover their complete account.
Response

I quickly made a POC and send it to them. After one week, they replied me:

Press enter or click to view image in full size
tuhin1729

Timeline

06/05/21 — Reported Vulnerability

14/05/21 — Replied with the bounty email

Follow me on Twitter: @tuhin1729_

Thanks for reading. I hope you enjoyed this blog.
