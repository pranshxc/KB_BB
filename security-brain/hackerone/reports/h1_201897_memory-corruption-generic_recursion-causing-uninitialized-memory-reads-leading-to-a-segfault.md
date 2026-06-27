---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '201897'
original_report_id: '201897'
title: Recursion causing uninitialized memory reads leading to a segfault
weakness: Memory Corruption - Generic
team_handle: shopify-scripts
created_at: '2017-01-29T10:18:43.076Z'
disclosed_at: '2017-02-28T13:30:02.780Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- memory-corruption-generic
---

# Recursion causing uninitialized memory reads leading to a segfault

## Metadata

- HackerOne Report ID: 201897
- Weakness: Memory Corruption - Generic
- Program: shopify-scripts
- Disclosed At: 2017-02-28T13:30:02.780Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The following code produces a segfault without causing a stack overflow, affecting the sandbox:

    def fn(n)
        return
        ensure
            if n == 0
        else fn(n-1)
        end
    end
    fn(24)

When the `n` parameter is less than 24, there is no segfault. However,
investigating with a memory sanitizer shows that uninitialized read errors
start to happen when `n >= 15`. The uninitialized read happens at the following
location in vm.c (with the relevant line marked):

```
1701         cipop(mrb);
1702         acc = ci->acc;  [***]
1703         mrb->c->stack = ci->stackent;
```

The issue seems to be in using the `ci` data after the call to `cipop`. The following patch stops the read errors and segfaults, and passes make test:

```
diff --git a/src/vm.c b/src/vm.c
index 9684dab..66fb692 100644
--- a/src/vm.c
+++ b/src/vm.c
@@ -1698,9 +1698,10 @@ RETRY_TRY_BLOCK:
           mrb->jmp = prev_jmp;
           return v;
         }
-        cipop(mrb);
+        ci = mrb->c->ci;
         acc = ci->acc;
         mrb->c->stack = ci->stackent;
+        cipop(mrb);
         if (acc == CI_ACC_SKIP) {
           mrb->jmp = prev_jmp;
           return v;
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
