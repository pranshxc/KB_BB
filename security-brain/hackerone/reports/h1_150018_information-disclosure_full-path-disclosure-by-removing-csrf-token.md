---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150018'
original_report_id: '150018'
title: Full Path Disclosure by removing CSRF token
weakness: Information Disclosure
team_handle: paragonie
created_at: '2016-07-08T14:38:36.558Z'
disclosed_at: '2016-07-08T15:13:02.182Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure by removing CSRF token

## Metadata

- HackerOne Report ID: 150018
- Weakness: Information Disclosure
- Program: paragonie
- Disclosed At: 2016-07-08T15:13:02.182Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello, you can get an error and full path disclosure by following these steps:
on any user generated POST request (such as during login, or changing user data) remove the CSRF token from the post request entirely. For example, on the login POST request,

_CSRF_TOKEN=WqXB7vmysdM06gBarWZiNfnZ%3AOMznb0rVagzWr41P_h_N2Qj50LwPV2HZxKyJxR17lB6b&username=zrgzrgzerg&passphrase=sergsergsergrg&two_factor=

Becomes

username=zrgzrgzerg&passphrase=sergsergsergrg&two_factor=

We get the following error with a full path disclosure:

<br />
<b>Notice</b>:  Undefined variable: ex in <b>/var/www/csprng/src/public/index.php</b> on line <b>160</b><br />
<br />
<b>Fatal error</b>:  Uncaught Error: Call to a member function getMessage() on null in /var/www/csprng/src/public/index.php:160
Stack trace:
0 {main}
  thrown in <b>/var/www/csprng/src/public/index.php</b> on line <b>160</b><br />

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
