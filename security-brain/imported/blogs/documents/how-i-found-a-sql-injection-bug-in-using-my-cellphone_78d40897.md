---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-23_how-i-found-a-sql-injection-bug-in-using-my-cellphone.md
original_filename: 2023-06-23_how-i-found-a-sql-injection-bug-in-using-my-cellphone.md
title: How I found a SQL Injection bug in using my cellphone.
category: documents
detected_topics:
- sqli
- command-injection
- password-reset
- otp
- api-security
tags:
- imported
- documents
- sqli
- command-injection
- password-reset
- otp
- api-security
language: en
raw_sha256: 78d40897add8c33fe5e9da7e9f2a1ced6bf2054d6e005fdbb030008cee24a8aa
text_sha256: 2581fd39c90b96ef8b9862a341d08fc8547b5fb96e834451946fd693fd841614
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: true
---

# How I found a SQL Injection bug in using my cellphone.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-23_how-i-found-a-sql-injection-bug-in-using-my-cellphone.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, password-reset, otp, api-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: True
- Raw SHA256: `78d40897add8c33fe5e9da7e9f2a1ced6bf2054d6e005fdbb030008cee24a8aa`
- Text SHA256: `2581fd39c90b96ef8b9862a341d08fc8547b5fb96e834451946fd693fd841614`


## Content

---
title: "How I found a SQL Injection bug in using my cellphone."
url: "https://medium.com/@0xnaeem/how-i-found-a-sql-injection-bug-in-using-my-cellphone-5b5193fdc314"
authors: ["Naeem Ahmed Sayed (@0xNaeem)"]
bugs: ["SQL injection"]
bounty: "500"
publication_date: "2023-06-23"
added_date: "2023-06-25"
source: "pentester.land/writeups.json"
original_index: 1016
scraped_via: "browseros"
---

# How I found a SQL Injection bug in using my cellphone.

How I found a SQL Injection bug in using my cellphone.
Naeem Ahmed Sayed (0xNaeem)
Follow
2 min read
·
Jun 22, 2023

269

6

Assalamu Alaikum
I am Naeem Ahmed Sayed (0xNaeem),
Part Time Bug Bounty Hunter from Bangladesh .
and welcome to my story about a critical bug I found on the phone.

Let’s Start, I choose Hackerone VDP Program And Most Interesting Thing this vdp Program give reward critical and high bug . So I started my recon and searching for login forms , reset password using Google Dorking And also Shodan Help me to find origin IP without WAF I used a simple dork.
Google Dork: site:*.target.com intext: forgotpassword

and then I found a subdomain that caught my attention. This Subdomain look like sub.target.com/path/forgotPassword.jsp and I started testing time based SQL injection but WAF can't give me future exploit, Then simply use Shodan dork to find origin IP and play without WAF .

Shodan Dork:
Ssl.cert.subject.cn:"sub.target.com" 200

I used the following payload on forgot password=***REDACTED***XOR(if(now()=sysdate(),sleep(10),0))XOR'Z

Get Naeem Ahmed Sayed (0xNaeem)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And open DevTools on kiwi browser to see server response after 10 seconds. I quickly capture the post request in Kiwi Browser for exploit in SQLMap.

Press enter or click to view image in full size

When I see the sqlmap result I'm surprised and I couldn’t believe I got my first SQL Injection bug on my phone 🤳 .

Press enter or click to view image in full size

Report: April / 03 / 2022
Trigger: April / 04 / 2022
Resolved: Jun / 19 / 2023 :)

If you like this story follow me for more stories like this.

Note: I’m not expert in English.
So forgive me if I am wrong..
Allah Hafiz

Thank you !!!
