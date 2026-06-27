---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '120324'
original_report_id: '120324'
title: Multiple Stored XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: veris
created_at: '2016-03-03T11:47:48.900Z'
disclosed_at: '2016-06-12T16:04:56.095Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Multiple Stored XSS

## Metadata

- HackerOne Report ID: 120324
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: veris
- Disclosed At: 2016-06-12T16:04:56.095Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I have found multiple vulnerable fields which accepts malicious javascript inputs and reflects on another form which fails to sanitize the malicious javascript input.

Vulnerable Input Form: Edit Group Details

Reflects where: View Rule Book

Payload used: 1) <img src=x onerror=alert(document.domain)>

                         2) <img src=x onerror=alert(document.cookie)>

Browsers used: Mozilla Firefox and Google Chrome (Latest Version)

Steps to Reproduce:

1. Go to Edit Group Details Form.
2. Inject the above mentioned payload in both the input fields as shown in screenshot.
3. Submit and Save it.
4. Go to Rulebook and View it.
5. Tadaa! XSS Triggers. 

Proof of Concept: Please find the attached screenshots.

Do evaluate it and inform me accordingly.

Best Regards,

Hely H. Shah

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
