---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-27_how-did-i-earned-6000-from-tokens-and-scopes-in-one-day.md
original_filename: 2021-08-27_how-did-i-earned-6000-from-tokens-and-scopes-in-one-day.md
title: How did I earned 6000$ from tokens and scopes in one day
category: documents
detected_topics:
- access-control
- api-security
- jwt
- command-injection
- otp
- supply-chain
tags:
- imported
- documents
- access-control
- api-security
- jwt
- command-injection
- otp
- supply-chain
language: en
raw_sha256: a4594e8763cccf4d94d1b1f9ab8412ae6d06c1b68d8484a43585cdbe12e6545b
text_sha256: d50c36289abbc9f7e2d7611ae6000365e393a95dfd7b71e1cfacc59d0389c4db
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How did I earned 6000$ from tokens and scopes in one day

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-27_how-did-i-earned-6000-from-tokens-and-scopes-in-one-day.md
- Source Type: markdown
- Detected Topics: access-control, api-security, jwt, command-injection, otp, supply-chain
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `a4594e8763cccf4d94d1b1f9ab8412ae6d06c1b68d8484a43585cdbe12e6545b`
- Text SHA256: `d50c36289abbc9f7e2d7611ae6000365e393a95dfd7b71e1cfacc59d0389c4db`


## Content

---
title: "How did I earned 6000$ from tokens and scopes in one day"
url: "https://infosecwriteups.com/how-did-i-earned-6000-from-tokens-and-scopes-in-one-day-12f95c6bf8aa"
authors: ["Corraldev (@javier_corralg)"]
bugs: ["Broken authorization", "Privilege escalation"]
bounty: "6,000"
publication_date: "2021-08-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3382
scraped_via: "browseros"
---

# How did I earned 6000$ from tokens and scopes in one day

How did I earned 6000$ from tokens and scopes in one day
Corraldev
Follow
2 min read
·
Aug 26, 2021

334

I don’t do bug bounty quite often because it’s very hard to find something interesting and to be the first reporter… but the other day was different.

I opened my email and saw an invitation for a private Hackerone program. I took a look at it and the bounties were attractive so I said why not?

FIRST STAGE ( Recon )

Scope was very reduced, only two hosts:

api.company.com

app.company.com

I created an account and then I started to sniff my traffic with Burp, first look revealed that they were using Auth0 for handling authentication, Express.JS for the web and JWT for sessions.

First thing I tried was to change the alg of JWT to none and then impersonate some employee but that its too obviously. None is not an algorithm valid said an error message.

One feature of the application is you can invite users to a group and then change their account’s privileges/scopes.

At that point I was very focused on gain privileges and escalate my account to employee. After reading thousands lines of javascript code I realized that there were some scopes that do not appear in the edit user privileges menu…

SECOND STAGE ( Gain privileges )

Get Corraldev’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I detected 2 interesting scopes: company:support and company:operations

Their name was telling me that those scopes was reserved to employees, so first thing I tried was: invite other user into the group and then change his scopes to the employees ones.

Kids stuff… Intercept the request with burp and then spoof the scopes parameter. 200 OK From server and in that point I could receive a bounty but I wanted more…

THIRD STAGE ( Confirm it )

Now we have the account with employees privileges but the application seems to be the same, no changes, no admin actions. So back to recon again.

Inside javascript library were api references to a service that I wasn’t saw before and in a comment below it said something like: service for employees operations 🥳

So what I tried? You have guessed right, send a request to that api reference and cross the fingers to get a 200 OK.

At this point I confirmed the privilege escalation.

Report to the program, 9.9 CVSS 3.1 and a bounty of 3000$.

Wait! You said 6000$ ?

There was another feature: You can create API Keys for your account … and assign scopes to it! 🤭🤭🤭

Intercept the api generation request and spoof the parameter scopes with the employees one and done! Another 9.9 cvss 3.1 and 3000$
