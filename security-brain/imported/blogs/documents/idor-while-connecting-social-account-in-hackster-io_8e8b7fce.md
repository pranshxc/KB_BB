---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-18_idor-while-connecting-social-account-in-hacksterio.md
original_filename: 2017-07-18_idor-while-connecting-social-account-in-hacksterio.md
title: IDOR While Connecting Social Account in Hackster.io
category: documents
detected_topics:
- idor
- access-control
- command-injection
tags:
- imported
- documents
- idor
- access-control
- command-injection
language: en
raw_sha256: 8e8b7fce9086d969dcb851cb41ea2f65744b30d7099a0786255dcc87d0954376
text_sha256: ed208b15647c8ec2f2931521c1eb7315d3a9f7e4353abbf18379882ee253416e
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR While Connecting Social Account in Hackster.io

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-18_idor-while-connecting-social-account-in-hacksterio.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `8e8b7fce9086d969dcb851cb41ea2f65744b30d7099a0786255dcc87d0954376`
- Text SHA256: `ed208b15647c8ec2f2931521c1eb7315d3a9f7e4353abbf18379882ee253416e`


## Content

---
title: "IDOR While Connecting Social Account in Hackster.io"
url: "https://medium.com/@arbazhussain/idor-while-connecting-social-account-in-hackster-io-2296b316b7a7"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
programs: ["Hackster.io"]
bugs: ["IDOR"]
publication_date: "2017-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6153
scraped_via: "browseros"
---

# IDOR While Connecting Social Account in Hackster.io

IDOR While Connecting Social Account in Hackster.io
Arbaz Hussain
Follow
1 min read
·
Jul 18, 2017

173

Hackster.io is a community dedicated to learning hardware, from beginner to pro. Share your projects and learn from other developers.

Weakness : Insecure Direct Object Reference (IDOR) CWE-639

Severity : High

Complexity : Simple~Easy

Steps to Reproduce :

1. Create a Account on Hackster.io With Email .

2. Then Logout.

3. Then Try to Login into That Account With Facebook 0Auth of Same Email .

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4. This Time Hackster.io Ask the User That “We Have Found Existing User Account Registered on Same Email , Link This Two Account’s”

Press enter or click to view image in full size

5. If you Check the URL of The Page .

/users/authorization/<USER-ID>/edit

6. Just Change the User ID to Any other Account , And Link Our Facebook Account to Their Email .

7. And We Got Logged into Victim’s Account Remotely .

Timeline:

Reported to Benjamin Larralde(Co-founder of Hackster.io) ~ May 31

Fixed ~ May 31

Hall of Fame:

https://hacksterio.freshdesk.com/support/solutions/articles/9000009848-i-found-a-bug-on-your-website-where-can-i-report-it-
