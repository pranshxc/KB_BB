---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2476149'
original_report_id: '2476149'
title: 'Confirmed #2118458: Intentional redirect from www.hackerone.com to domain
  which is up for sale'
team_handle: security
created_at: '2024-04-23T17:16:26.613Z'
disclosed_at: '2024-05-09T21:38:31.890Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 73
asset_identifier: www.hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Confirmed #2118458: Intentional redirect from www.hackerone.com to domain which is up for sale

## Metadata

- HackerOne Report ID: 2476149
- Weakness: 
- Program: security
- Disclosed At: 2024-05-09T21:38:31.890Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

P.S.: Actually I submitted this issue back in August 2023 (#2118458), but the domain was just displaying an error. So, I contacted the domain owner for the deal to sell the domain to me and showed you the screenshot of our conversation, but it wasn't considered a valid bug (Even I realized later that it was not a valid proof 😀).

**Summary:**
There is this endpoint- https://www.hackerone.com/node/9386 which automatically redirects to https://www.iotna.com/. But the domain- **iotna.com** is on sale.

### Steps To Reproduce

1. Open any browser.
2. Visit [this](https://www.hackerone.com/node/9386) link.
3. You will be automatically redirected to https://www.iotna.com/.
4. Observe that the domain is up for sale.

{F3218688}
{F3218689}

## Impact

1. If anybody obtains the domain, it may use Hackerone as a starting point of the attack and trick users to perform unintended actions, make them download malwares, compromise their systems, etc.
1. Also, it may use this to bypass **External link warning** on hackerone.com submission form ([demo](https://www.hackerone.com/node/9386)) as there is no external warning for https://www.hackerone.com. This is the reason I have set the **Scope** in CVSS to **Changed**.

(The domain price is very high, which is why I couldn't provide you with working POC 😃)

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
