---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-20_unprivileged-user-with-readwrite-permission-to-user-access-can-escalate-their-ro.md
original_filename: 2021-06-20_unprivileged-user-with-readwrite-permission-to-user-access-can-escalate-their-ro.md
title: Unprivileged User with Read/Write permission to `User Access` can escalate
  their role to ADMIN — Privilege Escalation
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 6379f39525afaa311594058d10c14d0557bd8574d7d1058967aec222482594a6
text_sha256: ceea630cff399f4e36dfdd19ebdb7b7716807c30d7028b74ebc8a16721af3e20
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Unprivileged User with Read/Write permission to `User Access` can escalate their role to ADMIN — Privilege Escalation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-20_unprivileged-user-with-readwrite-permission-to-user-access-can-escalate-their-ro.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `6379f39525afaa311594058d10c14d0557bd8574d7d1058967aec222482594a6`
- Text SHA256: `ceea630cff399f4e36dfdd19ebdb7b7716807c30d7028b74ebc8a16721af3e20`


## Content

---
title: "Unprivileged User with Read/Write permission to `User Access` can escalate their role to ADMIN — Privilege Escalation"
url: "https://ertugrull.medium.com/unprivileged-user-with-read-write-permission-to-user-access-can-escalate-their-role-to-admin-a217d2d280a8"
authors: ["Ertugrul Ozdemir  (@ertugrulphp)"]
bugs: ["Privilege escalation"]
publication_date: "2021-06-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3556
scraped_via: "browseros"
---

# Unprivileged User with Read/Write permission to `User Access` can escalate their role to ADMIN — Privilege Escalation

Unprivileged User with Read/Write permission to `User Access` can escalate their role to ADMIN — Privilege Escalation
Ertugrul
Follow
2 min read
·
Jun 20, 2021

270

Hello, I wanted to share with you the “Privilege Escalation” vulnerability that I found in a private program on HackerOne.

Summary:

Only a team member with membership read/write permissions can make himself admin.

Description:

While browsing the panel features, I discovered that there is a team building feature. Like everyone else, my first thought was to make a user with limited privileges admin. To try this out, I first created a role that only allowed read/write to user data. I invited the second e-mail address to my team with this role I created.

After logging into the system with my second account, all I could edit was my own role and name. When I inspected the role edit request, I saw a parameter named roleId= in the body of the POST request. It was in UUID format.

Press enter or click to view image in full size
Role edit request

Except for the admin role, there was permission to switch from my own role to lower roles. Because each different role created was custom created, they all had a different UUID value, but no UUID for the basic admin role. I guess it didn’t have the UUID value as it was already a role that existed when you created the account.

Get Ertugrul’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I realized that there was no UUID value for the admin role, I tried to continue the request by typing ADMIN in the roleId= parameter.

Press enter or click to view image in full size
I changed the roleId to ADMIN

I continued the request and when I refreshed the page, I was now an Admin, I could access all the panel content and could delete other admin accounts.

CVSS:
Press enter or click to view image in full size

Thanks for reviewed my first Medium post, happy hunting!

Twitter: @ertugrulphp
