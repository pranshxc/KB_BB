---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '255125'
original_report_id: '255125'
title: Null Byte Injection in all fields of Profile
weakness: Improper Null Termination
team_handle: legalrobot
created_at: '2017-07-31T10:29:46.785Z'
disclosed_at: '2018-02-24T12:29:05.011Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-null-termination
---

# Null Byte Injection in all fields of Profile

## Metadata

- HackerOne Report ID: 255125
- Weakness: Improper Null Termination
- Program: legalrobot
- Disclosed At: 2018-02-24T12:29:05.011Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Team,

Null byte injection is possible in all the fields of Edit Profile functionality.

**Affected URL:** 
https://app.legalrobot.com/account

**Description:** 
Possible Injection of control characters, such as Null Byte 0x00, \000, \x00, \z, or the Unicode representation \u0000 into vulnerable fields in the Message endpoints in order to cause unexpected, harmful behaviors. 
 A null character can be placed in a any field of profile with the percent code %00.
The ability to represent a null character does not always mean the resulting string will be correctly interpreted, as many programs will consider the null to be the end of the string.

**POC:**
1. Register a User.
2. Click on Account.
3. Click on Edit Profile.
4. Put some control characters.
5. Click on submit.
6. Control characters will be saved at Server side as well as rendered at client side.

**Fix:** Block the control characters from being saved on the back-end when included in user-input, as well as to suppress the output and rendering of previously-submitted control characters.

Please find the attached screen shot as well.

Thanks,
Akash Saxena

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
