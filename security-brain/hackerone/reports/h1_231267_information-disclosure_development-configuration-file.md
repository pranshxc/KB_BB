---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '231267'
original_report_id: '231267'
title: Development configuration file
weakness: Information Disclosure
team_handle: pushwoosh
created_at: '2017-05-23T21:21:30.618Z'
disclosed_at: '2018-01-18T10:18:17.634Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- information-disclosure
---

# Development configuration file

## Metadata

- HackerOne Report ID: 231267
- Weakness: Information Disclosure
- Program: pushwoosh
- Disclosed At: 2018-01-18T10:18:17.634Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I found an **Sensitive Information Disclosure**.
A configuration file (e.g. Vagrantfile, Gemfile, Rakefile, ...) was found in this directory. This file may expose sensitive information that could help a malicious user to prepare more advanced attacks. It's recommended to remove or restrict access to this type of files from production systems.

#POC
https://go.pushwoosh.com/composer.json
https://go.pushwoosh.com/composer.lock

Open these URLs a configuration file will become download and these files contains very sensitive data.

###IMPACT:
These files may disclose sensitive information. This information can be used to launch further attacks.

###PATCH
Remove or restrict access to all configuration files accessible from internet.

Thanks,

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
