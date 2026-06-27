---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1592596'
original_report_id: '1592596'
title: Sensei LMS IDOR to send message
weakness: Insecure Direct Object Reference (IDOR)
team_handle: automattic
created_at: '2022-06-06T19:07:59.563Z'
disclosed_at: '2022-08-04T10:17:38.560Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
asset_identifier: WordPress Plugins & Themes
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Sensei LMS IDOR to send message

## Metadata

- HackerOne Report ID: 1592596
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: automattic
- Disclosed At: 2022-08-04T10:17:38.560Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there, hope you are doing great.
So, there is an option to send message to teacher privately by student on Sensei LMS.
Each message sent by student will have different ID,
Student1 cannot access or send message to the message from Student2 (which is meant to be private with teacher)
Similarly Student2 cannot view/send message sent by student1 to the teacher.

But due to lack of access control, it is possible for any student to reply on any thread of Student to teacher just by simply changing ID of the thread which is numeric.

This may sound a bit complex but i will try to explain this with video POC, please let me know if you still didn't understood the vulnerability here:
{F1759226}

## Impact

Any student can reply to other student's thread which is meant to be private between the original student [who sent message] and teacher.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
