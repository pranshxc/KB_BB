---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '999789'
original_report_id: '999789'
title: Getting New Invitations without Leaving Programs
weakness: Business Logic Errors
team_handle: security
created_at: '2020-10-06T14:04:15.197Z'
disclosed_at: '2020-10-15T23:53:05.561Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 314
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Getting New Invitations without Leaving Programs

## Metadata

- HackerOne Report ID: 999789
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2020-10-15T23:53:05.561Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello there,
I hope all is well!

#Description
When you leave the private program, you get a chance to get a new invitation.
But using this vulnerability, I can get new invitations without leaving private programs.

Steps:
1. Go to any private bug bounty program.
2. Click `Leave Program` button
3. Click `Confirm` button
4. Then you will see a questionnaire form. You can see this text: `When you fill out this questionnaire, we will fast track you for the next invite batch.`    
{F1022548}
5. Click any reason (for example: `Unresponsive`) and click `Submit` button
6. Return to Burp Suite and catch the request:   
{F1022553}
7. Now, send the request to `Repeater` and forward the request.
8. Go to repeater and change the `team_handle` parameter with another private program handle which you have.
9. Send the request and you will see `"was_successful":true`

So you didn't leave the 2nd program but you got a new pending invitation.

Note: Sometimes, I see `"was_successful":true` in response but to be honest, I don't know why.
Yesterday, I sent about 25-30 request with different private programs and I asked `how much pending invitations do I have?` to `support@hackerone.com` and they said `It looks like you currently have 19 pending invitations at this time.`. 
That's why I wanted to report it.

## Impact

Users can get invitations without leaving programs.

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
