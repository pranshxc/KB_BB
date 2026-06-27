---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '319279'
original_report_id: '319279'
title: '[critical] sql injection by GET method'
weakness: SQL Injection
team_handle: khanacademy
created_at: '2018-02-24T01:24:25.947Z'
disclosed_at: '2018-03-06T18:16:20.077Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- sql-injection
---

# [critical] sql injection by GET method

## Metadata

- HackerOne Report ID: 319279
- Weakness: SQL Injection
- Program: khanacademy
- Disclosed At: 2018-03-06T18:16:20.077Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey there, after tampering a bit with the values, since I figured out your backend is not php (most likely django or nodejs), I found an SQL injection .
You can view my steps to reproduce, if you need additional screenshots, please let me know.
Regards Gabriel Kimiaie

## Impact

If I dig deeper, I may be able to read datas from your database, hopefully I won't do it.

The hacker selected the **SQL Injection** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**Verified**
Yes

**What exploitation technique did you utilize?**
Boolean

**Please describe the results of your verification attempt.**
After submitting a single quote, I got the 500 error. after few steps, I got rid of the 500 error by forging a valid sql query which is as follows:
https://www.khanacademy.org/translations/videos/en'%20or'1'=='1_youtube_stats.csv 
it returns to me all csv since 1 is equal to one
when changing the boolean condition:
https://www.khanacademy.org/translations/videos/en'%20AND'1'=='0_youtube_stats.csv
(and '1'=='0): only the english csvs are shown.

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
