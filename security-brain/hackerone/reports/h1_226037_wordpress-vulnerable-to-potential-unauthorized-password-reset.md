---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226037'
original_report_id: '226037'
title: Wordpress Vulnerable to Potential Unauthorized Password Reset
team_handle: nextcloud
created_at: '2017-05-04T08:31:19.072Z'
disclosed_at: '2017-08-15T08:42:06.400Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
---

# Wordpress Vulnerable to Potential Unauthorized Password Reset

## Metadata

- HackerOne Report ID: 226037
- Weakness: 
- Program: nextcloud
- Disclosed At: 2017-08-15T08:42:06.400Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Yesterday, a new 0day on wordpress core has been discovered by Dawid Golunski, so i want you guys to be aware of it to take an immediate action since nextcloud was using wordpress.

>Wordpress has a password reset feature that contains a vulnerability which
might in some cases allow attackers to get hold of the password reset link
without previous authentication. 
Such attack could lead to an attacker gaining unauthorised access to a 
victim's WordPress account.

Affected WP version is up to the latest one `4.7.4` , so while waiting for the release of the new version that will fix the issue, you may want to apply a temporary solution, enable `UseCanonicalName` to enforce static SERVER_NAME value.

You can see the full details of the issue on this URL: https://exploitbox.io/vuln/WordPress-Exploit-4-7-Unauth-Password-Reset-0day-CVE-2017-8295.html

Regards
Japz

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
