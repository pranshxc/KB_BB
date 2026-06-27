---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229620'
original_report_id: '229620'
title: Information Disclosure on demo.weblate.org
weakness: Information Disclosure
team_handle: weblate
created_at: '2017-05-18T13:35:59.424Z'
disclosed_at: '2017-06-02T14:23:36.965Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# Information Disclosure on demo.weblate.org

## Metadata

- HackerOne Report ID: 229620
- Weakness: Information Disclosure
- Program: weblate
- Disclosed At: 2017-06-02T14:23:36.965Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
The demo instance, located on https://demo.weblate.org is leaking user's IP-adresses in the Activity log.
{F185728}

##Impact
The authenticated user can disclose valid IP adresses of other users through Activity log. The feature works as it should (*so no changes should be made on the GitHub or other sites like hosted.weblate.org*), but i still recommend you to hide IPs that do not belong to the user only on this particular instance, because user do not know before login, that his IP will become accessible to the public.

##Reproduction Steps
1) Login at the https://demo.weblate.org as demo:demo
2) Go to the https://demo.weblate.org/accounts/profile/#audit

##Suggested fix
The sensitive information can be hided in various ways - for example `x.x.x.x` or similar. It do not require code changes on your GitHub repositories, just in this particular instance.

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
