---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-02_instagram-photo-was-present-in-data-backup-nearly-after-two-years-being-deleted.md
original_filename: 2022-08-02_instagram-photo-was-present-in-data-backup-nearly-after-two-years-being-deleted.md
title: Instagram photo was present in data backup nearly after two years being deleted.
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: d5481c7a993f36408bca4e23e038effa8ad823b570deff20304b54611ea32a50
text_sha256: 613c24bc4243e67e7ceda45858079092160c6527e70f6bac089fd16ba718a6f4
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Instagram photo was present in data backup nearly after two years being deleted.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-02_instagram-photo-was-present-in-data-backup-nearly-after-two-years-being-deleted.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `d5481c7a993f36408bca4e23e038effa8ad823b570deff20304b54611ea32a50`
- Text SHA256: `613c24bc4243e67e7ceda45858079092160c6527e70f6bac089fd16ba718a6f4`


## Content

---
title: "Instagram photo was present in data backup nearly after two years being deleted."
page_title: "How I Recovered a Deleted Instagram Photo from Data Backup, deleted two years ago and Earned a $550 Bounty | by Jeewan Bhatta | InfoSec Write-ups"
url: "https://medium.com/@the_null_kid/instagram-photo-was-present-in-data-backup-nearly-after-two-years-being-deleted-f0e4d6e108"
authors: ["Jeewan Bhatta (@thenullkid)"]
programs: ["Meta / Facebook"]
bugs: ["Privacy issue"]
bounty: "550"
publication_date: "2022-08-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2373
scraped_via: "browseros"
---

# Instagram photo was present in data backup nearly after two years being deleted.

How I Recovered a Deleted Instagram Photo from Data Backup, deleted two years ago and Earned a $550 Bounty
Jeewan Bhatta
Follow
2 min read
·
Aug 2, 2022

308

Press enter or click to view image in full size

So this write up is about the bug in Instagram data download feature. So this features allows you to download your personal data including messages, photos, followers, comments and many other things for future backup. But what if the deleted content was also present in the data backup? That’s exactly what happened to me.

If a person deletes a message or any kind of photo, it takes upto 90 days to completely delete that item from data backup. I uploaded a photo during the Covid-19 pandemic period. Due to some reasons I instantly deleted that photo. Nearly after two years, I was checking the backup file which I had requested from my account, I saw that the photo which I deleted instantly that time was present there. The same photo was present in three different folders with different id names.

This was against the Facebook policy which says that photo might take up to 90 days to get completely removed. But in my case it was already around 2 years. So I made a detailed report to Facebook Security Team about the issue. The team verified that the photo was deleted and was also present in data backup.

Get Jeewan Bhatta’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After nearly six months of conversation with the security team, they fixed the issue and paid me a bounty of $550.

Also I got my name in the “Hall of Fame 2021” (https://m.facebook.com/whitehat/thanks). You can also connect with me on LinkedIn & Twitter.

Press enter or click to view image in full size

Report Timeline

Reported: May 25, 2021

Reviewed and asked for more information: May 26, 2021

Bounty Awarded: September 15, 2021

Bounty Amount: $500+$50(Delay bonus)
