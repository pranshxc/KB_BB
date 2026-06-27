---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '843421'
original_report_id: '843421'
title: Hyperlink Injection on Email Invitation
weakness: Open Redirect
team_handle: helium
created_at: '2020-04-08T17:57:42.830Z'
disclosed_at: '2020-11-24T15:08:32.808Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: https://helium-console-dev.herokuapp.com/
asset_type: URL
max_severity: high
tags:
- hackerone
- open-redirect
---

# Hyperlink Injection on Email Invitation

## Metadata

- HackerOne Report ID: 843421
- Weakness: Open Redirect
- Program: helium
- Disclosed At: 2020-11-24T15:08:32.808Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#DESCRIPTION
Found an hyperlink injection of the name of Organization when the attacker invites the victim to his organization with injection hyperlink.

#STEPS
1. Add organization with the name of https://attacker.com and switch it.
2. Go to user and invite the victim using email.
3. victim will seee the invitation with malicious link

#POC IMAGE

* Add organization name as https://attacker.com

{F779678}

* Go to user and invite someone and the victim will see the invitation

{F779676}

* accepted invitation for already registered

{F779677}

## Impact

Open Redirect from hyperlink injection to malicious website.

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
