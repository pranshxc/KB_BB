---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '423541'
original_report_id: '423541'
title: H1514 Server Side Template Injection in Return Magic email templates?
weakness: Code Injection
team_handle: shopify
created_at: '2018-10-13T22:34:15.431Z'
disclosed_at: '2019-04-04T17:35:23.641Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 400
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- code-injection
---

# H1514 Server Side Template Injection in Return Magic email templates?

## Metadata

- HackerOne Report ID: 423541
- Weakness: Code Injection
- Program: shopify
- Disclosed At: 2019-04-04T17:35:23.641Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Possible template injection in return magic email templates.

**Description:** 
I've been playing with return magic workflow email templates and there seems to be some kinda of template injection but I am not sure if it's exploitable or even valid.
Here is why I think it could be vulnerable: 
I set the email template to the following and then test the template and then the results go to my gmail inbox.
`{{ this }} ` -> `[Object Object]` 
`{{ this.__proto__ }}` --> `[Object Object]`
`{{ this.__proto__.constructor.name }}` --> `Object`
I couldn't go further but it seems like the backend is NodeJs.

## Steps To Reproduce:

1. Install Return Magic app
2. Navigate to `https://<shop>.myshopify.com/admin/apps/returnmagic`
3. Open Settings tab from the top menu and then open **Emails** --> **Workflow** from the left menu
4. Click Edit for any email template then at the editor click the code icon and enter `{{this}}` 
5. Go back to **Workflow** page and click **Send me a test email** for the template you edited then enter your email and check your inbox.
6. You'll see `[Object Object]`

## Supporting Material/References:
{F360290}

{F360291}

## Impact

Could be a Server Side template injection that can be used to take over the server ¯\_(ツ)_/¯

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
