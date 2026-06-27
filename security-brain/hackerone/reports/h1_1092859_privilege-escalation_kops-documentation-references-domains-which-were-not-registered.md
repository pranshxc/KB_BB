---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1092859'
original_report_id: '1092859'
title: KOPS documentation references domains which were not registered
weakness: Privilege Escalation
team_handle: kubernetes
created_at: '2021-02-02T13:35:54.112Z'
disclosed_at: '2021-04-02T06:42:57.997Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: https://github.com/kubernetes/kops
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# KOPS documentation references domains which were not registered

## Metadata

- HackerOne Report ID: 1092859
- Weakness: Privilege Escalation
- Program: kubernetes
- Disclosed At: 2021-04-02T06:42:57.997Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
While researching the kubernetes documentation, I found that the KOPS project's Route53 configuration references dangling DNS servers. I was able to register 3 / 4 of these domain names. I was also able to verify that some companies have been using this configuration, making them vulnerable to this specific attack. 

In our attack scenario, we are able to serve whatever DNS records we desire, for any domain connected to the NS record. As this is a DNS takeover, any type of DNS record could be added. This makes this far broader reaching than your typical subdomain takeover.

Along with hosting arbitrary content and services, this also allows me to create accounts where specific domain email verification is required such as Google services or Slack. Perhaps most notably, I could create a an email address such as 'postmaster@domain.com' which could be used to issue SSL certificates as outlined in the following article: https://support.dnsimple.com/articles/ssl-certificates-email-validation/. This can potentially allow the joining of internal services (such as slack, Jira, Confluence or Zendesk) or allow me to setup catch all e-mail addresses to collect any inbound e-mail for addresses that previously existed on this domain. These kinds of takeovers can have far reaching consequences for an organisation, and should be treated with a high threat model.

In addition to these risks, were PayPal subscriptions or other such payment providers previously connected to this subdomain and discovered by a malicious actor, then they would be able to re-claim these subscriptions and bill any customers who still had them active. It is worth noting that in testing I have verified that PayPal does not automatically cancel user subscriptions once a domain has gone stale, and that would be a realistic attack vector here if PayPal payments (via the subscription model) were taken using this subdomain at any point.

## Steps To Reproduce:
1. View lines 129 - 135 of https://github.com/kubernetes/kops/blob/master/docs/getting_started/aws.md

## Supporting Material/References:
Proof of domain ownership:
{F1180954}

## Impact

In our attack scenario, we are able to serve whatever DNS records we desire, for any domain connected to the NS record. As this is a DNS takeover, any type of DNS record could be added. This makes this far broader reaching than your typical subdomain takeover.

Along with hosting arbitrary content and services, this also allows me to create accounts where specific domain email verification is required such as Google services or Slack. Perhaps most notably, I could create a an email address such as 'postmaster@domain.com' which could be used to issue SSL certificates as outlined in the following article: https://support.dnsimple.com/articles/ssl-certificates-email-validation/. This can potentially allow the joining of internal services (such as slack, Jira, Confluence or Zendesk) or allow me to setup catch all e-mail addresses to collect any inbound e-mail for addresses that previously existed on this domain. These kinds of takeovers can have far reaching consequences for an organisation, and should be treated with a high threat model.

In addition to these risks, were PayPal subscriptions or other such payment providers previously connected to this subdomain and discovered by a malicious actor, then they would be able to re-claim these subscriptions and bill any customers who still had them active. It is worth noting that in testing I have verified that PayPal does not automatically cancel user subscriptions once a domain has gone stale, and that would be a realistic attack vector here if PayPal payments (via the subscription model) were taken using this subdomain at any point.

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
