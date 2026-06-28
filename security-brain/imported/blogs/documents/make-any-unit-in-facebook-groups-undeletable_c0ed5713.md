---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-09_make-any-unit-in-facebook-groups-undeletable.md
original_filename: 2018-10-09_make-any-unit-in-facebook-groups-undeletable.md
title: Make any Unit in Facebook Groups Undeletable
category: documents
detected_topics:
- idor
- access-control
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- business-logic
- api-security
language: en
raw_sha256: c0ed571316e84386e753e6e238d22e67d824e5154366233c06aff018dc2290f1
text_sha256: 8a81454892cd0eb26b45aef13f538a3c30ea81b6a7651a9bde853739d11a7e8b
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Make any Unit in Facebook Groups Undeletable

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-09_make-any-unit-in-facebook-groups-undeletable.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `c0ed571316e84386e753e6e238d22e67d824e5154366233c06aff018dc2290f1`
- Text SHA256: `8a81454892cd0eb26b45aef13f538a3c30ea81b6a7651a9bde853739d11a7e8b`


## Content

---
title: "Make any Unit in Facebook Groups Undeletable"
url: "https://medium.com/bugbountywriteup/make-any-unit-in-facebook-groups-undeletable-efb68e26adb9"
authors: ["Sarmad Hassan (@JubaBaghdad)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "IDOR", "Broken authorization"]
publication_date: "2018-10-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5655
scraped_via: "browseros"
---

# Make any Unit in Facebook Groups Undeletable

Make any Unit in Facebook Groups Undeletable
Sarmad Hassan (Juba Baghdad)
Follow
4 min read
·
Oct 10, 2018

60

Press enter or click to view image in full size

Sup guys, today I would like share with you how I was able to make any unit in facebook groups undeletable, so let’s get started :)

After Faebook Security Team asked me to confirm my last bug, I cam across Unit settings option in my test group, see the below photo

Press enter or click to view image in full size
More Settings Option for editing Units in your group

When I clicked on More Settings I saw the below options

You can put description and re-order your units of your group

hmmm interesting, I opened my Burpsuite and hit save to see what is going on behind the scene, and I saw the below request :

POST /groups/learning/edit_units_dialog/submit/?dpr=1 HTTP/1.1
Host: www.facebook.com

group_id=[my-group-ID]&description=[My-Unit-Description]&unit_ids[0]=[Unit ID no.1]&unit_ids[1]=[Unit ID no.2]…etc

As a bug hunter when you see this kind of request, of course you will check for the below two things:

1- group_id ===> Can I change my group ID to another group ID and add my units to it !!

2- Unit_ids ===> Can I change My Unit_ids with other groups unit ID’s and add them into my test group !!

So I changed the group_id to another group_id but it didn’t works :(

But when I changed my Unit_ids to another group unit IDs the response was like below:

200 response with no error :)

I checked my test group Units and I noticed that unit of the other group (that I am not admin on it) has been added to my test group

Press enter or click to view image in full size
Unit from other group added to my unit

I knew that facebook was only checking on group_id not unit_id that’s why I was able to add any unit to my group cause the server don’t check whether this unit is belong to the same group id or not.

OK, what next!!, I noticed two things:

1- When I add other Units to my group I can see it from the Group Insights option, which means I can download it too.

Get Sarmad Hassan (Juba Baghdad)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2- I can make those units from other group Undeletable once I added to my group and also I should invite the admin of other group into my test group.

Inviting the admin of other group was the trick to make their units undeletable.

I reported this bug to Facebook Security Team in 4-August-2018 and showed to them that I was able to make any unit undeletable and mentioned to them that units from other groups were added to my group, and I got answer from them as below:

They couldn’t reproduce the undeletable part, because they didn’t know about the invitation trick

When I saw this part from their reply “in your report. In our test when the attacker adjusts the id’s of the unit, the victims unit shows on the attacker’s page, however, the victim is still able to delete that unit”. he make feels like seeing Units (other group units that added to my test group) in My Unit tab is a normal issue and I thought they will know it can be downloaded through Group Insights , that’s why I only focused on Undeletable Unit part.

Coincidence

In 1-September-2018 I saw my fellow Richard Telleng posted bug in Facebook Bug Bounty Community group, when I saw his PoC video, it was the same bug that I submitted the same root, he submitted his bug in 18-August, while my bug was Triaged in 17-August, and he got bounty for it in 1- September, he only show how to download units from other groups using the Group Insights option, he didn’t know about the other impact (Undeletable unit).

I informed Facebook Security Team about this and told them that it was my bug and I am the first one who reported to you, they told me that I didn’t mention downloading other group units from Group Insights. so they only rewarded me the first impact which is (undeletable unit).

My Thoughts
Some people are connected to each other with a lot of things like thoughts, sharing ideas ..etc, It’s looks like Me and my fellow Richard Telleng are connected to each other with bugs :) see why.
Maybe some of you will say this is a silly bug, why Facebook pay for this, well, I think if someone can control your unit it’s not your unit anymore :).
Finally fixing this kind of bugs is always the right thing to do.

Timeline:
August. 04, 2018 — Initial Report
August. 17, 2018 — Report Triaged
September. 01, 2018 — Bug Fixed
September. 01, 2018 — Fix Confirmed
October. 05, 2018 — Bounty awarded

I would like to thanks Facebook Security Team for the Bounty.

Also I would like congratulate my fellow Richard Telleng for getting reward for the same bug.

PoC Video:

Takeways:

Don’t make the same mistake that I did, make sure you explain everything to the Security Team.

Thank you

Sarmad Hassan (JubaBaghdad)
