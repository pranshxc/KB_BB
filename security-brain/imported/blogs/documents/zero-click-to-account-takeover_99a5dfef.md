---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-14_zero-click-to-account-takeover.md
original_filename: 2021-12-14_zero-click-to-account-takeover.md
title: Zero Click To Account Takeover
category: documents
detected_topics:
- otp
- jwt
- command-injection
- password-reset
tags:
- imported
- documents
- otp
- jwt
- command-injection
- password-reset
language: en
raw_sha256: 99a5dfeffed20718a35df241c1a711ece9916400d6aa475acc0018a9c5ee0821
text_sha256: a15b44baa723666399bfdd35221d5e82297cdbe9cb37657f698e74d2ef35d10c
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: true
---

# Zero Click To Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-14_zero-click-to-account-takeover.md
- Source Type: markdown
- Detected Topics: otp, jwt, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: True
- Raw SHA256: `99a5dfeffed20718a35df241c1a711ece9916400d6aa475acc0018a9c5ee0821`
- Text SHA256: `a15b44baa723666399bfdd35221d5e82297cdbe9cb37657f698e74d2ef35d10c`


## Content

---
title: "Zero Click To Account Takeover"
url: "https://m7-arman.medium.com/zero-click-to-account-takeover-d764e12bee4b"
authors: ["M7.Arman (@ArmanSecurity)"]
bugs: ["Account takeover", "Password reset"]
publication_date: "2021-12-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3090
scraped_via: "browseros"
---

# Zero Click To Account Takeover

Zero Click To Account Takeover
M7arm4n
Follow
2 min read
·
Dec 14, 2021

181

2

Hello amazing hunter.

Press enter or click to view image in full size

Today, I want to explain one of my favorite reports which lead me to take over any user account without one click from user. My favorite endpoint for test is reset password function; In this endpoint we have a lot of different options for test.

Let me explain how my target works to reset password function. We can use phone number or email address, If we use phone number, we will give an OTP code. On the other hand if we use email addresses, we will give a link and token. Keep this information away and let’s talk about register function and JWT token.

In register function we must register with phone number , wait a minute…, I said in reset password we can use email too, but where we confirm our email address? here is honey moon :)

By the way, I said JWT token? all of us know that in body of JWT we access some information of our accounts, I always check JWT body and try to remember all of information for other attack. So, what do we have in body? some regular information such as name and phone number and one of the important parameters was “Sub: 123”.

I think it’s enough for start , Let’s play this game…

Ok everyone , i register in site with phone number; when i submit my email address , show me a pop up to say “click the link sent your email to confirm”

Link: Site.com/YXJlIHlvdSBraWRkaW5nIG1l8J+kqA==/d2hhdCBleGFjdGx5IHlvdSB3YW50Pz8/b2ggbWFuIGFyZSB5b3Uga2lkZGluZyBtZT8=

Oh man , it’s base64 encoded :)) let’s try to decode one by one:

YXJlIHlvdSBraWRkaW5nIG1l8J+kqA== -> i can’t decode this part clearly , i guess it’s token ***REDACTED***/ -> oh man:) it’s my email address(ex: m7.arman@gmail.com)
b2ggbWFuIGFyZSB5b3Uga2lkZGluZyBtZT8= -> is a number (123)

Wait. What ??😐😐😐 Token + email addresses + a number ???

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

where i saw this number? i guess the number is for detecting my account. Exactly, in my JWT token , i have a parameter(“Sub”: 123) with the same number.

I immediately create a new account as victim and i notice that the number of “Sub” grow one by one even create a new account.

Step By Step to Takeover:

Create attacker account (“Sub”:123) and Victim account (“Sub”:124)
In attacker account submit your email address to receive confirmation link
Replace the last part of link(Sub) with base64 encoded of victim sub
Open the poisoning link in Browser
Back to the site and submit a reset password for email you use in step 2
You will receive a link for change password.
After changing password you will redirect to Victim account :)

It’s a piece of cake

I Hope this write up was Helpful for you. Have Good Day

YouTube

Instagram

Twitter
