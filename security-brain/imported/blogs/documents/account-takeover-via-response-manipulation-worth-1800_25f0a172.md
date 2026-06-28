---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-20_account-takeover-via-response-manipulation-worth-1800.md
original_filename: 2021-02-20_account-takeover-via-response-manipulation-worth-1800.md
title: Account Takeover via Response Manipulation worth 1800$..
category: documents
detected_topics:
- otp
- command-injection
- rate-limit
- business-logic
tags:
- imported
- documents
- otp
- command-injection
- rate-limit
- business-logic
language: en
raw_sha256: 25f0a172541a6486499096ce3bee5563b91d599ea1c8d5cf16dd673f59289487
text_sha256: 56c0103f04f6d9a973bc907256d3b77c8597aca89308786c6ef6574111bdfe8c
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover via Response Manipulation worth 1800$..

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-20_account-takeover-via-response-manipulation-worth-1800.md
- Source Type: markdown
- Detected Topics: otp, command-injection, rate-limit, business-logic
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `25f0a172541a6486499096ce3bee5563b91d599ea1c8d5cf16dd673f59289487`
- Text SHA256: `56c0103f04f6d9a973bc907256d3b77c8597aca89308786c6ef6574111bdfe8c`


## Content

---
title: "Account Takeover via Response Manipulation worth 1800$.."
url: "https://ashutoshmishra00x0.medium.com/account-takeover-via-response-manipulation-worth-1800-ffb242cc55c9"
authors: ["Ashutosh mishra (@ashutoshmish_ra)"]
bugs: ["Authentication bypass", "OTP bypass", "Account takeover"]
bounty: "1,800"
publication_date: "2021-02-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3879
scraped_via: "browseros"
---

# Account Takeover via Response Manipulation worth 1800$..

Ashutosh mishra
 highlighted

Account Takeover via Response Manipulation worth 1800$..
Ashutosh mishra
Follow
3 min read
·
Feb 20, 2021

2.2K

6

Hello Everyone , This is my first writeup

To People who don’t know me , I Ashutosh Mishra , 3rd Year Btech Computer Science Student, A cybersecurity Researcher by day and bug hunter by night,Mainly love to find Business logic bugs.

Press enter or click to view image in full size

The Story Begins , in early Jan 2021 ,I decided to select a target, so started google dorking to select a bitcoin website , finally I was having 3 bitcoin websites with me to hunt on , after giving around 5 weeks, I got some low hanging fruits which was marked as duplicate , which made me disappointment and made me to closed my laptop and went out to hangout with friends,

After Two to Three days ,Luckily got Private invite on bugcrowd to hunt on cryptocurrency website

As soon as I saw this , i started my laptop and fired up the burp suite and started to explore the website , for website name we will refer redacted.io

Now I decided to test the login form and the authentication mechanism, so I made a account and then i tried to login , so when you enter your correct credentials you are redirected to enter the otp as multifactor authentication which is sent to your phone number.

So for a instance I saved my correct login response[Password + OTP]which can help me later to understand the workflow of the website.

Now I tried an incorrect login and intercepted the response and compared to correct login response and i observed that

<wrong_password_response>{token:91a1d5f4a8s5d1a2g1a5dfa15,”error”:”Please update the above field.”,”error_code”:”ErrFormFieldIncorrect”,”error_action”:{},”field_errors”:{“email”:”Password incorrect, please try again”}}

<correct_password_response>{token:91a1d5f4a8s5d1a2g1a5dfa15,”next”:”OTP”,”otp_step”:{“heading”:”Check your email”,”description”:”Enter the 4-digit code we sent to \u003cb\u003evictim@gmail.com\u003c/b\u003e to signin”,”num_digits”:4,”error”:””,”popup_message”:”Code sent to
victime@gmail.com”,”can_request_sms”:false}}

After seeing this response , I thought to give a try on manipulation of response so i just manipulated the response from “error” and replaced with correct response

Note: let the token be the same whatever is present in wrong response and enter your victim email address.

so manipulated response looks like

Get Ashutosh mishra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

{token:91a1d5f4a8s5d1a2g1a5dfa15,”next”:”OTP”,”otp_step”:{“heading”:”Check your email”,”description”:”Enter the 4-digit code we sent to \u003cb\u003evictim@gmail.com\u003c/b\u003e to signin”,”num_digits”:4,”error”:””,”popup_message”:”Code sent to
victime@gmail.com”,”can_request_sms”:false}}

As soon as I forwarded it , I got the goosebumps , the adrenaline started flowing into my blood , the website has redirected me to OTP page.

authentication bypassed

Now here I tried to brute force the OTP , but after the several attempts the website has blocked me for 24 hours ,

Next day I thought to apply same manipulation trick which I used in password , so when I intercepted the OTP request, I Found there was a paramter in body {“success”:”false”}

exactly i know what you are thinking, so I changed false to true and booooom we have successfully enter into victim account

Press enter or click to view image in full size

Timeline:
Bug Reported: 5 January 2021
Bug Triaged: 8 January 2021
Bounty Rewarded: $1800

Tip: Always Understand The workflow of website, Make it very Simple

Feel Free to message on Instagram any queries related to bug bounty

PROOF:

Well if you love this writeup drop a clap 👏(50X), let’s connect then:

Twitter: https://twitter.com/ashutoshmish_ra

Instagram: https://www.instagram.com/i.m.ashutoshmishra/

LinkedIn: https://www.linkedin.com/in/ashutosh-mishra-148864172/
