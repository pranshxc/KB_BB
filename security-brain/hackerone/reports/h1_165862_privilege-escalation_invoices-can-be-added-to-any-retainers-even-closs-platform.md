---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '165862'
original_report_id: '165862'
title: Invoices can be added to any retainers - even closs-platform
weakness: Privilege Escalation
team_handle: harvest
created_at: '2016-09-05T12:38:56.082Z'
disclosed_at: '2016-10-29T16:11:33.639Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- privilege-escalation
---

# Invoices can be added to any retainers - even closs-platform

## Metadata

- HackerOne Report ID: 165862
- Weakness: Privilege Escalation
- Program: harvest
- Disclosed At: 2016-10-29T16:11:33.639Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
------
Hey team,
there is an IDOR bug, which allows me to add an invoice to any retainer I wish, even if the retainer belongs to another app/subdomain.

Steps to reproduce
---------
1. Make sure you have two apps __A__ and **B**
2. In **A** create a retainer, let's say it has id `1234`.
3. In **B** open this link:
    https://SUBDOMAIN.harvestapp.com/invoices/new?invoice[client_id]=5678&invoice[kind]=retainer&invoice[retainer_id]=1234


    Here _5678_ needs to be a valid client id for account **B**. Then simply fill out the invoice form and save it.

4. Now in account **A** go to `https://[SUBDOMAIN].harvestapp.com/retainers/1234` and you will see that the invoice from account **B** was added to this retainer.

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
