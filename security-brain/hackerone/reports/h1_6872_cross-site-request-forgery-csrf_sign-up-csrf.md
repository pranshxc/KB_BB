---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6872'
original_report_id: '6872'
title: Sign up CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: irccloud
created_at: '2014-04-10T21:24:11.161Z'
disclosed_at: '2014-05-14T13:01:59.583Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Sign up CSRF

## Metadata

- HackerOne Report ID: 6872
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: irccloud
- Disclosed At: 2014-05-14T13:01:59.583Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Again sir,

There is no mitigation against CSRF attacks on the regsitration, I believe when not fixed you will be flooded with reports by researchers regarding this.

<form action="" method="post" class="signupForm" novalidate>
                <p>Sign up for a free account / <b><a href="/pricing" target="_blank">Pricing</a></b></p>
                <div class="userError"></div>
                <div id="signupOrgInfo" class="userInfo">You’re signing up to join the <b id="signupOrgName"></b> team.</div>
                <p class="form"><input class="input" name="realname" placeholder="Name"></p>
                <p class="form"><input class="input" name="email" type="email" placeholder="Email"></p>
                <p class="form"><input class="input" name="password" type="password" placeholder="Password"></p>
                <input type="hidden" name="invite">
                <input type="hidden" name="org_invite">
                <p class="form"><button type="submit" class="signup"><span>Sign up</span></button></p>
                <p><small>By signing up, you agree to our <a href="/terms">Terms of Service</a></small></p>
            </form>

Kindly let me know if you needed more information.

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
