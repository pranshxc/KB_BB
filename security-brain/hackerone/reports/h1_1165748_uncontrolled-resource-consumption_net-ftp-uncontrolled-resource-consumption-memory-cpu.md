---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1165748'
original_report_id: '1165748'
title: '''net/ftp'': Uncontrolled Resource Consumption (Memory/CPU)'
weakness: Uncontrolled Resource Consumption
team_handle: ruby
created_at: '2021-04-15T15:12:23.034Z'
disclosed_at: '2021-04-21T06:16:15.867Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 8
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# 'net/ftp': Uncontrolled Resource Consumption (Memory/CPU)

## Metadata

- HackerOne Report ID: 1165748
- Weakness: Uncontrolled Resource Consumption
- Program: ruby
- Disclosed At: 2021-04-21T06:16:15.867Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Current  `TIME_PARSER` implementation allows attackers to cause a denial of service (memory consumption) via a large integer value for the `fractions` property.

The problem code:
```ruby
    TIME_PARSER = ->(value, local = false) {
      unless /\A(?<year>\d{4})(?<month>\d{2})(?<day>\d{2})
            (?<hour>\d{2})(?<min>\d{2})(?<sec>\d{2})
            (?:\.(?<fractions>\d+))?/x =~ value
        raise FTPProtoError, "invalid time-val: #{value}"
      end
      usec = fractions.to_i * 10 ** (6 - fractions.to_s.size)
      Time.public_send(local ? :local : :utc, year, month, day, hour, min, sec, usec)
    }
```

# PoC

For example, a ran a malicious server that returns `"213 20371231000000.".("9"x999999999)."\r\n"`  for commands that use `TIME_PARSER`  (`mlst`, `mlsd`, `mdtm`, etc).  Also, such a response can be spoofed if the attacker is on the same network as the victim.

Here is the result of running of the process for an hour and a half:
```
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND  
18644 me        20   0   27.9g  12.3g     64 D 100.0  84.0  89:17.45 ruby
```
The process kept the CPU load around 90-100% all the time, and slowly but surely, devour all the available memory.

## Impact

Denial of Service.

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
