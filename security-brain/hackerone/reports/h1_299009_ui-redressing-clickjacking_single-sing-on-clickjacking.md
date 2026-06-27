---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '299009'
original_report_id: '299009'
title: Single Sing On - Clickjacking
weakness: UI Redressing (Clickjacking)
team_handle: semrush
created_at: '2017-12-18T05:11:32.852Z'
disclosed_at: '2018-02-21T15:27:13.238Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- ui-redressing-clickjacking
---

# Single Sing On - Clickjacking

## Metadata

- HackerOne Report ID: 299009
- Weakness: UI Redressing (Clickjacking)
- Program: semrush
- Disclosed At: 2018-02-21T15:27:13.238Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description:** 
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on.
**Browsers Verified In:**
Any

**Steps To Reproduce:** 
Create HTML file containg following code:
` <iframe src="https://sso.semrush.com/"></iframe> `
Execute the HTML file & you will see Single Sing On login page present trough the iframe.


**Supporting Material/References:**

## Impact

Revealing confidential information(credentials) AND/OR taking control of their computer/account while clicking on seemingly innocuous web pages.

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
