---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-16_a-small-tale-of-account-takeover-.md
original_filename: 2021-09-16_a-small-tale-of-account-takeover-.md
title: A Small Tale of Account Takeover …
category: documents
detected_topics:
- idor
- command-injection
- mfa
- rate-limit
tags:
- imported
- documents
- idor
- command-injection
- mfa
- rate-limit
language: en
raw_sha256: 16f6609e3fe8f574c4f841afd5ddc40a7bd6c10db12f2d5c6ad0f619dd0b5d88
text_sha256: 1af7091bbfc13edab8d8b776352814462467ca1ee2eb02fd74995fda70b137bf
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# A Small Tale of Account Takeover …

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-16_a-small-tale-of-account-takeover-.md
- Source Type: markdown
- Detected Topics: idor, command-injection, mfa, rate-limit
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `16f6609e3fe8f574c4f841afd5ddc40a7bd6c10db12f2d5c6ad0f619dd0b5d88`
- Text SHA256: `1af7091bbfc13edab8d8b776352814462467ca1ee2eb02fd74995fda70b137bf`


## Content

---
title: "A Small Tale of Account Takeover …"
url: "https://medium.com/@sarveshblogs/a-small-tale-of-account-takeover-2eba07a6ef5f"
authors: ["Sarvesh Salgaonkar"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2021-09-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3309
scraped_via: "browseros"
---

# A Small Tale of Account Takeover …

A Small Tale of Account Takeover …
Sarvesh Salgaonkar
Follow
3 min read
·
Sep 16, 2021

151

3

In order to implement a proper user management system in view of security, systems integrate a Change Password service that allows the user to change the existing password. Even though this functionality looks straightforward and easy to implement, it is a common source of vulnerabilities.

During My Recent Pentest Engagement, I was able to takeover any user’s and vendor’s account. The Application had two users — Normal user and Vendor (High Privileged). I will refer the URL as https://uat-example.com . By signing in and choosing Change Password Functionality we land onto a page depicted below:

Press enter or click to view image in full size
1. Change Password Page

Now as demonstrated, enter some random characters into “Old Password” Field. Enter new password into remaining fields and capture the request into Burpsuite.

Press enter or click to view image in full size
2. Request Captured into Burpsuite

Now as you can see, I have entered random characters into “Old Password” Field. By capturing response into Burpsuite, I manipulated response from “Incorrect Old Password” to “Success”.

3. Here I observed the original response
Press enter or click to view image in full size
4. Then I manipulated the response

After forwarding the response, the application accepted it and changed the password successfully.

Press enter or click to view image in full size
5. Application Successfully changed the password
oooohhh….that was kinda broken authentication !!!

But now you will ask me that this vulnerability clearly requires authenticated user then how you are able to takeover anyone’s account? Well, if you have already observed the Cookie Parameter in Request captured into Burpsuite then you my friend, you got that !

Get Sarvesh Salgaonkar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

For Newbies, there’s a cookie parameter which consists of cookie value and user-number (Base64 Encoded) which we can iterate or simply enumerate and can takeover anyone’s account. That’s it !!!

Note: Here the cookie value was not expiring after usage, so it was simply generating some random values and the server was accepting the same numerous times.

Preventive Measures :

There is no definitive “best way” to do this, and what is appropriate will vary hugely based on the security of the application, and also the level of control over the users. Where possible, implement multi-factor authentication to prevent automated, credential stuffing, brute force, and stolen credential re-use attacks.

Thanks for reading ! Hope you gained some knowledge from this one. Take Care and until the next one, Ciao !
