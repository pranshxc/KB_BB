---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-12_how-i-almost-got-2k-through-a-race-condition.md
original_filename: 2024-04-12_how-i-almost-got-2k-through-a-race-condition.md
title: How i Almost got 2K$ through a Race condition
category: documents
detected_topics:
- access-control
- mobile-security
- command-injection
- automation-abuse
- race-condition
- business-logic
tags:
- imported
- documents
- access-control
- mobile-security
- command-injection
- automation-abuse
- race-condition
- business-logic
language: en
raw_sha256: eaa8ef2f9c99e8465be3614e3a94835344de4c44aa0c92c23eb2d3ff90056f03
text_sha256: ad93baa8957fe4ab82693207e392aa23f696f45beaec2a3f3d663917009f32c0
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# How i Almost got 2K$ through a Race condition

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-12_how-i-almost-got-2k-through-a-race-condition.md
- Source Type: markdown
- Detected Topics: access-control, mobile-security, command-injection, automation-abuse, race-condition, business-logic
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `eaa8ef2f9c99e8465be3614e3a94835344de4c44aa0c92c23eb2d3ff90056f03`
- Text SHA256: `ad93baa8957fe4ab82693207e392aa23f696f45beaec2a3f3d663917009f32c0`


## Content

---
title: "How i Almost got 2K$ through a Race condition"
page_title: "How i gained organization takeover through a Race condition | by Anas Eladly ( 0x3adly ) | Medium"
url: "https://medium.com/@0x3adly/how-i-almost-got-2k-through-a-race-condition-3b09232b3a25"
authors: ["Anas Eladly (@0xanas_eladly)"]
bugs: ["Race condition"]
publication_date: "2024-04-12"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 346
scraped_via: "browseros"
---

# How i Almost got 2K$ through a Race condition

How i gained organization takeover through a Race condition
Anas Eladly ( 0x3adly )
Follow
4 min read
·
Apr 12, 2024

296

7

بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ

in the name of Allah, the most gracious, the most merciful

Today i will discuss a race condition finding that lead to gaining organization takeover unfortunately Didn’t get accepted and you will find out why

the target today is an eLearning website that allows teachers to create classes / add students and create tests for them, we will focus on user role management functionalities.

each class has 6 levels :

0 -> the user asked to join the class and pending admin’s approval

1 -> the user is a normal user in the class

3 -> the user is admin user in the class

-1 -> the user is rejected from joining the class

-2 -> the user is removed from the group (can still be restored by an admin)

-3 -> the user is permanently removed and can only join again by invitation or asking to join

a user can join the class either by requesting to join or by an invitation

now once i saw this feature i tried numerous attack scenarios including access controls, privilege escalations and Logic bugs but non of them worked and all lead to this message

this website was pretty secure

now i have spent 1–2 weeks on this program to come out empty handed so i had to think creatively.

now i have just finished my second rewatch of James Kettle’s smashing the state machine where he talked about Race condition in depth and what is there true potential.

i loved his Idea on multi-endpoint race condition and i have always wanted to implement them in one of my findings

so i thought of ways to use this technique in this target and then this idea came to my mind,

Get Anas Eladly ( 0x3adly )’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First you have to understand two things :

when the user requests to join the class / get’s invited into the class his user_id is set to 0
your user_id has to be set to 3 for you to be able to perform admin actions ( like adding and removing users in the class )

when an admin accepts / change a user’s role this is what the request looks like

Press enter or click to view image in full size

so my idea was :

when requesting to join the class ( setting your id to 0 ) their has to be a slight Race window where you are connected to this class but your user_id is not yet set, allowing us to perform admin actions, right ?

Press enter or click to view image in full size

i tried explaining the scenario through this illustration

so i grouped both the requesting to join a class request

and making my self admin in that class ( by making the same action in an attacker controlled class and changing the class id to the victim’s class id ) both in a group in the repeater

Press enter or click to view image in full size
Escalating my user to admin
Press enter or click to view image in full size
Joining the class request

then i Sent both requests in the same packet ( single packet attack ) and BOOM !! i am now an admin user in that class !

this looks like a p2, right ?

unforntualy not everything has a happy ending as this finding was pretty inconsistent ( out of 10 classes i tried this in only 4 were successful)

and once the attacker tried the attack on one class he can’t try it again as his user id is already set to 0 in that class

so this was closed as low severity and the program doesn’t reward bounties on those :D ( i think they scammed me there but we say الحمد لله علي كل حال)

i didn’t give up though and found 6 findings in their android application :D

but my main source of happiness was that i finally found a valid bug through multi-endpoint race condition even though it’s severity wasn’t that high

the main getaway from this target was to always spend more time on the application as the more time you spend fiddling around with functions the better you understand the application and think of more creative ways to exploit it

that's all for today, until we meet again.

Follow me on Social Media :

Facebook
Twitter
LinkedIn
