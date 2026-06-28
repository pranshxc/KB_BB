---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-19_simple-sweet-bypass-email-update-restriction-to-change-emails-of-team-members.md
original_filename: 2021-01-19_simple-sweet-bypass-email-update-restriction-to-change-emails-of-team-members.md
title: 'Simple & Sweet: Bypass email update restriction to change emails of team members'
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 96c19ef16229301293009b31a386b2d6cfac52c404985adec7a1909fc87dd70c
text_sha256: 6a934f0a659b410613c3d6103e58b084a34af5a587b72b0cd199ecdc611980bb
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Simple & Sweet: Bypass email update restriction to change emails of team members

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-19_simple-sweet-bypass-email-update-restriction-to-change-emails-of-team-members.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `96c19ef16229301293009b31a386b2d6cfac52c404985adec7a1909fc87dd70c`
- Text SHA256: `6a934f0a659b410613c3d6103e58b084a34af5a587b72b0cd199ecdc611980bb`


## Content

---
title: "Simple & Sweet: Bypass email update restriction to change emails of team members"
url: "https://sunilyedla.medium.com/simple-sweet-bypassing-email-update-restriction-to-change-emails-of-team-members-6ce5770e7929"
authors: ["Sunil Yedla (@sunilyedla2)"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2021-01-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3983
scraped_via: "browseros"
---

# Simple & Sweet: Bypass email update restriction to change emails of team members

Sunil Yedla
 highlighted

Simple & Sweet: Bypass email update restriction to change emails of team members
Sunil Yedla
Follow
3 min read
·
Jan 18, 2021

157

Hello everyone, I hope you all are healthy and safe. Today I would like to explain my recent find that I have found in 1st week of Jan this year. As I always say, Test each and every functionality and break it. Today’s report also falls under the same.

One day, I received a Bugcrowd notification about my old accepted report raised on <redacted>.com, since it’s been so many months since I tested this program, thought of giving it a look. That makes this program as my first target this year and switched to work mode almost immediately.

In this website, users can invite other users in various different roles. Only admin users are allowed to edit details of other admins and low level users but admin’s are only allowed to edit profile details but restricted to change emails of any user. When you go to all users list and trying to edit profile details of other users, email field will be like this:

Press enter or click to view image in full size

Which means you cannot edit email address. So I’ve started various techniques to break it. One old technique we all knew was to inspect the element. I did the same

Now to bypass this, I have simply removed readonly=””

Press enter or click to view image in full size

As you can see, the blocker is removed now. So I have edited email address in this field and submitted form and to my surprise email got updated successfully.

So right now any admin can change email address of any other team member which according to targets workflow should not happen. Which confirms that client side validation exists but backend validation is missing. Quickly Raised a report on Bugcrowd. Report got Triaged within a week with Severity P3.

Press enter or click to view image in full size

The severity is accepted because as per the website workflow only admin role users can change email address of other users and victim user can still login with old credentials since the website did not allow email update but any action victim performs will be recorded with attacker updated email. So the severity is accepted.

Get Sunil Yedla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Timeline:

Report sent : 4–01–2021
Triage Team requested for more information : 07 Jan 2021
Triaged Report with severity P3 : 11 Jan 2021

I hope you like my above explanation. All is well. Want to connect? You can send your queries via Twitter: https://twitter.com/sunilyedla2 / Instagram: https://www.instagram.com/sunil_yedla/ . Good Day!
