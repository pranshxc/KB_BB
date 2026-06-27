---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '31383'
original_report_id: '31383'
title: Ability to see common response titles of other teams (limited)
weakness: Information Disclosure
team_handle: security
created_at: '2014-10-14T23:37:10.258Z'
disclosed_at: '2014-10-15T14:14:10.542Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- information-disclosure
---

# Ability to see common response titles of other teams (limited)

## Metadata

- HackerOne Report ID: 31383
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2014-10-15T14:14:10.542Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello guys,

Not sure what's happening exactly but when I go to my team (program) dashboard add a new Trigger and then tamper the request and change JSON variable `common_response_id` to say **24** and after trigger gets added I see a title of ████████ which is not in my default team template nor added by someone else of the team. Similarly if I set `common_response_id` to **18**, I get a trigger title of ████████ in the trigger (refer screenshots).This certainly seems to be of some other team.

**JSON (which gives trigger title as ████████):**
`{"title":"hackerone","criteria":[{"field":"any","type":"inclusion","inverse":false,"data":"agfagasga"}],"actions":[{"type":"request-needs-more-info","common_response_id":24}],"disabled":false}`

**Steps to Reproduce**

1. Login to Program/Team Dashboard 
2. Goto https://hackerone.com/<team-name>/triggers/new
3. Leave all options default and add text to criteria and select any common response.
4. Start the intercepting proxy and configure it to intercept the request
5. Now add title and enable the trigger then hit **Save**
6. Modify `common_response_id` to 24 for ████████ title or 18 for ████████ title

Kindly refer to screenshots as well.Revert back if you have any further query.

Thanks,
Prakhar Prasad

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
