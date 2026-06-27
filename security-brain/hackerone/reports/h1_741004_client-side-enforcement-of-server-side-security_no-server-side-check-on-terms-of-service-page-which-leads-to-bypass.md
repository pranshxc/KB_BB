---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '741004'
original_report_id: '741004'
title: No server side check on terms of service page which leads to bypass
weakness: Client-Side Enforcement of Server-Side Security
team_handle: acronis
created_at: '2021-09-13T10:00:17.476Z'
disclosed_at: '2021-10-05T09:19:47.972Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 6
asset_identifier: account.acronis.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- client-side-enforcement-of-server-side-security
---

# No server side check on terms of service page which leads to bypass

## Metadata

- HackerOne Report ID: 741004
- Weakness: Client-Side Enforcement of Server-Side Security
- Program: acronis
- Disclosed At: 2021-10-05T09:19:47.972Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hi team,
I have found that there is no server side check implemented on the "Acronis Terms of Service and Privacy Statement" Page that is shown after filling the registration form which results in bypassing it without even accepting it.

Steps To Reproduce:

  1. Register as a new user by filling out the form.
  2. After that a new page will open it will require the user to check the box otherwise the button will remain disabled.
  3. Right click on the button choose inspect element.
  4. Find the button tag and remove the attribute "disabled=disabled" and "is-disabled" from the class.
  5. Now press enter and close the inspect element.
  6. As you can see the button is now enabled you can click on it and it will take you to your account.

Recommendations:

 A server side check must be implemented here so that if an attacker or a scammer bypasses the client side validation using inspect element the server 
 will validate the action and give an error based upon it preventing the attacker from going to the next page.

POC video attached!

Thanks.

## Impact

This bug has a very straight forward impact. Lack of server side check here will lead the attacker bypass the page easily and register as a legitimate user. The server will have no clue if the person registering had accepted the terms of service and privacy statement or not.

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
