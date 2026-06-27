---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '75702'
original_report_id: '75702'
title: No rate limit which leads to "Users information Disclosure" including verfification
  documents etc.
weakness: Violation of Secure Design Principles
team_handle: enter
created_at: '2015-07-15T22:19:27.309Z'
disclosed_at: '2015-11-27T06:24:38.895Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# No rate limit which leads to "Users information Disclosure" including verfification documents etc.

## Metadata

- HackerOne Report ID: 75702
- Weakness: Violation of Secure Design Principles
- Program: enter
- Disclosed At: 2015-11-27T06:24:38.895Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**HOST**
api.romit.io

**Endpoint**
/v0/cash/auth/login

**Issue**
When an attacker tries to login at app.romit.io, he is prompted to enter the PIN . There is no rate limit to verify this. Although there is a an authorization header `Authorization: Credential=b67b0b10571ac00444de3cffde0b5b05, SignedHeaders=host;x-locale;x-location-id;x-request-date;x-session-id, Signature=976aeeeb8a3d07aa9a927a4d8972c819674b4385a6466b17aad345d5cee1c082` which sends a signature with the request,which is generated using the PIN specified by the user, the attacker can simply generate this signature[see attached calSignature.js] Now this can be used to bruteforce the PIN but its pretty useless because the server prompts for the SMS code or GA code which the attacker has no way to know.

Now , it gets interesting because as soon as the correct pin is added, the users info is added to the operator waller(in this case the attackers wallet) including all the verification documents, email, DOB etc.[see attached pictures]
The attacker can see any users info once he knows the users phone number.

**PoC**
1. Setup an account at app.romit.io, use your apiKey, apiSecret and Location-ID to setup.
2. Now click on Send Money, add the Phone Number you want to bruteforce.
3. Once you get the correct PIN the users info will be added to your operator wallet.

**Solution**
1.  I believe there should be rate limit.
2. User should be added to operator wallet only after he/she has provided the SMS /GA code.


Thanks
crab

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
