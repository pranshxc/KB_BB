---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-27_abusing-json-web-token-to-steal-accounts-3000.md
original_filename: 2021-07-27_abusing-json-web-token-to-steal-accounts-3000.md
title: Abusing JSON Web Token to steal accounts — 3000$
category: documents
detected_topics:
- jwt
- idor
- xss
- sqli
- command-injection
- otp
tags:
- imported
- documents
- jwt
- idor
- xss
- sqli
- command-injection
- otp
language: en
raw_sha256: 25d6906235eddd80884b378605cdbd4e5ba4d8053a07552ef4948dac4693af2f
text_sha256: 6cbd5c36445a93a63f8aebbca749327a00e8128836e2dc984c9704187c769de2
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing JSON Web Token to steal accounts — 3000$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-27_abusing-json-web-token-to-steal-accounts-3000.md
- Source Type: markdown
- Detected Topics: jwt, idor, xss, sqli, command-injection, otp
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `25d6906235eddd80884b378605cdbd4e5ba4d8053a07552ef4948dac4693af2f`
- Text SHA256: `6cbd5c36445a93a63f8aebbca749327a00e8128836e2dc984c9704187c769de2`


## Content

---
title: "Abusing JSON Web Token to steal accounts — 3000$"
url: "https://filipaze.medium.com/abusing-json-web-token-to-steal-accounts-3000-b9f7daeaef81"
authors: ["Filipe Azevedo (@filipaze_)"]
bugs: ["IDOR"]
bounty: "3,000"
publication_date: "2021-07-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3473
scraped_via: "browseros"
---

# Abusing JSON Web Token to steal accounts — 3000$

Abusing JSON Web Token to steal accounts — 3000$
Filipe Azevedo
Follow
2 min read
·
Jul 27, 2021

236

Press enter or click to view image in full size
https://jwt.io/

Hello fellow hackers! 👋

My name is Filipe Azevedo, I am a Cyber Security Researcher from Portugal. I work mainly for Intigriti and Hackerone.

Today I’m going to show you a recent finding on a private program.

So, let’s go to the vulnerability.

What’s JWT?

JWTs provide a stateless solution to authentication by removing the need to track session data on the server. Instead, JWTs allow us to safely and securely store our session data directly on the client in the form of a JWT:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

The first part, HEADER, tell us the algorithm and token type.

The second, contains the payload itself, the information to pass.

Lastly, the verified signature, is what prevents the token from being edited.

Get Filipe Azevedo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You can know more about JWT here

Detection and exploitation of the vulnerability

I was looking for bugs such as XSS, SQL Injection, IDOR’S, but the target was pretty secure. So I start to search for bugs in the authentication flow.

I notice that the only difference between the two JWTs was the ID present on the payload. I found out that this value was the user’s account number. So, if I change my ID to the victim’s I could access any account.

How to find out the victim’s ID

There was no dedicated login and registration page. The user entered his email and clicked “Next”. The server would check the email and forward the user for login or registration.

But during this process, the ID was leaked. If the email existed, a request was sent with the email and the ID. Something like this:

email=victim@gmail.com&id=123456

Bug Reported: Apr 19, 2021

Bounty rewarded 3000$: May 31, 2021

Press enter or click to view image in full size

For queries, you can DM on Twitter. Feedbacks are always welcome!

Thanks for reading.

Happy Hacking!!!
