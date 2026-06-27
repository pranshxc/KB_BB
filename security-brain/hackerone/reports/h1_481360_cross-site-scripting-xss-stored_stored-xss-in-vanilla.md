---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '481360'
original_report_id: '481360'
title: Stored XSS in vanilla
weakness: Cross-site Scripting (XSS) - Stored
team_handle: vanilla
created_at: '2019-01-17T12:15:45.574Z'
disclosed_at: '2019-05-24T02:24:46.256Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 89
asset_identifier: https://github.com/vanilla/vanilla/
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in vanilla

## Metadata

- HackerOne Report ID: 481360
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: vanilla
- Disclosed At: 2019-05-24T02:24:46.256Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
There is a stored XSS in the latest version 2.6.4 of vanilla.  Attack with post privileges can trigger this.

**Description:**
This is a feature that user can post content in  markdown format. And the content and format type is inserted into database without check the format param. So attack can modify the format type. When the milicious content render by Gdn_format::to($content, $format), it will bypass the XSS filter.

File library/core/class.format.php
```php
    public static function to($mixed, $formatMethod) {
        // Process $Mixed based on its type.
        if (is_string($mixed)) {
            if (in_array(strtolower($formatMethod), self::$SanitizedFormats) && method_exists('Gdn_Format', $formatMethod)) {
                $mixed = self::$formatMethod($mixed);
            } elseif (function_exists('format'.$formatMethod)) {
                deprecated('format'.$formatMethod, 'gdn_formatter_'.$formatMethod, '2015-10-26');
                $formatMethod = 'format'.$formatMethod;
......
```
So when we set the format as 'String', it will call function `formatString` in functions.general.php. This function will not filter xss vector.

## Steps to reproduce:

1. Log in and Click New Discussion
2.  set content as `x<img src=x onerror=alert(document.cookie)>x`
3. Post Discussion and  Intercept request with Burpsuite
4. Modify the param `Format` as `String`
5. the the XSS vector will be triggered


## Anything else we should know?
Every input field support format may be vulnerable

## Impact

Stored XSS

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
