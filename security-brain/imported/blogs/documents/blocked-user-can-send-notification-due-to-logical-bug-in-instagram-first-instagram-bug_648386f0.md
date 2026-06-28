---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-14_blocked-user-can-send-notification-due-to-logical-bug-in-instagram-first-instagr.md
original_filename: 2020-03-14_blocked-user-can-send-notification-due-to-logical-bug-in-instagram-first-instagr.md
title: Blocked User Can Send Notification Due to Logical Bug in Instagram | First
  Instagram Bug
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- business-logic
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- business-logic
- mobile-security
language: en
raw_sha256: 648386f03e97dc6511b8747f93c1ff1be32897c99bbb53516c70af7326333aeb
text_sha256: ac0552cf709a77f43f22de4bbc82652b8bec4c1d3b3c65e72d7959d717536af0
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Blocked User Can Send Notification Due to Logical Bug in Instagram | First Instagram Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-14_blocked-user-can-send-notification-due-to-logical-bug-in-instagram-first-instagr.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, business-logic, mobile-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `648386f03e97dc6511b8747f93c1ff1be32897c99bbb53516c70af7326333aeb`
- Text SHA256: `ac0552cf709a77f43f22de4bbc82652b8bec4c1d3b3c65e72d7959d717536af0`


## Content

---
title: "Blocked User Can Send Notification Due to Logical Bug in Instagram | First Instagram Bug"
url: "https://medium.com/bugbountywriteup/blocked-user-can-send-notification-due-to-logical-bug-in-instagram-first-instagram-bug-2bd09aa52f14"
authors: ["Divyanshu Shukla (@justm0rph3u5)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2020-03-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4711
scraped_via: "browseros"
---

# Blocked User Can Send Notification Due to Logical Bug in Instagram | First Instagram Bug

Blocked User Can Send Notification Due to Logical Bug in Instagram | First Instagram Bug
Divyanshu
Follow
4 min read
·
Mar 14, 2020

167

1

Privacy Violation issue Instagram.

Description:

Block feature allows any user to block any other user whom they don’t want to interact or view their profile. There is a separate mute button when a user doesn’t want to block another user but don’t want to view their posts/story/message.

Here while testing I was able to find a way by which user who has blocked another user can still receive the notification which can lead to privacy violation.

Vuln Type:

· Privacy / Authorization

Product:

· Android

· Version: 108.0.23.19

Impact:

Suppose user A was harassing user B, so user B blocked the harasser. But earlier they used to know each other so they had all the chat in the message. But when harasser wants, he can make sure that user B receives a notification on Instagram which may disturb the user B who has blocked user A(harasser).

Get Divyanshu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In a separate scenario even after blocking harasses (user B), user B can see the changes in the profile picture without any tool/special script and further can download the pictures.

Intended Behaviors:

Block feature is to completely block any user with no visibility in photos, comments or even notification. Blocked user and blocking user both shouldn’t be allowed to view the changes in profile picture or even shouldn’t be allowed to receive notification from each other.

Proof of Concept:
User A and User B are chatting over the message and they have collected a pretty good amount of chats over time.
User A — Attacker
User B — Victim
Press enter or click to view image in full size
Attacker harass the victim

2) Now User A started harassing user B and user B blocked the user A.

Press enter or click to view image in full size
User B (victim) | User B harassed by user A- So B blocked A.

3) User B (Victim) deleted the chat in messages after blocking the attacker (User A).

Press enter or click to view image in full size
Left (User A attacker) | Right (User B Victim)
Press enter or click to view image in full size
Victim (User B) deleted all the chats of attacker

4) Attacker cannot message the victim once blocked and according to logic there shouldn’t be any kind of notification from attacker to victim and vice versa.

Press enter or click to view image in full size
User B (victim) blocked User A (attacker)
Press enter or click to view image in full size
Attacker (Left) |Victim (Right): Attacker cannot message the victim

5) User A(harasser/attacker) starts liking the messages and photos sent in the chat.

Press enter or click to view image in full size
Attacker starts liking the messages from the past and victim gets notification even attacker is blocked. Left(Victim) | Right (Attacker)

6) User B receives notification from the attacker but on opening the notification screen is blank.

Press enter or click to view image in full size
On opening the notification screen is blank

7) In another test scenario, User B changes his/her profile picture and user A(harasser) can see the changes in the picture even when he/she is blocked.

Press enter or click to view image in full size
Request to capture victims user id by attacker

8) For this case though attacker can view message and follow option. It won’t affect the user. This scenario never worked but part of the POC.

Press enter or click to view image in full size
On replaying the view user request and replacing with victim’s public user id, attacker can see the page with follow and message request although even attacker tries to send follow request but victim won’t get notification for that.
Result:

The issue went duplicate.

Duplicate

Thanks
justmorpheus

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
