---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1704035'
original_report_id: '1704035'
title: AWS Credentials Disclosure at ███
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2022-09-19T01:22:21.351Z'
disclosed_at: '2023-02-24T18:43:57.957Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- improper-access-control-generic
---

# AWS Credentials Disclosure at ███

## Metadata

- HackerOne Report ID: 1704035
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2023-02-24T18:43:57.957Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team!!
I found the config.json file, which contains sensitive information of AWS.

POC:
https://███████/config.json
```
{"aws": {
        "accessKeyID": "███████",
        "secretAccessKey": "██████████",
        "region": "███",
        "bucket": "██████",
        "endpoint": "https://s3.amazonaws.com"
    },
    "serverSettings": {
        "port": 443,
        "timeout": 18000000
    },
    "█████████": {
        "authorizationURL": "https://████/ms_oauth/oauth2/endpoints/oauthservice/authorize",
        "tokenURL": "https://████/ms_oauth/oauth2/endpoints/oauthservice/tokens",
        "clientID": "██████████",
        "clientSecret": "█████",
        "callbackURL": "https://████████/callback",
        "userProfileURL": "https://███/ms_oauth/resources/userprofile/me"
    }
}
```

## Impact

By using leaked AWS credentials or abusing credentials with misconfigured permissions, an attacker could try to gain access to sensitive information on the AWS account or perform arbitrary modification on the AWS resources.

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Use a browser to navigate to: https://██████/config.json

## Suggested Mitigation/Remediation Actions

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
