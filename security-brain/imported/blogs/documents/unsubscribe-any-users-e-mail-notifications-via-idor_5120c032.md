---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-28_unsubscribe-any-users-e-mail-notifications-via-idor.md
original_filename: 2022-08-28_unsubscribe-any-users-e-mail-notifications-via-idor.md
title: Unsubscribe any user’s e-mail notifications via IDOR
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: 5120c032fa7a892c7f7e917481660bb9076df963dcdd0e1006b0b945f00cf9df
text_sha256: ecd1333b0402ba48e4f6fb17b076b1f1e0986cc52d628cd7ce1621d36830f2a1
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Unsubscribe any user’s e-mail notifications via IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-28_unsubscribe-any-users-e-mail-notifications-via-idor.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `5120c032fa7a892c7f7e917481660bb9076df963dcdd0e1006b0b945f00cf9df`
- Text SHA256: `ecd1333b0402ba48e4f6fb17b076b1f1e0986cc52d628cd7ce1621d36830f2a1`


## Content

---
title: "Unsubscribe any user’s e-mail notifications via IDOR"
url: "https://sagarsajeev.medium.com/unsubscribe-any-users-e-mail-notifications-via-idor-2c2e05b79dac"
authors: ["Sagar Sajeev (@Sagar__Sajeev)"]
bugs: ["IDOR"]
bounty: "200"
publication_date: "2022-08-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2251
scraped_via: "browseros"
---

# Unsubscribe any user’s e-mail notifications via IDOR

Unsubscribe any user’s e-mail notifications via IDOR
Sagar Sajeev
Follow
3 min read
·
Aug 28, 2022

508

5

Hello fellow Hackers. I’m Sagar Sajeev

In this writeup, I would like to share how I was able to unsubscribe any user from the Target website’s email notification service.

Get Sagar Sajeev’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This was possible because the unsubscribe feature (which is often found near the footer of the mail) was vulnerable to IDOR.

Such options are often available at the footer section of every mail.
The unsubscribe link looked something like this:

https://target.com/unsubscribe?u=9x0xxx98xx5cxx5xx71&id=123456

?u = Lol it was just the timestamp encoded in base64. Not sure what’s the use of this parameter, maybe for logging the time at which this action was initiated. But manipulating this param didn’t seem to have any significant impact. But the presence of this param was necessary in the req or else status code 400 was returned.
?id = The user ID. It was easy to get the user ID as there was an API call which was leaking the User ID. All I had to do was visit the target user’s profile and the API leaked the User ID. (I chained it with this vuln and reported it.)
The modified link looked something like this:-

https://target.com/unsubscribe?u=9x0xxx98xx5cxx5xx71&id=654321

Modify the Id parameter to the Victim UserID and forward the req. The user is unsubscribed from the website’s email notification service.

Tips:-

To increase the severity of the vuln in your report, make sure you try to find a way to get the UserID’s of other users. Or else they will either close the report or you’ll be rewarded with low bounties.
Also, don’t blindly report a vuln as soon as you find one. I’ve noticed this habit among many beginner hunters. Guys, trust me I have been through that phase. At the time when I started, I too have reported many low hanging vulns which I could have escalated the severity to gain more bounties.
Maybe give it another try to somehow find a way to escalate the severity. Who knows maybe you’ll be rewarded with a higher bounty.

Timeline

Submitted : 18–08–2022

Accepted : 22–08–2022

Rewarded with joy and happiness : 😄

The company was a non-profit organization that ran an Old Age home. They did offer me $200. But I felt like accepting the bounty was not the right thing to do here.

Press enter or click to view image in full size

I do occasionally share some tips about Bug Bounties and related stuff over at my Twitter and LinkedIn handle. So do follow me there. If you’ve got any queries, feel free to message me. I will be more than happy to help.

LinkedIn : https://www.linkedin.com/in/sagar-sajeev/

Twitter : https://twitter.com/Sagar__Sajeev

Thanks for going through my writeup and I hope it was useful to you. I’ve made many other writeups on my Medium handle. Please do check those out as well.

Happy Hunting!
