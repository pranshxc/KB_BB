---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '54733'
original_report_id: '54733'
title: Sandboxed iframes don't show confirmation screen
weakness: UI Redressing (Clickjacking)
team_handle: coinbase
created_at: '2015-04-03T18:34:58.274Z'
disclosed_at: '2015-04-04T15:31:37.435Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- ui-redressing-clickjacking
---

# Sandboxed iframes don't show confirmation screen

## Metadata

- HackerOne Report ID: 54733
- Weakness: UI Redressing (Clickjacking)
- Program: coinbase
- Disclosed At: 2015-04-04T15:31:37.435Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Just like I anticipated in 2013 http://homakov.blogspot.com/2013/04/html5-sandbox-bad-idea.html sandbox was a bad idea.

As a payment gateway you do your best to seamlessly integrate with your customers and allow showing checkout in iframes. To prevent basic clickjacking you have data-confirm attribute on Pay button.

However with HTML5 sandbox we can completely switch off Javascript in that iframe, but forms will keep working:

data:text/html,<iframe sandbox="allow-forms"
src="https://www.coinbase.com/checkouts/6d670dea8505cc8805ae2c00294599b2?c=fiZ9HYh4OROMcVtKRtEK"
style="opacity:0.1"></iframe>

After a click in the transparent iframe the payment is made. Risk: This could be used to quickly steal a couple of bitcoins from random visitors and withdrawing them automatically to external address.

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
