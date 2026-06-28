---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-05_account-takeover-user-admin-via-password-reset.md
original_filename: 2021-08-05_account-takeover-user-admin-via-password-reset.md
title: Account Takeover (User + Admin) Via Password Reset
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- automation-abuse
- business-logic
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- automation-abuse
- business-logic
language: en
raw_sha256: bc65c4ae6df5adb99b298379f3f07be0e51e2ca30147f8a436782065b0ee273f
text_sha256: 7adeab213411c9b0f087cf5efa8ad701d11b1855b2299d76d5b332ff2f9fc318
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover (User + Admin) Via Password Reset

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-05_account-takeover-user-admin-via-password-reset.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `bc65c4ae6df5adb99b298379f3f07be0e51e2ca30147f8a436782065b0ee273f`
- Text SHA256: `7adeab213411c9b0f087cf5efa8ad701d11b1855b2299d76d5b332ff2f9fc318`


## Content

---
title: "Account Takeover (User + Admin) Via Password Reset"
url: "https://infosecwriteups.com/account-takeover-user-admin-via-password-reset-322b8020ea6"
authors: ["Hemant Patidar (@HemantSolo)"]
bugs: ["Account takeover", "Password reset", "Logic flaw"]
bounty: "200"
publication_date: "2021-08-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3441
scraped_via: "browseros"
---

# Account Takeover (User + Admin) Via Password Reset

Hemant Patidar
 highlighted

Account Takeover (User + Admin) Via Password Reset
Hemant Patidar
Follow
3 min read
·
Aug 6, 2021

420

Hello Everyone!

I’m Hemant Patidar, Final Year B.Tech - Civil Engineering Student at SRMIST, Chennai.

A Civil Engineer, Cyber Security Enthusiast, and a Bug Bounty Hunter by night.

Press enter or click to view image in full size
Let’s start...

When I’m doing a password reset of our own account we notice that the password reset link sent to our email contain a token which was of five-digit number.

Later on, I came to the conclusion that while doing a password reset of two different users (i.e. Account A and B) in a consecutive manner then the server will assign a token for both the user in a consecutive number. So that if account A is an attacker’s account then the attacker can change the token ID to the next consecutive number and can change the password of account B i.e. victim’s account. Which leads to account takeover.

Example:

If account A received the link: https://dashboard.example.com/password-reset/form?token=28604

Then Account B will receive: https://dashboard.example.com/password-reset/form?token=28605

Now, Let’s takeover the admin account.

After some research, we have found that there is no separate login page for the admin user. Which means that the admin user might be preset over the same login page. So let’s find out the email address of the admin user’s so that we can takeover their accounts. We simply went on the “about-us” page of the website and found the Founder's email address. Now, Let’s takeover the admin account.

Steps-To-Reproduce:

Open the URL in two different tabs: https://dashboard.example.com/login and perform a password reset for both accounts in a consecutive manner using the email address. (i.e. A - Your Account, B - Admin Account)
Now open notepad and copy the password reset link of account A in a notepad (i.e. https://dashboard.example.com/password-reset/form?token=12345)
Now change the Token ID to the next consecutive number. (As the Token ID assigned in a consecutive manner, If your’s is 12345 then the Admin token ID will be 12346)
Now use the modified link i.e. https://dashboard.example.com/password-reset/form?token=12346 and reset the admin password.
Boom!! Admin Account Takeover.

Impact:

Get Hemant Patidar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Account Takeover Of Anyone

#bounty

Timeline:

Bug Reported: Jun 2, 2021

Bounty Rewarded: $200 on Aug 5, 2021

Press enter or click to view image in full size

Thanks for reading :)

Happy Hacking ;)

You can see many writeups coming up…

Feel free to message me if you have any queries related to Bug Bounty Hunting

LinkedIn: linkedin.com/in/HemantSolo

Website:- hemantsolo.in

Twitter:- twitter.com/HemantSolo

Instagram:- instagram.com/hemant_solo
