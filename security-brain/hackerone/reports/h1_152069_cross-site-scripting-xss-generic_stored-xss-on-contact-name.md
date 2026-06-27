---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152069'
original_report_id: '152069'
title: Stored XSS on contact name
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-18T14:47:05.687Z'
disclosed_at: '2016-10-20T11:49:36.552Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS on contact name

## Metadata

- HackerOne Report ID: 152069
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-10-20T11:49:36.552Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi guys,

I found a stored XSS in olx.pt. I didn't tested on other domains so feel free to update this report if other domains are also affected.

When submiting a new ad, I added my XSS payload on data[person]. 
The ad got approved and no reflecting on this field. The output was sanitized.

One thing that I know of was that the input wasn't, because if I edited the ad, the payload was launched so the input wasn't sanitized when added to the database. 

Then I remembered to check the "other ads from this person" and guess what? Stored XSS payload was launched and reflected on the page twice:

<meta property="og:title" content="Todos os anúncios do utilizador Tomás Foz"><img src=x onerror=prompt(1)>"/>

And:

<h3 class="xxx-large fbold lheight24 c000">Tomás Foz"><img src=x onerror=prompt(1)></h3>

Check my attached screenshot.
This is very dangerous because it runs automatically when the victim visits the page:
https://olx.pt/ads/user/GGSl/

Meanwhile I deleted the add to prevent any damage to your users.

Hope it helps.

Best,
David Sopas
@dsopas

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
