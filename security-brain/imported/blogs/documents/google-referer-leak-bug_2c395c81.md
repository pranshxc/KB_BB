---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-15_google-referer-leak-bug.md
original_filename: 2019-09-15_google-referer-leak-bug.md
title: Google Referer Leak Bug
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- csrf
- information-disclosure
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- csrf
- information-disclosure
language: en
raw_sha256: 2c395c81a26901f09b77ac85e42301e5454080c92042f65244a95f21d0cba053
text_sha256: 509064f9c7055c36fb60ca506c6229627ee34808af16ca95c15a5101c202ee89
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Google Referer Leak Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-15_google-referer-leak-bug.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, csrf, information-disclosure
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `2c395c81a26901f09b77ac85e42301e5454080c92042f65244a95f21d0cba053`
- Text SHA256: `509064f9c7055c36fb60ca506c6229627ee34808af16ca95c15a5101c202ee89`


## Content

---
title: "Google Referer Leak Bug"
page_title: "GOOGLE REFERER LEAK BUG. I followed the usual Recon process… | by Jayateertha Guruprasad | Medium"
url: "https://medium.com/@jayateerthag/google-referer-leak-bug-434f6293ce66"
authors: ["Jayateertha Guruprasad (@JayateerthaG)"]
programs: ["Google"]
bugs: ["Referer leakage", "Information disclosure"]
publication_date: "2019-09-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5025
scraped_via: "browseros"
---

# Google Referer Leak Bug

GOOGLE REFERER LEAK BUG
Jayateertha Guruprasad
Follow
1 min read
·
Sep 15, 2019

36

1

This is a low hanging bug ,I discovered in Google ,This blog is going to be to short and to the point.

I followed the usual Recon process after enumerating subdomains ,

I selected https://datastudio.google.com.I tried to check for popular vulnerabilities XSS,CSRF,SSRF and What not!!!

But couldn’t find anything .Then I tried to see the features in the website.There was an option to EMBED any site in a report .

Get Jayateertha Guruprasad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I embeded a site and watched the request through BURP suite,I couldn’t believe my eyes ,Private link of the document was passed as referer header to the EMBEDED link.

Press enter or click to view image in full size

The impact was that ,A user could EMBED a website which he doesn’t own ,But the website owner can get to know the user’s private link of the report by seeing his logs.

Reported the incident to Google VRP ,and recieved reward of $$$.

Moral:So look for low hanging bugs too ,They may sometimes be unnoticed.

Link to GOOGLE HOF:https://bughunter.withgoogle.com/profile/46aa4887-b189-4d69-bda2-8f2f5fc569be

Liked my article ? Follow me on twitter (@jayateerthaG) and medium for more content about bugbounty, Infosec, cybersecurity and hacking.
