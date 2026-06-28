---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-19_an-idor-lead-joins-any-group-makes-me-2500.md
original_filename: 2023-08-19_an-idor-lead-joins-any-group-makes-me-2500.md
title: An IDOR lead joins any group makes me $2,500
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- automation-abuse
- cors
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- automation-abuse
- cors
language: en
raw_sha256: b67638143726c3ddd5c3c2f916baab3aafbf878a72c843511b76621ba9f2dcae
text_sha256: d98f6eb5ef447243bc91c79cd16f77cfe5fbc29603509d04cd86986acc320f50
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# An IDOR lead joins any group makes me $2,500

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-19_an-idor-lead-joins-any-group-makes-me-2500.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, automation-abuse, cors
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `b67638143726c3ddd5c3c2f916baab3aafbf878a72c843511b76621ba9f2dcae`
- Text SHA256: `d98f6eb5ef447243bc91c79cd16f77cfe5fbc29603509d04cd86986acc320f50`


## Content

---
title: "An IDOR lead joins any group makes me $2,500"
url: "https://infosecwriteups.com/an-idor-leads-join-any-group-makes-me-2-500-406eb9e463a3"
authors: ["Arman (@M7arm4n)"]
bugs: ["IDOR"]
bounty: "2,500"
publication_date: "2023-08-19"
added_date: "2023-08-21"
source: "pentester.land/writeups.json"
original_index: 846
scraped_via: "browseros"
---

# An IDOR lead joins any group makes me $2,500

An IDOR lead joins any group makes me $2,500
M7arm4n
Follow
3 min read
·
Aug 19, 2023

573

1

Press enter or click to view image in full size
What’s IDOR!?

IDOR stands for “Insecure Direct Object References.” It’s a type of security vulnerability that occurs when an application allows an attacker to access or manipulate resources directly by modifying input parameters, such as URLs, without proper authorization. In other words, an attacker can bypass access controls and gain unauthorized access to objects (such as files, databases, or other resources) that they should not have access to.

IDOR vulnerabilities typically arise when an application relies on user-supplied input to determine which object or resource to retrieve but does not properly validate or authorize the user’s access to that object. This can occur when an application exposes internal identifiers, like database record IDs, in URLs or parameters without properly checking whether the current user has permission to access those resources.

Overview of the Vulnerability

This website has a feature to create a private group, and group management can allow other users to access them by sending invitations, normally the information of private groups is confidential and inaccessible. When you are invited to a private group, in a part of the site you can see your invitations and accept or reject them. When you click Accept, the following message will be sent:

POST /GroupInvitations HTTP/1.1
Host: redacted.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://redacted.com/GroupActivity
Content-Type: application/x-www-form-urlencoded
X-Xsrf-Token: 6c2be6f7-3880-4652-951b-9ef779f201d6
Content-Length: 37
Origin: https://redacted.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

GroupInvitations&action=A&c2mId=7069

the c2mId parameter is a code for the invited group and is vulnerable to IDOR, The attacker by changing this value to upper or downer can easily access other private groups.

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps to reproduce

Create 3 accounts: Manager, Attacker, user.
Create 2 groups with the Manager account.
Invite the Attacker user to group A.
From attacker accepts the invitation and sends the request to the repeater.
Back to the manager Account and invite the user to group B.
Back to the repeater and add one digit to c2mId.
Go to the attacker account and see group B.

As a manager I created 2 different groups, Group-AAAA & Group-BBBB and both were private so other users were unable to leave comments and create topics, etc.

I invited the attacker to Group-AAAA to show you the flow of accepting and saving the request to the Burp repeater. So the attacker has access to Group-AAAA. The manager invited another user to Group-BBBB, but the attacker did not invite them to this group.

the attacker increased one to the c2mId value parameter and sent the request. Now the attacker refresh my group’s Page. The attacker of our story has access to Group-BBBB and can leave comments create topics etc. :D I should note that the value of c2mId is not one use. Even if a normal user accepts the innovation attacker can use this value again to access the groups.

Press enter or click to view image in full size
