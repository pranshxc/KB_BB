---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-14_improper-implementation-of-my-status-video-time-limit-in-whatsapp.md
original_filename: 2020-08-14_improper-implementation-of-my-status-video-time-limit-in-whatsapp.md
title: Improper Implementation of My Status video time limit in WhatsApp
category: documents
detected_topics:
- command-injection
- business-logic
- mobile-security
tags:
- imported
- documents
- command-injection
- business-logic
- mobile-security
language: en
raw_sha256: f759b59a2450699e5c0729f2a687ff4007ad85b7fcd637ef9607c7e5b70bc41a
text_sha256: db564d23e81d21e0748d640a30f1f8a23fc89893867383994e688989c03eb4ed
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Improper Implementation of My Status video time limit in WhatsApp

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-14_improper-implementation-of-my-status-video-time-limit-in-whatsapp.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `f759b59a2450699e5c0729f2a687ff4007ad85b7fcd637ef9607c7e5b70bc41a`
- Text SHA256: `db564d23e81d21e0748d640a30f1f8a23fc89893867383994e688989c03eb4ed`


## Content

---
title: "Improper Implementation of My Status video time limit in WhatsApp"
page_title: "Vulnerability- Privacy Violation| Improper Implementation of My Status video time limit in WhatsApp | Medium"
url: "https://medium.com/@vishalranjan00012/hi-folks-2f28dd8fdfe9"
authors: ["Vishal Ranjan"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Privacy issue", "Android"]
publication_date: "2020-08-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4324
scraped_via: "browseros"
---

# Improper Implementation of My Status video time limit in WhatsApp

Vishal Ranjan
Follow
4 min read
·
Aug 14, 2020

12

Hi Folks!

Recently I uncovered a bug in WhatsApp “Improper Implementation of My Status video time limit in WhatsApp”.Unfortunately, Facebook stated that “We have no way to tell on the server side that the video is long due to end-to-end encryption”

As a Cyber security professional, I am posting this bug for User Awareness!

Improper Implementation of My Status video time limit in WhatsApp

It was observed that My Status video time limit feature in WhatsApp was not implemented adequately. This results in application vulnerable to privacy violation issue.

Scenario 1:The end users can view the full length of the video instead of 30 seconds without the knowledge of the victim. It can lead to misuse of video (e.g. malicious user can send the data/video across multiple platforms to multiple users which the victim does not intent to do so.)

Step 1: Login as a “user A” and noted the version of WhatsApp installed in Android device is “2.20.195.17” which is the latest version as on date.

Step 2: Select the respective video from the “chats” and forward it to “My Status”.

Step 3: Observe pop-up message stating “Videos sent to My Status will be trimmed to the first 30 seconds”.

Step 4: Video has been successfully shared at “My Status” and “user A” can view only the first 30 seconds of the video.

Press enter or click to view image in full size

Step 5: Now login as a “user B” with another device and noted the version of WhatsApp installed in Android device is “2.20.195.17” which is the latest version as on date.

Step 6: Click on the status shared by “user A”.

Step 7: From the WhatsApp application UI, “User B” can view only the first 30 seconds of the video as shared by “user A”.

Step 8: On the mobile device of user B, navigate to the Gallery (/storage/emulated/0/WhatsApp/Media/.Statuses) and observe the full length of the video.(user A has shared only the first 30 seconds of the video as shown in the above steps).

Impact (Scenario 1):Hence, the user B can send the data/video across multiple platforms to multiple users which a user A does not intent to do so.

Impact (Scenario 2): A victim (user A) can share his/her “My Status” video of 30 seconds to Facebook or forward/share to other contact knowing that it is only of 30 seconds, but the content which is being received by recipients is of full length.

Get Vishal Ranjan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Step 1: Repeat above scenario 1 steps 1 to 4.

Step 2: Click on forward/share functionality and select the recipients (i.e. user B)

Step 3: User A believes that video which is shared to user B is of 30 seconds(video that is showed under My Status is of 30 seconds), but the content which is being received by user B is of full length.

Step 4: Similarly, a user A can click on “Share to Facebook” functionality and the full length video will be shared to his/her Facebook Story.

Thank You!
