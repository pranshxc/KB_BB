---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12782'
original_report_id: '12782'
title: Spamming any user from Reset Password Function
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-05-22T10:08:18.472Z'
disclosed_at: '2016-05-03T03:52:03.253Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Spamming any user from Reset Password Function

## Metadata

- HackerOne Report ID: 12782
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-05-03T03:52:03.253Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

It is possible to spam any user whose email-id is known.

This can be combined with csrf attack i.e automated to send 50 emails with a click.

This is reset password form --->

<form accept-charset="UTF-8" action="https://hackerone.com/users/password" class="new_user" id="new_user" method="post"><div style=""><input name="utf8" value="✓" type="hidden"><input name="authenticity_token" value="AjjZNIMzdX598CXInx9CMbovtHbiqL+ziw4qTJ7RFnZQh/oub+mYFKjjNb1TXyITVCpkFPJ21ViG4IQz72KbMQ==" type="hidden"></div>

  <h1 class="narrow-title">Forgot password</h1>

  <div class="narrow-container">
    <p>To retrieve your password enter the email address you used to sign up.</p>

    <div class="input-wrapper-small">
      <input autofocus="autofocus" class="input" id="user_email" name="user[email]" placeholder="Email address" type="email">
    </div>

    <input class="button success is-full-width" data-disable-with="Sending..." name="commit" value="Send" type="submit">
  </div>
</form>

Here,
<input name="authenticity_token" value="AjjZNIMzdX598CXInx9CMbovtHbiqL+ziw4qTJ7RFnZQh/oub+mYFKjjNb1TXyITVCpkFPJ21ViG4IQz72KbMQ==" type="hidden">

authencity token can be used more than one.
Users can be spammed heavily by just simple coding a script.
Only email-id should be known.

I tried it on my own account. I was able to use the token for more than 5 attempts.
This is not best practice.
Only one try must be allowed.

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
