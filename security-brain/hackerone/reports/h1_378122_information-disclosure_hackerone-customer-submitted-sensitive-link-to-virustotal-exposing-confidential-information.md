---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '378122'
original_report_id: '378122'
title: HackerOne customer submitted sensitive link to VirusTotal, exposing confidential
  information
weakness: Information Disclosure
team_handle: security
created_at: '2018-07-06T11:18:44.587Z'
disclosed_at: '2018-07-26T20:38:02.465Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 58
tags:
- hackerone
- information-disclosure
---

# HackerOne customer submitted sensitive link to VirusTotal, exposing confidential information

## Metadata

- HackerOne Report ID: 378122
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2018-07-26T20:38:02.465Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi There,
### Steps To Reproduce

1- open this site: https://www.virustotal.com/#/domain/hackerone.com 

-------------------------

2- Then Go down to the end of this page and you will see this:

████

``https://hackerone.com/reports/334677?invitation_token=███████``

--------------

3- when i open it, i see this:

█████

---------------------

4-after the step 3 i thought it's demo from hackerone to learn us the invitation process so i found the report is valid and it contain a valid issue to ████.


--------------------------------

5-clicked on accept will lead to open this: ██████

**You have been invited to manage the report submitted to ████.**
██████████



-----

6-Now after the step 5 I was shocked and i stopped my self from doing any things else because it's just one click to **manage** the report ;)

## Impact

I was able to manage a report for ███████ program:

1-Close the report as spam or resolve or any things
2-Public disclosure of this report 
3-Discredit the ████ team by comments with unprofessional reply.
4-i will see  **internal comment** between hackerone staff there too.

Best,
@Hackerone_007

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
