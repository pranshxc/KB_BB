---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226199'
original_report_id: '226199'
title: Changing Victim's JIRA Integration Settings Through Multiple Bugs
weakness: Business Logic Errors
team_handle: security
created_at: '2017-05-04T21:13:14.346Z'
disclosed_at: '2017-05-23T02:41:49.893Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
tags:
- hackerone
- business-logic-errors
---

# Changing Victim's JIRA Integration Settings Through Multiple Bugs

## Metadata

- HackerOne Report ID: 226199
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2017-05-23T02:41:49.893Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Changing victim's JIRA integration settings through multiple bugs.

**Description:**

Using multiple HackerOne bugs, an attacker can change the victim's JIRA integration settings.

### Bugs:

###1) The Jira integration consent screen lacks information about the Jira project that will be connected to HackerOne

{F181926}
***Malicious or good Jira trying to connect above?***
Impossible to know without clicking on `Link JIRA Instance to program`, this is bad.

###2) JIRA project automatic selection

When a user already have a JIRA connected to his HackerOne program, if an attacker sends 
a malicious link to him (with a malicious JIRA JWT token in it), clicking on `Link JIRA Instance to program` will change the JIRA account connected to the program and worst, it will automatically select the attacker's JIRA project without user interaction. Any new HackerOne report will be cloned to the attacker's JIRA project.

###3) Bypassing HackerOne link protection

[Link protection bypass](https://hackerone.com/users/%2E/saml/sign_in?email=teste@hackerone.com)

###4) HackerOne SAML Open Redirector ( #171398 )

###5) Jira OAuth CSRF

{F181925}

{F181924}

### Conclusion:

An attacker can use all bugs above in many ways to try to link his own JIRA project to the victim's HackerOne program.

### Optional: Supporting Material/References (Screenshots)

 * Video #1 (bugs #1 and #2 demonstration): ████████
 * Video #2 (bug #5 demonstration): █████

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
