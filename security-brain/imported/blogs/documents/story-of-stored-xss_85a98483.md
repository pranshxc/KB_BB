---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-28_story-of-stored-xss.md
original_filename: 2018-11-28_story-of-stored-xss.md
title: Story of Stored Xss
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 85a98483b974fc76170ffe970132ee478b5d4573f1ad25eea6c2837218505a31
text_sha256: 5b086cae662e2a85ae6bcc55156983d8d2636d50452882c97027a9563ef1c883
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Story of Stored Xss

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-28_story-of-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `85a98483b974fc76170ffe970132ee478b5d4573f1ad25eea6c2837218505a31`
- Text SHA256: `5b086cae662e2a85ae6bcc55156983d8d2636d50452882c97027a9563ef1c883`


## Content

---
title: "Story of Stored Xss"
url: "https://medium.com/@hossainwalid93/story-of-store-xss-d24c3ab862f0"
authors: ["Walid Hossain (@NoobWalid)"]
bugs: ["XSS"]
publication_date: "2018-11-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5556
scraped_via: "browseros"
---

# Story of Stored Xss

Story of Stored Xss
Walid Hossain
Follow
2 min read
·
Nov 29, 2018

27

1

Hi guys!!

Walid Hossain a bug hunter and web penetration tester from Bangladesh.This is my first write up to the medium community!I am sharing a write up about one of my recent finding(stored xss).

So when the Stored Xss occurs???

@@Stored XSS occurs when a web application gathers input from a user which might be malicious, and then stores that input in a data store for later use. The input that is stored is not correctly filtered.

Someday ago on twitter I read about a tip about xss !!That is : always put something before the xss payloads. Like TEST”><svg onload=alert(1)// And when you start finding for The TEST word.the xss should be fired( if not properly filtered).And I was like-

I was like

That time I was looking to a private site.And thought why not give it a try???So I started looking into this!!lets say the web app name redacted.com

Get Walid Hossain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I have created two accounts on redacted.com. while doing that I have set the display name as TEST”><svg onload=alert(1)// and created account. Now what??? I have started typing the name on search bar and BOOM! xss fired up !! I was really surprised that the input was not filtered and tip worked as Hell!Again I was like

Surprised!

Then honestly I did not think much and reported the issue to the private program!After two days they replied and marked it as wont fix saying self xss because victim could not find attackers name on the search bar thus victim only can attack himself.As I did not thought much about the issue.I was like:

Then I thought about how we can attack victim with this???I tried to understand the functionality of the redacted.com.And after spending a day I understood that

If user1 is following user2 then user2 will appear on user1s search bar
if user1 is not following user2 then will not appear!

And I have set the attack scenario like this:

Attacker set his display name as Attacker1"><svg onload=alert(1)//
Now Attacker1 is following victim1
Victim1 got interested and also followed Attacker1
Victim1 wanna see Attacker1 profile.So he start typing on Attacker1 on search bar
BOOM! XSS should be pop out in victims browser!!

And I have submitted with all of this.after someday one of the analyst traiged my report saying Thank you for a detailed POC N00B-Walid.I was like:

So thats the story of stored xss.Please pardon my any mistake as this is my first write up!And I am no one comparing any of the guys out there.thank you!

Issue found: 15 november

Submitted : 15 november

Marked wont fix: 21 november

traiged: 25 november

bounty awarded:26 november

Best regards,NOOB-Walid
