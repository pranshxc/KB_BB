---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1094151'
original_report_id: '1094151'
title: Leaking Rockset API key on Github
weakness: Cleartext Storage of Sensitive Information
team_handle: rockset
created_at: '2021-02-03T17:54:12.599Z'
disclosed_at: '2021-03-02T16:02:20.439Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: api.*.rockset.com
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Leaking Rockset API key on Github

## Metadata

- HackerOne Report ID: 1094151
- Weakness: Cleartext Storage of Sensitive Information
- Program: rockset
- Disclosed At: 2021-03-02T16:02:20.439Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
We all know that Github is great, but it runs the risk of some credentials being revealed by mistake. In this case I found a Rockset API key, This API key is not in the current code, but it is visible in an old commit.

## Steps To Reproduce:
You can find the leak in this link : https://github.com/rockset/recipes/pull/19/files

```
        /* Getting the distance covered by each vehicle using the latest and oldest locations */
        distance_for_vehicles AS (
        SELECT
            ST_DISTANCE(
@@ -128,7 +147,7 @@
    'q4': query4 
}

api_key = "skZMJRZSXLZZj5HAdBjNxUfZbarWV5dLqfVO6U623zW5KROzfY0vNRa22ToZfRRe"
```

Then I visited the documentation of Rockset ( https://docs.rockset.com/rest-api/ ) and I found this way to check if the API key is revoke or not
```
curl --request GET \
    --url https://api.rs2.usw2.rockset.com/v1/orgs/self/users/self/apikeys \
    -H 'Authorization: ApiKey skZMJRZSXLZZj5HAdBjNxUfZbarWV5dLqfVO6U623zW5KROzfY0vNRa22ToZfRRe'
```
and I got this answer:
```
{"data":[{"created_at":"2019-10-22T06:08:37Z","name":"K1","key":"skZMJRZSXLZZj5HAdBjNxUfZbarWV5dLqfVO6U623zW5KROzfY0vNRa22ToZfRRe","last_access_time":null,"created_by":null}]}
```
So I could verify that it was not revoked

## Impact

I just checked that the key was not revoked. I didn't try anything with the token  to be prudent, and I don't know the real impact of this, But I think it is a good idea to share this with you, to avoid any risk that may grow.

Regards!

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
