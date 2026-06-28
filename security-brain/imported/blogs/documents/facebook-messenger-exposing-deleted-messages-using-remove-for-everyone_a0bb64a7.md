---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-15_facebook-messenger-exposing-deleted-messages-using-remove-for-everyone.md
original_filename: 2019-08-15_facebook-messenger-exposing-deleted-messages-using-remove-for-everyone.md
title: Facebook Messenger exposing deleted messages using [Remove for Everyone]
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: a0bb64a7c697f9408357d4eacd3e68bf92a4b1dbd2de9d7e3440c156413d6ab0
text_sha256: 4f756b05ab2d408bbc2538575840ad3a9e555544fe5557df92ac81da600c180a
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Messenger exposing deleted messages using [Remove for Everyone]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-15_facebook-messenger-exposing-deleted-messages-using-remove-for-everyone.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `a0bb64a7c697f9408357d4eacd3e68bf92a4b1dbd2de9d7e3440c156413d6ab0`
- Text SHA256: `4f756b05ab2d408bbc2538575840ad3a9e555544fe5557df92ac81da600c180a`


## Content

---
title: "Facebook Messenger exposing deleted messages using [Remove for Everyone]"
url: "https://medium.com/@renwa/facebook-messenger-disclosing-deleted-messages-that-has-been-deleted-by-remove-for-everyone-1fb5a52cc7df"
authors: ["Renwa (@RenwaX23)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2019-08-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5080
scraped_via: "browseros"
---

# Facebook Messenger exposing deleted messages using [Remove for Everyone]

Facebook Messenger exposing deleted messages using [Remove for Everyone]
Renwa
Follow
3 min read
·
Aug 16, 2019

200

2

I don’t usually do write-ups for my findings but this one is so funny that every time i get a giggle when i think about how i found it, this also shows you don’t need to be a web expert to find bugs.

It’s July i was talking with a friend on FB messenger the topic was about boys, in one of my messages i made a typo instead of writing (kwr) i wrote (ker) both (w) and (e) keys are beside each other, this may look normal but..

I was talking in Kurdish and the translations are:

kwr = Boy

ker = Penis

It was embarrassing and i deleted the message immediately using [Remove for Everyone] feature, this will delete the message permanently in both sides and replace it with a text (You removed a message)

Press enter or click to view image in full size
Removing message box dialog

For a second i thought wait this may happened before and i didn’t notice it, Saying word (kwr) (boy) is not a rare thing and maybe i made this typo before. Messenger has a feature for searching for any message in all of your conversations so i used that to search for (ker), surprisingly this came out in the results:

Conversations search results

When i clicked to see the message it didn’t go to the conversations history and show the exact message, it only showed the result, Does that mean i made that typo before?

Get Renwa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After some investigation i figured out that that (1 result) prompt is my deleted message and i didn’t make any typos before.

But how is that possible? isn’t FB deleting that message permanently?

Using this bug i was able to see that FB is keeping a deleted message for about 9 days so next time think twice when you send nudes in Messenger, FB doesn’t state about this in anywhere but in the deleting dialog box it says you can still report a deleted message if it’s against community standards.

While reporting this to FB i made some nice POC’s using bruteforcing to recover a deleted message if it was a Porn website or a 4 digit number.

Here is the exact photo of my deleted message that lead to this discovery:

Typos can make you earn $

Isn’t that a funny find 😂

Press enter or click to view image in full size

Facebook patched it within a month are rewarded me with 0x1f4

buh-bye ~💜
