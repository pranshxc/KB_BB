---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '996122'
original_report_id: '996122'
title: Insufficient Session Expiration on Adobe Connect | https://█████████
weakness: Insufficient Session Expiration
team_handle: deptofdefense
created_at: '2020-10-01T20:51:32.134Z'
disclosed_at: '2021-06-03T16:34:46.568Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- insufficient-session-expiration
---

# Insufficient Session Expiration on Adobe Connect | https://█████████

## Metadata

- HackerOne Report ID: 996122
- Weakness: Insufficient Session Expiration
- Program: deptofdefense
- Disclosed At: 2021-06-03T16:34:46.568Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Due to lack of password protection and Insufficient Session Expiration I am able to brute force Adobe Connect meeting rooms. Many of the meeting rooms have chat history and files uploaded. Some of the chat history and files contains personal identifiable information.

Walkthrough Section:

1. To confirmed this vulnerability by first navigating to https://████

█████████

2. I then guessed a meeting room name such as ███████ 'https://████/████████'. The meeting requests a meeting ID which is proceed to test test

█████████

3. Then click on 'open in your browser'

██████

███

4. You are now in. Which is expected on normal occasions.. However... if you begin to notice.. These rooms are not expiring properly..

██████████

███

██████████

██████

5. Since the scale of meetings was large, i only selected a handful of meetings to search through which i provided chat logs and files. Also i have brute forced a total of 300+ meeting rooms. Some were locked some were open. I've provided a naming convention for the chat logs ███████.txt.

The handful:

Meeting with Certificates
https://███████/████████?proto=true

Meeting Personal Information
https://███████/███?proto=true

Meeting with Phone number ████
https://████/██████?proto=true

Meeting with interesting topic '██████'
https://███████/██████████?proto=true

Meeting with personal ██████████'
https://█████████/███████?proto=true

Meeting with phone number ██████████
https://████/███?proto=true

Meeting with '█████████'
https://███████/█████?proto=true

Meeting with '██████████'
https://█████/████████?proto=true

Not sure if the presented data is test data or real data.
https://█████████/███████

Meeting with '███████  Code: █████████ ████████  Code: ████#'
https://█████/███?proto=true

Meeting with '███'
https://██████████/████████?proto=true

## Impact

An attacker can use this information for malicious intentions such as blackmailing, phishing/spear phishing. This vulnerability puts military staff at risk.

## Step-by-step Reproduction Instructions

For steps on reproducing please follow the walkthrough section above.

## Product, Version, and Configuration (If applicable)
Adobe Connect

https://███████/version.txt

## Suggested Mitigation/Remediation Actions

If you have a SIEM that ingests adobe connect logs you may need to review the connections to check for any potential unauthorized access.

Enforce a setting in which all Adobe Connect users are forced to apply a meeting password might be the best option. This will also avoid people from invading into meetings such as teams and zoom bombings.

## Impact

An attacker can use this information for malicious intentions such as blackmailing, phishing/spear phishing. This vulnerability puts military staff at risk.

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
