---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-15_weak-cryptography-in-password-reset-to-full-account-takeover.md
original_filename: 2020-05-15_weak-cryptography-in-password-reset-to-full-account-takeover.md
title: Weak Cryptography in Password Reset to Full Account Takeover
category: documents
detected_topics:
- rate-limit
- password-reset
- idor
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- rate-limit
- password-reset
- idor
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 616b31f224b6ddbd2aa150d28241ba55ed0b49bc3c7b1dd025b658c087b6aac2
text_sha256: 9fa7f4ed2dfa5529d4f2997c78729be905aa8d46f235bcca5761b5dff1f35109
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Weak Cryptography in Password Reset to Full Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-15_weak-cryptography-in-password-reset-to-full-account-takeover.md
- Source Type: markdown
- Detected Topics: rate-limit, password-reset, idor, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `616b31f224b6ddbd2aa150d28241ba55ed0b49bc3c7b1dd025b658c087b6aac2`
- Text SHA256: `9fa7f4ed2dfa5529d4f2997c78729be905aa8d46f235bcca5761b5dff1f35109`


## Content

---
title: "Weak Cryptography in Password Reset to Full Account Takeover"
url: "https://medium.com/bugbountywriteup/weak-cryptography-in-password-reset-to-full-account-takeover-fc61c75b36b9"
authors: ["Harsh Bothra (@harshbothra_)"]
bugs: ["Account takeover", "Password reset", "Cryptographic issues"]
publication_date: "2020-05-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4589
scraped_via: "browseros"
---

# Weak Cryptography in Password Reset to Full Account Takeover

Top highlight

Weak Cryptography in Password Reset to Full Account Takeover
Harsh Bothra
Follow
3 min read
·
May 15, 2020

828

5

Press enter or click to view image in full size

Most of the applications provide the user’s with functionality to “Reset Password” via email. This functionality has always been a part of interest for most of the Bug Bounty Hunters or Security Researchers. From performing basic attacks such as Rate Limiting, Host Header Injections to performing account takeovers, this functionality is total fun and a big win to invest time in.

Hi Fellow Hackers & Hunters, In this article, I will describe one of my recent findings of Account Takeover via Analysing Cryptographic Patterns in Password Reset and eventually a P1 (critical) bug.

The application I was working on was a part of the Private Program. Let’s call it www.target.com for the demonstration purpose.

I switched back to this target after a few weeks and I forgot my credentials for the test accounts ( I usually do :P). I went ahead and did a Forget Password request for two of my test accounts.

The accounts were <bugcrowd_alias>+1@bugcrowdninja.com and <bugcrowd_alias>+2@bugcrowdninja.com.

For those who don’t what this “+” does the trick here. If you append a +sometext to your email, it actually creates an alias of your email and you will receive all the emails on your actual email. This helps a lot while testing because most of the application does not block and this finding was purely figured out because of this.

Example —

Actual Email: hbothra22@gmail.com

Alias: hbothra22+1@gmail.com OR hbothra22+harsh@gmail.com

All the emails of Aliases will be forwarded to Actual Email.

Now getting back to the application, the usual Password Reset flow includes:

Request New Pass. → Receive Unique Reset Link → Resets the Pass

Get Harsh Bothra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, While resetting the password using Reset Link, I observed the only difference between these two Reset Links was: 1 and 2.

Reset Link of Account 1: https://target.com/reset_password?token=zbp.nwavaqjbeptho%401+neugboufenu

Reset Link of Account 2: https://target.com/reset_password?token=zbp.nwavaqjbeptho%402+neugboufenu

The second thing I observed is the length of the reset token was = No. of characters in email and %40=@.

Cool. So this was sure that the application has a weak cryptographic mechanism in place but how the application is encoding the token was still left. After spending a few more minutes, I derived this formula on which the token was being generated.

Ceaser_Cipher_Key13(reverse(email)) == Password Reset Token

Take victim email, ex: hbothra22@gmail.com
Reverse the email, i.e.: moc.liamg@22arhtobh
Now encrypt reversed email with Ceaser Cipher, having Key=13, i.e.: zbp.yvnzt@22neugbou
At least change @ to %40 and we will have our reset token.

Final Example Token = zbp.yvnzt%4022neugbou

Now using this, we can reset the password for any user. The application was also allowing to enumeration valid emails on forget password and that makes our task easier.

Takeaways
While testing for the password, always use Two Aliases and try to see what bits are different in the reset token.
Check Reset token and try to see if any public encoding library/weak encryption is used.
