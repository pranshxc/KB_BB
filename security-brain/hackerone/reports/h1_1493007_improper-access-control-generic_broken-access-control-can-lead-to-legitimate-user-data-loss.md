---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1493007'
original_report_id: '1493007'
title: Broken access control, can lead to legitimate user data loss
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2022-02-27T10:19:35.520Z'
disclosed_at: '2022-04-07T20:03:26.165Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-access-control-generic
---

# Broken access control, can lead to legitimate user data loss

## Metadata

- HackerOne Report ID: 1493007
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2022-04-07T20:03:26.165Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
During testing the security of ██████████ I found another possible attack vector:
(There are two reports preceding this one -  https://hackerone.com/reports/1489470 and  https://hackerone.com/reports/1489744)

I will try to explain:
When an user need access to that information system he fills a request form at:
https://█████████/████████
or
https://█████████/██████
After submitting the form the server response contains a █████████ which identifies this user request.
Then  the request is reviewed by an administrator, and he decides if user access will be granted or rejected.
The vulnerability I found is that unauthorized person can access the end point responsible for deleting user requests - █████████ and by providing just the ███ parameter he can delete any request.

## References

## Impact

An attacker can delete  legitimate user requests, disturbing the normal operation  of the system and causing data loss.
The user request ids are sequential numbers - my requests were given ids - ████████, so the attacker can delete all requests in the system by accessing the ████ end point with each ██████ from ██████████.

## System Host(s)
███████

## Affected Product(s) and Version(s)
██████████

## CVE Numbers


## Steps to Reproduce
1.  Activate Burp proxy, go to https://███/██████████, fill and submit the form (screenshot1)
2. Inspect server response in Burp and take a note of the returned █████ (screenshot2) which is number, referencing this user access request
3. (optional) we can confirm our request is in the system by performing the attack described in the other report I made (https://hackerone.com/reports/1489470) - resulting in our request being exfiltrated from the database:
execute following command, and replace the █████ parameter with the one you noted on step 2 (screenshot)
curl https://██████/██████████ -X POST -data="url=%2F████&██████████=████████" -k

4. Deleting the request - CAUTION - execute this step only by referencing ██████████ for requests, you made otherwise you will delete legitimate user request!(sceenshot4)
the command abusing the delete request endpoint is:
curl https://██████/███████████████ -X POST -data="url=%2F███████&███████=██████" -k

5. (optional) to confirm request is deleted you can execute again Step 3, which now responds with empty body - the request is no longer present in the database.

## Suggested Mitigation/Remediation Actions
The ██████████ endpoint should perform check if the user is logged in and authorized to use it.

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
