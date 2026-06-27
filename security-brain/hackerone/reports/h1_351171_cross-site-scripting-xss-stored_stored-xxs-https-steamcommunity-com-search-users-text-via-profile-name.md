---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '351171'
original_report_id: '351171'
title: Stored XXS @ https://steamcommunity.com/search/users/#text= via Profile Name
weakness: Cross-site Scripting (XSS) - Stored
team_handle: valve
created_at: '2018-05-13T17:41:15.480Z'
disclosed_at: '2018-05-24T21:57:17.440Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
asset_identifier: steamcommunity.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XXS @ https://steamcommunity.com/search/users/#text= via Profile Name

## Metadata

- HackerOne Report ID: 351171
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: valve
- Disclosed At: 2018-05-24T21:57:17.440Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear Valve security staff,


Short description
---------------------

There is a stored cross-site-scripting vulnerability present at the user search endpoint which can be exploited by modifying profile name of the would be attacking account. See POC picture.


Steps to reproduce
---------------------

1. Obtain a account to act as a attacker and log in
2. Go to https://steamcommunity.com/profiles/PROFILE_NUMBER/edit
3. Edit field "Profile Name" to contain short name, and the payload. For example: "__NAME'); alert(document.cookie+'__", without the outermost double quotes
4. With another browser or session, obtain a account to act as a victim and log in
5. Navigate to https://steamcommunity.com/search/users/#text=
6. Using the search field, search for the attacking account "__NAME'); alert(document.cookie+'__" without the outermost double quotes
7. Click "ADD AS FRIEND" button next to the profile name
8. Verify that clicking the button launches the payload and pops an alert dialog


Why is it there
---------------------

All culminates on AddFriend-function call on the following line of code in user search html and the fact, that the function call can be escaped. The payload is "__NAME'); alert(document.cookie+'__" without the outermost quotes in the snippet.
```
<a href="#" onclick="AddFriend(false,'PROFILE_NUMBER','NAME'); alert(document.cookie+''); $J(this).hide(); return false;" class="btnv6_blue_hoverfade btn_small btn_uppercase" style="display: none;">
    <span>Add as friend</span>
</a>
```

Impact and assesment
---------------------

As on any cross-site-scripting vulnerability. The top line would be that the attacker might steals cookies to abuse users session. For this particular vulnerability only by it self, successful exploiting is a bit more tricky, as currently the Profile Name -field only accepts 32 characters and it requires the victim to click on the button. Payloads can also utilize jQuery on the domain context.

As a mitigation of this, and vulnerabilities like this: addition to <, > and &, characters such as ' ; $ ( and ) should also be encoded when retrieved from the database, or even better, could be stored encoded.

PS. It was funny to see that many users had tried to exploit the Profile Name -field previously, as they show on the search when searching for "__alert(...)__". I hope I'm in time not to be on the duplicate pool!

## Impact

As on any cross-site-scripting vulnerability. The top line would be that the attacker might steals cookies to abuse users session. For this particular vulnerability only by it self, successful exploiting is a bit more tricky, as currently the Profile Name -field only accepts 32 characters and it requires the victim to click on the button.

As a mitigation of this, and vulnerabilities like this: characters such as ' ; $ ( and ) should also be encoded when retrieved from the database, or even better, could be stored encoded.

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://steamcommunity.com/search/users/#text=

**Verified**
Yes

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
