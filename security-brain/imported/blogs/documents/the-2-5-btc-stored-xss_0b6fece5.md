---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-13_the-25-btc-stored-xss.md
original_filename: 2018-06-13_the-25-btc-stored-xss.md
title: The 2.5 BTC Stored XSS
category: documents
detected_topics:
- xss
- sso
- command-injection
- otp
- api-security
tags:
- imported
- documents
- xss
- sso
- command-injection
- otp
- api-security
language: en
raw_sha256: 0b6fece5c866619b4b92c79d09c01d3f4de99e308c26de2b5bfc3da88e61cc1f
text_sha256: b54acdc1eb83eff92a30623fd60c0cb0b92f3ed09151b9e07c026cd4476f7b21
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# The 2.5 BTC Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-13_the-25-btc-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `0b6fece5c866619b4b92c79d09c01d3f4de99e308c26de2b5bfc3da88e61cc1f`
- Text SHA256: `b54acdc1eb83eff92a30623fd60c0cb0b92f3ed09151b9e07c026cd4476f7b21`


## Content

---
title: "The 2.5 BTC Stored XSS"
url: "https://medium.com/@khaled.hassan/the-2-5-btc-stored-xss-f2f9393417f2"
authors: ["Khaled Hassan"]
bugs: ["Stored XSS"]
publication_date: "2018-06-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5840
scraped_via: "browseros"
---

# The 2.5 BTC Stored XSS

The 2.5 BTC Stored XSS
Khaled Hassan
Follow
3 min read
·
Jun 13, 2018

147

1

Severity : High
Complexity : Easy

In September 2016, I had found a simple Stored XSS that I earned 2.5 BTC for it from a crypto exchange platfrom. and In this time I was trading too much in cryptocurrencies and I was trying to find the best crypto exchange platform that I can trade on it easily without any restrictions, so I decided to find a one.

After a few hours on searching on the web, My eyes came on a Taiwan crypto exchange platform with awesome features and very good referral system too. Quickly I registered on the website and posted my referral link on facebook and twitter.

The referral URL was as follow:
https://www.reacted.com/users/sign_up/32427/shared

In the second day, When I logged into my account on the website, I noticed two notifications about that two guys just registered using my referral link.

Press enter or click to view image in full size

An interesting thing, application prints the accounts names that registered using your referral link, So what If I register a new account with XSS name using my referral link. very simple, very easy.

Quickly I registered a new account using my referral link with my favorite XSS payload “><img src=x onerror=prompt(1)>

Then after I created the account I browsed to the notification page and I noticed that the payload didn’t get executed and I didn’t know why even the payload isn’t filtered by the application.

Hmmm, I tried many payloads and it didn’t get popup too. Then I tried to register a new account with this payload (“ <script>alert(1)</script>”)

Get Khaled Hassan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After I registered the account, I browsed to notification page again. But this
time the payload has been executed on the page using script alert payload.

My reaction after this

I felt this moment that this payload tells me he is still the king of XSS even if no one uses it anymore ;”D

XSS’ing all platform users

However, haven’t you noticed that you can change the ID on the referral link to another account ID that you want to register by his referral link ?

It looks like that this website generates referral links depends on the ID of user which is very easy to known or enumerated. In other websites, the referral link is consists of hashed token.

And because of this feature or bug, I was able to XSS all users by sending registration requests to intruder tap and this will request register accounts by users referral link with XSS names From User ID 1 to 32427 USER ID

And XSS will get executed on accounts of user when they see the notification page

Quickly, I sent an email support team asking them If they have bug bounty or something like that, and after 6 hours their response was as follow

Great reply! After this encouraging response I wrote the report of Stored XSS that I found and other two medium severity issues and sent the report to them.

26 Hours later of sending the report, I got this awesome email.

The company rewarded me with 2.5 BTC as bounty for my effort and offered me to do pentest on their application from time to time.

Lessons learned

Do not hesitate to report something you found on a service or application that you use and I’m sure It’s probably going to be appreciated by them and it might end up getting great stuff.
Don’t forget to test referral function because I never thought that it maybe be vulnerable to anything like that
