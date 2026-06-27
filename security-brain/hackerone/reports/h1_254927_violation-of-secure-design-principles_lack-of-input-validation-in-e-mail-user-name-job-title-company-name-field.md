---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '254927'
original_report_id: '254927'
title: Lack of input validation in e-mail & user name, job title, company name field
weakness: Violation of Secure Design Principles
team_handle: legalrobot
created_at: '2017-07-30T09:59:47.545Z'
disclosed_at: '2017-07-31T02:48:01.721Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- violation-of-secure-design-principles
---

# Lack of input validation in e-mail & user name, job title, company name field

## Metadata

- HackerOne Report ID: 254927
- Weakness: Violation of Secure Design Principles
- Program: legalrobot
- Disclosed At: 2017-07-31T02:48:01.721Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,
During sign up input validation didn't deploy properly on e-mail & name field. I've tested inputing following e-mail during sign up:
``hacker~%@gmail.com``
Your system send email to verification the account though the e-mail address is invalid as gmail doesn't allow user to sign up using special characters like ``%,~``  etc.
{F208264}
Another issue is during sign up name field & from account profile edit option name feild, job title, company name field also failed to validate user input and accept special characters like ``$, %, ~,!,{}  ``.  I've tested this using my account ``kazishaheb.me@gmail.com``
{F208268}
{F208270}

Hope you'll deploy a quick fix. I look forward to hear backck from you, thank you!

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
