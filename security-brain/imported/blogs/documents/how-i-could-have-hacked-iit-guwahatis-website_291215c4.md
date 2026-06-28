---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-01-09_how-i-could-have-hacked-iit-guwahatis-website.md
original_filename: 2017-01-09_how-i-could-have-hacked-iit-guwahatis-website.md
title: How I could have Hacked IIT Guwahati’s website
category: documents
detected_topics:
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 291215c455ea0fe23c23bbff161822ce2cb799eedce84e414d21459f5ec02a84
text_sha256: 80b4c6ec0926f667da08e7b9a68101b4cb2ffec1aa3f4848f70769a135de471b
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I could have Hacked IIT Guwahati’s website

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-01-09_how-i-could-have-hacked-iit-guwahatis-website.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `291215c455ea0fe23c23bbff161822ce2cb799eedce84e414d21459f5ec02a84`
- Text SHA256: `80b4c6ec0926f667da08e7b9a68101b4cb2ffec1aa3f4848f70769a135de471b`


## Content

---
title: "How I could have Hacked IIT Guwahati’s website"
url: "https://medium.com/bugbountywriteup/how-i-could-have-hacked-iit-guwahatis-website-52dff319b056"
authors: ["Sai Krishna Kothapalli (@kmskrishna)"]
programs: ["IIT Guwahati"]
bugs: ["Unrestricted file upload"]
publication_date: "2017-01-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6235
scraped_via: "browseros"
---

# How I could have Hacked IIT Guwahati’s website

Top highlight

Press enter or click to view image in full size
How I could have Hacked IIT Guwahati’s website.
Sai Krishna Kothapalli
Follow
2 min read
·
Dec 9, 2017

530

3

This story is going to be about how I was able to hack the IIT Guwahati website.

Okay, another click-bait title to get you people to read my blog. Well, the title isn’t completely false either. And as you’ve already opened the story, let me tell you why a bug bounty program is necessary to your university or organisation taking this as an example.

Get Sai Krishna Kothapalli’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So IITG has a complaint booking portal with a feature which allows the user to upload JPG or PNG files. It then checks for the file name extension. Which means if I try to upload a .php file it issues a warning saying only JPG and PNG files are allowed. But unfortunately it also processes the request which I thought was weird. To understand this better, you can watch the video embedded below.

POC video made to report
if(!Image):
  Print Error
Process request

There it is, the vulnerability. Can you see it? The request is being processed irrespective of the error. That means the php file I uploaded was being written to the server. The fix was simple, they just have to make it something like this(add an else case).

if(!Image):
  Print Error
else:
  Process request

As you can see any script kiddie can try and upload a php shell whenever he sees a file upload action. In this case the web admin was actually checking the file type that is being uploaded (like JPG or PNG) but there was a minor mistake in the code which could have resulted in someone taking down the entire website or defacing it.

Since, IIT Guwahati had a Bug Bounty program, I used it to submit this issue and got it fixed before someone else could misuse it.

I also made another video where I could have added my own name to the Hall Of Fame. This write up is a part of my talk which I gave at IIT Guwahati during GCCS regional event on 10 Nov 2017.

Adding my own name to the Hall Of Fame page

Thank you for reading.

Peace :)
