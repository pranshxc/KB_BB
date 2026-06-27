---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '135797'
original_report_id: '135797'
title: Session Fixation
weakness: Violation of Secure Design Principles
team_handle: enter
created_at: '2016-05-02T15:12:07.605Z'
disclosed_at: '2016-06-22T12:26:59.678Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- violation-of-secure-design-principles
---

# Session Fixation

## Metadata

- HackerOne Report ID: 135797
- Weakness: Violation of Secure Design Principles
- Program: enter
- Disclosed At: 2016-06-22T12:26:59.678Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
-------------

Your login flow is vulnerable to session fixation. This can allow an attacker to steal a valid user session from a victim.

Steps to reproduce
--------------

1. As the attacker go to https://wallet.sandbox.romit.io (but do not login!) and check the cookies `romit.sandbox.session` and `SANDBOX-XSRF-TOKEN`, that are set. For example:

    ```
SANDBOX-XSRF-TOKEN=AAG02cId-yyza3k8uhQR7JKuB-4YOmhizkjM; 
romit.sandbox.session=s%3AEHm0kA9uwWYHayOwdRQXbuZWEIRIliQZ.ndejz36ofa52c9ENnApLuaLkMnTYCot3IiY1qdTvz0w;
```
2. Now simulate the victim by opening a second browser and setting those two cookies.
3. As the victim, login in the second browser.
4. As the attacker, go to https://wallet.sandbox.romit.io (using the first browser / same cookies as in step 1). You are now logged in to the victims account.

Possible exploitation scenarios
---------------

This can be exploited if there is another bug like HTTP Response Splitting on your website. 

But a far easier way is to exploit this on shared computers. For example in a library, as an attacker open https://wallet.sandbox.romit.io (but do not login!) and keep note of the cookies as above in step 1. Then simply go away and now when a victim will use the same computer and try to login, the attacker will have access to the victims account.

Mitigation
--------------

If you assign a new session when someone logs in, this flaw should be fixed.

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
