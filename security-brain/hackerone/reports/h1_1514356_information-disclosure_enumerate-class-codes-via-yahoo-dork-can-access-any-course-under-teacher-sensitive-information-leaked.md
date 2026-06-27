---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1514356'
original_report_id: '1514356'
title: Enumerate class codes via yahoo dork - Can access any course under teacher
  - Sensitive information leaked
weakness: Information Disclosure
team_handle: khanacademy
created_at: '2022-03-16T23:30:59.079Z'
disclosed_at: '2022-05-01T18:05:32.828Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- information-disclosure
---

# Enumerate class codes via yahoo dork - Can access any course under teacher - Sensitive information leaked

## Metadata

- HackerOne Report ID: 1514356
- Weakness: Information Disclosure
- Program: khanacademy
- Disclosed At: 2022-05-01T18:05:32.828Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,
I am quality researcher and I found some links using yahoo dorking techniques
I used yahoo dork `site:pl.khanacademy.org/join` 
I used Firefox browser.

Steps to reproduce:
1.Go to yahoo search page and use above query to enumerate.
2.Create student account by filling all the required details
3.Now you are in the class without actually invited by teacher.
4.You can pick any course from item and start you course.

I can also able to see teacher Full name- This is sensitive information 

Attached POC:

## Impact

Any black hacker can enumerate all the classes and join in them and can make chaos.
Some chances of IDOR too.
If you can encrypt this class details which some hashing technique and this will not showed up with dorking queries.

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
