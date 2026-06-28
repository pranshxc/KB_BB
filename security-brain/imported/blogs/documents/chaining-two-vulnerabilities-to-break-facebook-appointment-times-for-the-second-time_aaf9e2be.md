---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-14_chaining-two-vulnerabilities-to-break-facebook-appointment-times-for-the-second-.md
original_filename: 2018-12-14_chaining-two-vulnerabilities-to-break-facebook-appointment-times-for-the-second-.md
title: Chaining Two Vulnerabilities to Break Facebook Appointment Times For the Second
  Time
category: documents
detected_topics:
- command-injection
- graphql
- business-logic
tags:
- imported
- documents
- command-injection
- graphql
- business-logic
language: en
raw_sha256: aaf9e2be3b87f09910614b9d3cd1e18bddf93f8b46698f0c0a6ade41bd62acba
text_sha256: f3597a684e8de90acafe286c2cb3ec2546a538180934945e26cf22e7aba242e1
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining Two Vulnerabilities to Break Facebook Appointment Times For the Second Time

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-14_chaining-two-vulnerabilities-to-break-facebook-appointment-times-for-the-second-.md
- Source Type: markdown
- Detected Topics: command-injection, graphql, business-logic
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `aaf9e2be3b87f09910614b9d3cd1e18bddf93f8b46698f0c0a6ade41bd62acba`
- Text SHA256: `f3597a684e8de90acafe286c2cb3ec2546a538180934945e26cf22e7aba242e1`


## Content

---
title: "Chaining Two Vulnerabilities to Break Facebook Appointment Times For the Second Time"
url: "https://medium.com/@maxpasqua/chaining-two-vulnerabilities-to-break-facebook-appointment-times-for-the-second-time-ac639f8c8773"
authors: ["Max Pasqua"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Application-level DoS"]
bounty: "500"
publication_date: "2018-12-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5526
scraped_via: "browseros"
---

# Chaining Two Vulnerabilities to Break Facebook Appointment Times For the Second Time

Chaining Two Vulnerabilities to Break Facebook Appointment Times For the Second Time
Max Pasqua
Follow
1 min read
·
Dec 15, 2018

159

Along with https://medium.com/bugbountywriteup/breaking-appointments-and-job-interview-schedules-with-malformed-times-edef103e46ba during my searching I found a second vulnerability to break the newly added appointment tab in Facebook pages. The first vulnerability allowed for the start time and end time of Facebook appointments to be the set to the same value making no available times for job interviews or services to be booked. Normally this wouldn’t be too impactful as an admin could just change the times back to normal but that’s where the second vulnerability comes into play. Providing a malformed time in the same graphql POST call to the max_advanced_notice parameter would then cause an integer overflow when trying to load the time schedule rendering it unchangeable and therefor locking in the previous vulnerability from being changed

Proof of Concept

1) Browse to your pages appointment settings

2) Hit change on the available appointment times

3) Intercept the POST request sent to /api/graphqlbatch/ to change the times

4) Edit the end_times and start_times parameters so they match (eg. end_times”:[540,540,540,540,540],”start_times”:[540,540,540,540,540])

Get Max Pasqua’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

5) Edit the max_advanced_notice parameter to a malformed/larger time (eg. 15552000000)

6) The appointment time settings should now be broken

Video

Timeline

Submitted- October 12th, 2018

Triaged- October 16th, 2018

Bounty Awarded($500)- December 14th, 2018
