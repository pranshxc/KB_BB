---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-09_idor-leads-to-project-takeover.md
original_filename: 2019-06-09_idor-leads-to-project-takeover.md
title: IDOR Leads To Project Takeover
category: documents
detected_topics:
- idor
- command-injection
- otp
tags:
- imported
- documents
- idor
- command-injection
- otp
language: en
raw_sha256: 909b4f3f4a6eb5d8b065909c51fdf3b4c55e4499abd4e61fc37e464fe22f7d2a
text_sha256: ce2accd0cba2cbbadf9313573a288666c929d175e07ad9411b45607d00a36a52
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR Leads To Project Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-09_idor-leads-to-project-takeover.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `909b4f3f4a6eb5d8b065909c51fdf3b4c55e4499abd4e61fc37e464fe22f7d2a`
- Text SHA256: `ce2accd0cba2cbbadf9313573a288666c929d175e07ad9411b45607d00a36a52`


## Content

---
title: "IDOR Leads To Project Takeover"
url: "https://medium.com/@hariharan21/idor-leads-to-project-takeover-548a1bfd4d66"
authors: ["Hariharan.s (@DJHARIZ1)"]
bugs: ["IDOR"]
publication_date: "2019-06-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5225
scraped_via: "browseros"
---

# IDOR Leads To Project Takeover

IDOR Leads To Project Takeover
Hariharan S
Follow
1 min read
·
Jun 9, 2019

101

It's all about Changes

Hi Guys,

This is my second bug bounty write up of how i managed to takeover a victims project using collaboration Invite.

A redacted.com is running a online project management service and people can post comments,images,files etc of their work on a single project. The admin of the project can add users as collaborators of the project.

Get Hariharan S’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The request of the collaboration invite was like this..

POST /project_api/project_invitation HTTP/1.1
Host: redacted.com
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://redacted.com
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 121
Connection: close

x_token=748f5bba976e3a202a7dbfa939271cde11e260fa52b7bbe4f3a024d80d08df92&project_id=5401234&role=1&emails=test%40test.com

And when i saw the request i thought..What If I

So we have 3 Request Parameters:

project_id=

role=

emails=

I Changed the request to:

project_id= Victims Project ID

role=0 (0=Owner, 1=Editor)

emails= My Email

I forwarded the request and ..

Checked my inbox and there it was ..A Collaboration Invite to the victims project as a owner . I was able to edit, delete, add more users, remove the original owner of the project etc

And i was like

I immediately reported the bug and recieved a good 3 digit bounty :)
