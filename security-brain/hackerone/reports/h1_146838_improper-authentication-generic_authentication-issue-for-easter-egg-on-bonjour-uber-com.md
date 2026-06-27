---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146838'
original_report_id: '146838'
title: Authentication Issue for easter egg on bonjour.uber.com
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2016-06-23T16:49:38.774Z'
disclosed_at: '2016-07-07T23:03:05.302Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# Authentication Issue for easter egg on bonjour.uber.com

## Metadata

- HackerOne Report ID: 146838
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-07-07T23:03:05.302Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

This probably (ok, almost definitely) is just informative but thought I would throw it out here anyways. :)

[bonjour.uber.com](bonjour.uber.com) hosts an easter egg (view source and scroll down) where the passcode is insecurely stored as a javascript variable. The source for the easter egg is: 

``` html
<script type="text/javascript">//error easter egg - call stack is intentionally complex
var pressed = [];
var passcode = 'abcde';
document.addEventListener('keypress', keyPressed);
function keyPressed(e) {
  pressed.push(String.fromCharCode(e.charCode));
  if (pressed.join('') == passcode) {
    throw new Error('sentry test');
    pressed = [];
  }
  if (passcode.indexOf(pressed.join(''))) {
    pressed = [];
  }
}
</script>
```

The problem is that the passcode is stored as a string which means I can analyze the code in order to figure out that I must type in abcde to get the sentry test error. Instead of including it that way, I would like to suggest the following code change to increase security: 

``` javascript
var pressed = [];
var hashedPasscode = '03de6c570bfe24bfc328ccd7ca46b76eadaf4334';
document.addEventListener('keypress', keyPressed);
function keyPressed(e) {
  pressed.push(String.fromCharCode(e.charCode));
  if (sha1(pressed.join('') )== hashedPasscode) {
    throw new Error('sentry test');
    pressed = [];
  }
}
```

You could even switch to scrypt or some other more secure hashing algorithm for added security! :P

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
