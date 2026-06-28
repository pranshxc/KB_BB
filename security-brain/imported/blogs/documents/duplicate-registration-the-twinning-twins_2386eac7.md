---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-08_duplicate-registration-the-twinning-twins.md
original_filename: 2021-02-08_duplicate-registration-the-twinning-twins.md
title: Duplicate Registration - The Twinning Twins
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- automation-abuse
- cloud-security
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- automation-abuse
- cloud-security
language: en
raw_sha256: 2386eac7131d4920710d9fa65287318ae24e5421881d7cc9cf8526b514aad114
text_sha256: 3175df66b47fdfa58a46464a697617b7b9c355180617a5c6fdc5ab7d57555c24
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Duplicate Registration - The Twinning Twins

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-08_duplicate-registration-the-twinning-twins.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `2386eac7131d4920710d9fa65287318ae24e5421881d7cc9cf8526b514aad114`
- Text SHA256: `3175df66b47fdfa58a46464a697617b7b9c355180617a5c6fdc5ab7d57555c24`


## Content

---
title: "Duplicate Registration - The Twinning Twins"
url: "https://shahjerry33.medium.com/duplicate-registration-the-twinning-twins-883dfee59eaf"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Account takeover", "Broken authentication"]
publication_date: "2021-02-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3928
scraped_via: "browseros"
---

# Duplicate Registration - The Twinning Twins

Top highlight

Duplicate Registration - The Twinning Twins
Jerry Shah (Jerry)
Follow
4 min read
·
Feb 8, 2021

458

3

I would like to share one of my unique finding about a bug called Duplicate Registration which led to Account Takeover. Using this bug it was possible to takeover any account with the same username.

Summary :

Duplicate registration is when an application allows us to register or sign up with the same email address, username or phone number. It can have critical consequences based on what kind of attack is performed.

I was looking for different bugs and just tried to register my self with the same email but it didn’t happen. So I tried to register myself with same username and it was successful. While logging in to the application they ask for username or email address, so as of now everything is fine. I then tried to exploit the password reset functionality where they asks you Which did you forget : Password or Username so after selecting password they will ask you to enter your username and then the link is sent to your email which means you can reset password of any account using only 1 email because the usernames are same and which also means you can takeover any of the account.

In this case when I changed the password it got changed for both the accounts because the usernames of both the accounts were same.

NOTE : In this web application all the profiles were public so it was easy to identify the usernames and emails of different users. For exploiting it on my end I created two trial accounts

Attack Scenario :

Phase 1 :

Let’s assume a victim register him/her self with the email (for eg. abc@gmail.com) and username as Bob, now as the profile is public an attacker can see his/her profile and he/she creates an account with same username Bob with different email address (for eg. xyz@gmail.com).

Phase 2 :

Now attacker uses password reset functionality where he/she was asked Which did you forget : Password or Username and attacker chose the option of Password, now the application will send the password reset link to attacker’s email (xyz@gmail.com) and he/she reset’s the password (which got changed for both the accounts because of the same username).

Phase 3 :

Now an attacker can login into both the accounts but using an email instead of username.

NOTE : An attacker needs to login using email because same usernames cannot have same password but different email addresses can have same password.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How I found this vulnerability ?

I created an account on browser A (Firefox) with the username UserTwo
Account 1

2. I created another account on browser B (Firefox Private) with same username UserTwo but with different email ID

Account 2

3. Now I logged in to first account on browser A (Firefox)

Press enter or click to view image in full size
Account 1 - Login
Press enter or click to view image in full size
Account 1

4. Then I logged into another account from browser B (Firefox Private)

Press enter or click to view image in full size
Account 2 - Login
Press enter or click to view image in full size
Account 2

5. I logged out and went to reset password page on browser A

Press enter or click to view image in full size
Password Reset
Password Reset Link Sent

After resetting the password I was able to access both the accounts using different emails with same password.

Why It Happened ?

To know why this happened I sent the password reset link on both of my test accounts and found that the token that was used for password reset was same for both the accounts because the usernames of both the account were same.

Account 1 - Password Reset Link
Account 2 - Password Reset Link

Here in the above screenshots you can see the the token and the username are same of both the accounts.

Impact :

Anyone can takeover the account of any user without his/her knowledge.

Mitigation :

An application should always check for duplicate entries of Usernames, Emails and Phone Numbers to avoid such kind of web application flaws.

Press enter or click to view image in full size
