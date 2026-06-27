---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '965267'
original_report_id: '965267'
title: Potential HTTP Request Smuggling in ruby webrick
weakness: HTTP Request Smuggling
team_handle: ruby
created_at: '2020-08-23T13:25:24.033Z'
disclosed_at: '2020-10-29T07:08:50.517Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 52
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- http-request-smuggling
---

# Potential HTTP Request Smuggling in ruby webrick

## Metadata

- HackerOne Report ID: 965267
- Weakness: HTTP Request Smuggling
- Program: ruby
- Disclosed At: 2020-10-29T07:08:50.517Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

function read_body in file /lib/webrick/httprequest.rb use  expression ```/chunked/io``` to decide ```transfer-encoding``` whether or not.
that is not rigorous. When using webrick as a http server, a attacker may use  a ```Transfer-Encoding: AAAchunkedBBB``` header to fake a legal header. than can make a HTTP Request Smuggling attack.
```
def read_body(socket, block)
      return unless socket
      if tc = self['transfer-encoding']
        case tc
        when /chunked/io then read_chunked(socket, block)
        else raise HTTPStatus::NotImplemented, "Transfer-Encoding: #{tc}."
        end
      elsif self['content-length'] || @remaining_size
        @remaining_size ||= self['content-length'].to_i
        while @remaining_size > 0
          sz = [@buffer_size, @remaining_size].min
          break unless buf = read_data(socket, sz)
          @remaining_size -= buf.bytesize
          block.call(buf)
        end
        if @remaining_size > 0 && @socket.eof?
          raise HTTPStatus::BadRequest, "invalid body size."
        end
      elsif BODY_CONTAINABLE_METHODS.member?(@request_method)
        raise HTTPStatus::LengthRequired
      end
      return @body
    end
```

## Impact

It is possible to smuggle the request and disrupt the user experience.

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
