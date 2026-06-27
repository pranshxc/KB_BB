---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '228648'
original_report_id: '228648'
title: WannaCrypt “Killswitch”
team_handle: security
created_at: '2017-05-13T12:00:00.000Z'
disclosed_at: '2017-05-13T12:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 801
tags:
- hackerone
---

# WannaCrypt “Killswitch”

## Metadata

- HackerOne Report ID: 228648
- Weakness: 
- Program: security
- Disclosed At: 2017-05-13T12:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

WannaCrypt (a.k.a. WannaCry) is the name of a malware used in the May 2017 global ransomware attack targeting Microsoft Windows operating systems via known vulnerabilities leaked by The Shadow Brokers. 

In MalwareTech’s research, it was found that the malware sends an HTTP request to a seemingly random domain name in the early stages of its execution. If the HTTP call fails, the malware encrypts the user’s files, requests ransom, and will spread to other vulnerable machines. If the HTTP call is successful, the malware exits, halting encrypting files and spreading itself.

Malware Tech also discovered that the domain name used in the malware’s HTTP request was available for sale and was able to register it. The malware relied on the domain name being unregistered so the HTTP call would always fail and it would continue to spread. By registering the domain name, it was possible to make the malware’s HTTP call return successfully. This resulted in the malware exiting early on new infections and effectively stopped this variant of the malware from spreading further.

Original disclosure: https://www.malwaretech.com/2017/05/how-to-accidentally-stop-a-global-cyber-attacks.html

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
