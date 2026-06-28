---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-04_how-i-discovered-authentication-bypass-that-blocks-users-from-accessing-the-webs.md
original_filename: 2024-07-04_how-i-discovered-authentication-bypass-that-blocks-users-from-accessing-the-webs.md
title: How I Discovered Authentication Bypass That Blocks Users from Accessing the
  Website ?
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
raw_sha256: d0c4a8c0c89843698f7bf90efda376066ce1779506761deffff8f4b3669d2796
text_sha256: a873f3cc63c3d8b791c41383a9336b6b21063298d60fb8792d0bbdffee157272
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# How I Discovered Authentication Bypass That Blocks Users from Accessing the Website ?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-04_how-i-discovered-authentication-bypass-that-blocks-users-from-accessing-the-webs.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `d0c4a8c0c89843698f7bf90efda376066ce1779506761deffff8f4b3669d2796`
- Text SHA256: `a873f3cc63c3d8b791c41383a9336b6b21063298d60fb8792d0bbdffee157272`


## Content

---
title: "How I Discovered Authentication Bypass That Blocks Users from Accessing the Website ?"
page_title: "How I Got $$$ From Privilege Escalation That Ban Users From The Website? | by Mohamed Sayed | Medium"
url: "https://sayedv2.medium.com/how-i-discovered-authentication-bypass-that-blocks-users-from-accessing-the-website-93140fa180ac"
authors: ["Mohamed Sayed (@Sayed_v2)"]
bugs: ["Application-level DoS", "Privilege escalation"]
publication_date: "2024-07-04"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 192
scraped_via: "browseros"
---

# How I Discovered Authentication Bypass That Blocks Users from Accessing the Website ?

Top highlight

How I Got $$$ From Privilege Escalation That Ban Users From The Website?
Mohamed Sayed
Follow
3 min read
·
Jul 4, 2024

431

5

Hi amazing hackers ,

Today we gonna talk about authentication bypass vulnerability that i found in a public bug bounty program .

Press enter or click to view image in full size
Let’s start our story

I started hunting on the program and I spent about 3 days to understand it.

The program allows you to create an organization and invite users with different roles

now the organization contains :

Owner → User 1

Admin → User 2

Member → User 3

There is an option for the owner to create a new role so he created a new role called “Test” and gave it to user 3

Press enter or click to view image in full size

User 2 (Admin) also can reach the role section but he cannot delete the roles .

So first thing came to my mind , what if i tried to delete the new role that the Owner gave to User 3 ??

Lets try ..

I went to the role section with User 2 and pressed on the new role and sent the request to repeater

So i tried to delete the role by replacing the GET with DELETE

but i couldn’t , because the system doesn’t allow to delete a role if a user still have it ..

Press enter or click to view image in full size

I spent a lot of time trying to delete it , but i failed .

Get Mohamed Sayed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I saw in the response that the system allow using some different methods in the request

So I said what if i tried to send different method then use DELETE again??

lets try…

I tried all the methods but it didn’t work with me .

But , When I sent PATCH in the request i got information about the role in the response .

Press enter or click to view image in full size

So lets try to delete it after the PATCH request.

lets use DELETE again and send the request ….

BOOOOOM….

I got ( 204 no content ) response and the role has been deleted…

Now lets see what happened to User 3 when i deleted his role ..

I went to user 3 account and refreshed the page and guess what ??

Press enter or click to view image in full size

He can’t even access the website or anything again , he will get error page every time he tries to access the website

Timeline

27 Jun 2024 → reported

2 July 2024 → awarded $$$

Follow me on:

twitter / linkedin
