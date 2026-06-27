---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '318295'
original_report_id: '318295'
title: clickjacking to Semrush auth login
weakness: UI Redressing (Clickjacking)
team_handle: semrush
created_at: '2018-02-21T17:57:55.777Z'
disclosed_at: '2018-03-13T14:25:36.732Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- ui-redressing-clickjacking
---

# clickjacking to Semrush auth login

## Metadata

- HackerOne Report ID: 318295
- Weakness: UI Redressing (Clickjacking)
- Program: semrush
- Disclosed At: 2018-03-13T14:25:36.732Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Description:
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on. this attack could be perform to semrush auth user because its direct popup for geo.semrush.com login.

Steps To Reproduce:
Create HTML file containg following code:
<iframe src="https://geo.semrush.com/"></iframe>
Execute the HTML file & you will see Single Sing On login page present trough the iframe.

## Impact

Revealing confidential information(credentials) AND/OR taking control of their computer/account while clicking on seemingly innocuous web pages.

The hacker selected the **UI Redressing (Clickjacking)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://geo.semrush.com/

**Can a victim be tricked into unknowingly initiating a specific action?**
Yes

**What specific action can the user be tricked into?**
semrush auth login could be hack

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
