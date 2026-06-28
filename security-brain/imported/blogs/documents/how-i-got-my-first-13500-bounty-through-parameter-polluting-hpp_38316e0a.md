---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-10_how-i-got-my-first-13500-bounty-through-parameter-polluting-hpp.md
original_filename: 2024-08-10_how-i-got-my-first-13500-bounty-through-parameter-polluting-hpp.md
title: How I got my first $13500 bounty through Parameter Polluting (HPP)
category: documents
detected_topics:
- xss
- idor
- command-injection
- file-upload
- automation-abuse
tags:
- imported
- documents
- xss
- idor
- command-injection
- file-upload
- automation-abuse
language: en
raw_sha256: 38316e0ab5fe688d767049e5dc7f3e1b990ff7e87e29e0faf0be17486d19717e
text_sha256: b5878a00c3ed30b6b7338f11fcb75e9dd6ab995183345c94740638e038192398
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# How I got my first $13500 bounty through Parameter Polluting (HPP)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-10_how-i-got-my-first-13500-bounty-through-parameter-polluting-hpp.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, file-upload, automation-abuse
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `38316e0ab5fe688d767049e5dc7f3e1b990ff7e87e29e0faf0be17486d19717e`
- Text SHA256: `b5878a00c3ed30b6b7338f11fcb75e9dd6ab995183345c94740638e038192398`


## Content

---
title: "How I got my first $13500 bounty through Parameter Polluting (HPP)"
url: "https://infosecwriteups.com/how-i-got-my-first-13500-bounty-through-parameter-polluting-hpp-179666b8e8bb"
authors: ["rAmpancist"]
bugs: ["IDOR", "XSS"]
bounty: "13,500"
publication_date: "2024-08-10"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 81
scraped_via: "browseros"
---

# How I got my first $13500 bounty through Parameter Polluting (HPP)

How I got my first $13500 bounty through Parameter Polluting (HPP)
rAmpancist
Follow
3 min read
·
Aug 10, 2024

612

3

1

Press enter or click to view image in full size
From Invicti

Hey, Its rAmpancist and I’m thrilled to have you join me for this post.

This write-up is about 2 IDORs and an XSS I found on a housing website. However what led me into these bugs is the point of this article.

The structure revolved around a main website which you had to create your account on, which had different privilege levels based on what you actually want to do, and then a second website which was a subdomain of the main website and included a sub-service which functioned getting help from main website.

In main website, you could’ve been a host or a customer. In this sub-service you could’ve used different functionalities depending on whether your main account is a host or a customer.

Press enter or click to view image in full size
Registration form

The registration form looked like something like this. You chose whether your main account is host or not, and then enter your ID, which then required the website to prompt a check to see whether ID is valid and retrieve information. Wonderfully enough though, the hosting section completely malfunctioned. Like no matter how valid your hosting ID was, the service told you its invalid or couldn’t retrieve information.

That’s when I knew, no hunter has successfully created a host account, and whatever lies behind, is mine.

The registration body looked something like this if you selected that you are a host:

IsHost=1&HostId=123&Email=test%40test.com

And this if you selected you are a customer:

IsHost=0&Email=test%40test.com

It wouldn’t supply a HostId if you selected that you’re non-host…

The way it functioned was funny :

If HostId exists and IsHost=1 -> search for hostID and fail

Get rAmpancist’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If HostId doesn’t exist and IsHost=0 -> user is customer and proceed

If HostId exists and IsHost=0 -> user is host but don’t search for hostID (!!!?)

That precisely means that it determined whether or not you are a host by checking if you supplied any HostID but processed the check only if you selected that isHost=1 , which is a flaw and lets you create invalid host accounts.

That way I unlocked 4 features and I immediately knew they have bugs.

One of them was a form submission. The form contained confidential user both inputted directly from user and retrieved from the main website (makes the information critical).

When you submitted a form you were granted a 3 character unique ID on the URL that opened your form. Easiest way possible, the ID was public and had no protection.

This is public IDOR which means 2 things:

1- You can see other people’s stuff (of course)

2- You can achieve reflected XSS if you find an XSS on the form and pass the URL to victim

Now you might ask, well were any of the inputs not properly sanitized and vulnerable? The answer is no, they were all fine.

However this is where I chain my OTHER finding! Previously I found that the field name is vulnerable to XSS, but the sad thing was that my name was entirely private and only I could see it, so self-XSS.

However now we suddenly leveraged self-XSS to a reflected one, thanks to the IDOR! Since my name gets reflected in the form and outputted in the 3 character page.

So we have 2 bugs now. Ones IDOR leading to heavy leakage (Critical, Due to information being retrieved from main website) and XSS (Medium, sadly, It was not elevate-able, trust me).

Now the last one, the form contained a file upload. The file upload itself gave you Another link to the file which was separate from main form and was vulnerable by itself, as you could’ve seen other files.

Main IDOR $12000, File IDOR $1000, XSS $500.

I hope you’ve enjoyed reading my article.
