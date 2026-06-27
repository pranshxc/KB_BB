---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '459634'
original_report_id: '459634'
title: GitHub users outside of HackerOne organization can create and update Wiki pages
  of certain public HackerOne repositories
weakness: Phishing
team_handle: security
created_at: '2018-12-10T13:15:50.535Z'
disclosed_at: '2018-12-12T17:35:47.433Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- phishing
---

# GitHub users outside of HackerOne organization can create and update Wiki pages of certain public HackerOne repositories

## Metadata

- HackerOne Report ID: 459634
- Weakness: Phishing
- Program: security
- Disclosed At: 2018-12-12T17:35:47.433Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary**
Hi HackerOne team,
recently this vulnerability have been reported and resolved in various programs, so I'm going to try my bad luck, reporting the same kind of report also in this program.

**Steps**
1. Go on https://github.com/Hacker0x01/react-datepicker/wiki/BB-test
2. I've created a simple page in the wiki without be a collaborator of the repo, or and without any permission
3. Going on https://github.com/Hacker0x01/react-datepicker/wiki/ you can add a new `fake` or `phishing` page clicking on the `New page` or `edit` buttons.
4. {F388246}

**PS**
First of all, 
I'm not sure that this type of issue is allowed on your program, but seeing the following report (https://hackerone.com/reports/457009) seem that is quite accepted by anyone, so I will try my luck (I'm going to fail, I know lol).
I know also that the impact isn't interesting, but as I said previously, let me try :)

## Impact

Add and edit pages in the `wiki` of the https://github.com/Hacker0x01/react-datepicker/ repo

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
