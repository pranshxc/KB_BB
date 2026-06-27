---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '282339'
original_report_id: '282339'
title: Cross-domain linkability when system time changed in Tor Browser
weakness: Privacy Violation
team_handle: torproject
created_at: '2017-10-24T08:59:56.241Z'
disclosed_at: '2017-10-26T11:30:53.199Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- privacy-violation
---

# Cross-domain linkability when system time changed in Tor Browser

## Metadata

- HackerOne Report ID: 282339
- Weakness: Privacy Violation
- Program: torproject
- Disclosed At: 2017-10-26T11:30:53.199Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

This report is inspired by #257942. That report uses `languagechange` event as an indicator for different tabs to link multiple visits to a single user. This report uses another trick to achieve the same thing.

Malicious websites keeps reading `Date.now()` inside a `setInterval` loop with a short interval (the PoC uses 3000 ms). Normally, the values of `Date.now()` between two consecutive iterations should differ by around 3000 ms (i.e. 2900 ms - 3100 ms). However, if the user's system time changes (either by user's manual modification or by some program's auto clock synchronization), the websites can detect this change, because the time difference between two iterations are likely to be larger than 3000 ms. In this case the script can send a log to the malicious server with the current and previous timestamp. Since it is very unlikely that two users change their system clocks at the same time and with the same old/new time pair, it is possible to link the same user on different domains.

PoC:
1. Open https://xiaoyinl.github.io/dds24f/tals.html and https://jsfiddle.net/a4faupwj/ on two different tabs in Tor Browser.
2. Change the computer's system time to more than 4 seconds later or a few seconds earlier.
3. Check the output from the two websites.

I think this issue is probably more severe than #257942, because the time change can happen without user action. There is a paper describing how major operating systems synchronize the system time and that most of the time synchronization protocol is vulnerable to MITM attacks.[1] The frequency of clock synchronization ranges from minutes to hours. The fact that Tor decreases timing precision to 100 ms doesn't really matter. Although I didn't test, I feel that if the user's clock lags more than 0.3 second right before a clock synchronization, using `setInterval(100ms)` should be able to detect that.

To fix this, the only feasible way I can think of is to prohibit non-active tabs from calling `Date.now()`.

[1] https://www.blackhat.com/docs/eu-14/materials/eu-14-Selvi-Bypassing-HTTP-Strict-Transport-Security-wp.pdf

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
