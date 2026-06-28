---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-25_dos-on-facebook-android-app-using-65530-characters-of-zero-width-no-break-space.md
original_filename: 2018-10-25_dos-on-facebook-android-app-using-65530-characters-of-zero-width-no-break-space.md
title: DoS on Facebook Android app using 65530 characters of ZERO WIDTH NO-BREAK SPACE.
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
raw_sha256: fe9b1caba10f29eec3a416fddbd7d22e2daf78500b3ebb26852e21b110d76409
text_sha256: 8302889f2c9eafccb833f1edf6081515e5006fd86764b7a82c592ed4848bf10f
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# DoS on Facebook Android app using 65530 characters of ZERO WIDTH NO-BREAK SPACE.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-25_dos-on-facebook-android-app-using-65530-characters-of-zero-width-no-break-space.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `fe9b1caba10f29eec3a416fddbd7d22e2daf78500b3ebb26852e21b110d76409`
- Text SHA256: `8302889f2c9eafccb833f1edf6081515e5006fd86764b7a82c592ed4848bf10f`


## Content

---
title: "DoS on Facebook Android app using 65530 characters of ZERO WIDTH NO-BREAK SPACE."
url: "https://medium.com/@kankrale.rahul/dos-on-facebook-android-app-using-65530-characters-of-zero-width-no-break-space-db41ca8ded89"
authors: ["Rahul Kankrale (@RahulKankrale)"]
programs: ["Meta / Facebook"]
bugs: ["DoS"]
publication_date: "2018-10-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5629
scraped_via: "browseros"
---

# DoS on Facebook Android app using 65530 characters of ZERO WIDTH NO-BREAK SPACE.

Rahul Kankrale
Follow
1 min read
·
Oct 25, 2018

5

DoS on Facebook Android app using 65530 characters of ZERO WIDTH NO-BREAK SPACE.

Step to reproduce:

copy content of https://pastebin.com/0tpucbuv
Open facebook.com in Mozilla, Create a new note, give title and paste the copied content in body of note and publish the note.
Visit created note on facebook’s android app, App will goes in infinity loop and user have to close app.
Proof of concept: https://youtu.be/FepNtq2MKus

Status of Vulnerability: Fixed with comment (fb consider DoS attacks in scope as long as they are persistent. (e.g. would require a user to uninstall an app or break a complete functionality)).

Thanks

Get Rahul Kankrale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Rahulkankrale
