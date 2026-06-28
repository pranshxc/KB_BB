---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-30_whatsapp-for-android-retains-deleted-contacts-locally.md
original_filename: 2021-12-30_whatsapp-for-android-retains-deleted-contacts-locally.md
title: WhatsApp for Android Retains Deleted Contacts Locally
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: 1bb96da969a680c75d10af471e89bba105a7ec553203949eadc8509ad8fd45a6
text_sha256: 11a44802703de835e1ea1c9fe4120355496d643be6f476ad3c5e6858dbc0098e
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# WhatsApp for Android Retains Deleted Contacts Locally

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-30_whatsapp-for-android-retains-deleted-contacts-locally.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `1bb96da969a680c75d10af471e89bba105a7ec553203949eadc8509ad8fd45a6`
- Text SHA256: `11a44802703de835e1ea1c9fe4120355496d643be6f476ad3c5e6858dbc0098e`


## Content

---
title: "WhatsApp for Android Retains Deleted Contacts Locally"
page_title: "WhatsApp for Android Retains Deleted Contacts Locally | Nightwatch Cybersecurity"
url: "https://wwws.nightwatchcybersecurity.com/2021/12/30/whatsapp-for-android-retains-deleted-contacts-locally/"
final_url: "https://wwws.nightwatchcybersecurity.com/2021/12/30/whatsapp-for-android-retains-deleted-contacts-locally/"
authors: ["Nightwatch Cybersecurity (@nightwatchcyber)"]
programs: ["Meta / Facebook"]
bugs: ["Privacy issue"]
publication_date: "2021-12-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3048
---

# WhatsApp for Android Retains Deleted Contacts Locally

[December 30, 2021](https://wwws.nightwatchcybersecurity.com/2021/12/30/whatsapp-for-android-retains-deleted-contacts-locally/) [nightwatchcyber](https://wwws.nightwatchcybersecurity.com/author/nightwatchcyber/) [Advisories](https://wwws.nightwatchcybersecurity.com/category/advisories/), [Research](https://wwws.nightwatchcybersecurity.com/category/research/)[facebook](https://wwws.nightwatchcybersecurity.com/tag/facebook/), [whatsapp](https://wwws.nightwatchcybersecurity.com/tag/whatsapp/)

## Summary

WhatApp for Android retains contact info locally after contacts get deleted. This would allow an attacker with physical access to the device to check if the WhatsApp user had interactions with specific contacts, even though they have been deleted.

## Vulnerability Details

When a contact is deleted on WhatsApp, their information about security code changes is retained (while the chat content is not). The only way to get rid of that is to select “Clear Chat” for the contact before deleting it. Even deleting the chat itself doesn’t do it unless the “Clear Chat” operation is done first. [The “security code change notifications” option](https://faq.whatsapp.com/general/security-and-privacy/security-code-change-notification/?lang=en) must be enabled in order for this to work.  
  
Someone getting access to the user’s device can figure out whether they ever chatted with specific contacts, even if those contacts and their chats are no longer on the device. This is a privacy issue – especially for people like journalists and those living in dangerous countries.

Since WhatsApp uses Android’s contact app for contact information but supports chats with numbers that aren’t contacts, our theory is that the application retains information about security code changes even for contacts no longer on the device. There seems to be a discrepancy between how the “Clear chat” option and “Delete Chat” options are implemented in the application, with the first option deleting security notification data.

To reproduce:

  1. Delete a chat with a contact that had security code changes before.
  2. Delete the contact from the device via the Android Contacts app.
  3. Re-add contact to the device via the Android Contacts app.
  4. Start a new chat in WhatsApp with that contact but do not send any messages.
  5. Observe that security code changes are listed with dates in the chat.
  6. Select “Clear Chat” to remove the security code changes, and repeat sterps 1-4. Observe that the security code changes no longer appear.

![](https://wwws.nightwatchcybersecurity.com/wp-content/uploads/2021/12/screen-shot-2021-12-30-at-4.13.16-pm.png?w=612)

Tested on WhatsApp for Android, app version 2.21.20.20, running on Android 12.

## Vendor Response

We haven’t retested on a more recent version but our recommendation to users is to use the “Clear Chat” option in order to prevent this. 

The vendor will not be fixing this issue, here is their response:

> _As part of the attack scenario you describe getting access to a person’s WhatsApp account to obtain private data, as you mention yourself, people do have a way to remove these messages from their account, if a bad actor gets access to their WhatsApp account prior to that person deleting that information then they will be able to view this information. As such, we are closing this report._

## References

CWE: [CWE-212 – Improper Removal of Sensitive Information Before Storage or Transfer](https://cwe.mitre.org/data/definitions/212.html)

Facebook # 10102482597361835

## Timeline

2021-10-24: Initial report sent to the vendor, report ID assigned  
2021-10-27: Vendor asks for more info, additional info and screenshots sent  
2021-11-03: Vendor sent interim status report, still investigating  
2021-11-09: Vendor rejects the vulnerability and closes the report  
2021-12-30: Public disclosure  

### Share this:

  * [ Share on X (Opens in new window) X ](https://wwws.nightwatchcybersecurity.com/2021/12/30/whatsapp-for-android-retains-deleted-contacts-locally/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://wwws.nightwatchcybersecurity.com/2021/12/30/whatsapp-for-android-retains-deleted-contacts-locally/?share=facebook)
  * 

Like Loading...
