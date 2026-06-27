---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '228383'
original_report_id: '228383'
title: IDOR on DoD Website exposes FTP users and passes linked to all accounts!
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2017-05-14T21:23:33.371Z'
disclosed_at: '2019-10-04T15:21:57.473Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR on DoD Website exposes FTP users and passes linked to all accounts!

## Metadata

- HackerOne Report ID: 228383
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2019-10-04T15:21:57.473Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
https://████/██████/ is vulnerable to Insecure Direct Object Reference. The application does not validate whether or not who a Push Server belongs to thus allowing an attacker to view the credentials of any FTP / sFTP server linked to any user's account. 

## Impact
An attacker can view anybody's FTP server information, thus **compromising** the user's FTP servers. This also allows an attacker to **update** or **edit** the Push Server in the ██████████ CMS.

## Step-by-step Reproduction Instructions
1. Log into or create an account on `https://██████████/██████████`
2. Now visit `https://████████/█████/filepush/ftp/303/` 

You will be able to see my ftp server details and you will be able to update or delete it!

An attacker can bruteforce the id to see if the server gives back a valid response. The attacker can then log into the person's FTP servers with the credentials stolen using this vulnerability, giving them full access to private / confidential information!

Example: `https://██████████/█████████/filepush/ftp/1/`

Hostname: ██████
Username: ██████
Password: █████
Path: /from_pub/cr/████████

`https://█████████/████/filepush/ftp/<ID>/`

## Suggested Mitigation/Remediation Actions
Check whether or the user's account should have access to the specified Push Server

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
