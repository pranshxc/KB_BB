---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '984947'
original_report_id: '984947'
title: Tab nabbing via window.opener.location (target "_blank")
weakness: Open Redirect
team_handle: automattic
created_at: '2020-09-17T19:35:31.355Z'
disclosed_at: '2020-12-26T16:42:32.124Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: www.tumblr.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Tab nabbing via window.opener.location (target "_blank")

## Metadata

- HackerOne Report ID: 984947
- Weakness: Open Redirect
- Program: automattic
- Disclosed At: 2020-12-26T16:42:32.124Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
When you open a link using target="_blank", the page that opens in a new tab get access to the initial tab and change its location using the window.opener.location function.
## Platform(s) Affected:
website

## Steps To Reproduce for the first target _blank:
  1. First target "_blank" 
  1. On https://www.tumblr.com/customize add the following script : 

```javascript
<script>
window.opener.location = 'https://davidebove.com/blog/2016/05/05/target_blank-vulnerability-test-page/';
</script>
``` 

  1. Send to test account your link blog.
  1. On the test account open the link ; the initial page will be changed.
  1. Watch the POC video if you want more details.

## Steps To Reproduce for the second target _blank:
  1. Second target "_blank" 
  1. On https://www.tumblr.com/customize add the following script : 

```javascript
<script>
window.opener.location = 'https://davidebove.com/blog/2016/05/05/target_blank-vulnerability-test-page/';
</script>
``` 

  1. Send to test account random message.
  1. On the test account click on the account name and the blog view page will be opened, next click on account blog link.
  1. Watch the POC video if you want more details. 

## Steps To Reproduce for the third target _blank:
  1. Third target "_blank" 
  1. On https://www.tumblr.com/customize add the following script : 

```javascript
<script>
window.opener.location = 'https://davidebove.com/blog/2016/05/05/target_blank-vulnerability-test-page/';
</script>
``` 
  1. Send to test account your link blog.
  1. On the test account navigate somewhere, click on the name account of sender ; the initial page will be changed.
  1. Watch the POC video if you want more details.

## Supporting Material/References:

  * don't forget to close all tabs
  * POCs ! 
  * relative report that can maybe help you : https://hackerone.com/reports/179568

## Impact

It can allow an attacker to open a malicious site on the victim account.
Perform phishing attacks.

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
