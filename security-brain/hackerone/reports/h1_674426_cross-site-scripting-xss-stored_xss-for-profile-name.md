---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '674426'
original_report_id: '674426'
title: XSS For Profile Name
weakness: Cross-site Scripting (XSS) - Stored
team_handle: vanilla
created_at: '2019-08-15T09:48:11.561Z'
disclosed_at: '2020-03-25T19:41:54.386Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 32
asset_identifier: https://github.com/vanilla/community
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS For Profile Name

## Metadata

- HackerOne Report ID: 674426
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: vanilla
- Disclosed At: 2020-03-25T19:41:54.386Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

In short, if your username is something as simple as <script>alert(1)</script> this will not be filtered when viewing your profile page. The unfiltered script alert is echo'd underneath your image in your profile. This can be viewed by anyone viewing your profile (Although in some cases the browser will attempt to block it so you might not see it immediately - but it will show in the console etc).

While you are unable to change your username to have <> tags via the web, I noticed if I edited the name directly in the database I could get it to prompt. 

From there I found two ways to make your name accept tags. 

- via the API, you can create a user with a script tag as a name and it goes through fine. 
- via social logins. Although Facebook, Twitter and Google all block <> tags in their "Name" field, things like Github and Steam do not and the social login plugins take the "name" wholesale without any filtering. 

**Description:**

## Steps to reproduce:

You can ofcourse just edit the name of a user in the gdn_user table if you want to short circuit it. Otherwise... 

1. Call the API (Even via Swagger in the admin panel) with the following : (RoleId may need to be changed to suite local install)

{
  "bypassSpam": false,
  "email": "test@test.com",
  "emailConfirmed": true,
  "name": "<script>alert(1)</script>",
  "password": "P@ssw0rd",
  "photo": "",
  "roleID": [
    8
  ]
}

2. Login as this user/view this users profile via the front end web. You should see the alert. 

(And again alternatively you can set up OpenID/Social Logins with a provider that also allows script tags in the name and it will come through also)

## Anything else we should know?

While the web does block it so the exploit relies on either an API integration or a social login, I think relying on third parties to block script tags on their end so they don't get into the Vanilla DB is probably pretty dangerous. If Vanilla has inbuilt support for something like Github this would be a much larger problem etc.

## Impact

Standard XSS rules apply

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
