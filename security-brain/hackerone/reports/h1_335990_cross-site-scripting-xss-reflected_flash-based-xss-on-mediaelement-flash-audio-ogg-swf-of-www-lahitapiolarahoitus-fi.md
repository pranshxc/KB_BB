---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '335990'
original_report_id: '335990'
title: Flash-based XSS on mediaelement-flash-audio-ogg.swf of www.lahitapiolarahoitus.fi
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: localtapiola
created_at: '2018-04-11T16:16:39.552Z'
disclosed_at: '2018-04-13T12:10:12.310Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: www.lahitapiolarahoitus.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Flash-based XSS on mediaelement-flash-audio-ogg.swf of www.lahitapiolarahoitus.fi

## Metadata

- HackerOne Report ID: 335990
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: localtapiola
- Disclosed At: 2018-04-13T12:10:12.310Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
The lahitapiolarahoitus.fi contains an SWF-file which is vulnerable to reflected cross-site scripting attacks via crafted URL.

**Description:** 
The file `https://www.lahitapiolarahoitus.fi/wp-includes/js/mediaelement/mediaelement-flash-audio-ogg.swf` contains a XSS-vulnerability which allows malicious actor to create URLs which contain javascript. When the victim (anonymous or authenticated) opens this URL, the javascript is executed on the victim's session.

**Impact:**
The vulnerability allows an attacker to use every functionality on lahitapiolarahoitus.fi that the victim is able to use. In case of an admin-victim, the attacker can use this to gain RCE on the server by uploading a malicious shell-plugin. The vulnerability can also be used to redirect the victim to a malicious third-party domain and also to serve spoofed content on the lahitapiolarahoitus.fi-domain. If the myynti.lahitapiolarahoitus.fi uses domain-wide cookies, this vulnerability can possibly be used to read/write these cookies. 

## Browsers / Apps Verified In:

  * Latest Firefox
  * Latest Internet Explorer
  * Latest Edge

## Steps To Reproduce:

  1. Go to URL https://www.lahitapiolarahoitus.fi/wp-includes/js/mediaelement/mediaelement-flash-audio-ogg.swf?uid="]}))}catch(e){}alert(document.cookie)//
  2. Notice, that the user's cookies are shown.

## Mitigation

As the vulnerable files are removed in the latest Wordpress version, simply update your own version to the latest one. If the previous is not possible, just remove the swf-files as those are fairly rarely neede.

## Additional material

  * https://wordpress.org/news/2018/01/wordpress-4-9-2-security-and-maintenance-release/

## Related reports, best practices

  * https://hackerone.com/reports/134546

## Impact

The vulnerability allows an attacker to use every functionality on lahitapiolarahoitus.fi that the victim is able to use. In case of an admin-victim, the attacker can use this to gain RCE on the server by uploading a malicious shell-plugin. The vulnerability can also be used to redirect the victim to a malicious third-party domain and also to serve spoofed content on the lahitapiolarahoitus.fi-domain. If the myynti.lahitapiolarahoitus.fi uses domain-wide cookies, this vulnerability can possibly be used to read/write these cookies.

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
