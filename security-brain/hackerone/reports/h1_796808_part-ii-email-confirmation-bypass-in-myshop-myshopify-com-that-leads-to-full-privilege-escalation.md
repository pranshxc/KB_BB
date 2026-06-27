---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '796808'
original_report_id: '796808'
title: '[Part II] Email Confirmation Bypass in myshop.myshopify.com that Leads to
  Full Privilege Escalation'
team_handle: shopify
created_at: '2020-02-14T17:37:31.543Z'
disclosed_at: '2020-04-01T21:02:00.348Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 877
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# [Part II] Email Confirmation Bypass in myshop.myshopify.com that Leads to Full Privilege Escalation

## Metadata

- HackerOne Report ID: 796808
- Weakness: 
- Program: shopify
- Disclosed At: 2020-04-01T21:02:00.348Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary 
In #791775, I submitted a bug at Sunday 5pm Canada time, it was triaged two hours later, and I got the **temp** fix message at around 3am the next day in Canada time. Truly awesome, the next day I retested after the first fix, and found that I

- Cannot receive the email confirmation in the email used to sign up
- Cannot integrate across stores/partner even they share the same email address after confirming them

And the report was later resolved after I verified the fix.

For some reason, I decided to test again to see what's something new that I can find.

Then I found user can change their email prior to receiving the verification message on their original email. i.e. the same technique, I don't know what went wrong in my first retest, but Shopify security and engineering team again showed their professionalism, quickly resolving the second comments I left in ~3.5 hrs.

And when I thought this is the end of story, I later received a comment asking me to open a new report about the second retest, and here I am writing this report.

Thanks,
Ron

## Impact

.

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
