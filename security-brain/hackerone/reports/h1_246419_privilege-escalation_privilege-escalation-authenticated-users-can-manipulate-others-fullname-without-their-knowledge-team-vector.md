---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '246419'
original_report_id: '246419'
title: '[Privilege Escalation] Authenticated users can manipulate others fullname
  without their knowledge [Team Vector]'
weakness: Privilege Escalation
team_handle: wakatime
created_at: '2017-07-06T13:00:55.541Z'
disclosed_at: '2017-08-10T02:14:02.065Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- privilege-escalation
---

# [Privilege Escalation] Authenticated users can manipulate others fullname without their knowledge [Team Vector]

## Metadata

- HackerOne Report ID: 246419
- Weakness: Privilege Escalation
- Program: wakatime
- Disclosed At: 2017-08-10T02:14:02.065Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

## Summary,
When my free trial subscription was activated on wakatime.com, i also found that there is a new tab or features which is the `Teams`, 
In `Teams` you can manipulate again others `fullname` without their knowledge.
as the details of my other reports [[Privilege Escalation] Authenticated users can manipulate others fullname without their knowledge
](https://hackerone.com/reports/244567) This time the endpoint that we are using is Teams, not Leaderboards.

## Steps:
1.) Go to the Teams->Settings->Members
2.) Invite other users on your Teams member settings
3.) Now you will see again that there is `Edit Icon` on the victim after fullname, Click that.
4.) Then prompt will pop up saying "Enter new name for blahblah.." then just put a value e.g. HACKED AGAIN!
5.) Now go login the victim email, and you will notice that the fullname of the victim was change into HACKED AGAIN!

## Here is the PoC Video for clearer demonstration.
{F200597}

## Suggested Mitigation/Remediation Actions

Don't allow other authenticated users to manipulate others fullname.

Kind Regards,
@reydd

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
