---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141463'
original_report_id: '141463'
title: Stored XSS via AngularJS Injection
weakness: Cross-site Scripting (XSS) - Generic
team_handle: drchrono
created_at: '2016-05-27T16:01:41.237Z'
disclosed_at: '2016-06-13T19:02:06.315Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS via AngularJS Injection

## Metadata

- HackerOne Report ID: 141463
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: drchrono
- Disclosed At: 2016-06-13T19:02:06.315Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi All,
I've found a stored XSS vulnerability via an Angular Template Injection in the messages referral address field.

##Description
After visiting ``https://1337test.drchrono.com/messages/referrals/contacts/```, you can enter new contact information. In the field for the address, if enter [[5*5]], when the referrals contact overview will show the address as 25. This indicates an injection. 

Opening the browser console and using the command angular.version, we can see you are using 1.1.5. So, entering the address for a contact as ```[[constructor.constructor('alert(document.cookie)')()]]```, saving and reloading the page, an stored XSS is executed {F96481}

##Steps to reproduce
1. Create a doctors account
2. Visit ```https://1337test.drchrono.com/messages/referrals/contacts/```
3. Add a new contact
4. In the address field, enter ```[[constructor.constructor('alert(1)')()]]```

Confirm the alert pop up with **1** in it.

##Vulnerability
The stored xss could be used for a complete account take over if an admin visited this contact page. An attacker only needs permission to create a referral contact to store the payload. In the example image, I've printed all cookies to the screen but this could easily be sent to a remote endpoint.

Please let me know if you have any questions.
Pete

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
