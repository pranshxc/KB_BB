---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-24_from-file-upload-to-emailpass.md
original_filename: 2019-05-24_from-file-upload-to-emailpass.md
title: From file upload to email:pass
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
raw_sha256: cfb0cf1e115ca72cf38e7ee131167f2e78632e61509598e969b126a1733e3941
text_sha256: fe4c127afece6dc7e388912f9dc8d260c339c56a3750bccafbb5dc59823f91c1
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# From file upload to email:pass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-24_from-file-upload-to-emailpass.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `cfb0cf1e115ca72cf38e7ee131167f2e78632e61509598e969b126a1733e3941`
- Text SHA256: `fe4c127afece6dc7e388912f9dc8d260c339c56a3750bccafbb5dc59823f91c1`


## Content

---
title: "From file upload to email:pass"
url: "https://medium.com/@frostnull/from-file-upload-to-email-pass-dc7141aa1ff6"
authors: ["fr0stNuLL"]
bugs: ["Unrestricted file upload"]
publication_date: "2019-05-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5245
scraped_via: "browseros"
---

# From file upload to email:pass

From file upload to email:pass
fr0stNuLL
Follow
3 min read
·
May 24, 2019

242

1

Hi everybody, today I want to show you a cool experience that I had, doing a Pentest in a private program. First of all, I overshadowed all the sensitive information of the company. Let’s go...

Get fr0stNuLL’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First, there was a form that a non-authenticated user could send information about errors or suggestions of the application and in this form it was also possible to upload files like the image bellow:

Press enter or click to view image in full size

Through the request response headers I knew it was a Microsoft server, so I uploaded a reverse shell in .asp (more info how to create web shells here) and put the .png at the end of the .asp file, as illustrated below:

Press enter or click to view image in full size

however, the application did not let me upload, so I put the Content-type header as png, deleted the .png that I had placed before and it worked, as illustrated below:

Press enter or click to view image in full size

Through the application response I was able to get the location where my reverse shell was placed, so I copied the path, put the password and we got a reverse shell, as follows:

Press enter or click to view image in full size
Press enter or click to view image in full size

The next step was to check which were the users with administrative privileges in the environment so I used the (net group “Domain Admins” / domain) command. And as a result all domain administrators are shown. The image below demonstrates the fact:

Press enter or click to view image in full size

After searching for sensitive files like passwords, backup files and other things, I came across the database connection string:

Press enter or click to view image in full size

By opening the database connection string file, it was possible to obtain the database password and login, as shown below:

Press enter or click to view image in full size

Finally, after obtaining the credentials of access to the database, in the reverse shell I put the information collected previously and I made a query in the database mentioned, and as a result I was able to obtain the password of the administrator of the application and the other users:

Press enter or click to view image in full size

So that’s it folks. This was simple I hope to have contributed a bit with you xD.

Sharing is Caring

best regards, fr0stNuLL
