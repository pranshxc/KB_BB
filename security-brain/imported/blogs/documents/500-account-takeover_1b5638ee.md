---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-14_500-account-takeover.md
original_filename: 2022-06-14_500-account-takeover.md
title: 500$ Account Takeover
category: documents
detected_topics:
- oauth
- jwt
- command-injection
- password-reset
- otp
- automation-abuse
tags:
- imported
- documents
- oauth
- jwt
- command-injection
- password-reset
- otp
- automation-abuse
language: en
raw_sha256: 1b5638eecb64f4bfa2a82dd6e94085e29d53ede280b7922959817f27a9498b6d
text_sha256: d8af597f5af7afcd50be6fdca6c85e0b4781443626ad6056e061e05243195b18
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# 500$ Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-14_500-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, jwt, command-injection, password-reset, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `1b5638eecb64f4bfa2a82dd6e94085e29d53ede280b7922959817f27a9498b6d`
- Text SHA256: `d8af597f5af7afcd50be6fdca6c85e0b4781443626ad6056e061e05243195b18`


## Content

---
title: "500$ Account Takeover"
url: "https://medium.com/@kashyapherry147/500-account-takeover-b008f1ccb4a2"
authors: ["Hemant Kumar"]
programs: ["Xsolla"]
bugs: ["Account takeover", "Information disclosure", "HTTP response manipulation"]
bounty: "500"
publication_date: "2022-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2559
scraped_via: "browseros"
---

# 500$ Account Takeover

500$ Account Takeover
HEMANT
Follow
2 min read
·
Jun 14, 2022

61

1

I guys, today i’m gonna share with you one of my intresting finding, which is Account Takeover by chaining 3 vulnerabilities . 1) Preaccount 2) Response manipulation 3) Login token leaked in response .

Lets’ start

Program Xsolla.com

Press enter or click to view image in full size

So, last month (may 2022 ). I got a target from one of my friend circle . Which is Xsolla.com . So, first of all i gathered all subdomains . And i choosed https://clubs.xsolla.com subdomain. And i got a login and sign up page there . Then I tried there Pre account takeover ( Account Squatting) , Because there is both way to login ( oauth and normal login ) . So, i sign-upped there and in the response of sign-up request , i got a JWT token leakaged , Which is used for Login also . After sign-upped there, i directly login into account, and update name and lastname . There was not any kind of email verification . And then i logged out from there and now i tried to login with oauth. And i was lucky i found (Account squatting ) vulnerability. But when i tried to login with credentials , site shows (email and password wrong) . Then i thought , why not we try here that leaked Token and and response manipulation . So, i just put email and password, and then captured the request in burpsuite. And go to response to this request and forward the request , and in reponse, changed 400 to 200 OK , and submitted the leaked token in response and click on forward . And BOOM, I logged in successfully . And i was like

Linkedin : https://www.linkedin.com/in/hemant-k-714564199/

Get HEMANT’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

instagram: https://www.instagram.com/cyber__hawk/

Youtube: https://www.youtube.com/channel/UCKNK64OMhj8y1YByqRPalUw

Submit report : 12 may 2022

Triage : 16 may 2022

Bounty: 22 may 2022

After this, i reported 10 More Vulnerabilities . 8 was Duplicate. 1 Accepted .1 Informative
