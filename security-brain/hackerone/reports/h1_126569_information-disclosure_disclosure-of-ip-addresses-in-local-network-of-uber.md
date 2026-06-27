---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126569'
original_report_id: '126569'
title: Disclosure of ip addresses in local network of uber
weakness: Information Disclosure
team_handle: uber
created_at: '2016-03-28T19:32:54.628Z'
disclosed_at: '2016-06-13T22:22:56.071Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Disclosure of ip addresses in local network of uber

## Metadata

- HackerOne Report ID: 126569
- Weakness: Information Disclosure
- Program: uber
- Disclosed At: 2016-06-13T22:22:56.071Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi, i have found several DNS records at Google DNS server 8.8.8.8 pointing to Uber local servers:

```
▶ nslookup logs.uber.com
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	logs.uber.com
Address: 10.6.0.1
```

```
▶ nslookup kerberos.uber.com
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	kerberos.uber.com
Address: 10.6.0.74
```

```
▶ nslookup ldap.uber.com
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	ldap.uber.com
Address: 10.30.14.3
```

This information could be used, if attacker gets SSRF,XXE,LFI etc in order to address local network of Uber.

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
