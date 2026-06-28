---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-16_attacking-postgresql-database_2.md
original_filename: 2018-07-16_attacking-postgresql-database_2.md
title: Attacking PostgreSQL Database
category: blogs
detected_topics:
- command-injection
- rate-limit
- supply-chain
tags:
- imported
- blogs
- command-injection
- rate-limit
- supply-chain
language: en
raw_sha256: 781b66358ad8cb2ecc9d43c7e7ca0a3496ea1adfe144dd0c61989e7536dbca92
text_sha256: 1ba69e897b25b90c991cb9ac0670e21a9758c893df3e575912953ae7ff712c55
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Attacking PostgreSQL Database

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-16_attacking-postgresql-database_2.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, supply-chain
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `781b66358ad8cb2ecc9d43c7e7ca0a3496ea1adfe144dd0c61989e7536dbca92`
- Text SHA256: `1ba69e897b25b90c991cb9ac0670e21a9758c893df3e575912953ae7ff712c55`


## Content

---
title: "Attacking PostgreSQL Database"
url: "https://medium.com/@vishnu0002/attacking-postgresql-database-834a9a3471bc"
authors: ["Vishnuraj"]
bugs: ["Bruteforce", "Weak credentials"]
publication_date: "2018-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5808
scraped_via: "browseros"
---

# Attacking PostgreSQL Database

Attacking PostgreSQL Database
vishnuraj
Follow
2 min read
·
Jul 16, 2018

391

2

This is write up in which I’ll explain a vulnerability I recently found, and reported through oracle bug bounty program.

Vulnerability Explanation:

PostgreSQL is a database that comes with MacOS X Lion, as a default standard database. According to wikipedia the majority of Linux distributions have the PostgreSQL in the supplied packages.So besides the regular databases (Oracle,MySQL etc.) there will be times as a penetration tester that we will need to assess and this database

Network Mapping :

Lets say that we have perform a port scan on a server and we have identify that is running a PostgreSQL database at port 5432

Press enter or click to view image in full size

Vulnerability Identification :

Get vishnuraj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

We will try a brute force attack in order to discover any weak credentials that will allow us then to connect to the database.We will open the metasploit framework and we will use the postgres_login scanner.

Press enter or click to view image in full size

Penetration

Now that we have a valid username and password we can use that to connect to the database by using a psql client.The first query that we want to execute is the select usename, passwd from pg_shadow; because it will return to us the password hashes of the database from the pg_shadow table.

Press enter or click to view image in full size
Press enter or click to view image in full size

Hope You liked this finding and i apologize for if there is any mistakes in this post. ☺

reference : https://medium.com/@cryptocracker99/a-penetration-testers-guide-to-postgresql-d78954921ee9
