---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-13_hey-userid-x-whats-your-secret-token-broken-api-enables-me-to-leakmodify-any-use.md
original_filename: 2017-07-13_hey-userid-x-whats-your-secret-token-broken-api-enables-me-to-leakmodify-any-use.md
title: Hey UserID x, what’s your secret token? Broken API enables me to leak/modify
  any users personal information
category: documents
detected_topics:
- api-security
- mobile-security
- idor
- command-injection
- otp
tags:
- imported
- documents
- api-security
- mobile-security
- idor
- command-injection
- otp
language: en
raw_sha256: e848695b50fb91b5aa29f754fa04be69f3876073fa5c0b8f3b0f276b12206fc7
text_sha256: 8d770b618be89534585445c7a986afcd67118c5bee8a8cdf461d7351245f0554
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: true
---

# Hey UserID x, what’s your secret token? Broken API enables me to leak/modify any users personal information

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-13_hey-userid-x-whats-your-secret-token-broken-api-enables-me-to-leakmodify-any-use.md
- Source Type: markdown
- Detected Topics: api-security, mobile-security, idor, command-injection, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: True
- Raw SHA256: `e848695b50fb91b5aa29f754fa04be69f3876073fa5c0b8f3b0f276b12206fc7`
- Text SHA256: `8d770b618be89534585445c7a986afcd67118c5bee8a8cdf461d7351245f0554`


## Content

---
title: "Hey UserID x, what’s your secret token? Broken API enables me to leak/modify any users personal information"
url: "https://zseano.medium.com/fun-with-mobile-apps-broken-api-leads-to-leak-of-millions-of-personal-information-e7eb0b9dcce7"
authors: ["Zseano (@zseano)"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2017-07-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6156
scraped_via: "browseros"
---

# Hey UserID x, what’s your secret token? Broken API enables me to leak/modify any users personal information

Hey UserID x, what’s your secret token? Broken API enables me to leak/modify any users personal information
Sean (zseano)
Follow
3 min read
·
Jul 13, 2017

590

1

Here is a fun story about how I found IDOR to leak any users’ details, and then broke their patch. The mobile app was leaking any users unique hash, which was required to view & modify your personal data, along with their userid (just an integer). Let’s begin!

I downloaded the app from the iOS store and setup BURP. I quickly signed up for an account and began monitoring the traffic. Usually a mobile app will use an API to query users’ details, and typically it will look like this: https://api.example.com/api?act=get_user&id=1 — and it will return user id 1details. (usually in JSON format). The same applies for modifying your profile information.

I thought why not just change the id to 2 and see what happens. This is where things were just a bit too easy.. because it just worked. Changing the id value to any userid I wanted would reveal their information, as well as let me update their password! (without ANY verification).

I quickly reported it via Bugcrowd and was given a P1.

Shortly after they issued a fix and after re-trying it appeared to be fixed.

Fast forward to now and I decided to revisit a majority of my bugcrowd reports. Now when you query this sites API, the request looks like this:

https://api.example.com/api?act=get_user&id=1&hash=E9ih29plz0a

The “hash” value had to match whoever’s id you was querying in order to view that ids information. Pretty good protection, but not wanting to try decode the hash value, I decided to see if I could break it. Time to play!

Get Sean (zseano)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Querying for your information with a blank hash would respond:

“result_msg”:”The \”hash\” parameter is mandatory for this api key”,”result_cached”:”none”,”data”:[],”sync”:[]}

Hmm, ok. Interesting. Now what about updating your account information? The query looked like this:

https://api.example.com/api?act=update_user&id=1&hash=E9ih29plz0a&name=sean&password=***REDACTED***

Sending a valid hash updated my information, so now let’s see what would happen if I send a blank hash with this request (the ?act param has changed, so different code will be executed behind the scenes.). Now here’s where things again got a bit too easy. Changing hash to null replied with the following:

{“result”:1,”result_code”:null,”result_detail”:””,”result_msg”:””,”result_cached”:null,”data”:{“user_id”:1,”hash”:”E9ih29plz0a"},”sync”:[]}

(The fact that I changed the “act” parameter is critical here. From testing, this was the only endpoint which leaked the users hash.)

Are you thinking what i’m thinking? Is that hash value tied to userid 1? I changed the id to 2 and the hash value changed. Interesting..

Now what happens if we take that hash and now try view their info by sending it with the first request? Bingo! We have access to all their users’ data again! Not only this, but we can remotely reset any users password… ouch.

So from sending a blank hash on a certain function we’ve managed to find a way to leak any users secret hash, which can then be used to obtain access to their account/reveal private information. The bonus? The hash never changes.

Press enter or click to view image in full size
