---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1004833'
original_report_id: '1004833'
title: Cross-site Scripting (XSS) - DOM - iqcard.informatica.com
weakness: Cross-site Scripting (XSS) - DOM
team_handle: informatica
created_at: '2020-10-10T21:10:57.716Z'
disclosed_at: '2020-10-13T09:22:13.451Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Cross-site Scripting (XSS) - DOM - iqcard.informatica.com

## Metadata

- HackerOne Report ID: 1004833
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: informatica
- Disclosed At: 2020-10-13T09:22:13.451Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello all

I found a DOM based XSS at iqcard.informatica.com

# Description

After finding the path **iqcard.informatica.com/pub/fujitsu/fm3v2/player/attach.html**. I noticed that the code inside attach.html was vulnerable to DOM XSS, due to the fact of the javascript *document.location function. search*. The code below illustrates the code contained in the attach.html file

```
<HTML>
<HEAD>
<SCRIPT>
function GetAttach()
{
	var strSearch = document.location.search
	strSearch = strSearch.substring(1)
	
	document.location.replace(strSearch)
}
</SCRIPT>
</HEAD>
<BODY onload='GetAttach()'>


</BODY>
</HTML>
```
As can be seen through the code above, the variable * strSearch * receives everything that comes from the URL after the character? and then insert it into the function *document.location.replace ()*. Through this scenario we have some possibilities.

1 - We can direct the user to any page we want for example:

```
https://iqcard.informatica.com/pub/fujitsu/fm3v2/player/attach.html?evil.com
```


2 - We can run a DOM Based XSS, running the javascript schema, javascript: alert (1);

```
https://iqcard.informatica.com/pub/fujitsu/fm3v2/player/attach.html?javascript:alert(1)
```


# PoC 

I uploaded a video and an image.

## Impact

An attacker can redirect a user to a malicious page or execute XSS attacks against users of the application or use that domain as a phishing vector to attack other users of informatica.com

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
