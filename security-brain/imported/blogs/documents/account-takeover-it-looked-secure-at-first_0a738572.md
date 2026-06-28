---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-15_account-takeover-it-looked-secure-at-first.md
original_filename: 2024-02-15_account-takeover-it-looked-secure-at-first.md
title: Account Takeover [It Looked Secure at First]
category: documents
detected_topics:
- password-reset
- idor
- access-control
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- password-reset
- idor
- access-control
- command-injection
- otp
- rate-limit
language: en
raw_sha256: 0a7385726105d7a97495c195d8d67cea9cffa45ec51799ed85802301253e4d4d
text_sha256: 36714344ef5a406baad3aa2b670f020f4e07478f00492abeeaf8162fc5a193b6
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: true
---

# Account Takeover [It Looked Secure at First]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-15_account-takeover-it-looked-secure-at-first.md
- Source Type: markdown
- Detected Topics: password-reset, idor, access-control, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: True
- Raw SHA256: `0a7385726105d7a97495c195d8d67cea9cffa45ec51799ed85802301253e4d4d`
- Text SHA256: `36714344ef5a406baad3aa2b670f020f4e07478f00492abeeaf8162fc5a193b6`


## Content

---
title: "Account Takeover [It Looked Secure at First]"
url: "https://cristivlad.medium.com/account-takeover-it-looked-secure-at-first-f14a31cb7f5c"
authors: ["Cristi Vlad (@CristiVlad25)"]
bugs: ["IDOR", "Account takeover", "Privilege escalation", "Password reset"]
publication_date: "2024-02-15"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 431
scraped_via: "browseros"
---

# Account Takeover [It Looked Secure at First]

Top highlight

Account Takeover [It Looked Secure at First]
Cristi Vlad
Follow
3 min read
·
Feb 15, 2024

491

2

Press enter or click to view image in full size

In a recent pentest for a client, I was going through the password reset flow. You know:

1. Forgot password=***REDACTED*** Enter email => Receive email with link:

Click on this link to reset your password.The link expires in...

2. The reset link was something like this:/passreset/<token>

The token looks like some salted bcrypt, but it will really not matter in the end…

3. Clicking on the link takes you to the /passreset/<token> page, where you have 2 inputs: New Passwordand Confirm New Password.

Get Cristi Vlad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4. Filling in the 2 fields, sending and intercepting the request takes you into a whole different game:

Press enter or click to view image in full size

What is going on here?

There is an id parameter, which, as you may guess, holds value for the id of the user whose password is being reset.
This id is 10 characters long. Looking at other user IDs, it appears the format is alpha-numeric only. Thus, this is an easy job for bruteforcing, especially in the context of lacking rate limits.
Thus, to take over any account, just input a valid id .

Going further, this app was far from secure because a low-privileged user could enumerate all the users with their details (an admin feature). Thus, another way to collect IDs for account takeover.

And even more critical, a low-privileged user could elevate their privileges to admin. I went a step further and also found that the role updating operation could be performed unauthenticated (Yes, you heard that right!):

Press enter or click to view image in full size

You may wonder, how can there be apps like this working in 2024?

Well, it’s not an exception, but rather an encounter more frequent than you might think. And sadly, for this company, this was their production environment.

Their focus was to implement frontend limitations, potentially thinking that may be sufficient for keeping away privy eyes from peeking into unauthorized areas. I keep seeing this behavior frequently in pentests. Bad way to go about it.

When it comes to the password reset feature, their token thing has not been implemented all the way to the end. It has been lost somewhere in translation. The token should be time-sensitive and bound to the user. Moreover, the token must actually be used in the request responsible for the password reset, instead of the user ID.

With these (and other) issues uncovered, they’ll very likely start implementing a stronger security posture. Hopefully.
