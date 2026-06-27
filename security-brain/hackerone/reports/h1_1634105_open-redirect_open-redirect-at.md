---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1634105'
original_report_id: '1634105'
title: Open Redirect at █████
weakness: Open Redirect
team_handle: deptofdefense
created_at: '2022-07-12T06:06:11.564Z'
disclosed_at: '2022-11-18T18:37:37.835Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- open-redirect
---

# Open Redirect at █████

## Metadata

- HackerOne Report ID: 1634105
- Weakness: Open Redirect
- Program: deptofdefense
- Disclosed At: 2022-11-18T18:37:37.835Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Open Redirect on https://███

User can be redirect to malicious site
POC: ████████/texis/search/redir.html?query=1234&pr=External+Meta&prox=page&rorder=500&rprox=500&rdfreq=500&rwfreq=250&rlead=500&rdepth=62&sufs=3&order=r&u=http://evil.com&m=0&p=2

I hope you know the impact of open redirect and more info refer

https://cwe.mitre.org/data/definitions/601.html

## Impact

User can be redirect to malicious site.

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Just open:  █████/texis/search/redir.html?query=1234&pr=External+Meta&prox=page&rorder=500&rprox=500&rdfreq=500&rwfreq=250&rlead=500&rdepth=62&sufs=3&order=r&u=http://evil.com&m=0&p=2

Vulnerable parameter: u=

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
