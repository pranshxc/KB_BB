---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-12_write-up-1-hellosign-integration-full-read-ssrf.md
original_filename: 2022-07-12_write-up-1-hellosign-integration-full-read-ssrf.md
title: 'Write Up 1: Hellosign Integration [Full Read SSRF]'
category: documents
detected_topics:
- ssrf
- sso
- access-control
- command-injection
- file-upload
- otp
tags:
- imported
- documents
- ssrf
- sso
- access-control
- command-injection
- file-upload
- otp
language: en
raw_sha256: 986c964b1fbf0e15e4e2fa558254c721c9ad86c37976f53df71eaa7253d513b1
text_sha256: 381809e203d5300f0df9fe597e9d7aa15ec47b81bbf55670e33f51522973c185
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Write Up 1: Hellosign Integration [Full Read SSRF]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-12_write-up-1-hellosign-integration-full-read-ssrf.md
- Source Type: markdown
- Detected Topics: ssrf, sso, access-control, command-injection, file-upload, otp
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `986c964b1fbf0e15e4e2fa558254c721c9ad86c37976f53df71eaa7253d513b1`
- Text SHA256: `381809e203d5300f0df9fe597e9d7aa15ec47b81bbf55670e33f51522973c185`


## Content

---
title: "Write Up 1: Hellosign Integration [Full Read SSRF]"
url: "https://medium.com/@soufianehabti/write-up-1-hellosign-integration-full-read-ssrf-df5e1a5bc627"
authors: ["Soufiane Habti (@wld_basha)"]
bugs: ["SSRF"]
bounty: "2,000"
publication_date: "2022-07-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2465
scraped_via: "browseros"
---

# Write Up 1: Hellosign Integration [Full Read SSRF]

Write Up 1: Hellosign Integration [Full Read SSRF]
Soufiane Habti
Follow
2 min read
·
Jul 12, 2022

120

1

بسم الله الرحمن الرحيم

Well, after a lot of attempts to start this series of write-ups I’m finally doing it. Briefly, this series of write-ups will be just some stories about my cool findings.

Press enter or click to view image in full size
Target:

Since the target had a private bug bounty program, I won’t be disclosing the name, but it was a company that makes the recruiting process more manageable.

Attack surface:

From the target description, you can already tell what could the attack surface be: access controls (different privileges), file uploads (CVs, company documents, etc), and so much more. I tried to focus first on features that include uploading/modifying files.

Recon:

After going through every button and feature, one of the used integrations caught my attention which was signing company documents with HelloSign,

Get Soufiane Habti’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I visualized the normal flow to sign a company’s document on the application

Press enter or click to view image in full size
Low Quality visualization of the flow -_-’

Everything about the flow above seemed good until I saw an edit button.

After submitting a modification on the signed document (name, type, etc), the application sends a multipart form to the server with the S3 bucket link to the file.

Press enter or click to view image in full size
That’s where the bug happened

Without any further thinking I easily put the famous http://169.254.169.254/latest/meta-data/ and opened the file using the hellosign integration, finally I enumerated my way to get the access token.

Press enter or click to view image in full size
Happy image right ?

Timeline

Jun 01, 2022 — Report Sent.
Jun 02, 2022 — Hackerone Triage asking for more information (Using documents signing feature was a PIA).
Jun 13, 2022 — Vulnerability Fixed.
Jun 13, 2022 — $2000 bounty awarded by the program.

Tips: maybe I didn’t share any cool technic in this write-up, but I shared an important lesson : don’t ignore edit buttons :).
