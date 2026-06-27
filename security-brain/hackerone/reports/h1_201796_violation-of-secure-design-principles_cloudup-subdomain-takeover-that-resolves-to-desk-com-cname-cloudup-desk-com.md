---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '201796'
original_report_id: '201796'
title: cloudup Subdomain Takeover That resolves to Desk.com ( CNAME cloudup.desk.com
  )
weakness: Violation of Secure Design Principles
team_handle: automattic
created_at: '2017-01-28T18:13:14.150Z'
disclosed_at: '2017-02-02T14:16:27.727Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
tags:
- hackerone
- violation-of-secure-design-principles
---

# cloudup Subdomain Takeover That resolves to Desk.com ( CNAME cloudup.desk.com )

## Metadata

- HackerOne Report ID: 201796
- Weakness: Violation of Secure Design Principles
- Program: automattic
- Disclosed At: 2017-02-02T14:16:27.727Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

While Looking On The CloudUp Website I found That One of The Subdomain of CloudUp [HELP](help.cloudup.com) was Hosted on [Desk](Desk.com) and I think tHe Desk Account of Cloudup was Expired or Canceled by any cause So I have Checked The Site for its CNAME and The CNAME was Resolving to 
###CNAME	http://cloudup.desk.com
So I Tried to Make an Account on [Desk](desk.com) With the same as The CNAME Cloud.desk.com And I was Successful in this Coz Of The Account of cloudup was Expired or cancelled, Now I have setup my page on the site.


But Due to some Problem The Main Domain ***help.cloudup.com (See Screenshot Below 0.png) is Showing SSL Error Maybe due to expired Certificate I'm Not sure as I'm just a Started still have to learn many things! 
So Due to the Error I'm unable to Show my Message on The Main Domain But Still I have Full Control over The CNAME ( See Screenshots) 

Hope This Will Be Resolved

Thanks,
Muhammad Khizer Javed

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
