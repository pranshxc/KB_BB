---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '265740'
original_report_id: '265740'
title: '[Cross Domain Referrer Leakage] Password Reset Token Leaking to Third party
  Sites.'
weakness: Information Disclosure
team_handle: radancy
created_at: '2017-09-04T07:53:26.427Z'
disclosed_at: '2017-09-07T15:56:37.356Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: werkenbijdefensie.nl
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# [Cross Domain Referrer Leakage] Password Reset Token Leaking to Third party Sites.

## Metadata

- HackerOne Report ID: 265740
- Weakness: Information Disclosure
- Program: radancy
- Disclosed At: 2017-09-07T15:56:37.356Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Domain and URL:**
https://werkenbijdefensie.nl

**Summary:**:  Password Reset Token Leaking to Third party Sites from the link in the footer

**Description:** Hello,
I found that the if a user request for a password reset link and open it but don't change the password and click on the Third Parties Sites link in the Footer his Password Reset Token will be leaked by the Server to that third party site and that token can be used by third parties to reset the password and take over the account.

## Steps To Reproduce:

1. Request a password reset token to your email.
2. When received open the link.
3. Click the Link to the social media sites like facebook, twitter, youtube and etc.
4. The Following Request would be sent:


GET /werkenbijdefensie HTTP/1.1
Host: www.facebook.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://werkenbijdefensie.nl/het-vizier/wachtwoord-wijzigen.html?token=<some token>
Cookie: <cookies>
Connection: keep-alive


If you need any further information please be free to ask me.

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
