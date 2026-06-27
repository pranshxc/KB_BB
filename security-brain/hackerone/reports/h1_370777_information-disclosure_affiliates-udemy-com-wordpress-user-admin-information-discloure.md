---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '370777'
original_report_id: '370777'
title: '[affiliates.udemy.com] Wordpress user admin information discloure'
weakness: Information Disclosure
team_handle: udemy
created_at: '2018-06-25T08:36:27.771Z'
disclosed_at: '2019-04-28T06:33:07.115Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 57
tags:
- hackerone
- information-disclosure
---

# [affiliates.udemy.com] Wordpress user admin information discloure

## Metadata

- HackerOne Report ID: 370777
- Weakness: Information Disclosure
- Program: udemy
- Disclosed At: 2019-04-28T06:33:07.115Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary
This website using Wordpress CMS, so developer forget to disable the link that can view information of admin user.
By access to this link, attacker can get all username and other information of user admin:
> http://affiliates.udemy.com/wp-json/wp/v2/users

{F312155}

Admin user list:
* hamza
* imanrana
* nupoora

## Impact

With this vulnerability, attacker can get username of user admin and only brute-force the password for logging in the system.

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
