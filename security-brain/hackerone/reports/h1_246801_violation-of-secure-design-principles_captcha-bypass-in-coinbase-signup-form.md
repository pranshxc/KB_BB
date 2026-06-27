---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '246801'
original_report_id: '246801'
title: Captcha Bypass in Coinbase SignUp Form
weakness: Violation of Secure Design Principles
team_handle: coinbase
created_at: '2017-07-07T07:33:35.203Z'
disclosed_at: '2017-09-05T17:09:43.099Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- violation-of-secure-design-principles
---

# Captcha Bypass in Coinbase SignUp Form

## Metadata

- HackerOne Report ID: 246801
- Weakness: Violation of Secure Design Principles
- Program: coinbase
- Disclosed At: 2017-09-05T17:09:43.099Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability description:

The g-recaptcha-response is not validated on the server-side when submitting a Signup form to the endpoint. Any or no value can be provided for this header

Step to reproduce:

1. https://www.coinbase.com/signup
2. Fill the input field and Validate the captcha.
3. Trun on Brurp submit form and capture the request.
4. Remove the g-recaptcha-response( response value) and foreword it.

Impact.
Fake accounts can be created. Also username enumeration can be performed because no application will allow two email to choose same email.

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
