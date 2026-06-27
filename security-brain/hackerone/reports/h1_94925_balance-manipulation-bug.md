---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '94925'
original_report_id: '94925'
title: Balance Manipulation - BUG
team_handle: coinbase
created_at: '2015-10-20T21:47:22.640Z'
disclosed_at: '2016-02-26T22:15:58.612Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
---

# Balance Manipulation - BUG

## Metadata

- HackerOne Report ID: 94925
- Weakness: 
- Program: coinbase
- Disclosed At: 2016-02-26T22:15:58.612Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello once again,

I have discovered another balance manipulation bug. This time it is much more simpler, but basically has the same outcome. 

EXPLANATION: When you create basic standard Vault and transfer money from your Main Wallet to the vault the balance doesn't "lock up", which means that even when the transfer is pending to the vault you are still freely able to transfer the balance to other btc wallets from your main wallet. Once you approve the transfer to Vault your balance would go into Negative resulting in balance manipulation.

If you have any more questions/concerns feel free to ask.


Thanks,

David.

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
