---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '4931'
original_report_id: '4931'
title: CONCRETE5 - path disclosure.
weakness: Information Disclosure
team_handle: concretecms
created_at: '2014-03-27T15:59:53.362Z'
disclosed_at: '2014-06-09T18:30:08.593Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# CONCRETE5 - path disclosure.

## Metadata

- HackerOne Report ID: 4931
- Weakness: Information Disclosure
- Program: concretecms
- Disclosed At: 2014-06-09T18:30:08.593Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

When you emtpy the cookie `CONCRETE5` it will throw the following error on the page :

`Warning: session_start() [function.session-start]: The session id contains illegal characters, valid characters are a-z, A-Z, 0-9 and '-,' in /home/c5host/msm_versions/012312/concrete/startup/session.php on line 22
Warning: session_start() [function.session-start]: Cannot send session cookie - headers already sent by (output started at /home/c5host/msm_versions/012312/concrete/startup/session.php:22) in /home/c5host/msm_versions/012312/concrete/startup/session.php on line 22`
`Warning: session_start() [function.session-start]: Cannot send session cache limiter - headers already sent (output started at /home/c5host/msm_versions/012312/concrete/startup/session.php:22) in /home/c5host/msm_versions/012312/concrete/startup/session.php on line 22
Warning: Cannot modify header information - headers already sent by (output started at /home/c5host/msm_versions/012312/concrete/startup/session.php:22) in /home/c5host/msm_versions/012312/concrete/libraries/view.php on line 841`

Best regards,

Olivier Beg

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
