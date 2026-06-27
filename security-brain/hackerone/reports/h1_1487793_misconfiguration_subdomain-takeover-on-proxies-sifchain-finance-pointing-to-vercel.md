---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1487793'
original_report_id: '1487793'
title: Subdomain Takeover on proxies.sifchain.finance pointing to vercel
weakness: Misconfiguration
team_handle: sifchain
created_at: '2022-02-21T19:10:08.447Z'
disclosed_at: '2022-04-01T15:25:49.253Z'
has_bounty: true
visibility: full
substate: informative
vote_count: 7
tags:
- hackerone
- misconfiguration
---

# Subdomain Takeover on proxies.sifchain.finance pointing to vercel

## Metadata

- HackerOne Report ID: 1487793
- Weakness: Misconfiguration
- Program: sifchain
- Disclosed At: 2022-04-01T15:25:49.253Z
- Has Bounty: Yes
- Visibility: full
- Substate: informative

## Original Report

Hello Team,

Subdomain takeover vulnerabilities occur when a subdomain (subdomain.example.com) is pointing to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that subdomain. For example, if subdomain.example.com was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a CNAME file containing subdomain.example.com, and claim subdomain.example.com.
Here there is a Sifchain domain  (proxies.sifchain.finance) which is pointing towards vercel pages so  this domain can be taken over can can be used to do any type of attacks mostly i can make a fake login page on your behalf and spoof your users, this is a critical vulnerability and needs to be fixed .

{F1627827}

Vulnerable url : https://proxies.sifchain.finance/

{F1627821}

Cname: cname.vercel-dns.com
Name: proxies.sifchain.finance
Type: CNAME
Class: IN

## Steps To Reproduce/Concept:

1. Visit https://vercel.com/login and login with dev sifchain account

2. Check the availability of the proxies.sifchain.finance sub domain at https://vercel.com/[YourUsername]/sveltekit/settings/domains

3. The proxies.sifchain.finance sub domain does not exist. Potential to be claimed by others

## Remediation:
Remove the cname entry or claim the subdomain proxies.sifchain.finance on vercel.com

## References:
https://github.com/EdOverflow/can-i-take-over-xyz/issues/183

{F1627822}
{F1627826}

https://github.com/EdOverflow/can-i-take-over-xyz
https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/
https://0xpatrik.com/subdomain-takeover/
http://yassineaboukir.com/blog/neglected-dns-records-exploited-to-takeover-subdomains/

Best Regards,
@hrdfrdh

## Impact

Fake website
Malicious code injection
Users tricking
Company impersonation
This issue can have really huge impact on the companies reputation someone could post malicious content on the compromised site and then your users will think it's official but it's not

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
