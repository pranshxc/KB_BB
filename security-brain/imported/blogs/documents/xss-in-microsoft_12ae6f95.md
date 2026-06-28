---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-18_xss-in-microsoft.md
original_filename: 2018-05-18_xss-in-microsoft.md
title: Xss in Microsoft
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 12ae6f957ce1e9273003d6287d46f073613c320ff31bb7d2b7f5141ce1568cd7
text_sha256: f286ca290201d5dd0126c23bad11e00e8948f42c809e84ad01d492809ea358b6
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Xss in Microsoft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-18_xss-in-microsoft.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `12ae6f957ce1e9273003d6287d46f073613c320ff31bb7d2b7f5141ce1568cd7`
- Text SHA256: `f286ca290201d5dd0126c23bad11e00e8948f42c809e84ad01d492809ea358b6`


## Content

---
title: "Xss in Microsoft"
url: "https://medium.com/@hacker_eth/xss-in-microsoft-7a70416aee75"
authors: ["hacker_eth"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2018-05-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5880
scraped_via: "browseros"
---

# Xss in Microsoft

Xss in Microsoft
hacker_eth
Follow
1 min read
·
May 18, 2018

60

2

I have done the usual recon process and found a subdomain of microsoft (imagineacademy.microsoft.com) ,which faced XSS(cross side scripting) bug..

I had reported the same following responsible disclosure measures to microsoft ,in the month of march.

After few days,I received a confirmation mail from Microsoft stating that a –“ A ﬁx was conﬁrmed for the issue you presented. Microsoft would like to recognize your eﬀorts on our public security researcher acknowledgement page: “Security Researcher Acknowledgments for Microsoft Online Services”. “

This was my first bug report and achievement from Microsoft.

Get hacker_eth’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

They have provided me security acknowledgement in their website(hall of fame equivalent for microsoft) and also swag(for other vulnerabilty,which i cannot disclose now).

The payload was simple one :<svg/onload=alert(document.charset)>,in the search bar.

Press enter or click to view image in full size

This is my first article on my findings…..

I will continue to update my further finding,

To receive updates kindly follow me up.
