---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-06_reflected-xss-primagamescom.md
original_filename: 2018-08-06_reflected-xss-primagamescom.md
title: Reflected XSS Primagames.com
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
raw_sha256: 03cdd23724cad4a3de99602688207943af351b2027293b097debd8cc4dba03b4
text_sha256: af90dc1e8bb04aad816dc7a6037e33d1d1578d7eb5bd20cfbc712cb77ec9a029
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS Primagames.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-06_reflected-xss-primagamescom.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `03cdd23724cad4a3de99602688207943af351b2027293b097debd8cc4dba03b4`
- Text SHA256: `af90dc1e8bb04aad816dc7a6037e33d1d1578d7eb5bd20cfbc712cb77ec9a029`


## Content

---
title: "Reflected XSS Primagames.com"
url: "https://medium.com/@friendly_/reflected-xss-primagames-com-c7a641912626"
authors: ["Friendly (@SkeletorKeys)"]
programs: ["Prima Games"]
bugs: ["Reflected XSS"]
publication_date: "2018-08-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5772
scraped_via: "browseros"
---

# Reflected XSS Primagames.com

Reflected XSS Primagames.com
Friendly
Follow
1 min read
·
Aug 6, 2018

77

Long story short, I’ve emailed them a few times, tweeted at them and no answer to fix their security.

I have decided to do a full disclosure regarding this.

You have a reflected XSS vulnerability located at this domain: https://shop.primagames.com/us/search?p=

This was tested on the latest version of Firefox 61.0.1 (64-bit).

Get Friendly’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

By entering this payload in the URL, you are able to execute a script (XSS):

<img/on=><img/onerror=%27confirm(1)%27src=%23>
Press enter or click to view image in full size
…. We get the famous confirm(1) to popup!
Impact:

This allows an attacker to inject custom Javascript codes that can be used to steal information from Primagames’s user base and lure them to malicious websites on the internet on behalf of Primagames’s website.

Once again, this post is NOT meant to do anything harmful to the website. I am just a security researcher who is trying to help secure your website — other websites as well.

I hope you see this post and fix your issue very soon and secure your users.

If you have any questions or comments, feel free to message me on Twitter @Skeletorkeys

Thanks for reading.
