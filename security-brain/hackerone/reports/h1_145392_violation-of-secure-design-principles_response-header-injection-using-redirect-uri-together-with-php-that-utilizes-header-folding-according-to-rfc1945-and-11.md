---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145392'
original_report_id: '145392'
title: Response Header injection using redirect_uri together with PHP that utilizes
  Header Folding according to RFC1945 and Internet Explorer 11
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-06-17T13:20:10.321Z'
disclosed_at: '2016-08-17T07:27:52.561Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- violation-of-secure-design-principles
---

# Response Header injection using redirect_uri together with PHP that utilizes Header Folding according to RFC1945 and Internet Explorer 11

## Metadata

- HackerOne Report ID: 145392
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2016-08-17T07:27:52.561Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I noticed that the `redirect_uri` used to redirect users to any location on the page, passes in all data into a `header("Location..` without any validation. The problem is that PHP (current PHP-versions of Debian/Ubuntu, there seem to be a patch properly in place in other dists) actually built the header-function according to RFC1945 which says:

```
HTTP/1.0 headers may be folded onto multiple lines if each
continuation line begins with a space or horizontal tab. All linear
whitespace, including folding, has the same semantics as SP.
```
Ref: https://tools.ietf.org/html/rfc1945#page-11

This means that doing the following request:

http://nextcloud/index.php?redirect_url=/%3f%0d%0a%09set-cookie:+hello=yoyoo

Will result in the following response:
```
Location: http://nextcloud/?
	set-cookie: hello=yoyoo
```

The problem is that IE is actually not caring at all about that rule from RFC1945 and will strip the tab-character from that header and listen to it:

{F99965}

You should most likely disallow this character sequence completely so the failed backported versions of PHP won't do this. Properly secured PHP versions will fail doing the request due to new-lines in the header.

Regards,
Frans

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
