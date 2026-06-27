---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '264934'
original_report_id: '264934'
title: Application allowing old password to be set as new password | hosted.weblate.org
team_handle: weblate
created_at: '2017-08-31T09:46:56.320Z'
disclosed_at: '2017-10-05T14:22:17.624Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: hosted.weblate.org
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Application allowing old password to be set as new password | hosted.weblate.org

## Metadata

- HackerOne Report ID: 264934
- Weakness: 
- Program: weblate
- Disclosed At: 2017-10-05T14:22:17.624Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I found an issue that your application is allowing user to set new password same as that of the old password.

Steps to reproduce the defect

-Firstly logged into the application with existing password (refer screenshot named : Original Password login Request)-Old password highlighted in screenshot

-secondly now go to change password link and tried to set the new password with same value set in old password (refer screenshot named : Change Password Request Old and new password are same )

-thirdly now as a result of the above step you can see the new password same as old password (refer screenshot named : Change Password Request and Response- Old and new password are same)


Issue Description

As per secure password policy application should not allow same old password value to be used in setting new password value cos there might be possibility that old password might be exposed or leaked to an adversary so its advisable on application end to enforce strong password policy and should implement check to not to allow user to set old password value in new password value.

See the attached screenshots for issue details.

Please also refer the below mentioned link for reference:

https://www.owasp.org/index.php/Testing_for_Weak_password_policy_(OTG-AUTHN-007)

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
