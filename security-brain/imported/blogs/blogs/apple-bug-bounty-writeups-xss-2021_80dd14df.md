---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-07_apple-bug-bounty-writeups-xss2021.md
original_filename: 2021-05-07_apple-bug-bounty-writeups-xss2021.md
title: Apple Bug bounty writeups XSS(2021)
category: blogs
detected_topics:
- idor
- xss
- command-injection
- rate-limit
tags:
- imported
- blogs
- idor
- xss
- command-injection
- rate-limit
language: en
raw_sha256: 80dd14df995e673031888d4058c10988fcb677a506cfc1bf96e1661a29c845a9
text_sha256: dd4a26445e72cf7c62db2cbb241714cdf4e232d2b7f48e6b81dbe2fcfbcda17c
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Apple Bug bounty writeups XSS(2021)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-07_apple-bug-bounty-writeups-xss2021.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `80dd14df995e673031888d4058c10988fcb677a506cfc1bf96e1661a29c845a9`
- Text SHA256: `dd4a26445e72cf7c62db2cbb241714cdf4e232d2b7f48e6b81dbe2fcfbcda17c`


## Content

---
title: "Apple Bug bounty writeups XSS(2021)"
url: "https://takashi-suzuki.medium.com/apple-bug-bounty-xss-2021-78c2f4fc4106"
authors: ["Takashi Suzuki"]
programs: ["Apple"]
bugs: ["XSS"]
publication_date: "2021-05-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3670
scraped_via: "browseros"
---

# Apple Bug bounty writeups XSS(2021)

Apple Bug bounty writeups XSS(2021)
Takashi Suzuki
Follow
1 min read
·
May 7, 2021

87

About me:
Takashi Suzuki - Security Researcher - フリーランス | LinkedIn
View Takashi Suzuki's profile on LinkedIn, the world's largest professional community. Takashi has 3 jobs listed on…

www.linkedin.com

https://hackerone.com/kamikaze?type=user

Enumeration:

Get apple’s reachable host from censys.io

Search query: 17.0.0.0/8 AND 443.https.get.status_code: 200

Screenshot:

Censys-CLI & Aquatone

Tool for scrape ip: https://github.com/censys/censys-python

Tool for screenshot: https://github.com/michenriksen/aquatone

Terminal command:
Scrape reachable host from censys CLI

censys search -q “17.0.0.0/8 AND 443.https.get.status_code:\”200\”” -query_type ipv4 — fields ip protocols -max-pages 15 -f json -o apple

2. Grep ip address

grep -o ‘[0–9]\{1,3\}\.[0–9]\{1,3\}\.[0–9]\{1,3\}\.[0–9]\{1,3\}’ apple >> ip-apple

Get Takashi Suzuki’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. Adds “https” for ip address in order to use for Aquatone

sed ‘s/^/https:\/\//’ ip-apple >> http-apple

4. Take screenshots

cat http-apple | ./aquatone -ports 443 -http-timeout 9000 -screenshot-timeout 90000 — out apple

I found a site which is vulnerable to XSS.

Site:

https://apple.channel.support

Step to reproduce:

1. Create a ticket

2. Upload SVG image with XSS payload in reply

3. When victim views attacker’s SVG image from mobile device, XSS triggers

POC
Timeline:

Reported: 02/16/2021

Fixed & Asked to how to be credited in Hall of Fame page : 31/03/2021
