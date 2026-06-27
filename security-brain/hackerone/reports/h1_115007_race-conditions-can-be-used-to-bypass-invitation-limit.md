---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115007'
original_report_id: '115007'
title: Race conditions can be used to bypass invitation limit
team_handle: keybase
created_at: '2016-02-06T01:41:33.280Z'
disclosed_at: '2016-08-10T19:47:01.886Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
tags:
- hackerone
---

# Race conditions can be used to bypass invitation limit

## Metadata

- HackerOne Report ID: 115007
- Weakness: 
- Program: keybase
- Disclosed At: 2016-08-10T19:47:01.886Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I have received 3 invites from Chris (I might have screwed up the PGP email, but thanks anyway), added to my account https://keybase.io/josipfranjkovic. Using race conditions, I was able to send out a total of 7 invites to my throwaway emails, obviously bypassing the 3 invitations limit. 
Here are the steps to reproduce:
1. Login to your Keybase account, which has >0 invitations left.
2. Go to https://keybase.io/account/invitations
3. Enter an email, and click the invitation button
4. A POST request will be sent to `/_/api/1.0/send_invitation.json`. Repeat this POST request multiple times in short time frame, and change the `email` POST parameter as needed.
5. Multiple invitations will be send, bypassing the limit. 

(I have reclaimed the invitations for further testing)

Best regards,

Josip

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
