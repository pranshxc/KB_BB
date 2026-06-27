---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260838'
original_report_id: '260838'
title: Special characters are not filtered out on profile fields
team_handle: legalrobot
created_at: '2017-08-16T22:33:17.411Z'
disclosed_at: '2017-08-26T23:24:32.058Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Special characters are not filtered out on profile fields

## Metadata

- HackerOne Report ID: 260838
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-08-26T23:24:32.058Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hi there , 

While looking around into your web application I noticed in the fields Firstname and Lastname you can set a url . example ` ( http://www.evilsite.com) ` .  where I am using special characters like `://` and `.` . but when I try out other special characters - or particularly a payload such as `"><svg/onload=prompt(1)>` , it will not be allowed in the first name and last name fields . which means as a protection mechanism this is getting filtered out along with the additional special characters . again using null valus like `%00%` , is allowed in the fields and updates First name or last name , so it means when you are trying to update your name with such values your name is getting reverted back to the old one .

The intended behavior is not applied for all cases , that is why first name and last name can be updated with multiple special characters and null values . I think usage of special characters should be controlled and checked again by you guys . as you are filtering out payloads which potentially contain multiple special characters but you are allowing usage of special characters in under few circumstances . 

I am also attaching a video . Hope you will check and get back with a response soon . 

Thanks .

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
