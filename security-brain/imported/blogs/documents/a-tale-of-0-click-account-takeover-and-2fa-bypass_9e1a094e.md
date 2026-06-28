---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-12_a-tale-of-0-click-account-takeover-and-2fa-bypass.md
original_filename: 2022-02-12_a-tale-of-0-click-account-takeover-and-2fa-bypass.md
title: A tale of 0-Click Account Takeover and 2FA Bypass.
category: documents
detected_topics:
- mfa
- rate-limit
- api-security
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- mfa
- rate-limit
- api-security
- command-injection
- password-reset
- otp
language: en
raw_sha256: 9e1a094e12a7ac76fcff6e646be9961526657000ddb40fbf2be382f6e5a0206b
text_sha256: b1a9e434be42f5178b098bf6c35c21fbd798b6011fb2f1fc2e0d630bf2afa5d9
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# A tale of 0-Click Account Takeover and 2FA Bypass.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-12_a-tale-of-0-click-account-takeover-and-2fa-bypass.md
- Source Type: markdown
- Detected Topics: mfa, rate-limit, api-security, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `9e1a094e12a7ac76fcff6e646be9961526657000ddb40fbf2be382f6e5a0206b`
- Text SHA256: `b1a9e434be42f5178b098bf6c35c21fbd798b6011fb2f1fc2e0d630bf2afa5d9`


## Content

---
title: "A tale of 0-Click Account Takeover and 2FA Bypass."
url: "https://infosecwriteups.com/a-tale-of-0-click-account-takeover-and-2fa-bypass-b369cd70e42f"
authors: ["Firas Fatnassi (@Fatnass1F1ras)"]
bugs: ["Account takeover", "Password reset", "2FA / MFA bypass"]
publication_date: "2022-02-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2912
scraped_via: "browseros"
---

# A tale of 0-Click Account Takeover and 2FA Bypass.

Top highlight

A tale of 0-Click Account Takeover and 2FA Bypass.
Firas Fatnassi
Follow
4 min read
·
Feb 12, 2022

431

Hey, it’s been a long time since I published a bug bounty write-up. I was in an internship period. So, I had a lot of free time. Anyways, this writeup is about a 0-click account takeover and 2FA bypass. Let’s get started. For the sake of NDA let’s assume https://redacted.com is the target.

Account takeover:
- I started testing doing basic things like changing the host header, seeing if I can brute force the token but nothing seems to be working…(I wrote an article a while ago that had my methodology for testing the password reset functionality: https://medium.com/@fatnassifiras45/how-i-was-able-to-take-over-any-account-via-the-password-reset-functionality-ef1659f8b481).
- The request for getting a password reset link looked like this:

Press enter or click to view image in full size
Password reset request.
As you can see that the email is getting sent to the server using JSON format in a param named email, So, I thought what if I change the type of that parameter from string to an array. So it would be like this: “email”: [“my1stEmail1@gmail.com”, “my2ndEmail@gmail.com”]. Changed the request body to that payload, sent the request, went checking both my emails and fortunately, I received the password reset link on both accounts.
Press enter or click to view image in full size
Changed the email from string to array.

Attack scenario:

Attacker requests a password reset link, intercept that request, and change the email parameter value to [“victim@gmail.com”, “attacker@gmail.com”]
The password reset link will be sent to both the victim’s and attacker's email accounts therefore the attacker can use it and change the victim’s password.

I made a PoC, reported the issue and it made my day seeing a message like this from the triager:

Press enter or click to view image in full size

2FA Bypass:
- Now, Moving to the 2FA mechanism. Here, I enabled the 2FA on my account using the google authenticator app. Yes, the google authenticator app so the code will be 6 digits (1 million possibilities) which would take quite a good time to brute force. Also, not to forget about the rate limit and that Google Authenticator changes the Code every 60 seconds or so. I gave up on brute force as it is not logically possible. And went to the login page put my credentials and intercepted the login request to understand the 2FA mechanism properly and test a few things including:

Response manipulation (e.g., Change param value from false to true → “success”: “true”.
Forced browsing (Going directly to the dashboard page in a new tab after authenticating.)
Code Leakage in response.
Searching for parameters like `2FA_Enabled` so maybe if I change them to false the server will redirect me directly to the dashboard.

Nothing of the above worked. So, I simply intercepted the response to the login request, surprisingly there were some keys leaked there including the API Key.

Press enter or click to view image in full size
API Key/Secret leaked in response.

And having already read the API documentation of the target I knew how to use these keys. So, here if an attacker had the victim credentials the 2FA mechanism would be useless as the attacker can get the victim’s API Key which would give him the ability to do a lot of actions using various API endpoints.

Get Firas Fatnassi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Sometimes, you only need to take a close look at what the server returns to you :). The program was heavily tested by other bug hunters and they missed the above issues. So, never quit a program if it is already tested because everyone has his own methodology and way of thinking!

Bonus TIP to bypass 2FA: If the target allows API authentication via email and password or BASIC auth (base64Encode(username:password)), try setting up the 2FA and see if you can still authenticate to the API using only the email and password. If it is the case then you already bypassed the 2FA as most APIs will allow you to do the same actions done on the web app.

Shout-out to the dev team for their professionalism, fixing the above issues in less than 2 hours efficiently, and for the bounties :-)!

Here is my Twitter: https://twitter.com/Fatnass1F1ras, Please reach out if you have any questions.

Happy hacking!

🔈 🔈 Infosec Writeups is organizing its first-ever virtual conference and networking event. If you’re into Infosec, this is the coolest place to be, with 16 incredible speakers and 10+ hours of power-packed discussion sessions. Check more details and register here.
IWCon2022 - Infosec WriteUps Virtual Conference
Network With World's Best Infosec Professionals. Find How Cybersecurity Pros Achieved Success. Add New Skills to Your…

iwcon.live
