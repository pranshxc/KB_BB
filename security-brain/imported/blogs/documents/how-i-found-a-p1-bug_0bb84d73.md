---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-05_how-i-found-a-p1-bug.md
original_filename: 2022-10-05_how-i-found-a-p1-bug.md
title: How I Found A P1 Bug
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 0bb84d732e42896d7d304cbe4690206af0be665cf271bede8276d69832e32785
text_sha256: 496b5cef19d3ad137bbf68cb6b27ddde04f6c85b3e5f01004fe9e97bb4ea7f8d
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found A P1 Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-05_how-i-found-a-p1-bug.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `0bb84d732e42896d7d304cbe4690206af0be665cf271bede8276d69832e32785`
- Text SHA256: `496b5cef19d3ad137bbf68cb6b27ddde04f6c85b3e5f01004fe9e97bb4ea7f8d`


## Content

---
title: "How I Found A P1 Bug"
url: "https://medium.com/@amithc38/how-i-found-a-p1-bug-a9873819a2d0"
authors: ["Amith"]
bugs: ["Authentication bypass", "Information disclosure"]
publication_date: "2022-10-05"
added_date: "2022-10-06"
source: "pentester.land/writeups.json"
original_index: 2085
scraped_via: "browseros"
---

# How I Found A P1 Bug

Top highlight

How I Found A P1 Bug
Amith
Follow
2 min read
·
Oct 5, 2022

216

6

Hi,

Myself Amith,

So let’s get started “How I Found A P1 Bug”

As usual after my office hour, I thought to hunt on a domain and started browsing through Bugcrowd and found a program. As per the policy, I can’t reveal the target domain name, so let’s say domain as “x.com”.

Information Gathering:

As usual I started gathering subdomains, used some google dorks to find subdomains. After gathering subdomains, I started looking for login portals of x.com.

Get Amith’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

site:*.x.com inurl:”*admin | login” | inurl:.php | .asp

Press enter or click to view image in full size

The above dork found a login page for one of the sub-domains of x.com, After a lot of manual checks and filtering each outputs, finally I found a sub-domain “y.x.com” which points to WHM Console. When I click on that link it directly gave me access to WHM Console Dashboard.

Press enter or click to view image in full size

I was surprised and when I checked the URL, the username and password itself is passed with the URL and it automatically logged me in to the console.

Press enter or click to view image in full size

So immediately reported the misconfiguration to them via their Bugcrowd bug bounty program.

After three days I got the response from Bugcrowd, unfortunately they said that it was a duplicate.

But, I’m happy that I could find this bug with less efforts.

“Google Dorking” will never let you down.

Thank you
