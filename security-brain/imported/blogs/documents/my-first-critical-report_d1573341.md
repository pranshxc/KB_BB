---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-08_my-first-critical-report.md
original_filename: 2018-08-08_my-first-critical-report.md
title: My First Critical Report
category: documents
detected_topics:
- otp
- rate-limit
- command-injection
- password-reset
- csrf
- api-security
tags:
- imported
- documents
- otp
- rate-limit
- command-injection
- password-reset
- csrf
- api-security
language: en
raw_sha256: d157334101775420b0e52455285029f1d2c0c44baba3144b5391e0fff1a8e5c8
text_sha256: 3413cf45dc6a10e8dfcbfb062fe463d73a1694613d33c77e4c642ffa1131fe20
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# My First Critical Report

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-08_my-first-critical-report.md
- Source Type: markdown
- Detected Topics: otp, rate-limit, command-injection, password-reset, csrf, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `d157334101775420b0e52455285029f1d2c0c44baba3144b5391e0fff1a8e5c8`
- Text SHA256: `3413cf45dc6a10e8dfcbfb062fe463d73a1694613d33c77e4c642ffa1131fe20`


## Content

---
title: "My First Critical Report"
url: "https://medium.com/mcorral74/my-first-critical-report-9ceeb15f20c3"
authors: ["Miguel Corral (@mcorral74)"]
bugs: ["Password reset", "Account takeover"]
bounty: "2,500"
publication_date: "2018-08-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5764
scraped_via: "browseros"
---

# My First Critical Report

Top highlight

My First Critical Report
Miguel
Follow
5 min read
·
Aug 8, 2018

187

2

Hello guys ,

Some time ago, i wanted to write my first write-up about bug bounties, but the lack of time (work and family) i never found the moment, but the other day talking with @saamux encouraged me to do it. So let’s go !!!

I’ll share with you an interesting bug i’ve found in a private program of HackerOne, some months ago.

It was Friday and i was ready to take a nap, after a hard day of work, before that, i took my mobile and started browsing through one of the program’s endpoints (redacted.com), when suddenly I saw that the url changed to m.redacted.com.

I hadn’t seen that endpoint before, it seemed new, so I started to take a look.

I started surfing the website and capturing traffic with Burp … there were no tokens to avoid csrf attacks so it looked good.. my next step was try to create an account on the website but I needed a Chinese phone number (there was no option to register with an email)..First Problem !!

Press enter or click to view image in full size

To register on the website you need a Chinese mobile phone, they will send you an OTP (one-time password), so you can register on their website.

I used different websites that give you a mobile number from any country to recieve sms… many didn’t work, most didn’t operate in China and those that gave you a Chinese mobile phone number did not receive SMS, only calls.. Second Problem !!

Press enter or click to view image in full size
Press enter or click to view image in full size

I spent some days trying to find a website that could give me that service, i had a feeling that I could find something in that endpoint, but I couldn’t verify it.

I tried to do a brute force attack, to see if I could guess the OTP and register on the page, but I didn’t know the length of the OTP (normally it’s 4 or 6 digits). I tried brute-force but it didn’t let me test more than 5 OTP.

At the end, i found a payment page that gave you a Chinese phone number to receive the OTP.

You had to select for what service you wanted it, so the famous OTP would arrive, but logically the company that was testing wasn’t on that list.

Press enter or click to view image in full size

So I sent them an email, explaining the problem … The days passed but I didn’t get an answer.. Suddenly, one morning I received an email that had already added the company.

My next step was register an account on the website, I got the famous OTP (6 digits length), so finally I could create an account on the endpoint m.redated.com… GREAT !!!

Get Miguel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The first thing i noticed, was that certain functions were vulnerable to CSRF, but my idea was if I could find something more critical on this endpoint.

The first thing that came to my mind, was to check Forget Password Functionality, you had to enter the mobile number and the server will send you a 6-digit OTP, if the OTP is correct you could change the password.

So, i checked if there was any difference when you sent the OTP correct and incorrect. When i sent an incorrect OTP i got from the server this message:

Sorry…what is “\u9a8c\u8bc1\u7801\u65e0\u6548" ? After a small research i discovered that it was Unicode Entities, so i try to decode it, i found this website http://online-toolz.com/

Press enter or click to view image in full size

Next, i used google translate (sorry i don’t speak Chinese) ;-)

Press enter or click to view image in full size

Ok, nothing special or weird, but what happens when we introduce the correct OTP ?

Press enter or click to view image in full size

My chinese mobil number was 17088016446, so my next step was use Password Reset Functionality again, in this case i sent the pin 111111 (that wasn’t right) and intercept the request from server, when the server sent the request that is failed, i deleted the request and inserted the following data:

{“data”:”17088016446",”error”:1,”mess”:””}

I was be able to reset the password !!!!!!!!!!!!! Bingo !!!!

At this point, I just had to know the mobile number and could change their password. Simply using the Reset Password Functionality and inserted a mobile number, the website told me if that number exists or not in the database, after that, sent any OTP, intercept the request from the server, deleted the request and insert the following data:

{“data”:”mobilenumber",”error”:1,”mess”:””}

GAME OVER !!!!

I had found my first Full Account Takeover …..

I reported it immediately, and they fixed it and rewarded over the weekend.

This was all about this finding… i hope you like it !!

@mcorral74
