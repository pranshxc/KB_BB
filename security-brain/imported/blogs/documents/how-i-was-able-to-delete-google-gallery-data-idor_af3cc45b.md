---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-30_how-i-was-able-to-delete-google-gallery-data-idor_2.md
original_filename: 2018-12-30_how-i-was-able-to-delete-google-gallery-data-idor_2.md
title: How I was able to delete Google Gallery Data [IDOR]
category: documents
detected_topics:
- idor
- command-injection
- api-security
tags:
- imported
- documents
- idor
- command-injection
- api-security
language: en
raw_sha256: af3cc45b9393982e0596ffc5e290ba03105a7446fecba1f1254220c848803bf0
text_sha256: 878b8d803971a27b22939ec63b8768adc98dad22f36f307d4408efbf2a4b3203
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to delete Google Gallery Data [IDOR]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-30_how-i-was-able-to-delete-google-gallery-data-idor_2.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `af3cc45b9393982e0596ffc5e290ba03105a7446fecba1f1254220c848803bf0`
- Text SHA256: `878b8d803971a27b22939ec63b8768adc98dad22f36f307d4408efbf2a4b3203`


## Content

---
title: "How I was able to delete Google Gallery Data [IDOR]"
url: "https://medium.com/@yogeshtantak7788/how-i-was-able-to-delete-google-gallery-data-idor-53d2f303efff"
authors: ["Yogesh Tantak"]
programs: ["Google"]
bugs: ["IDOR"]
publication_date: "2018-12-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5498
scraped_via: "browseros"
---

# How I was able to delete Google Gallery Data [IDOR]

How I was able to delete Google Gallery Data [IDOR]
Yogesh Tantak
Follow
2 min read
·
Dec 30, 2018

398

2

Hi,
This is Yogesh Tantak a Security Researcher from India. Today I am writing about a critical bug that I found in Google’s new Product “Gallery”.

You can find out more information about this product by below url:
https://www.theverge.com/2016/10/26/13418012/google-material-design-stage-gallery-pixate

This bug could allowed a malicious user to delete all collection from Gallery.io or Google gallery app.

I found this google product when I was testing some google websites.

Get Yogesh Tantak’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The vulnerable api has two parameters

Project id
Collection id <Actual Vulnerable input parameter>

The issue here is that the vulnerable api endpoint doesn’t check if the provided value for the collection_id is actually an id of a “Logged in user’s Collection_id” and not another users collection_id.
I replaced my project collection id to other user’s collection_id and after hitting the delete button other user’s collection got deleted.

Press enter or click to view image in full size
Vulnerable API endpoint
Press enter or click to view image in full size
Success Response

Reply from Google:

Press enter or click to view image in full size
Reply from Google Security Team
Press enter or click to view image in full size
Reward mail from Google
