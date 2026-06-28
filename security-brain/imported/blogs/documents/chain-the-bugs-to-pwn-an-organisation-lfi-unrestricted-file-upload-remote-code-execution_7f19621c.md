---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-18_chain-the-bugs-to-pwn-an-organisation-lfi-unrestricted-file-upload-remote-code-e.md
original_filename: 2018-09-18_chain-the-bugs-to-pwn-an-organisation-lfi-unrestricted-file-upload-remote-code-e.md
title: Chain The Bugs to Pwn an Organisation ( LFI + Unrestricted File Upload = Remote
  Code Execution )
category: documents
detected_topics:
- command-injection
- file-upload
- path-traversal
- api-security
tags:
- imported
- documents
- command-injection
- file-upload
- path-traversal
- api-security
language: en
raw_sha256: 7f19621c5885734ad0a53d679f46ca0c482582bc9083f58e0ad8f1dbb48d77bf
text_sha256: 8f940deeda635eda420d017b5a482b91bff5aeae9cdda8523fd1c07b9bf49d70
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Chain The Bugs to Pwn an Organisation ( LFI + Unrestricted File Upload = Remote Code Execution )

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-18_chain-the-bugs-to-pwn-an-organisation-lfi-unrestricted-file-upload-remote-code-e.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, path-traversal, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `7f19621c5885734ad0a53d679f46ca0c482582bc9083f58e0ad8f1dbb48d77bf`
- Text SHA256: `8f940deeda635eda420d017b5a482b91bff5aeae9cdda8523fd1c07b9bf49d70`


## Content

---
title: "Chain The Bugs to Pwn an Organisation ( LFI + Unrestricted File Upload = Remote Code Execution )"
url: "https://medium.com/@armaanpathan/chain-the-bugs-to-pwn-an-organisation-lfi-unrestricted-file-upload-remote-code-execution-93dfa78ecce"
authors: ["Armaan Pathan (@armaancrockroax)"]
bugs: ["LFI", "Unrestricted file upload", "RCE"]
publication_date: "2018-09-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5694
scraped_via: "browseros"
---

# Chain The Bugs to Pwn an Organisation ( LFI + Unrestricted File Upload = Remote Code Execution )

Chain The Bugs to Pwn an Organisation ( LFI + Unrestricted File Upload = Remote Code Execution )
Armaan Pathan
Follow
2 min read
·
Sep 18, 2018

241

3

Hi everyone,
After completing my OSCP certification I thought to give a try to bug bounty, as OSCP has sharpened my exploitationSkills.

I will use lol.com to represent an application as can not disclose the website’s name.

While i was enumerating an application i got a domain which was basically an image server and was managing the images which has uploaded by a user, while enumerating more, i got an endpoint which was allowing me to call the server local files such as passwd , cron jobs and current running services on the server.

Press enter or click to view image in full size

As it was a image server means the server stores all the images which user uploads form his/her profiles.

Get Armaan Pathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I again went back to lol.com and started looking for photo upload functionality that from where i can upload the photo and i got the profile photo option which is allowing me to upload the photos to an application and the photos were storing to the image server.

Now photo upload functionality has ext parameter which is used for file extensions checks but due to improper validations on the parameter, i was able to tamper the values and can upload unrestricted files on the server, i tried to upload php shell but as it was image server so it was not serving the php but by reconig more via lfi i came to know that i can get a shell via perl so i uploaded a perl reverse shell to get a reverse shell on my public IP.

Press enter or click to view image in full size

And with the use of LFI I called the file and i got the reverse shell on my public IP.

Press enter or click to view image in full size

Thanks for reading, Hope you guys liked it.
