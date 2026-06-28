---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-15_how-i-found-the-authentication-bypass-bug-and-earn-.md
original_filename: 2021-12-15_how-i-found-the-authentication-bypass-bug-and-earn-.md
title: How I found the Authentication Bypass bug and Earn $$$$
category: documents
detected_topics:
- oauth
- command-injection
- otp
- api-security
tags:
- imported
- documents
- oauth
- command-injection
- otp
- api-security
language: en
raw_sha256: 8d479b2ea480ea5caf2c863bdf03e6feda0511131eece5f895fe77df2ac90587
text_sha256: 162ab5dcacfd0c425592ac44ba7b0eede1659f8d2fa34e48d8a07b46673d6bc8
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I found the Authentication Bypass bug and Earn $$$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-15_how-i-found-the-authentication-bypass-bug-and-earn-.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `8d479b2ea480ea5caf2c863bdf03e6feda0511131eece5f895fe77df2ac90587`
- Text SHA256: `162ab5dcacfd0c425592ac44ba7b0eede1659f8d2fa34e48d8a07b46673d6bc8`


## Content

---
title: "How I found the Authentication Bypass bug and Earn $$$$"
url: "https://medium.com/@thedarkwayg/bypass-authentication-1bfab09332fe"
authors: ["Thedarkwayg (@shadow_CLAY)"]
bugs: ["Session expiration issue"]
bounty: "1,000"
publication_date: "2021-12-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3086
scraped_via: "browseros"
---

# How I found the Authentication Bypass bug and Earn $$$$

How I found the Authentication Bypass bug and Earn $$$$
thanhdat1011
Follow
2 min read
·
Dec 15, 2021

303

3

Hi all,

I am @goj0s4t0ru. Today I am going to write about a rather interesting bug that I found 😎

Summary:

This is an application that specializes in online news, media and entertainment.

There are two options when logging in:
+ Login via Oauth
+ Login with Email

Press enter or click to view image in full size
Photos are for illustrative purposes

When I sign in with Google, I need to authenticate my Google account. Then I will be redirected to the redacted.com account.

Suppose: I log out at redacted.com (not signed out of Google) and log back in to redacted.com using Google, I am automatically redirected to the redacted.com account.

Get thanhdat1011’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This is often a misconfiguration because when signed in with Google, users will often be given a choice of the Google account they want to use instead of being redirected directly to redacted.com

Photos are for illustrative purposes

Even if I sign out all, including the Google account. I can still sign in to redacted.com with Google

Exploit:

Now I will login via Oauth -> Google -> Complete the steps to authenticate -> Sign out all including Google account -> Sign in again via Oauth -> Direct access to the account without authentication

Time to attack:

Victim logs into redacted.com account via Google on public computer => Moments later, victim leaves their computer (despite being signed out of redacted.com and Google account) => At this point, anyone can access the victim’s account using Google.

Why does it happen?

Two cases:

Access token/code is not canceled
Auto login

When attacker login with Google => Access token/code will be called by redacted.com and automatically login to the account

Sweet fruit 😎
Press enter or click to view image in full size

The severity of this bug has been reduced because: “the attacker needs access to the victim’s device”

Advice:

I would love to experiment with authentication functions as well as Oauth but I never thought a bug like this would happen in real life.

My advice to you is to always jump out of your comfort zone and think in a bolder direction. Sometimes we think it won’t happen in reality, but in fact it has been happening somewhere. The question is who will find it first?

Thank you everyone for reading!!! ❤

Happy Hacking :)))

Twitter: https://twitter.com/goj0s4t0ru
