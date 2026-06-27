---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '915573'
original_report_id: '915573'
title: Reflected XSS on ███████ page
weakness: Cross-site Scripting (XSS) - Generic
team_handle: deptofdefense
created_at: '2020-07-04T22:02:35.204Z'
disclosed_at: '2020-07-30T17:54:08.060Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS on ███████ page

## Metadata

- HackerOne Report ID: 915573
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: deptofdefense
- Disclosed At: 2020-07-30T17:54:08.060Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The page at https://█████/NtMView.php is vulnerable to reflected cross-site scripting. 

**Description:**
The page takes a user input in the form of a drop down list, then uses that text in the resulting page ( ███████ ). An attacker can intercept the query to the page and insert an XSS payload, as shown in ██████████. 

This input is then displayed back to the user, popping up the XSS payload ██████████. The XSS payload is actually inserted a number of times into the resulting HTML, which can be seen in ████████. This results in numerous pop ups to the user. 

## Step-by-step Reproduction Instructions
While intercepting requests with a proxy such as Burp, carry out the following steps

1. Visit the page at https://██████/usnotice.php
2. Select a value from the drop down list and press "View Now"
3. Add an XSS payload to the POST parameters,  eg, ``<script>alert('xss')</script>``
4. Observe on the next page the XSS pop-ups


## Suggested Mitigation/Remediation Actions
Any user controlled input should be filtered by the application to remove special characters such as  ``<`` and ``>``, as well as special words such as ``script``. 

For further guidance, see: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

## Impact

In this instance, the only person the XSS affects is myself, ie, Self-XSS. This could be weaponised to affect other users though, for example by being placed in a web form on an attacker controlled page, then tricking a user to click the link to visit the .mil page. An attacker who exploited this vulnerability could rewrite the contents of the page, potentially redirecting users to further malicious sites, or temporarily defacing the .mil page

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
