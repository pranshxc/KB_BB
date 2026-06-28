---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-02_indias-aadhar-card-source-code-disclosure-via-exposed-svnwcdb.md
original_filename: 2023-01-02_indias-aadhar-card-source-code-disclosure-via-exposed-svnwcdb.md
title: India’s Aadhar card source code disclosure via exposed .svn/wc.db
category: documents
detected_topics:
- sqli
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- sqli
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 34730e3a3a8ececd2b23746db272b37a8a5d36c4b794a91b058b677f1fa102fe
text_sha256: b248c1549b27b727e93f13903c3dbaa2eb9a39793ef49e080d79fe7f8d20895d
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: true
---

# India’s Aadhar card source code disclosure via exposed .svn/wc.db

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-02_indias-aadhar-card-source-code-disclosure-via-exposed-svnwcdb.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: True
- Raw SHA256: `34730e3a3a8ececd2b23746db272b37a8a5d36c4b794a91b058b677f1fa102fe`
- Text SHA256: `b248c1549b27b727e93f13903c3dbaa2eb9a39793ef49e080d79fe7f8d20895d`


## Content

---
title: "India’s Aadhar card source code disclosure via exposed .svn/wc.db"
url: "https://0xlittlespidy.medium.com/indias-aadhar-card-source-code-disclosure-via-exposed-svn-wc-db-c05519ea7761"
authors: ["0xLittleSpidy (@0xLittleSpidy)"]
programs: ["Aadhaar"]
bugs: ["Source code disclosure", ".svn folder disclosure"]
publication_date: "2023-01-02"
added_date: "2023-01-06"
source: "pentester.land/writeups.json"
original_index: 1713
scraped_via: "browseros"
---

# India’s Aadhar card source code disclosure via exposed .svn/wc.db

India’s Aadhar card source code disclosure via exposed .svn/wc.db
0xLittleSpidy
Follow
3 min read
·
Jan 2, 2023

120

2

Press enter or click to view image in full size

Hi Guys, I recently found a .svn/wc.db folder exposed on a resident.uidai.gov.in, and used it to reconstruct the Web app’s source code. I cannot find any article about svn, So this will be very useful for those who find svn on a website.

what is .svn/wc.db?

The .svn/wc.db file is a database file used by Subversion, a version control system and it contains information about the state of the working copy, including the revision numbers of the files, the dates and times when they were last updated, and any local modifications that have been made. It is used by Subversion to track changes to the files in the working copy and to manage the process of merging changes from the repository into the working copy.

what is the Difference between .svn/wc.db and .git ?

.svn/wc.db is a database file used by Subversion, a centralized VCS

.git, on the other hand, is a database file used by Git, a distributed VCS

Note: I haven’t used any directory or file brute-forcing. I used a chrome extension called DotGit which automatically finds .git and .svn in a website while surfing.

Let's Look at How I downloaded all the source codes of an Aadhar website

I just appended .svn/wc.db to https://resident.uidai.gov.in and downloaded the database file

wget https://resident.uidai.gov.in/.svn/wc.db

when I opened the database file with SQLite browser. I came occurs a lot of tables.

sqlitebrowser wc.db
Press enter or click to view image in full size

The nodes table contains many columns but 2 important columns are “local_relpath” and “checksum”

local_relpath →It contains the path of a web app

checksum → It contains a checksum value of the path

For Example:

local_relpath = /Bio-Lock-Enable.php

Get 0xLittleSpidy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

checksum = $sha1$***REDACTED-SUSPECT-TOKEN***I know that SVN keeps a backup copy of all files in a one location

.svn/pristine/<XX>/<CHECKSUM>.svn-base
CHECKSUM is Sha1 sum of the file (remove $sha1$)
XX is the first two characters of CHECKSUM.
https://resident.uidai.gov.in/.svn/pristine/c7/c7fb9f76455732203cb734de0c6016366d729428.svn-base

It is easy to download a single file with wget command. but I have more than 500 paths.so I wrote a simple script to download all the source code.

link to the below code ↓

https://gist.github.com/0xLittleSpidy/***REDACTED-SUSPECT-TOKEN***script to download all the source code
Press enter or click to view image in full size
Downloaded source code

Finally, I got the complete source code of the Aadhar website.

The Indian government has fixed the issue and I encourage ethical hacking practices.

Here are some more good resources:

GitHub - anantshri/svn-extractor: a simple script to extract all web resources by means of.SVN…
Many a times web application pen-testers are encountered with the presence of .svn folders. For those not aware .svn…

github.com

Hacking the .SVN directory (Archive)
This comes from a blog post I wrote on 01/26/2009. I see people are still searching for it and landing at my old site…

www.adamgotterer.com

Special thanks to Dinesh Kumar for guiding me.

Thanks for taking the time to read my write-up.

Want to Connect? Please consider following me on Medium, and Twitter, connecting with me on LinkedIn, or buying me a coffee!
