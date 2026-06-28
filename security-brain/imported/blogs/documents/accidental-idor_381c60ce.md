---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-01_accidental-idor_2.md
original_filename: 2019-07-01_accidental-idor_2.md
title: Accidental IDOR
category: documents
detected_topics:
- idor
- command-injection
- csrf
tags:
- imported
- documents
- idor
- command-injection
- csrf
language: en
raw_sha256: 381c60cedb539f45168ddf33466669547e583274f061cc5f82f8ddee3eb8236f
text_sha256: cdf451e98db8d0adfb2436d7072a3fc234250c69d3ca9873eb49c1f2dffdc749
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Accidental IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-01_accidental-idor_2.md
- Source Type: markdown
- Detected Topics: idor, command-injection, csrf
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `381c60cedb539f45168ddf33466669547e583274f061cc5f82f8ddee3eb8236f`
- Text SHA256: `cdf451e98db8d0adfb2436d7072a3fc234250c69d3ca9873eb49c1f2dffdc749`


## Content

---
title: "Accidental IDOR"
url: "https://medium.com/@saadahmedx/accidental-idor-8987a2728d4"
authors: ["Saad Ahmed (@XSaadAhmedX)"]
bugs: ["IDOR"]
publication_date: "2019-07-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5174
scraped_via: "browseros"
---

# Accidental IDOR

Accidental IDOR
Saad Ahmed
Follow
2 min read
·
Jul 1, 2019

452

Hi guys I hope you all are doing good so this write-up is all about the accidental IDOR that I found in the PRIVATE program, so let’s assume the name redacted.com. I was checking the CSRF vulnerability in the update address functionality, the API was sending the JSON DATA to the server & there was no CSRF protection when i tried to change the content type to text/plain I got this.

Press enter or click to view image in full size

An error disclosed another hidden endpoint, when i made an OPTIONS request to that hidden endpoint & checked the allow methods i got this.

Press enter or click to view image in full size

After trying all methods one by one the GET method did something magical

Press enter or click to view image in full size

If you notice in the hidden end-point there is an email which is my own account email & then i created another account & replaced the email in the end-point.

Press enter or click to view image in full size

I was able to see my second account information & after further testing if I send the PUT request i was able to update the address of my 2nd account & similarly if I send a DELETE request I was able to delete the address on my 2nd account.

Get Saad Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

./Logout
