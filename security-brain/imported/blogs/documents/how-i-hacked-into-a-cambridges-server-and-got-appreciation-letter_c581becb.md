---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-04_how-i-hacked-into-a-cambridges-server-and-got-appreciation-letter.md
original_filename: 2022-11-04_how-i-hacked-into-a-cambridges-server-and-got-appreciation-letter.md
title: How I hacked into a Cambridge’s server and got appreciation letter.
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
raw_sha256: c581becbab4f2bdf6464551325ad4e0bac71b205355aa390f988d9d2b1b2ae07
text_sha256: 7af083c5f45c7141d75f5f3909db21ce3d0ec84e897d6d20197de32e95d1de82
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked into a Cambridge’s server and got appreciation letter.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-04_how-i-hacked-into-a-cambridges-server-and-got-appreciation-letter.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `c581becbab4f2bdf6464551325ad4e0bac71b205355aa390f988d9d2b1b2ae07`
- Text SHA256: `7af083c5f45c7141d75f5f3909db21ce3d0ec84e897d6d20197de32e95d1de82`


## Content

---
title: "How I hacked into a Cambridge’s server and got appreciation letter."
url: "https://medium.com/@prathamrajgor/how-i-hacked-into-a-cambridges-server-and-got-appreciation-letter-d19a830756b2"
authors: ["Prathamrajgor"]
programs: ["Cambridge"]
bugs: ["Unrestricted file upload", "RCE"]
publication_date: "2022-11-04"
added_date: "2022-11-05"
source: "pentester.land/writeups.json"
original_index: 1951
scraped_via: "browseros"
---

# How I hacked into a Cambridge’s server and got appreciation letter.

How I hacked into a Cambridge’s server and got appreciation letter.
Prathamrajgor
Follow
2 min read
·
Nov 4, 2022

88

Hello Hackers, Hope you are doing fine. So today, I will explain how I found a RCE on Cambridge’s Server.

What was the issue and how did I find it?

So few days ago, I was searching for some information on Cambridge’s website when I stumbled upon a subdomain. Let’s assume the subdomain was subdomain.cam.ac.uk. Digging more into the subdomain, I found an interesting path. Lets assume it to be subdomain.cam.ac.uk/dir1/dir2/upload.

When I opened wappalyzer, I saw that I was running a PHP server and It had a file upload feature where we could an Image. The page looked something like this:

Press enter or click to view image in full size

I thought this might be vulnerable to php file-upload vuln. I immediately fired up my burp started testing. First, I tried uploading a simple PHP file which echos “Hello World”, And it got successfully It got uploaded on their server. Lets assume its location to be subdomain.cam.ac.uk/dir/dir/upload/images/shell.php.573645783462.png.

Get Prathamrajgor’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I visited the location, It told “ file does not exist”. However, When I removed the .png from the location, Boom! I saw Hello World on the screen. Which means that my php file got successfully executed on the server. Now, I tried uploading php shell on the server and It got successfully uploaded again. I tried running some commands like ‘whoami’ and ‘ls’ and I was able to run them successfully.

Press enter or click to view image in full size

I immediately made a report and sent them. After a day, I got a reply along with an appreciation letter.

Thank you for reading!
