---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-20_tricky-2fa-bypass-leads-to-4-digit-bounty-.md
original_filename: 2023-09-20_tricky-2fa-bypass-leads-to-4-digit-bounty-.md
title: Tricky 2FA Bypass Leads to 4 digit Bounty $$$$
category: documents
detected_topics:
- mfa
- command-injection
- password-reset
- automation-abuse
tags:
- imported
- documents
- mfa
- command-injection
- password-reset
- automation-abuse
language: en
raw_sha256: b7e20e1e0f31b4a3948b9ea946eedf563d246d4e99511836d3b9fb4114cd09eb
text_sha256: 12d5c421f31f240104a16530815e742f43270f409c58b6b1a847a05dddc5b843
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Tricky 2FA Bypass Leads to 4 digit Bounty $$$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-20_tricky-2fa-bypass-leads-to-4-digit-bounty-.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, password-reset, automation-abuse
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `b7e20e1e0f31b4a3948b9ea946eedf563d246d4e99511836d3b9fb4114cd09eb`
- Text SHA256: `12d5c421f31f240104a16530815e742f43270f409c58b6b1a847a05dddc5b843`


## Content

---
title: "Tricky 2FA Bypass Leads to 4 digit Bounty $$$$"
url: "https://medium.com/@roohaa_n/tricky-2fa-bypass-leads-to-4-digit-bounty-3a148bc7d4a"
authors: ["Rohaangupta (@roohaa_n)"]
bugs: ["2FA / MFA bypass"]
bounty: "1,000"
publication_date: "2023-09-20"
added_date: "2023-09-22"
source: "pentester.land/writeups.json"
original_index: 758
scraped_via: "browseros"
---

# Tricky 2FA Bypass Leads to 4 digit Bounty $$$$

Rohaangupta
 highlighted

Tricky 2FA Bypass Leads to 4 digit Bounty $$$$
Rohaangupta
Follow
2 min read
·
Sep 20, 2023

619

17

Hii Everyone i am Rohan Gupta part time bug hunter and Full time as a Jr. Security analyst.

Now Lets know about 2FA !

2FA stands for “Two-Factor Authentication.” It is a security process that requires users to provide two different authentication factors before gaining access to a system, account, or application. The goal of 2FA is to enhance security by adding an additional layer of verification beyond just a username and password.

Why do we need 2FA ?

Enhanced Security: The primary purpose of 2FA is to provide an extra layer of security beyond just a username and password. Passwords can be easily compromised through various means like data breaches, phishing attacks, or social engineering. 2FA makes it significantly more challenging for unauthorized individuals to access your accounts because they would need both something you know (your password) and something you have or are (the second factor).
Protection Against Password Theft: Even if someone manages to steal your password, they won’t be able to access your account without the second factor. This adds a crucial barrier to prevent unauthorized access.
Mitigating Phishing Attacks: Phishing attacks involve tricking users into revealing their login credentials on fake websites that mimic legitimate ones. With 2FA, even if a user enters their password on a phishing site, the attacker won’t have the second factor, making it much harder to compromise the account.
Reducing the Impact of Data Breaches: Data breaches are common, and they can expose usernames and passwords. If you’re using 2FA, even if your credentials are exposed in a breach, the attacker still can’t access your account without the second factor.
Knowing that your accounts are protected by 2FA can give you peace of mind, reducing the risk of unauthorized access and potential harm to your digital identity.

While 2FA adds an extra step to the login process, the security benefits it provides far outweigh the inconvenience. It’s an effective and widely adopted security measure that helps safeguard your online presence in an increasingly digital and interconnected world.

Let’s directly Jump into Vulnerability without wasting time.

Get Rohaangupta’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Lets know how i was able to Bypass the 2FA successfully on a bugcrowd private program.

Steps to Reproduce :

Create an account on http://domain.com
Enable the 2FA via authenticator app
Now logout the account
Goto forgot password page
Reset password
Change the password and click on Save changes
It was observed that without 2FA attacker was able to login

This was the steps i was able to bypass the 2FA and rewarded $$$$.

Press enter or click to view image in full size

Thank you for reading.Hope you liked it.

You can follow me on twitter for more tips : https://x.com/roohaa_n
