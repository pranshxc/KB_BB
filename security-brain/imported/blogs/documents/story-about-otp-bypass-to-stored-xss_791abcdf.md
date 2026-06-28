---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-23_story-about-otp-bypass-to-stored-xss.md
original_filename: 2020-05-23_story-about-otp-bypass-to-stored-xss.md
title: Story About OTP Bypass To Stored XSS
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 791abcdf61ff322cefe6931ff37da6266fd100f469f010164a0a60cc24e37064
text_sha256: 9d6afd2c9efd8ee29137dadd59c214b03211179d03080d7c0e339df983b55d8e
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Story About OTP Bypass To Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-23_story-about-otp-bypass-to-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `791abcdf61ff322cefe6931ff37da6266fd100f469f010164a0a60cc24e37064`
- Text SHA256: `9d6afd2c9efd8ee29137dadd59c214b03211179d03080d7c0e339df983b55d8e`


## Content

---
title: "Story About OTP Bypass To Stored XSS"
url: "https://medium.com/@pallabjyoti218/story-about-otp-bypass-to-stored-xss-81bfd735c709"
authors: ["PJ Borah (@PJBorah1)"]
bugs: ["OTP bypass", "Stored XSS"]
publication_date: "2020-05-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4564
scraped_via: "browseros"
---

# Story About OTP Bypass To Stored XSS

PJBorah
Follow
3 min read
·
May 23, 2020

123

3

Story About OTP Bypass To Stored XSS

Hello Hunters!

Greetings everyone! I am PJBorah From India @cyber_xyz218

Today This is my second write-up about one of my best findings OTP Bypass To Stored XSS . It’s an tricky exploitation How i Anonymously Account creation to user account takeover .

Its about Private program Responsive Disclosure Some of Responsive Disclosure Google Dork after decide I simply start Recon As My target Is www.xyz.xom/ i cant disclose Name

Now, I simply try to create a account on www.xyz.com Here And i fill up Registration form and after registration it ask for OTP Verification.

Now, I got OTP On my email Its 4 digit number actually OTP was Vulnerable OTP looks like 1234 Here 34 value only change when i request for OTP again and again It vulnerable For Bruteforce.

here, Now we need to enter OTP verification Here i randomly entered 0000 Before i click next i have already setup By Burp Now i click next capture request.

As request i got

POST /v1/email?change=false&code=0000 HTTP/1.1

Host: xyz.com

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0

Accept: application/json, text/plain, */*

Accept-Language: en-US,en;q=0.5

Now, simply do forward and Response To This host

As Response

HTTP/1.1 401 Unauthorized

Content-Security-Policy: frame-ancestors ‘none’

Content-Type: application/json; charset=utf-8

Content-Length: 42

Date: Fri, 22 May 2020 19:20:04 GMT

{“err”:”Incorrect code”,”ECODE”:”USR_014"}

As above Response i got 401 Unauthorized No worry ,

Now, bypass using response manupulate simply change response to

HTTP/1.1 200 OK

Content-Security-Policy: frame-ancestors ‘none’

Content-Type: application/json; charset=utf-8

Content-Length: 42

Get PJBorah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Date: Fri, 22 May 2020 19:20:04 GMT

{}

BOOM! Now i have logged in without any verification as i bypass OTP(One time password)

Here You will find some stuff for OTP bypass, xss, csrf, ssrf

Now Lets Turn For Stored XSS ,

After i have look for some stuff Now i turn for finding XSS

Here, As from my User Dashboard we can Add some stuff like HTML As Custom Embed

Press enter or click to view image in full size
Image-1

Here in Custome Embed i simply start

“><svg/onload=alert(1);>

Uff it’s not executing It only accept HTML here , I used one more payload

<button onclick=”window.alert(1)”>click</button>

Now As Result As my HTML payload was executed

Press enter or click to view image in full size
Image 2

As Above Picture You have seen click Button Where i actually hide my payload now i simply click “Click” Button BOOM Xss Was Executed !

Press enter or click to view image in full size
Image 3

Now,

till now its self XSS now When i look i got way that always A bug hunter try to find ! Here, i found where i can invite any user to my Dashboard Here, I simply Add my another ID Email and send invitation to my Dashboard

Press enter or click to view image in full size
Image 4

Now, I successfully invited Victim now as Victim click on “CLICK” Button My payload was executed and BOOM Now i can Takeover anyone account by stealing cookie

Press enter or click to view image in full size
Image 5 (Victim Browser)

To learn:

Think in the box :D
Chain bugs for higher impact.
Never stop searching

! I Reported This issue

! Bounty ill discuss on Next Write UP:::::

By — PJBorah @cyber_xyz216

Thank You For Reading ………….(Keep Hunting Keep Learning )
