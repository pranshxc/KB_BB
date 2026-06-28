---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-18_how-i-hacked-one-of-the-biggest-airline-in-the-world.md
original_filename: 2022-06-18_how-i-hacked-one-of-the-biggest-airline-in-the-world.md
title: How I hacked one of the biggest Airline in the world
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- rate-limit
- api-security
language: en
raw_sha256: d6326f88c679ce9df9b4ee945eb9e7fe59ee29fc13c6392b2cfe237f2532049e
text_sha256: d356aea73e498409947c5052d8027a33eaff33516aaefde96de60cf672e158e2
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# How I hacked one of the biggest Airline in the world

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-18_how-i-hacked-one-of-the-biggest-airline-in-the-world.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `d6326f88c679ce9df9b4ee945eb9e7fe59ee29fc13c6392b2cfe237f2532049e`
- Text SHA256: `d356aea73e498409947c5052d8027a33eaff33516aaefde96de60cf672e158e2`


## Content

---
title: "How I hacked one of the biggest Airline in the world"
url: "https://medium.com/@sazouki/how-i-hacked-one-of-the-biggest-airline-in-the-world-e7810dc43791"
authors: ["Dali Jandro (@Sazouki_)"]
bugs: ["IDOR", "Account takeover", "Broken authorization"]
publication_date: "2022-06-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2537
scraped_via: "browseros"
---

# How I hacked one of the biggest Airline in the world

How I hacked one of the biggest Airline in the world
Sazouki
Follow
2 min read
·
Jun 18, 2022

145

3

Hello Bug Bounty community, this is my first write up about a bug that I managed to takeover all accounts in one of well known Airline in the world

Due to the program policy I will not mention the program name so I will refer to it as redacted.com.

This program has wide scope, and I found couple of account takeover in different subdomains. As always I start with subdomains enumeration, I suggest to use reconftw, and extract the live domains. I found one domain x.y.redacted.com which you can signup but you cannot login until the admin approve your account.

Get Sazouki’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Once you create your account you will receive confirmation email with link https://x.y.redacted.com/Home/Index?Value=[Token], clicking on that link will confirm your account but still you cannot login due to missing admin approval, with a quick directory fuzzing I found that the endpoint https://x.y.redacted.com/Admin/User/Me which let me bypass the login, also gospider found an interesting endpoint /Admin/User/activate but it throw Invalid Token, so I decided to add the token which I received in the email confirmation https://x.y.redacted.com/Admin/User/activate?value=[Token], surprisingly I found out I can edit my account details and set a new password, the request was something like this

POST /Admin/User/Activate HTTP/2

Host: x.y.redacted.com

Cookie: XXXXX

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0

Content-Type: application/x-www-form-urlencoded

Content-Length: 745

Connection: close

User.Id=127874&User.Name=sazouki&User.U_status=NonVerified&User.FirstName=sazouki&User.MiddleName=victim&User.LastName=victim&User.PreferredFirstName=&User.PreferredMiddleName=&User.PreferredLastName=&User.UserProfile.WorkPhone=&User.UserProfile.CellPhone=66666666666&User.NewPassword=***REDACTED***

Notice the User.Id? change that to the victim ID and forward the request you will end up changing his account email & password

Thanks all.
