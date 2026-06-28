---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-21_how-2-cute-bugs-offered-me-a-reward-of-650.md
original_filename: 2023-09-21_how-2-cute-bugs-offered-me-a-reward-of-650.md
title: How 2 Cute Bugs offered me a reward of 650€
category: documents
detected_topics:
- xss
- sqli
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: f74a82613dfb5c419826b1bc00017c8cdd715d94c73a62d3ca711a0062f3ac49
text_sha256: c0a220771233a50968a486391d7589ab4c17dc4f5c5b54e8e13061a0f643881b
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: true
---

# How 2 Cute Bugs offered me a reward of 650€

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-21_how-2-cute-bugs-offered-me-a-reward-of-650.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: True
- Raw SHA256: `f74a82613dfb5c419826b1bc00017c8cdd715d94c73a62d3ca711a0062f3ac49`
- Text SHA256: `c0a220771233a50968a486391d7589ab4c17dc4f5c5b54e8e13061a0f643881b`


## Content

---
title: "How 2 Cute Bugs offered me a reward of 650€"
url: "https://medium.com/@anirudhkrishna012/how-2-cute-bugs-offered-me-a-reward-of-650-7f13abf36c65"
authors: ["Anirudh Krishnakumar"]
bugs: ["XSS", "SQL injection"]
bounty: "691"
publication_date: "2023-09-21"
added_date: "2023-09-22"
source: "pentester.land/writeups.json"
original_index: 756
scraped_via: "browseros"
---

# How 2 Cute Bugs offered me a reward of 650€

How 2 Cute Bugs offered me a reward of 650€
Anirudh Krishnakumar(a.k.a)0x_s3cur1ty_r3s34rch3r
Follow
4 min read
·
Sep 21, 2023

279

4

Hey amazing cyberfolks 😊 !!. This is me ani ! back with an interesting vulnerabilities I found ,for which I was awarded a bounty of 650€.

Okay now lets started !!!. That was a fine weekend saturday, I was lazy af and bored🥱 , I decided to start hunting to kick off my laziness😎 . I usually hunt on private programs i discover from google dorks since hackerone and bugcrowd is “crowded” sometimes. I don’t recommend you either to always hunt on these random dork programs as you may be disappointed with unresponsiveness many times :(

Anyways I went to this Github repo where it contains curated list of google dorks to discover program which offer responsible disclosure programs. I randomly picked one dork.

responsible disclosure bounty r=h:eu

I decided to choose an very old program so I traversed many pages and picked on random domain. Lets call it “redacted.com“. “redacted.com” was an online travel goods purchasing e commerce site. It had various functionalities , I registered an account and started to play around. I tested for login issues and authentication related bugs but unfortunately no luck :(

There was a search feature , i searched for testbro and I noticed my input was reflected in the webpage. I decided to break the “” and inject an XSS payload (like “<img src=xss onerror=alert(1)>) and when I hit search to my surprise payload got executed and I saw an pop 🤩.

I noticed an important thing whenever we click on any project the product ID was with an numerical number in the url like “redacted.com/products?productID=21”. Any idea struck on my mind why don’t we try for Sql Injection and decided to put an ‘ after like productId=21’. To my surprise i got an sql syntax error back from the server like the below

Press enter or click to view image in full size

I was like WHATTTTT!!. Since I am an lazy ass hunter I decided to exploit this using SQLMAP tool (but I highly recommend trying out payload manually to understanding) . Okayy now back with the hunting.

Get Anirudh Krishnakumar(a.k.a)0x_s3cur1ty_r3s34rch3r’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I used the below command to dump all the databases present in the target:

 sqlmap -u http://redacted.com/products?productID=21 --dbs

It dumped all the databases , next I several databases one of them caught my eye. I used that database name and dumped all the tables present using the below command:

sqlmap -u http://redacted.com/products?productID=21 -D redacted --tables

It dumped all the tables, one of them caught my eye , it named “users”. I decided to dump that tables . I used the below command for that:

sqlmap -u http://redacted.com/products?productID=21 -D redacted -T users --dump-all 

Wow, it dumped all the details and WHATT admin username and password were also among them

Press enter or click to view image in full size

I got the admin username and password was of some sort of encoding. I used cyberchef.io and figured out it was base64 and decoded it and got the password=***REDACTED***

Okay now that I have username and password. I need to find a way to login as admin. I decided to do directory brute force using gobuster tool , i got an endpoint like “redacted.com/admin/login”. So now you guys might have guessed what I must have done. I used those credentials and logged in as admin , YEA !!!

Now I made an detailed reported regarding the findings and submitted to redacted.com security team. After 3 days , they decided to offer me a reward of 650€ for report.

Connect with me in linkedin(https://www.linkedin.com/in/anirudh-krishnakumar-%E0%AE%95%E0%AE%BF-%E0%AE%85%E0%AE%A9%E0%AE%BF%E0%AE%B0%E0%AF%81%E0%AE%A4%E0%AF%8D-369b20190).

That’s it for today folks. C you guys in another write up :). Peace
