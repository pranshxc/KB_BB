---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-03_600-for-idor-file-or-folder-download.md
original_filename: 2021-10-03_600-for-idor-file-or-folder-download.md
title: $600 for IDOR (File or Folder Download)
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: 3d7a5e31654685780f5d3bf1624d909160ab543c482d5336ad40bab34865ed2a
text_sha256: 1172a7da189846c82791ba7701c59874554c2d04819b90e874a658df1573bac7
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# $600 for IDOR (File or Folder Download)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-03_600-for-idor-file-or-folder-download.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `3d7a5e31654685780f5d3bf1624d909160ab543c482d5336ad40bab34865ed2a`
- Text SHA256: `1172a7da189846c82791ba7701c59874554c2d04819b90e874a658df1573bac7`


## Content

---
title: "$600 for IDOR (File or Folder Download)"
url: "https://encodedguy.medium.com/600-for-idor-file-or-folder-download-243166452dad"
authors: ["Inderjeet Singh - encodedguy (@3nc0d3dGuY)"]
bugs: ["IDOR"]
bounty: "600"
publication_date: "2021-10-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3265
scraped_via: "browseros"
---

# $600 for IDOR (File or Folder Download)

$600 for IDOR (File or Folder Download)
Inderjeet Singh - rashahacks
Follow
3 min read
·
Oct 3, 2021

230

4

0xHello Hackers

I hope you all are doing too well in your journey to be better. I would like to share one of my findings today via Medium.

0x1/0 About Scenario

1/0 — Bit. Due to disclosure issues, let’s call the host as example.com. After navigating through the site, there are few public documents and folders present on the home page. Those folders and files are downloadable.

Press enter or click to view image in full size
0xExploitation

I fetched the download request in Burpsuite Intercept. The folder request was a GET Request with one parameter as folderId=xxxxxx (6 digit number).

Press enter or click to view image in full size

I thought why not try folderId=106564. I got 200 in response, but unfortunately that was the public file already on the home page.

Then , I fetched folderId’s for all the public folders and realized that there are 7 folderId’s that are public. This I did by downloading other folders, intercepting them and noting down the folderId’s.

Get Inderjeet Singh - rashahacks’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I thought, why not bruteforce the folderId parameter values to enumerate maybe more id’s which are not public.

Press enter or click to view image in full size

I did brute forcing on the folderId using Burpsuite Intruder from value 106000 to 107000. And I got twenty 200 HTTP status codes.

Tried to change the id’s to private id’s that I got by brute forcing and got some private documents of company. Some folders were even gigabytes in size ($$Data$$). All these private folders were sensitive.

Press enter or click to view image in full size
0xConclusion

I did this for folderId parameter. fileId was also one of the parameter but it have 16 characters long value. I don’t know why they haven’t done the same for folderId’s.

This issue was present on 20+ hosts of this infrastructure. I made report for 2 hosts and said to the Security Team that it is also available on these hosts as well. They paid me for 2 hosts. Highest amount from this program is $500 for RCE bug and they paid $300 for each report.

Received $600 after almost a month for two reports (same issue different host).

What I Learnt

Go for manual exploitation, check functionalities in the site and exploit the functionalities. If you have found some values in parameters, change them. If they are encoded, decode them (if possible). Exploit functionalities.
