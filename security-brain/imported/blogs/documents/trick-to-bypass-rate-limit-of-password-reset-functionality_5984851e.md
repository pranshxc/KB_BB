---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-12_trick-to-bypass-rate-limit-of-password-reset-functionality.md
original_filename: 2021-07-12_trick-to-bypass-rate-limit-of-password-reset-functionality.md
title: Trick to bypass rate limit of password reset functionality
category: documents
detected_topics:
- rate-limit
- command-injection
- password-reset
tags:
- imported
- documents
- rate-limit
- command-injection
- password-reset
language: en
raw_sha256: 5984851e1f8d14f30a136576dee97dd9648cfa7effb3b972353327dc25ea6481
text_sha256: 6e005d1810d432663f2235ae5ad0345a177fe81d70186225be46ad65f78fc1ad
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Trick to bypass rate limit of password reset functionality

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-12_trick-to-bypass-rate-limit-of-password-reset-functionality.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `5984851e1f8d14f30a136576dee97dd9648cfa7effb3b972353327dc25ea6481`
- Text SHA256: `6e005d1810d432663f2235ae5ad0345a177fe81d70186225be46ad65f78fc1ad`


## Content

---
title: "Trick to bypass rate limit of password reset functionality"
url: "https://4bdoz.medium.com/trick-to-bypass-rate-limit-of-password-reset-functionality-a9923d3d7c4b"
authors: ["Abdulrahman-Kamel"]
bugs: ["Rate limiting bypass"]
publication_date: "2021-07-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3514
scraped_via: "browseros"
---

# Trick to bypass rate limit of password reset functionality

Trick to bypass rate limit of password reset functionality
Abdulrahman-Kamel
Follow
2 min read
·
Jul 12, 2021

455

1

Note: Since its a private program, I will call it example.com

Server behavior
If you send many requests, the reset password will block you with response code => 429 and response message “Too many requests”.

Press enter or click to view image in full size

A
ttempts in testing

1- Change the user-agent header’s value randomly in every request. [Failed]
2- Adding some headers like below: [Failed]
X-Forwarded-For : 127.0.0.1
X-Forwarded-Host : 127.0.0.1
X-Client-IP : 127.0.0.1
X-Remote-IP : 127.0.0.1
X-Remote-Addr : 127.0.0.1
X-Host : 127.0.0.1
3- Trying to add a null byte in the email’s request body (%00, %09, %0d, %0a) [Faield]
4- A lot of fuzzing such as add space, numbers, role:admin, and others but [Faield]
5- Adding a parameter in the path [sucess] bypassed !!

Press enter or click to view image in full size
Press enter or click to view image in full size

https://dashboard.example.io/password-reset [block]
https://dashboard.example.io/password-reset?anyCharacter=1 [bypass]

Get Abdulrahman-Kamel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I can send more than 100 requests without taking a block.

R
eproduce the issue step by step

Go to this endpint https://dashboard.example.io/password-reset
Reset the password and capture the request with burp proxy
Add a parameter in the endpoint of the request and send to intruder or send many requests manually => https://dashboard.example.io/password-reset?anyCharacter=1

You will find out that you bypass the “Too many requests” prevention.

Thank you for reading
wait for the best.
