---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-31_2fa-bypass-due-to-information-disclosure-improper-access-control.md
original_filename: 2022-10-31_2fa-bypass-due-to-information-disclosure-improper-access-control.md
title: 2FA Bypass due to information disclosure & Improper access control.
category: documents
detected_topics:
- mfa
- jwt
- access-control
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- mfa
- jwt
- access-control
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: db60a23b899c43729afc584ca344ab04ba73bf70ce05fe913499c9ca73eeee28
text_sha256: 6c9f5cd9b1e41c2502ac0f581adb81072137fa82f513181c231b34d27fa0f4e9
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: true
---

# 2FA Bypass due to information disclosure & Improper access control.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-31_2fa-bypass-due-to-information-disclosure-improper-access-control.md
- Source Type: markdown
- Detected Topics: mfa, jwt, access-control, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: True
- Raw SHA256: `db60a23b899c43729afc584ca344ab04ba73bf70ce05fe913499c9ca73eeee28`
- Text SHA256: `6c9f5cd9b1e41c2502ac0f581adb81072137fa82f513181c231b34d27fa0f4e9`


## Content

---
title: "2FA Bypass due to information disclosure & Improper access control."
url: "https://akashhamal0x01.medium.com/2fa-bypass-due-to-information-disclosure-improper-access-control-f9a5a8a4e0af"
authors: ["Akash Hamal (@AkashHamal0x01)"]
bugs: ["DoS", "2FA / MFA bypass"]
publication_date: "2022-10-31"
added_date: "2022-10-31"
source: "pentester.land/writeups.json"
original_index: 1969
scraped_via: "browseros"
---

# 2FA Bypass due to information disclosure & Improper access control.

2FA Bypass due to information disclosure & Improper access control.
Akash Hamal
Follow
4 min read
·
Oct 31, 2022

304

1

Hi there, I hope you all are doing well.

This is my 3rd medium writeup on Medium.

Today i will be explaining how i found a 2FA bypass while i was looking for DOS but DOS is possible if the logic isn’t implemented so its worth to look these types of vulnerabilities in organization/team based websites, etc. I hope you enjoy and learn something from it too.

There are some things which should be known or some conditions/functionalities a website must have in order to execute the attack like :

You can create your own Organization & Join other Orgs
You will be logged in into the Org last time you were in when you logged out. For example, if you are Owner of Org A and you have joined Org B, if you switch to Org B and logout then if you login again, you should be in Org B.
You have two 2FA : i) Account Based 2FA ii) Org Based 2FA

If there is Org Based 2FA enabled then you should have Account Based 2FA enabled in order to login into that Org.

Those were technical details above, I enabled my account 2FA and started messing around authentication flow. When i entered my credentials (email and password), in response there were some details revealed like:

The response revealed a parameter with JWT token such as : “2fa”:”<JWT_TOKEN>”
The response also revealed the name of Orgs i was joined in with Org ID and also if those Orgs have 2FA enabled or not.

I tried to use the leaked <JWT_TOKEN> to issue direct HTTP requests to API endpoints [Since the website uses API for most of CRUD actions] but it resulted in 403 Denied because the token is not actually authentication token but i was trying things just to make sure if something will happen.

The <JWT_TOKEN> was used in 2FA HTTP request with the “code” parameter and the “code” has 6 digit google authenticator code value.

So the flow was like this :

Enter email and password=***REDACTED*** reveals “2fa”:”<JWT_TOKEN>, in response => You have to enter 2fa code => Enter 6 digit 2fa code and HTTP body contains {“2fa”:”<JWT_TOKEN>”, “code”:<6 digit 2fa code”>}

So the “2fa” and its value is issued along with “code” parameter which completes 2FA step and logs us into the account. So which means here “2fa” is necessary for completing the 2FA step.

Get Akash Hamal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I couldn’t find any vulnerability but one scene struck my mind and i wanted to try out as i thought it would lead to DOS. The scene is like this:

Suppose you have joined two Orgs: One is your Own Org where you are Owner and Second is the Attacker Org where you have “Member” role. Assume that you don’t have Account 2FA enabled and none of those Org have Org based 2FA enabled. Let’s say that you are logged into the Attacker Org (Org B) and you now logout. When you login into your account you will be in Org B because that was the Org you were in when you logged out. The flow looks simple but what if before you login, the Owner of Attacker Org (Org B) enables Org Based 2FA , will it deny you to login? because you need to have 2fa enabled in order to login. Let’s find out:

I found out that, upon doing what i said above, i am given two options when i enter my mail and password=***REDACTED*** Org have 2FA enabled, please Setup 2FA”, option but when u click it then a code will be sent to the mail since we don’t have access to Victim mail , choosing this ain’t worth
The second option was “Switch Org” , it allowed me to switch to Org which don’t have 2FA enabled (which in this case is my Own Org). Upon analyzing the HTTP request, i came to know that the leaked information can be used in the HTTP request to get into the Org which don’t have 2FA enabled because the HTTP request to switch to Org was :

POST /api/org/<ORGID>
Host: example.com

{“2fa”:”<JWT_TOKEN>”}

So i discovered an endpoint, which accepts the leaked info and lets us into the account.

So the final scenario will be :

NOTE: In this scene, The victim has joined two Org, and only one Org have 2FA enabled. Also the Victim have account based 2FA enabled.

=> Enter email and password -> Get “2fa”:”<JWT>” from response and get Org ID of Org which don’t have 2FA enabled. Then issue the following http request:

POST /api/org/<ORG ID>
Host: example.com

{“2fa”:”<JWT_TOKEN>”}

It will login you into the account hence bypassing Account 2FA.

In short: I found an endpoint which accepts leaked values and lets you into the account.

This writeup is mostly dependant on how functionalities/exceptions/edge cases are implemented. I hope this writeup taught you something and is applicable to finding DOS mostly, finding new endpoints, etc.

Thanks again for spending your valuable time, if you got any questions. You can reach me out on twitter, or reply here. Stay tuned for other writeups ahead!
