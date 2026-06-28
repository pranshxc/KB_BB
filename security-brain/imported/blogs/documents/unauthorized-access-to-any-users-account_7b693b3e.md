---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-28_unauthorized-access-to-any-users-account.md
original_filename: 2021-10-28_unauthorized-access-to-any-users-account.md
title: Unauthorized access to any user’s account.
category: documents
detected_topics:
- jwt
- idor
- command-injection
- otp
tags:
- imported
- documents
- jwt
- idor
- command-injection
- otp
language: en
raw_sha256: 7b693b3ecac1571301081cbfd36065ac0cab8ce66334bbebf7698a0bd423fb02
text_sha256: 9af5ce553946163d633e55ad473340da2560822d2aa24f1500c8e433c3c89358
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthorized access to any user’s account.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-28_unauthorized-access-to-any-users-account.md
- Source Type: markdown
- Detected Topics: jwt, idor, command-injection, otp
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `7b693b3ecac1571301081cbfd36065ac0cab8ce66334bbebf7698a0bd423fb02`
- Text SHA256: `9af5ce553946163d633e55ad473340da2560822d2aa24f1500c8e433c3c89358`


## Content

---
title: "Unauthorized access to any user’s account."
url: "https://medium.com/@vikramroot/unauthorized-access-to-any-users-account-600e8efe7de0"
authors: ["vikram naidu (@ImVikram7msd)"]
bugs: ["IDOR", "Authentication bypass", "Account takeover"]
publication_date: "2021-10-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3210
scraped_via: "browseros"
---

# Unauthorized access to any user’s account.

Unauthorized access to any user’s account.
vikram naidu
Follow
3 min read
·
Oct 28, 2021

100

Hi everyone! This is Vikram Naidu, Bug bounty hunter and cybersecurity researcher from India. Hope you all are safe. This is my second writeup and it is about my recent finding on a private program where I was able bypass the authentication mechanism . I will be demonstrating how I was able to gain unauthorized access to all the user’s accounts and can see all their data. (In simple terms I was able to hack into anyone’s account without knowing their password).

Lets dive into the process . Below is the login portal where it asks user to enter user id and password.

I have observed that usernames of all the users are in fixed pattern.

So the usernames will look something like : *******001, *******002, *******003, etc .. and passwords are unique for every user.

First I have created 2 accounts(Victim account and attacker account). Now I have entered attacker’s username and password and checked the response of this request using burpsuite (proxy tool). It looks something like this :

Press enter or click to view image in full size

If you observe the response from the server clearly , it is sending JWT (JSON WEB TOKEN).

Get vikram naidu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

WHAT IS A JSON WEB TOKEN?

A JSON web token(JWT) is JSON Object which is used to securely transfer information over the web(between two parties). It can be used for an authentication system and can also be used for information exchange. The token is mainly composed of header, payload, signature. These three parts are separated by dots(.)

After decoding the jwt token i have found out that its sending userid.

Press enter or click to view image in full size

Here in payload data you can see attacker’s username as *********2. Now i have changed the payload data username to victim’s username and got new jwt token and I replaced it with my token in the response and forwarded the response to the browser to check if I am able to login to victim’s account or not. But as soon as I replaced and forwarded the response, browser showed victim’s username only but was not able to login completely , but I am sure that there is some misconfiguration here. So I tried the process from step 1 again to check the response. This time, before forwarding the response to browser I have changed the username to victim’s username in the browser itself. Check in pic below :

Here I have changed the username to *******106 and forwarded the response to the browser and as expected the server was vulnerable due to lack of validation and response manipulation. I was able to login to victim account. Check the screenshot below where i was able to see all his details and logged into his account.

Successfully achieved the mission . Hacked into victim’s account.

Note : I have reported it to the organization on 08–10–2020 and within hours it was fixed and received a $$$$ bounty.

Hope you enjoyed my blog.
