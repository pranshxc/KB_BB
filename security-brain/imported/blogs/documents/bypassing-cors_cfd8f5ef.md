---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-01_bypassing-cors.md
original_filename: 2019-08-01_bypassing-cors.md
title: Bypassing CORS
category: documents
detected_topics:
- cors
- command-injection
- csrf
tags:
- imported
- documents
- cors
- command-injection
- csrf
language: en
raw_sha256: cfd8f5ef171f4a1e4100a91cdb055faa6ab2d324ea8f448e35c1487f35c518e5
text_sha256: 2e7fea65047bb8d1486b30bdbe678523ec93a8c6d6fe7908f2f3784da0370d39
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing CORS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-01_bypassing-cors.md
- Source Type: markdown
- Detected Topics: cors, command-injection, csrf
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `cfd8f5ef171f4a1e4100a91cdb055faa6ab2d324ea8f448e35c1487f35c518e5`
- Text SHA256: `2e7fea65047bb8d1486b30bdbe678523ec93a8c6d6fe7908f2f3784da0370d39`


## Content

---
title: "Bypassing CORS"
url: "https://medium.com/@saadahmedx/bypassing-cors-13e46987a45b"
authors: ["Saad Ahmed (@XSaadAhmedX)"]
bugs: ["CORS misconfiguration"]
publication_date: "2019-08-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5109
scraped_via: "browseros"
---

# Bypassing CORS

Bypassing CORS
Saad Ahmed
Follow
2 min read
·
Aug 1, 2019

232

Hello friends this write-up is about how I bypassed the CORS validation. Let assume the website name redact.com. Simply I logged into the website checked for CSRF attack but there was a Current Password pram which means if I am able to bypass, there is a CSRF protection. I still need the victim’s current password to exploit it

Then I saw..

Access-Control-Allow-Origin: https://redact.com

Access-Control-Allow-Credentials: true

Get Saad Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried to set the attacker.com in the Origin header but didn’t worked out I tried by adding another Origin header it also failed basically the server was checking the Origin header value like this

Press enter or click to view image in full size

So we can simply trick the server to bypass that validation by setting the Origin header value to redact.com.attacker.com.

Press enter or click to view image in full size

Simply tried this on the redact.com & it worked.

Press enter or click to view image in full size

Loading the Account-Detail page from Evil origin to steal the information

Press enter or click to view image in full size

Send that fetch request to steal the account information page & display it on the evil.com

Press enter or click to view image in full size

Boom data steal I hope you guys like it.

./LOGOUT
