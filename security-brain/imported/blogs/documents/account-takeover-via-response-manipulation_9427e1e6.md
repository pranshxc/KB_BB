---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-08_account-takeover-via-response-manipulation.md
original_filename: 2022-07-08_account-takeover-via-response-manipulation.md
title: Account Takeover via Response Manipulation
category: documents
detected_topics:
- mfa
- idor
- xss
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- mfa
- idor
- xss
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 9427e1e6f3b17076b0c57eb29c3194f998fd4803e9833e463ff94adc8c13f88c
text_sha256: 789ed057fd822d7851846d41280c3886079e30ba51be77bd18b2a14b2a2f334d
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover via Response Manipulation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-08_account-takeover-via-response-manipulation.md
- Source Type: markdown
- Detected Topics: mfa, idor, xss, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `9427e1e6f3b17076b0c57eb29c3194f998fd4803e9833e463ff94adc8c13f88c`
- Text SHA256: `789ed057fd822d7851846d41280c3886079e30ba51be77bd18b2a14b2a2f334d`


## Content

---
title: "Account Takeover via Response Manipulation"
url: "https://medium.com/@bughunt789/account-takeover-via-response-manipulation-96be568feb7e"
authors: ["BUG HUNTER"]
bugs: ["Authentication bypass", "Account takeover", "2FA / MFA bypass", "HTTP response manipulation"]
bounty: "2,500"
publication_date: "2022-07-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2477
scraped_via: "browseros"
---

# Account Takeover via Response Manipulation

Top highlight

Account Takeover via Response Manipulation
Abhishek (Bug Hunter)
Follow
2 min read
·
Jul 8, 2022

180

2

Hello everyone I am Abhishek pal here with my First blog ,In this blog I am going to give details about an easy P1 bug I encountered while hunting.

So let’s proceed to the exploitation part now.

Let’s consider our target as Redacted.com.

“Because it’s a private invitation /program“

It had so many features including ability to create groups add Users, and so many other features, and I love to test website with ability to create groups as it opens a big window for vulnerabilities .

So initially I tested for bugs like HTML , XSS, CSRF, IDOR everything , didn’t find much success sadly. Later I noticed they have a 2fa function .With 2fa user is able to login and reset his password also.

So, I think I perform an Response Manipulation attack.

First I go to login page and Enter my credentials which redirect me to 2FA page. I insert an random OTP and With the help of burp suite and capture the request on the burp suite.

Right click on the request and Send request to the response, Response Like

Get Abhishek (Bug Hunter)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

200 OK with this response

I just change the response “error”:false to “error”:true.

This lead to bypass the 2fa . Now i know that it is any valid issue and i reported instantly. After i report it then i memorized that the forget password functionality is also on OTP.

I click on Logout and click on the forget password feature. Enter the email id and it Gave me a option that from which you want to reset you password like 2FA Code, Email OTP , Phone Number OTP.

I choose the 2FA code and Again it redirect me to the OTP page, Insert an random OTP 000000 and capture the request with the help of Burp suite .

Right click on the request and send the request to the response .

In response again I changed the error [ false to true ] and Website redirect me to the new password page. I changed the password.

I got excited again as I got a feeling that here that Authentication Bypass could work, I immediately entered the victim email and repeated all steps and guess what i was able to change password of anyone without any interaction at all within seconds by just a simple manipulation in response

I reported 2FA bypass in P3 severity and Authentication Bypass in P1 severity. Both vulnerability Got Accepted and rewarded.

Timeline:
Bug Reported: 7 May 2022
Bug Triaged: 7 May 2022
Bounty Rewarded: $2500

Tip: Always Understand The workflow of website, Make it very Simple
