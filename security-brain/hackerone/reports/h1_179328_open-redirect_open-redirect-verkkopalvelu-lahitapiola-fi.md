---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '179328'
original_report_id: '179328'
title: Open Redirect (verkkopalvelu.lahitapiola.fi)
weakness: Open Redirect
team_handle: localtapiola
created_at: '2016-11-01T09:07:04.277Z'
disclosed_at: '2016-12-26T06:50:17.157Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
- open-redirect
---

# Open Redirect (verkkopalvelu.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 179328
- Weakness: Open Redirect
- Program: localtapiola
- Disclosed At: 2016-12-26T06:50:17.157Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**PoC:**
Open link and wait a full load
```
https://verkkopalvelu.lahitapiola.fi//blackfan.ru/%2f../e2/kotivakuutus/vakuutuslaskuri/
```

**Result:**
Redirect to another site - blackfan.ru

**Vulnerable script:**
https://verkkopalvelu.lahitapiola.fi/e2/kotivakuutus/vakuutuslaskuri/scripts/app.js
```js
        function a(e) {
            window.location.replace(window.location.pathname + window.location.search + "#" + e)
        }
```

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
