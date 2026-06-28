---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-13_turning-self-xss-to-good-xss-via-access-control.md
original_filename: 2019-01-13_turning-self-xss-to-good-xss-via-access-control.md
title: Turning Self XSS to good XSS via access control
category: documents
detected_topics:
- access-control
- xss
- command-injection
tags:
- imported
- documents
- access-control
- xss
- command-injection
language: en
raw_sha256: 7f61d8478ea4a0483c9cb41df4d0c4c98ef75b62ff816d713015f19745892e88
text_sha256: adb70716a1ec937f88a41d3bda8c34c37baa7062bc1029e66841d776f99e87d0
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Turning Self XSS to good XSS via access control

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-13_turning-self-xss-to-good-xss-via-access-control.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `7f61d8478ea4a0483c9cb41df4d0c4c98ef75b62ff816d713015f19745892e88`
- Text SHA256: `adb70716a1ec937f88a41d3bda8c34c37baa7062bc1029e66841d776f99e87d0`


## Content

---
title: "Turning Self XSS to good XSS via access control"
page_title: "TURNING SELF XSS TO GOOD XSS VIA ACCESS CONTROL | Hacklad’s Blog"
url: "https://hacklad.github.io/blog/2019/01/13/Xss-it.html"
final_url: "https://hacklad.github.io/blog/2019/01/13/Xss-it.html"
authors: ["Yusuf Yazir (@Hacklad)"]
bugs: ["Stored XSS", "Self-XSS"]
publication_date: "2019-01-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5478
---

# TURNING SELF XSS TO GOOD XSS VIA ACCESS CONTROL

Jan 13, 2019 

![xss](/images/xss.png)

I will be covering a story of a bug I found in a private program as a result of improper access control. Access control is how a web application grant access to content and functions to some users and not other(OWASP). However, an organisation staff with no write permission(can’t perform any worthwhile action) was able to maliciouly run javascript code which could be used to XSS the owner of the organisation! Surreal, isn’t it?. Reading your mind, I guess you are asking _“How?”_

![forreal](/images/forreal.jpg)

Hi, I am Yusuf Yazir. Follow me as I take you through this short and pleasant journey.

## INTRODUCTION:

For the sake of privacy, let’s call this website example.com. On example.com, whenever the owner of the organisation registers, he gets a subdomain similar to the name of his organisation. For example, Org name is Hacklad, we will get Hacklad.example.com. Hacklad! Nice name, isn’t it? :) Thanks Thanks. However, the owner could add admins, manager, staff etc.

Role | Permission  
---|---  
Owner | Read, Write, edit settings  
Admin | Read and write only  
Staff | Read only  
Browser | Role  
---|---  
Chrome | Owner  
Firefox | Admin  
Firefox | Staff  
  
## SELF XSS (OWNER)

On the owner account, like most people will do, I added my XSS payload `<img src=x onerror=alert(1)>` when creating a project in the _project name_ field. XSS popped, I smiled, grabbed a cup of water. Logged In quickly into the Admin browser(Firefox), Guess what? NO XSS on the Admin page.. Whoops, I couldn’t cry! Yes, I couldn’t!

I tried creating project with Admin so that I can XSS the owner but sadly there were no features like that for the admin account. I felt bad and disappointed, My hopes were shattered!!! Needed Motivation to continue!…

## INSPIRATION:

Normally when I am in a situation like this, I go checkup some of my chats with Elite Hackers on Twitter just to get myself up and running again. I was scrolling through Nahamsec’s Chat and I saw this… Whooot?

![Nahamsec](/images/nahamsec.png)

## Access Control:

I took enough time to understand the flow of the application. Then I started creating another project with the owner, on landing on the create project page I noticed the url `https://hacklad.example.com/add/new/project`. My mind told me, “copy that url into the staff browser” I immediately changed my browser to the staff browser, and I tried accessing this URL(`https://hacklad.example.com/add/new/project`) directly and suprisingly I saw a staff with no write could actually create project.. How?? Who cares!..

## STORED XSS:

I added my XSS payload `<img src=z onerror=alert(9)>` in the project field and NO XSS again! Another Heartbreak! It is time to give up having in mind to submit a low severity permission issue(staff without write permission could create project). I closed the staff browser and I was about closing the Owner’s browser, I decided to reload and on doing that, I saw 9, oh Yes. XSS POPPED!

I raised a ticket immediately. The vulnerability was fixed and Bounty awarded few days later.

The Org Owner’s payload led to self xss(culd only xss himslef) but as a result of broken access control, a staff without write permission was able to create a project with a XSS payload, eventually affecting the owner of the organisation. Isn’t it a cool story? Cheers.

## TAKEAWAY:

  1. A user without write permission was table to XSS the owner of the Organisation, always take that into consideration.
  2. Try the imposssible, that’s the only way amazing things happen.
  3. Be with people better than you and you’d be suprised how well you will improve with time.
  4. Few things we can do with the xss is to “change the staff to an owner. Assuming the owner can promote other people to owner. In that case, it becomes organization takeover because you can promote yourself to owner.” - Sugessted by Justin Gardner

Thanks for reading!

Shotout to my friends [Stefano](https://twitter.com/stefanohablando), [Justin Gardner](https://twitter.com/Rhynorater) and [Sawzeey](https://twitter.com/_sawzeeyy) for their support!

[](/blog/2019/01/13/Xss-it.html)
