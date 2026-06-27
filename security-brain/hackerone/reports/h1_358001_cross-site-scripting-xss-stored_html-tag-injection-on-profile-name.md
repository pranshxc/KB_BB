---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '358001'
original_report_id: '358001'
title: HTML TAG INJECTION ON PROFILE NAME
weakness: Cross-site Scripting (XSS) - Stored
team_handle: gitlab
created_at: '2018-05-27T00:05:21.177Z'
disclosed_at: '2018-07-27T20:29:54.770Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# HTML TAG INJECTION ON PROFILE NAME

## Metadata

- HackerOne Report ID: 358001
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: gitlab
- Disclosed At: 2018-07-27T20:29:54.770Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Allows me to change the profile name to an image tag <img src="........"/> and convert it into an html code and this tag appears perfectly on the "snippets" page.

Suppose I include an image tag with source <img src="http://progress28.web.id/abc.jpg"> and when another user sees it on the "https://gitlab.com/snippets/1718284" page it will appear an image of an anonymous.

I can also add a header tag in the profile name with the tag "<h1>HACKED BY TALAOHU28</h1>" and will look perfect on the same page "https://gitlab.com/snippets/1718284".

Other tags that run perfectly include:
</br>
<div></div>
<a href=""></a>
<b></b>


Here's the complete payload I've made as the profile name

</br><h1>HACKED BY TALAOHU28</h1><img src="http://progress28.web.id/abc.jpg"></br><h1>I WANT TO BACK FREE</h1></br>

## Impact

other users can see the page "https://gitlab.com/snippets/1718284" as if being hacked by hackers

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
