---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '275515'
original_report_id: '275515'
title: Stored XSS in dev-ucrm-billing-demo.ubnt.com In Client Custom Attribute
weakness: Cross-site Scripting (XSS) - Stored
team_handle: ui
created_at: '2017-10-08T15:38:12.215Z'
disclosed_at: '2017-12-30T13:26:58.038Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in dev-ucrm-billing-demo.ubnt.com In Client Custom Attribute

## Metadata

- HackerOne Report ID: 275515
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: ui
- Disclosed At: 2017-12-30T13:26:58.038Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,

Was Testing the subdomins when I came Accross the subdomain https://dev-ucrm-billing-demo.ubnt.com/ I logged in as an Administrator and while testing i added a User and In Client Custom Attribute 1 i added the Payload: `"><IMG src=x onerror=prompt(1);>"">><marquee><img src=x onerror=confirm(3)></marquee>"/` and Save the Client and Then on client page i.e: https://dev-ucrm-billing-demo.ubnt.com/client/24 When User click on Show more (under Custom Attribute 1) The XSS payload executes :) 

{F227283}

{F227284}

If another Admin or A user will perform the steps to see the custo atributes his/her account can be takenover By Such Pentest XSS By using tools like https://xsshunter.com/app etc :)

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
