---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-25_rocketchat-monitor-user-messages.md
original_filename: 2021-11-25_rocketchat-monitor-user-messages.md
title: RocketChat - Monitor User Messages
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
raw_sha256: eb9c9eded989e009a866ba493a2dfac8c0558b809f7bd5bb3a473bdaf107e0e7
text_sha256: 26367a0b2d49fdae3c2d9d7de2b680a93d12b8fc9609d307b6d3bab9228b7527
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# RocketChat - Monitor User Messages

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-25_rocketchat-monitor-user-messages.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `eb9c9eded989e009a866ba493a2dfac8c0558b809f7bd5bb3a473bdaf107e0e7`
- Text SHA256: `26367a0b2d49fdae3c2d9d7de2b680a93d12b8fc9609d307b6d3bab9228b7527`


## Content

---
title: "RocketChat - Monitor User Messages"
page_title: "Rocket.Chat - Security Issue - Monitor Messages of Users — Securify"
url: "https://securifyinc.com/disclosures/rocketchat-monitor-messages"
final_url: "https://securifyinc.com/disclosures/rocketchat-monitor-messages"
authors: ["Rojan Rijal (@uraniumhacker)"]
programs: ["Rocket.Chat"]
bugs: ["Broken authorization"]
publication_date: "2021-11-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3140
---

# RocketChat - Monitor User Messages

Nov 25

Written By [Rojan Rijal](/disclosures?author=603dc78c54d7950fdae7af75)

### Background

During a recent engagement, a client was using an updated version of Rocket.Chat with registration disabled. Since services like Rocket.Chat, Slack etc may contain internal and sensitive information, I wanted to see if I could find a way into the service or get a unauthenticated read access to some of the channels and messages. In the end, I identified a way to read last messages of any rooms without any authentication. This could then be leveraged with a script to monitor messages sent to the channel. 

## Vulnerability

### What are rooms (rid)

In Rocket.Chat, rooms are ways you can communicate with other users. Some examples are: channels, direct messages, and group messages. **_rid_** s are unique IDs that help identify these rooms. While they are unique, some of them are easy to guess: 

  * #general channel’s Room ID is **GENERAL**

  *  _rids_ for direct messages are concatenation of the user’s IDs. For example, a _rid_ for private message could be UserA’s ID + UserB’s ID. 

When messages are returned, the ID of the user who sent it is also returned. This makes it easier to identify all potential direct messages between users. 

### Vulnerable Function

Similar to my last vulnerability, I wanted to identify vulnerable **methods**(functions that could be called via Meteor.call) that had no authentication checks. In Rocket.Chat most of the authenticated checks in methods are done by a simple check. 

> 
>  const user = Meteor.user() as IUser | undefined;
>  if (!user) {
>  throw new Meteor.Error('error-invalid-user', 'Invalid user', { method: 'sendFileMessage' } as any);
>  }

In the snippet above, the code checks if user ID is undefined. An undefined or null user ID indicates that the request is unauthenticated and it returns _error-invalid-user_. 

While going through these methods, _canAccessRoom_ method stood out. 

![](https://images.squarespace-cdn.com/content/v1/603dc7d9cd5ee7681ca00145/1634146619396-F6BNEFA55M8CPUHD5ARD/Screen+Shot+2021-10-13+at+10.35.39+AM.png)

User ID validation

This specific method took two parameters: **_rid_** and **_userID_**. The userID passed into the function is provided by the user rather than through the Meteor.user() session controller. Once called, the function checked if the userID was null or undefined. After the validation, it would then pull the user information. 

![](https://images.squarespace-cdn.com/content/v1/603dc7d9cd5ee7681ca00145/1634146917424-MAEFD2ZV3WOTTSS3G97F/Screen+Shot+2021-10-13+at+10.40.36+AM.png)

Room and Access validation

Next, the room validation is done by checking:

  * If given rid is null/undefined

  * If the rid is not null, get the room information via _findOneByID_

  * canAccessRoom authorization check is called

The functionality did not check to see if the current user had the right to query the message of another user (admin, or the user themselves). As a result, it was possible to call _canAccessRoom_ with a userID and a _rid_ to view the last message. There are couple ways you can retrieve the User IDs without authentication so this was not a blocker either.

After finding this vulnerability, I signed up on open.rocket.chat with two different user accounts and created dummy/flag messages. After that, I called the function with authentication and confirmed this worked on the latest version deployed to Rocket.Chat community as well. 

![](https://images.squarespace-cdn.com/content/v1/603dc7d9cd5ee7681ca00145/1634147729319-4JJANJAH5UFBCYJVSZ1F/Screen+Shot+2021-10-13+at+10.54.24+AM.png)

### Exploit

The exploit for this is now available at <https://github.com/bugbounty-site/exploits/blob/master/rocketchat/rocketchat-monitor.py>

### Report Timeline

  * **September 24, 2021** \- Reported to Rocket.Chat security

  * **September 30, 2021** \- Vulnerability confirmed by Rocket.Chat security

  * **November 05, 2021** \- Vulnerability fixed as part of 4.1.1 update

  * November 25, 2021 - Vulnerability disclosed here  

[rocketchat](/disclosures/tag/rocketchat)[sev:critical](/disclosures/tag/sev%3Acritical)[exploits](/disclosures/tag/exploits)

[ Rojan Rijal ](/disclosures?author=603dc78c54d7950fdae7af75)
