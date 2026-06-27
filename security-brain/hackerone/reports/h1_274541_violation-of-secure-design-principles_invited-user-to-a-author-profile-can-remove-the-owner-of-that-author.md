---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '274541'
original_report_id: '274541'
title: Invited user to a Author profile can remove the owner of that Author
weakness: Violation of Secure Design Principles
team_handle: paragonie
created_at: '2017-10-05T09:06:48.197Z'
disclosed_at: '2017-10-16T05:48:39.116Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Invited user to a Author profile can remove the owner of that Author

## Metadata

- HackerOne Report ID: 274541
- Weakness: Violation of Secure Design Principles
- Program: paragonie
- Disclosed At: 2017-10-16T05:48:39.116Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##SUMMURY:

-------------------------------------
A user invite another user to his author by giving ownership.
------------------
Later invited user can completely remove the real owner from  that author .
-------------------

-----------------------------------


##STEP TO REPRODUCE:

-----------------------------

1. Create two user ABC and XYZ.
--------------------
2. Create a author profile in user ABC and invite user XYZ to that author using public_id. Give the ownership to user XYZ.Now user XYZ has full access to that author profile.
---------------------
3. Now goto user XYZ account  and  remove user ABC from that author.
---------------
And see ABC is owner of that author is completely removed from  that author and ABC user cant able to access that Author.
---------------
4. finally user XYZ is the main owner of that author
------------



-----------------------
##FIX:

--------------------------------
check before invited user try to remove  real owner from his Author profile.
-----------
if so , access denied that invited user cant delete real owner from his author profile.
---------

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
