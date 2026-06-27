---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '459084'
original_report_id: '459084'
title: The taint flag is not propagated at JSON.parse
team_handle: ruby
created_at: '2018-12-08T15:22:20.393Z'
disclosed_at: '2024-01-05T02:48:28.241Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 40
tags:
- hackerone
---

# The taint flag is not propagated at JSON.parse

## Metadata

- HackerOne Report ID: 459084
- Weakness: 
- Program: ruby
- Disclosed At: 2024-01-05T02:48:28.241Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I confirmed that the taint flag is not propagated in `JSON.parse`,`JSON.parse!`, `JSON.load`.

```ruby
$ irb
irb(main):001:0> require 'json'
=> true

# dump
irb(main):002:0> hash = {"key".taint => "value".taint}.taint
=> {"key"=>"value"}
irb(main):003:0> json_str = JSON.dump(hash)
=> "{\"key\":\"value\"}"
irb(main):004:0> json_str.tainted?
=> false
irb(main):005:0>

# prepare tainted string
irb(main):006:0> json_str.taint
=> "{\"key\":\"value\"}"
irb(main):007:0> json_str.tainted?
=> true
irb(main):008:0>

# parse
irb(main):009:0> json_parse = JSON.parse(json_str)
=> {"key"=>"value"}

# not propagated 
irb(main):010:0> json_parse.tainted?
=> false
irb(main):011:0> json_parse.keys[0].tainted?
=> false
irb(main):012:0> json_parse["key"].tainted?
=> false
irb(main):013:0> json_parse.to_s.tainted?
=> false
irb(main):014:0>

irb(main):015:0> json_parse_2 = JSON.parse!(json_str)
=> {"key"=>"value"}
irb(main):016:0> json_parse_2.tainted?
=> false
irb(main):017:0> json_parse_2.keys[0].tainted?
=> false
irb(main):018:0> json_parse_2["key"].tainted?
=> false
irb(main):019:0> json_parse_2.to_s.tainted?
=> false
irb(main):020:0>

irb(main):021:0> json_parse_3 = JSON.parse!(json_str)
=> {"key"=>"value"}
irb(main):022:0> json_parse_3.tainted?
=> false
irb(main):023:0> json_parse_3.keys[0].tainted?
=> false
irb(main):024:0> json_parse_3["key"].tainted?
=> false
irb(main):025:0> json_parse_3.to_s.tainted?
=> false
```

It propagates in `load` of Yaml and Marshal.

```ruby
# -- yaml

irb(main):026:0> require 'yaml'
=> true

# dump
irb(main):027:0> hash = {"key".taint => "value".taint}.taint
=> {"key"=>"value"}
irb(main):028:0> yaml_str = YAML.dump(hash)
=> "---\nkey: value\n"
irb(main):029:0> yaml_str.tainted?
=> false # ?
irb(main):030:0>

# prepare tainted string
irb(main):031:0> yaml_str.taint
=> "---\nkey: value\n"
irb(main):032:0> yaml_str.tainted?
=> true
irb(main):033:0>

# load
irb(main):034:0> yaml_load = YAML.load(yaml_str)
=> {"key"=>"value"}

irb(main):035:0> yaml_load.tainted?
=> false # ?
irb(main):036:0> yaml_load.keys[0].tainted?
=> true
irb(main):037:0> yaml_load["key"].tainted?
=> true
irb(main):038:0> yaml_load.to_s.tainted?
=> true
irb(main):039:0>


# -- marshal

# dump
irb(main):040:0> marshal_str = Marshal.dump(hash)
=> "\x04\b{\x06I\"\bkey\x06:\x06ETI\"\nvalue\x06;\x00T"
irb(main):041:0> marshal_str.tainted?
=> true
irb(main):042:0>

# prepare tainted string
irb(main):043:0> marshal_str.taint
=> "\x04\b{\x06I\"\bkey\x06:\x06ETI\"\nvalue\x06;\x00T"
irb(main):044:0> marshal_str.tainted?
=> true
irb(main):045:0>

# load
irb(main):046:0> marshal_load = Marshal.load(marshal_str)
=> {"key"=>"value"}
irb(main):047:0> marshal_load.tainted?
=> true
irb(main):048:0> marshal_load.keys[0].tainted?
=> true
irb(main):049:0> marshal_load["key"].tainted?
=> true
irb(main):050:0> marshal_load.to_s.tainted?
=> true
```

## Impact

It is possible that an incorrect decision may be made if the user is using the taint flag.
I can not judge whether to propagate also about `dump`.

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
