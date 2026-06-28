---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-16_how-i-earned-9000-with-privilege-escalations.md
original_filename: 2022-02-16_how-i-earned-9000-with-privilege-escalations.md
title: How I earned $9000 with Privilege escalations
category: documents
detected_topics:
- access-control
- sso
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- sso
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 2506e5f7965eb44c50518bbad15834cdedb7932cabe0887896fc551abc08321c
text_sha256: 59c0237102e919d5940613373f1dc973ecfce5af4a6f34215e19e73018a59466
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# How I earned $9000 with Privilege escalations

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-16_how-i-earned-9000-with-privilege-escalations.md
- Source Type: markdown
- Detected Topics: access-control, sso, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `2506e5f7965eb44c50518bbad15834cdedb7932cabe0887896fc551abc08321c`
- Text SHA256: `59c0237102e919d5940613373f1dc973ecfce5af4a6f34215e19e73018a59466`


## Content

---
title: "How I earned $9000 with Privilege escalations"
url: "https://junoonbro.medium.com/how-i-earned-9000-with-privilege-escalations-b187d1f8f4fe"
authors: ["Junaid Khan (@JunoonBro)"]
bugs: ["Privilege escalation"]
bounty: "9,000"
publication_date: "2022-02-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2898
scraped_via: "browseros"
---

# How I earned $9000 with Privilege escalations

Top highlight

How I earned $9000 with Privilege escalations
JunoonBro
Follow
4 min read
·
Feb 16, 2022

1.1K

11

Press enter or click to view image in full size
Some of my bounties

Hello Community, It’s my very first time that I am sharing my experience and knowledge with you guys and I hope it will add some values to your Bug Bounty journey. Please don’t mind any mistake as I am sharing for the first time ❤

Who I am?

My name is Junaid Khan aka JunoonBro, Founder & Acting CEO of Security Foster. I started my Bug Bounty Journey in 2020 and received my first bounty at 14 Jan 2020. I mainly focus on Data Leakage & Access Control because it give me some different crazy feelings and confidence on work. I do Bug Bounty as a Part Time hobby now as I am having a Cyber Security Solution startup here in my country PAKISTAN ❤

What is Privilege escalations?

Its simple mean breaking logic of the application and getting illicit access of raised freedoms, or honors, past what is planned or entitled for a utilization.

How I was able to Find Privilege escalations?

Methodology One

So lets consider that target name site.com. The main aim of the site.com was to fast the process of Video Editing with team collaboration. site.com has multiple roles in the project like Owner, Team Member, Collaborator etc where Owner is a Super Admin & Collaborator is simple user with limited access in the project.

I created two accounts, One for Owner where i created a Project and invite collaborator in the project which was my second account.

Now listen, Owner is able to create Private Folder, Private File, Review Link & Presentation in the project which is not accessible to collaborator.

So, there was a search bar in the project for both Owner and Collaborator as you can see below;

Press enter or click to view image in full size
Search bar

I fired up a Burp Proxy and randomly type “abcdef” and capture the request for further inspection. Below is the captured request.

Press enter or click to view image in full size
Vulnerable Request

On proceeding the request, I got 200 OK only, After playing and inspecting the request a lot, I came across to a very crazy bypass which were leaking Owner Private Information & Invite Links for Reviews & Project

Get JunoonBro’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The q parameter in the request is responsible for taking the search query and when I removed the search query from the q parameter and proceed the request so It leak me all the Owner Metadata and Invite Links as you can see below

Press enter or click to view image in full size
Request
Response (Owner data leaking)

This approach is always my favorite, Where you don’t need or have to look for ID’s or UUID’s of Victim or Target and bounty for this was mentioned in the next image.

Press enter or click to view image in full size
Bounty Recived

There were two more endpoints which were associated with Search request and both of them were vulnerable with same issue but DATA were different but sensitive as same.

2. Methodology Two

Now let’s come to the second part of hunting, I have gathered all the endpoints of Owner which were restricted to Collaborator by using Owner site of the project.

Now, it’s time to try each and single request with Collaborator account but wait, there is something which is very important to understand in this case. Every project is having a unique UUID and this unique were same for every participant in the project either it is Owner, Team Member and Collaborator.

So, Now there is no tension for UUID, We have to just use restricted endpoints from collaborator request or account and you will not believe, There were multiple endpoints which were leaking sensitive Data to collaborator, as you can see below

Press enter or click to view image in full size
Bounties ❤
Press enter or click to view image in full size
Bounties ❤
Press enter or click to view image in full size
Bounties ❤

For finding more endpoints, You have to always look for JS Files, Try to understand the pattern and you will for sure find more and more endpoints.

CONCLUSION

This writ-up is not for showing my BOUNTIES, It’s for pushing your limits and thinking out of box. There are multiple ways to break the Mechanism but it all required your creativity and passion for the work. I user very few tools and i don’t use every tool without proper understanding and I don’t want to run in the race blindly.

I must say Thank You to my brother 
Bilal Khan
 for being nice and supportive mentor in this journey ❤

I hope this blog post will give some value addition to your Bug Bounty Journey. You can follow me for more on Twitter and LinkedIn at JunoonBro
