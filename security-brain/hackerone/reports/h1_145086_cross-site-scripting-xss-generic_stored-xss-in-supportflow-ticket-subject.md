---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145086'
original_report_id: '145086'
title: Stored XSS in SupportFlow Ticket Subject
weakness: Cross-site Scripting (XSS) - Generic
team_handle: iandunn-projects
created_at: '2016-06-16T04:41:51.873Z'
disclosed_at: '2016-06-28T19:44:34.721Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in SupportFlow Ticket Subject

## Metadata

- HackerOne Report ID: 145086
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: iandunn-projects
- Disclosed At: 2016-06-28T19:44:34.721Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

SupportFlow contains an XSS vulnerability in how it handles ticket subjects in the admin-side ticket form, because the subject is not escaped before being used in the `value` attribute of the subject input element.

This first requires wptexturize to be disabled (not that uncommon):

```add_filter( 'run_wptexturize', '__return_false' );```

Then, create a ticket with a subject like this:

```
"><script>alert('hi');</script>
```

The next time someone views that ticket (any other user) in the admin area at _SupportFlow -> All Tickets -> [Ticket]_, XSS is triggered.

This is due to this line not using `esc_attr()` on the title value (core does not do this automatically):

https://github.com/SupportFlow/supportflow/blob/71a6053848c523f7b50b61a1f3770013badc76c0/classes/class-supportflow-admin.php#L905

I've attached a screenshot demonstrating the XSS `alert` - please let me know if you have any questions or if I can clarify anything.

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
