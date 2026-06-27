---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '997198'
original_report_id: '997198'
title: Content Spoofing/Text Injection in https://support.cs.money and JS file not
  minified and uglyfied which makes it clearly readable
weakness: User Interface (UI) Misrepresentation of Critical Information
team_handle: cs_money
created_at: '2020-10-03T16:41:07.818Z'
disclosed_at: '2020-11-12T13:18:11.591Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: support.cs.money
asset_type: URL
max_severity: critical
tags:
- hackerone
- user-interface-ui-misrepresentation-of-critical-information
---

# Content Spoofing/Text Injection in https://support.cs.money and JS file not minified and uglyfied which makes it clearly readable

## Metadata

- HackerOne Report ID: 997198
- Weakness: User Interface (UI) Misrepresentation of Critical Information
- Program: cs_money
- Disclosed At: 2020-11-12T13:18:11.591Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Issue 1:
Greetings,

Hello Team,
I have found a Content Spoofing/Text Injection on this domain https://support.cs.money
Using the below link the attacker can trick any genuine user to go to the attacker's phishing site.

The attacker could craft the URL by providing discounts which will tempt the user to visit the attacker URL mentioned, as the site displaying the message still belongs to https://support.cs.money

## Steps To Reproduce

POC URL
[support cs money url](https://support.cs.money//.cs.money(!has-moved-to-[www.support.cs.money.in]).Please-visit__[www.cs.money.in]___present__resource)

## Issue 2 - worker.js file is user-readable 
https://cs.money/js/worker.js?language=en&v=1331&csrf_token=[removed]
The worker.js contains a lot of business logic which is deployed in production whiteout being minified or uglified. This might lead an attacker to craft attacks in future as it uses 
1. location.href`
2. eval
  in the below code snipped 
```
case 'method':
            try {
                postMessage({
                    cbid: data.cbid,
                    result: eval(`(${data.method})`)()
                });
            } catch (err) {
                console.warn(err);
            }
            break;
```

PoC Screenshots attached.

Let me know if you need more information.

Cheers!

## Impact

Crafted phishing attacks on cs.money

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
