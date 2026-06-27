---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1127455'
original_report_id: '1127455'
title: Hackers can reveal the names of private programs that have an external link
weakness: Information Disclosure
team_handle: security
created_at: '2021-03-16T20:18:41.101Z'
disclosed_at: '2021-08-24T03:20:25.898Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 16
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Hackers can reveal the names of private programs that have an external link

## Metadata

- HackerOne Report ID: 1127455
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2021-08-24T03:20:25.898Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Hi team,

Our team has found a way to distinguish between private programs with external links. Due to the ability to select Severity Rating Options, the program can set two options : `Rating or CVSS Score` and `CVSS Score Only`. One of them removes the possibility of setting the severity(directly). Since no one can do this in sandbox programs, and both options are set by default, this difference allows us to understand that the changes were made by the program administrator. This means that the program has control, and therefore a private part

 

## Steps To Reproduce:

1. Create new account( Ideally)
2. Go to https://hackerone.com/hacktivity/publish
3. Input Program - :handle: external program
4. Other fields - **test** and click create report
5. After, You need to click on the severity button 

{F1233314}
6. Looking at a possible variation of the severity setting

7. If we have only one option, then the program has a private part
{F1233318}
 

## Recommendation:

We believe that at the end of the check, for the `severity_options` attribute, we need to create a check for whether the report belongs to the `is_published` attribute, and if it is set to `true`, then always set `severity_options` to the `rating_and_cvss` value

## Impact

Hackers can reveal the names of private programs that have an external link

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
