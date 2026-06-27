---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '55431'
original_report_id: '55431'
title: 'XML Parser Bug: XXE over which leads to RCE'
weakness: Code Injection
team_handle: drchrono
created_at: '2015-04-08T22:37:09.977Z'
disclosed_at: '2016-06-13T19:02:48.525Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
tags:
- hackerone
- code-injection
---

# XML Parser Bug: XXE over which leads to RCE

## Metadata

- HackerOne Report ID: 55431
- Weakness: Code Injection
- Program: drchrono
- Disclosed At: 2016-06-13T19:02:48.525Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello security team,

I have reported this issue on Feb 6, 2015 and i'm resubmit it here again.
I was able to do XXE attack on your site and exposed the /etc/passwd file.
Scenario:
1. Login to drchrono  site.
2. Click on patients->patient
3. Click on ' Update patient (via C-CDA XML).'
4. Select the file I attached, (AXAX000001.xml), I download it from your site and added there struct for my exploit.
5. Click on 'Preview' and you'll see the content of /etc/passwd, (That can be any file on the system or any command). See xxe.png atttachement.


Best regards,
Sasi

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
