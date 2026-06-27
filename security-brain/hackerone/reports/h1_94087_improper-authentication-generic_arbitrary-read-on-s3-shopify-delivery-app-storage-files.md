---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '94087'
original_report_id: '94087'
title: Arbitrary read on s3://shopify-delivery-app-storage/files
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-10-15T20:38:59.534Z'
disclosed_at: '2015-10-20T20:27:10.858Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Arbitrary read on s3://shopify-delivery-app-storage/files

## Metadata

- HackerOne Report ID: 94087
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-10-20T20:27:10.858Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Short
====
An attacker is able to read arbitrary files from the delivery app storage if the bucket key is known to him.

Vector
====
1) The victim uploads a.png to a product his shop located at https://myhackeronestore.myshopify.com.
1a) The file is stored at s3://shopify-delivery-app-storage/files/myhackeronestore.myshopify.com/5682196162/a.png
2) The attacker uploads b.png to a product in his shop (location irrelevant) and changes the 'attachment[filepath]' parameter from "b.png" to "b.png/../../../../files/myhackeronestore.myshopify.com/5682196162/a.png" in the initial call to /attachments.
3) The attacker will now go ahead an generate a manual download link for his newly created attachment
3a) When he visits the generated manual download link the site will state "b.png/../../../../files/myhackeronestore.myshopify.com/5682196162/a.png" as the file name
3b) When the attacker proceeds to press the download button he'll get a working link to get a.png from the victim.

What's wrong here
====
The attacker is able to craft the bucket key in a way to use path traversals (and possibly other wired things related to AWS S3 key names) to get files he shouldn't have access to. 

How it should be
====
In an ideal world the delivery app should control 100% of the bucket key name to make sure no harm can be done by attacks like this. This could be achieved by having a mapping from uploaded_filename to actual_key_in_s3 (is there a way to tell S3 how the downloaded file should be named?). 

Conclusion
====
In my book this is fraud and shouldn't be there ;) You might consider the approach to control 100% of the bucket key to rule an entire class of bugs/vulnerabilities here out as filtering of the filename is tricky and will probably fail (now or in the near feature, who knows what S3 offers as a neat new 'feature' in the future).  Also there are just too many variants on how things could get wrong, what comes to mind is: Encoding interpretation failures on the app side, hidden/not well documented features on the AWS side,...

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
