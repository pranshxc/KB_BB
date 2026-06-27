---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1342422'
original_report_id: '1342422'
title: Subdomain Takeover due to ████████ NS records at us-east4.37signals.com
weakness: Information Disclosure
team_handle: basecamp
created_at: '2021-09-17T10:50:58.838Z'
disclosed_at: '2021-09-17T21:45:28.908Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 73
tags:
- hackerone
- information-disclosure
---

# Subdomain Takeover due to ████████ NS records at us-east4.37signals.com

## Metadata

- HackerOne Report ID: 1342422
- Weakness: Information Disclosure
- Program: basecamp
- Disclosed At: 2021-09-17T21:45:28.908Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description
 
 Hi!
 I have discovered that  us-east4.37signals.com was pointing to an unclaimed ████ NS zone and I've managed to claim it in my account.
 
 ##POC
 
 http://nagli.us-east4.37signals.com/takeover.html
 

{F1451587}


 ## Remediation
 Make sure to configure the DNS records under us-east4.37signals.com
 
Best regards,
@ nagli

## Impact

Subdomain takeovers can be used for
 Account takeovers (cookies set to .█████████ will be shared with this subdomain and can be obtained)
 Stored XSS (arbitrary javascript code can be executed in a users browser)
 Phishing
 Hosting malicious content

Since you cannot control the content hosted on the site, your brand is at risk of being damaged.
Additionally, the vulnerabilities in these sites, such as XSS, RCE, etc could put your sites/users at risk of attack, since they would occur on your domain.

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
