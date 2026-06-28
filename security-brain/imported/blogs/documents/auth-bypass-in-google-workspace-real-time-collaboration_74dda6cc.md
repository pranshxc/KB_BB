---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-20_auth-bypass-in-google-workspace-real-time-collaboration.md
original_filename: 2021-04-20_auth-bypass-in-google-workspace-real-time-collaboration.md
title: Auth Bypass in Google Workspace Real Time Collaboration
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 74dda6ccf160b9a3b8a095a17823eb7951f859f7606705c8276d1c9e4d8bf794
text_sha256: b148d9501306ec938af3b197dceb12d7001442cbf2ab9ed17c3183518d98a8bd
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Auth Bypass in Google Workspace Real Time Collaboration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-20_auth-bypass-in-google-workspace-real-time-collaboration.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `74dda6ccf160b9a3b8a095a17823eb7951f859f7606705c8276d1c9e4d8bf794`
- Text SHA256: `b148d9501306ec938af3b197dceb12d7001442cbf2ab9ed17c3183518d98a8bd`


## Content

---
title: "Auth Bypass in Google Workspace Real Time Collaboration"
page_title: "[#0002] Moving the cursor and acting as other people in Google Docs products | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0002"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0002"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Google"]
bugs: ["Authentication bypass", "Information disclosure"]
publication_date: "2021-04-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3723
---

#0002  
Vendor: Google  
Status: unfixed  
Reported: Jan 20, 2021  
Disclosed: Apr 20, 2021 (90 days) 

# Moving the cursor and acting as other people in Google Docs products

**Short summary:**

In products that use the same real-time collaboration system as Google Docs, an attacker could take over other user’s “real-time sessions”. This means that the attacker could chat, move the cursor, and perform other collaboration-related actions in the name of any victim.

**POC Video:**

<https://youtu.be/q34AZ3I4gK8> \- `2:37`

**Core Issue:**

The real-time collaboration system uses a custom 16 char long session ID to authenticate users. When a user opens e.g. a Docs document, the page starts polling the `/bind` endpoint, which returns as soon as a new event occurs on the document.

The core issue is that the events received by this endpoint _almost always_ contain the session ID of the event initiator. For example, if a new user joins the document, everyone who already has the document open will receive a user object with the new user’s name, profile picture, and among others, **with the new user’s session ID**.

The obtained session ID then can be used to perform real-time actions in the name of that user.

**Steps to reproduce:**

_This is a written version of the attack performed in the POC video._

  1. Install Burp Suite
  2. Create 3 new users, `Attacker`, `Victim`, and `Observer`
  3. Only start proxying `Attacker`’s traffic with Burp
  4. With `Victim`, Create a new Document, and invite `Attacker` and `Observer` as `Editor`s
  5. Open the document in all 3 browser windows
  6. Refresh `Victim`’s page to generate a new join event on the `/bind` endpoint
  7. In Burp, look for new `/bind` responses, and find the one that includes `Victim`’s user object
  8. Note the `Victim`’s `sid` from the user object, and `Attacker`’s `sid` from the `/bind` request’s `sid` parameter
  9. Go to `Proxy` -> `Options` -> `Match and Replace` and click `Add`
  10. Set the type to `Request first line`, set `Match` to `Attacker`’s `sid`, set `Replace` to `Victim`’s `sid`, and click `OK`
  11. With `Attacker`, send a new chat message
  12. With `Observer`, open the chat pane, and see that the message was sent by `Victim`
  13. With `Attacker`, start typing and/or selecting text
  14. With `Observer`, see that it looks like `Victim` is selecting/editing the document

**Extra Attacks:**

  * Other actions can also be performed when the attacker has the victim’s session ID. For example, using the `/leave` endpoint, the victim can be “kicked off” from the document, making her invisible for the other users (but can still edit). Any other endpoint that authenticates with that session ID is probably vulnerable, like `/active`.
  * Moving the cursor requires `Editor` or `Commenter` privileges, so a normal `Viewer` can’t move the cursors of `Editor`s, since the permission is checked on a Google session level. But, endpoints like `/chat` and `/leave` can be used by `Viewer`s as well. **I was able to chat in the name of any editor with an anonymous (not logged in) account when the document was link-shared with the`Viewer` permissions.** That is interesting, since by design only `Editor`s and `Commenter`s should be able to chat, other roles can’t even see the chat pane.
  * Changing the `sid` (from `Attacker`’s to `Victim`’s) in the `bundles` object when making an edit with `Attacker` will crash `Victim`’s page, with the message `Unable to load file - Try to load it again or send an error report.`. Other `Viewer`s will not crash, and **if they have the`Live edits` accessibility pane enabled, they will see that the edit was made by `Victim`**. The edit initiator (`Attacker`) will be correctly shown in the `Version history`.

**Limitations:**

  * Changing the `sid` in the `Request first line` only changes the user of the `selection` commands. So, it looks like `Attacker` is typing in the name of `Victim`, but actually, `Attacker` is **only moving the cursor** in the name of `Victim`, and editing using her own account. So, checking `Version history` will correctly show that the edits were made by `Attacker`.
  * In my research, I wasn’t able to trick the `Version history` using these session IDs, as it is most likely checking the user’s full Google session.

**[Disclosure Warning]:**

_This is a new system I am experimenting with:_

**This issue is subject to a 90 day disclosure deadline.** On `2021-04-20` this issue with all additional comments will be publicly disclosed. Sensitive details from the report/comments such as names/email addresses will be redacted. If you would like to redact additional information or if for some reason the issue can’t be fixed until the deadline, let me know in a comment.

Thank you!
