---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-10_bugbounty-how-i-was-able-to-read-chat-of-users-in-an-online-travel-portal.md
original_filename: 2018-01-10_bugbounty-how-i-was-able-to-read-chat-of-users-in-an-online-travel-portal.md
title: '#BugBounty — How I was able to read chat of users in an Online travel portal'
category: documents
detected_topics:
- idor
- command-injection
- api-security
tags:
- imported
- documents
- idor
- command-injection
- api-security
language: en
raw_sha256: db15404adf7e11a4161fc727cca650b28f6cf3625e6432b3b34fc360e5e1a6ec
text_sha256: c0b7f9b2c27969c02ca49f95fe707328272419a58678f68694d47885cbe8b5e4
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — How I was able to read chat of users in an Online travel portal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-10_bugbounty-how-i-was-able-to-read-chat-of-users-in-an-online-travel-portal.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `db15404adf7e11a4161fc727cca650b28f6cf3625e6432b3b34fc360e5e1a6ec`
- Text SHA256: `c0b7f9b2c27969c02ca49f95fe707328272419a58678f68694d47885cbe8b5e4`


## Content

---
title: "#BugBounty — How I was able to read chat of users in an Online travel portal"
page_title: "#BugBounty — How I was able to read chat of users in an Indian Online travel portal | by Avinash Jain (@logicbomb) | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/bugbounty-how-i-was-able-to-read-chat-of-users-in-an-online-travel-portal-c55a1787f999"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["IDOR"]
publication_date: "2018-01-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6014
scraped_via: "browseros"
---

# #BugBounty — How I was able to read chat of users in an Online travel portal

#BugBounty — How I was able to read chat of users in an Indian Online travel portal
Avinash Jain (@logicbomb)
Follow
3 min read
·
Jan 10, 2018

443

3

Hi Guys,

While doing my usual bug hunting, I came across an interesting IDOR vulnerability that could aid me to read the complete chat of the users with the customer support team of an Online Travel company.

While browsing through a company’s website, I found an online chat forum, that allows customer to chat online with the support team to query about one’s bookings,payments, refund etc. that tricked me to extract user’s sensitive data :) . The first thing that hit my mind was “how can I read other users’ chat” and so I started the hunt. When triggering the online chat functionality, it fires up the following HTTP request —

Chat Request

and the response of the above request was the conversation messages exchanged during the chat —

Chat Response

The values marked in yellow (in chat request pic) were something which I have to play with. While traversing more,I realized that the first value i.e hari013903158 was the customer id and the second value FL-132756 comes out to be the chat id which on further analysis found to be incremental. Now I knew what to do :D .

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But there was one hurdle “How to find the valid customer id” which in this case was an 13 digit long alpha numeric id. I went back to the login page, profile section to see if it can help but nothing was helping me out. Then comes “blog section” in rescue — Traveller’s blog page where people share their traveling stories . I opened one blog to read (not for reading ;) ) which was published by one user and it was as simple as this, I could see the user id in the URL itself. Pheww! Something to cheer about! Now I copied that user id, replaced it in the “chat request” , bruteforced using burp tool for the chat id and…. still I was not able to get anything. May be that user never had an online chat with the support team. :/ . Race was still not complete so I opened 10–20 more blogs ,did the same and below is the request-response with one particular user id . ☺

Press enter or click to view image in full size
User’s Chat History

I was able to access the entire chat history of that user.

Report details -

09-Nov-2017 — Bug Reported to the concerned company.

29-Nov-2017 — Bug was marked fixed.

30- Nov-2017 — Re-tested and confirmed the fix.

21- Dec- 2017 —Awarded with reward and hall of fame .

This was all about this interesting finding. ☺

Thanks!

~Logicbomb (https://twitter.com/logicbomb_1)
