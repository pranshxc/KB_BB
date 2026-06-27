---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '317931'
original_report_id: '317931'
title: Bypassing Homograph Attack Using /@ [ Tested On Windows ]
weakness: Violation of Secure Design Principles
team_handle: brave
created_at: '2018-02-20T16:51:53.302Z'
disclosed_at: '2018-02-23T06:03:51.214Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- violation-of-secure-design-principles
---

# Bypassing Homograph Attack Using /@ [ Tested On Windows ]

## Metadata

- HackerOne Report ID: 317931
- Weakness: Violation of Secure Design Principles
- Program: brave
- Disclosed At: 2018-02-23T06:03:51.214Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

__Bypassing Homograph Attack Using /@__

I look at on my previous report on #268984 and see patch code in the github https://github.com/brave/browser-laptop/commit/f2e438d6158fbc62e2641458b6002a72d223c366 I look at code at 

```
it('returns the punycode URL when given a valid URL', function () {
        assert.equal(urlUtil.getPunycodeUrl('http://brave:brave@ebаy.com:1234/brave#brave'), 'http://brave:brave@xn--eby-7cd.com:1234/brave#brave')
 })
```
And i think the punycode will return to ASCII just after `@` before it is not checked. And i give the try. and got some homograph attack. ( Correct Me If I Wrong )

## Products affected: 

 * Brave	0.20.27 ( Windows )

## Steps To Reproduce:

This is punycode URL ebаy.com@ebаy.com = xn--eby-7cd.com@xn--eby-7cd.com
Add to homepage.
```
Attempt : 
- ebаy.com@ebаy.com it'll become = ebаy.com@xn--eby-7cd.com 
- ebаy.com/ebаy.com it'll become = xn--eby-7cd.xn--com/eby-7fg.com
- ebаy.com/@ebay.com it'll become = ebаy.com/@xn--eby-7cd.com
```
if user input `ebаy.com/@brave.com` user will be redirect to `xn--eby-7cd.com` 
punycode failed return to ascii because brave just check after `@` not all of URL 

## Supporting Material/References:

Video : https://youtu.be/Zz7KV_R0Wp8

SS : 
{F265262}

Thanks

## Impact

User will be tricked by attacker to visit malicious link with punycode inside it.

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
