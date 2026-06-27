---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '170301'
original_report_id: '170301'
title: Invalid username updating
team_handle: rubygems
created_at: '2016-09-18T23:56:51.907Z'
disclosed_at: '2016-10-17T11:58:16.808Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: rubygems.org
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Invalid username updating

## Metadata

- HackerOne Report ID: 170301
- Weakness: 
- Program: rubygems
- Disclosed At: 2016-10-17T11:58:16.808Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Rubygems,

This is my first report on Hackerone, so please tell me if you need further information.

This vulnerability/glitch uses the 'Edit Profile' page.

How to do it:
1. Login to any account on Rubygems

2. Go to your profile

3. Go to 'Edit Profile'

4. In Handle, put the invalid username

5. Click 'Update'

6. It will show the "invalid username" error message, but in the top right corner, it will change the username to whatever you put it handle, whether it was valid or invalid. 

If it was invalid, when you leave that page/reload it, it will return the username to it's previous state, but this allows for any username in that space for a temporary amount of time, which could have potential for harmful code.

Another issue with this, besides the obvious glitch, is that in browsers with XSS blockers (Chrome, IE, etc.), it moves the avatar icon downward and the name section will be blank. (See pictures for an example)


Hopefully this has enough information. Thanks for reading

- Jack

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
