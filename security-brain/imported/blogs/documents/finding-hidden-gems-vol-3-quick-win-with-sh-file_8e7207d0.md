---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-01_finding-hidden-gems-vol-3-quick-win-with-sh-file.md
original_filename: 2018-11-01_finding-hidden-gems-vol-3-quick-win-with-sh-file.md
title: 'Finding hidden gems vol. 3: quick win with .sh file'
category: documents
detected_topics:
- oauth
- sso
- command-injection
- otp
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- oauth
- sso
- command-injection
- otp
- automation-abuse
- information-disclosure
language: en
raw_sha256: 8e7207d02f04cfb2e9a1219f165ff09626f56d9f8a3ba6e83947e4bdb29b93f0
text_sha256: a739981967c9fb3e61d2fb6f381298315d16f032ad13f8df79dc8b01f532385b
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Finding hidden gems vol. 3: quick win with .sh file

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-01_finding-hidden-gems-vol-3-quick-win-with-sh-file.md
- Source Type: markdown
- Detected Topics: oauth, sso, command-injection, otp, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `8e7207d02f04cfb2e9a1219f165ff09626f56d9f8a3ba6e83947e4bdb29b93f0`
- Text SHA256: `a739981967c9fb3e61d2fb6f381298315d16f032ad13f8df79dc8b01f532385b`


## Content

---
title: "Finding hidden gems vol. 3: quick win with .sh file"
url: "https://medium.com/@mateusz.olejarka/finding-hidden-gems-vol-3-quick-win-with-sh-file-722e58636ded"
authors: ["Mateusz Olejarka (@molejarka)"]
bugs: ["Information disclosure"]
publication_date: "2018-11-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5613
scraped_via: "browseros"
---

# Finding hidden gems vol. 3: quick win with .sh file

Finding hidden gems vol. 3: quick win with .sh file
Mateusz Olejarka
Follow
2 min read
·
Nov 1, 2018

116

I
observed that some application deployment’s automation is done by the use of shell scripts, mostly files with .sh extensions.

Based on the popular filenames found on GitHub (search for site:github.com ext:sh) I routinely check for such files during bug bounty hunting in my spare time.

Once it ended up quite unexpected.

I
found a file, let’s say it was install.sh on one site which was WordPress based blog.

[--CUT--]
echo "Setting up blog"
echo "- Admin URL: ${local_url}/wp-admin"
echo "- Wp User: c[--EDITED--]"
echo "- Wp Pass: [--EDITED--]
[--CUT--]

What? WordPress admin credentials in plaintext?!

When I saw this, I said to myself “No way it works. Forget it”.

Get Mateusz Olejarka’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

S
till I opened the /wp-admin and entered login and password just to see the login error. I looked for a few seconds on the spinner waiting for this error to show up. To my surprise I was logged in instead. I immediately checked if I was an admin.

Press enter or click to view image in full size

Yes I was. So, I filled the report. Few hours later I got the message below.

Thank you for this report, and given the severity, I have gone ahead and paid a full P1 bounty. We are working on resolving this now and should have it done soon.

Thank you for your participation in the program and we look forward to future reports!

Nice of them.

Lessons learned
For myself - build a list of common sh files
Bug hunters - search for common sh files during recon
Developers - make sure you do not have any shell scripts in web root, if you do definitely do not store admin password in those files

If you enjoyed this story go see two previous parts:

Finding hidden gems vol. 1: forging OAuth tokens using discovered client id and client secret
Finding hidden gems vol. 2: REAMDE.md, the story of a bit too helpful readme file
