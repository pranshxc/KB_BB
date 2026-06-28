---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-13_my-first-critical-on-hackerone-with-a-6400-bounty-sql-injection.md
original_filename: 2023-08-13_my-first-critical-on-hackerone-with-a-6400-bounty-sql-injection.md
title: My first Critical on hackerone with a $6,400 bounty — SQL Injection
category: documents
detected_topics:
- sqli
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- sqli
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 16dcc0d81ff24fe6a16ddb6e2f20ea011e87c1e09d34d5a2a486022b08557dbe
text_sha256: 429fdfe8020840da85ef86bdafd4fb7ce3a193dea4c1dd1b03439e3f005878bd
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# My first Critical on hackerone with a $6,400 bounty — SQL Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-13_my-first-critical-on-hackerone-with-a-6400-bounty-sql-injection.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `16dcc0d81ff24fe6a16ddb6e2f20ea011e87c1e09d34d5a2a486022b08557dbe`
- Text SHA256: `429fdfe8020840da85ef86bdafd4fb7ce3a193dea4c1dd1b03439e3f005878bd`


## Content

---
title: "My first Critical on hackerone with a $6,400 bounty — SQL Injection"
url: "https://aryasec.medium.com/my-first-critical-on-hackerone-with-a-6-400-bounty-sql-injection-913566a12c6b"
authors: ["Tengku Arya Saputra (@AryaaSec)"]
bugs: ["SQL injection"]
bounty: "6,400"
publication_date: "2023-08-13"
added_date: "2023-08-14"
source: "pentester.land/writeups.json"
original_index: 859
scraped_via: "browseros"
---

# My first Critical on hackerone with a $6,400 bounty — SQL Injection

My first Critical on hackerone with a $6,400 bounty — SQL Injection
Tengku Arya Saputra
Follow
3 min read
·
Aug 12, 2023

398

4

Press enter or click to view image in full size
Photo by pentest-tools

Hello everyone, introduce my name is Tengku Arya Saputra(Follow my Linkedin) on this occasion I will tell you how I found a security hole with a very critical vulnerability level on one of the bug bounty platforms HackerOne.

in the bug bounty program owned by a security company ****, I found it on the cloud subdomain, which is the most important domain on the company’s website, with which I was rewarded $6,400 by *****.

The first step I did was try to visit the link https://cloud.****/ after that because I did not have access to login I would register on the SignUp page.

The next step I registered by registering my email address [username]@wearehackerone.com

After successful registration I was directed to fill in the information as shown below

after completing the filling, I pressed the next button and saw the data recorded from burpsuite.

I am interested in the endpoint https://cloud.****/****/****/****/dnt?level=standard&region=gcp-us-central1 after that I tried to connect it with the repeater menu on brupsuite, in the picture below it can be seen when I send a request to the server it looks normal

Press enter or click to view image in full size

but the response changes when I give a single quote on the region paramater will display the server response which is 500 internal server error, can be seen in the image below

Here I use the SQLmap automated tool to make it easier to bypass the server information dmns back-end DBMS: ****.

Impact

An attacker can manipulate the SQL statements that are sent to the PostgreSQL database and inject malicious SQL statements. The attacker is able to change the logic of SQL statements executed against the database.

Get Tengku Arya Saputra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Timeline

Report — July 26, 2023

Change To Triaged — July 27, 2023

Respond Staff **** — 1 Agust, 2023

Retesting a bonus — 2 Agust, 2023

Reward Bounty — 8 Agust, 2023

Resolved — 8 Agust, 2023
