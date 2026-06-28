---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-10_utilizing-lockdown-blind-sqli-leads-to-account-takeover-data-extraction_2.md
original_filename: 2020-06-10_utilizing-lockdown-blind-sqli-leads-to-account-takeover-data-extraction_2.md
title: 'Utilizing Lockdown: Blind Sqli leads to Account Takeover & Data Extraction'
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: a54fefd151a15529532a9ed835a9001670a5e486f213419d61e475f0b9c55dcf
text_sha256: feef6cd3cdd68b12dc3247b5333104766525c8482bae76022c0319b3ef3418ce
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: true
---

# Utilizing Lockdown: Blind Sqli leads to Account Takeover & Data Extraction

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-10_utilizing-lockdown-blind-sqli-leads-to-account-takeover-data-extraction_2.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: True
- Raw SHA256: `a54fefd151a15529532a9ed835a9001670a5e486f213419d61e475f0b9c55dcf`
- Text SHA256: `feef6cd3cdd68b12dc3247b5333104766525c8482bae76022c0319b3ef3418ce`


## Content

---
title: "Utilizing Lockdown: Blind Sqli leads to Account Takeover & Data Extraction"
url: "https://medium.com/@shakti.gtp/utilizing-lockdown-blind-sqli-leads-to-account-takeover-data-extraction-3705ce8bdb62"
authors: ["Shakti Mohanty (@3ncryptSaan)"]
bugs: ["Blind SQL injection", "Account takeover"]
bounty: "1,400"
publication_date: "2020-06-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4512
scraped_via: "browseros"
---

# Utilizing Lockdown: Blind Sqli leads to Account Takeover & Data Extraction

Utilizing Lockdown: Blind Sqli leads to Account Takeover & Data Extraction
shakti mohanty
Follow
3 min read
·
Jun 10, 2020

124

3

Hello Hunters,

This is Shakti Ranjan Mohanty a security researcher from Odisha. This write-up is all about my last finding on which i was able to Takeover the Administrative account and was able to extract data. Later I got rewarded with 🤑🤑1400€🤑🤑

Press enter or click to view image in full size
Awarded Bounty

I am on to this field from past 2 to 3 years. As i am professionally a security analyst, i couldn’t afford time towards Bug hunting. Whenever i find some time from the professional life, i give all the time towards Bug hunting. During this pandemic situation, Corporate sectors are providing Work from Home and I got a lot of time to Boost myself & For Bug Bounty.

I was eyeing on a private program which was a medical management application(i.e. redacted.com). I checked their policies and got to know that all the subdomain(*.redacted.com) are out of scope, only redacted.com is in scope. The Organisation is giving priorities towards user information. Going Out of the Box, I thought to test its out of scope subdomains because those are the domains which aren’t tested by anyone. I started recon with Amass & Assetfinder and got a lots of subdomains. I harvested 30 subdomains, checked each subdomain and finally got a subdomain( m***.redacted.com ). It has a Login page for an Administrative Doctor. I gave a single quote(‘) as a value on the user id & password parameter. I got an SQL Error, i was bit excited. I tried with 1’ or ‘1’=’1 to bypass the Login, But failed. The failed response to login request was ‘200 Ok’. Then without wasting time i fired up Burp Intruder having Blind Sqli payloads, and got a response with ‘302 found’. I cross checked with the succeed Payload ‘)) or ((‘x’))=((‘ by giving

Userid=’)) or ((‘x’))=((‘ &Password=***REDACTED*** or ((‘x’))=((‘

BBBOOOOMMMMMM……………..

I was Successfully logged in to the administrative account. There are lots of admin functionality now i can access, like adding blogs, adding/deleting members, uploading/viewing receipts.

But the problem was the administrative subdomain in which i have admin access was out of scope, but their priority was user’s information. So i thought if i’ll get the database then it will leave an impact on declining the report as N/A. I tried to dump data from the database manually through the
“userid” and “password” parameter (Result= Failed),fired up Sqlmap and tried to dump database (Result=failed). Then i thought of finding some hidden parameters from the accessed admin panel. I started digging more paths through burp spider, after some time i got a path m***.redacted.com/ImagingCenter/MailingList.php?personID=1&lang=en&navigation=1&namesOnly=1&view=board

With the help of Sqlmap, I also get the database and the Vulnerable param was “personID” and the database was MySql.

Get shakti mohanty’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Yesssss…Now i had data of all users, members, students and other stuffs.

Everything was on my fever, I thought of trying uploading a malicious file on the upload section, for which i seek their permission but they denied to do so.

Reported the bug: 5/11/2020, 7:28:34 PM

Bug Accepted: 5/12/2020, 12:50:43 PM

Triaged & Status Changed from High to Critical: 5/12/2020, 12:50:51 PM

Bounty Time with A little Tragedy: 1400 €

Press enter or click to view image in full size
Reply from the Organisation

Thank You for reading…..

….Love you 3000…

For you: You Are 1337 on your own way

./Logging_out
