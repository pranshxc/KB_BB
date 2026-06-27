---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '142096'
original_report_id: '142096'
title: '[Screenhero] Subdomain takeover'
weakness: Violation of Secure Design Principles
team_handle: slack
created_at: '2016-05-30T17:37:42.583Z'
disclosed_at: '2017-01-21T17:25:56.100Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- violation-of-secure-design-principles
---

# [Screenhero] Subdomain takeover

## Metadata

- HackerOne Report ID: 142096
- Weakness: Violation of Secure Design Principles
- Program: slack
- Disclosed At: 2017-01-21T17:25:56.100Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found out some neglected DNS records that can be exploited to takedown the subdomain of Slack's acquisition `feedback.screenhero.com`

The security issue is that you have CNAME record that points `feedback.screenhero.com` to a `screenhero.uservoice.com`, but the problem is that the service is inactive, thus any malicious hacker would simply sign up for the service and claims the username `Screenhero` as his and no verification is done by the Service Provider, besides that the DNS-setup is already correctly set.

{F97017}

**Scenario attack :**
Attacker can now build a complete clone of the real site, add a login form, redirect the user, steal credentials (e.g. admin accounts), cookies and/or completely destroy business credibility for your company along with along with injecting malicious codes to steal their sensitive cookies, redirect them to malicious web pages etc.

**Mitigation :** To mitigate the threat you should remove CNAME DNS records for the services you don't use anymore.

**Reference:** http://yassineaboukir.com/blog/neglected-dns-records-exploited-to-takeover-subdomains/

Best regards.

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
