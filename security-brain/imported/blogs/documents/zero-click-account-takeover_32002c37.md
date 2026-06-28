---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-19_zero-click-account-takeover.md
original_filename: 2021-06-19_zero-click-account-takeover.md
title: Zero Click account Takeover
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- automation-abuse
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- automation-abuse
language: en
raw_sha256: 32002c379625f78b0c68548378bd5a9554cabb80ebbbf737020116db896eff6a
text_sha256: 6ecd0288908e7c6b33ea79a2bc9db2b4e4ca445a928571ad6bed70b054271ebc
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Zero Click account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-19_zero-click-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `32002c379625f78b0c68548378bd5a9554cabb80ebbbf737020116db896eff6a`
- Text SHA256: `6ecd0288908e7c6b33ea79a2bc9db2b4e4ca445a928571ad6bed70b054271ebc`


## Content

---
title: "Zero Click account Takeover"
url: "https://medium.com/@zahirtariq/zero-click-account-takeover-32e888d13e73"
authors: ["Zahir Tariq (@ZahirTariq3)"]
bugs: ["Account takeover", "Password reset"]
publication_date: "2021-06-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3559
scraped_via: "browseros"
---

# Zero Click account Takeover

Zero Click account Takeover due to API Misconfiguration
Zahir Tariq
Follow
2 min read
·
Jun 19, 2021

468

5

.

.

.

السلام عليكم

my name is zahir , Bug bounty Hunter from Sudan

I will share a critical bug that I found in Upchieve program in h1

Description :-

I like to test reset password functionality , so I made a temp mail with mohmal and I signed up in upchieve

in reset password request there was a post Json parameter => email

“email":”me@mail.com”

and the response was

“msg”:”password reset email sent”

I tried to make the email parameter value as an Array with 2 mails to manipulate the functionality and send the email link to email1 and email2

{

“email”:[”victimMail”,”attackerMail"]

}

Press enter or click to view image in full size

Nice , the msg is “password reset email sent"

Get Zahir Tariq’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I checked my 2nd mail “I didn’t sign up with it in upchieve and I got a reset password mail from upchieve

from : upchieve

To : my victim email , and my attacker email

I checked if the reset link token is the same in both emails and it was :’)

until now it’s a critical bug but I liked to escalate it more

my burp scanner found a email address disclosed belongs to upchieve

I can’t take over it ' as the program policy says but I mentioned it as the attack scenario

triaged with severity critical 9.8

Notice :-

email address is not private information you can get it from linkedin ..etc so this is a zero click ATO

I will share a tip with every writeup

Tip :- in reset password request

use content type converter burp ext

2. convert the request to json , if the application accepted it try this trick

3. convert the request to xml and if the application accepted it u can try xxe

Twitter :- @zero_or_1
