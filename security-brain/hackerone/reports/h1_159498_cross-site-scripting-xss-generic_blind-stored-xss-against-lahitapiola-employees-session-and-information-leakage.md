---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159498'
original_report_id: '159498'
title: Blind Stored XSS Against Lahitapiola Employees - Session and Information leakage
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localtapiola
created_at: '2016-08-15T15:36:39.469Z'
disclosed_at: '2017-02-22T11:24:45.093Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 69
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Blind Stored XSS Against Lahitapiola Employees - Session and Information leakage

## Metadata

- HackerOne Report ID: 159498
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localtapiola
- Disclosed At: 2017-02-22T11:24:45.093Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I am pretty sure that I found a vulnerability similar to https://hackerone.com/reports/135154.

An adversary can use the "Lähetä viesti"-functionality of the LähiTapiola Asiakassalkku to send a malicious file. When the customer service opens the file, an XSS will execute and will leak user IP address and Lähitapiola session cookies and also for example the "tapiola.cem.uid" which I suspect is the username of the employee (e.g. "██████████").

## Steps to reproduce:
1. Log in to the Lähitapiola customer site (https://www.lahitapiola.fi/henkilo/asiakaspalvelu/asioi-verkossa/kirjaudu-verkkoon).
2. Navigate to the "Lähetä viesti"-page (https://verkkopalvelu.tapiola.fi/a2/AskoWeb/faces/sivut/viesti/laheta.xhtml).
3. Fill the fields with anything you want and click the "Lataa liite"-button and upload a malicious file (see the attached file kirje.txt).
4. Send the message.
5. Navigate to "Postilaatikko" and make sure that the message was sent and that the attachment is properly uploaded (see the attached image1.png and image2.png).
6. The attached kirje.txt contains a SVG image file which is modified to contain malicious javascript that sends an AJAX-request to attacker's server (mine) and adds website cookies to the URL as GET-parameter. As the Lähitapiola employees are probably using Internet Explorer, the IE will sniff the MIME type from the file and open it as SVG instead of text/plain and it will trigger the XSS.

## Proof of exploitation
See the attacked file xsspoc.txt for an proof. The file is from my nginx-server logs and in the file you can see that an Lahitapiola employee (notice the IP-address) has opened the attachment and it triggered the XSS which sent the employees cookies to my server.

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
