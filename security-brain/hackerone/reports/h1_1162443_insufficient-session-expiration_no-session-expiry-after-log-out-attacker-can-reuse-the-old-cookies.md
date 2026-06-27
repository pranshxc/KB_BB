---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1162443'
original_report_id: '1162443'
title: No Session Expiry after log-out, attacker can reuse the old cookies
weakness: Insufficient Session Expiration
team_handle: shopify
created_at: '2021-04-13T11:03:11.033Z'
disclosed_at: '2024-05-01T18:16:40.098Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 46
asset_identifier: exchangemarketplace.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- insufficient-session-expiration
---

# No Session Expiry after log-out, attacker can reuse the old cookies

## Metadata

- HackerOne Report ID: 1162443
- Weakness: Insufficient Session Expiration
- Program: shopify
- Disclosed At: 2024-05-01T18:16:40.098Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
There is no session expiry after log-out which can help an attacker to take-over the full account by reusing it. 

**Reproduction Steps**
1. Go to https://exchangemarketplace.com/ and click on Sign In
2. Continue with Google Account
3. Use "EditThisCookie" Extension to export the cookies
4. Once you logged in - click on "EditThisCookie" Extension and export the cookies
5. Now open another browser and import those cookies - you can able to login an account by using cookies
6. Logout from your first browser - it should logout from another browser as well.
7. Now, login again with your google account - This time use old cookies. 
8.  By using old cookies, you can able to login victim's account. (Whenever victim's session is active)

Please find the attached POC video
████████

## Impact

**Attack Scenario:** If a malicious user gets the victim's cookies by exploiting any vulnerability, he can log in to victim's account . Whenever the victim's session is active an attacker can login victim's account by using old cookies.

**Impact:** If a malicious user gets the cookies by exploiting any vulnerability, he can log in to the victim's account.

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
