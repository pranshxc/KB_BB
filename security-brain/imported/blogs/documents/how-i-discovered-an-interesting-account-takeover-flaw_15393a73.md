---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-14_how-i-discovered-an-interesting-account-takeover-flaw.md
original_filename: 2020-01-14_how-i-discovered-an-interesting-account-takeover-flaw.md
title: How I discovered an interesting account takeover flaw?
category: documents
detected_topics:
- password-reset
- rate-limit
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- password-reset
- rate-limit
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 15393a736dae5f2c3e338d27394e17869802c0bf241098e26cd5292bae94c0c3
text_sha256: 37692b3c224b8452d067ee3e691f94861282d3fc0966fba0aa6d0fa39b730c10
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I discovered an interesting account takeover flaw?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-14_how-i-discovered-an-interesting-account-takeover-flaw.md
- Source Type: markdown
- Detected Topics: password-reset, rate-limit, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `15393a736dae5f2c3e338d27394e17869802c0bf241098e26cd5292bae94c0c3`
- Text SHA256: `37692b3c224b8452d067ee3e691f94861282d3fc0966fba0aa6d0fa39b730c10`


## Content

---
title: "How I discovered an interesting account takeover flaw?"
url: "https://medium.com/bugbountywriteup/how-i-discovered-an-interesting-account-takeover-flaw-18a7fb1e5359"
authors: ["Akash Methani (@0xAkash)"]
bugs: ["Account takeover", "Password reset", "Lack of rate limiting"]
publication_date: "2020-01-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4829
scraped_via: "browseros"
---

# How I discovered an interesting account takeover flaw?

Top highlight

How I discovered an interesting account takeover flaw?
Akash Methani
Follow
3 min read
·
Jan 14, 2020

612

3

Hi everyone, today I will talk about an interesting account takeover flaw which I found around a year back. The root cause of this issue was in the algorithm which was generating the password reset tokens.

Let’s consider the application as program.com

Like any other application on the web, this one also had a forget password functionality. I literally forgot my account’s password and requested for a reset link and something weird I noticed was, every time I request reset link for this account the first 3 characters of token would always remain same. This caught my attention and I started to dig.

https://program.com/forgot_password/<TOKEN-HERE>

After a few minutes, I realised these 3 characters were my email’s fourth letter to second letter in reverse order. For example, suppose you have an email address johndoe@domain.com and you request for a password reset link. The first 3 characters of token for this account would always be “nho” (without quotes) What the application did was, it picked the email’s fourth letter (n) and traversed in reverse order up to the second letter (o)

After finding this I thought since the first 3 characters of token were not random, chances are that remaining characters would also have a meaning.I requested tokens multiple times with this and one more test account and turns out, last few characters were the timestamp.

Get Akash Methani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The only thing left to figure out now was the meaning of 2 characters which were in between of “nho” and the timestamp. I did a lot of things, tried analysing patterns in all the tokens requested so far but everything went in vain. I couldn’t find the meaning of those 2 characters (maybe they were random?)

Press enter or click to view image in full size

I thought why not simply bruteforce for those 2 characters? Luckily, the application didn’t have rate limiting in place.

I requested for password reset links for two identical email addresses (johndoe@domain.com and johndoe@domain2.com) exactly at the same time. Since we sent the request at the same time and email’s username part is identical, tokens sent to both accounts would be same except those 2 random characters.

Press enter or click to view image in full size

I checked inbox of second email and intercepting the request clicked the reset link. I then sent the request to burp’s intruder and started bruteforce attack for those 2 characters. After sending a few requests, I saw a 302 response which means I was successfully able to find reset token of first account and eventually could have takeover the account.

It was marked as P1/Critical. I hope you enjoyed the writeup.

You can follow me @0xAkash

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
