---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '88105'
original_report_id: '88105'
title: XSS on vimeo.com | "Search within these results" feature (requires user interaction)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: vimeo
created_at: '2015-09-09T04:39:40.338Z'
disclosed_at: '2017-08-31T10:26:41.247Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on vimeo.com | "Search within these results" feature (requires user interaction)

## Metadata

- HackerOne Report ID: 88105
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: vimeo
- Disclosed At: 2017-08-31T10:26:41.247Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

__Description__

When you search in pages such as the videos of some Category or the videos of some User, and you receive more than 0 results, the path of the URL is put in the attribute `data-start-page` of a `<li>` element without escaping. This allows to insert another attribute like `onmouseover` to execute Javascript code.
To exploit this bug, you need to retitle a video to something like `"onmouseover="alert(document.domain)&#x2f;` and put the title as the search query in the URL. The character `/` has to be encoded like `&#x2f;` because if you send the character `/` as `%2F` you will get a 404 response.

__Proof of concept__
1. Upload a new video via https://vimeo.com/upload, or go to the Settings of one that you already uploaded.
2. Enter `"onmouseover="alert(document.domain)&#x2f;` for the _Title_ of the video.
3. Click on _Save Changes_.
4. Using other user, go to https://vimeo.com/[the_user_used_to_upload_the_video]/videos/search:%22onmouseover%3D%22alert%28document.domain%29%26%23x2f%3B/.
5. Move your mouse over the thumbnail of the video that you uploaded (it should be the only video that appears in the results).
6. `alert(document.domain)` is executed.

To see the proof of concept in action, you can go to https://vimeo.com/user36690798/videos/search:%22onmouseover%3D%22alert%28document.domain%29%26%23x2f%3B/.

Happily, I can only reproduce it on Firefox, because XSS Auditor notices that `"onmouseover="alert(document.domain)&#x2f;` appears in the document and in the URL. I will try a little more to reproduce it on Chrome too, but I see it very difficult.

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
