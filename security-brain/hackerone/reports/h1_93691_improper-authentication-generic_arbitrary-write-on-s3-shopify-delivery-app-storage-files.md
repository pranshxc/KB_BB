---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '93691'
original_report_id: '93691'
title: Arbitrary write on s3://shopify-delivery-app-storage/files
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-10-13T19:22:49.202Z'
disclosed_at: '2015-10-15T18:55:26.436Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# Arbitrary write on s3://shopify-delivery-app-storage/files

## Metadata

- HackerOne Report ID: 93691
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-10-15T18:55:26.436Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Short
====
The policy used to upload files via the Delivery app is too generic which results in an arbitrary write (and replace) of files in the files/ directory.

Disclaimer: While I was unable to create a second store to fully test this (I can't create new development stores right now, support is researching this), I strongly believe that this vulnerability works as I expect it to work due to the nature of the policy.

Current Policy
====

    {
    "expiration": "2015-10-14T15:27:47Z",
    "conditions": [
        {
            "bucket": "shopify-delivery-app-storage"
        },
        [
            "starts-with", "$key", "files/"
        ],
        {
            "acl": "private"
        },
        {
            "success_action_status": "200"
        },
        ["content-length-range", 0, 5368709120]
    ]
    }


What's wrong here
====

The only (security relevant) limitations we have here are:
 - Signature + Policy are only valid for one day
 - The key has to start with files/
 - ACL has to be set private

So, one can basically write arbitrary files to the S3 bucket as long as those are within the files/ dir. This doesn't hinder anybody as all the 'good stuff to replace' is under that dir. As the ACL is private, files can just be downloaded when the delivery app signed a download request, so the attacker needs to get a hold on a valid link.  

The vector
====
 - Find a shop with a downloadable good and purchase it OR get a manual direct link
 - Grab the bucket key when the file will be downloaded directly from S3 (via signed url)
 - Go to your own shop, create a product with a downloadable good
 - Note down the parameters used to POST the file when you upload it
 - Issue a new request to the key recorded from the data you don't own with the parameters you just grabbed from your own delivery app
 - Profit

One could do a ton of fun stuff to the files, to my mind come Viruses, Exploits, Illegal Content, etc.

How it should be
====

The policy should be tailored directly to the upload at hand, especially the key. The app does return the specific path already where the file should be placed by the client, I don't see why the policy doesn't reflect that. The policy should be nailed directly to that key to eliminate this vulnerability.

What I did that you should cleanup
====
I did upload 2 files to the bucket which don't belong to anyone, those files are:
 - files/hackerone/simon/brakhane/kitty.jpg
 - files/kitty.jpg

You might want to clean them away as they can't be downloaded anyway and just cost you money.

Cheers,
Simon

PS: I do hope strongly this isn't already known ;)

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
