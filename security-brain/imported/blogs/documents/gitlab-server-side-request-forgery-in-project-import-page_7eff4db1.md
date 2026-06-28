---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-13_gitlab-server-side-request-forgery-in-project-import-page.md
original_filename: 2021-02-13_gitlab-server-side-request-forgery-in-project-import-page.md
title: '[GITLAB] — Server Side Request Forgery in “Project Import” page.'
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: 7eff4db1004dd5ed1ef617fe81afcd6dcf68d247e9e28e232a5ac027df41652c
text_sha256: 8f47b50439c052b58007b231252ee6dc0fec77cc7f7dfb47719006f52243d66e
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# [GITLAB] — Server Side Request Forgery in “Project Import” page.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-13_gitlab-server-side-request-forgery-in-project-import-page.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `7eff4db1004dd5ed1ef617fe81afcd6dcf68d247e9e28e232a5ac027df41652c`
- Text SHA256: `8f47b50439c052b58007b231252ee6dc0fec77cc7f7dfb47719006f52243d66e`


## Content

---
title: "[GITLAB] — Server Side Request Forgery in “Project Import” page."
url: "https://ltsirkov.medium.com/gitlab-server-side-request-forgery-in-project-import-page-6fdb9ef423e4"
authors: ["Lyubomir Tsirkov (@lyubo_tsirkov)"]
programs: ["GitLab"]
bugs: ["SSRF"]
bounty: "1,500"
publication_date: "2021-02-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3912
scraped_via: "browseros"
---

# [GITLAB] — Server Side Request Forgery in “Project Import” page.

[GITLAB] — Server Side Request Forgery in “Project Import” page.
Lyubomir Tsirkov
Follow
2 min read
·
Feb 12, 2021

33

1

I decided to share a story about my first bug bounty earned in HackerOne. It’s about SSRF vulnerability that had been previously exploited by other h1 members.

The Gitlab team implemented several patches in order to remediate the issue. Unfortunately, it wasn’t enough, so I was able to bypass the latest applied fix.

Technical Analysis

Let’s go over the report created by “edoverflow” — https://hackerone.com/reports/215105.

As you can see the author successfully exploited SSRF vulnerability in “Project Import” page even though the patch had already been implemented.

“You have blocked the usage of http://127.0.0.1, http://localhost/, etc., but http://0177.1/ and http://0x7f.1/, for instance, can still be used to scan internal ports.“

Edoverflow

To resolve the aforementioned issue, the reporter suggested to:

“Block decimal, octal and hex localhost notation.“

At this moment, some thoughts came to my mind … What would happen if I used redirection?

Get Lyubomir Tsirkov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Anyway, I started to look for a way to bypass the latest patch applied by the team so at first, I hosted my “redirect.php” on my VPS server.
The URL was “HTTP://<IP>/redirect.php” and the file contained the following code:

<?php header(“Location: http://127.0.0.1:1339”); ?>

redirect.php

I would like to clarify that I executed “nc -lvvp 1339” on the GitLab server in order to open port “1339” and confirm that SSRF was possible.

I reproduced the same steps as the author did.

Create a new project.
Import Project — Repo by URL.
Fill in the URL field with my VPS url http://<IP>/redirect.php.
Click Create Project.

After creating the project, I successfully received a connection on the listener.

root@debian:/home/test# nc -lvvp 1339 
listening on [any] 1339 ...
connect to [127.0.0.1] from localhost [127.0.0.1] 39282 
GET / HTTP/1.1 Host: localhost:1339 
User-Agent: git/2.14.3 
Accept: */* 
Accept-Encoding: gzip 
Pragma: no-cach

It turned out that “Server-Side Request Forgery” was still possible with the redirection technique.

Impact

Any user with regular access to Gitlab can leverage it to access the internal network, perform port scanning etc … To remediate the issue it is highly recommended to disable the “Follow Redirection” property until any security patches are applied.

One year later, Gitlab board decided to reward me $1,500.

Press enter or click to view image in full size
