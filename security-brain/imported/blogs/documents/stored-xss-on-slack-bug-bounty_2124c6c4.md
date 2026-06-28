---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-06_stored-xss-on-slack-bug-bounty.md
original_filename: 2020-08-06_stored-xss-on-slack-bug-bounty.md
title: Stored XSS on Slack, Bug Bounty
category: documents
detected_topics:
- xss
- command-injection
- file-upload
tags:
- imported
- documents
- xss
- command-injection
- file-upload
language: en
raw_sha256: 2124c6c4ab0cb2ecd64084655f785aee5b907e5d707113884d418a4463831eb7
text_sha256: 4d1c192cd0e4caab99e5757a5cc2898fa2173085822d9e740f04933456e58c40
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS on Slack, Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-06_stored-xss-on-slack-bug-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `2124c6c4ab0cb2ecd64084655f785aee5b907e5d707113884d418a4463831eb7`
- Text SHA256: `4d1c192cd0e4caab99e5757a5cc2898fa2173085822d9e740f04933456e58c40`


## Content

---
title: "Stored XSS on Slack, Bug Bounty"
url: "https://medium.com/@tommysuriel/stored-xss-on-slack-bug-bounty-88fe167d75df"
authors: ["Tommysuriel"]
programs: ["Slack"]
bugs: ["Stored XSS"]
bounty: "4,875"
publication_date: "2020-08-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4348
scraped_via: "browseros"
---

# Stored XSS on Slack, Bug Bounty

Stored XSS on Slack, Bug Bounty
Tommysuriel
Follow
2 min read
·
Aug 6, 2020

117

1

This was my first XSS related finding that was considered a high severity vulnerability on a bug bounty program. For finding this vulnerability I was paid a bounty of $4,875.

For general information about XSS vulnerabilities and their security impact I suggest you read the information in this link https://portswigger.net/web-security/cross-site-scripting.

Exploit:

The exploit of this vulnerability consists of uploading a PDF file with JavaScript code in it on the chat of Slack, if you clicked on it it opened on their PDF viewer and the JavaScript was executed. In this case I made it display my session cookies.

Get Tommysuriel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This was possible due to a vulnerability in an outdated version of PDF.js: CVE-2018–5158.

Discovery:

How did I discover that Slack had this vulnerability? Around the time I found this bug there had been a few disclosed reports of XSS in Hackerone related to PDF file uploads, so I was looking for bugs similar to those. I finally found this report https://hackerone.com/reports/819863 which is about the same vulnerability I found on Slack but this was on a company called Nextcloud. I simply used the same Payload provided on that report but changed the code in it to display cookies in an alert message and finally I tried it on Slack.

Takeaways:

Always keep yourself informed about vulnerabilities in JavaScript libraries /frameworks and think about what companies/bug bounty programs could be using those libraries. Always read the reports from Hackerone and any other write-ups from security researchers.
