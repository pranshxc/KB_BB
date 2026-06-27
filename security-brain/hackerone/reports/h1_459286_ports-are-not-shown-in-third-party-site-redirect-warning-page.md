---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '459286'
original_report_id: '459286'
title: Ports are not shown in third-party site redirect warning page.
team_handle: semrush
created_at: '2019-01-18T13:36:14.206Z'
disclosed_at: '2019-04-12T13:53:13.206Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 0
asset_identifier: '*.semrush.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Ports are not shown in third-party site redirect warning page.

## Metadata

- HackerOne Report ID: 459286
- Weakness: 
- Program: semrush
- Disclosed At: 2019-04-12T13:53:13.206Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

**Summary:** 
[Ports are not shown in third-party site redirect warning page]

Vulnerable Endpoint :- https://www.semrush.com/redirect?urlhttp://example.com:1337

**Description:** I noticed #311330 this report where you guys fixed a open redirect report by adding a external third-party site redirect warning page . It was a great fix . Although a issue caught in my eye . Urls contains a protocol and Ports . If I add a url with any other ports like 1337 then it's not shown in the external warning page what can be used to take a user to any other place then user expected to go .

Browsers Verified In: Chrome and Mozilla Firefox

## Steps To Reproduce:

Visit https://www.semrush.com/redirect?url=http://example.com:1337
You will see a warning page only saying about the domain but no warning about the ports like screenshot added below
But the source says it will take user to http://example.com:1337 not only example.com
<a href="http://example.com:1337" id="js-site-link" class="site_link" data-test-site-link="">
Go to site </a>

FIX :-
I can suggest possible fix here :-

Show the Ports of the inputted url in the Warning page .
Thanks

## Impact

I noticed in url= parameter many protocols can be used . Like I can use any port  and on my android if I visit https://www.semrush.com/redirect?url=http://example.com:1337 and click on Go to site then it will open my virtual environment's.

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
