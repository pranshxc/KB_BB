---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-27_the-untold-sendbird-misconfigurations.md
original_filename: 2022-11-27_the-untold-sendbird-misconfigurations.md
title: The Untold SendBird Misconfigurations
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 6f87020de11ecbb73bbee3597500894006356b13584a3d42a6ca338c1529412d
text_sha256: d162ac0525e024b7fa1cd4a0aed823733fc1dc95fca22a398efd673d23190d96
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# The Untold SendBird Misconfigurations

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-27_the-untold-sendbird-misconfigurations.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `6f87020de11ecbb73bbee3597500894006356b13584a3d42a6ca338c1529412d`
- Text SHA256: `d162ac0525e024b7fa1cd4a0aed823733fc1dc95fca22a398efd673d23190d96`


## Content

---
title: "The Untold SendBird Misconfigurations"
url: "https://ltidi.medium.com/the-untold-sendbird-misconfigurations-1496d252bc69"
authors: ["LTiDi (@dunglt140150)", "Thái Vũ (@thaivd98)", "LamScun (@LamScun)", "fergus (@fergustr4n)", "thefool45"]
programs: ["SendBird"]
bugs: ["Broken Access Control"]
publication_date: "2022-11-27"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 1847
scraped_via: "browseros"
---

# The Untold SendBird Misconfigurations

The Untold SendBird Misconfigurations
LTiDi
Follow
6 min read
·
Nov 28, 2022

211

Press enter or click to view image in full size

At a random bug hunting collaboration with my team (thaivu, lamscun, thefool45, fergustr4n), we had bumped into a random private target as usual. On the way exploiting the target, I found that our target has implemented a chatting feature using a service from a third party platform. After doing some google dork, I found that the chatting feature of our target is a product of SendBird — “the leading interaction API platform trusted by modern digital apps like Paypal, Yahoo, Reddit, Delivery Hero, and Hinge to easily embed real-time chat, voice, and video into their apps”. It’s catched my interest and I decided to research more on how it work to see if there would be any hidden actions I could do or hidden configurations that developers might miss…

1st — Learn the third party’s products and documents

I went straight to the SendBird Main Site to know what I would face with. The SendBird Developer Portal provides for developers a very clear and useful documents for each type of products (usage guides, sample APIs, Notes, Recommendations,…).

There are a few interesting notes at the time I started my research (Some might be outdated when you read this blog):

The host of the Customer’s SendBird Application would be in form of “https://api-{application_id}.sendbird.com”
Sendbird provides various access control options and some are turned on by default to avoid unexpected errors when creating sample apps.
Customers cannot changing Access Control List setting by themselves. Changing ACL setting only possible by a member of Sendbird’s Solutions Engineering team.
By default, SendBird Application Security Settings for “users without access tokens” are “Read & Write” — chat and “Call & Answer” — call.
2nd — Understand functions, verify the knowledge and find out the vulnerabilities

After having an overview about how SendBird works, I got back to my targets to use, play around the functions to verify with what I’d read above. I confirmed that there were APIs with the host as the same pattern as “api-{application_id}.sendbird.com” and with paths as the same as I’d seen in the documents. Then, I quickly used the current API session to try different APIs in the API documents. Randomly, I picked an API that list users in the SendBird Application “GET /v3/users/” and surprisingly, the server responded back with all the users listed !!! Jumping for joy, I told all my teammates to check on it.

We tried and knew that our users’ session could call various APIs and done lots of actions on users, channels, messages, … within the SendBird Application of our targets. It was definitely a big broken access control because of ACLs misconfiguration !!!

However, there was one thing that we could not understand that where did the “Session-Key” come from and how was it generated since we could not see the “Session-Key” value in any responses ?

Back to SendBird Documents to read more and do more, we knew some more things:

“By default, Sendbird server can authenticate a user just by a unique user ID”
“If no matching user ID is found, the server creates a new user account with the user ID”
“A user authentication can be done with just their own user ID, but also with either an access token or a session token”
Our target as ClientApp could have authenticated to SendBird Server via WebSocket with the Upgrade WebSocket URL format as: “wss://ws-{application_id}.sendbird.com/?user_id={user_id}&ai={application_id}&access_token={access_token}”

Finally, we confirmed that:

The SendBird Client of our target authenticated to SendBird server via WebSocket.
The “Session-Key” would be sent to client via WebSocket Message after the client call Upgrade WebSocket URL as above
The SendBird Client of our target could authenticate by only user ID with the “access_token=null”
We also found a hidden API to authenticate via USER ID only as the WebSocket way in JS file: “POST https://api-{application_id}.sendbird.com/v3/users/{user_id}/login — body: {“app_id”:”<application_id>”}”

In summary, in the target above, as unauthenticated user, we could create a SendBird Client User ourselves, authenticate successfully and call APIs to abuse the broken access control because of ACLs misconfiguration.

3rd — How to perform massive check vulnerabilities on other SendBird Intances in different targets
We have to confirm that our targets implementing SendBird in their applications by crawling, perform content discovery on the targets and grep for “sendbird” word and the regex of SendBird’s Application ID “[0–9A-F]{8}-[0–9A-F]{4}-[0–9A-F]{4}-[0–9A-F]{4}-[0–9A-F]{12}”
After having confirmed the targets implementing SendBird and get the SendBird Application ID, we check whether SendBird Application Security Settings for “users without access tokens” are misconfigured or not by performing anonymous user login/creation using following ways:
wss://ws-{application_id}.sendbird.com/?user_id={user_id}&ai={application_id}&access_token={access_token}
POST https://api-{application_id}.sendbird.com/v3/users/{user_id}/login — body: {“app_id”:”<application_id>”}

3. If the step above were success, we will get the “Session-Key” for our user session. Now, we check whether the ACLs are misconfigured or not by sequently calling all the APIs to perform actions on the SendBird Application using the SDK User Session that we got.

Get LTiDi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4. If the step number 2 were not success, we will manually go through functions on the target, get the SDK User Session by the normal way that the target do and check for the ACLs misconfiguration as the step 3.

5. Automation them all !

References for SendBird APIs to check:

https://www.postman.com/sendbird/workspace/sendbird-platform-api/overview
https://sendbird.com/docs
4th — Bird Hunting

After having checked the vulnerabilities on different SendBird Applications, most of them are vulnerable to the ACLs misconfiguration. However, base on different applications with different business requirements and impacts, the severity must be considered different as well (from Medium — Critical).

The impacts are varied:

Leak Users Sensitive Information
Create a chat channel (without create a new league)
Manage the chat channel
Update the user’s chat profile
Update the group channel configuration
Chatting with any users
An attacker could edit/delete messages of any users while being operator role of the self created channel.
An attacker could update the details, configurations of the channel while being the member of any channels.
As documented, a single SendBird User could only join a limit of 2000 group channels, the attacker could create 2000 group channels and add all the users in the SendBird Application to those channels. As a result, all the users could not join any SendBird channels after that, which could cause Denial of Service.
…

Some example reports:

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Great collaborations with thaivu, lamscun, thefool45, fergustr4n $$$$

### Updates from SendBird

SendBird has more documents about security recommendations, especially about the ACLs.
SendBird now allows their customers to change the ACLs by themselves.

However, the ACLs and the SendBird Application Security Settings for “users without access tokens”are still vulnerable by default !!!

THANKS FOR READING! HAPPY HACKING, LEARNING, HUNTING AND KEEPING BIRDS SAFE!
