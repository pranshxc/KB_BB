---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-21_confirmation-bypass-.md
original_filename: 2019-04-21_confirmation-bypass-.md
title: '[CONFIRMATION BYPASS ]'
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- information-disclosure
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- information-disclosure
language: en
raw_sha256: 4f0bdd1e507e7f37e1aed3b1d5a152212bb4a8fc0fbbcec1182b542b99386605
text_sha256: a49c8bd6699d6dfdb239eceb22c5fdc304ffb27d00d249eea54c01c1dc5f5e24
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# [CONFIRMATION BYPASS ]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-21_confirmation-bypass-.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `4f0bdd1e507e7f37e1aed3b1d5a152212bb4a8fc0fbbcec1182b542b99386605`
- Text SHA256: `a49c8bd6699d6dfdb239eceb22c5fdc304ffb27d00d249eea54c01c1dc5f5e24`


## Content

---
title: "[CONFIRMATION BYPASS ]"
url: "https://medium.com/@navne3t/confirmation-bypass-ab57c29ae413"
authors: ["Navneet (@na5n33t)"]
bugs: ["Email verification bypass", "Information disclosure"]
publication_date: "2019-04-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5299
scraped_via: "browseros"
---

# [CONFIRMATION BYPASS ]

[CONFIRMATION BYPASS ]
Navneet
Follow
1 min read
·
Apr 21, 2019

89

1

Description :-

The website have functionality which let user to add another email on his/her account. But to confirm whether newly added email belongs to user or not , website sends the confirmation link to the added email address account.

In this article we will see how this confirmation was bypassed which let the bug hunter to add any email which he/she does not own.

I tried to add my email and gets the confirmation link which looks like this

https://www.SomeWebsite.com/account_settings/confirm_email/[SOME_TOKEN_HERE]?and_other_parameters_with_some_values

First I thought this [SOME_TOKEN_HERE] is randomly generated unique token which should be expired after a use and it cannot be predicted. But I was wrong this was nothing but token generated for given email address and this token was reflected at HTTP response of the HTTP request to add email

Get Navneet’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, now what we can do is to add any email which we don't own. e.g. notmyemail@xoxo.com and then intercept the request and look for [SOME_TOKEN_HERE_OF_notmyemail@xoxo.com]

at response of the respective request.
Now the final link will look like this

https://www.SomeWebsite.com/account_settings/confirm_email/[SOME_TOKEN_HERE_OF_notmyemail@xoxo.com]?and_other_parameters_with_some_value

As soon you click on above link , the email address notmyemail@xoxo.com gets confirmed without access of the email address account.

Point to note :-

Look whether any link for any confirmation you recieved at email account is reflecting at HTTP response or not. Somehow, try to use that for bypassing the confirmation.

BOUNTY :-

The program doesn't offer bounty , all I got was +7 reputation points and words from triager "NICE FIND!"
