---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-26_how-to-bypass-a-2fa-with-a-http-header.md
original_filename: 2019-04-26_how-to-bypass-a-2fa-with-a-http-header.md
title: How to bypass a 2FA with a HTTP header
category: documents
detected_topics:
- mfa
- rate-limit
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- mfa
- rate-limit
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 6cc09083a85ec1e57fc819fc1a8c216bc098a96ed2bca7fd02a987439debc8b4
text_sha256: ba101f31302f980cbbc471ef89aa597372a544f203776b723ca0b48352a3d13c
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How to bypass a 2FA with a HTTP header

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-26_how-to-bypass-a-2fa-with-a-http-header.md
- Source Type: markdown
- Detected Topics: mfa, rate-limit, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `6cc09083a85ec1e57fc819fc1a8c216bc098a96ed2bca7fd02a987439debc8b4`
- Text SHA256: `ba101f31302f980cbbc471ef89aa597372a544f203776b723ca0b48352a3d13c`


## Content

---
title: "How to bypass a 2FA with a HTTP header"
url: "https://medium.com/@YumiSec/how-to-bypass-a-2fa-with-a-http-header-ce82f7927893"
authors: ["Yumi"]
bugs: ["2FA / MFA bypass"]
publication_date: "2019-04-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5284
scraped_via: "browseros"
---

# How to bypass a 2FA with a HTTP header

How to bypass a 2FA with a HTTP header
Yumi
Follow
3 min read
·
Apr 26, 2019

304

2

Hi everyone and welcome back on this new write-up.

Today, I would like to talk about a vulnerability I found on some programs that allowed me to bypass their 2FA protections. On a side note, due to the fact that the programs are private, all the informations about the websites will be redacted. That’s said, let’s start !

Introduction:

As many hunters, when I start my research on a new bug bounty program, I use the application as a lambda user. This allow me to understand how the applications work and notice which features can be interesting to test. I noticed that the applications had a 2FA feature, I enabled it and I started to play with it.

For those who are not familiar with the concept of 2FA (Two-factor authentication), this can be defined by:

Two-factor authentication (2FA) is a way to add additional security to your account. The first “factor” is your usual password that is standard for any account. The second “factor” is a verification code retrieved from an app on a mobile device or computer. (Wikipedia)

Press enter or click to view image in full size
Illustration by DoubleOctopus

In a 2FA protection, the verification code is usually an integer between 4 and 6 digits. This mean that the number of combinations for each case is:

4 digits: 10⁴ → 10.000 combinations
6 digits: 10⁶ → 1.000.000 combinations

In both cases, due to the low numbers of combinations, the 2FA code can be brute-forced (especially for 4 digits verification code). With those informations in mind, a 2FA should absolutely have a strong rate limit to not be easily bypassable.

Get Yumi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In the case of the applications I tested, they had a rate limit in place to avoid any kind of brute-force attack against the Two-factor authentication feature.

The bypass:

To be efficient, a rate limit need to be well implemented. I started to search if this limit could be bypassed. My first thought was to search on which value the rate limit was based. I tested the following parameters:

User email address
Session cookies

Strangely, none of this parameter had an impact on the rate limit in place. After few minutes, I remembered a report by corb3nik. He was able to bypass a rate limit on Dashlane bug bounty program with the help of the X-Forwarded-For HTTP header.

According to MDN Web Docs:

Press enter or click to view image in full size

I tested to bypass the rate limit a new time by adding a X-Forwarded-For header to the HTTP request and I was surprised by the fact that the applications accepted my request.

With this issue an attacker could brute-force the Two-factor authentication by using the X-Forwarded-For header when his request will be blocked.

Conclusion:

A rate limit is a solid way to increase the security of your web-application. Nevertheless, they need to be well implemented to be efficient. In the case of a Two-factor authentication feature, the rate limit shouldn’t be based on an information that could be manipulated by the user via the HTTP request.

I hope you enjoyed this reading !

Yumi
