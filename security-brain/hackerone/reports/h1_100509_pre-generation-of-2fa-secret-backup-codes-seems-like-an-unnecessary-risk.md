---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '100509'
original_report_id: '100509'
title: Pre-generation of 2FA secret/backup codes seems like an unnecessary risk
team_handle: security
created_at: '2015-11-19T16:06:20.160Z'
disclosed_at: '2015-12-02T05:09:10.288Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
---

# Pre-generation of 2FA secret/backup codes seems like an unnecessary risk

## Metadata

- HackerOne Report ID: 100509
- Weakness: 
- Program: security
- Disclosed At: 2015-12-02T05:09:10.288Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

If you manage to get a malicious script running in HackerOne, requesting `https://hackerone.com/settings/authentication/edit` and parsing out the two factor authentication form will yield either… 

- the 2FA secret key and backup codes that *will* be used if 2FA is enabled for the first time this session
- the backup codes that *will* be used if 2FA is already being used and the codes are regenerated during this session

While *activating* 2FA or *confirming* backup codes regeneration requires knowledge of the user's password/TOTP code, reading the values out from the DOM does not (again, provided that you've compromised the user's session and are running script in their domain)

A theoretical attack might play out like this:

- A victim clicks a link or something in HackerOne which triggers XSS (which seems unlikely, but …)
- The XSS makes a request to `https://hackerone.com/settings/authentication/edit` to obtain the victim's potential 2FA secret and backup codes.  Possibly the attacker is able to abuse a password manager's behavior to obtain the victim's username/password at this point.
- Because of the strange behavior that occurred when they clicked the link, the victim possibly closes and re-opens the window (in an attempt to stop whatever the script is doing) and then enables 2FA on their account
- The attacker would now know the 2FA secret and backup codes that are currently being used for the victim's account

While achieving this attack seems rather unlikely, it seems that it could be mitigated by not generating the 2FA values until the user is trying to enable 2FA or generate their codes and has provided their password (and then generating new codes each time, regardless of whether the process was cancelled previously)

(Also, I was somewhat surprised to see that the `https://hackerone.com/settings/authentication/edit` form contained a 2FA secret/backup codes for users that aren't allowed to set up two factor authentication.)

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
