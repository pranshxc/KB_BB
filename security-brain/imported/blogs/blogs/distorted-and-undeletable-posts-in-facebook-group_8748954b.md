---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-12_distorted-and-undeletable-posts-in-facebook-group.md
original_filename: 2018-08-12_distorted-and-undeletable-posts-in-facebook-group.md
title: Distorted and Undeletable Posts in Facebook Group
category: blogs
detected_topics:
- sso
- access-control
- command-injection
- csrf
- business-logic
- api-security
tags:
- imported
- blogs
- sso
- access-control
- command-injection
- csrf
- business-logic
- api-security
language: en
raw_sha256: 8748954b6c32ca7890ad8dd8e017439c1bf97558c146e4f026e461ec8120762d
text_sha256: 80fb8194cf8384d6333f1d6484e2424b3a28f1d0629a601b734700c8c295e1e6
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Distorted and Undeletable Posts in Facebook Group

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-12_distorted-and-undeletable-posts-in-facebook-group.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, csrf, business-logic, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `8748954b6c32ca7890ad8dd8e017439c1bf97558c146e4f026e461ec8120762d`
- Text SHA256: `80fb8194cf8384d6333f1d6484e2424b3a28f1d0629a601b734700c8c295e1e6`


## Content

---
title: "Distorted and Undeletable Posts in Facebook Group"
url: "https://medium.com/bugbountywriteup/distorted-and-undeletable-posts-in-facebook-group-9424e15f5551"
authors: ["Sarmad Hassan (@JubaBaghdad)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
publication_date: "2018-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5753
scraped_via: "browseros"
---

# Distorted and Undeletable Posts in Facebook Group

Distorted and Undeletable Posts in Facebook Group
Sarmad Hassan (Juba Baghdad)
Follow
5 min read
·
Aug 13, 2018

266

1

Sup guys, Today I would like to share with you an interesting bug that I found in facebook group through their BugBounty program, so let’s get started :)

one day in June 18, I was trying to test Live Video option in facebook group cause I never tested it before, so I created Live video in my test group (Attacker group)and I spent some time playing around with this option searching for something that may leads me to a valid bug, but unfortunately I didn’t find anything in it :(

so I wanted to delete my live video post by clicking on the three dots, and I saw this:

Unit option will appear in the post option, if you enabled units in the group

as you can see in the above image there is an option called Units.

What is Units: Units feature, allows you to leverage the group as a platform for online course content or to simply organize your posts by topic, for more details check this link.

Note: Only admin of group can create, edit, delete or add post in the Units.

I said to myself I remember I’ve already tested that option (Units Option) before but I didn’t find anything interesting in it, but when I saw it again I said to myself, let’s give it a shot one more time cause I never tested it from this place, so I clicked on “ Add to new unit” and I saw this:

when you create new unit this window will pop up, fill the details and create new one

I filled the details randomly and Intercepted the request with Burpsuite, the request was like as below:

POST /groups/learning/create_with_post/?group_id=[My_Test_Group_ID]&post_id=[My_Post_ID]&dpr=1 HTTP/1.1

jazoest=[number]&fb_dtsg=[anti_csrft ]&unit name=bla&unit description=bla&post title=bla

when I saw the above request, two things caught my attention, group_id= and post_id=

I asked myself two questions:

1-what will happen if I change my group_id value to another group id (victim group), is it possible to create new unit and add my post (Live video post) in the other group (victim group).

2- what will happen if I change my post_id value to other post id from another group (victim group), is it possible to add posts from other group (victim group) to my unit in my test group (attacker group).

All right let’s do it and see :), So I changed the group_id value to another group (victim group), but it didn’t work :(

Distort Posts:

O.K. let’s try to change the post_id value with another post id from another group (Victim_group), the response was as below:

HTTP/1.1 200 OK

for (;;);{“__ar”:1,”payload”:null,”jsmods”:{“require”:[[“ServerRedirect”,”redirectPageTo”,[],[“\/groups\/[attacker_group_id]\/learning_content\/?filter=filter number&post=[victim_post_id],false,false]]]},”js”:[“IO8eo”,”EizOb”],”bootloadable”:{},”resource_map”:{“IO8eo”:{“type”:”js”,”src”:”https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ioAY4\/yo\/l\/en_US\/rcyi0X4VRXd.js”,”crossOrigin”:1},”EizOb”:{“type”:”js”,”src”:”https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i6Hv4\/yd\/l\/en_US\/si3hiFNne1g.js”,”crossOrigin”:1}},”ixData”:{},”gkxData”:{},”lid”:”lid number"}

When I saw the above response, I directly Switched to the victim group account and I checked the post and I saw this :

Attachment Unavailable appears when the attacker added “text post only” from victim group to his unit

as you can see above, I was able to Distort post (only text post) in victim group and make it look like the above ugly form.

Undeletable Post:

I tried to reproduce the bug again and applied it to another victim group (noobs group) just to make sure that the bug is working in all types of groups, so I get the request from my group as an attacker and replaced the post_id value with post_id of victim group (noobs group), knowing that (The post was mine but in victim group that I’m not admin in it), the response give me 200 o.k. and everything was working like a charm, but when I checked my post in the victim group (noobs group) I saw this:

Delete me if you can was the title of attacker unit in his group, and it appears above the post in victim group

as you can see above, I saw my unit title appear in my post in the victim group, hmmm that’s weird, when I tested the bug in the first victim group I saw “Attachment Unavailable” , but when i tested it again in another victim group (noobs group), I was able to put the title of my unit above any post and make the post undeletable by its owner and by admin of the group, that’s really weird right!!!!

Get Sarmad Hassan (Juba Baghdad)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Wtf is going on!! After playing around for a little bit, I figured it out, below is the conclusion of the bug Impact:

the bug have two impacts:

1- Attacker can Distort only Text Post in victim group for any member (Admin, Moderator, normal user), if the owner of the post is not a member in the attacker group.

2- Attacker can make any post (Photo, Video, Events ..etc) for any member (Admin, Moderator, normal user)in victim group Undeletable and also can put title of his unit above the vicim post, by just inviting the owner of the post in his group (Attacker group).

Coincidence

After I submitted the bug to Facebook Sec. Team, I remembered that I read that before about undeleteble post in facebook, so I searched in google and I saw this :

Other bug hunter have already found the bug before me in May 9, 2018

when I saw that video it was the same bug but from different end point, at the same time I was shocked wtf!!!, I said if he disclosed the bug in youtube it means the bug is fixed, but to make sure let’s search for this researcher and contact him, so I found his facebook account and I talked to him about the bug, I told him that the bug is still working, he told me the bug is fixed and facebook had already rewarded him bounty for that, I also informed Facebook Sec. Team about the whole story.

I just want to thanks Richard Telleng (The researcher who found the bug before me) for his honest and politeness, you’re really a great guy, thank you so much for your huge support, I really appreciate that my bro.

Timeline:
June. 18, 2018 — Initial Report
June. 20, 2018 — Report Triaged
July. 31, 2018 — Bug Fixed
July. 31, 2018 — Fix Confirmed
Aug. 02, 2018 — Bounty awarded

I would like to thanks Facebook Security Team for the Bounty.

PoC Video:

Takeways:

1- Try to check the option that you’re testing from different areas, there is a chance that you will find something interesting in it.

2- If you faced the same situation that I faced, try to contact with the other researcher, asked him whether the bug is fixed or not, and just be honest with him.

3- Be honest with the Security Team too, just to make sure every thing is clear.

Thank you

Sarmad Hassan (JubaBaghdad)
