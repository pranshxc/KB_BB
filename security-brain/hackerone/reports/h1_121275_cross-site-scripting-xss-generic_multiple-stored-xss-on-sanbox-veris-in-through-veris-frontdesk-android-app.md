---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '121275'
original_report_id: '121275'
title: Multiple Stored XSS on Sanbox.veris.in through Veris Frontdesk Android App
weakness: Cross-site Scripting (XSS) - Generic
team_handle: veris
created_at: '2016-03-08T10:59:23.569Z'
disclosed_at: '2016-06-12T16:04:43.677Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Multiple Stored XSS on Sanbox.veris.in through Veris Frontdesk Android App

## Metadata

- HackerOne Report ID: 121275
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: veris
- Disclosed At: 2016-06-12T16:04:43.677Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I have found multiple cross site scripting vulnerabilities on sanbox.veris.in due to the malicious input injected through veris frontdesk android app.

Vulnerable App : Veris Frontdesk Android App

Vulnerable Input Fields: 1) Who do you wish to meet?
                                2) Additional Information

Payload used: <img src=x onerror=alert(3)> and <img src=x onerror=alert(4)>

Reflects where: https://sandbox.veris.in/portal/visitor-log/

Steps to Reproduce:

1. Open Veris Front Desk App.
2. Go to Check In.
3. Enter the required details like first name, last name and phone number.
4. Proceed to Next.
5. Inject the above mentioned payload in vulnerable input fields.
6. Submit it and Check In.
7. Login to your account on sandbox.veris.in
8. Go to https://sandbox.veris.in/portal/visitor-log/
9. Tadaa! XSS Triggers.

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
