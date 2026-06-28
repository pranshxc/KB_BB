---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-30_mfa-bypass-in-private-program-the-abdulsec-way.md
original_filename: 2022-08-30_mfa-bypass-in-private-program-the-abdulsec-way.md
title: mfa bypass in private program, the abdulsec way
category: documents
detected_topics:
- mfa
- command-injection
- rate-limit
tags:
- imported
- documents
- mfa
- command-injection
- rate-limit
language: en
raw_sha256: 1e4dfc4815abe5078fa0fb116f71e70c55f89e31659ab6b5a8d544d446866cd7
text_sha256: 42c2f5a988be146801684710fbb19efede17e5cdbe14257a447cfb7d8d50d628
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# mfa bypass in private program, the abdulsec way

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-30_mfa-bypass-in-private-program-the-abdulsec-way.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `1e4dfc4815abe5078fa0fb116f71e70c55f89e31659ab6b5a8d544d446866cd7`
- Text SHA256: `42c2f5a988be146801684710fbb19efede17e5cdbe14257a447cfb7d8d50d628`


## Content

---
title: "mfa bypass in private program, the abdulsec way"
url: "https://abdulsec.medium.com/mfa-bypass-in-private-program-the-abdulsec-way-f677fea209f7"
authors: ["abdulsec (@moodiAbdoul)"]
bugs: ["2FA / MFA bypass"]
bounty: "600"
publication_date: "2022-08-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2239
scraped_via: "browseros"
---

# mfa bypass in private program, the abdulsec way

mfa bypass in private program, the abdulsec way
abdulsec
Follow
2 min read
·
Aug 30, 2022

184

2

image by rezo

Hi , i hope you are doing well , it’s been a while since my last write up , today i wanna share with you a technique that i used to bypass a multi factor authentication in a private program

Tools used:

burp community and firefox

first
when you login in to your account and you enable Two-factor authentication , and logout
if you login the next time you will redirect to setup Two-factor authentication

second
when you login to an account that has completely setup the mfa you will be redirect to challenge page where to have to enter a valid code composed of (6) number , don't even think about to brute force as it’s not sms based mfa

after i analyzed the different response between an account that has two-factor authentication , and an account that has enabled 2fa but didn’t set up it i have found the different are only the response header
X-Mfa-Redirect: mfaChallengePage and X-Mfa-Redirect: mfaSetupPage

Get abdulsec’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

to bypass the 2fa , i have modified the response header X-Mfa-Redirect: to redirect to mfaSetupPage insted of mfaChallengePage

Step to Reproduce
in burp suite , go to proxy > options — match and replace
add response header , match : mfaChallengePage and replace : mfaSetupPage
login in your victim account that has two-factor authentication
you will redirect to setup a new 2fa
finish to setup the mfa and you will redirect to your victim account without having a valid mfa code
boom you have successfully bypassed the two factor authentication

thank you so much ,

if you liked this write-up follow me in twitter , you can also buy me a coffee

JavaScript is not available.
Edit description

twitter.com

https://www.buymeacoffee.com/abdulsec

timeline

Submitted: 16 Oct 2021 01:39:34 UTC

rewarded :$600 19 Oct 2021 13:53:15 UTC

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!
