---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-17_my-first-blind-sql-injection.md
original_filename: 2022-03-17_my-first-blind-sql-injection.md
title: My First Blind SQL Injection
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: fef77683247927d75e12df37b1a567ce432f405d92cceffcaa1d6232c9e9b102
text_sha256: ac52565b96db8d76f360b3c15426263f8d411f3c3727651b02872d2658d6cb50
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# My First Blind SQL Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-17_my-first-blind-sql-injection.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `fef77683247927d75e12df37b1a567ce432f405d92cceffcaa1d6232c9e9b102`
- Text SHA256: `ac52565b96db8d76f360b3c15426263f8d411f3c3727651b02872d2658d6cb50`


## Content

---
title: "My First Blind SQL Injection"
url: "https://medium.com/@vamshivaran110/my-first-blind-sql-injection-7db4b5e5c66d"
authors: ["T VAMSHI"]
bugs: ["SQL injection"]
publication_date: "2022-03-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2808
scraped_via: "browseros"
---

# My First Blind SQL Injection

Top highlight

My First Blind SQL Injection
T VAMSHI
Follow
2 min read
·
Mar 17, 2022

201

4

Hello Hackers and security community..

I’m going to share my experience in finding the blind sql Injection.

I was hacking on a big scope target, I started by collecting the subdomains of the target from the different resources.

Tools: Subfinder, sublist3r, Amass

after collecting the subdomains i wanted to resolve them to get only domains that have web services running on them so i uses the Tomnomnom’s httprobe and collect subdomains having port 80 And 443.

I always check the subdomains manually, open every subdomain and see what’s in there. If the List is really big i use aquatone to get screenshots of the webpage of each subdomain. Aquatone also consists of various features to find services and ports running on the domains.

Get T VAMSHI’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was opening few subdomains, i randomly selected one subdomain started hunting on it, As always tried different attack techniques. I wanted to test for SQL injection, fired up burp suite and spider the host. Got the full website endpoints, Tried to inject SQL payloads in some of the endpoints no result.

Later i wanna try blind sql injection. so i’ve sent the all endpoint requests to burp repeater and maually inject payloads to test for time based SQL payloads. after checking few endpoints I came across a endpoint that is vulnerable to Time Based SQL inject.

Payload: 0'XOR(if(now()=sysdate(),sleep(20),0))XOR’Z (* is replaced with any seconds ).

Request:

Press enter or click to view image in full size

The payload is triggered and it is Delaying Response the exact time given in payload. I was so exited and created Report and submitted and It got accepted within few hours.

Key Takeaways: Try Different SQL payloads to trigger. also look for blind SQL Injections.

Thanks..
