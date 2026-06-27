---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '407319'
original_report_id: '407319'
title: ActiveStorage service's signed URLs can be hijacked via AppCache+Cookie stuffing
  trick when using GCS or DiskService
weakness: Information Disclosure
team_handle: rails
created_at: '2018-09-07T20:39:10.582Z'
disclosed_at: '2018-12-27T21:27:02.574Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# ActiveStorage service's signed URLs can be hijacked via AppCache+Cookie stuffing trick when using GCS or DiskService

## Metadata

- HackerOne Report ID: 407319
- Weakness: Information Disclosure
- Program: rails
- Disclosed At: 2018-12-27T21:27:02.574Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

`ActiveStorage` tries to force `content-disposition: attachment` for [a list of content-types](https://github.com/rails/rails/blob/2a470d73a75ebf8cd7975e469bd82586d9234442/activestorage/lib/active_storage/engine.rb#L33-L42), including `text/html`. However, `response-content-type` and `response-content-disposition` in GCS and DiskService's URLs aren't signed, which means an attacker can modify them at will. This is not the case for Azure or S3.

This can be exploited using `AppCache` and cookie bombing as follows:
1. Upload the following file as `ActiveStorage::Blob`
File: fallback.html
```
<html>
<script>
  alert('Your request to the page '+location.href+' is hijacked!');
</script>
</html>
```
Grab the service signed URL for it and modify content type and content disposition params to `text/html` and `inline`. 

2. Now upload this other file using that URL as fallback:
File: manifest.appcache
```
CACHE MANIFEST 
FALLBACK:
/bucket_name/ [fallback_url from previous step]
```
In the same way, grab the signed service URL and modify content disposition and type to ensure it's served inline and as `text/cache-manifest`. 

3. Finally, upload this file using the service URL for manifest.appcache:
File: main.html
```
<html manifest="[manifest_url from the manifest above]">
Any requests to this bucket will be hijacked.
<script>
setTimeout(function(){
for(var i = 1e3; i>0; i--){document.cookie = i + '=' + Array(4e3).join('0') + '; path=/'};
}, 3000);
</script>
</html>
```
Grab the service URL for `main.html`, modify content type and disposition to ensure it's served as `inline` and `text/html`, and trick a user of the Rails app with access to `ActiveStorage` attachments into clicking it.

Since it'll be open inline and as HTML, the JS code to overflow the cookies for the service (storage.googleapis.com in the case of GCS) will be executed. Next time the user makes a request for a file under the same bucket as `main.html`, googleapis.com will return an error due to the size of the cookie headers. This will be interpreted as being offline by the browser, which will offer the fallback specified in the manifest.  The `fallback.html` above will be opened inline and as HTML as well, and its JS code executed. That code can be made to send `location.href` (the signed URL)  to the attacker.

## Impact

Gain access to signed URLs for private objects, which in practice means access to those objects, as signed URLs is all that is needed.

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
