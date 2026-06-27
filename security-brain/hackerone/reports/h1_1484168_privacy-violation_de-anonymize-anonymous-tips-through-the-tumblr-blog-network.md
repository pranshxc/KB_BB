---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1484168'
original_report_id: '1484168'
title: De-anonymize anonymous tips through the Tumblr blog network
weakness: Privacy Violation
team_handle: automattic
created_at: '2022-02-18T03:44:45.796Z'
disclosed_at: '2022-02-21T14:58:39.181Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: www.tumblr.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# De-anonymize anonymous tips through the Tumblr blog network

## Metadata

- HackerOne Report ID: 1484168
- Weakness: Privacy Violation
- Program: automattic
- Disclosed At: 2022-02-21T14:58:39.181Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey y’all! 👋 Hope all is well!

## Summary:
I noticed that, if you send an anonymous tip through the Tumblr dashboard, you can be de-anonymized through the notes view on the blog network (& maybe elsewhere?).

## Platform(s) Affected:
All platforms, but requires a blog that is served on the blog network.

## Steps To Reproduce:
To reproduce, you’ll need to…:

1. Have a blog with tips enabled
2. Use a Tumblr blog theme that shows avatars in the permalinked post notes view

Then, to reproduce the issue:

1. Make an anonymous tip from the Tumblr dashboard.
2. Notice that, in the post view on the dashboard, it says “Anonymous” as the tipper.
3. Go to the blog on the blog network and find the post that you tipped for.
4. Open the post permalink view and expand the notes. The avatar from your primary blog that you “anonymously” tipped from will be shown.

## Supporting Material/References:
A couple of things:

* I don’t quite remember how the notes are rendered on the blog network. The blog I noticed this on (████████.tumblr.com) uses a custom theme instead of “Tumblr Official” but that doesn’t change that a user can be de-anonymized on the blog network.
* I also wasn’t sure if anonymous tips were actually anonymous to the receiver too but, if they aren’t, that would allow for the receiver to be considered an “attacker” here.
* When this was an issue with anonymous asks many many years ago, we just removed the `user_id` association with that anonymous ask. Dunno if that’s possible here but I’ll offer it as a suggestion. :)

I’ve also attached screenshots of the blog network notes view and the Tumblr dashboard notes view.

## Impact

An attacker (either the blog owner or a curious brower) can de-anonymize blogs that left an anonymous tip on a post.

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
