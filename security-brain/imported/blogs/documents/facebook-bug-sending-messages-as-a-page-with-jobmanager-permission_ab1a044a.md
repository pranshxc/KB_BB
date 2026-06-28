---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-15_facebook-bug-sending-messages-as-a-page-with-jobmanager-permission.md
original_filename: 2019-07-15_facebook-bug-sending-messages-as-a-page-with-jobmanager-permission.md
title: 'Facebook Bug : Sending messages as a page with jobmanager permission'
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: ab1a044a4b848be1a9d4a0f04de3ac96a11f78d51c581fa632c5838cafa562fe
text_sha256: 9a6ab830abf0b6494e60948d3184ac05ee8c492847253ed326bda77b85f726b5
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Bug : Sending messages as a page with jobmanager permission

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-15_facebook-bug-sending-messages-as-a-page-with-jobmanager-permission.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `ab1a044a4b848be1a9d4a0f04de3ac96a11f78d51c581fa632c5838cafa562fe`
- Text SHA256: `9a6ab830abf0b6494e60948d3184ac05ee8c492847253ed326bda77b85f726b5`


## Content

---
title: "Facebook Bug : Sending messages as a page with jobmanager permission"
url: "https://medium.com/@0x01devansh/facebook-bug-sending-messages-as-a-page-with-jobmanager-permission-763dc0d8e32c"
authors: ["Devansh batham (@devanshwolf)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Privilege escalation"]
publication_date: "2019-07-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5149
scraped_via: "browseros"
---

# Facebook Bug : Sending messages as a page with jobmanager permission

Facebook Bug : Sending messages as a page with jobmanager permission
Devansh batham
Follow
3 min read
·
Jul 15, 2019

77

Hey , One of my college friend called me , and said she wants to hire some content creators and graphic designers for her page , She was asking for an efficient way of hiring ,I told her about “Facebook Jobs”and how she can find/recruit creators using this feature.

Facebook Jobs

Anyone can find jobs in the Jobs dashboard at facebook.com/jobs and the “Jobs” option in the “Explore” section on mobile, by clicking the Jobs icon in Marketplace, or visiting the Jobs tab of a business’ Page.

Confusion for her

She isnt tech savvy, so she asked me if I can create and publish jobs on behalf of her page, I agreed and asked her to assign me as a “Jobmanager” of her page.

A lil about “Jobmanager”

Facebook allows 6 different roles for Facebook Pages ,among those one role is of “Jobmanager”

Privileges of Jobmanager :

View insights.
Create ads, promotions or boosted posts.
View Page Quality tab.
See who published as the Page.
Publish and manage jobs.

Trynna helping her

Accidentally she added me as an Admin of her page, instead of adding me as a jobmanager. I tried sending message to her , telling about the fact that she added me as an admin, so I sent a message to her using her page.(https://www.facebook.com/{page-username}/inbox/).

After recieving my message she changed my role permission to “Jobmanager”. Jobmanager has no access to the Page’s Inbox, But I havent refreshed the inbox page yet, So the page inbox was still in front of me , I thought of testing role permission issues there, So I tried to open the page’s inbox (https://www.facebook.com/{page-username}/inbox/) in a new tab , I got error.(that was pretty obvious as Jobmanager has no access to the page’s inbox). That inbox page was still infront of me , as I haven’t refreshed the page, I asked my friend to send a message to her facebook page, I thought maybe I can read new messages from existing inbox tab, But this also failed , “No new messages arrived”. I then tried sending message to her from the same inbox page that was still non-refreshed(I knew that, if I will refresh the page , that inbox page will no longer be available.), And Boom , I was able to send message from the existing page.

Get Devansh batham’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Note : I was not able to receive new messages , But I was able to send messages to anyone from that existing/non-refreshed inbox page with jobmanager permissions.

Diagrammatic Representation of the flow

Press enter or click to view image in full size
simple asf

I reported the issue soon after the discovery.

Sadly they marked the bug as “Duplicate”.

Press enter or click to view image in full size

Video PoC :

https://youtu.be/rztZkCVE6Rk

Takeaways :

Change the role permissions(do not refresh the existing tabs) and try to escalate previleges.
Spend time reading about “Facebook help posts” and important announcements in facebook newsroom.(expecially when it comes to these kind of bugs)
Sometimes there is no need of bypasses , (like in this case, The issue was direct).
Duplicates/Informatives are the part of the game, Keep playing :)

Timeline :

[29 may 2019] : Bug submitted

[1 june 2019] : Bug Reproduced by FB security team.

[6 june 2019] : Bug marked as Duplicate.

[15 july 2019] : Retested , Bug Fixed

wanna connect ?

Facebook : https://facebook.com/devansh.batham

Twitter : @devanshwolf
