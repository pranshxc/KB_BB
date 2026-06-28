---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-20_facebook-bugbounty-disclosing-page-members_3.md
original_filename: 2018-12-20_facebook-bugbounty-disclosing-page-members_3.md
title: Facebook BugBounty — Disclosing page members
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 7b366769c8049cc20209eae1da47629afeea2298a8884fc886238150f1bb7d3f
text_sha256: e8d44085e1747586749f9304dbfb9e77c13691395e5dbddafb72e3e70715274c
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook BugBounty — Disclosing page members

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-20_facebook-bugbounty-disclosing-page-members_3.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `7b366769c8049cc20209eae1da47629afeea2298a8884fc886238150f1bb7d3f`
- Text SHA256: `e8d44085e1747586749f9304dbfb9e77c13691395e5dbddafb72e3e70715274c`


## Content

---
title: "Facebook BugBounty — Disclosing page members"
page_title: "Facebook BugBounty — Disclosing page members | by Nirmal Thapa | Medium"
url: "https://medium.com/@tnirmalz/facebook-bugbounty-disclosing-page-members-1178595cc520"
authors: ["Nirmal Thapa (@tnirmalz)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2018-12-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5511
scraped_via: "browseros"
---

# Facebook BugBounty — Disclosing page members

Facebook BugBounty — Disclosing page members
Nirmal Thapa
Follow
4 min read
·
Dec 20, 2018

292

2

Because of some privacy reasons, identity of page members (admins/mods/analysts) is kept secret by facebook and normal page visitors cannot find the details about these members. But.. back in July 2018, when I was hunting for bugs in Facebook, I found multiple ways to disclose members of a facebook page.

Disclosing post creators with 'Get messages' feature

This feature named “Get Messages” is available in Facebook pages when uploading posts and stuffs.

Get Messages feature

Mainly e-commerce and online shopping websites use this feature with one of their product so whenever a visitor wants to know more about that particular product, they can simply click on “Send message” button. A post with this feature enabled looks something like below screenshot.

Press enter or click to view image in full size
A post with “Get messages” feature enabled

The bug here is, if we click on this “Send message button”, profile ID of the creator is leaked in one of the responses coming from host https://x-edge-chat.facebook.com which is not visible in general..

Press enter or click to view image in full size
Inbox demo

.. but if we check burp suite logs, we can see that the ID of creator is leaked.

Press enter or click to view image in full size
Creator’s profile leaked

In the above screenshot, 100027117349417 is the ID of my test account.

Impact?

This particular bug is really easy to exploit and if an attacker needs to find the creator of a Facebook page, s/he can just go to the page, find posts with this feature enabled, click on send message button, check the logs and BOOM profile ID of the creator is disclosed.

Timeline

6th July 2018: Issue found and reported.

10th July 2018: First Reply by Facebook Security

11th July 2018: Issue triaged

27th July 2018: Issue fixed

4th Sep 2018: Bounty awarded *Nice bounty :P*

Disclosing the identity of people sending message on the behalf of page

When I was going through Burp Suite logs to report the above issue, I noticed this weird response too.

Press enter or click to view image in full size
Unknown_response.png

I was pretty sure this was something else and could lead to another leak so I just saved this screenshot and decided to look into this issue later.

Get Nirmal Thapa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

*Fast forward to 1 week later*

I tried to reproduce this issue by simply sending a message to the page as a normal visitor..

Sending message to a page as normal visitor

.. and replied from the page

Press enter or click to view image in full size
Replying to the above visitor from page

As soon as I recieved this “Hello visitor” message, I checked Burp Suite logs and saw this exact same response like before.

Press enter or click to view image in full size
Message senders’ profile leaked

Here, 100027405052940 is the profile ID of page member who replied “Hello visitor”. This means.. You send a message to a Facebook page, someone who has ability to read/reply messages replies to you and immediately his profile ID is leaked.

Surprised Pikachu

Impact?

Very very very easy to exploit. Anyone can just randomly send message to a facebook page, someone replies to that message and BOOM, their profile ID is leaked. ;)

Timeline

6th Jul 2018: Initial Discovery of bug

14th Jul 2018: Mystery behind the ‘leak’ found and reported

18th Jul 2018 3:37 AM: Issue triaged

18th Jul 2018 10:53 PM: Issue fixed

1st Aug 2018: Bounty awarded

T̶h̶a̶t̶’̶s̶ ̶a̶l̶l̶ ̶f̶o̶r̶ ̶2̶0̶1̶8̶.̶ ̶I̶ ̶h̶o̶p̶e̶ ̶t̶o̶ ̶d̶i̶v̶e̶ ̶m̶o̶r̶e̶ ̶i̶n̶t̶o̶ ̶F̶a̶c̶e̶b̶o̶o̶k̶ ̶B̶u̶g̶B̶o̶u̶n̶t̶y̶ ̶p̶r̶o̶g̶r̶a̶m̶ ̶i̶n̶ ̶2̶0̶1̶9̶ ̶❤

Thank you for reading this post. If you have any queries/suggestions, I’m available on Twitter :)

Happy Hacking!! .. until next time.
