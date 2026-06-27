---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '107960'
original_report_id: '107960'
title: Reflected File Download in community.ubnt.com/restapi/
team_handle: ui
created_at: '2016-01-03T17:39:43.907Z'
disclosed_at: '2017-05-27T08:36:53.903Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
---

# Reflected File Download in community.ubnt.com/restapi/

## Metadata

- HackerOne Report ID: 107960
- Weakness: 
- Program: ui
- Disclosed At: 2017-05-27T08:36:53.903Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

https://community.ubnt.com/restapi/vc/authentication/sessions/Ubiquiti_update.cmd?restapi.response_format=json&callback=\%22||calc||

The above URL is vulnerable to RFD. Here is the proof of concept:

Browser Chrome:

* Embedded the above URL in html 5 anchor tags with download attribute:

```
<a href='https://community.ubnt.com/restapi/vc/authentication/sessions/Ubiquiti_update.cmd?restapi.response_format=json&callback=\%22||calc||' download='ubiquiti_update.cmd'>Download</a>
```

We can embedded this on any webpage and the moment user clicks on, it gets automatically download and when clicked can compromise the victim PC by executing any commands. (a calculator pops up in this case) 

Browser **IE10/8**:

* Give the URL directly in IE 10/8 and it directly download a file named `Ubiquiti_update.cmd`. The moment user clicks on the file, it executes and a calculator pops up.


Browser Firefox:

* Embedded the download link in such a way  that user has to do save link as option in firefox and downloads the file `ubiquiti_update.cmd`.

```
<a href='https://community.ubnt.com/restapi/vc/authentication/sessions/Ubiquiti_update.cmd?restapi.response_format=json&callback=\%22||calc||' download='ubiquiti_update.cmd' onclick="return false">Download</a>
```

I can give any commands inside the file as I want and inturn use this for a complete victim machine compromise. If victim checks where the download occurs, it will show as `community.ubnt.com`.

References about this attack:

http://www.paulosyibelo.com/2015/10/coinbase-reflected-file-download.html (RFD reported in coinbase)
https://www.trustwave.com/Resources/SpiderLabs-Blog/Reflected-File-Download---A-New-Web-Attack-Vector/  (original research work)

**Mitigation**:

Callbacks should contain only alphabets and not special characters. All special characters much be stripped of before reflecting it in the response !

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
