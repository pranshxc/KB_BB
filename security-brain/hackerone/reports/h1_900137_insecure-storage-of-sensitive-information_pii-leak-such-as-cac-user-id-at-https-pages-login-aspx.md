---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '900137'
original_report_id: '900137'
title: PII Leak (such as CAC User ID) at https://████████/pages/login.aspx
weakness: Insecure Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2020-06-17T04:28:16.531Z'
disclosed_at: '2020-11-02T21:48:26.968Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# PII Leak (such as CAC User ID) at https://████████/pages/login.aspx

## Metadata

- HackerOne Report ID: 900137
- Weakness: Insecure Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2020-11-02T21:48:26.968Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An attacker can create an account on https://█████/pages/login.aspx and gain access to a wealth of PII for practically every member that is registered on the website. This information that the attacker has access to includes usernames, CAC User ID's, e-mail addresses, telephone numbers, first/middle/last name, and other information about a vast majority of U.S. military personnel. The portal also clearly indicates "For Official Use Only - Privacy Sensitive". Additionally, an attacker conveniently has access to export this data as a pdf, csv, or xls file, which makes data exfiltration easy. Note that this vulnerability appears to be very similar to report #808338. Please see the attached PoC videos (note that there are 2 videos because after I made the first video I realized I could scroll across and see the user's CAC User ID information, which seems very important in terms of logging into U.S. military systems). I believe this is a critical vulnerability based on the CVSS scale.

## Impact
An adversary can sign up for an account on https://█████████/pages/login.aspx to gather a vast amount of PII related to a large portion of U.S. military personnel. This can be used for many purposes and should not be accessible by a regular user.

## Step-by-step Reproduction Instructions

1. Go to https://██████████/pages/login.aspx
2. Select 'Request New Account' and log into your account
3. Once logged in go to Administration -> User -> Users
4. Observe all the information about different users on the platform

## Product, Version, and Configuration (If applicable)
https://██████/pages/login.aspx

## Suggested Mitigation/Remediation Actions
Limit this function to administrators only, as regular users should not be able to access this type of data (especially when any user can sign up from the open internet.

##References
Please see the attached PoC videos.

## Impact

An attacker can sign up for an account on https://█████████/pages/login.aspx to gather a vast amount of PII related to a large portion of U.S. military personnel. This information can then be used for various malicious purposes and should not be accessible by a regular user.

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
