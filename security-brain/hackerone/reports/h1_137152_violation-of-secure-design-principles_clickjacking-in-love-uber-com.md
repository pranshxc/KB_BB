---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137152'
original_report_id: '137152'
title: Clickjacking in love.uber.com
weakness: Violation of Secure Design Principles
team_handle: uber
created_at: '2016-05-08T18:40:30.734Z'
disclosed_at: '2016-07-07T23:31:22.306Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Clickjacking in love.uber.com

## Metadata

- HackerOne Report ID: 137152
- Weakness: Violation of Secure Design Principles
- Program: uber
- Disclosed At: 2016-07-07T23:31:22.306Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi , 


Your domain love.uber.com is vulnerable to Clickjacking.

I'm able to load the domain love.uber.com in an iframe , 
so an attacker can certainly take advantage of this clickjacking bug in love.uber.com

Click-jacking is a process of “stealing” clicks on your site, redirecting them to other places,  by putting your page in an iframe and placing the attacker’s content over yours. The idea is to make this look as seamless as possible, so the user can’t tell right away that something is wrong.

if someone frames your site and puts login controls directly over yours, then even tools like SiteKey , won’t prevent them from collecting username and password data.

POC Screenshot Attached !

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
