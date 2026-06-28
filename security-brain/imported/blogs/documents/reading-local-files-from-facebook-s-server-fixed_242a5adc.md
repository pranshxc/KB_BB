---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-12-06_reading-local-files-from-facebooks-server-fixed.md
original_filename: 2014-12-06_reading-local-files-from-facebooks-server-fixed.md
title: Reading local files from Facebook's server (fixed)
category: documents
detected_topics:
- sso
- command-injection
- file-upload
- path-traversal
- api-security
tags:
- imported
- documents
- sso
- command-injection
- file-upload
- path-traversal
- api-security
language: en
raw_sha256: 242a5adc3e23dbebcf2d5400fbd5f0bc16290ec71e387c0665ca37341525f097
text_sha256: 9c5769c1369d5f2fdff0821da69840bab3e9d6cd6ef34e0de1b89d94383907af
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: true
---

# Reading local files from Facebook's server (fixed)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-12-06_reading-local-files-from-facebooks-server-fixed.md
- Source Type: markdown
- Detected Topics: sso, command-injection, file-upload, path-traversal, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: True
- Raw SHA256: `242a5adc3e23dbebcf2d5400fbd5f0bc16290ec71e387c0665ca37341525f097`
- Text SHA256: `9c5769c1369d5f2fdff0821da69840bab3e9d6cd6ef34e0de1b89d94383907af`


## Content

---
title: "Reading local files from Facebook's server (fixed)"
page_title: "Josip Franjković - archived security blog: Reading local files from Facebook's server (fixed)"
url: "https://josipfranjkovic.blogspot.com/2014/12/reading-local-files-from-facebooks.html"
final_url: "https://josipfranjkovic.blogspot.com/2014/12/reading-local-files-from-facebooks.html"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Meta / Facebook"]
bugs: ["LFI", "Unrestricted file upload"]
publication_date: "2014-12-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6356
---

Hello,  
  
Recently I found a vulnerability in Facebook which allowed me to read local files from Facebook's servers. The vulnerable part of Facebook was their Careers resume uploader, located at every job offer, for example this [one](https://www.facebook.com/careers/resume?dept=engineering&req=a0IA000000CzAekMAF).  
  
You can upload any extension there, so I decided to upload a .php file :-) - one can always hope. Of course, it was not executed nor could I get file path, but contents of the file were returned, after being base64 encoded. Next thing I tried was to name my file /etc/passwd, "file:///etc/passwd" and couple others. None of these worked.  
  
Couple tries later I uploaded a zipped .php file, and the response contained **unzipped, base64'd contents of .php**. If you read Facebook's ["Bounty hunter's guide"](https://www.facebook.com/notes/facebook-bug-bounty/a-bounty-hunters-guide-to-facebook/946955115318715) you will know where this leads.  
The guide describes how one researcher uploaded zip with symlink to /etc/passwd, and couple steps later Facebook returned few lines of /etc/passwd.  
  
I have done exactly the same, so:  
1\. create a symlink to /etc/passwd (or any other file you want to read)  

> ln -s /etc/passwd link

2\. zip the created link while preserving symlinks:  

> zip --symlinks test.zip link

3\. upload test.zip as your resume, system will unzip it  
**4\. the response to POST will have details of (whole) /etc/passwd or other file.**  
**  
**Here is a screenshot of response containing /etc/passwd=***REDACTED***

  

I have speculated about symlinking a directory, but never tried it. Neal from Facebook thought that this might get me contents of files from the directory, but not necessarily filenames. We shall never know. 

  
Here is a timeline of the bug report:  
Nov 30, 2014 **09:45** \- **vulnerability reported**  
Nov 30, 2014 17:58 - reply from Facebook's security (Neal) saying they cannot reproduce bug  
Nov 30, 2014 18:08 - update from Neal, they can reproduce it  
Nov 30, 2014 **19:10** \- **temporary fix has been pushed, disabling resume uploads**  
Dec 01, 2014 ~23:00 - more permanent fix pushed, now server no longer responds with contents of uploaded resume (Emrakul)  
Dec 05, 2014 18:15 - bounty awarded (Neal).  
Dec 05, 2014 ~19:00 - objection about reward sent to Facebook's team  
Dec 06, 2014 ~23:30 - Neal from Facebook explains this is actually a third party system they run  
  
I'd like to ramble a bit about the award for this bug. When I found it, it looked like a critical bug that could allow me to read parts of Facebook's source. It turned out to actually be a third party software they used to analyse uploaded resumes, therefore I could **not** actually access any part of Facebook's internals. The network this system is hosted on was pretty locked down, too.  
  
Basically, this is a bug that looks really critical, but is much lower severity. It is an exact opposite to a [low severity bug I found some time ago that turned out to be more dangerous.](http://josipfranjkovic.blogspot.com/2013/11/facebook-bug-bounty-secondary-damage.html)  
  
Lessons learned:  
  

  * **Read all write-ups you can get your hands on.** I would never think of uploading the zip with symlinks if I did not read Facebook's blog. Philippe has a good list of Facebook bugs [here.](https://www.facebook.com/notes/phwd/facebook-bug-bounties/707217202701640)

  * Some bugs are not what they look like :-)

Huge thanks to researcher who first used ZIP with symlinks, and to Facebook for blogging about it, and their security team for being awesome as always, fixing the bug in 10 hours on Sunday.
