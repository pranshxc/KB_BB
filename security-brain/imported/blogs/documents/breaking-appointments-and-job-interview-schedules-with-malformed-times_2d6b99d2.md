---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-14_breaking-appointments-and-job-interview-schedules-with-malformed-times.md
original_filename: 2018-11-14_breaking-appointments-and-job-interview-schedules-with-malformed-times.md
title: Breaking Appointments and Job Interview Schedules With Malformed Times
category: documents
detected_topics:
- command-injection
- graphql
tags:
- imported
- documents
- command-injection
- graphql
language: en
raw_sha256: 2d6b99d216e89afc5477e05b4a793c92104209af74019b183405c4657b3fa6f1
text_sha256: 182543c0f3d52ac85e45edee009767d59327eece7ca1db94e3f4744befbe7fde
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Breaking Appointments and Job Interview Schedules With Malformed Times

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-14_breaking-appointments-and-job-interview-schedules-with-malformed-times.md
- Source Type: markdown
- Detected Topics: command-injection, graphql
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `2d6b99d216e89afc5477e05b4a793c92104209af74019b183405c4657b3fa6f1`
- Text SHA256: `182543c0f3d52ac85e45edee009767d59327eece7ca1db94e3f4744befbe7fde`


## Content

---
title: "Breaking Appointments and Job Interview Schedules With Malformed Times"
url: "https://medium.com/@maxpasqua/breaking-appointments-and-job-interview-schedules-with-malformed-times-edef103e46ba"
authors: ["Max Pasqua"]
programs: ["Meta / Facebook"]
bugs: ["DoS"]
bounty: "500"
publication_date: "2018-11-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5590
scraped_via: "browseros"
---

# Breaking Appointments and Job Interview Schedules With Malformed Times

Breaking Appointments and Job Interview Schedules With Malformed Times
Max Pasqua
Follow
1 min read
·
Nov 14, 2018

56

1

Facebook recently added an “Appointments” feature to pages. After a bit of searching through all the requests made I found that it was possible to use malformed times to break the appointment tab. The impact of this is that a malicious admin/editor can create irreversible damage to Appointments and Job Interview Schedules. This will stay permanently so even if the malicious actor was removed from the page. This could be especially impactful in a large organizations Facebook page as they would need to remake the entire page losing all current following on it to get a working Appointments tab back.

Proof of Concept

1) Go to https://www.facebook.com/PAGEID/manage_jobs

2) Click on a job application and hit schedule interview

3) Turn on a HTTP Interceptor such as burp suite

4) Intercept the graphql query and change suggested_end_time to a malformed time such as 15393834250000

Get Max Pasqua’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

5) The Appointments calendar should now be broken and if anybody trys to view the applicants schedule info the window will break on them

Video

Timeline

Submitted- October 19th, 2018

Triaged- October 24th, 2018

Bounty Awarded($500)- November 13th, 2018
