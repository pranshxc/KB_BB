---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1159371'
original_report_id: '1159371'
title: '[www.█████] Path-based reflected Cross Site Scripting'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-04-09T18:10:16.529Z'
disclosed_at: '2022-04-07T20:08:56.113Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [www.█████] Path-based reflected Cross Site Scripting

## Metadata

- HackerOne Report ID: 1159371
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-04-07T20:08:56.113Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
The `www.██████` endpoint is vulnerable to path-based reflected XSS which allows attackers to pass rogue JavaScript to unsuspecting users.

## Impact

This flaw allows attackers to pass rogue JavaScript to unsuspecting users. Since the user’s browser has no way to know the script should not be trusted, it will execute the script, which can then access any cookies, session tokens, or other sensitive information retained by the browser and used with your website. In fact, here is a list of 21 other things that hackers can do with an XSS flaw: https://s0md3v.github.io/21-things-xss/

## System Host(s)
www.██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit `https://www.█████████/███/"><script>alert(document.domain)</script>`

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
