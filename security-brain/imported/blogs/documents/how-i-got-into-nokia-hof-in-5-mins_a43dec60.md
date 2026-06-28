---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-22_how-i-got-into-nokia-hof-in-5-mins.md
original_filename: 2023-02-22_how-i-got-into-nokia-hof-in-5-mins.md
title: How I got into Nokia HOF in 5 Mins
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
raw_sha256: a43dec60b2aaa6718652ef58dc98c016152bbfcafa9ad45405691320b036faa6
text_sha256: f62b83bfaa486c3bc8f97483ded6852e6b56d281c308c5072ed2805ccc59929f
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# How I got into Nokia HOF in 5 Mins

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-22_how-i-got-into-nokia-hof-in-5-mins.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `a43dec60b2aaa6718652ef58dc98c016152bbfcafa9ad45405691320b036faa6`
- Text SHA256: `f62b83bfaa486c3bc8f97483ded6852e6b56d281c308c5072ed2805ccc59929f`


## Content

---
title: "How I got into Nokia HOF in 5 Mins"
url: "https://sl4x0.medium.com/how-i-got-into-nokia-hof-in-5-mins-99ce16583bd4"
authors: ["Abdelrhman Allam (@sl4x0)"]
programs: ["Nokia"]
bugs: ["Information disclosure"]
publication_date: "2023-02-22"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1489
scraped_via: "browseros"
---

# How I got into Nokia HOF in 5 Mins

How I got into Nokia HOF in 5 Mins
Abdelrhman Allam (sl4x0)
Follow
2 min read
·
Feb 22, 2023

308

3

Press enter or click to view image in full size
https://www.nokia.com/notices/responsible-disclosure/
بسم الله الرحمن الرحيم
[In the name of God, the most gracious, the most merciful]

In this write-up, I will share my journey of how I got into the Nokia Hall of Fame through GitHub dorkings. I hope that my experience will inspire others to pursue their passion for security research and report vulnerabilities responsibly.

Abstract

What is GitHub Dorking?

GitHub Dorking is a technique that involves using advanced search operators in GitHub to find sensitive information or vulnerabilities in public repositories.

Methodology

First of all, I don’t use any Automated Tools in this type of recon “Github Recon”
That’s why you can find a lot of treasures that some people just left it behind depending only on Automated Tools.

Get Abdelrhman Allam (sl4x0)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Ok, Let’s Pull the Stuff…

The first step is to Find Any of the Organization's Github Accounts

website.tld github

Press enter or click to view image in full size
The Second Step is to go deeper inside the ORG Account with Droks
Press enter or click to view image in full size

Actually, it’s frustrating to check all of these code snippets one by one...
One thing you can do is to check the most popular dorks that find treasures through these snippets.

This list helped me get some cool dorks: https://github.com/techgaun/github-dorks/blob/master/github-dorks.txt

From Developer Fails to Hunter Tales

After spending some minutes, fortunately, I found this file holding the Database username and password Publicly!

Reporting

I wrote a report to their Responsible Disclosure E-Mail and After 3 Hrs they Just Replied with this

Press enter or click to view image in full size

Don’t hesitate to reach out: https://twitter.com/sl4x0
