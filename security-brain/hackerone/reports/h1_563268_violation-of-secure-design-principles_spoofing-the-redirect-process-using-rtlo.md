---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '563268'
original_report_id: '563268'
title: Spoofing the redirect process using RTLO
weakness: Violation of Secure Design Principles
team_handle: vanilla
created_at: '2019-05-03T11:51:01.753Z'
disclosed_at: '2020-06-28T22:58:04.116Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: '*.vanillacommunities.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Spoofing the redirect process using RTLO

## Metadata

- HackerOne Report ID: 563268
- Weakness: Violation of Secure Design Principles
- Program: vanilla
- Disclosed At: 2020-06-28T22:58:04.116Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

### Description:

I was testing this subdomain `rinkerboats.vanillacommunities.com` and after some search, I found this path
```url
https://rinkerboats.vanillacommunities.com/home/leaving?Target=https://google.com/
```
which used to redirect the users to external websites now this is good because you tell the user where he will be redirected on the above link the message will be
```
You are now leaving Rinker Boat Company. Click the link to continue to https://google.com/
```
and he will click on the link to be redirected now I found a way to spoof this process to show a wrong domain to the user this way is RTLO (Right to Left Override ) this makes the text wrote from the right to left for example if we have `flex` if we use RTLO it will be `xelf` but the website will see it as `flex` so this is an issue because I can do it with a domain which will spoof the process like that
```
https://rinkerboats.vanillacommunities.com/home/leaving?Target=https://%E2%80%AE@moc.rettiwt
```
the message will be
```
You are now leaving Rinker Boat Company. Click the link to continue to https://@moc.rettiwt.
```
but when the user clicks on `https://.twitter.com@` he will be redirected to `https://moc.rettiwt/` this can be used to spoof the process and redirect the users to other websites.

**similar report #299403**

### POC:

{F483412}

{F483411}

**Video:**
{F483421}

### Fix:

you can easily block any URL encoding characters or filter them.

## Impact

This bug can be used to spoof the users using your website to redirect them to unsafe websites.

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
