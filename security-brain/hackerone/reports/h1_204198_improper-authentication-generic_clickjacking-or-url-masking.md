---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '204198'
original_report_id: '204198'
title: Clickjacking or URL Masking
weakness: Improper Authentication - Generic
team_handle: brave
created_at: '2017-02-07T13:33:57.940Z'
disclosed_at: '2017-08-10T05:10:43.866Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# Clickjacking or URL Masking

## Metadata

- HackerOne Report ID: 204198
- Weakness: Improper Authentication - Generic
- Program: brave
- Disclosed At: 2017-08-10T05:10:43.866Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I am able to reproduce the bug in :
Brave: 0.13.2 
rev: 25b1199fb6154b089cbad37926483239495b9800 
Muon: 2.0.19 
libchromiumcontent: 54.0.2840.100 
V8: 5.4.500.41 
Node.js: 7.0.0 
Update Channel: dev 
os.platform: win32 
os.release: 6.1.7601 
os.arch: x64

Steps to reproduce : 
1. Open click.html 
2. Then try to visit google.com 
OR 
http://hackies.in/click.html

Visually the browser says you(user) will be visiting google.com but it actually goes to 
datarift.blogspot.in 
An attacker may craft the link and may perform phishing attack or spoofing and etc.

Just do a mouseover on the link and see left bottom the URL says the browser will be visiting google.com but actually goes to datarift.blogspot.in 

In case if the repro doesn't works please perform the testcase 1 more time. 
Attaching the test case and the click.html file and Video POC for reference

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
