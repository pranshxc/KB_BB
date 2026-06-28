---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-18_my-first-bug-500.md
original_filename: 2019-11-18_my-first-bug-500.md
title: My First Bug ($500)
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 39065a0d3909b68708188faaec8fff90e6ae89836d17c869b5e875f24332108a
text_sha256: 48635f1310f3fff65ddbae663abf8477269c1fa13d8e51b9d13b95b875a6d9dc
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# My First Bug ($500)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-18_my-first-bug-500.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `39065a0d3909b68708188faaec8fff90e6ae89836d17c869b5e875f24332108a`
- Text SHA256: `48635f1310f3fff65ddbae663abf8477269c1fa13d8e51b9d13b95b875a6d9dc`


## Content

---
title: "My First Bug ($500)"
url: "https://medium.com/@abhishake100/my-first-bug-500-9222998e6249"
authors: ["Abhishek Yadav (@abhishake100)"]
bugs: ["No valid SPF records"]
bounty: "500"
publication_date: "2019-11-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4936
scraped_via: "browseros"
---

# My First Bug ($500)

My First Bug ($500)
Abhishek
Follow
3 min read
·
Nov 19, 2019

493

4

This is my first blog so ignore if i make any mistakes.

Press enter or click to view image in full size

Curated list of Bug Bounty programs — https://bugbountydirectory.com

After spending 2 to 3 months looking for bugs i couldn’t find anything. So i went on 
HackerOne
’s Hacktivity page where you can read disclosed reports of vulnerabilities reported by researchers.

HackerOne
Edit description

hackerone.com

As i was reading the reports i found this vulnerability that i didn’t know about.

Chainlink disclosed on HackerOne: No Valid SPF Records.
Hiii, There is any issue No valid SPF Records Desciprition : There is a email spoofing vulnerability.Email spoofing is…

hackerone.com

The vulnerability was that you can spoof their email address and then the attacker can send emails from their email address which could lead to sending fake emails or attempts of phishing.

To see if you can send an email of a target domain you need to check if it has an SPF (Sender Policy Framework) Record. Its basically a framework that checks which hosts are authorized to send mail for a domain.

Get Abhishek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To check this visit https://www.kitterman.com/spf/validate.html There are many websites to check this but i find this very simple. Just type the domain name and click on Get SPF Record (if any).

For eg: If you receive an email like support@example.com then type example.com

Press enter or click to view image in full size
Response

If you get No valid SPF record you probably can send an email using that domain. To send an email visit https://emkei.cz . A lot of websites are available to send emails i just find this easy to use and the emails are received fairly quick. Fill in all the details and hit send and if you receive an email from that domain its vulnerable.

I tried this on the websites that i used to hack and 3 of them didn’t have the SPF record and so i reported them and after a few days they replied.

Press enter or click to view image in full size
Press enter or click to view image in full size

The first one turned out duplicate which led me thinking that the other two would be duped as well cause how easy it was to find, but they turned out to be valid and i received a bounty for it. 😁

Hope you find this useful, i tried my best to explain. Please share so that others can learn from it.

Follow me on twitter — https://twitter.com/abhishekY495

Thank You.
