---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '535827'
original_report_id: '535827'
title: Buffer overflow in yywarning_s
weakness: Classic Buffer Overflow
team_handle: shopify-scripts
created_at: '2019-04-11T14:44:25.684Z'
disclosed_at: '2019-09-04T13:35:50.392Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
tags:
- hackerone
- classic-buffer-overflow
---

# Buffer overflow in yywarning_s

## Metadata

- HackerOne Report ID: 535827
- Weakness: Classic Buffer Overflow
- Program: shopify-scripts
- Disclosed At: 2019-09-04T13:35:50.392Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

PoC
===
The following demonstrates a crash:

```
300000000000000000000000000000000000000000000000E0030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

Debug info
==========
In the same vein as our last two reports, we've found more instances of problematic string concatenation. This crash happens due to a buffer overflow in `yywarning_s`. `strcat` is called without making sure `buf` is large enough. The patch below adds the check.

```diff
diff --git a/mrbgems/mruby-compiler/core/parse.y b/mrbgems/mruby-compiler/core/parse.y
index cb62ec3f..82df8c08 100644
--- a/mrbgems/mruby-compiler/core/parse.y
+++ b/mrbgems/mruby-compiler/core/parse.y
@@ -3759,10 +3759,15 @@ static void
 yywarning_s(parser_state *p, const char *msg, const char *s)
 {
   char buf[256];
-
-  strcpy(buf, msg);
-  strcat(buf, ": ");
-  strcat(buf, s);
+  const char delim[] = ": ";
+
+  if (strlen(msg) + strlen(s) + strlen(delim) + 1 > sizeof(buf)) {
+      strcpy(buf, msg);
+  } else {
+      strcpy(buf, msg);
+      strcat(buf, delim);
+      strcat(buf, s);
+  }
   yywarning(p, buf);
 }

```

Test platform
=============
* Arch Linux

mruby SHA: 9c252410cf6e43eb7e19683844c83581445fc089

Thank you,
Dinko Galetic
Denis Kasak

## Impact

DOS through crashing the mruby process and probable execution flow control through stack smashing.

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
