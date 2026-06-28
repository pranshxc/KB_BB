---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-23_arbitrary-file-corruption-end-to-end-encrypted-messaging-application.md
original_filename: 2022-09-23_arbitrary-file-corruption-end-to-end-encrypted-messaging-application.md
title: 'Arbitrary File Corruption: End - to - End Encrypted Messaging Application'
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
raw_sha256: 5ccdb175d285cbe4b0e29d9b80aa4c60b998c6a6df3edfd094e9f2602fb54e7c
text_sha256: 9174b032cabdb57d1783feff2b1bd270bf050a08631d3c15e07c2086baabccfe
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Arbitrary File Corruption: End - to - End Encrypted Messaging Application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-23_arbitrary-file-corruption-end-to-end-encrypted-messaging-application.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `5ccdb175d285cbe4b0e29d9b80aa4c60b998c6a6df3edfd094e9f2602fb54e7c`
- Text SHA256: `9174b032cabdb57d1783feff2b1bd270bf050a08631d3c15e07c2086baabccfe`


## Content

---
title: "Arbitrary File Corruption: End - to - End Encrypted Messaging Application"
url: "https://nmochea.medium.com/arbitrary-file-corruption-end-to-end-encrypted-messaging-application-674963dceef8"
authors: ["Neil Mark Ochea (@nmochea)"]
bugs: ["Insecure intent", "Android"]
publication_date: "2022-09-23"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2128
scraped_via: "browseros"
---

# Arbitrary File Corruption: End - to - End Encrypted Messaging Application

Arbitrary File Corruption: End - to - End Encrypted Messaging Application
Neil Mark Ochea / mhl_0xnmo
Follow
3 min read
·
Sep 23, 2022

In this write-up, I’ll tell you how I was able to Exfiltrate Database and Sandbox Files on End-to-End Encrypted Messaging Application.

Description

End-to-End Messaging application there are several places where the application use URI returned from a GET_CONTENT, PICK, etc. intent. Due to the lack of URI returned sanitizing an attacker/malicious actor able to the theft of files including database and sandbox files by copying them to public storage or by sending them.

Application Vulnerable Codes
In file redacted/redacted/messenger/discussion/DiscussionActivity.java
Press enter or click to view image in full size
In file redacted/redacted/messenger/App.java
Press enter or click to view image in full size
In file redacted/redacted/messenger/discussion/DiscussionActivity.java
Press enter or click to view image in full size
In file redacted/redacted/messenger/App.java
Press enter or click to view image in full size
In file redacted/redacted/messenger/discussion/DiscussionActivity$$ExternalSyntheticLambda23.java
Press enter or click to view image in full size
Note the codes with // end lines. This is where the vulnerability exists.
Another Vulnerable Codes
In file redacted/redacted/messenger/settings/StorageExplorer.java
Press enter or click to view image in full size
In file redacted/redacted/messenger/App.java
Press enter or click to view image in full size
In file redacted/redacted/messenger/settings/StorageExplorer$$ExternalSyntheticLambda2.java
Press enter or click to view image in full size
Note the codes with // end lines. This is where the vulnerability exists.
Attack Scenario
The app launches an implicit intent startActivityForResult(new Intent("android.intent.action.PICK"), ANY_REQUEST_CODE)
The atracker app performs the action and puts a Uri in the data value setResult(-1, new Intent().setData("file:///data/user/0/redacted.redacted.messenger/databases/app_database"))
The app receives the result in onActivityResult(requestCode, responseCode, resultIntent) from its local file system.
Attacker Application
In file AndroidManifest.xml
Press enter or click to view image in full size
In file EvilActivity.java
Press enter or click to view image in full size
Proof of Concept
Press enter or click to view image in full size
The uploaded database file of the End-to-End Messaging application.
Disclosure Timeline
August 30, 2022 — I reported this vulnerability issue.
September 1, 2022 — The vulnerability is confirmed, and implementing a patch soon.
September 21, 2022 — The vulnerability has been patched and got a bounty.

Thanks for reading this article, I hope you guys learn something new today. Please share this article to spread the knowledge.

Get Neil Mark Ochea / mhl_0xnmo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Don’t forget to follow and connect with me through LinkedIn, and Twitter.
