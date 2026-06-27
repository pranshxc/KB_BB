---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '384255'
original_report_id: '384255'
title: Stored XSS on Issue details page
weakness: Cross-site Scripting (XSS) - Stored
team_handle: gitlab
created_at: '2018-07-19T17:49:43.530Z'
disclosed_at: '2018-10-30T06:12:08.889Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on Issue details page

## Metadata

- HackerOne Report ID: 384255
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: gitlab
- Disclosed At: 2018-10-30T06:12:08.889Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The detail page of Issue (the page that provides the content of an Issue) is vulnerable to Stored XSS.

**Description:**
The two exploits are via the function of submittin an issue or the function of editing an issue.
This vulnerability is reproduced in `Firefox` and`Chrome`. `IE11` and`Edge` are not. I did not test the reproduction on other browsers.

## Steps To Reproduce:
1. Sign in to GitLab.
2. Click the "[+]" icon.
3. Click "New Project".
4. Fill out "Project name" form with "PoC".
5. Check the check box of "Public".
6. Click "Issues"
7. Click "New issue" button.
8. Fill out the each form as follows:
    * Title: PoC
    * Description: `![xss" onload=alert(1);//](a)`
9. Click "Submit issue".

Furthermore, when editing an already existing issue, you can also reproduce by entering A in the "Description" form and saving it.

## Impact

The security impact is the same as any typical Stored XSS.

Thank you!

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
