---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-24_csv-injection-at-comment-section.md
original_filename: 2019-06-24_csv-injection-at-comment-section.md
title: CSV injection at Comment Section.
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: e262d6f858b20488a3124ea335aac23816b6cbf1cd57a17d31b260f1d9bfbc7c
text_sha256: 2811c61f91fe2598bc17696ff6de45cd786b6322693a028e677f3070a1eb5e15
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# CSV injection at Comment Section.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-24_csv-injection-at-comment-section.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `e262d6f858b20488a3124ea335aac23816b6cbf1cd57a17d31b260f1d9bfbc7c`
- Text SHA256: `2811c61f91fe2598bc17696ff6de45cd786b6322693a028e677f3070a1eb5e15`


## Content

---
title: "CSV injection at Comment Section."
url: "https://medium.com/@navne3t/csv-injection-at-comment-section-d5009ddd176"
authors: ["Navneet (@na5n33t)"]
bugs: ["CSV injection"]
publication_date: "2019-06-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5187
scraped_via: "browseros"
---

# CSV injection at Comment Section.

CSV injection at Comment Section.
Navneet
Follow
1 min read
·
Jun 24, 2019

40

This article is about a security bug/issue I found on a managed private program at H1(Hackerone).

Yes it was a CSV injection. If you don’t know what CSV injection or formula injection is ? Let me summarise it for you.

The excel software allow user to insert the formulas in excel sheet but sometime if web application(if web app have any functionality which generates CSV file) let anyone to insert the untrusted data into this CSV file, anyone can inject the malicious formulas which can run when user open that CSV file in excel software.

For more info on CSV injection visit below links

https://www.owasp.org/index.php/CSV_Injection

https://payatu.com/csv-injection-basic-to-exploit/

Affected Functionality:-

The user can download all the comments(data) on his/her articles as a CSV file.

Get Navneet’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now anyone can inject the formula (payload) as a comment on the article.

e.g. the payload I used in report.

=HYPERLINK (’www.BadSite.com’)

Now when user download the data(comments) as a CSV file and open the file. The payload will be triggered and a web browser will be open with above website.

Reward/Bounty:-

The bug/issue is fixed now and the program does not offers bounty. All i got +7 repo points.

The feedback/comments are welcomed.
