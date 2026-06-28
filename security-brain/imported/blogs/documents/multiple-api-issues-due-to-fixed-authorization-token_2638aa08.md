---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-24_multiple-api-issues-due-to-fixed-authorization-token.md
original_filename: 2019-05-24_multiple-api-issues-due-to-fixed-authorization-token.md
title: Multiple API issues due to Fixed Authorization token.
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: 2638aa082019f645ca26d15d388b9864360afa11fc199b50be86fe17cfbbbfb6
text_sha256: 8299db8ed6fb19bf53a74f19cfa06d2e0a93f87cf8fc7b949d1abe0d98dd6c32
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple API issues due to Fixed Authorization token.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-24_multiple-api-issues-due-to-fixed-authorization-token.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `2638aa082019f645ca26d15d388b9864360afa11fc199b50be86fe17cfbbbfb6`
- Text SHA256: `8299db8ed6fb19bf53a74f19cfa06d2e0a93f87cf8fc7b949d1abe0d98dd6c32`


## Content

---
title: "Multiple API issues due to Fixed Authorization token."
url: "https://medium.com/@mustafakhan_89646/multiple-api-issues-due-to-fixed-authorization-token-17365056f17a"
authors: ["Mustafa Khan (@by6153)"]
bugs: ["Broken authorization"]
publication_date: "2019-05-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5244
scraped_via: "browseros"
---

# Multiple API issues due to Fixed Authorization token.

Multiple API issues due to Fixed Authorization token.
Zeeshan Mustafa
Follow
3 min read
·
May 24, 2019

250

2

Press enter or click to view image in full size

This bug isn’t fixed yet and it’s on a private program so I can’t disclose the program name and their users data.

The root cause was a fixed Authorization token for every users which led to users’ information disclosure, exploitation of misconfigured CORS, and remotely changing users’ information.

My methodology for testing API endpoints:

Chrome > F12 > network tab > and signup/login to my account.

Most of the endpoints are reflecting over here and I can see the HTTP request and response like which headers are passing and is there any authorization token and origin header is present or not.

Get Zeeshan Mustafa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So here I begin, I was testing this program using the same above method I created a test account and logged into my account and I was checking for interesting requests and I got “someapi.domain.com” with a nice rest API endpoint which is “/v1/users/my-uid”. So, I was checking the request headers for Authorization header and Origin header both were present I lost my hope.

Because when in the request header Authorization header is present even misconfigured CORS won’t be exploitable. For my confirmation I visited the endpoint along with my UID I was shocked it was showing all my information without the authorization token in a GET based request. I immediately tried to exploit the CORS but I failed due to the authorization token so I logged out of my account to check whether the token gets expired or not and it wasn’t expired. Then I created a second account and took the second account’s uid and replaced with my current uid with the same authorization token and it was showing the second account’s information so I compared both authorization token and I was way surprised it was same so all the users get the same fixed authorization token with different UIDS and ran a brute force via burp intruder and got so many valid UIDS.

The below images show the requests and responses.

Press enter or click to view image in full size
User’s info disclosure.
Press enter or click to view image in full size
Updating anyone’s information by changing the UID.

Summary: Don’t give up when you see a dead end instead try it to understand whats happening and is the server validating it correctly.

To my luck it got duplicate but it was too fun to find and exploiting it and I learned new things.

NOTE: It’s not fixed yet but when it gets fixed I’ll update this write up with a video poc for clear steps.

I tried hard to write it as a fun read so that no one get bored I hope it won’t bore anyone. ❤
