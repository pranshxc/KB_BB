---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-11_how-i-unlocked-the-blocked-accounts.md
original_filename: 2020-04-11_how-i-unlocked-the-blocked-accounts.md
title: How i Unlocked the blocked accounts?
category: documents
detected_topics:
- password-reset
- rate-limit
- idor
- command-injection
- path-traversal
- otp
tags:
- imported
- documents
- password-reset
- rate-limit
- idor
- command-injection
- path-traversal
- otp
language: en
raw_sha256: 31738506f584d73bccbe34fc92a730a21197d23e0098130ca3f31c25048cc400
text_sha256: 2a018d99258d4e4240339662a0ca6fa52419cf49c6933e72fb27f53197134ae5
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How i Unlocked the blocked accounts?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-11_how-i-unlocked-the-blocked-accounts.md
- Source Type: markdown
- Detected Topics: password-reset, rate-limit, idor, command-injection, path-traversal, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `31738506f584d73bccbe34fc92a730a21197d23e0098130ca3f31c25048cc400`
- Text SHA256: `2a018d99258d4e4240339662a0ca6fa52419cf49c6933e72fb27f53197134ae5`


## Content

---
title: "How i Unlocked the blocked accounts?"
url: "https://medium.com/bugbountywriteup/how-i-unlocked-the-blocked-accounts-545e9b7d7be1"
authors: ["Maria Zulfiqar"]
bugs: ["Password reset", "HTTP parameter pollution", "IDOR"]
publication_date: "2020-04-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4658
scraped_via: "browseros"
---

# How i Unlocked the blocked accounts?

How i Unlocked the blocked accounts?
Maria Zulfiqar
Follow
3 min read
·
Apr 11, 2020

1.2K

3

welcome Everyone !!! . This is my first write up :) Hope you enjoy.

Background

Vulnerability was identified in a bug bounty program . Let’s keep the name confidential.

So I started to brute-force my own password for checking Brute Force Vulnerability. And i was blocked after 4–5 attempts. The company was charging a good amount to unlock your account.

Press enter or click to view image in full size
O !!!!!!!!!!!!!!!!!!!!!!!!!!!!

Now i really wanted my account back. So I started searching for any vulnerability that allowed me to get my account access back.

i started testing their password reset functionality. The password rest link was still sent even if you are blocked. But when i clicked the link, i received message on their web page like :-

“ Sorry your Account is Blocked due to security reasons”.

I thought to trick the system. So i copied the password reset token from the blocked account link and in password request for a valid account, i replaced the token with blocked account token in Burp Suite.

& WOW!!!

Password Reset was successful. And i got my account back. I reported the vulnerability and the bounty was paid.

Story doesn’t ends here.

Get Maria Zulfiqar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After few months i tested this vulnerability again. And above technique was rejected every time. Means its fixed!

what i did is :P With original request i Just added another parameter (e.g password_rest_token =blockedaccounttoken )into burp request like below.

Wowww!!! It was successful again. i Got my blocked account back. :) and a goood bounty :D

Press enter or click to view image in full size

Thanks for Reading :) Maria Zulfiqar !

Hope you liked it.

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
