---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-28_how-i-takeover-wordpress-admin-fiiipaymy.md
original_filename: 2018-12-28_how-i-takeover-wordpress-admin-fiiipaymy.md
title: How I Takeover Wordpress Admin fiiipay.my
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: d190ae8cd30678806cda60ca4857c7f29fc8178e72fef174a124ce5edefc7256
text_sha256: e0cacca10be6b35b88b47a9a25c42677e14cf57106d491c2f53bae0074755bfd
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I Takeover Wordpress Admin fiiipay.my

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-28_how-i-takeover-wordpress-admin-fiiipaymy.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `d190ae8cd30678806cda60ca4857c7f29fc8178e72fef174a124ce5edefc7256`
- Text SHA256: `e0cacca10be6b35b88b47a9a25c42677e14cf57106d491c2f53bae0074755bfd`


## Content

---
title: "How I Takeover Wordpress Admin fiiipay.my"
url: "https://medium.com/@sahruldotid/how-i-takeover-wordpress-admin-fiiipay-my-1bdede83635d"
authors: ["Syahrul Akbar Rohmani (@sahruldotid)"]
programs: ["FiiiPay"]
bugs: ["Account takeover", "CMS default files"]
bounty: "408"
publication_date: "2018-12-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5500
scraped_via: "browseros"
---

# How I Takeover Wordpress Admin fiiipay.my

Syahrul Akbar R
Follow
2 min read
·
Dec 28, 2018

30

Press enter or click to view image in full size

How I Takeover Wordpress Admin fiiipay.my

Hello everyone, in this post im gonna show you how i takeover admin on cms wordpress and get bounty 😆.

First of all is RECON, so i goto https://fiiipay.my and check what cms they use and i see they are using wordpress .
Then i check admin page with adding “/wp-admin” after home url
i got redirected to “/setup-config.php”
Press enter or click to view image in full size
w00t ?

4. W00t?,, I click lets go and set new database configuration with remote my sql, https://www.freemysqlhosting.net/

Get Syahrul Akbar R’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

5. After that i got redirect to “/wp-admin/install.php” and i set new user & password wordpress

Press enter or click to view image in full size

6. Login to wordpress

Press enter or click to view image in full size

After this, i reported this vulnerability to AntiHack,

Nov 20, 2018 — Sent Report to AntiHack
Nov 20, 2018 — AntiHack change status to New
Dec 13, 2018 — AntiHack rewarded me $300 SGD
Dec 28, 2018 — Bounty received
