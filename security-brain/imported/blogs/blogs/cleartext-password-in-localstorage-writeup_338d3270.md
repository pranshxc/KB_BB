---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-07_cleartext-password-in-localstorage-writeup.md
original_filename: 2019-07-07_cleartext-password-in-localstorage-writeup.md
title: Cleartext password in LocalStorage (Writeup)
category: blogs
detected_topics:
- api-security
- xss
- command-injection
- otp
tags:
- imported
- blogs
- api-security
- xss
- command-injection
- otp
language: en
raw_sha256: 338d32709cf6655c28c5bcaea85a5d1c7a6ee4272acb5eba1b2607d2135881f8
text_sha256: 0f240b573de3ba2eae19a4039f83e11714220b9f21305e115076b07eacb90fc6
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# Cleartext password in LocalStorage (Writeup)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-07_cleartext-password-in-localstorage-writeup.md
- Source Type: markdown
- Detected Topics: api-security, xss, command-injection, otp
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `338d32709cf6655c28c5bcaea85a5d1c7a6ee4272acb5eba1b2607d2135881f8`
- Text SHA256: `0f240b573de3ba2eae19a4039f83e11714220b9f21305e115076b07eacb90fc6`


## Content

---
title: "Cleartext password in LocalStorage (Writeup)"
url: "https://medium.com/@ruvlol/cleartext-password-in-localstorage-writeup-245294762829"
authors: ["ruvlol"]
bugs: ["Violation of secure design principles"]
bounty: "1,500"
publication_date: "2019-07-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5163
scraped_via: "browseros"
---

# Cleartext password in LocalStorage (Writeup)

Cleartext password in LocalStorage (Writeup)
ruvlol
Follow
2 min read
·
Jul 7, 2019

98

2

Press enter or click to view image in full size

Hey. I want to share a cool and uncommon vulnerability I found in one of bug bounty programs.

Once I was testing an application, I suddenly decided to look into LocalStorage content. For those who are not familiar, LocalStorage is a key-value storage in browsers. It is not safe to use LocalStorage for storing a sensitive information, because it is always accessible from javascript. Unlike cookies, when setting one you can simply add a HttpOnly flag to make it safe against XSS attacks (unless you reflect it somewhere else), but in case of LocalStorage there is no such thing, it is impossible to restrict access to javascript and any XSS on target origin compromises it’s LocalStorage completely.

By the way, it is also reasonable to look into SessionStorage along. The difference between them is that LocalStorage keys are not expiring, while SessionStorage keys expiring after tab closing. In case of XSS it is possible to get SessionStorage keys, if XSS is stored.

Get ruvlol’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, basically I was looking for something like api keys or tokens if they were saved there. Once I opened it in browser (F12 -> Storage -> LocalStorage | SessionStorage), I saw only one row and it was log history for marketing purpose.

Press enter or click to view image in full size

It is a big json containing any action I did on a website. It also had an object with two fields:

[{

“account.username” : “ruvlol”,

“account.password” : “redacted”

}]

On the moment I saw that I didn’t believe it. This behaviour was constant, giving absolutely same results after I logged in the application via blank browser and looked in LocalStorage.

I reported it immediately and got $1500 bounty which was a High severity according to their policy.

It only required to run following javascript to get someone else’s password=***REDACTED*** test = JSON.parse(localStorage.edited);

console.log(‘your username is: ‘ + test.edited.account.username + ‘ and your password is: ‘ + test.edited.account.password);

By the way, I have patreon where I am writing infosec articles. If you are interested you can check it out on https://www.patreon.com/ruvlol , I am working hard to make it a good source of ethical hacking exprience, a lot of articles are coming there including bug bounty writeups.
