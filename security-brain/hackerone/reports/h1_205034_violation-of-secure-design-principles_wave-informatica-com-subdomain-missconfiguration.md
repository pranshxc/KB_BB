---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '205034'
original_report_id: '205034'
title: '[wave.informatica.com]- Subdomain missconfiguration'
weakness: Violation of Secure Design Principles
team_handle: informatica
created_at: '2017-02-09T18:11:17.002Z'
disclosed_at: '2017-02-19T14:26:36.778Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# [wave.informatica.com]- Subdomain missconfiguration

## Metadata

- HackerOne Report ID: 205034
- Weakness: Violation of Secure Design Principles
- Program: informatica
- Disclosed At: 2017-02-19T14:26:36.778Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

One of your subdomain https://wave.informatica.com has a CNAME record that resolved to ghs.google.com and shows 404 error when navigating to subdomain. You should remove CNAME entry for that subdomain pointing towards ghs.google.com. Although I couldnt verify the domain ownership process to fully takeover subdomain but it still possess thread in a sense that anyone can claim gsuite account using https://wave.informatica.com subdomain.For sake of poc I claim gsuite account with your subdomain name as shown in picture3. I will remove it if you want.
THREAD:
This could potentially prevent informatica from using services such as Google Drive, GMail, and Google Calendar with that particular subdomain.
POSSIBLE FIX:
To fully resolve the issue you need to remove the CNAME record and put in place a web forwarding rule for wave.informatica.com towards  new web landing page

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
