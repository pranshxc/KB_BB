---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-04_reflective-xss-and-open-redirect-on-indeedcom-subdomain_2.md
original_filename: 2017-09-04_reflective-xss-and-open-redirect-on-indeedcom-subdomain_2.md
title: Reflective XSS and Open Redirect on Indeed.com subdomain
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
raw_sha256: 5fc39ed613b1514f202396a8b57ddf2774ea1a2fe066e44c66e77c918746d163
text_sha256: f76306a92f882ee2093d9fa2e8e8bcb73308bf39fd228ff700b3720f5b0a1765
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Reflective XSS and Open Redirect on Indeed.com subdomain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-04_reflective-xss-and-open-redirect-on-indeedcom-subdomain_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `5fc39ed613b1514f202396a8b57ddf2774ea1a2fe066e44c66e77c918746d163`
- Text SHA256: `f76306a92f882ee2093d9fa2e8e8bcb73308bf39fd228ff700b3720f5b0a1765`


## Content

---
title: "Reflective XSS and Open Redirect on Indeed.com subdomain"
url: "https://medium.com/@SyntaxError4/reflective-xss-and-open-redirect-on-indeed-com-subdomain-b4ab40e40c83"
authors: ["Syntax Error (@SYNTAXERRORBA)"]
programs: ["Indeed"]
bugs: ["Reflected XSS", "Open redirect"]
publication_date: "2017-09-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6108
scraped_via: "browseros"
---

# Reflective XSS and Open Redirect on Indeed.com subdomain

Reflective XSS and Open Redirect on Indeed.com subdomain
Syntax Error
Follow
2 min read
·
Sep 4, 2017

352

Hi Again! So here is one more writeup on a simple bug I found on Indeed.com subdomain.

As always I looked up for subdomains using Sublist3r tool.

While I was browsing through offfers.indeed.com subdomain ,I noticed a functionality where a user could choose some filters from dropdown and create a PDF report of the data which was generated.

I quickly selected some values and generated the report.When I Opened the Report ,I noticed that the URL had an extra parameter Target which had the file location for the PDF file.

http://offers.indeed.com/directcontent.html?target=http://offers.indeed.com/company/xy/xxyy.pdf

On seeing Target parameter in URL, my instant thought was to test for Open redirect .So I entered Target parameter value as https://www.google.com and I noticed it was actually taking user to Google.com

Get Syntax Error’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Vulnerable URL :http://offers.indeed.com/directcontent.html?target=http://www.google.com

Next was to check if the same parameter was vulnerable to XSS as well. I gave the Target parameter value as javascript:alert(1) and as I was suspecting alert box popped up.

Press enter or click to view image in full size

I reported this issue to Indeed Via Bugcrowd and the bug was resolved within a week.As part of fix, they completely removed this functionality from the site.

For any question,You can get in touch with me @syntaxerror

Untill next time
