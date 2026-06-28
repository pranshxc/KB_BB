---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-30_improper-storage-of-private-projects-files.md
original_filename: 2017-08-30_improper-storage-of-private-projects-files.md
title: Improper Storage of Private Project’s Files
category: documents
detected_topics:
- cloud-security
- idor
- command-injection
- otp
tags:
- imported
- documents
- cloud-security
- idor
- command-injection
- otp
language: en
raw_sha256: e44061c54d57a5dc57768fb30981178573757c2badc8a6cfae4b41f03bb1b6e9
text_sha256: dfc62865837f5011a77e4227f031fbe5561b16903295bc75fd0a38f61e625d20
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Improper Storage of Private Project’s Files

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-30_improper-storage-of-private-projects-files.md
- Source Type: markdown
- Detected Topics: cloud-security, idor, command-injection, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `e44061c54d57a5dc57768fb30981178573757c2badc8a6cfae4b41f03bb1b6e9`
- Text SHA256: `dfc62865837f5011a77e4227f031fbe5561b16903295bc75fd0a38f61e625d20`


## Content

---
title: "Improper Storage of Private Project’s Files"
url: "https://medium.com/@arbazhussain/improper-storage-of-protected-projects-files-9ece8e9a4743"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
bugs: ["IDOR"]
publication_date: "2017-08-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6118
scraped_via: "browseros"
---

# Improper Storage of Private Project’s Files

Improper Storage of Private Project’s Files
Arbaz Hussain
Follow
2 min read
·
Aug 30, 2017

113

1

Severity: High

Complexity: Easy

Weakness: Improper Storage of files on S3 Buckets

While Testing one of the private on Hackerone , Their Main Feature functionality is to Write code for Their project and save the project’s as (Private/Public)
Whenever we store something in public Project . it’s files get store to

https://REDACTED.s3.amazonaws.com/sagewfextdg/uploads/ 1494851423/1.py

Here sagewfextdg is the ID for the PUBLIC Projects

Same thing tried with Private Projects :

https://REDACTED.s3.amazonaws.com/sawexvecswt/uploads/ 1494851123/1.py

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here sawexvecswt is the ID for the Private Projects

Now we got ID for Public/Private projects files at s3 Bucket where files are getting saved.

/uploads/1494851423/1.py

Only thing we have this/1494851423/ which is nothing but timestamp

Timestamp is encoded information identifying current date-month-year-hour-minutes-seconds

You can convert the timestamp to human readable format from here http://www.unixtimestamp.com/
Wrote a simple script to generate timestamp for whole day(24 hours) using datetime python module and Started Fuzzing
Press enter or click to view image in full size
Demonstrated by Placing simple .JPG File in Project
Able to access private files of Other User’s.
They have Added Auth Token Verifier to View or Download Files from S3 Bucket as a FIX.
