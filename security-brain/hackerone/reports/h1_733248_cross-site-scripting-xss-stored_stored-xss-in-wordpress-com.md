---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '733248'
original_report_id: '733248'
title: Stored XSS in wordpress.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2019-11-09T22:04:23.291Z'
disclosed_at: '2020-02-17T11:34:36.958Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 349
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in wordpress.com

## Metadata

- HackerOne Report ID: 733248
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2020-02-17T11:34:36.958Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Stored XSS as a comment or as a post (body or title)  at 
`https://wordpress.com/read/feeds/{blog_id}/posts/{post_id}`
`https://yoursubdomain.wordpress.com`
using the payload:
 ```
<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=&gt;&lt;/iframe&gt;
```
## Steps To Reproduce:
- As a comment 
  1. Log in to wordpress.com
  2. Choose a post from the feeds
  3. Add a comment with the payload:
         `<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=&gt;&lt;/iframe&gt;`
 4. By clicking on `Click Here`, an alert will fire with cookies of the domain `wordpress.com`
- As a post
  1. Log in to wordpress.com
  2. Create a new post or site.
  3. Add the payload `<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=&gt;&lt;/iframe&gt;`  to the body or the title of the blog post
  4. preview or publish your new blog post
  5. By clicking on `Click Here`, an alert will fire with cookies of the domain `yoursubdomain.wordpress.com` or `wordpress.com` if the post is previewed from the WordPress feed.  
 6. If you add comments to your blog post and using the payload mentioned above as a comment an Stored XSS alert will fire when you click on the link.

## Impact

- Perform arbitrary requests on the behalf of other users with security context of  wordpress.com or blogsubdomain.wordpress.com
- Read any data the attacked user has access to.

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
