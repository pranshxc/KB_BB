---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-30_blind-sql-injection-on-delete-request.md
original_filename: 2022-10-30_blind-sql-injection-on-delete-request.md
title: Blind SQL Injection on Delete Request
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
raw_sha256: 003936ee16a8130542e986af19de5033d477a0394926a708638991735bf3ea57
text_sha256: f077793219f03963052837ade5539882d8e642fd14cbe3217b4f2adf8511849f
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Blind SQL Injection on Delete Request

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-30_blind-sql-injection-on-delete-request.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `003936ee16a8130542e986af19de5033d477a0394926a708638991735bf3ea57`
- Text SHA256: `f077793219f03963052837ade5539882d8e642fd14cbe3217b4f2adf8511849f`


## Content

---
title: "Blind SQL Injection on Delete Request"
url: "https://medium.com/@jawadmahdi/blind-sql-injection-on-delete-request-486770af75a6"
authors: ["Jawad Mahdi (@hunter0x1)"]
bugs: ["Blind SQL injection"]
bounty: "1,300"
publication_date: "2022-10-30"
added_date: "2022-11-01"
source: "pentester.land/writeups.json"
original_index: 1966
scraped_via: "browseros"
---

# Blind SQL Injection on Delete Request

Blind SQL Injection on Delete Request
Jawad Mahdi
Follow
2 min read
·
Oct 31, 2022

76

1

Hi everyone, I am an Independent Cyber Security Researcher and a Red Team Member of SYNACK from Bangladesh.

I recently got invited to a private program, and it had allowed to be hunted on all the assets that belongs to them. I asked my friend 
Ansar Uddin
 to collaborate with me, and we immediately started hunting on the assets we’ve found through recon.

We’ve come across a domain where we started testing on all input fields. Since it allowed us to create free user accounts, and after that, we’ve started checking inside functionalities. We’ve noticed that when we created a file and while deleting it, we’ve used a SQLI blind payload, and it slept for 5 seconds since the sleep(5). We used it again and it did not work. It is because the file we’ve created has been deleted.

We created another file, and performed the same process, and it successfully slept again, and finally, we had to create another file and while deleting it, we captured the request, and used SQLMAP, and it had found all the available databases.

Payload used: ‘ AND (SELECT 8839 FROM (SELECT(SLEEP(5)))uzIY) AND ‘mSUA’=’mSUA

Get Jawad Mahdi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The vulnerable delete request looked liked this:

Press enter or click to view image in full size

After using SQLI blind payload:

Press enter or click to view image in full size

Rewarded $1300

Press enter or click to view image in full size

Important Tip: Do not fuzz on delete request, rather, check each parameters manually.
