---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '411930'
original_report_id: '411930'
title: User with privilege to maintain External Programs can update certain churned
  HackerOne programs
weakness: Improper Authorization
team_handle: security
created_at: '2018-09-20T19:53:35.226Z'
disclosed_at: '2018-10-25T18:47:02.288Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
tags:
- hackerone
- improper-authorization
---

# User with privilege to maintain External Programs can update certain churned HackerOne programs

## Metadata

- HackerOne Report ID: 411930
- Weakness: Improper Authorization
- Program: security
- Disclosed At: 2018-10-25T18:47:02.288Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
You wrote that some programs are behind, but you are trying to get them back (sorry maybe bad translation)

**Description:**
Apparently because of a system error, I have access to change information in the public program.
This option is given only for external programs.But here is a public program, so I create a report

### Steps To Reproduce

1. Go to @uzbey -- https://hackerone.com/uzbey
2. I can see button `edit`
F348953
3. Try to change `about`
4. I write -- `test @jobert`
F348952

Check about page
`The goal of Uzbey is to create the worlds largest selfie to be launched into space. test @jobert`
Hi @jobert :)


PS I understand that this is an old program, but it has the ability to return. Perhaps there are still such programs.I'm still searching. If I understood something wrong, then close the report as information, thank you!

fix: to change the program state

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

## Impact

Change fields:

`Website`
`Twitter handle`
`About`
`Cover color`
and i think , i can change `logo` ?
in public(public_mode) programs

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
