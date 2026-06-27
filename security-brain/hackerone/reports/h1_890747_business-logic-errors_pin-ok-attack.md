---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '890747'
original_report_id: '890747'
title: PIN OK attack
weakness: Business Logic Errors
team_handle: qiwi
created_at: '2020-06-04T11:40:13.603Z'
disclosed_at: '2021-02-17T08:57:19.337Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
tags:
- hackerone
- business-logic-errors
---

# PIN OK attack

## Metadata

- HackerOne Report ID: 890747
- Weakness: Business Logic Errors
- Program: qiwi
- Disclosed At: 2021-02-17T08:57:19.337Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

PIN OK attack is an attack when a wedge-device (created for MiTM) is used to substitute the response from the card during an offline-PIN check and say that PIN was correct.
Reproduction steps:
* An attacker with a stolen card without the correct PIN knowledge can use either a so-called wedge device for carrying out the "man-in-the-middle" attack and to use attended/unattended terminals or their own terminals which work only with DDA modes.
* An attacker is making a payment for £100 using a chip. The card sends to the terminal its CVM list. The first rule in the CVM list for your card is "4201 Encrypted PIN online", which is correct and the CVM list should be protected with CDA. However if DDA is chosen, it's possible to conduct the CVM Tampering and to change the first CVM rule to the "offline PIN".
* When Offline PIN was used but no PIN provided, your card sets "Byte 2 Bit 3 = 1, Byte 2 Bit 2 = 1" in IAD/CVR field indicating failed PIN verification, which can be used for detection of a fraudulent transaction on the processing side
* And fraudulent Qiwi transaction has been authorised at 04 June 2020 10:37 GMT on the issuer's side even though there is no "Offline PIN Verification Successful" in IAD and no online PIN was presented.

The account is +79999913370, Card *0760

Fix:
Even if cards like yours support CDA for EMV, for terminals that don't support them, you should check in CVR that PIN was correctly presented AND checked on the card. Default settings here would be:
When your card actually verified PIN offline, the chip will set CVR
Byte 1 Bit 1 = 1 Offline PIN Verification Successful

But when no offline PIN verification was made, it will set
Byte 4 Bit 6 = 1 Offline PIN Verification Not Performed

If a wrong PIN was entered:
Byte 1 Bit 3 = 1 Offline PIN Verification Performed
Byte 1 Bit 2 = 1 Offline Encrypted PIN Verification Performed
Byte 4 Bit 5 = 1 Offline PIN Verification Failed

## Impact

The attacker also can use lost&stolen cards to conduct fraudulent payments without the PIN knowledge.

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
