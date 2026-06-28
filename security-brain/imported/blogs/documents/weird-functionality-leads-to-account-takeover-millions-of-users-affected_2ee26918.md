---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-27_weird-functionality-leads-to-account-takeover-millions-of-users-affected_2.md
original_filename: 2021-01-27_weird-functionality-leads-to-account-takeover-millions-of-users-affected_2.md
title: Weird functionality leads to Account Takeover (Millions of Users affected)
category: documents
detected_topics:
- command-injection
- automation-abuse
- mobile-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- mobile-security
language: en
raw_sha256: 2ee26918a5ff8d3bf87c5440435b8a7fa373b8673708a7c25b59a0ff0c99ed33
text_sha256: 6d01493e0a59f9430ebe6e0918135ff95da12c4e8306f4c51aabaa4d9b5fe089
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Weird functionality leads to Account Takeover (Millions of Users affected)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-27_weird-functionality-leads-to-account-takeover-millions-of-users-affected_2.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `2ee26918a5ff8d3bf87c5440435b8a7fa373b8673708a7c25b59a0ff0c99ed33`
- Text SHA256: `6d01493e0a59f9430ebe6e0918135ff95da12c4e8306f4c51aabaa4d9b5fe089`


## Content

---
title: "Weird functionality leads to Account Takeover (Millions of Users affected)"
url: "https://nullr3x.medium.com/weird-functionality-leads-to-account-takeover-millions-of-users-affected-3fdf06be45"
authors: ["Sahil Mehra (@nullr3x)"]
bugs: ["Account takeover", "Broken authentication"]
bounty: "4,000"
publication_date: "2021-01-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3961
scraped_via: "browseros"
---

# Weird functionality leads to Account Takeover (Millions of Users affected)

Weird functionality leads to Account Takeover (Millions of Users affected)
Sahil Mehra
Follow
3 min read
·
Jan 28, 2021

174

1

Hey Everyone,

Summary:

Recently, I discovered an Authentication Bypass that can lead to a complete Account Takeover. This write-up will explain how I figured & exploited that issue. So Let’s get started.

Scenario:
Phase 1 (Figured Vulnerability):
Android-App:

While testing on Android App, I created an account with <redacted>@gmail.com & after account creation, I logged into my account & a pricing page popped up in which all the features are described. So to get full feature access. I have to pay for it. (Account was too Expensive)

Web-App:

I follow the same steps for account creation on their web portal. But, after filling in all the details, I landed on a pricing page that’s weird for me. But in the android app, I was able to create an account without paying. But on the Web portal. I have to pay first to create an account.

Note:

Ah, The functionality is too weird for me. Because in the android app (I can create an account & then the pricing page pops up).

But in a web application, things are a little weird (the pricing page pops up after filling in all the details)

Phase 2 (Exploiting Vulnerability):

Let’s try to exploit this weird functionality. So, I try again to create an account on the web portal with the same email address that I used in the android app. But with the different details Like (First Name, Last Name & Password). Later, I noticed that the same details reflect in an android app.

Get Sahil Mehra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, these are few cases that I used to exploit this vulnerability:

Case 1: (web portal)

First, I tried to create an account on a web portal with the same email address that I used in an android app for account creation but with a different First Name & Last Name.

Result 1: (android app)

The following details that I used in the web portal are reflected in my android app. (An unauthorized actor can change the first name & last name).

Press enter or click to view image in full size
Changing First Name & Last Name

After that, I go for a password change or set up a new password.

Case 2: (web portal)

Then, I again create an account on the web portal with the same email address but with a different password.

Result 2: (android app)

I found logged out from my account & when I use the same password that I used in the web portal. So, that password worked & logged in to my account in the android app. (A proper Unauthorized actor can takeover any account).

Steps to Reproduce:
Open your android app & signup.
After account creation. (skip the price section)
Now, go to the web portal “https://www3.redacted.com/account".
Fill in the same email address but with different details (First Name, Last Name & Password).
Click on the Next button & after that pricing page popped up. (skip that section too)
Now, Go to Android App & Enter the victim’s email & use that password that you fill on the web portal during account creation.
You noticed that the Victim’s Account Compromised.
Timeline:
Press enter or click to view image in full size
Bounty

Oct 20, 2020 — Reported to a private program
Oct 20, 2020 — Report Triaged
Oct 22, 2020 — Vulnerability Fixed
Oct 28, 2020 — Bounty of $XXXX USD awarded

Special thanks to sechunt3r ( Bad Bro 🤑 )
