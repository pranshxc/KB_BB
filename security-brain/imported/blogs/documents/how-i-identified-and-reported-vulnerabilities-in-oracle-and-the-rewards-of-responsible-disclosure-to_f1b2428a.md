---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-18_how-i-identified-and-reported-vulnerabilities-in-oracle-and-the-rewards-of-respo.md
original_filename: 2023-01-18_how-i-identified-and-reported-vulnerabilities-in-oracle-and-the-rewards-of-respo.md
title: How I identified and reported vulnerabilities in Oracle and the rewards of
  responsible disclosure:From Backup Leak to Hall of Fame
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- information-disclosure
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- information-disclosure
language: en
raw_sha256: f1b2428a607549e1a712510de8dd5393d188321b09baec330f43d8245ccfeb31
text_sha256: 8d04fb56b85aa892f69a23f750b9807aaec4c2c6e5ca1fc8c8dbb6ed47c313ad
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# How I identified and reported vulnerabilities in Oracle and the rewards of responsible disclosure:From Backup Leak to Hall of Fame

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-18_how-i-identified-and-reported-vulnerabilities-in-oracle-and-the-rewards-of-respo.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `f1b2428a607549e1a712510de8dd5393d188321b09baec330f43d8245ccfeb31`
- Text SHA256: `8d04fb56b85aa892f69a23f750b9807aaec4c2c6e5ca1fc8c8dbb6ed47c313ad`


## Content

---
title: "How I identified and reported vulnerabilities in Oracle and the rewards of responsible disclosure:From Backup Leak to Hall of Fame"
url: "https://medium.com/@Parag_Bagul/how-i-identified-and-reported-vulnerabilities-in-oracle-and-the-rewards-of-responsible-43ee5fea457f"
authors: ["ParagBagul"]
programs: ["Oracle"]
bugs: ["Information disclosure"]
publication_date: "2023-01-18"
added_date: "2023-01-26"
source: "pentester.land/writeups.json"
original_index: 1656
scraped_via: "browseros"
---

# How I identified and reported vulnerabilities in Oracle and the rewards of responsible disclosure:From Backup Leak to Hall of Fame

How I identified and reported vulnerabilities in Oracle and the rewards of responsible disclosure:From Backup Leak to Hall of Fame
ParagBagul
Follow
2 min read
·
Jan 19, 2023

41

2

Hello folks . I’m a Parag Bagul security Researcher and bug bounty hunter.

This article is based on a 2022 finding in which I discovered the Backup file leak vulnerability on Oracle website which leads to sensitive information disclosure.

THE FINDING:

While i was exploring this website i found some subdomains

subdomain enumeration:

subfinder -d oracle.com -o domain.txt

2.Extracting Live Subdomains using HTTPX

cat domain.txt |httpx > active.txt

3.Uncovering Hidden Backup Files:

I found the domain ‘labs.oracle.com’ in the active domains list.

Sometimes, developers save backup files with the subdomain name included, such as ‘test.example.com/test.zip’.

Get ParagBagul’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Same scenario in my case After open labs.oracle.com/lab.zip in a browser I found that it was leaking sensitive information .sql files.

labs.oracle.com/lab.zip

So the final tip is Always check every combination Backup files like:

test.example.com/test.zip

test.example.com/example.zip

test.example.com/test.example.zip

Also check different file extension like zip,7z,tar,gz,bz2,xz

test.example.com/test.rar

test.example.com/test.7z

test.example.com/test.tar

test.example.com/test.gz

test.example.com/test.bz2

test.example.com/test.xz

Also check common format of Common names that developers use for a website source code backup in a ZIP file format you can also fuzz them.

sourcecode.zip

website_source.zip

website_backup.zip

website-source-code.zip

source.zip

backup.zip

code.zip

website-code.zip

website_code_backup.zip

source-code-backup.zip

website-files.zip

website-folder.zip

source-code.zip

code-backup.zip

website-code-backup.zip

website-src.zip

website-src-code.zip

website-src-backup.zip

src-code.zip

website-data-backup.zip

Also you can automate this kinds of things with burpsuite intruder,nuclei.

Report status:

Report date: 08-AUG-2022

Patch date: 09-AUG-2022

Added in Hall of fame : 18-OCT-2022

Press enter or click to view image in full size
Oracle Hall of fame.

Thank you,

Parag Bagul!!

HaxWizard
