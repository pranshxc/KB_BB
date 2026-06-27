---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1628012'
original_report_id: '1628012'
title: IDOR Lead  To VIEW & DELETE & Create api_key [HtUS]
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2022-07-06T14:07:41.852Z'
disclosed_at: '2022-09-14T20:32:38.142Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR Lead  To VIEW & DELETE & Create api_key [HtUS]

## Metadata

- HackerOne Report ID: 1628012
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2022-09-14T20:32:38.142Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#### Hi Dod & Hackerone Team i hope you are Doing Well Today :)



#### Explaining:

* i found That a User With a Member Permission in a Organization Can Create & View & DELETE API_KEYS

#### Step To Reproduce: 

1_ First Create 2 Accounts From Here `https://███`

2_ Log in With The Victim User and Create New Group From Here `https://███/organization`

3_ After Creating The org, Go Here To invite New Users `https://█████████/organization/ORG-UUID/members`

4_ invite The Attacker User With The Role Member

5_ Now add Some Private Keys Here `https://██████████/organization/ORG-UUID/apiKeys` , and save The Req as Create_Req 

6_ Switch Back To The Attacker User and Try To Access The Endpoint `https://██████/organization/ORG-UUID/apiKeys` , you will Notice You have Access To Read The apikey Now Copy The UUID of The apikey & Put it Here 

7_  https://██████████/organization/ORG-UUID/apiKeys/API-UUID , make a DELETE req

8_ Now Copy The Cookies of The attacker & replace it with The Create_Req in Step `5`, 

*  Now you can Create & View & DELET

#### Poc_Video:
█████

## Impact

IDOR Lead  To VIEW & DELETE & Create Private api_key

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
