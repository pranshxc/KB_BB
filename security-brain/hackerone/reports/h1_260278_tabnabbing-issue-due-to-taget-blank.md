---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260278'
original_report_id: '260278'
title: TabNabbing issue (due to taget=_blank)
team_handle: legalrobot
created_at: '2017-08-15T11:02:27.983Z'
disclosed_at: '2017-08-16T04:58:46.256Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: app.legalrobot-test.com
asset_type: URL
max_severity: none
tags:
- hackerone
---

# TabNabbing issue (due to taget=_blank)

## Metadata

- HackerOne Report ID: 260278
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-08-16T04:58:46.256Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

i get to know in this particular url 
https://app.legalrobot-uat.com/dmca-safe-harbor  and i found one 3rd party url.

Issue lies Here :
```
<a href="https://eff.org" target="_blank">Electronic Frontier Foundation</a>
```
Here i can see you are using target=_blank and  no more rel tag.
Here , target=_blank means it will open in another new tab. but due to tabnabbing it can change parent tab as well (Legalrobot).
so as per security principal , don't trust much on 3rd party. and be at your safe sight,

i can recommend you to add rel="noreferer, ,noopener" to avoid this issue.

So final tag for that particular anchor tag will be:
``
<a href="https://eff.org" target="_blank" rel="norefere,noopener">Electronic Frontier Foundation</a>
```

more safe !!
Please let me know for more information.

Thanks,
Vishal

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
