---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-04_low-hanging-fruits-on-facebook-group-room-unable-to-remove-post-on-group-when-po.md
original_filename: 2021-03-04_low-hanging-fruits-on-facebook-group-room-unable-to-remove-post-on-group-when-po.md
title: Low hanging fruits on Facebook Group Room. Unable to remove post on group when
  post room add with event ($500)
category: blogs
detected_topics:
- command-injection
- business-logic
- mobile-security
tags:
- imported
- blogs
- command-injection
- business-logic
- mobile-security
language: en
raw_sha256: cfd38b166faa197fbe01f6bd14fab2edf857aa71cb0cba0685fede05fb7f541b
text_sha256: 87d49f5e15f45fb1398403ece93b504ef331449a749175cb3502c5dbdfbb06d8
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Low hanging fruits on Facebook Group Room. Unable to remove post on group when post room add with event ($500)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-04_low-hanging-fruits-on-facebook-group-room-unable-to-remove-post-on-group-when-po.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, mobile-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `cfd38b166faa197fbe01f6bd14fab2edf857aa71cb0cba0685fede05fb7f541b`
- Text SHA256: `87d49f5e15f45fb1398403ece93b504ef331449a749175cb3502c5dbdfbb06d8`


## Content

---
title: "Low hanging fruits on Facebook Group Room. Unable to remove post on group when post room add with event ($500)"
url: "https://randyarios.medium.com/low-hanging-fruits-on-facebook-group-room-b8d17c7ea886"
authors: ["Randy Arios"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "500"
publication_date: "2021-03-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3841
scraped_via: "browseros"
---

# Low hanging fruits on Facebook Group Room. Unable to remove post on group when post room add with event ($500)

Randy Arios
Follow
2 min read
·
Mar 4, 2021

24

Low hanging fruits on Facebook Group Room. Unable to remove post on group when post room add with event ($500)

Hello reader,

My name is Randy Arios and this is the story about my finding on facebook.com, this is also my 1st write-up after a long time not publishing my advisories and Bug Bounty finding.

OK, without wasting time lets we talk to the point. This finding is about low hanging fruit in facebook.com group room, when you join a group, there is 1 new menu (not really new actually) called room. A new way to spend time with friends, family and fellow group members.

i found that when we create/post room to group, and add event on that post. after the room ended the event we add before is not deleted with the room post and become an single post by it self and it can not be deleted.

Get Randy Arios’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

step to reproduce:
1. create room and add event on that and post to the group.
2. ended the room, and you will see the room ended but the event will become post.
3. delete the post event, you will get error and can not delete that “event” post

Press enter or click to view image in full size

after 3 weeks, i got reply from the Facebook security team that the issue has been fixed and i got $500 bounty.

Press enter or click to view image in full size

Time Line:

3 February 2021 : Report send
6 February 2021: Triaged
26 February 2021: Bounty Paid (even though the fix is still pending)
3 March 2021: Issue Fully resolved and confirmed.

I am sorry if my English is not good, and also sorry if the write-up very simple, i am kind of lazy guys hahaha..

Thanks for reading.

#facebook #bugbounty #writeup
