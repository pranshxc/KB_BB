---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-26_antihack-idor-on-create-submission.md
original_filename: 2019-01-26_antihack-idor-on-create-submission.md
title: AntiHack IDOR on Create Submission
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: 1590f91e201b4cf73b06fe1f1f056fb612c060d151cdec37ccc833253162e727
text_sha256: de7f08ee17e03de570f9f06916cd73af1f88247d9f420e1adc649a6d9e6aaf93
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# AntiHack IDOR on Create Submission

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-26_antihack-idor-on-create-submission.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `1590f91e201b4cf73b06fe1f1f056fb612c060d151cdec37ccc833253162e727`
- Text SHA256: `de7f08ee17e03de570f9f06916cd73af1f88247d9f420e1adc649a6d9e6aaf93`


## Content

---
title: "AntiHack IDOR on Create Submission"
url: "https://medium.com/@sahruldotid/antihack-idor-on-create-submission-ddb3cf40c26b"
authors: ["Syahrul Akbar Rohmani (@sahruldotid)"]
programs: ["AntiHack.me"]
bugs: ["IDOR"]
publication_date: "2019-01-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5450
scraped_via: "browseros"
---

# AntiHack IDOR on Create Submission

AntiHack IDOR on Create Submission
Syahrul Akbar R
Follow
2 min read
·
Jan 26, 2019

24

1

Press enter or click to view image in full size

Hello everyone, this is my PoC of AntiHack IDOR. So this vulnerability can make attacker create submission on all program, even the program was locked.

Create submission and intercept request using burpsuite.
Send the request to intruder
Press enter or click to view image in full size

The vulnerable parameter is “comp_id”

3. So i create python script to generate number of comp_id

Get Syahrul Akbar R’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4. After that load into intruder and launch attack

My AntiHack inbox

Press enter or click to view image in full size

And My Profile

Press enter or click to view image in full size
Press enter or click to view image in full size
Locked Program

Timeline

Dec, 3 2018 — Reported to AntiHack

Dec, 27 2018 — AntiHack change status to Resolved and sent me a swag
