---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1131887'
original_report_id: '1131887'
title: CSV injection in the credentials export
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2021-03-21T18:11:36.375Z'
disclosed_at: '2021-09-22T19:33:42.956Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# CSV injection in the credentials export

## Metadata

- HackerOne Report ID: 1131887
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2021-09-22T19:33:42.956Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello team!

We have found out that a hacker can inject malicious excel formulas into the credentials details which will be executed when program user exports the credentials details via `https://hackerone.com/hackerone_h1p_bbp3/credentials` -> export credentials and opens this CSV using MS excel. This how an attacker could execute abritary commands in the program user's windows machines throught the malicious CSV files. However, since this attack vector requires an older windows machine the impact is pretty low so we decided to report this as best practice instead of vulnerabilitys (severity none).

## Steps To Reproduce:

- Login to the system as a program user
- Add credentials to the program at `https://hackerone.com/hackerone_h1p_bbp3/credentials`
- Now login as a hacker user of this program and request your credentials using *show credentials* button
- Set value of the account details to the `;=1+1;`
- As a program user navigate to the `https://hackerone.com/hackerone_h1p_bbp3/credentials` and export the credentials

Note: The program user does not see the account details in this phase so s/he won't expect anything harmless.

- Once you open the CSV in the MS excel the formula has been executed and there is a new cell with value `2` instead of `;=1+1`
 

## Recommendation:

Make sure that the payload can't start with the following characters: `;`, `=`, `-`, `@` or `+`.

 

## References:

`https://owasp.org/www-community/attacks/CSV_Injection`

## Impact

Possible command execution in the victim's windows machines

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
