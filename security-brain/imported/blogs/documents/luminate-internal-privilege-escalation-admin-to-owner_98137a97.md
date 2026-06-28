---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-21_luminate-internal-privilege-escalation-admin-to-owner.md
original_filename: 2017-09-21_luminate-internal-privilege-escalation-admin-to-owner.md
title: Luminate Internal Privilege Escalation — Admin to Owner
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: 98137a971d5b37ec8d5891df4e9f3d7bc8fb9358b502511e9ab0bdfb497de76c
text_sha256: 726351983ca05d451ddc4398d922c59d8670a5ed8d3753769de2fc17d6dbbbcc
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Luminate Internal Privilege Escalation — Admin to Owner

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-21_luminate-internal-privilege-escalation-admin-to-owner.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `98137a971d5b37ec8d5891df4e9f3d7bc8fb9358b502511e9ab0bdfb497de76c`
- Text SHA256: `726351983ca05d451ddc4398d922c59d8670a5ed8d3753769de2fc17d6dbbbcc`


## Content

---
title: "Luminate Internal Privilege Escalation — Admin to Owner"
url: "https://medium.com/@rojanrijal/luminate-internal-privilege-escalation-admin-to-owner-2ca28e575985"
authors: ["Rojan Rijal (@uraniumhacker)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Broken authorization"]
publication_date: "2017-09-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6095
scraped_via: "browseros"
---

# Luminate Internal Privilege Escalation — Admin to Owner

Luminate Internal Privilege Escalation — Admin to Owner
Rojan Rijal
Follow
3 min read
·
Sep 22, 2017

154

This is continuation of series of write-ups that will be posted regarding vulnerabilities found in Yahoo while participating in Yahoo’s bug bounty program.

Luminate offers three different services in their platform: 1) Web Hosting, 2) Store CMS and 3) Marketing. This is vulnerability writeup on Web Hosting service.

After buying Luminate’s web hosting service, user is provided with multiple internal services all of which are listed below:

Web Hosting (managing addons, installing softwares)
Email service
Access manager

In access manager, owner can invite other users to help them manage the domain and its hosting. Invited users can have either of two roles: 1) Administrators or 2) Limited user with access to tools that owner specifies.

For this writeup, let User A be Owner and let User B be the invited administrator.

Once user B is invited they have access to the web hosting service, access manager and all other services except for payment information for the organization. Through access manager, User B can also invite other users and edit their profile. When editing the profile, they can only change their name but not their email or expiration date. This system was found to have a flaw.

When the profile is saved, a POST request is sent with following data:

{"alias":"{name}","company":"","creation":1501976914,"email":"{email}","expiration":1517903999,"guid":"","modification":1501977146,"roles":{"actorrolesarray":[{"application":"YAHOO","creation":1501976914,"creator":"{usera_id}","display":"{role_name}","modification":1501976914,"name":"{role_id}"}],"count":1,"start":0,"total":1},"status":"ACTIVE","yuid":"{userb_id}"}&profile_yuid={userb_id}&crumb={crumb}&action=update

When we break down the data, what we care about will be two things: 1) role_id and usera_id .

Get Rojan Rijal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First to see how this worked, I changed my role_id to be Owner instead of Admin . Once that was done, I was assigned the role: Owner by the system however, because the default owner, user A, was still there, I did not have Owner permissions yet.

Next goal was to remove the main owner. This however was protected because user A profile was protected from edits even by user A them self.

While investigating further the user ids for both user B and user A caught my attention. When I saved user B’s profile, I could see the id of user A through the creator parameter. At the same time, user B’s id was passed in two places: yuid and profile_yuid. So, I decided to play around this section and see if this could be modified to conduct a solid attack.

I decided to switch around the parameters but first I had to find the creator id for the Owner. Finding this was simple because simply checking the source code of the page would give that information out. It turns out that the creator id of User A was user A’s own id because there were no prior users before that.

To attack this, I replaced the profile_yuid and yuid which had user B’s id with user A’s id. After that, I modified the {role_id} to Admin. I changed the role_id to Admin because user A already had role_id to Owner. After the request was sent, it initially did not work.

After about 30 mins of investigation, I found that I also had to change the following inputs: alias, email, expiration . These data were changed to have data of user A. These were also obtained from the source code.

Once that was done, user A was no longer an owner but an admin instead. After that I changed the expiration date of User A to be of the same day of attack. Once that day passed, user A had no access to edit web hosting, email management and access manager.

This exploit also worked if user B’s expiration date was really short. For example, if user A invited User B for about 1 day to manage something, User B could modify the expiration parameter and be a permanent member.

It has been a great pleasure working with Yahoo!’s security team. Be on the lookout for more reports write-ups that will be disclosed once they get resolved. :)

Timeline:
August 5, 2017: Report Submitted

August 10, 2017: Changed to Triaged

September 5, 2017: Report resolved

September 13, 2017: Bounty Awarded
