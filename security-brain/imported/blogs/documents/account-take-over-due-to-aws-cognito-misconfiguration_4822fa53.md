---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-16_account-take-over-due-to-aws-cognito-misconfiguration.md
original_filename: 2023-01-16_account-take-over-due-to-aws-cognito-misconfiguration.md
title: Account Take Over Due To AWS Cognito Misconfiguration
category: documents
detected_topics:
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- command-injection
- otp
- cloud-security
language: en
raw_sha256: 4822fa53139816e32cd120d458ea9fa6b7f416ee9f810edcdc3c9dce64e00a30
text_sha256: 82fa3bb3700fd3ad2eeca46cedb310765564d5693004f015c58f0f366a4a94bf
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Account Take Over Due To AWS Cognito Misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-16_account-take-over-due-to-aws-cognito-misconfiguration.md
- Source Type: markdown
- Detected Topics: command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `4822fa53139816e32cd120d458ea9fa6b7f416ee9f810edcdc3c9dce64e00a30`
- Text SHA256: `82fa3bb3700fd3ad2eeca46cedb310765564d5693004f015c58f0f366a4a94bf`


## Content

---
title: "Account Take Over Due To AWS Cognito Misconfiguration"
url: "https://medium.com/@_deshine_/account-take-over-due-to-aws-cognito-misconfiguration-7b092c667ee3"
authors: ["Deshine"]
bugs: ["Amazon cognito misconfiguration", "Account takeover"]
publication_date: "2023-01-16"
added_date: "2023-01-18"
source: "pentester.land/writeups.json"
original_index: 1669
scraped_via: "browseros"
---

# Account Take Over Due To AWS Cognito Misconfiguration

Account Take Over Due To AWS Cognito Misconfiguration
Deshine
Follow
2 min read
·
Jan 16, 2023

54

1

Press enter or click to view image in full size

In this post, I will share how I check the misconfiguration in AWS Cognito leads to Account Takeover.

I was invited to a Hackerone program a few months ago. It’s a banking app but uses AWS Cognito to authenticate users. (To know more about AWS Cognito, check out this link: https://docs.aws.amazon.com/cognito/?icmpid=docs_homepage_security)

When register in the application, the request will look like this:

Press enter or click to view image in full size

The app will ask for username, password, email, and a “custom:userId” field that the app itself adds. The “custom:userId” value will be the userId used inside the app.

Then confirm the OTP with the following request:

Press enter or click to view image in full size

The misconfiguration in here is when a new user registers with the same “custom:userId” and use ForceAliasCreation as true.

Get Deshine’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The AWS Cognito will replace value “custom:userId” of previous user with the latest one. The application does not check whether this “custom:userId” belongs to someone else, so at this time the new user will take over the owner account.

Press enter or click to view image in full size

Because the format of “custom:userId” is UUID, the severity is downgraded to high.

This is one of the rare cases i come across.

In most AWS Cognito applications that I tested, they do not allow user to create an account.

So if you find a website using AWS Cognito, please check this case.

Thank you for spending time reading.

Have a wonderful year!!!

DESHINE
