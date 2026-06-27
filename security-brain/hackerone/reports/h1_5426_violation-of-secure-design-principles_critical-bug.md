---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '5426'
original_report_id: '5426'
title: CRITICAL BUG!
weakness: Violation of Secure Design Principles
team_handle: msdos
created_at: '2014-04-01T00:36:43.743Z'
disclosed_at: '2014-04-01T17:13:51.670Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# CRITICAL BUG!

## Metadata

- HackerOne Report ID: 5426
- Weakness: Violation of Secure Design Principles
- Program: msdos
- Disclosed At: 2014-04-01T17:13:51.670Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

CRITICAL BUG!

If you type in color followed by a space and 2 numbers it can potentially render the screen unreadable! So far, my extensive testing has led me to find that certain letters work as well, though without a real pattern I'm not sure which ones. So far I know the letters "AF" will render a color change. 

I know this bug seemed to appear in later versions than are included in the bounty, but I thought you should be aware...

My proposed fix is to not type in color followed by any letters or numbers. For extra security, I have initiated a command told to me by a friend, "del *.*". I don't know if this will have any effect but I will report back once the command finis

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
