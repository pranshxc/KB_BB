---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '484420'
original_report_id: '484420'
title: Subdomain takeover on usclsapipma.cv.ford.com
weakness: Privilege Escalation
team_handle: ford
created_at: '2019-01-23T05:09:30.817Z'
disclosed_at: '2019-03-24T23:26:15.015Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 99
asset_identifier: '*.ford.com'
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover on usclsapipma.cv.ford.com

## Metadata

- HackerOne Report ID: 484420
- Weakness: Privilege Escalation
- Program: ford
- Disclosed At: 2019-03-24T23:26:15.015Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Ford H1 team,

I want to report a Subdomain takeover vulnerability in this report, a pretty serious security issue in some context.

##Overview:
One of the ford.com subdomains is pointing to Azure, which has unclaimed CNAME record. ANYONE is able to own ford.com subdomain at the moment.

This vulnerability is called subdomain takeover. You can read more about it here:

https://blog.sweepatic.com/subdomain-takeover-principles/
https://labs.detectify.com/tag/hostile-subdomain-takeover/
https://hackerone.com/reports/325336

##Details:
usclsapipma.cv.ford.com has CNAME usclsapipma.trafficmanager.net wich has a CNAME to feuscspma3fcvapi.eastus.cloudapp.azure.com. However, feuscspma3fcvapi.eastus.cloudapp.azure.com is not registered in Azure cloudapp Virtual machine anymore and thus can be registered as FQDN for a easus VM by anyone. After registering the Cloud App Virtual Machine in Azure portal, the person doing so has full control over traffic on dynatraceppeast01.cf.ford.com (so, not only HTTP/HTTPS but also mails traffic, etc, since we have full control over the virtual machine and it's OS).

##Mitigation:
Remove the CNAME record from ford.com DNS zone completely.
OR
Claim it back in Azure portal

##Files : 
Azure-check-availability.png -> Screenshot of the Azure website api "check availability" for the "eastus" cloudapp virtual machine. on the link, you can see the location "eastus" part of the fqdn ad the DomainNameLabel "feuscspma3fcvapi" part of the FQDN, and the "available : true" response for this fqdn.
dns-proof.png -> Result of a "dig" command for this domains, showing the "NXDOMAIN" reponse for the CNAME entry of the ford subdomain.

Cheers,

March_42

## Impact

Subdomain takeover can be abused to do several things like :

Malware distribution
Phishing / Spear phishing
XSS
Authentication bypass
Legitimate mail sending and receiving on behalf of ford subdomain
...
List goes on and on.

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
