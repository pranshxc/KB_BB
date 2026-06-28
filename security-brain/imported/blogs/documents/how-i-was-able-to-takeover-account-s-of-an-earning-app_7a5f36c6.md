---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-01_how-i-was-able-to-takeover-accounts-of-an-earning-app.md
original_filename: 2018-10-01_how-i-was-able-to-takeover-accounts-of-an-earning-app.md
title: How I was able to takeover account's of an Earning App
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 7a5f36c67c7976d071b7b769267729326912b853e632f0cdfb0b633f3ed00d1a
text_sha256: 85b3aec9e6306ca532d45b8e6d2559aedcdf49d21c8e5320ff8729a690fe310f
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to takeover account's of an Earning App

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-01_how-i-was-able-to-takeover-accounts-of-an-earning-app.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `7a5f36c67c7976d071b7b769267729326912b853e632f0cdfb0b633f3ed00d1a`
- Text SHA256: `85b3aec9e6306ca532d45b8e6d2559aedcdf49d21c8e5320ff8729a690fe310f`


## Content

---
title: "How I was able to takeover account's of an Earning App"
url: "https://medium.com/@alexali5080/how-i-was-able-to-takeover-accounts-of-an-earning-app-c22d07d8ce9"
authors: ["Abbas Wafa"]
bugs: ["Information disclosure"]
publication_date: "2018-10-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5673
scraped_via: "browseros"
---

# How I was able to takeover account's of an Earning App

How I was able to takeover account’s of an Earning App
Hey Everyone, I intend to write this one down to express my methodology for this bug that I found in one of the the best Earning app.
Thoughtful Perspectives 😉
Follow
2 min read
·
Oct 1, 2018

209

With that being said, let’s start 😃

I was searching on Google playstore “ Real Money Earning apps” and I selected the first one..I create a account and start earning money.. when I earned upto a 1.08 dollar in 1 week :( now I have decided to cashout this money . so I clicked on cashout button in app.. It’s redirect me to account on their web page .

https://www.app.com/redirect?client-id=56543-user-key=JjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0=myemail@gmail.com&page=account%2Fcashout&lang=en&version=39.0.2

While redirecting I notice their is no session token I was wow:)

now I changed mymail@ to test@ and the webpage result was “Please correct your Client-id and user-key”

Now It’s time to get dig into more..Their was feature in app chatting. I decided to dig.I open myaccount in Firefox which is configure with burp and testaccount on my phone I meassage to myacc from testacc .I recieved a notification and Intercept the notification message by clicking on it will show all the info relted to message and also its show me user id and user key..in Burp Repeater Response

Get Thoughtful Perspectives 😉’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

{“account”:{“Key”:”GxhgadH3fCbzAPSnSHXHLAIMSYUMNS9nbSBSAbSGXJSKOREYQBTS1.”account”:{“id”:”61247ec0-c3ec-11e8–81e3-e9265c5b6228"

Now I put this id&key in

https://www.app.com/redirect?client-id=61247-user-key=GxhgadH3fCbzAPSnSHXHLAIMSYUMNS9nbSBSAbSGXJSKOREYQBTS1=testmail@gmail.com&page=account%2Fcashout&lang=en&version=39.0.2

able to login victime account successfully…Simple

Hope you guys like this…Thanks for reading and sorry for poor engish:/

Timeline

Report on 27–09–2018

patched 28–09–2018

#Nobounty Fu****

Fixed They added session token’s for unique user per session ..
