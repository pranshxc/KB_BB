---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '300454'
original_report_id: '300454'
title: '[www.zomato.com] Privilege Escalation - /php/restaurant_menus_handler.php'
weakness: Privilege Escalation
team_handle: zomato
created_at: '2017-12-25T13:27:52.919Z'
disclosed_at: '2018-03-29T17:00:35.760Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# [www.zomato.com] Privilege Escalation - /php/restaurant_menus_handler.php

## Metadata

- HackerOne Report ID: 300454
- Weakness: Privilege Escalation
- Program: zomato
- Disclosed At: 2018-03-29T17:00:35.760Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Introduction
In the following ██████████ the endpoint `/php/restaurant_menus_handler.php` was found. This endpoint is meant solely to be accessible for admins, however due to insufficient protections normal users can access this endpoint too. This results in any Zomato user being able to edit and remove menu's from any restaurant. The following actions have been found in the JS file but there might be more: `menu_collected`, `toggle-res-menu-type`, `clear_menu_tool`, `change-menu-type`.

#POC
Toggle-res-menu-type will be used in the POC since it switches between text and image menu's which makes it very easy to see the change happen on the page of the restaurant. When switching to text the images of the menu will disapear (and reappear when enabled).

Go to https://www.zomato.com/████ and view the images under the menu section. After that submit the following JS code in the developers console. After this reload the page and the menu images should be gone. Do it once more and the images should reappear again.

```js
$.ajax({url:"/php/restaurant_menus_handler.php",type:"POST",data:{action:"toggle-res-menu-type",res_id:██████}
```

## Impact

Any user can delete and edit any menu of any restaurant. The reason is that an admin endpoint has insufficient access protection.

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
