---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '160981'
original_report_id: '160981'
title: Extracting private info of estimates.
weakness: Information Disclosure
team_handle: harvest
created_at: '2016-08-18T22:19:09.718Z'
disclosed_at: '2017-01-12T03:56:56.919Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- information-disclosure
---

# Extracting private info of estimates.

## Metadata

- HackerOne Report ID: 160981
- Weakness: Information Disclosure
- Program: harvest
- Disclosed At: 2017-01-12T03:56:56.919Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey there,
So when someone creates a new estimate for a client it is not accessible to anyone except the admin and the person with the private URL of the web invoice.
Now their is an option to convert estimate into invoice through ``` https://amandhakertest.harvestapp.com/invoices/new?estimate_id=ID_HERE``` through which an project manager can extract information about the private estimates of the project which he is assigned to.
If a user ( **PROJECT MANAGER** ) is not assigned to project **X** he cannot access any info of **X** .
If is not necessary to accept the payment for the attacker to perform this kind of attack & it will be helpful as a project manager cannot check the invoices made by the other so it is quite impossible to check into the estimates and it can also lead into accessing the private invoice created by the admin as if the admin or the client accepts the payment now he is asked to create invoice for the estimate and after creating it only he is allowed to access it but attacker can use this method and guess out what a admin would have created with the particular estimate.

Thanks.
Please let me know if you need any further assistance with.
God is great <3
Jai maa kali <3 jai maa saraswati <3 jai maa durga <3 jai maa bhawani <3 jai maa lakshmi <3 jai maa ganga <3 jai maa sita <3 jai maa vaishnodevi <3 jai shree ram <3 jai shree ganesha <3 jai shree krishna <3 jai shiv shambhu <3 jai shree shani dev <3 jai bajrang bali <3

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
