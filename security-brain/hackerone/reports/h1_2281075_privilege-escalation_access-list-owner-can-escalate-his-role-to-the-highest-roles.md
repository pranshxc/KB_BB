---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2281075'
original_report_id: '2281075'
title: access list owner can escalate his role to the highest roles
weakness: Privilege Escalation
team_handle: teleport
created_at: '2023-12-11T18:28:32.289Z'
disclosed_at: '2023-12-29T21:08:31.495Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 258
asset_identifier: h1-your-domain.teleport.sh
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# access list owner can escalate his role to the highest roles

## Metadata

- HackerOne Report ID: 2281075
- Weakness: Privilege Escalation
- Program: teleport
- Disclosed At: 2023-12-29T21:08:31.495Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

1. Go to [your-domain.teleport.sh/web/accesslists].

2. Create a new access list and add a role to "Roles Granted," e.g., "reviewer" role.

3. Add a user as the Access List Owner.

4. The user, as the Access List Owner, can escalate the role of the list to higher roles, thereby escalating their own account's role.

This is a prohibited procedure, as stated [here](https://goteleport.com/docs/access-controls/access-lists/reference/#access-list-ownership), that Owners are not able to control what roles and traits are granted by the Access List.

## Steps To Reproduce:

### From Organization Owner Account:

1. Go to [your-domain.teleport.sh/web/accesslists].

2. Create a new access list.

3. Add a user as List Owner.

4. Add a role to "Roles Granted," e.g., "reviewer" role.

### From Access List Owner Account:

1. Add a new member to the access list and intercept the request.

2. Add "editor" role on "grants roles."

3. The "editor" role will be added to "Permissions Granted."

4. Logout and relogin.

5. Now, the user has the "editor" role and can perform any action on the organization.

## Impact

- Unauthorized Access: Potential for unauthorized access to sensitive information.
- Security Breach: Risk of compromising the overall security of the system.
- Privilege Escalation: Violation of the principle of least privilege.
- Violation of Access Control Policies: Contradiction with Teleport's documentation and policies.
- Risk of Insider Threats: Potential exploitation by malicious insiders.

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
