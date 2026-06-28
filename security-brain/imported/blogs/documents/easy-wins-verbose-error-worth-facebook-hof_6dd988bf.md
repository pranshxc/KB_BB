---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-05_easy-wins-verbose-error-worth-facebook-hof.md
original_filename: 2020-10-05_easy-wins-verbose-error-worth-facebook-hof.md
title: 'Easy wins : verbose error worth Facebook HOF'
category: documents
detected_topics:
- information-disclosure
- oauth
- command-injection
- api-security
tags:
- imported
- documents
- information-disclosure
- oauth
- command-injection
- api-security
language: en
raw_sha256: 6dd988bf4660e2e69633331ae8748f90a7c9b32a01b6f7903950da5ea820fadc
text_sha256: 3e87dc85b26a213e3e9bfec05861d3add36a78ea373f3f3c140ad56f14ac8811
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Easy wins : verbose error worth Facebook HOF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-05_easy-wins-verbose-error-worth-facebook-hof.md
- Source Type: markdown
- Detected Topics: information-disclosure, oauth, command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `6dd988bf4660e2e69633331ae8748f90a7c9b32a01b6f7903950da5ea820fadc`
- Text SHA256: `3e87dc85b26a213e3e9bfec05861d3add36a78ea373f3f3c140ad56f14ac8811`


## Content

---
title: "Easy wins : verbose error worth Facebook HOF"
url: "https://medium.com/@ironfisto/easy-wins-verbose-error-worth-facebook-hof-7d8a99dd920b"
authors: ["Mukul Lohar (@ironfisto)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2020-10-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4219
scraped_via: "browseros"
---

# Easy wins : verbose error worth Facebook HOF

Easy wins : verbose error worth Facebook HOF
Mukul Lohar
Follow
2 min read
·
Oct 5, 2020

59

Hi Info sec community

Been long time I am not active in bug bounty and security. Since beginning of my hacking interest, Facebook HOF always special to me. Here is story of how little recon and bit weird testing got me Facebook HOF 2020.

POC

I used waybackurls by tomnomnom to get all the urls of facebook.com domain.
I wanted URL with app_id parameter in url . So using grep i extracted them .

https://www.facebook.com/sharer?u=https%3A%2F%2Fgoogle.com

Above URL is Facebook common sharing endpoint for sharing anything like facebook profile , video and external urls.

Later one URL caught my attention from extracted url txt file.

Get Mukul Lohar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://www.facebook.com/dialog/feed?app_id={appi_id}&link={sharing url}&redirect_uri={sharing url}

Surprisingly above endpoint also share links. I decided to poke this URL .

3. Later, I decided to test feeling/activity feature. I selected watching option in activity and typed random thing & shared as Story.

Press enter or click to view image in full size
facebook sharing

4. Right after sharing this as story it was leaking file names with file paths.

Press enter or click to view image in full size
Verbose error with file paths

I was not sure about acceptance this bug . Still reported and accepted. Thanks to FB security. Made my way to Facebook hof.

Thanks for reading.

Byeee
