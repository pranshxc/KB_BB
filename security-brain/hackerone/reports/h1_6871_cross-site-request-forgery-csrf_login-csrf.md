---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6871'
original_report_id: '6871'
title: Login CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: irccloud
created_at: '2014-04-10T21:22:34.406Z'
disclosed_at: '2014-04-21T16:02:37.838Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Login CSRF

## Metadata

- HackerOne Report ID: 6871
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: irccloud
- Disclosed At: 2014-04-21T16:02:37.838Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi sir,

There is no mitigation of XCSRF in your login form. 

Kindly check the source code of login:

<form class="signin" action="" method="post" novalidate>
                    <p class="form">
                        <input class="input" name="email" type="email" placeholder="Email">
                        <input class="input" name="password" type="password" placeholder="Password">
                        <input type="hidden" name="org_invite">
                        <button type="submit"><span>Login</span></button>
                        <a class="forgotten" href="#?/password-reset">Forgotten your password?</a>
                    </p>
                    <div class="userError"></div>
                </form>

kindly let me know if you needed more information.

Clifford

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
