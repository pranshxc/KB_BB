---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1220688'
original_report_id: '1220688'
title: Blind SSRF External Interaction on ████████
weakness: Server-Side Request Forgery (SSRF)
team_handle: mtn_group
created_at: '2021-06-08T19:36:59.706Z'
disclosed_at: '2022-08-21T08:40:51.584Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 49
asset_identifier: mtngbissau.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Blind SSRF External Interaction on ████████

## Metadata

- HackerOne Report ID: 1220688
- Weakness: Server-Side Request Forgery (SSRF)
- Program: mtn_group
- Disclosed At: 2022-08-21T08:40:51.584Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hii Security Team,

I am S █████(Metaxone Certified Ethical Hacker) and a Security Researcher I just checked your website and found Blind SSRF External Interaction on ██████████

What is SSRF?
Server-side request forgery (also known as SSRF) is a web security vulnerability that allows an attacker to induce the server-side application to make HTTP requests to an arbitrary domain of the attacker's choosing.
In typical SSRF examples, the attacker might cause the server to make a connection back to itself, or to other web-based services within the organization's infrastructure, or to external third-party systems.
SSRF attacks often exploit trust relationships to escalate an attack from the vulnerable application and perform unauthorized actions. These trust relationships might exist in relation to the server itself, or in relation to other back-end systems within the same organization.

Steps to reproduce:-

1.Navigate to the website █████
2.Now you can see at bottom on the right there is chat box or messanger box.
3.Click on it and paste the Burp Collaborator URL { Example : In this scenario the URL belike ██████ } and click on send
4.Now we will get HTTP and DNS interaction in Burp Collab and In HTTP requesting it is fetching the file ( test.png ) it means it is vulnerable to Blind SSRF

References:- Similar report which is reported by another researcher ███████

## Impact

Impact:--
This Vulnerability can lead to Attack Surface Analysis is about mapping out what parts of a system need to be reviewed and tested for security vulnerabilities.
The attacker can fetch malicious files which can infect the server
This will allow attackers to gain access to an internal IP of a website along with other sensitive information that may be leaked with the request

POC Attached Below :-

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
