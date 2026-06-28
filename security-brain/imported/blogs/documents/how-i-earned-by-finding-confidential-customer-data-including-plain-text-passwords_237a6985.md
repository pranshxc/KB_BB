---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-24_how-i-earned-by-finding-confidential-customer-data-including-plain-text-password.md
original_filename: 2019-10-24_how-i-earned-by-finding-confidential-customer-data-including-plain-text-password.md
title: How I earned $$$$ by finding confidential customer data including plain-text
  passwords!
category: documents
detected_topics:
- information-disclosure
- oauth
- command-injection
- path-traversal
- otp
tags:
- imported
- documents
- information-disclosure
- oauth
- command-injection
- path-traversal
- otp
language: en
raw_sha256: 237a6985a7d5b0e13e57e4fc50867e621556b975487350ee3b68e85b407a5356
text_sha256: 9454cf851a2539b0b805151c0d87d3a0fddd5009e4c467a87486aaad7cd60142
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I earned $$$$ by finding confidential customer data including plain-text passwords!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-24_how-i-earned-by-finding-confidential-customer-data-including-plain-text-password.md
- Source Type: markdown
- Detected Topics: information-disclosure, oauth, command-injection, path-traversal, otp
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `237a6985a7d5b0e13e57e4fc50867e621556b975487350ee3b68e85b407a5356`
- Text SHA256: `9454cf851a2539b0b805151c0d87d3a0fddd5009e4c467a87486aaad7cd60142`


## Content

---
title: "How I earned $$$$ by finding confidential customer data including plain-text passwords!"
url: "https://medium.com/@saurabh5392/how-i-earned-by-finding-confidential-customer-data-including-plain-text-passwords-f93c4ce2631"
authors: ["Sushant Soni (@sushantsoni5392)"]
bugs: ["Directory listing", "Information disclosure"]
publication_date: "2019-10-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4975
scraped_via: "browseros"
---

# How I earned $$$$ by finding confidential customer data including plain-text passwords!

How I earned $$$$ by finding confidential customer data including plain-text passwords!
Sushant Soni
Follow
2 min read
·
Oct 24, 2019

335

2

How directory indexing and file path traversal led to confidential customer data in plain sight!

Get Sushant Soni’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It
was like any other Friday night while I was learning more about Web Application security, I remembered that I had forgotten to make arrangements for an upcoming family meeting. It required me to avail the services of a very popular Indian startup. And that’s when it struck me “why not spend some of my time to look for some security loopholes on the site which I use regularly?”

Finding Sub-Domains
I started my recon with enumerating the subdomains. Here I used @tomnomnom’s AssetFinder, the output was then fed to an another great tool by @tomnomnom httprobe.
One domain in particular looked important to me, it is something like “https://api.xxxx.com”
Directory Searching
Second step I usually do is searching for directories/files. Here, I used Dirsearch with a custom wordlist from SecLists to discover content.
While traversing through all the results, I browsed “https://api.xxxx.com/application/logs”, to my surprise, the directory was accessible and indexing was enabled.
Source: https://docs.typo3.org/m/typo3/guide-security/8.7/en-us/GuidelinesAdministrators/DirectoryIndexing/Index.html

It was a log directory, some of the logs were old, dating back to 2018, so I tried to access the most recent log files, it was a php file “log-09–09–2019.php” and got an error “No direct script access allowed”. Moving on I noticed there was a gunzipped/compressed version of the same log file “log-09–09–2019.php.gz”.

The gunzip file was getting downloaded, I uncompressed it and opened the file in vim and “VOILA!!”. It opened me to a completely different world, it was a stash of gold/customer data for any hacker out there.
In the file I found customer’s email address, phone no., credit card numbers (some digits masked), PLAIN-TEXT passwords (no way). There were FB OAuth tokens, basically all of the data which can lead to a data breach.

The issue was reported and I received a 4 digit bounty in $
