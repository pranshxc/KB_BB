---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1615790'
original_report_id: '1615790'
title: Any expired reset password link can still be used to reset the password
weakness: Improper Access Control - Generic
team_handle: acronis
created_at: '2022-06-28T05:32:43.640Z'
disclosed_at: '2022-09-01T09:31:42.112Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.5nine.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Any expired reset password link can still be used to reset the password

## Metadata

- HackerOne Report ID: 1615790
- Weakness: Improper Access Control - Generic
- Program: acronis
- Disclosed At: 2022-09-01T09:31:42.112Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Aronis team!

When requesting a password reset link at https://alt.5nine.com/passwordrecovery.aspx and using it, after a short time the link becomes invalid.
When I open the link I get the message:
*"Your validation request is invalid or expired"*
But it is still possible to use it to reset the password, because it is still linked with the "__VIEWSTATE" parameter on the server side and this is the only value needed in the password reset process, and it can be used infinite times to reset the password.
So in short, you use the reset link to get the value of "__VIEWSTATE" and use it to reset the password

Therefore, in a scenario where an attacker has somehow gained access to the victim's inbox, they can use any expired link to change the user's password.

##STEPS TO REPRODUCE

1- Go to https://alt.5nine.com/passwordrecovery.aspx
2- Enter your account email and click "reset"
3- Use the link and reset your password
4- Wait some time (about 30 min) for the link to expire, as shown below

{F1795088}
*(just to confirm it's expired and you can use it to reset the password anyway)*

5- Now view the page source code, search for "viewstate" and capture its value
{F1795365}

6- Encode it's value as url --> https://urlencode.org
7- Now use the encoded value in the following request

```
POST /TokenValidation.aspx HTTP/2
Host: alt.5nine.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 405

__VIEWSTATE=<viewstate-here>&ctl00%24mainContentId%24Password=hacked123&ctl00%24mainContentId%24ConfirmPassword=hacked123&ctl00%24mainContentId%24FinalizeRegistration=Submit
```
8- And the password will be changed to "hacked123"
{F1795370}

##References
https://hackerone.com/reports/898841
https://hackerone.com/reports/772886

## Impact

Password reset link must become completely useless after used, to prevent someone malicious who has access to it use it to reset the password, in this case the user will lose the account if the attacker has access to any old link

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
