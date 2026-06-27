---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '671406'
original_report_id: '671406'
title: Account takeover via Google OneTap
weakness: Improper Authentication - Generic
team_handle: priceline
created_at: '2019-08-11T14:34:02.500Z'
disclosed_at: '2022-05-11T09:37:14.985Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 71
asset_identifier: www.priceline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Account takeover via Google OneTap

## Metadata

- HackerOne Report ID: 671406
- Weakness: Improper Authentication - Generic
- Program: priceline
- Disclosed At: 2022-05-11T09:37:14.985Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

It's possible to take over any priceline.com user's account knowing their email. The only requirement is that the victim's email domain is not registered with Google's Gsuite. The root cause of this issue is that the backend does not verify whether the email provided is a confirmed one.

## Steps To Reproduce:

1. Create Account A (in my case `badca7@wearehackerone.com`) with priceline.com, without any SSO, via the "Create an account" link (aka "register with email").
2. Once the account has been created, add a dummy phone number to the profile. It will serve as a canary to demonstrate we accessed the same data in the next steps.
3. In another browser/session (eg, incognito/private mode) sign up for a trial GSuite account at https://gsuite.google.com/signup/basic/welcome  . This will be Account B.
4. Use any email to register as you won't need to confirm that email. 
5. When the wizard comes to the "Does your business have a domain?" confirm and enter `wearehackerone.com` (or any other domain that hosts the victim's email box) as in F552718. You may not use the same domain name at this stage, as I claimed it for the purposes of this PoC however you can do so when my GSuite trial expires. From this comes the requirement that the victim's email domain name must not be registered with Google prior to this attack. 
6. Once you saved the domain record with Google, stop there as there's no need to verify the domain.
7. At this stage the OneTap/GoogleYOLO popup will be showing on priceline.com when visited in the same browser session. It took me some time to get it to show however signing in and out of Google Account several times with the newly created GSuite credentials and then refreshing the priceline.com page helped. On another occasion a Gmail account, which I signed in in the same browser window helped too. You may need to play around with these until you see the newly created account to show in the list. F552723 
8. Once you have that, just sign in (`badca7@wearehackerone.com` in my case). You can confirm you accessed Account A by seeing the phone number you added in step (2). In the other browser window/session with Account A you can see that now there are two accounts showing in the top right corner and the profile data is blank.
9. Account takeover complete. F552724

# Notes

- IP used for this PoC: 139.59.90.143

## Impact

Attackers can take over any priceline.com account given they were able to register a specific domain with GSuite.

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
