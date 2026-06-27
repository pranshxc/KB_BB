---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '759418'
original_report_id: '759418'
title: Reflected Xss  https://██████/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2019-12-16T14:02:42.015Z'
disclosed_at: '2021-10-18T19:28:55.426Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected Xss  https://██████/

## Metadata

- HackerOne Report ID: 759418
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-10-18T19:28:55.426Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello security all teams
**Relevant Products/Components:**
last version

**Detailed Description:**
Reflected XSS so have high impact.

**Steps To Reproduce:**

1-go in subdomain
2-and check url if tableau uses
3-Uses you can add this redirect dir in url with Authentication redirect:-
/en/embeddedAuthRedirect.html?auth=javascript:alert(%22xElkomy%22)

**Such as**

 https://████████/en/embeddedAuthRedirect.html?auth=javascript:alert(%22xElkomy%22)

**Browsers Verified In:**
all browsers supporting javascript

**Supporting Material/References:**
███

**Access Vector Required for Exploitation:**

no required any access but need only web access :)

**Vulnerability Exists in Default Configuration?:**
yes

**Exploitation Requires Authentication?:**
no need anything



#xElkomy

## Impact

The need for an external delivery mechanism for the attack means that the impact of reflected XSS is generally less severe than stored XSS, where a self-contained attack can be delivered within the vulnerable application itself.

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
