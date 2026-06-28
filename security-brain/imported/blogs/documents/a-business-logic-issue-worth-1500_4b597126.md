---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-21_a-business-logic-issue-worth-1500.md
original_filename: 2022-05-21_a-business-logic-issue-worth-1500.md
title: A business Logic issue worth $1500
category: documents
detected_topics:
- business-logic
- mobile-security
- command-injection
tags:
- imported
- documents
- business-logic
- mobile-security
- command-injection
language: en
raw_sha256: 4b59712615f63efd8f6d738af31c7e1a1f3631086537d11afa46275395799a4d
text_sha256: 21293c6304a47479760413ff2d5881aab0f8d70aa0be8581094a966d564c4b29
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# A business Logic issue worth $1500

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-21_a-business-logic-issue-worth-1500.md
- Source Type: markdown
- Detected Topics: business-logic, mobile-security, command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `4b59712615f63efd8f6d738af31c7e1a1f3631086537d11afa46275395799a4d`
- Text SHA256: `21293c6304a47479760413ff2d5881aab0f8d70aa0be8581094a966d564c4b29`


## Content

---
title: "A business Logic issue worth $1500"
url: "https://mokhansec.medium.com/a-business-logic-issue-worth-1500-a0f1a0b76570"
authors: ["Mohsin Khan (@tabaahi_)"]
bugs: ["Logic flaw"]
bounty: "1,500"
publication_date: "2022-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2620
scraped_via: "browseros"
---

# A business Logic issue worth $1500

A business Logic issue worth $1500
Mohsin khan
Follow
2 min read
·
May 21, 2022

531

4

Hello everyone,

Its me Mohsin khan AKA tabaahi_.Today I would like to talk about one of my recent findings.

It was a private bug crowd program. The issue is resolved now. But I don’t have permission from the program so will call it redirect.com.

The program has a website, android, IOS app, and desktop app in the scope. Started with a Web application, and I found the block device option.

After reading docs (related to block devices) I understand User can log in to his/her account in android, IOS apps, and desktop apps. And devices will show on the device option.

Get Mohsin khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If I click on the blocked device the account of the user will log out from the device, and the User will not be able to login to the application (on the blocked device) until I unblock the device.

So I installed android, IOS app, and desktop app. And login to the application. I notice IOS app and desktop app working fine. But when I blocked the android application login, The user is still logged in. Security implementation for the android app is not working properly.

I reported to them

Press enter or click to view image in full size

There are so many programs that allow block device features. Go and try now :)

Thank you for reading! And don’t forget to follow me on Twitter.

Tabaahi_
