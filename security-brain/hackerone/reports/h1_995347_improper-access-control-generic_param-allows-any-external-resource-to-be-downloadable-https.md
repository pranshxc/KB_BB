---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '995347'
original_report_id: '995347'
title: param allows  any external resource to be downloadable | https://████████
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2020-10-01T04:20:06.041Z'
disclosed_at: '2021-03-11T20:59:16.737Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-access-control-generic
---

# param allows  any external resource to be downloadable | https://████████

## Metadata

- HackerOne Report ID: 995347
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2021-03-11T20:59:16.737Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
The following param allows an attacker to trick people into downloading malicious files, scripts and other payloads.

https://██████████?url=https://<MaliciousURL>

PoC

1. I will show you how the page looks normally without any changes. If you directly access https://███ you will be shown the following page. You can click on 'Click to download' but nothing happens.

█████

2. I replace the download param with the url param and entered my attacking vps server ip address as the URL and execute.

█████

3. On my attacking vps server (The black console) you can see that i have received the request from my personal computers ip address showing that it is 100% possible to perform this attack.

https://██████████?url=https://████/poc

████████

## Impact
If an attacker abuses this vulnerability he/she will be able to compromise accounts, computers and identities of people. Potentially Military staff if the attacker had bad intentions.

## Step-by-step Reproduction Instructions

1. Navigate to https://███████
2. Click on 'Click to download'
3. Replace download with url
4. Type in a url and click download

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions
Dev needs to add validation to the url param so that it doesn't allow external resources to be downloadable.

Resources:

The only article i can find pertaining to this type of vulnerability

https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html

## Impact

If an attacker abuses this vulnerability he/she will be able to compromise accounts, computers and identities of people. Potentially Military staff if the attacker had bad intentions.

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
