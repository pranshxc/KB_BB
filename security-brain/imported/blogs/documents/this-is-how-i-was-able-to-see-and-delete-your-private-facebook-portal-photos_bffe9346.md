---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-04_this-is-how-i-was-able-to-see-and-delete-your-private-facebook-portal-photos.md
original_filename: 2021-12-04_this-is-how-i-was-able-to-see-and-delete-your-private-facebook-portal-photos.md
title: This is how i was able to See and Delete your Private Facebook Portal photos
category: documents
detected_topics:
- idor
- command-injection
- otp
- graphql
- mobile-security
tags:
- imported
- documents
- idor
- command-injection
- otp
- graphql
- mobile-security
language: en
raw_sha256: bffe934620e7503be66306c79d0d6a8e45e1a9153b0182619ad5043a8aae42cf
text_sha256: 45b4f7b7fdac99df5c57fda22b32c41d79ddcbcc6dd6778de7a0c718a2a8e8fc
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# This is how i was able to See and Delete your Private Facebook Portal photos

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-04_this-is-how-i-was-able-to-see-and-delete-your-private-facebook-portal-photos.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, graphql, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `bffe934620e7503be66306c79d0d6a8e45e1a9153b0182619ad5043a8aae42cf`
- Text SHA256: `45b4f7b7fdac99df5c57fda22b32c41d79ddcbcc6dd6778de7a0c718a2a8e8fc`


## Content

---
title: "This is how i was able to See and Delete your Private Facebook Portal photos"
url: "https://pathleax.medium.com/this-is-how-i-was-able-to-see-and-delete-your-private-facebook-portal-photos-a93ed22f875b"
authors: ["Abhishek Pathak (@pathleax)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2021-12-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3113
scraped_via: "browseros"
---

# This is how i was able to See and Delete your Private Facebook Portal photos

Top highlight

This is how i was able to See and Delete your Private Facebook Portal photos
ecstasy
Follow
4 min read
·
Dec 4, 2021

390

2

Hello everyone! This is my second Bug Bounty from Facebook (Meta Platforms, Inc)

Press enter or click to view image in full size
About Facebook Portal

Facebook Portal is a multi functional app mainly designed for Portal devices which helps to make calls, create/share albums and photos to connected Portal devices, although it works without a Portal device too.

Description

This bug could have allowed a malicious user to view and delete a targeted photo on Facebook Portal app without having access of victim’s login credentials or album ownership

Impact

Private photos of users could be read and deleted improperly, a malicious user could have been able to permanently remove/delete user’s photos from their secret albums, add photos to malicious album and regenerate a valid CDN url of photos.

Story

One day i was using my android smartphone while enjoying my tea, while scrolling Facebook homepage i saw an ad of “Facebook Portal video calling devices” just after seeing the ad i became very curious to explore it more.

After some research i’ve found that Portal video calling devices has an official app called “Facebook Portal” on Google Play store.

Press enter or click to view image in full size

Without thinking twice i instantly installed it to check how does it works and what’s inside it.

Press enter or click to view image in full size

After seeing this homepage i got to know that it’s a photo sharing app, so decided to check backend stuffs of upload functionality by intercepting the traffic through proxy tools (ie. BurpSuite, Charles, Fiddler)

But unfortunately laptop’s battery was dead so decided to do all the traffic intercepting stuff on my android smartphone through HttpCanary proxy.

Repro Steps

Created two Portal users UserA and UserB, where UserA is Victim and UserB is Malicious User or Attacker.

UserA Steps

Press enter or click to view image in full size
Clicked on upload button, selected an image and clicked on “Add 1 Photo”.
Press enter or click to view image in full size
Clicked on “New Album” to upload that selected image in newly created album.
Press enter or click to view image in full size
Just after uploading the image i got the details of uploaded media in request response like Media ID, CDN Url, etc.
Press enter or click to view image in full size
Copied that Media ID from response to test it further.

UserB Steps

Did everything same as UserA but this time i noticed something new.
Press enter or click to view image in full size
While checking all the requests in HttpCanary, I’ve found this endpoint which creates the Album, but most importantly some of the parameters were empty, Mainly “album_media_ids” was empty.
I was curious to know what will happen if i append/add UserA’s Media ID in this empty array/list.

Vulnerable Endpoint Details (Sensitive Data is REDACTED)

Get ecstasy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Endpoint:

https://graph.facebook.com/graphql

Request Body:

access_token=[REDACTED]&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=BPPhotosHubAlbumGraphQLHelperCreateAlbumMutation&variables={"album_media_ids":["[REDACTED]"],"name":"Portal Uploads","cover_photo_id":null,"scale":2.75,"thumbnail_size":null}&server_timestamps=true&doc_id=[REDACTED]

Press enter or click to view image in full size
I immediately replaced [] with [“135XXXXXXXXXX39”] where 135XXXXXXXXXX39 was UserA’s Media ID and sent the request.
Press enter or click to view image in full size
Well it didn’t gave me any error like “You are not allowed to perform this action” or “You are not allowed to access/upload this media” instead gave a valid response with media CDN url just because it was not verifying the Owner ID of that particular Media in backed, due to this misconfiguration it was vulnerable to an IDOR attack.
Press enter or click to view image in full size
When i opened UserB’s Facebook Portal app, saw that UserA’s Photo has been added in newly created album.
Well now i decided to delete the Photo from UserB’s newly created album to see what will happen in UserA’s account.
Press enter or click to view image in full size
I immediately deleted that photo from UserB’s album and checked UserA’s account.
Press enter or click to view image in full size
Well! Well! Well, The photo was deleted from UserA’s album too.
I stopped the testing process and made the vulnerability report to Facebook WhiteHat program.
Bonus

The “cover_photo_id” json parameter was also vulnerable along with “album_media_ids”

Timeline

16 Sept 2021 — Initial Report

19 Sept 2021 — Asked For An Update

21 Sept 2021 — Triaged

28 Sept 2021 — Fixed

28 Sept 2021 — Confirmation of Fix

13 Oct 2021 — $$$$$ Bounty Awarded by Facebook

Thank you for reading this write-up!

You can follow me on Twitter @hi_ecstasy
