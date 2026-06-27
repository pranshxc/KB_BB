---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '106315'
original_report_id: '106315'
title: Potential for Double Spend via Sign Message Utility
weakness: Cryptographic Issues - Generic
team_handle: coinbase
created_at: '2015-12-21T14:43:00.047Z'
disclosed_at: '2016-01-06T16:29:44.923Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- cryptographic-issues-generic
---

# Potential for Double Spend via Sign Message Utility

## Metadata

- HackerOne Report ID: 106315
- Weakness: Cryptographic Issues - Generic
- Program: coinbase
- Disclosed At: 2016-01-06T16:29:44.923Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi, 

There is an unlikely (but theoretically exploitable vulnerability) is caused by allowing users to sign messages with their addresses. So far I have not been able to exploit this, but I believe that it is exploitable. 

On coinbse.com, the user can see a list of their addresses [here](https://www.coinbase.com/addresses). When they click on an address, they get the option to "Sign a message". 

An attacker could create a raw transaction (explanation of how to do so is [here](http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html)) spending from one of the addresses listed there to an attacker controlled address. The attacker would then sign the raw transaction so that it is ready to be sent out to the entire network. Then the attacker would send some amount of bitcoin to Coinbase (a predetermined amount to a predetermined address). Shortly after sending the bitcoin to Coinbase, the attacker would then relay his signed transaction to send the bitcoin to his own privately held address. 

The end outcome of this is that Coinbase believes they have received some amount of Bitcoin (and it had a number of confirmations in an address controlled by Coinbase), but in reality they lost it since the attacker stole it before Coinbase could transfer it elsewhere. 

Realistically, I'm not sure whether this can be practically exploited. None the less, I would recommend adding some sort of parsing code to the "Sign a message" utility so that it will refuse to sign a transaction. 

Thanks,
David Dworken

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
