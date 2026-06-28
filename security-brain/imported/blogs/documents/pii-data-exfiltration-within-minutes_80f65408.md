---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-12_pii-data-exfiltration-within-minutes.md
original_filename: 2022-12-12_pii-data-exfiltration-within-minutes.md
title: PII data exfiltration within minutes
category: documents
detected_topics:
- jwt
- access-control
- command-injection
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- jwt
- access-control
- command-injection
- otp
- information-disclosure
- api-security
language: en
raw_sha256: 80f65408e9daa126c8b2524f946c5180bc5a20d46f2893033400123f31a10a05
text_sha256: d2c1ce635d0166746483d52b7accc8df95c1d800c57fbf1fee1d08947c5519e6
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# PII data exfiltration within minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-12_pii-data-exfiltration-within-minutes.md
- Source Type: markdown
- Detected Topics: jwt, access-control, command-injection, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `80f65408e9daa126c8b2524f946c5180bc5a20d46f2893033400123f31a10a05`
- Text SHA256: `d2c1ce635d0166746483d52b7accc8df95c1d800c57fbf1fee1d08947c5519e6`


## Content

---
title: "PII data exfiltration within minutes"
url: "https://0xmayankgarg.medium.com/pii-data-exfiltration-within-minutes-f06d4587d201"
authors: ["Mayank Garg"]
bugs: ["Information disclosure"]
publication_date: "2022-12-12"
added_date: "2022-12-15"
source: "pentester.land/writeups.json"
original_index: 1788
scraped_via: "browseros"
---

# PII data exfiltration within minutes

PII data exfiltration within minutes
Mayank Garg
Follow
4 min read
·
Dec 13, 2022

110

Hello Everyone,

Here I am with a story about one of my findings: I was able to exfiltrate complete PII data, not just of their customers but also of their employees’.

So, the company is about crypto exchange and is a popular company in the US. As the bug is not fixed yet let us make an alias for the domain name and call it crypto.com.

On the first day of hacking on this I started with reconnaissance, obviously. Got the subdomains, fuzzed for different endpoints, port scanning, and other stuff. The most exciting thing was their main application only. So I started on that main application which is a crypto exchange platform. I found a couple of low-hanging bugs but I wanted to find a bug with high severity.

I again started the next day, and the first thing I did was GitHub recon.

Do you know what GitHub recon is?
If you don’t, I’ll tell you in simple words. It is simply doing reconnaissance on GitHub.
Still not clear? So, the companies develop a product, and what goes into developing a product? Programming codes. And that is developed by a team of software developers. GitHub provides a platform where software developers can come and develop something together, share codes, and collaborate.

Press enter or click to view image in full size

How can you use GitHub to find something useful?
So, during developing a product and programming and collaborating on GitHub the developers often share something confidential which can be a password to a live login page or even to an SSH server, tokens, API keys, and other sensitive information.
You can make queries and search on GitHub to fetch sensitive information. Examples:
crypto.com token
crypto.com password
crypto.com “Authorization: Bearer”
et cetera

Get Mayank Garg’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

What did I do?
I formed a query as “crypto.com token” and I found a repository with a JWT in a code. That JWT had admin privileges.

Press enter or click to view image in full size

But how did I know that the token had admin privileges? You can use https://jwt.io/ to get more information about the structure of the JWT. For example, you can get the signing algorithm used, the body of the JWT (actual data of JWT), etc. There was a key-pair in the body of the JWT as “authority”: “ADMIN”. I will surely write a blog explaining JWT in detail and some common attacks you can make use of if you find any JWT during your penetration test or bug hunt.

Press enter or click to view image in full size

NOTE: You should verify every sensitive information found as they can be dummy tokens/passwords or there are chances that they had already been nullified by the company.

Then I started looking for endpoints that were meant for admin users and needed some kind of Authorization. I found 3 such endpoints.
The next thing was to send the JWT to these endpoints, and I did this by adding a header in the HTTP Request: Authorization: Bearer <JWT_Token>
To my surprise, the JWT Token was valid and I got a response with massive data.
You can also make a request with cURL: curl -X GET ‘https://api.crypto.com/transaction/admin/orders/list' -H “Authorization: Bearer <JWT_Token>”

What kind of information was fetched?
First endpoint: It contained PII data of the employees like their email addresses and phone numbers.
Second endpoint: It contained PII data of customers like their email addresses and phone numbers, whether their KYC is done, etc.
Third endpoint: It contained the transaction details like what cryptocurrency they bought, at what rate, transaction ID, etc. This data was massive, and it was refreshed after some time as the transactions used to take place at an extremely high rate.

It took me around 15–20 minutes on the second day to exfiltrate this much of data.

What did I get as a reward?
After 3–4 days of reporting, I got a reply that the company has closed their bug bounty program, hence, they won’t be able to pay me. That was disheartening, and also, that is not fair.
But they offered me a job role as a Security Engineer. I was delighted about that, but I had an internship at Deloitte USI lined up for the very next month. So, I declined that offer and went for an internship at Deloitte.
I’ll write a blog on that as well sharing my experience working at Deloitte and also how I got an internship at Deloitte.

Till then, take care ✌️, and keep hustling 💪
