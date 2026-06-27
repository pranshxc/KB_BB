---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '341634'
original_report_id: '341634'
title: Invalid URL parsing '#'
team_handle: ruby
created_at: '2018-04-21T19:23:14.376Z'
disclosed_at: '2018-05-01T14:47:21.018Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
---

# Invalid URL parsing '#'

## Metadata

- HackerOne Report ID: 341634
- Weakness: 
- Program: ruby
- Disclosed At: 2018-05-01T14:47:21.018Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

`URI` is not correctly parsed when "#" is included in the URL.
Therefore, could instead be tricked into connecting to a different host. 

### PoC

```bash
$ ruby --version
ruby 2.4.1p111 (2017-03-22 revision 58053) [x86_64-darwin16]
```

```ruby
require 'uri'
uri = URI("http://www.example.com#@test.evil.com/test")
# => #<URI::HTTP http://www.example.com.evil.com/test>
p uri.hostname
# => "www.example.com.evil.com"
```

But, does not happen if use single quotes,  like this.

```ruby
uri = URI.parse('http://www.example.com#@evil.com/test')
p uri.hostname
# => www.example.com
```

However, in RFC 3986 it is defined that after "#" it is interpreted as a fragment.
Therefore, this behavior is contrary to the user's intuition and easy to overlook.

## Impact

The user may connect to an unintended host.

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
