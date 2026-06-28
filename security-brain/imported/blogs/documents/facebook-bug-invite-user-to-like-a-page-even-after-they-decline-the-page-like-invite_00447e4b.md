---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-14_facebook-buginvite-user-to-like-a-page-even-after-they-decline-the-page-like-inv.md
original_filename: 2021-08-14_facebook-buginvite-user-to-like-a-page-even-after-they-decline-the-page-like-inv.md
title: Facebook Bug:Invite user to Like a Page even after they decline the Page Like
  Invite
category: documents
detected_topics:
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 00447e4b08d80c064c0d299469994b808aa91be392b8999da2cbc14c839bf801
text_sha256: d75640cd8c31062b7121661bdf6f76a3ca8c1492905d3a905bec678a38f447b6
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Bug:Invite user to Like a Page even after they decline the Page Like Invite

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-14_facebook-buginvite-user-to-like-a-page-even-after-they-decline-the-page-like-inv.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `00447e4b08d80c064c0d299469994b808aa91be392b8999da2cbc14c839bf801`
- Text SHA256: `d75640cd8c31062b7121661bdf6f76a3ca8c1492905d3a905bec678a38f447b6`


## Content

---
title: "Facebook Bug:Invite user to Like a Page even after they decline the Page Like Invite"
url: "https://medium.com/bug-bounty-hunting/facebook-bug-invite-user-to-like-a-page-even-after-they-decline-the-page-like-invite-f83d9ec845b3"
authors: ["Circle Ninja (@circleninja)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2021-08-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3422
scraped_via: "browseros"
---

# Facebook Bug:Invite user to Like a Page even after they decline the Page Like Invite

Facebook Bug:Invite user to Like a Page even after they decline the Page Like Invite
Ronnie Joseph
Follow
3 min read
·
Aug 14, 2021

23

Note: This bug went informative. So if you are not interested please skip. Though I personally consider it valid.

Description/Impact

The bug makes it possible to again and again notify a fb user (friend) and send him page invite request even after he has “declined” the Page Like Request.

This enables a person to send Page Like invite request to a FB friend who has already declined the invite request to like the page.

Repro Steps

User named Ruth is owner of LOL page .
User named Tom is victim who has already decline request to like her page. (Tom is friend of Ruth)

1. As Ruth, go in mbasic.facebook.com , to the particular page she owns and click on Invite friends.
2. Select Tom from the list and save the request in burp repeater.
3. As Tom in another browser, we see that invite has come to like the page, but we now decline the request.
4. Go to burp repeater and again replay /resend the request for no. 2.
5. We see that as Tom he has once again received request For Page Like by Ruth which bypasses the block set up in FB for web.

Get Ronnie Joseph’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

By design, FB does not allows to resend page like invite request, once the user decline the request but here we see it can be bypassed.

Reply By Facebook:

Press enter or click to view image in full size

My reply:

Press enter or click to view image in full size

Reply by FB:

Press enter or click to view image in full size

My Take:

I don’t consider it just as an QA Bug. It is a bypass of their implementation(from the UI) which doesn’t allow a user to reinvite a person to like a page after the user has declined to like the page. So in an attack scenario, I may send hundreds of invite notifications to a victim and this will continue unless the user comes and block the page( which I consider another feature). If , they wanted to mitigate this by asking users to block the page; why was the Page Decline Feature implemented in the first place ?

The report was closed as informative and remains unfixed.
