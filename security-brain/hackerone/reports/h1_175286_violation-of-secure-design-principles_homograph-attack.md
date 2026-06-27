---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175286'
original_report_id: '175286'
title: Homograph attack
weakness: Violation of Secure Design Principles
team_handle: brave
created_at: '2016-10-12T04:25:35.756Z'
disclosed_at: '2016-10-14T18:15:01.305Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- violation-of-secure-design-principles
---

# Homograph attack

## Metadata

- HackerOne Report ID: 175286
- Weakness: Violation of Secure Design Principles
- Program: brave
- Disclosed At: 2016-10-14T18:15:01.305Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

when we add a site to our **Homepage**, it's not validate a url properly, make sure it's display the **punycode.**

## Products affected: 

 * Brave 0.12.4 (Tested on mac os)

## Steps To Reproduce:

 * In browser add homepage with IDN  http://ebаy.com/
 * now close and open browser again
 * you can see it's redirect to http://xn--eby-7cd.com/

## References:

  * https://hackerone.com/reports/29491

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
