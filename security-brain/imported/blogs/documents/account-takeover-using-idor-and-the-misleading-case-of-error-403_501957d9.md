---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-11_account-takeover-using-idor-and-the-misleading-case-of-error-403.md
original_filename: 2019-06-11_account-takeover-using-idor-and-the-misleading-case-of-error-403.md
title: Account takeover using IDOR and the misleading case of error 403.
category: documents
detected_topics:
- oauth
- idor
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- oauth
- idor
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 501957d9ea7e0bff2b553134255ec7df93aabac66c98995835d93d4944fed4b3
text_sha256: 0b473d9868e80754de1cb10a5779dc69b4ab40f4ba011ae72d8fab35eccc9621
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Account takeover using IDOR and the misleading case of error 403.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-11_account-takeover-using-idor-and-the-misleading-case-of-error-403.md
- Source Type: markdown
- Detected Topics: oauth, idor, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `501957d9ea7e0bff2b553134255ec7df93aabac66c98995835d93d4944fed4b3`
- Text SHA256: `0b473d9868e80754de1cb10a5779dc69b4ab40f4ba011ae72d8fab35eccc9621`


## Content

---
title: "Account takeover using IDOR and the misleading case of error 403."
url: "https://medium.com/bugbountywriteup/account-takeover-using-idor-and-the-misleading-case-of-error-403-cb42c96ea310"
authors: ["Plenum (@plenumlab)"]
bugs: ["IDOR"]
publication_date: "2019-06-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5224
scraped_via: "browseros"
---

# Account takeover using IDOR and the misleading case of error 403.

Account takeover using IDOR and the misleading case of error 403.
Plenum
Follow
3 min read
·
Jun 11, 2019

240

2

H
ello and welcome again, today i want to share with you the story of how i found a quite simple bug in under 45 minutes this bug was there for a long time and was missed by top hunters on a public program with 100+ resolved reports. This is why you should NEVER trust status codes.

Press enter or click to view image in full size

It was late and i was not that motivated so i went checking new programs and saw this one program that looked promessing it had simple functionalities nothing fancy, perfect for a light hunting session. The app looked pretty straightforward users can interact with other accounts posting comments and rating stuff.

Anyways once i created an account i immediatly went to check my profile to understand how the app works and answer pretty basic questions like:

Does the app fetch information from an api and where is it located (a subdomain, a path on root domain)?
What kind of authentication is in place and how does it work?
Is there any id to identify current user?
Is this id being disclosed anywhere publicly?

Started to get an idea of the app and then refeshed the page but this time i kept the proxy on and manually forwarded all the requests and this is where i noticed something interesting, in the app you can link your facebook account, the connect button was loaded seperatly inside an iframe the request however is what cought my eye it was a get request that looked like this

Get Plenum’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://www.redacted.com/connect/facebook_login?id=[ID]&token=[TOKEN]

No signature no hash :D

The response contained the facebook redirect link all with the necessary information to start the oauth flow including the account id so i immediatly went and created a new account and started playing with the two accounts the idea was if i can control the iframe response it maybe possible to takeover the account.

Grabbed the id from account A then went to account B modified the iframe request and forwarded the request then cliqued on connect facebook button on account B all went as planned but after the redirect from facebook i got error 403 refreshed the page on both accounts and the button still showed up but then i had an idea lets logout from account A and click connect with facebook and sure enough i was inside account A with the facebook of account B so i took over the account without the user being notified he didn’t even know he had facebook connected because the button kept showing up.

The id is not a secret i could get it by simply visiting victim’s profile, to make matters worse even if the victim had their facebook connected you can overwrite it using this method.

This is not the first time i get an error and end up finding that the attack worked you should always double check.
