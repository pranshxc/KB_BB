---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2271054'
original_report_id: '2271054'
title: DoS in bigdecimal's sqrt function due to miscalculation of loop iterations
weakness: Uncontrolled Resource Consumption
team_handle: ruby
created_at: '2023-12-04T03:30:16.777Z'
disclosed_at: '2023-12-20T00:02:47.805Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 13
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# DoS in bigdecimal's sqrt function due to miscalculation of loop iterations

## Metadata

- HackerOne Report ID: 2271054
- Weakness: Uncontrolled Resource Consumption
- Program: ruby
- Disclosed At: 2023-12-20T00:02:47.805Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

# Vulnerability
__Affected Product__: `bigdecimal` extension in https://github.com/ruby/ruby
__Affected Versions__: At least version 3.2.2, I didn't test any previous versions

The current implementation of `BigDecimal#sqrt` in `ext/bigdecimal/bigdecimal.c` erroneously checks its parameter
and allows users of the function to control how long it will run. This may lead to
a DoS if the parameter to the function can be controlled by an attacker.

The implementation of `BigDecimal#sqrt` involves a loop that iteratively calculates
the value of the square root:
```c
do {
    y->MaxPrec *= 2;
    if (y->MaxPrec > y_prec) y->MaxPrec = y_prec;
    f->MaxPrec = y->MaxPrec;
    VpDivd(f, r, x, y);        /* f = x/y    */
    VpAddSub(r, f, y, -1);     /* r = f - y  */
    VpMult(f, VpConstPt5, r);  /* f = 0.5*r  */
    if (VpIsZero(f))
        goto converge;
    VpAddSub(r, f, y, 1);      /* r = y + f  */
    VpAsgn(y, r, 1);           /* y = r      */
} while (++nr < n);
```
The number of iterations is determined by the number `n`, which is derived from the
parameter of the `sqrt` function.
The application tries to impose a limit on the number of iterations, as can be seen
in line 4659:
```c
#define maxnr 100UL    /* Maximum iterations for calculating sqrt. */
```
However, the calculation of `n` is erroneous and uses `maxnr` as a _lower_ bound and not
an upper bound for `n` as can be seen in line 7220:
```c
if (n < (SIGNED_VALUE)maxnr) n = (SIGNED_VALUE)maxnr;
```
This may cause the program to have more iterations than originally intended.

# Proof of Concept
The following ruby program iterates 10000 times instead of 100 and takes longer than 10 min to complete on my machine:
```rb
require 'bigdecimal'
BigDecimal("6E19").sqrt(10000)
```
Furthermore, it can be observed the ruby interpreter stalls completely. The program has to be killed with SIGKILL.

# Solution
The following patch resolves the error:
```diff
diff --git a/ext/bigdecimal/bigdecimal.c b/ext/bigdecimal/bigdecimal.c
index 07c2bcf0b5..31e5574574 100644
--- a/ext/bigdecimal/bigdecimal.c
+++ b/ext/bigdecimal/bigdecimal.c
@@ -7217,7 +7217,7 @@ VpSqrt(Real *y, Real *x)
     y->MaxPrec = Min((size_t)n , y_prec);
     f->MaxPrec = y->MaxPrec + 1;
     n = (SIGNED_VALUE)(y_prec * BASE_FIG);
-    if (n < (SIGNED_VALUE)maxnr) n = (SIGNED_VALUE)maxnr;
+    if (n > (SIGNED_VALUE)maxnr) n = (SIGNED_VALUE)maxnr;

     /*
      * Perform: y_{n+1} = (y_n - x/y_n) / 2
```
This change maintains the correctness of the implementation. 
I have checked this against the test suite from https://github.com/ruby/bigdecimal and all the tests still pass.

## Impact

If an attacker can control the parameter to `BigDecimal#sqrt` he/she can cause a ruby program to hang
for a long time.
Furtermore, since the loop is inside of a function of an extension it blocks the interpreter / execution engine
as a whole hindering the delivery of events or signals.
As seen above, a ruby program that is caught up in such a loop can only be interrupted by a SIGKILL signal.
Since the bug is
1. Easy to trigger if the necessary conditions are met
2. Has a huge effect for relatively small input values

I chose the severity medium.

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
