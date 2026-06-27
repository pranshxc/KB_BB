---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1176794'
original_report_id: '1176794'
title: Specific Payload makes a Users Posts unavailable
weakness: Uncontrolled Resource Consumption
team_handle: fetlife
created_at: '2021-04-27T11:59:43.265Z'
disclosed_at: '2022-01-26T04:10:51.338Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 45
asset_identifier: fetlife.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Specific Payload makes a Users Posts unavailable

## Metadata

- HackerOne Report ID: 1176794
- Weakness: Uncontrolled Resource Consumption
- Program: fetlife
- Disclosed At: 2022-01-26T04:10:51.338Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Good Morning, 

Like we talked about in the email, I'm reporting an issue that I've found that is possible, by crafting a specific payload, other users that try to access **/posts** of a user will face the **500 Internal Server Error** issue, not only when they access the specific crafted post. With this, the posts of the user will be blocked for other users. This could cause other problems like people possibly doing this on other's accounts and blocking all their posts for other users or it could be chained with some other vulnerability in the future.

I found this issue when I was fuzzing with the markdown as I saw you guys were using **Links**, so trying some HTML encodings led me to the following payload: `[PoC](&#65534;(&#41;)`.
 - `&#65534;` decoded will endup a [invalid character](https://charbase.com/fffe-unicode-invalid-character)
 - `&#41;` decoded will endup a `)`. 

With this, we can see that the markdown doesn't take our encoding very well which then causes a 500 Internal Server Error and blocks the **Posts** of any user to other users.

Proof that the **Fetlife Security Team** gave me the **go-ahead** to report this issue. 

{F1280132}

Steps to Reproduce
=====================

1. Go to **Write Post**
2. On the **Body** insert the following payload `[PoC](&#65534;(&#41;)`

{F1280189}

3. Click on **Express Yourself**
4. We are now faced with the **500 Internal Server Error** and if we try to access https://fetlife.com/users/OUR_USER_ID/posts, we can see that our posts are completely blocked for us and everyone and that we're still faced with a **500 Internal Server Error**.

Final
=====================
Thank you for your time, best regards, Rafael Castilho

## Impact

This could cause other problems like people possibly doing this on other's accounts and blocking all their posts for other users or it could be chained with some other vulnerability in the future.

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
