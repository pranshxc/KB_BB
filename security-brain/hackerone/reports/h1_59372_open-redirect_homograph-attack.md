---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '59372'
original_report_id: '59372'
title: Homograph Attack
weakness: Open Redirect
team_handle: security
created_at: '2015-05-03T02:26:42.169Z'
disclosed_at: '2015-05-09T12:39:31.193Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- open-redirect
---

# Homograph Attack

## Metadata

- HackerOne Report ID: 59372
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2015-05-09T12:39:31.193Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello HackerOne,

Fix of Report #29491 and #58612 is incomplete.
I found another way to to replicate homograph attack using Hex Code:

_www.%00ebаy.com_
_www.%01ebаy.com_
_www.%02ebаy.com_
_www.%03ebаy.com_
_www.%04ebаy.com_
_www.%05ebаy.com_
_www.%06ebаy.com_
_www.%07ebаy.com_
_www.%08ebаy.com_
_www.%0Bebаy.com_
_www.%0Cebаy.com_
_www.%0Eebаy.com_
_www.%0Febаy.com_
_www.%10ebаy.com_
_www.%1Aebаy.com_
_www.%1Bebаy.com_
_www.%1Cebаy.com_
_www.%1Debаy.com_
_www.%1Eebаy.com_
_www.%1Febаy.com_

Internationalized Domain Name or IDN are displayed in **Unicode** and there is no *encoding* into **Punycode** on external link warning page

Thanks,
@atom

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
