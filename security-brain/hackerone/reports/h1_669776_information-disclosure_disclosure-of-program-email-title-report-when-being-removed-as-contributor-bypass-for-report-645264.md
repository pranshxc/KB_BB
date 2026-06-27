---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '669776'
original_report_id: '669776'
title: 'Disclosure of Program email Title Report when being removed as contributor.
  Bypass for Report #645264'
weakness: Information Disclosure
team_handle: security
created_at: '2019-08-08T15:48:03.185Z'
disclosed_at: '2019-09-06T17:37:14.304Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Disclosure of Program email Title Report when being removed as contributor. Bypass for Report #645264

## Metadata

- HackerOne Report ID: 669776
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2019-09-06T17:37:14.304Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
It is somehow related to this report #645264. But I found an alternative way to reproduce the issue even it is considered as resolved.



### Steps To Reproduce

1. As a Program admin, navigate to ```Program Settings``` 
2. Click ```Program```
3. Click ```Email Notifications```
4. Make sure it is set to ```No Content```
5. Go to any report in your program and invite any hacker to the report.
6. Notice that the contributors email will receive an email WITHOUT REPORT TITLE (SINCE IT IS ALREADY FIXED)
 [F550181]

### Steps To Bypass the #645264
1. Go to the report that you added to the contributor’s email ( step 5 )
2. Participants section then hover on the invited contributor’s email. ```SELECT REMOVE PARTICIPANT```
████
3. Hackerone will send another email that the invitation has been revoked. But notice that the email sent disclosed the Title that supposed to be mask.
{F550178}
{F550179}

## Impact

Even thou #645264 is considered as resolved and fixed has been implemented, there’s still a way that it the Notification Settings is not totally fix since it still send email with Title that supposed to be mask. I know you will think that “ but the contributor is already remove so it is not an issue” the fact that it disclose information that supposed to be not is considered a bug. What if the Title contains confidential information like type of attack and the domain?

I hope you get what I mean, if you need more information, please let me know 

Thanks,

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
