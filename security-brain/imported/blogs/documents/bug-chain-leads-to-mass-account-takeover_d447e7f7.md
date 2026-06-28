---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-26_bug-chain-leads-to-mass-account-takeover.md
original_filename: 2021-07-26_bug-chain-leads-to-mass-account-takeover.md
title: Bug Chain leads to Mass Account Takeover!
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- automation-abuse
- information-disclosure
- business-logic
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- automation-abuse
- information-disclosure
- business-logic
language: en
raw_sha256: d447e7f751605bdab5bf930d27c73b44faba9b0d3de3b1ff80a37117ab44bb6d
text_sha256: abccd5f8c9a80bc594db9b0679207a95a46bad94367f3bc039fc7865a79addf1
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Chain leads to Mass Account Takeover!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-26_bug-chain-leads-to-mass-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, automation-abuse, information-disclosure, business-logic
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `d447e7f751605bdab5bf930d27c73b44faba9b0d3de3b1ff80a37117ab44bb6d`
- Text SHA256: `abccd5f8c9a80bc594db9b0679207a95a46bad94367f3bc039fc7865a79addf1`


## Content

---
title: "Bug Chain leads to Mass Account Takeover!"
url: "https://medium.com/@shubhayumajumdar/bug-chain-leads-to-mass-account-takeover-25dc76205f5d"
authors: ["Shubhayu Majumdar (@shubhayu64)"]
bugs: ["Information disclosure", "Password reset", "Account takeover"]
publication_date: "2021-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3479
scraped_via: "browseros"
---

# Bug Chain leads to Mass Account Takeover!

Top highlight

Bug Chain leads to Mass Account Takeover!
Mass account takeover via password reset functionality.
Shubhayu Majumdar
Follow
4 min read
·
Jul 27, 2021

291

1

Press enter or click to view image in full size

I have always thought of finding a P1 or P2 bug to write a medium article which would mean that I have really done some good research and have gotten better at bug hunting. Fortunately, I did some good research and got my hands on few bugs, which I chained, leading to mass account takeover.

I’m Shubhayu Majumdar, currently pursuing BTech in Computer Science and I hunt bugs as a hobby. I recently came across a set of bugs on a private program. To maintain privacy, I’ll refer to the website as redated.in.

What is an account takeover vulnerability?

This vulnerability allows the attacker to gain unauthorized and full access to the victim’s account by exploiting the authentication flaw in the application.

Get Shubhayu Majumdar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now let's have a look into the bugs individually.

Bugs found:
Default SQL data dump.
Account takeover via Password Reset functionality.
Re-registration using the same email.

To give an overview, I could easily take over a user’s account via a logic flaw present in the password reset functionality. In addition to that, the SQL dump exposed information of all users. Together, I get to take over the account of all users who have ever created an account on the website.

Default SQL data dump

While testing the website, I came across a few interesting end-points. Two of them sums up the data dump.

redated.in/backup. This updated the backup database from the main database. Which gave a response
Press enter or click to view image in full size
Response of visiting redated.in/backup

2. redated.in/backup.sql. Which dumped the backed up data

Press enter or click to view image in full size
Response of visiting redated.in/backup.sql

And this data dump had all the user’s login information like the usernames, passwords (MD5 hashed), email addresses/phone numbers depending on the mode user used to register the account. And it looks like

Press enter or click to view image in full size
User data leaked via the data dump

Here, my username, hashed password value and email have been dumped.

Account takeover via Password Reset functionality

When I tried to recover my account by resetting the password, I found the reset page takes the username and email to validate if the account exists. Upon validation, it directly gives an option to set a new password without sending any password reset link/OTPs.
Honestly, I didn’t expect such a website to have poor password reset logic.

Press enter or click to view image in full size
Password reset page of redated.in
Re-registration using the same email

I also found that it was possible to register a different username with an already used email. But this created a problem. For some reason, both the accounts now cannot reset their passwords. This is also a major vulnerability in itself.

Chaining the bugs

You must have already guessed it by now. We can easily find the user details from the SQL data dump and use it to take over the accounts of all users. After applying the new password, we create another account with a random username and the same email address as the victim account. This will ensure they cannot recover their accounts via password reset.

Every user who has created an account and every user who would have created their accounts in future are vulnerable to lose their accounts that too permanently.

They could have evaded the vulnerabilities by sending a password reset link or an OTP during password reset. And prevent the creation of multiple accounts with the same email address.

Special thanks to @tuhin1729

It was really fun hunting on this website and I’ll be publishing more articles and write-ups in the upcoming days.

Hope you enjoyed it :)

Cheers & Stay Safe !! :) ❤

Connect me at LinkedIn ._. Twitter ._. Buy me a coffee
