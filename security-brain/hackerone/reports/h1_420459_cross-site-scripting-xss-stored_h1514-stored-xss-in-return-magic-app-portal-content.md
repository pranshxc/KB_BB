---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '420459'
original_report_id: '420459'
title: H1514 Stored XSS in Return Magic App portal content
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2018-10-07T23:37:26.921Z'
disclosed_at: '2019-11-08T11:03:14.937Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# H1514 Stored XSS in Return Magic App portal content

## Metadata

- HackerOne Report ID: 420459
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2019-11-08T11:03:14.937Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
Stored XSS vulnerability was found in return magic app portal content which executes in the application domain in `https://services.alveo.io/dashboard-shopify/settings/portal/content` 

**Description:** 
It's been found that Return Magic app allows users to add HTML content to their return portal without sanitizing the HTML which makes it possible to inject malicious tags that can be used to execute arbitrary JavaScript through other users' sessions.

## Steps To Reproduce:
1. Install Return Magic app
2. Navigate to `https://<shop>.myshopify.com/admin/apps/returnmagic`
3. Open **Settings** tab from the top menu and then open **Portal** --> **Content** from the left menu 
4. For the textarea where you enter your portal content, click the **Code** icon and enter `Test <img src=x onerror=alert(2)>` then click **Save** 
5. Now each time a user opens the portal settings page, `alert(2)` will be executed.
6. XSS also triggers in `https://services.alveo.io/portal/search?shop=<shop>.myshopify.com` 
{F356974}

## Impact

Through this vulnerability a malicious user will be able to execute JavaScript through other user's sessions' which allows him to do malicious actions such as stealing sensitive information, submitting requests that bypass csrf protection ..etc

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
