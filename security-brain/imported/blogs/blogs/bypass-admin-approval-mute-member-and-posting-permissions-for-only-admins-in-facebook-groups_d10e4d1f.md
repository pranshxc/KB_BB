---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-18_bypass-admin-approval-mute-member-and-posting-permissions-for-only-admins-in-fac.md
original_filename: 2018-07-18_bypass-admin-approval-mute-member-and-posting-permissions-for-only-admins-in-fac.md
title: Bypass Admin approval, Mute Member and Posting Permissions for Only admins
  in Facebook groups
category: blogs
detected_topics:
- access-control
- command-injection
- graphql
- business-logic
- api-security
tags:
- imported
- blogs
- access-control
- command-injection
- graphql
- business-logic
- api-security
language: en
raw_sha256: d10e4d1f8a561fd759623bdacd8d2b5bc83b621fe7045b3fd1af215c0b5c64ca
text_sha256: 22285525be032c18ff57ee6403e895e802f362a547f3996ae719b0c4bc214589
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass Admin approval, Mute Member and Posting Permissions for Only admins in Facebook groups

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-18_bypass-admin-approval-mute-member-and-posting-permissions-for-only-admins-in-fac.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, graphql, business-logic, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `d10e4d1f8a561fd759623bdacd8d2b5bc83b621fe7045b3fd1af215c0b5c64ca`
- Text SHA256: `22285525be032c18ff57ee6403e895e802f362a547f3996ae719b0c4bc214589`


## Content

---
title: "Bypass Admin approval, Mute Member and Posting Permissions for Only admins in Facebook groups"
url: "https://medium.com/bugbountywriteup/bypass-admin-approval-mute-member-and-posting-permissions-for-only-admins-in-facebook-groups-ef476cb3d524"
authors: ["Sarmad Hassan (@JubaBaghdad)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
publication_date: "2018-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5804
scraped_via: "browseros"
---

# Bypass Admin approval, Mute Member and Posting Permissions for Only admins in Facebook groups

Bypass Admin approval, Mute Member and Posting Permissions for Only admins in Facebook groups
Sarmad Hassan (Juba Baghdad)
Follow
4 min read
·
Jul 18, 2018

460

3

Hello guys, today I want to share with you how I was able to Bypass Admin approval, Mute Member and Posting Permissions for Only admins in Facebook groups, so let’s get started :)

The story began when Facebook Security Team announced their Facebook June Whitehat Promotion in June 1, 2018, they said they will take only two researchers to join Defcon in Vegas for free for BEST QUALITY REPORT and HIGHEST REWARD VALUE.

I said hmmm sounds good, so let’s hunt some bugs maybe I got lucky to win that promotion, I directly opened my Facebook notes Document to see what areas I should start digging in it and I saw this:

Press enter or click to view image in full size
My Facebook Document Notes where I put everything related to facebook for future hunting

So what is Watch Party Option:

It’s a new feature in Facebook groups that allows Group admins even normal members to pick any public video on Facebook and show it to other members at the same time with a dedicated comment reel to create a “shared viewing experience”, for more Details.

This is how Watch Party Option looks like

as usual I opened my test group From Sarmad Hassan account and clicked on Watch Party Option to make a post and Intercepted the request with Burpsuite to see what is going on inside that feature, the request was as below:

POST /api/graphql/ HTTP/1.1
variables={“input”:{“client_mutation_id”:”2",”actor_id”:”userID”,”composer_session_id”:”SESSIONID”,”creator_actor_id”:”actorID”,”custom_name”:null,”group_id”:”MyTestGroupID",”video_ids”:[“VIDEO-ID”]}}&doc_id=doc-id

what brought my attention is ”group_id” parameter, I said let’s change the value of this group ID to my second test group ID from another account (group named Noobs), to see if I can make Watch Party post in Noobs group that I am member in it. and it works the response was as below:

{
“data”: {
“group_living_room_create”: {
“client_mutation_id”: “2”,
“living_room”: {
“__typename”: “LivingRoomSession”,
“id”: “id of the video party”
}
}
}
}

Bypassing Mute Members

hmmmm interesting, I Switched to my second test group (victim group)(group named Noobs) from my second test account in a virtual machine and then clicked on the Members tab and clicked on Sarmad Hassan (Attacker User) and Muted him from the group, so Saramd Hassan will not be able to Make any Post in the Noobs group

Admin of Victim Group (Noobs) Muted the attacker Sarmad Hassan

I Switched back to the first test group from Sarmad Hassan Account and made watch party post and changed the group_id to the victim group ID (Noobs) and boom, it works so even if the admin of victim group muted the attacker he still be able to make watch party video and Bypass mute option.

Bypass Admin approval and Posting Permissions for Only admins

I said OK let’s dig more and see what we can do with watch party, so I switched back again to My second group Noobs and clicked on group settings and checked the below things:

Post Approval: All group posts must be approved by an admin or a moderator
Posting Permissions: Only admins

if the admin checked the above options no one can make any post and if the posting permissions is set to anyone, all posts should be approved by the Admin

Get Sarmad Hassan (Juba Baghdad)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

so I got the Graph API call again from the first test group from Sarmad Hassan account and changed the group_id parameter to the victim group id (Noobs group) and booooom, the response was as below:

{
“data”: {
“group_living_room_create”: {
“client_mutation_id”: “2”,
“living_room”: {
“__typename”: “LivingRoomSession”,
“id”: “199255894077754”
}
}
}
}

I was like:

where “id”: “199255894077754” is the id of the watch party room

The attacker can go to :

https://www.facebook.com/groups/[group-id]/wp/[watch party room id]

and will be able to watch this video and invite all group members to see it, so Imagine with all these protections that made by the admin of victim group (Noobs), the attacker Sarmad Hassan Bypassed it ALL :), Imagine if you’re an Admin of group and you checked all the above settings to make sure no one can post in your group except you and you feels so happy, But someone actually can bypass that and make a post without your approval, what will you think!!!

Timeline:
June. 03, 2018 — Initial Report
June. 14, 2018 — Report Triaged
June. 27, 2018 — Fixed the first two impacts
July. 17, 2018 — Complete Fix
July. 18, 2018 — Fix Confirmed
July. 18, 2018 — Bounty awarded

I would like to thanks Facebook Security Team for the Bounty.

Also congratulations for the Winners SASAE and Pranav Meghsham for winning Facebook June Whitehat Promotion.

PoC Video:

Takeways:

1- Try to make a Document note for your target and check it from time to time

2- If you found a bug, don’t stop try to dig deeper maybe you get more than one impact

3- Always ask yourself what if !! when you search for bugs

4- If I can do it, You can do it too, trust me :)

Thank you

Sarmad Hassan (JubaBaghdad)
