---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '128856'
original_report_id: '128856'
title: Send email asynchronously
weakness: Uncontrolled Resource Consumption
team_handle: gratipay
created_at: '2016-04-07T02:15:36.529Z'
disclosed_at: '2017-03-17T17:58:17.878Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Send email asynchronously

## Metadata

- HackerOne Report ID: 128856
- Weakness: Uncontrolled Resource Consumption
- Program: gratipay
- Disclosed At: 2017-03-17T17:58:17.878Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It seems like the https://gratipay.com/~USER/emails/modify.json endpoint has some protection to prevent email flooding as seen here https://github.com/gratipay/gratipay.com/blob/master/gratipay/models/participant.py#L407 plus CSRF validation.

However, it is possible to flood the server with multiple email requests as long as you send different email addresses. This might be a door to a DoS attack considering emails are sent synchronous on the request (this means each email sending request will hold that thread and connection for quite a good time). Finally, depending on what email server you are using, if this can be abused you might end up paying for a lot of sent emails.

Note that I'm not 100% sure there's no other kind of throttling on this endpoint and I was too afraid to test.

Below is the screenshot of a few sent emails showing how all of them were sent correctly and high time it took on the server and another one of me receiving all of them.

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
