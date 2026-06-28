---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-19_facebook-bug-bounty-reading-whatsapp-contacts-list-without-unlocking-the-device.md
original_filename: 2019-08-19_facebook-bug-bounty-reading-whatsapp-contacts-list-without-unlocking-the-device.md
title: 'Facebook Bug Bounty: Reading WhatsApp contacts list without unlocking the
  device'
category: documents
detected_topics:
- access-control
- command-injection
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- mobile-security
language: en
raw_sha256: 3f196af28ba7ba23663d663fb7dcbafc62f83d7fc66034594efd93345e7f2859
text_sha256: 00494a2f1e150eea99041fe690ace347d2e547f8e150b870b1f59331483675a1
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Bug Bounty: Reading WhatsApp contacts list without unlocking the device

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-19_facebook-bug-bounty-reading-whatsapp-contacts-list-without-unlocking-the-device.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `3f196af28ba7ba23663d663fb7dcbafc62f83d7fc66034594efd93345e7f2859`
- Text SHA256: `00494a2f1e150eea99041fe690ace347d2e547f8e150b870b1f59331483675a1`


## Content

---
title: "Facebook Bug Bounty: Reading WhatsApp contacts list without unlocking the device"
page_title: "WhatsApp Bug Bounty: Reading contact list without unlocking the device | InfoSec Write-ups"
url: "https://medium.com/@ar_arvind/facebook-bug-bounty-reading-whatsapp-contacts-list-without-unlocking-the-device-a40e9c660a42"
authors: ["Arvind (@ar_arv1nd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-08-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5074
scraped_via: "browseros"
---

# Facebook Bug Bounty: Reading WhatsApp contacts list without unlocking the device

WhatsApp Bug Bounty: Reading contacts list without unlocking the device
Arvind
Follow
2 min read
·
Aug 20, 2019

183

Press enter or click to view image in full size

Note: This is being published with the permission of Facebook under the responsible disclosure policy. The vulnerability is now fixed.

Press enter or click to view image in full size

A bug allows anyone who has the victim’s phone to read all the contacts stored in the device without unlocking the security lock.

In WhatsApp voice/video call, “Add participant” option is available to add more participants to the call (Group call).

I started one-on-one voice/video call and tapped “Add participant” button in the top right corner, now it displays all the contacts without prompting security lock when the device is locked.

Get Arvind’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This vulnerability is exploitable only in some stock android based devices.

Tested devices
Google Pixel (Android 8.1)
Moto g4 plus (Android 7.0)
Timeline

June 13, 2019: Report submitted.

July 10, 2019: Report Triaged.

August 16, 2019: Issue patched and bounty awarded.

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
