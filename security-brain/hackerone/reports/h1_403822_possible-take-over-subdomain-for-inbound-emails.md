---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '403822'
original_report_id: '403822'
title: Possible Take Over Subdomain For Inbound Emails
team_handle: khanacademy
created_at: '2018-09-01T12:43:59.247Z'
disclosed_at: '2018-11-08T20:19:27.954Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
---

# Possible Take Over Subdomain For Inbound Emails

## Metadata

- HackerOne Report ID: 403822
- Weakness: 
- Program: khanacademy
- Disclosed At: 2018-11-08T20:19:27.954Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello KhanAcademy Security Team,

I'm **rootbakar**, The researcher identified that the affected url points to sendgrid.net, via a DNS CNAME record. As a result of this an attacker could potentially initate a subdomain take over by registering the subdomain sendgrid.khanacademy.org on sendgrid and consiquently leverage this for further attacks. Additionally it has been noted that sendgrid is a service for email marketing so theoretically should an attacker be able to gain access to the subdomain they could potentially gain access to emails too.


###Affected URLs
sendgrid.khanacademy.org

###Risk Breakdown
Risk: **Medium**
Difficulty to Exploit: **Medium** 
Authentication: None

###Recommended Fix
Check your DNS-configuration for subdomains pointing to services not in use.
Set up your external service so it fully listens to your wildcard DNS.


###Reference
https://www.hackerone.com/blog/Guide-Subdomain-Takeovers
http://blog.pentestnepal.tech/post/149985438982/reading-ubers-internal-emails-uber-bug-bounty
https://hackerone.com/reports/166826

## Impact

**a way to take over subdomain for inbound emails**

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
