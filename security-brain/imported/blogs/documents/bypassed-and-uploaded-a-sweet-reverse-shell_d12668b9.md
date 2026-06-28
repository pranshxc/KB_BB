---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-05_bypassed-and-uploaded-a-sweet-reverse-shell.md
original_filename: 2021-09-05_bypassed-and-uploaded-a-sweet-reverse-shell.md
title: Bypassed! and uploaded a sweet reverse shell
category: documents
detected_topics:
- command-injection
- file-upload
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- file-upload
- api-security
- mobile-security
language: en
raw_sha256: d12668b9596b745c3e7158ba4c62b1b00629d71b3df336958f890f6811603d81
text_sha256: 4a26b9056de16db5453d857c7ea3f71c043d1c7ec1e9668bbf5c0d039eed52d9
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassed! and uploaded a sweet reverse shell

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-05_bypassed-and-uploaded-a-sweet-reverse-shell.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `d12668b9596b745c3e7158ba4c62b1b00629d71b3df336958f890f6811603d81`
- Text SHA256: `4a26b9056de16db5453d857c7ea3f71c043d1c7ec1e9668bbf5c0d039eed52d9`


## Content

---
title: "Bypassed! and uploaded a sweet reverse shell"
url: "https://infosecwriteups.com/bypassed-and-uploaded-a-sweet-reverse-shell-d15e1bbf5836"
authors: ["Ajay Sharma (@security_donut)"]
bugs: ["Unrestricted file upload"]
publication_date: "2021-09-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3346
scraped_via: "browseros"
---

# Bypassed! and uploaded a sweet reverse shell

Top highlight

Bypassed! and uploaded a sweet reverse shell
Hey, Today I will showcase how I found a file upload vulnerability which I bypassed and popped a reverse shell .
Ajay Sharma
Follow
2 min read
·
Sep 5, 2021

564

5

Press enter or click to view image in full size

Initially being a private program, lets call it target.com. They had a functionality to upload a profile pic which only accepts jpg, png, jpeg images.

Starting with I tried uploading a php-reverse shell file which you can get from pentestmonkey

Tricks I tried to upload a reverse-shell but miserably failed :

Just uploading .php file instead of jpg file.
Trying double extensions to bypass and upload php file pic.jpg.php or pic.php.jpg
Changing Content-type filtering i.e., changing Content-Type: txt/php to image/jpg
Tried Case sensitives — pic.PhP also tried pic.php5, pHP5.
Tried special characters to bypass pic.php%00 , pic.php%0a, pic.php%00

All the above scenarios didn’t worked at all, obvious they are the basic security remediations companies keep it.

Get Ajay Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now lets try something new, Have you heard of magic numbers ?

Basically every file extension has its own magic number, and I took a php-reverse-shell.php file and using hex editor I added the magic number of jpeg i.e., FF D8 FF E0 at start of the php file using the hex tool.

Press enter or click to view image in full size

I just uploaded the file and it worked!

Then just by clicking on view profile got me an access to the reverse shell.

Reason behind this worked is because,

“ the image filters are looking at the ‘Magic Number’ at the beginning of a file to determine if it is a valid image and that is where we just bypassed. ”

Reported, Rewarded — $*****

Hope you like this sweet and short story of file upload vulnerability I have found.

If you have questions and anything about the post you want to ask me, please contact me via Twitter(security_donut) My DMs are always open.

See you soon with next article!
