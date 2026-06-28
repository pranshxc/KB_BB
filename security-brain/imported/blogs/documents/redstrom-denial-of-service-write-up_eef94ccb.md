---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-12_redstrom-denial-of-service-write-up.md
original_filename: 2019-06-12_redstrom-denial-of-service-write-up.md
title: Redstrom Denial Of Service — Write Up
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: eef94ccbe1bad0bbda0226291916095c201f5ae6380017df73abc58580b7b5c6
text_sha256: b9f85f9242c50263b63026a2b7c24dc8ff22bda91337454578455cbddc0775b5
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Redstrom Denial Of Service — Write Up

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-12_redstrom-denial-of-service-write-up.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `eef94ccbe1bad0bbda0226291916095c201f5ae6380017df73abc58580b7b5c6`
- Text SHA256: `b9f85f9242c50263b63026a2b7c24dc8ff22bda91337454578455cbddc0775b5`


## Content

---
title: "Redstrom Denial Of Service — Write Up"
page_title: "Redstrom Denial Of Service — Write Up | by zer | Medium"
url: "https://medium.com/@androgaming1912/redstrom-denial-of-service-write-up-d8fd97f18335"
authors: ["Zerb0a"]
bugs: ["DoS"]
publication_date: "2019-06-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5221
scraped_via: "browseros"
---

# Redstrom Denial Of Service — Write Up

Redstrom Denial Of Service — Write Up
zer
Follow
2 min read
·
Jun 12, 2019

5

Press enter or click to view image in full size
-

Hi everyone, today im gonna write about my found 2 month ago ( resolved now ). This vulnerability found on Restrom.io ( Bug Bounty Platform ). Btw Restrom is a Indonesian Bug Bounty Platform.

I found this bug while searching for an xss on redstorm.io. im tried to input payload xss but not fired ;v. I got 503 Gateway Error after that.

Get zer’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reproduce :

I go to program > submit a report .
On the description i put :
[Click](javascript:confirm(‘1'))
Submit The Report
Now You can’t visit the submission page ( Because it’s displaying 503 Gateway Error )

Before i reported it im not sure about this one. But after i create a submission and wait for a week they said :
(Translated from indonesian Language)
“Hi Zerboa,
After we check the submission in question, there was an error during the submission (“Secon”) was sent yesterday that the submission could not be seen in us and this caused a timeout on the side of researcher.
After that we report it to the technical team and after fixing it is known that the problem is in the filtering of the XSS itself.
Now it’s been fixed by replacing it into a “-” character when it reads an error.

Therefore, we consider this submission P4 unless it can be further proven which will make the severity increase.
You also have the right to get a T-shirt and will be notified by email for details.”

Reward : (P4) Swag :D

Thx For Everyone who read my story, have a nice day :D
