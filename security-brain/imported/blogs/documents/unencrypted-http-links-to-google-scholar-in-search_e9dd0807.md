---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-13_unencrypted-http-links-to-google-scholar-in-search.md
original_filename: 2021-07-13_unencrypted-http-links-to-google-scholar-in-search.md
title: Unencrypted HTTP Links to Google Scholar in Search
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: e9dd080753a6b8356840e3f9a5420cb7b5818619a39755298ce1fba65e65c56e
text_sha256: 8e64490a6a9a687bd5e474645ec8455d478d03901e6b66381762f70942e5d84a
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Unencrypted HTTP Links to Google Scholar in Search

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-13_unencrypted-http-links-to-google-scholar-in-search.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `e9dd080753a6b8356840e3f9a5420cb7b5818619a39755298ce1fba65e65c56e`
- Text SHA256: `8e64490a6a9a687bd5e474645ec8455d478d03901e6b66381762f70942e5d84a`


## Content

---
title: "Unencrypted HTTP Links to Google Scholar in Search"
page_title: "[#0010] Unencrypted HTTP Links to Scholar results in Google Search allows MITM | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0010"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0010"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Google"]
bugs: ["MiTM"]
publication_date: "2021-07-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3510
---

#0010  
Vendor: Google  
Status: unfixed  
Reported: Mar 09, 2021  
Disclosed: Jul 13, 2021 (126 days) 

# Unencrypted HTTP Links to Scholar results in Google Search allows MITM

**Core Issue:**

On Google Search, the special `Scholar` search results starting with `Scholarly articles for` use unencrypted HTTP links, instead of HTTPS. Thus, when a user clicks on a `Scholar` results, an unencrypted HTTP request is made.

**Steps to Reproduce:**

  1. Go to `https://www.google.com`
  2. Search for `A Theory of Human Motivation`
  3. Under the `Ads` section, see the `Scholarly articles for` section
  4. See that the link to the Scholar search `Scholarly articles for A Theory of Human Motivation` and the direct links to the documents are HTTP links instead of HTTPS

**Extras:**

  * Weirdly enough, in the parameters of the Scholar direct links, a parameter `nossl=1` can be found. Was this intentional for some reason?
  * For the query `A Theory of Human Motivation` the seconds result is a `[BOOK]` result, pointing to Google Books. While from the Scholar search page, the link to Google Books is HTTPS, here, the direct link is also HTTP (`http://scholar.google.hu/scholar_url?url=http://www.google.com/books`). That should also be HTTPS.

**Impact:**

A passive eavesdropper who has access to the victim’s network traffic (targeted attack, ISP) could capture and read these unencrypted requests, and track what Scholar query the victim has searched for, and what documents she opened.

This leaks private information (queries, documents opened), which should never be visible to any passive eavesdropper.

Furthermore, an active MITM attacker might also spoof the unencrypted HTTP response from Google Scholar, and redirect the user to a fake/malicious page.
