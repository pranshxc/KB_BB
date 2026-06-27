---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '48422'
original_report_id: '48422'
title: Team member invitations to sandboxed teams are not invalidated consistently
  (v2)
weakness: Privilege Escalation
team_handle: security
created_at: '2015-02-20T23:58:42.957Z'
disclosed_at: '2015-02-27T23:27:32.912Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- privilege-escalation
---

# Team member invitations to sandboxed teams are not invalidated consistently (v2)

## Metadata

- HackerOne Report ID: 48422
- Weakness: Privilege Escalation
- Program: security
- Disclosed At: 2015-02-27T23:27:32.912Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

As per our email conversation on ticket 2527, I am giving you a proof of concept of my claim.

1. I have a sandboxed team in hackerone,named movielee.
2. The manager of that team (@haxorsistz) sends an invite to => ██████████
3. The link which I received on email was => https://hackerone.com/invitations/6fbca8af2f861c8174136f97ec51fde6

4. I logged in from another researcher (@geekboy) account and visited the link.Accepted the request.
5. Now I can see that invitation is still live.

So, a member of any team can pass this token to other people and they will be added to the team.I used this token 3 times and it's still live.

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
