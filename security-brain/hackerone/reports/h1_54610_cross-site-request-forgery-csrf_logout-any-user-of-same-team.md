---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '54610'
original_report_id: '54610'
title: Logout any user of same team
weakness: Cross-Site Request Forgery (CSRF)
team_handle: slack
created_at: '2015-04-03T06:32:13.344Z'
disclosed_at: '2015-05-05T05:59:54.329Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Logout any user of same team

## Metadata

- HackerOne Report ID: 54610
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: slack
- Disclosed At: 2015-05-05T05:59:54.329Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It is possible for a user to logout other member of same team even if they had selected *Keep me signed in* option.

**Steps to Verify:**
1. Login to your team i.e [https://yourteamname.slack.com](https://yourteamname.slack.com).
2. On new tab on the same browser request a url which would be like [https://yourteamname.slack.reset/youareloggedout](https://yourteamname.slack.reset/youareloggedout)
3. You will be automatically logged out of your account even if you have selected **Keep me signed in** option.

Attacker can embed the invalid password reset link in a image tag in a website of his/her control and when users visists the page they will be logged out.

`<html>
<head>
	<title>I Logged You Out</title>
</head>
<body>
<img src='https://yourteamname.slack.com/reset/youareloggedout'>
</body>
</html>`

You should not logout a user when an invalid password reset link is accessed rather than you should redirect a user to homepage whenever a password reset link is accessed when user is allready logged in.

Thanks
**Uttam Soren**

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
