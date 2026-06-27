---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '692154'
original_report_id: '692154'
title: Open Redirect in the Path of vendhq.com
weakness: Open Redirect
team_handle: vend_vdp
created_at: '2019-09-11T05:17:31.445Z'
disclosed_at: '2019-10-31T00:23:42.098Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: www.vendhq.com
asset_type: URL
max_severity: high
tags:
- hackerone
- open-redirect
---

# Open Redirect in the Path of vendhq.com

## Metadata

- HackerOne Report ID: 692154
- Weakness: Open Redirect
- Program: vend_vdp
- Disclosed At: 2019-10-31T00:23:42.098Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
There is an open redirection vulnerability in the path of 
```
https://www.vendhq.com/
```

**Description:**
An attacker can redirect anyone to malicious sites.

## Steps To Reproduce:

Type in this URL:

```
https://www.vendhq.com//evil.com/
```

As, you can see it redirects to that website when you inject this payload:
 ```
//evil.com/
```

evil.com was used as an example but this could be any website note, the `//` is the bypass.



## Supporting Material/References:

  * https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html

## Impact

* Attackers can serve malicious websites that steal passwords or download ransomware to their victims machine due to a redirect and there are a heap of other attack vectors.

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
