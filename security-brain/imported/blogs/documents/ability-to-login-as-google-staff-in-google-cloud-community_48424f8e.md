---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-15_ability-to-login-as-google-staff-in-google-cloud-community.md
original_filename: 2022-07-15_ability-to-login-as-google-staff-in-google-cloud-community.md
title: Ability to login as google staff in Google Cloud Community
category: documents
detected_topics:
- access-control
- command-injection
- password-reset
tags:
- imported
- documents
- access-control
- command-injection
- password-reset
language: en
raw_sha256: 48424f8e0c7abac16dcbfbb708a2982c18d46d816d3ad91b1f31b28ffe276f47
text_sha256: 438f4a31fd0e9b8247abe1a434ff16a2ce15bc0d5828dd4b3427109f2fa7de66
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Ability to login as google staff in Google Cloud Community

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-15_ability-to-login-as-google-staff-in-google-cloud-community.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, password-reset
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `48424f8e0c7abac16dcbfbb708a2982c18d46d816d3ad91b1f31b28ffe276f47`
- Text SHA256: `438f4a31fd0e9b8247abe1a434ff16a2ce15bc0d5828dd4b3427109f2fa7de66`


## Content

---
title: "Ability to login as google staff in Google Cloud Community"
url: "https://medium.com/@bhatiagaurav1211/ability-to-login-as-google-staff-in-google-cloud-community-57c45809de05"
authors: ["Gaurav Bhatia"]
programs: ["Google"]
bugs: ["Privilege escalation"]
bounty: "100"
publication_date: "2022-07-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2446
scraped_via: "browseros"
---

# Ability to login as google staff in Google Cloud Community

Ability to login as google staff in Google Cloud Community
gaurav bhatia
Follow
2 min read
·
Jul 15, 2022

121

-Gaurav Bhatia (Bug Hunter, CTF Player)

Summary:-

While using Google Cloud Community I saw that there was a feature of creating an account which we usually don’t see in any other google domains. I simply created an account for accessing the website as a normal user and to see the various functionalities. I started with creating a post and when the post got created I remembered that after creating an account i didn’t get any email verification mail nor there was any email verification after creating a post. It means that there is verification of email after creating an account. This bug doesn’t have a great impact on the organization so I thought to escalate it to increase the impact.

Get gaurav bhatia’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I came up with the idea of what if we get a google staff privilege? For this i tried to create an account with test@google.com and the account successfully created.

Press enter or click to view image in full size

And as shown in the picture i got the google staff privileges which gives the permission of uploading videos and replying to any other users being an internal google staff.

Steps To Reproduce:-
Go to https://www.googlecloudcommunity.com/gc/user/userregistrationpage?dest_url=https%3A%2F%2Fwww.googlecloudcommunity.com%2Fgc%2FGoogle-Cloud%2Fct-p%2Fgoogle-cloud
Create a account with mail id (test@google.com)
Account successfully created without any requirement of email verification
Finally, Got the privilege of replying to any member being an internal google staff.
Attack Scenario(Impact):-

An attacker can login as internal google staff and can spread malicious URLs, files, etc. Also an attacker can spread rumors among the communities being an internal google staff which makes a negative impression of google in people’s mind.

Timeline:-
2022–02–24: Initial Report to Google VRP
2022–02–24: Issue Triaged
2022–03–09: Internal bug report filed
2022–03–25: VRP issued reward($100)
