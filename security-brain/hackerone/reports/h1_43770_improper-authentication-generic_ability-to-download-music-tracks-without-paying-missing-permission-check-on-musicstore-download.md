---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '43770'
original_report_id: '43770'
title: Ability to Download Music Tracks Without Paying (Missing permission check on`/musicstore/download`)
weakness: Improper Authentication - Generic
team_handle: vimeo
created_at: '2015-01-14T17:59:02.757Z'
disclosed_at: '2015-03-01T23:09:50.388Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Ability to Download Music Tracks Without Paying (Missing permission check on`/musicstore/download`)

## Metadata

- HackerOne Report ID: 43770
- Weakness: Improper Authentication - Generic
- Program: vimeo
- Disclosed At: 2015-03-01T23:09:50.388Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I'm not sure how serious this is to be honest. If you're downloading tracks without paying, then I'm sure you could find a copy somewhere on the internet anyway. But I guess it's still an issue.

When browsing the Music Store (https://vimeo.com/musicstore), some tracks are free. To download these, a `GET` request is sent to `/musicstore/download`, with a query string of `track_id=[track_id]&license_id=4`.

For non-free tracks, the link is replaced with an Add to Cart icon, and you're expected to go through the checkout procedure. This is done by a `POST` request to `/cart/music`with a body of `action=add&license_id=2&license_name=Personal&price=1.99&track_id=110947&track_title=Remind%2BMe&uid=110947_2&&&token=[token]`.

Copying the `track_id` from the Add to Cart request and transplanting it into the `/musicstore/download` successfully redirects you to Amazon S3 to download the track, despite you not having paid for it.

Note: I submitted the `GET` request to `/musicstore/download`, but didn't follow the 302 redirect to S3 to download the track since I didn't pay for it. Because of this I can't 100% verify that the resulting file is the track, but judging by the URL it looks like it is.

### Proof-of-Concept
**Accounts Needed**
* User #1 - Standard Vimeo user

**Steps**
1. Login, and browse to https://vimeo.com/musicstore
2. Find a **non-free** track, and click the Add to Cart icon
3. Inside the `POST` request to `/cart/music` copy the `track_id`
4. Browse to the following URL, replacing `[track_id]` with the one from step 3. You should be redirected to S3 to download the track (without paying): `https://vimeo.com/musicstore/download?track_id=[track_id]&license_id=4`

If you need anymore info just shout,
Cheers,
Jack

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
