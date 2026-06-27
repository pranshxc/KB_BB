---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '208719'
original_report_id: '208719'
title: Subdomain Takeover at Landing.udemy.com
weakness: Privilege Escalation
team_handle: udemy
created_at: '2017-02-24T21:02:45.710Z'
disclosed_at: '2017-03-30T04:09:01.874Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- privilege-escalation
---

# Subdomain Takeover at Landing.udemy.com

## Metadata

- HackerOne Report ID: 208719
- Weakness: Privilege Escalation
- Program: udemy
- Disclosed At: 2017-03-30T04:09:01.874Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Target:**  `Landing.udemy.com`

###Details: 

The target subdomain points to _unbounce.com_ service, via a _DNS CNAME_ record. As a result of this, an attacker could potentially initiate a subdomain takeover by registering the subdomain on unbounce.com.

Additionally, 

Unbounce is a custom 404-page hosting service, therefore leveraging its functionality an attacker can host custom HTML/Javascript webpage on the domain which will look very legitimate to the end-user and can be used to conduct large-scale phishing/XSS attacks.

###Proof of Concept:

CNAME Record:
>**Cname:**	unbouncepages.com
>**Name:**	landing.udemy.com
>**Type:**  CNAME
>**Class:**	IN
>**TTL:**	300

I did not proceed with the takeover, Contacting the support and confirming from them was more sensible.

{F163493}

###Remediation:

Remove the CNAME entry or claim the domain by signing up on unbounce.com

~Regards

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
