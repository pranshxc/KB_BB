---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1536899'
original_report_id: '1536899'
title: HTML Injection in E-mail
team_handle: acronis
created_at: '2022-04-10T21:52:52.711Z'
disclosed_at: '2022-06-14T10:21:46.411Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 49
asset_identifier: account.acronis.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# HTML Injection in E-mail

## Metadata

- HackerOne Report ID: 1536899
- Weakness: 
- Program: acronis
- Disclosed At: 2022-06-14T10:21:46.411Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Gents,
+ While testing "account.acronis.com", I found that "first name" could be injected with HTML tags while sending an email invitation. But this attack requires user interaction to confirm the email first, then he/she will receive a welcome email "Welcome to your Acronis Cyber Protect trial!" Contains the injected payload!

### Steps to Reproduce:
1. Please register at https://www.acronis.com/en-us/products/cyber-protect/trial/#registration with the victim's email.
2. Inject "First Name" field with HTML tags, for example: `"/><img src="x"><a href="https://evil.com">login</a>`.
3. Check the email inbox, HTML tags will be executed. "Your Acronis Cyber Protect trial starts today!"

### Proof of Concept:
+ {F1687466}

## Impact

HTML Injection

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
