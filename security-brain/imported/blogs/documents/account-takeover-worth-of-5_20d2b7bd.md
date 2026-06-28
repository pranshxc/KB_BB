---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-26_account-takeover-worth-of-5.md
original_filename: 2023-02-26_account-takeover-worth-of-5.md
title: Account Takeover worth of $5
category: documents
detected_topics:
- oauth
- command-injection
tags:
- imported
- documents
- oauth
- command-injection
language: en
raw_sha256: 20d2b7bd281553f84c50e45a086fb9fdd31361a9861d981ab45fff3d683826cf
text_sha256: 61de64bfe4a2d68691398ef2e4d8eb9b801dfd4f5ff7d1d574ce91c916141c7a
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover worth of $5

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-26_account-takeover-worth-of-5.md
- Source Type: markdown
- Detected Topics: oauth, command-injection
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `20d2b7bd281553f84c50e45a086fb9fdd31361a9861d981ab45fff3d683826cf`
- Text SHA256: `61de64bfe4a2d68691398ef2e4d8eb9b801dfd4f5ff7d1d574ce91c916141c7a`


## Content

---
title: "Account Takeover worth of $5"
url: "https://gonzxph.medium.com/account-takeover-worth-of-5-dba784b32383"
authors: ["Jefferson Gonzales (@gonzxph)"]
bugs: ["OAuth", "Account takeover"]
publication_date: "2023-02-26"
added_date: "2023-02-28"
source: "pentester.land/writeups.json"
original_index: 1469
scraped_via: "browseros"
---

# Account Takeover worth of $5

Account Takeover worth of $5
Jefferson Gonzales
Follow
4 min read
·
Feb 26, 2023

237

11

$whoami

I’m Jefferson Gonzales from Philippines you can call me Gonz in short, 19 years old a first year college student taking the degree Bachelor of Science in Information Technology, I do Bug Bounty Hunting when I have free time.

Acknowledged by Google, Nokia, UN, BBC and 20+ companies.

In this write-up I will tell you how I found an Account Takeover vulnerability and received a $5 amazon voucher, without wasting your time let’s get started.

Let’s call the target redacted.com, when I have a target my first approach is to test the login/signup feature, in redacted.com you can sign in and signup using Google, Facebook and GitHub OAuth.

When I test a signup/register functionality I tried these tricks to signup the existing email hoping that I can overwrite the password of the existing email.

First I signup on https://redacted.com/register using the existing email but failed

Press enter or click to view image in full size

I signed up using existing email and try to put “%00” after the email, but I got “Invalid email ID”

Then I tried to put a space after the email address, but I got “Email is already registered”

I tried to put the space before the email address, and to my surprise I was redirected to the dashboard, but in my case I wasn’t able to overwrite the existing account, the password and other information of the existing account was not change at all so this bug has no impact. But you can try this trick to your target program if your are lucky then you can overwrite the existing account.

I tried the lower and upper case to trick the server, but still I got “Email is already registered”

In my case all the tricks above is not working, so I tried to explore other functionalities, and I found that a user in redacted.com can signup using Google OAuth.

Press enter or click to view image in full size

so I test the Google OAuth then I register an account using it and it redirected me to the Dashboard after I signed up

Get Jefferson Gonzales’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

One thing that comes to my mind is “What if I will use to register the email address of a user that uses the Google OAuth when they signup?” and yeah! redacted.com is not checking if the email address is already registered or not if it is uses the Google OAuth when signing up

Step to Reproduce
As a victim create an account on https://redacted.com/register using Google OAuth

2. As attacker create an account using email and password on https://redacted.com/register and use the victim’s email address that he used when he register using the Google OAuth

Press enter or click to view image in full size

After that you will be redirected to the Dashboard of the victim’s account

Attack Scenario

Suppose the victim used the Google OAuth when he/she register his/her account on redacted.com, when the attacker tried to register the victims email using email & password, redacted.com is not checking if the email is already registered or not and this mistake can lead to Account Takeover of any user on redacted.com that uses the Google OAuth when they register.

Reward Time:
Contact me on:

Twitter: https://twitter.com/gonzxph

LinkedIn: https://www.linkedin.com/in/gonzxph/
