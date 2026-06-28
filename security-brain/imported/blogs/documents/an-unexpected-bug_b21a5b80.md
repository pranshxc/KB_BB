---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-31_an-unexpected-bug.md
original_filename: 2021-01-31_an-unexpected-bug.md
title: An unexpected bug
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: b21a5b8098b216538eaefb9231a2152cc615cd2e69259b8abd3af5d9b6b85c68
text_sha256: 766b1328a75338715cf6b9e4af578382ac4a2f28331043ce6c393081fdc4ca65
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# An unexpected bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-31_an-unexpected-bug.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `b21a5b8098b216538eaefb9231a2152cc615cd2e69259b8abd3af5d9b6b85c68`
- Text SHA256: `766b1328a75338715cf6b9e4af578382ac4a2f28331043ce6c393081fdc4ca65`


## Content

---
title: "An unexpected bug"
url: "https://cyberhacks200.medium.com/an-unexpected-bug-9cab5072e009"
authors: ["Nitin yadav (@Nitinydv14)"]
bugs: ["Bruteforce"]
publication_date: "2021-01-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3949
scraped_via: "browseros"
---

# An unexpected bug

An unexpected bug
Nitin yadav
Follow
4 min read
·
Jan 30, 2021

199

2

Hello everyone,

I am Nitin yadav from India with my first ever write up so please ignore my mistakes. So without wasting time lets roll to the bug and how i found it.

Press enter or click to view image in full size
Photo by Gia Oris on Unsplash

So it was my first time hunting on a live website . I was so much excited to hunt on a program lets say site.com(cant disclose as per program rules). I don't know much about the bug types and was new to it. So after 3 or 4 days my excitement turned into boredom. But then i saw a tweet about recon and searched about recon.

Then i came with a video the bug hunters methodology and after watching that i followed every steps showed in the video by 
Jason Haddix

Press enter or click to view image in full size

and got with a a subdomain terminal.epm.site.com.

At first I was like what’s this. And now am totally blank. But i wanted to find a bug so i thought to get the usernames and password for it but cant find. So I thought of password spraying attack. So first I need the internal domain name of the target. Which can be found quickly in the RDS login page source as the WorkSpaceId.

Now the challenging part was that i got the internal domain but from where do i get the user list. So for that i searched about the company on social media if i find something but it was of no use. But i thought of checking LinkedIn and found some names for the company. But the problem was that how can i get all the usernames from linkdin. Then i remembered about a blog about it and quickly cloned the tool (linkdin2usernames).

Press enter or click to view image in full size

Now for the structure that the company uses for RD web access was first_last . And the tool does not create this format and from the blog which i got to know about the tool i modified the username list with the tip given there wit sed .

$sed -i 's/\./_/g' site-first.last.txt

Now its time for some action

Press enter or click to view image in full size
Photo by Attentie Attentie on Unsplash

Setting up burp intruder for the action-

Get Nitin yadav’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

There are many ways to perform password spraying but Burp suite gives us a considerable amount of flexibility and control. So i started by capturing the login POST request and leaving a placeholder for the username and using the list which i got from Linkdin2username. I launch a attack . But wait it is important to tune this to minimize impact and load on the service.

Press enter or click to view image in full size
Launching the Password Spraying Attack

Now its the showtime. And i launched the attack. And after 2 hours i got 302 redirection. And BOOM…… Its what i was thinking about.

Press enter or click to view image in full size
Photo by Windows on Unsplash
Accessing the RDS Service with the Obtained Credentials

I accessed the RD web service using the credentials i got from password spraying attack and the user has a little access but its not what i have concern about.

Press enter or click to view image in full size

Without wasting time I reported the bug to company. And within some days i was awarded for that.

Press enter or click to view image in full size
Photo by Crawford Jolly on Unsplash
