---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-05_directory-traversal-in-pdf-viewing-application-leading-to-full-database-takeover.md
original_filename: 2022-11-05_directory-traversal-in-pdf-viewing-application-leading-to-full-database-takeover.md
title: Directory traversal in PDF viewing application. Leading to full database takeover
category: documents
detected_topics:
- idor
- path-traversal
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- idor
- path-traversal
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: e41b1fc694d474c92928096763bfb0f21ef0e4d2983ea3847bed2b60f69d2023
text_sha256: a904c679074da3daaf5e51d170940871a25407137cca288c0eedaac36347fe5d
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Directory traversal in PDF viewing application. Leading to full database takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-05_directory-traversal-in-pdf-viewing-application-leading-to-full-database-takeover.md
- Source Type: markdown
- Detected Topics: idor, path-traversal, command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `e41b1fc694d474c92928096763bfb0f21ef0e4d2983ea3847bed2b60f69d2023`
- Text SHA256: `a904c679074da3daaf5e51d170940871a25407137cca288c0eedaac36347fe5d`


## Content

---
title: "Directory traversal in PDF viewing application. Leading to full database takeover"
url: "https://medium.com/@wrinnsec/directory-traversal-in-pdf-viewing-application-leading-to-full-database-takeover-376e68eadd86"
authors: ["Tom Wrinn"]
bugs: ["Path traversal"]
publication_date: "2022-11-05"
added_date: "2022-11-08"
source: "pentester.land/writeups.json"
original_index: 1947
scraped_via: "browseros"
---

# Directory traversal in PDF viewing application. Leading to full database takeover

Directory traversal in PDF viewing application. Leading to full database takeover
Tom Wrinn
Follow
3 min read
·
Nov 6, 2022

131

4

Hello everyone, this is my first write-up on here and i hope you enjoy.

Press enter or click to view image in full size
Introduction

I was looking at a new target, it was a English tutoring website with 50,000 active members. I started off with subdomain enumeration using subfind3r, not many subdomains were found, and the ones that i found were not very interesting. I decided to do some URL recon with waybackurls. The results seemed really intriguing, i noticed a lot of PHP web apps with interesting parameters that i might be able to find a IDOR vulnerability on. I found one php web app in particular that seemed very interesting:

https://redacted.org/program/pdf/pdf_install.php?filename=sample.pdf

*Website name redacted as per their request.

I started to think, what if i changed the parameter entry to something other than a pdf file? So i input “index.php” in place of “sample.pdf”

https://redacted.org/program/pdf/pdf_install.php?filename=index.php

To my surprise, the download started, but my downloaded file was a suspiciously small size of just 251 bytes. Opening the file read:

Warning:  readfile(./index.php) [function.readfile]: failed to open stream: No such file or directory in /home/hosting_users/languageweb/www/program/pdf/pdf_install.php on line 10

I recognize this, this is a error within the php application, and its caused because it couldn’t find a “index.php” file in that folder. Well, if that’s the only error, it should mean that as long as i back out of that directory and find a folder that does contain their “index.php” file, I should be able to download it. to test my theory, i went backwards 2 directories by using the backward directory command(“../”):

redacted.org/program/pdf/pdf_install.php?filename=../../index.php

The response was a download of a file that was 57.5 kb. It was a success!

Escalating Directory/Path Traversal

So great, now i can download any file i want from their server. Using my completed scan from waybackurls gave me tons of good directories to look through. I was able to find a /mysql/ folder that provided me with tons of .php config files, and i was able to get both SMTP and MYSQL credentials! This could have resulted in a full database takeover and hijacking of their companies emailing!

<?
$DBCONF[host] = "localhost";
$DBCONF[dbname] = "languageweb";
$DBCONF[user] = "REDACTED";
$DBCONF[passwd] = "REDACTED";
?>

*mysql credential file

Get Tom Wrinn’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After finding all these files, i was satisfied with my report and sent it to their IT team.

Timeline
9–28–22 Reported the bug in an email to their main contact email
10–16–22 After 2 weeks of no response emailed secondary contact email
10–23–22 IT team reached out and said they were investigating
10–25–22 IT team reaches out and says they have deployed a fix
11–1–22 I confirm fix works, ask to publish this report
11–3–22 IT team approves but requests not to include companies name
11–3–22 I send a draft of this Article and ask if it complies.
11–4–22 IT Team approves article.
11–5–22 Article is published.

Thanks for reading!
