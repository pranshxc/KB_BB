---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-26_misconfiguration-whatsapp-messenger.md
original_filename: 2019-01-26_misconfiguration-whatsapp-messenger.md
title: Misconfiguration-Whatsapp Messenger
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: b5a231f4551829fc3dabf737c734061431e02dd54358b7e890c2abfcfa6d2428
text_sha256: 5df06243ac099c9dcf190596562a9002261a630765424fa66b2fe800682340d2
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Misconfiguration-Whatsapp Messenger

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-26_misconfiguration-whatsapp-messenger.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `b5a231f4551829fc3dabf737c734061431e02dd54358b7e890c2abfcfa6d2428`
- Text SHA256: `5df06243ac099c9dcf190596562a9002261a630765424fa66b2fe800682340d2`


## Content

---
title: "Misconfiguration-Whatsapp Messenger"
url: "https://medium.com/@pratheesh.p.narayanan/misconfiguration-whatsapp-messenger-1f0f1cf3ef00"
authors: ["Pratheesh P Narayanan"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2019-01-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5449
scraped_via: "browseros"
---

# Misconfiguration-Whatsapp Messenger

Misconfiguration-Whatsapp Messenger's
Pratheesh P Narayanan
Follow
2 min read
·
Jan 26, 2019

61

1

This report is all about the Misconfiguration which I came across on the Cross Platform Instant Messaging App- WhatsApp

You might be aware of recent policy changes on Whatsapp which prevents users from forwarding messages to more than 5 chats at a time.Also,whenever a user forwards something,the application shows that this is a forwarded message.

Forwarded Message

Whatsapp Introduced this feature to prevent fake messages from being circulated on the platform. They had even launched a program which awards researchers upto 50K USD for providing them with better ideas to prevent spam/fake messages from being circulated.

WhatsApp Research
WhatsApp Messenger: More than 1 billion people in over 180 countries use WhatsApp to stay in touch with friends and…

www.whatsapp.com

About the bug…

Get Pratheesh P Narayanan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The bug is pretty much simple and straight forward. The forward limit of upto 5 chats and the forwarded tag was not implemented on The Business Version of the Application as well as on Whatsapp Messenger for Windows Phone. Any malicious user using any of the above versions of the application can exploit this vulnerability. No preventive measures are taken.

No Limit On Forward
Press enter or click to view image in full size
No Forward Tag

I was responsible enough to report this to the Facebook Security Team. I felt that since they were investing a lot into resolving this issue of Spam/fake message on their platform,I felt this might qualify as a report,but it was not a security risk according to Sec Team.

They’re not gonna fix it any time soon

Initial Report: January 8

More Information: January 10

Report Closed as Informative on 25th January

Let’s hope someone from the product team will come across this and will roll out a fix ;)
