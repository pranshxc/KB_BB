---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '198494'
original_report_id: '198494'
title: Lack of Controls Allowing for Card and PIN Enumeration Leading to Fraud
team_handle: starbucks
created_at: '2017-01-15T02:39:58.133Z'
disclosed_at: '2017-07-01T02:15:32.468Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
---

# Lack of Controls Allowing for Card and PIN Enumeration Leading to Fraud

## Metadata

- HackerOne Report ID: 198494
- Weakness: 
- Program: starbucks
- Disclosed At: 2017-07-01T02:15:32.468Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The pages https://www.starbucks.com/account/card/addcard and https://www.starbucks.com/account/card/Balance do not properly enforce security controls to limit POST requests. This bug allows attackers to successfully hijack a loaded Starbucks card and transfer all the funds into their own account. Cards linked with auto-reload features could exponentially increase fraud. 
*NOTE: You will need to pass primary authentication before testing these pages. I have set up a temporary account for this purpose.*

**Card Enumeration:**
In a POST request to the above https://www.starbucks.com/account/card/addcard URL, if an attacker sets the Register.MyCard attribute to “FALSE” they can enumerate the 16-digit Card Number without limits. 
Another important note is all Starbucks locations have unactivated cards at their registers. It is highly possible for a threat actor to obtain a 16-digit card number from the next card in line, and sit on the account until it has been loaded up. Furthermore, in my research I've discovered each card only increments a singular digit in their 16-digit number. Because of this, a threat actor can easily discern which cards are about to be purchased, as well as which cards have been recently purchased.
{F152532}

**PIN Enumeration:**
In a POST request to the second https://www.starbucks.com/account/card/Balance URL, an attacker can check the PIN of a card they’ve already added via the previous /addcard Card Enumeration method. 
If an attacker already knows the 16-digit card number (via Starbucks stores), with the original POST request to the https://www.starbucks.com/account/card/addcard URL, if an attacker sets the Register.MyCard attribute to “TRUE” they can enumerate the 8-digit PIN number without limits.
Due to this, an attacker is able to successfully test every PIN number against 16-digit card data.
{F152533}
{F152534}

**Fraud/Risk:**
If an attacker is able to successfully validate PIN and Card information, they now have full access to all funds in the account. At this point they are able to commit fraudulent purchases and even migrate funds off the account onto their own card. Cards linked with auto-reload features could exponentially increase fraud damages. 
{F152535}

**Documentation:**
My test card was used in this demonstration. On the attached image, you can see the card number ending in 4769 was successfully processed. In the second image, you can see the PIN correctly enumerating once the PIN ending in 89 was processed.

**Remediation:**
My recommendation is to add velocity checks to both the /addcard and /Balance pages when attempting to add a Starbucks gift card. Additionally, CAPTCHA can be used as another authorization process. 

Please let me know if you need additional information to help triage this bug.
Thanks!

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
