---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '202362'
original_report_id: '202362'
title: Null pointer dereference in mrb_random_initialize
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2017-01-31T14:26:03.652Z'
disclosed_at: '2017-02-07T07:57:31.445Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Null pointer dereference in mrb_random_initialize

## Metadata

- HackerOne Report ID: 202362
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-02-07T07:57:31.445Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Sorry I was not quite sure about the scope. This bug is not triggerable in the sandbox, because it does not use the Random class, but it is triggerable in mruby with the following piece of code:

```ruby
$r = Random.new
a = Object.new
def a.to_int
    $r.rand
end

$r.initialize a
```
The data pointer of $r is set to NULL before parsing arguments in `mrb_random_init`. The srand() call will try to dereference it to get the mt_state and this results in a crash. 

The problem lies in `mrbgems/mruby-random/src/random.c` and is similar to  #182274:
```c
128   t = (mt_state*)DATA_PTR(self);
129   if (t) {
130      mrb_free(mrb, t);
131   }
132   mrb_data_init(self, NULL, &mt_state_type);
133   
134   t = (mt_state *)mrb_malloc(mrb, sizeof(mt_state));
135   t->mti = N + 1;
136   
137   seed = get_opt(mrb);        /* Move this up before line 127 */
```

Please let me know if you are explicitly just looking for bugs affecting the sandbox, so I won't submit invalid reports. Thanks!

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
