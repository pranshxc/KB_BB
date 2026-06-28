---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-05_bugbounty-how-i-could-book-cab-using-your-wallet-money-in-indias-largest-auto-tr.md
original_filename: 2018-03-05_bugbounty-how-i-could-book-cab-using-your-wallet-money-in-indias-largest-auto-tr.md
title: '#BugBounty — How I could book cab using your wallet money in India’s largest
  auto transportation company!'
category: documents
detected_topics:
- mobile-security
- command-injection
- otp
tags:
- imported
- documents
- mobile-security
- command-injection
- otp
language: en
raw_sha256: 206364de6f865f89da5fe6fae396a23ff40e817f5799bee6891aac9c3e7d491a
text_sha256: 223dfc57fa168b933ac8eb959c7d88e279f0d7461b37e6b24051ea50eaf39f95
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — How I could book cab using your wallet money in India’s largest auto transportation company!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-05_bugbounty-how-i-could-book-cab-using-your-wallet-money-in-indias-largest-auto-tr.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `206364de6f865f89da5fe6fae396a23ff40e817f5799bee6891aac9c3e7d491a`
- Text SHA256: `223dfc57fa168b933ac8eb959c7d88e279f0d7461b37e6b24051ea50eaf39f95`


## Content

---
title: "#BugBounty — How I could book cab using your wallet money in India’s largest auto transportation company!"
url: "https://medium.com/bugbountywriteup/bugbounty-how-i-could-book-cab-using-your-wallet-money-in-indias-largest-auto-transportation-e0c4252ca1a3"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["OTP bypass"]
publication_date: "2018-03-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5957
scraped_via: "browseros"
---

# #BugBounty — How I could book cab using your wallet money in India’s largest auto transportation company!

#BugBounty — How I could book cab using your wallet money in India’s largest auto transportation company!
Avinash Jain (@logicbomb)
Follow
3 min read
·
Mar 5, 2018

599

5

Hi Guys,

So one more good hack that I managed to found out during my bug bounty hunt and this comes in India’s largest online auto transportation company. As the title says , I was able to book cab for myself using the victim wallet money. :D . Let’s see what was the whole scenario —

I targeted their web application instead of android app and that I did intentionally. The reason is pretty obvious as companies are more concerned about their android application rather than website just because customer traffic is always more for mobile apps and so their always comes more chances of loopholes where security attention is less.

I went to their site and entered pick up and destination location and was presented with the page to enter mobile number for OTP confirmation —

Press enter or click to view image in full size
Mobile number needed to authenticate
Press enter or click to view image in full size
OTP Verification

The first general thing that always strikes hunters mind seeing OTP verification is “How to bypass it” . I tried to bruteforce it but some blocking was set on the application after successive wrong attempts. Captured the raw HTTP request to analyse but nothing was helping out. Based on my previous hunt, I have realized one thing that sometime somewhere in the application developers misses server side validation and completely resides on client side .

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s try the same thing here . I entered my test mobile number , put the right OTP in the box and saved the success response for it —

Press enter or click to view image in full size
HTTP Success Response

As you see, there is no session management hence the only thing left for me is to bypaas OTP verification. Now I entered victim mobile number ,put the wrong OTP and below was the HTTP response —

Press enter or click to view image in full size
Wrong OTP HTTP response

I tried bypassing it by capturing the wrong OTP HTTP response and replacing it with the HTTP response of correct OTP and forwarded it and when I did so, I got the following below page —

Ride successfully booked

My ride was successfully booked with victim’s mobile number!!! but the things didn’t stop here. As almost all the cab/auto online platform have their own wallet from where the money automatically deducts if you haven’t chosen some other mode of payment, the same was happening here, money was getting deducted from victim’s wallet hence I was able to book cab with his mobile number using his wallet money. :)

Report details-

03-Feb-2018 — Bug reported to the concerned company.

03-Feb-2018 — Bug was marked fixed.

03-Feb-2018 — Re-tested and confirmed the fix.

09-Feb-2018 — Rewarded by company.

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )
