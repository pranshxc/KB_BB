---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '154963'
original_report_id: '154963'
title: Stealing User emails by clickjacking cards.twitter.com/xxx/xxx
weakness: UI Redressing (Clickjacking)
team_handle: x
created_at: '2016-07-29T15:50:43.743Z'
disclosed_at: '2017-02-03T16:14:43.940Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 49
tags:
- hackerone
- ui-redressing-clickjacking
---

# Stealing User emails by clickjacking cards.twitter.com/xxx/xxx

## Metadata

- HackerOne Report ID: 154963
- Weakness: UI Redressing (Clickjacking)
- Program: x
- Disclosed At: 2017-02-03T16:14:43.940Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hello**

In twitter you can create cards to generate leads.
For example:
https://twitter.com/i/cards/tfw/v1/759046372544741376?cardname=promotion&autoplay_disabled=true&earned=true&lang=en&card_height=357

If you visit the above URL and click the button your email and username is sent to my domain.

Since this page is missing X-FRAME-HEADERS,
a user could simply iframe the URL and could steal victim's emails.

**Proof of concept code**
```
<html>
<iframe src=https://twitter.com/i/cards/tfw/v1/759046372544741376?cardname=promotion&autoplay_disabled=true&earned=true&lang=en&card_height=357>
</html>
```

**Regards,
Akhil**

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
