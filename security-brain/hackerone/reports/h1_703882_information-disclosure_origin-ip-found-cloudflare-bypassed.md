---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '703882'
original_report_id: '703882'
title: Origin IP found, Cloudflare bypassed
weakness: Information Disclosure
team_handle: people_interactive
created_at: '2019-09-29T17:13:40.048Z'
disclosed_at: '2023-07-27T04:05:02.265Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: www.shaadi.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Origin IP found, Cloudflare bypassed

## Metadata

- HackerOne Report ID: 703882
- Weakness: Information Disclosure
- Program: people_interactive
- Disclosed At: 2023-07-27T04:05:02.265Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Non-Cloudflare IPs allowed to access origin servers
## Description
The frontend currently resolves to 104.16.100.160,  owned by Cloudflare, which act as your reverse proxy and WAF. By correlating your SSL Certificates to other hosts on the internet that serve the same content I was able to determine the current Origin Server as 3.211.245.254, operated by Amazon's AWS services.
By using these IP address as a resolver instead of the intended addresses I'm able to access the service without going through the WAF, thus I'm able to forward unfiltered payloads to the service, as well as avoiding the common protections offered by Cloudflare, also being able to perform crippling denial-of-services towards the origin.
##PoC
https://www.shodan.io/host/3.211.245.254
http://3.211.245.254
## Suggestions
My recommendations fall in line with Cloudflare's own guidelines: the Origin server must communicate exclusively with Cloudflare's IP address ranges, otherwise—as reported in this post on Cloudflare's blog, the protection offered by having a reverse proxy basically becomes useless.
## Bug Reference
https://www.cloudflare.com/learning/cdn/glossary/origin-server/
https://blog.detectify.com/2019/07/31/bypassing-cloudflare-waf-with-the-origin-server-ip-address/
https://support.incapsula.com/hc/en-us/articles/211809478-How-do-I-conceal-my-origin-server-IP-
https://www.secjuice.com/finding-real-ips-of-origin-servers-behind-cloudflare-or-tor/
## Similar reports on hackerone
https://hackerone.com/reports/255978
https://hackerone.com/reports/360825
https://hackerone.com/reports/315838

## Impact

As reported in many other submissions, Cloudflare bypasses can have a significant impact, as any adversary is now able to communicate with the origin server directly, enabling them to perform unfiltered attacks (such as denial-of-service), and data retrieval.

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
