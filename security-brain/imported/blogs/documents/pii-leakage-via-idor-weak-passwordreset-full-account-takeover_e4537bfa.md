---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-25_pii-leakage-via-idor-weak-passwordreset-full-account-takeover.md
original_filename: 2020-09-25_pii-leakage-via-idor-weak-passwordreset-full-account-takeover.md
title: PII Leakage via IDOR + Weak PasswordReset = Full Account Takeover
category: documents
detected_topics:
- password-reset
- idor
- command-injection
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- password-reset
- idor
- command-injection
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: e4537bfa5ed4f6d79efe9ecd66cbb253bce4f42140a1c6a49d02d23a3d640777
text_sha256: 029d23e6dc9f11e59fa377cbf72725d8440e301beff66d82afe9766e4811ba0f
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# PII Leakage via IDOR + Weak PasswordReset = Full Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-25_pii-leakage-via-idor-weak-passwordreset-full-account-takeover.md
- Source Type: markdown
- Detected Topics: password-reset, idor, command-injection, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `e4537bfa5ed4f6d79efe9ecd66cbb253bce4f42140a1c6a49d02d23a3d640777`
- Text SHA256: `029d23e6dc9f11e59fa377cbf72725d8440e301beff66d82afe9766e4811ba0f`


## Content

---
title: "PII Leakage via IDOR + Weak PasswordReset = Full Account Takeover"
url: "https://medium.com/bugbountywriteup/pii-leakage-via-idor-weak-passwordreset-full-account-takeover-58d159f88d73"
authors: ["Pradeep Kumar (@Killer007p)"]
bugs: ["IDOR", "Information disclosure"]
publication_date: "2020-09-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4240
scraped_via: "browseros"
---

# PII Leakage via IDOR + Weak PasswordReset = Full Account Takeover

Pradeep Kumar
 highlighted

Pradeep Kumar
 highlighted

PII Leakage via IDOR + Weak PasswordReset = Full Account Takeover
Pradeep Kumar
Follow
2 min read
·
Sep 26, 2020

557

1

Hello Hunters, this is a quick write up on one of my recent findings on a bug bounty program. Before jumping into the vulnerability, let us get familiarized with few terms.

What is PII Leakage?

Personally identifiable information (PII) is any data that could potentially identify a specific individual, such as username,userID or any other personal information. PII Leakage is the exposure of such data.

What is Account Takeover Vulnerability?

It is a type of vulnerability that allows hackers to take full control of the user’s account by exploiting a flaw in the application’s logic.

Since the program does not allow disclosure, let’s consider the program as redacted.com. It started when i began to test the reset password functionality of the target. Just like any other website, the forgot password on https://redacted.com/forgotpassword also sent a email to the registered mail address for the password change. The reset password link was as below:

https://redacted.com/forgot_password/5f12cc7079f273.12051864/1597479504/NTg4NTg4a2lsbGVyQGdtYWlsLmNvbWFzZGZnaGprbDkxODI3Mzc0NjUwMDA=+++NTg4NTg4a2lsbGVy+++NTg4NTg4

The link did not expire even after changing the password.Weird Right!!. Requesting for reset password once again gave the following link:

https://redacted.com/forgot_password/8ac79ccf2a33.12057854/1597486704/NTg4NTg4a2lsbGVyQGdtYWlsLmNvbWFzZGZnaGprbDkxODI3Mzc0NjUwMDA=+++NTg4NTg4a2lsbGVy+++NTg4NTg4

The thing to observe is that the last part of the URL is same for both the link.

Press enter or click to view image in full size

After analyzing the above link:

1597486704 → Unix Time Stamp

The last part of the url was base64, decoding which gave the following:

588588killer@gmail.comasdfghjkl9182737465000+++588588killer+++588588

Here, 588588 is my User ID and killer@gmail.com is my email address. But wait, what was the gibberish look-alike thing [asdfghjkl9156837463000]?

Get Pradeep Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Nevermind, after playing with the link for some time, I found that only the last part of the URL I,e the userID was being validated by the server for the password reset.

https://redacted.com/forgot_password/5f12cc7079f273.12051864/1597479504/NTg4NTg4a2lsbGVyQGdtYWlsLmNvbWFzZGZnaGprbDkxODI3Mzc0NjUwMDA=+++NTg4NTg4a2lsbGVy+++[VALIDATED_PART]

So now, If i knew the userID any user, I could change his password with ease. Win? Nah!!

Now the goal was to find the spot where the UserID of the users were revealed or leaked. After a couple of days of recon I was able to find an IDOR on an endpoint in an javascript file .The endpoint only required the userID parameter, which leaked many sensitive pieces of information such as username, email address and even residence address that belonged to that userID.

IDOR Link:

https://redacted.com/razor/verify_email?rand=588588&request=wcq

Now all I had to do was enumerate to the email address for each user ID via brute force. [PS: UserID 1 belonged to the admin ;)]

IN BRIEF:

Enumerate the userID and EmailAddress from the endpoint → Reset the password → Login with the new password → Full Account Takeover

PS: The website stored personal information such as bank account number, PAN,Adhar card and other sensitive data which could be accessed after signing to the victim’s account.

Thank you for the read !!

Follow me on Twitter: Sickuritywizard
