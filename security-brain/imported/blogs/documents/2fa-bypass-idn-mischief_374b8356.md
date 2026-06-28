---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-15_2fa-bypass-idn-mischief.md
original_filename: 2024-08-15_2fa-bypass-idn-mischief.md
title: 2FA Bypass - IDN Mischief
category: documents
detected_topics:
- mfa
- automation-abuse
- command-injection
tags:
- imported
- documents
- mfa
- automation-abuse
- command-injection
language: en
raw_sha256: 374b8356ea39b9ea912ff3e7c2e5939e324703be8f20090709e566d2220a1263
text_sha256: f4fa757d8553c1ab6b77a2ca3428c747e2e85c6a8a87b1d9968593d3e47b33b6
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: true
---

# 2FA Bypass - IDN Mischief

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-15_2fa-bypass-idn-mischief.md
- Source Type: markdown
- Detected Topics: mfa, automation-abuse, command-injection
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: True
- Raw SHA256: `374b8356ea39b9ea912ff3e7c2e5939e324703be8f20090709e566d2220a1263`
- Text SHA256: `f4fa757d8553c1ab6b77a2ca3428c747e2e85c6a8a87b1d9968593d3e47b33b6`


## Content

---
title: "2FA Bypass - IDN Mischief"
url: "https://shahjerry33.medium.com/2fa-bypass-idn-mischief-157f06cb6904"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["2FA / MFA bypass", "IDN homograph attack"]
publication_date: "2024-08-15"
added_date: "2024-08-22"
source: "pentester.land/writeups.json"
original_index: 70
scraped_via: "browseros"
---

# 2FA Bypass - IDN Mischief

2FA Bypass - IDN Mischief
Jerry Shah (Jerry)
Follow
5 min read
·
Aug 15, 2024

302

3

Press enter or click to view image in full size

Summary

Internationalized Domain Name (IDN) Homograph Attacks involve exploiting similarities between visually identical characters from different writing systems (e.g., Latin ‘a’ and Cyrillic ‘á’). In the context of Two-Factor Authentication (2FA), this vulnerability can occur when an application incorrectly normalizes or fails to distinguish between similar-looking characters in email addresses or usernames.

Description

I found a vulnerability where the website was using 2FA which can be bypassed using IDN homograph attack. I created two accounts on the website using normal and look-a-like emails (for e.g. emailOne@gmail.com and emailOne@gmáil.com) and setup second factor authentication on both the accounts. Then I logged into 1st account (emailOne@gmail.com) and used the 2FA code of a look-a-like email account (emailOne@gmáil.com) and I was logged in successfully. Then I also checked the reverse way where I logged in as look-a-like email (emailOne@gmáil.com) and used the 2FA code of the 1st email (emailOne@gmail.com) and I was logged into the account. So the attack was possible both the ways but as an attacker’s perspective I used look-a-like email to bypass the 2FA of the 1st email.

Anatomy of 2FA bypass with IDN

1. Account Creation

Two accounts are created with email addresses user1@gmail.com and user1@gmáil.com
The system stores both accounts as separate entities without normalization

2. 2FA Setup

Each account sets up 2FA and receives a unique secret key
The secret keys are stored against the respective normalized email addresses

3. Normalization Issue

During 2FA validation, the email addresses are normalized (e.g., converting user1@gmáil.com to user1@gmail.com)

4. 2FA Validation

The system retrieves the secret key for the normalized email, leading to the same secret key being used for both accounts
This allows the 2FA code generated for user1@gmáil.com to validate against the account of user1@gmail.com and vice versa

What is Normalization ?

Normalization in this context refers to the process of converting different forms of a string (such as email addresses) into a standardized or canonical format before processing. This is often done to ensure consistency in handling user inputs, especially when dealing with characters that will look similar but are technically different, such as those found in Internationalized Domain Names (IDN) or Unicode characters.

How Normalization Occurs in the Scenario

1. Input Email Address

The user registers or logs in using an email address such as user1@gmáil.com or user1@gmail.com

2. Normalization Process

During the 2FA setup or validation process, the system automatically normalize the email address
This could involve converting Unicode characters to their closest ASCII equivalents, such as converting á to a. For example, user1@gmáil.com can be normalized to user1@gmail.com

3. Result of Normalization

After normalization, user1@gmáil.com and user1@gmail.com can be treated as the same string: user1@gmail.com
This means that any process relying on this normalized string (such as generating or validating 2FA codes) would incorrectly treat these distinct email addresses as the same account

Prerequisites

An attacker should know the password of the victim for initial access.

How I found this vulnerability ?

I registered two accounts on the website with 2 emails, normal (emailOne@gmail.com) and look-a-like (emailOne@gmáil.com)
Press enter or click to view image in full size
Registration - Account 1 (Normal email)
Press enter or click to view image in full size
Registration - Account 2 (Look-a-like email)

2. I setup and enabled 2FA on both the accounts

Press enter or click to view image in full size
Enable 2FA - Account 1 (Normal email)
Press enter or click to view image in full size
Normal Email - 2FA
Press enter or click to view image in full size
Enable 2FA - Account 2 (Look-a-like email)
Press enter or click to view image in full size
Look-a-like Email - 2FA

3. Then from another browser I logged into to the normal account (emailOne@gmail.com)

Press enter or click to view image in full size
Login - Normal Account
Press enter or click to view image in full size
Login - Normal Account

4. Now from the authenticator app I used the 2FA code of the look-a-like email (emailOne@gmáil.com) and website allowed me to logged into the application

Press enter or click to view image in full size
2FA Code - Look-a-like email
Press enter or click to view image in full size
Logged in - 2FA Bypass

Why this happened ?

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In my opinion,

It happened primarily due to the improper handling of email addresses during the 2FA process, specifically the normalization of email addresses that involve characters from different writing systems, such as IDN homographs. The system incorrectly normalized the email addresses, treating distinct emails with similar characters (such as á and a) as identical which led to the same 2FA seed being used for both accounts, causing the 2FA codes to be interchangeable.

Press enter or click to view image in full size
Attack Flow

Impact

1. Shared 2FA Seed: If the system uses the normalized email to generate or retrieve the 2FA seed, both user1@gmail.com and user1@gmáil.com will share the same 2FA seed, leading to the same 2FA codes being generated.

2. Cross-Account Validation: When validating the 2FA code, the system will incorrectly validate a code meant for one account (e.g., user1@gmáil.com) as valid for another account (e.g., user1@gmail.com) due to the normalization process.

Calculated CVSS

Vector String - CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:L

Score - 4.8 Medium

Mitigation

It is recommended to implement the below fixes to mitigate this kind of issues

1. Avoid Email Normalization During Validation

Do not normalize the email address when validating the 2FA code. Use the email address as it is.

2. Use Unique Identifiers

Utilize unique user identifiers, such as a user ID, to retrieve the 2FA secret key, ensuring that the correct key is used for each user.

Improved Implementation Code

1. Account Creation

def create_account(email, password):
# Store account in the database without normalization
db.store_account(email, password)

2. 2FA Setup

def setup_2fa(user_id):
# Generate 2FA seed based on unique user ID
seed = generate_2fa_seed(user_id)

# Store 2FA seed in the database
db.store_2fa_seed(user_id, seed)

3. 2FA Code Validation

def validate_2fa_code(user_id, input_code):
# Retrieve the 2FA secret key using the unique user ID
secret_key=***REDACTED***

# Generate the expected 2FA code using the secret key
expected_code = generate_code(secret_key)

# Compare the expected code with the input code
return expected_code == input_code

Press enter or click to view image in full size
