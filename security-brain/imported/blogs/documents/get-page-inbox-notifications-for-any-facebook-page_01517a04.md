---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-20_get-page-inbox-notifications-for-any-facebook-page.md
original_filename: 2019-07-20_get-page-inbox-notifications-for-any-facebook-page.md
title: Get Page Inbox notifications for any Facebook page
category: documents
detected_topics:
- access-control
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- access-control
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 01517a048ac4d5f4bcd1861ea8e857b71c0d11477b126c32cde6b942fec92308
text_sha256: ec0b6682ead690759c98c58a70ff749b0686908a784d7e4e803d02f7e415b4a1
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Get Page Inbox notifications for any Facebook page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-20_get-page-inbox-notifications-for-any-facebook-page.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `01517a048ac4d5f4bcd1861ea8e857b71c0d11477b126c32cde6b942fec92308`
- Text SHA256: `ec0b6682ead690759c98c58a70ff749b0686908a784d7e4e803d02f7e415b4a1`


## Content

---
title: "Get Page Inbox notifications for any Facebook page"
page_title: "Get Page Inbox notifications for any Facebook page - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/get-page-inbox-notifications-for-any-facebook-page/"
final_url: "https://philippeharewood.com/get-page-inbox-notifications-for-any-facebook-page/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Information disclosure"]
publication_date: "2019-07-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5134
---

Posted on [July 20, 2019](https://philippeharewood.com/get-page-inbox-notifications-for-any-facebook-page/)

# Get Page Inbox notifications for any Facebook page

Facebook sends out an MQTT subscription for page administrators so that they can be notified of any new incoming messages. As a user with no role, it is possible to subscribe to this endpoint.

1\. Head to any page inbox (B) under a user.

https://facebook.com/pagetoken-ID/inbox

2\. Open developer tools network tab and filter the web socket (WS) option. Refresh the page if need be so an item appears named “[edge-chat.facebook.com/chat?region=frc](http://edge-chat.facebook.com/chat?region=frc)“. Clear the binary messages under the “Messages” module.

3\. Open a console drawer and enter the following

`require('PagesManagerPageCommItemEditSubscription').subscribe({page_id:'PAGE_ID'})`

Where PAGE_ID is the ID for the target page (A).

4\. As a user not connected to the page, send the Instagram connected page, a direct message.

5\. Under the WebSocket messages, a new binary message with details from the subscription should appear immediately after sending the message

The binary message does not contain anything sensitive however based on the timing, this is an indicator the page received a message or at the very least, a communication item was changed.

**Timeline**

Jul 20, 2019 – Report sent  
Jul 22, 2019 – Confirmation of submission by Facebook  
Aug 14, 2019 – Confirmation of patch by Facebook  
Aug 28, 2019 – Bounty awarded by Facebook
