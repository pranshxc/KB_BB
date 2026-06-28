---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-15_facebook-group-members-disclosure.md
original_filename: 2021-03-15_facebook-group-members-disclosure.md
title: Facebook Group Members Disclosure.
category: documents
detected_topics:
- command-injection
- graphql
- information-disclosure
tags:
- imported
- documents
- command-injection
- graphql
- information-disclosure
language: en
raw_sha256: ded05f5527b7a6afe64bed90e71c7b58562961bf82c4710320fff49ebb2f7f19
text_sha256: 440fbc4de3ae473be0be7ff114e8cb59d6161620c1cc8818fcf8e945b7f0efd8
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Group Members Disclosure.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-15_facebook-group-members-disclosure.md
- Source Type: markdown
- Detected Topics: command-injection, graphql, information-disclosure
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `ded05f5527b7a6afe64bed90e71c7b58562961bf82c4710320fff49ebb2f7f19`
- Text SHA256: `440fbc4de3ae473be0be7ff114e8cb59d6161620c1cc8818fcf8e945b7f0efd8`


## Content

---
title: "Facebook Group Members Disclosure."
url: "https://spongebhav.medium.com/facebook-group-members-disclosure-e53eb83df39e"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "9,000"
publication_date: "2021-03-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3818
scraped_via: "browseros"
---

# Facebook Group Members Disclosure.

Facebook Group Members Disclosure.
Baibhav Anand
Follow
2 min read
·
Mar 15, 2021

411

2

Press enter or click to view image in full size

Hello bug bounty family, In this article I will be sharing about two of my bugs on Facebook. $4500 each, a total of $9000.

Bug 1st:

Description: A Non-member can determine if someone is the member of a private group or not via CometHovercardQueryRendererQuery graphQL mutation. Doc_ID: 4997502340291357. By changing the actorID with the victim’s actorID and groupID with the group we want to test and in the response if it shows “WeakEntityReference” than he/she is not the member of the group. However, if it shows “StrongEntityReference” than he/she is the member of the group.

Steps:
1. From a non-member’s account send this request by replacing the actorID variable to that of the victim and groupID variable to that of the group which you want to test against.

Press enter or click to view image in full size

2. If you get “StrongEntityReference” in response. He/She is the member of the group. However, If you get “WeekEntityReference” in the response he she is not the member of the group. Using this technique you can find out if someone is a member of the private group or not.

Get Baibhav Anand’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Bounty: $4500

Video: https://drive.google.com/file/d/1XAitPW8Evnoh11N8yQqkAxKkyX3zpFSK/view?usp=sharing

Bug 2nd: (using phone)

Description: It was possible to disclose the members of a private group via the endpoint in FbLite which is responsible to show group member posts.

Steps:
1. From User A account in Fblite (while I am the member of the group) I open the group.
2. From User A account in my PC (I leave the group)
3. Now when I click on members profile (I cannot see the group posts but I can see the membership dates)
4. Now I see the membership date of User B and User C after leaving the group.
5. From User B account in my PC I leave the group.
6. Now we will notice that membership date for User B disappeared as User B was no longer the member of the group but membership date for User C was still there.
7. Now to further confirm the vulnerability from User C account in my PC I left the group.
8. Now we will notice that the membership date also disappeared for User C, confirming the vulnerability.

Bounty: $4500

Video: https://drive.google.com/file/d/16Po19jSemG-SBwTMwfftQrFaZQ8zyXeN/view?usp=drivesdk

Thanks for making it to the end of this article. If you have any questions regarding anything, feel free to message me on Twitter: https://twitter.com/spongebhav
