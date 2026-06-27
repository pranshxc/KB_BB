---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '895730'
original_report_id: '895730'
title: Contacts menu (not app) fails to restrict (to local groups) for contacts from
  federated servers
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2020-06-11T00:03:52.909Z'
disclosed_at: '2020-07-25T08:10:36.069Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Contacts menu (not app) fails to restrict (to local groups) for contacts from federated servers

## Metadata

- HackerOne Report ID: 895730
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2020-07-25T08:10:36.069Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In two Nextclouds A and B, in settings/admin/sharing, these settings are enabled:
* Restrict users to only share with users in their groups
* Restrict username autocompletion to users within the same groups
* Add server automatically once a federated share was created successfully

Some user on A now shares something to some other user on B → federation for that server is established and green on both NCs.

On B, add a new group with a new user N. That user is the only user in that new, separate group. Log in as N. Click on contacts menu (next to the user menu). One sees all contacts of A. One shouldn't see any.

This is relevant since it is unexpected and NC lacks a means to restrict viewing of such contact data. This may lead to a GDPR relevant data breach. (In my case, it did!) IF data were COPIED to B (cached?, not sure), this would be even worse.

Deleting the federation solves the issue (but breaks functionality otherwise desired). I propose to add further restriction selections (for contacts from federated servers) to sharing.

Sidenote: The way it is now also has a functional glitch: If one clicks in the info "i" next to one contact from a federated server, the "contacts" app opens and shows an error "No such contact found"…

## Impact

Well, what SECURITY impact? It's a PRIVACY impact. But since Nextcloud strives to be the privacy-friendly alternative to big players…

OK: Impact is simple contact information disclosure. But to make clear what dimensions this could lead to: Imagine all business contact information in A (in my case >1000 contacts), readable to completely unrelated people on another instance.

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
