---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-08_account-verification-code-bypass-lead-to-a-4000-bounty.md
original_filename: 2022-05-08_account-verification-code-bypass-lead-to-a-4000-bounty.md
title: Account verification code bypass lead to a $4000 bounty
category: documents
detected_topics:
- otp
- command-injection
- api-security
tags:
- imported
- documents
- otp
- command-injection
- api-security
language: en
raw_sha256: 6bf8182b8e1d7962e79c814ce845494cfee5da389b393309bb3e55e51481e8f4
text_sha256: 6a960fb6e8da025b756fff8bcc8ad72e655a9a23c353db4fcedb86293f30790d
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Account verification code bypass lead to a $4000 bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-08_account-verification-code-bypass-lead-to-a-4000-bounty.md
- Source Type: markdown
- Detected Topics: otp, command-injection, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `6bf8182b8e1d7962e79c814ce845494cfee5da389b393309bb3e55e51481e8f4`
- Text SHA256: `6a960fb6e8da025b756fff8bcc8ad72e655a9a23c353db4fcedb86293f30790d`


## Content

---
title: "Account verification code bypass lead to a $4000 bounty"
url: "https://mokhansec.medium.com/account-verification-code-bypass-lead-to-a-4000-bounty-b31dda6f3011"
authors: ["Mohsin Khan (@tabaahi_)"]
bugs: ["OTP bypass"]
bounty: "4,000"
publication_date: "2022-05-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2652
scraped_via: "browseros"
---

# Account verification code bypass lead to a $4000 bounty

Account verification code bypass lead to a $4000 bounty
Mohsin khan
Follow
2 min read
·
May 8, 2022

899

15

Hello reader,

I hope you are doing well. Today I want to talk about one of my findings. It was a private program and the bug is not fixed yet. So I am not going to include any information about the program/platform here. Let's call it redirect.com.

So redirect.com has a session logout feature. This means on redirect.com there is one option called the session. Here users can see login devices and can log out user/block devices of the particular user.

When a user blocks a device. There is 2 option to unblock the device

Users can unblock from the login device.
Block device login again and for security, redirect.com sends a 4-digit code to the user's email address.

The second option looks interesting right. It looks like a hidden feature to me. So I log in and now redirect.com asks for a 4-digit OTP code. I tried everything from my checklist and nothing works.

Get Mohsin khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The request was a POST request and the content type is application/JSON. I read it somewhere that you can use an Array to bypass OTP verification. Like this (let day the valid OTP was 1337)

{
"otp":[
"1234",
"1111",
"1337",
"2222",
"3333",
"4444",
"5555"
]
}

I tried this and it worked. I reported to them and paid out $4000.

If you are following me on Twitter you know about this finding. I shared a screenshot before.

As you can see I did nothing crazy. The only thing I did was spend time on target and understand features. It was a hidden feature for me. So be the first one to find a hidden feature and test :)

Let me know if you like this.

Thanks for reading!
