---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '493324'
original_report_id: '493324'
title: Privilege escalation from any user (including external) to gitlab admin when
  admin impersonates you
weakness: Privilege Escalation
team_handle: gitlab
created_at: '2019-02-09T14:13:39.950Z'
disclosed_at: '2020-08-26T14:10:18.484Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 232
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Privilege escalation from any user (including external) to gitlab admin when admin impersonates you

## Metadata

- HackerOne Report ID: 493324
- Weakness: Privilege Escalation
- Program: gitlab
- Disclosed At: 2020-08-26T14:10:18.484Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hey team,
I have discovered a way for any logged in user (attacker) to escalate his privileges to gitlab administrator if the real gitlab administrator impersonates attacker's account.

**Description:**
When the gitlab admin impersonates some user, he gets new `_gitlab_session` cookie and then clicking at `Stop impersonating` he gets his own admin's cookie back. The vulnerability is that the impersonated user (attacker in our case) can see impersonated session at the `Active sessions` so he can switch to it (manually setting it in cookie) and click `Stop impersonating` by himself. This is a way how he can become gitlab administrator.

## Steps To Reproduce:

1. Sign into gitlab app as some user (`attacker`)
1. Go to the active sessions settings tab and revoke all the sessions besides the current active one
1. Sign into gitlab app in other browser as administrator (`admin`)
1. Go to users admin section and impersonate `attacker` user
1. Update the active sessions tab as `attacker` and make sure the second session appeared there (this is the admin logged into your account)
{F420971}
1. Inspect the `Revoke` button and make sure you see the session ID there. Copy it.
████
1. Go to index page of gitlab as `attacker` (http://gitlab.bb/ in my case), I do not know why, but it is important step
1. Clear `attacker` browser's cookie
1. Open the developer console as `attacker` and manually set `_gitlab_session` to the copied one with:

```javascript
document.cookie = "_gitlab_session=█████";
```
9. Refresh the attacker's page and make sure you are now inside the impersonated session
{F420978}
10. Click `Stop impersonating` at the top-right corner as `attacker` and make sure you are now logged in as gitlab admin.
███

## Impact

Every gitlab authenticated user can escalate his privileges to admin ones and give complete access to all gitlab services, projects and abilities. Only he needs to do is ask admin to impersonate his account because of something works bad there.

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
