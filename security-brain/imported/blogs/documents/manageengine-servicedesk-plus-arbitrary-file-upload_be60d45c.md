---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-03_manageengine-servicedesk-plus-arbitrary-file-upload.md
original_filename: 2020-03-03_manageengine-servicedesk-plus-arbitrary-file-upload.md
title: 'ManageEngine ServiceDesk Plus: Arbitrary File Upload'
category: documents
detected_topics:
- idor
- command-injection
- file-upload
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- command-injection
- file-upload
- rate-limit
- api-security
language: en
raw_sha256: be60d45ccce2a1428d0a6569afabe2b75bb9ee39a1782e31f0558cff0404edb9
text_sha256: 60000c8011c64d2038fff6eef2b123828b7e04e72ae585001bb2908ae1f5d94e
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# ManageEngine ServiceDesk Plus: Arbitrary File Upload

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-03_manageengine-servicedesk-plus-arbitrary-file-upload.md
- Source Type: markdown
- Detected Topics: idor, command-injection, file-upload, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `be60d45ccce2a1428d0a6569afabe2b75bb9ee39a1782e31f0558cff0404edb9`
- Text SHA256: `60000c8011c64d2038fff6eef2b123828b7e04e72ae585001bb2908ae1f5d94e`


## Content

---
title: "ManageEngine ServiceDesk Plus: Arbitrary File Upload"
url: "https://medium.com/@ducanhbui/manageengine-servicedesk-plus-arbitrary-file-upload-4bab0bd00425"
authors: ["Duc Anh Bui"]
bugs: ["Arbitrary file upload", "RCE"]
publication_date: "2020-03-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4738
scraped_via: "browseros"
---

# ManageEngine ServiceDesk Plus: Arbitrary File Upload

ManageEngine ServiceDesk Plus: Arbitrary File Upload
Duc Anh Bui
Follow
3 min read
·
Mar 3, 2020

38

Introduction

This article is a write up on how I found my second critical vulnerability at the company’s internal bounty program.

I wrote this for educational purposes only. Do not perform any illegal activity or pen-testing without permission.

Vulnerability exploitation

After a bunch of enumerations and information gathering on subdomains. I found an interesting subdomain that uses ManageEngine ServiceDesk Plus, which have lots of potential security risk.
A few minutes in, I discovered a way to get RCE on this subdomain. This method required an authenticated user to send a POST request to a vulnerable endpoint. (CVE-2019–8394).

2020 solving 2020 problems

In file common/FileAttachment.jsp line 332 only check file upload extension when parameter ‘module’ equal to ‘SSP’ or ‘DashBoard’ or ‘HomePage’, and if parameter ‘module’ is set to ‘CustomLogin’ will skip check file upload extension function and upload arbitrary file to folder ‘/custom/login’ and this file can access directly from url ‘host:port/custom/login/filename’ . An authenticated user with minimum permission (ex: guest) can upload webshell to server.

So the first thing is to acquire an account (don’t care about the privileges). Rolled the dices and found the simplest account credentials of all time. This made me remembered about my first bug bounty case for V* with admin:admin credentials, easy money easy life.

Press enter or click to view image in full size
admin:admin

Got the account, let’s dive into the process of gaining RCE

The first step is to authenticate to access the application with guest credentials, then the server will send a response with cookie parameters.

Press enter or click to view image in full size

After that, take the cookie parameters and webshell content and put them in sections showed in the image below (I got the webshell from this repo)

Press enter or click to view image in full size

Notes: Edit your webshell content to have no newlines (spaces are ok), I struggled for half an hour to get my shell run properly.

Get Duc Anh Bui’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The server send me an 200 OK response. Go check the path

/custom/login/{your_shell_name}.jsp

Thank god the shell popped up. I can execute arbitrary code on the web server from now on!

Press enter or click to view image in full size
First time RCE on Window
Press enter or click to view image in full size
Corona Quarantine List?
Conclusion
Always keep your application up-to-date to mitigate security issues.
Keep trying, there’s still a light at the end of the tunnel xD
References
Offensive Security's Exploit Database Archive
Exploit Title: Zoho ManageEngine ServiceDesk Plus (SDP) before 10.0 build 10012 - arbitrary file upload # Date…

www.exploit-db.com

CVE - CVE-2019-8394
Common Vulnerabilities and Exposures (CVE®) is a list of entries - each containing an identification number, a…

cve.mitre.org

https://github.com/SecurityRiskAdvisors/cmd.jsp
