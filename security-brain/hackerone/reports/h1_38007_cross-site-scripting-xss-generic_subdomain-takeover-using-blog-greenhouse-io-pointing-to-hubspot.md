---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '38007'
original_report_id: '38007'
title: Subdomain Takeover using blog.greenhouse.io pointing to Hubspot
weakness: Cross-site Scripting (XSS) - Generic
team_handle: greenhouse
created_at: '2014-12-01T23:27:54.941Z'
disclosed_at: '2015-02-26T13:51:15.430Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Subdomain Takeover using blog.greenhouse.io pointing to Hubspot

## Metadata

- HackerOne Report ID: 38007
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: greenhouse
- Disclosed At: 2015-02-26T13:51:15.430Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Your subdomain blog.greenhouse.io is pointing to the service called Hubspot. However, your account at Hubspot has expired or has been cancelled. This basically means that anyone can claim your subdomain pointing to Hubspot and create their own site at this URL. This is EXTREMELY dangerous as whatever the attacker want can be placed on this domain. This is also a foolproof phishing attack since no one would be able to verify that this is not a legit greenhouse.io-login form.

I have temporarily claimed this domain for PoC. You should immediately remove the DNS-entry for blog.greenhouse.io pointing to Hubspot.

And since I'm able to run javascript at Hubspot, I'm able to do whatever I like on that domain. Creating a login form that would fool anyone, since it's present on a greenhouse.io domain.

```
$ host blog.greenhouse.io
blog.greenhouse.io is an alias for san.secure001.hubspot.com.edgekey.net.
san.secure001.hubspot.com.edgekey.net is an alias for e1395.b.akamaiedge.net.
```

PoC-link: 
http://blog.greenhouse.io/

PoC-images attached.

As you might understand, this is really bad. Foolproof phishing. XSS on greenhouse.io. Potential malware spread through a domain you - in this case - do not control. Extremely painful for the company brand.

Please make sure you're always going through your DNS-entries so no subdomains are pointing to external services you do not use.

We've written an advisory about this at Detectify: 
http://blog.detectify.com/post/100600514143/hostile-subdomain-takeover-using-heroku-github-desk

Where you can read more about this sort of attack.

Regards,
Frans Rosén

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
