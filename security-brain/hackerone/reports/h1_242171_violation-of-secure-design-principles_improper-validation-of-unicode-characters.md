---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '242171'
original_report_id: '242171'
title: Improper validation of unicode characters
weakness: Violation of Secure Design Principles
team_handle: weblate
created_at: '2017-06-21T19:43:02.301Z'
disclosed_at: '2017-08-19T05:47:06.499Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Improper validation of unicode characters

## Metadata

- HackerOne Report ID: 242171
- Weakness: Violation of Secure Design Principles
- Program: weblate
- Disclosed At: 2017-08-19T05:47:06.499Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I just saw a report of #229483

This issue still persist. When i tried some Unicode characters like smilies etc. It is working perfectly by displaying the Error message on the same page that **Username may only contain letters, numbers or the following characters: @ . + - _**

See 1.jpg for smilies handling (Expected)
See 2.jpg for other Unicode characters (Not handled correctly)

But when i put some other unicode charachters like  👨‍👩‍👧‍👦

1. Copy this  👨‍👩‍👧‍👦
2. Put in the username field and save.
3. Following Error will be displayed. 
It still showing the same error as in previous report. 

```

Server Error
The server had serious problems while serving your request. We've just sent our trained monkeys to fix the issue.

```
Please check.

Thanks,
Akash Saxena

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
