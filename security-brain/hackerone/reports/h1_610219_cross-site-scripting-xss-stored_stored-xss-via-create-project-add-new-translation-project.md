---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '610219'
original_report_id: '610219'
title: Stored XSS via Create Project (Add new translation project)
weakness: Cross-site Scripting (XSS) - Stored
team_handle: weblate
created_at: '2019-06-12T14:28:32.362Z'
disclosed_at: '2019-07-09T13:43:21.812Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: https://github.com/WeblateOrg/docker
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS via Create Project (Add new translation project)

## Metadata

- HackerOne Report ID: 610219
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: weblate
- Disclosed At: 2019-07-09T13:43:21.812Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, Input validation and/or sanitisation is not currently applied in the **Project Name** field in https://<domain>/create/project/. As, a result, it is possible to have a stored XSS that will affect all the users in the Weblate application. To identify this XSS I used the Docker environment from https://github.com/WeblateOrg/docker.

**Steps to reproduce:**

1. Administrator creates a project and then adds a user in that project.
2. Depending on permissions the user will login go to **watched projects** pick the project -> **Manage** -> **Settings** and will have the ability to change the Project Name. Here I changed it to `<svg/onload=alert(document.domain)>` and hit save.
3. When the user visits his `/accounts/profile/` page, he will trigger the Stored XSS.

I also found that even a user that doesn't have access to that project, but I guess the project is public, he will also get xss'ed. Furthermore, with this he also has the ability to xss the Admin, all the have to do is visit the `/accounts/profile/` page.

So, this has the potential to affect all users.

## Impact

Input validation and/or sanitisation on the Project Name field.

Please let me know if you require any additional information regarding this issue.

Thanks.

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
