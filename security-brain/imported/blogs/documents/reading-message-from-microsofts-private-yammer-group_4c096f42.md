---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-28_reading-message-from-microsofts-private-yammer-group.md
original_filename: 2022-07-28_reading-message-from-microsofts-private-yammer-group.md
title: Reading Message from Microsoft’s Private Yammer Group
category: documents
detected_topics:
- access-control
- command-injection
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- cloud-security
language: en
raw_sha256: 4c096f42fbf1dd78e464f49b418968e1866c0009157ff9ee0f28ac81804760ee
text_sha256: 8a9ec97038949e2849a51c2b36079b8ae3ed92f8d0a4313797efa82f6338edca
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Reading Message from Microsoft’s Private Yammer Group

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-28_reading-message-from-microsofts-private-yammer-group.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `4c096f42fbf1dd78e464f49b418968e1866c0009157ff9ee0f28ac81804760ee`
- Text SHA256: `8a9ec97038949e2849a51c2b36079b8ae3ed92f8d0a4313797efa82f6338edca`


## Content

---
title: "Reading Message from Microsoft’s Private Yammer Group"
url: "https://mearegtu.medium.com/reading-message-from-microsofts-private-yammer-group-6be844639bca"
authors: ["Meareg"]
programs: ["Microsoft"]
bugs: ["Broken authorization"]
publication_date: "2022-07-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2384
scraped_via: "browseros"
---

# Reading Message from Microsoft’s Private Yammer Group

Reading Message from Microsoft’s Private Yammer Group
Meareg | ማዕረግ | 𐩧𐩴oמארג | 𐩣
Follow
3 min read
·
Jul 29, 2022

18

Hi All,

I returned with another blog about a vulnerability I found in Microsoft’s business application. This time we will try to read some messages/posts from Microsoft’s private Yammer group.

To summarize, what Microsoft employees were discussing in these Yammer groups: Covid19+ Vaccine, discussion about customers, competitors & business strategies.

Technical Detail

Detection

Login to https://<x>.transform.microsoft.com/ using my testing AAD user account.

Testing Account: maotg@msobb??.onmicrosoft.com.

As you can see from the below picture, the user is not authorized to access the business transform application.

Press enter or click to view image in full size
Fig 0x00 — User is not Authorized

The permission of the user is verified from the server side by sending a ‘userwhitelist’ API call. Let’s investigate this API call’s request and respond.

GET /api/user/maotg@*.onmicrosoft.com/userwhitelist 
Host: ?*.azurewebsites.net
The user is authorized (white-listed) if the response to the above request is true.
The user is not authorized if the response to the above request is false.
Press enter or click to view image in full size
Fig 0x01 — checking user’s authorization

Obviously, the above authorization can be easily bypassed by intercepting the request and modifying the response from false to true, unless there is a verification of permission for the subsequent API calls.

Press enter or click to view image in full size
Fig 0x02 — Original Response — false
Press enter or click to view image in full size
Fig 0x03 — Edited response — changing to true

After changing the response from false to true. I was able to unlock some of the functionality of the application. One of the application’s most important features is that authorized users can access Microsoft’s Yammer Private group (group belonging to Microsoft and their business partners).

Press enter or click to view image in full size

The latest Yammer posts can be seen on the right side of the above picture. Let’s focus on the API call responsible for fetching the Yammer posts. The application invokes an API call to /api/Yammer/group/15003/feeds/5 in order to fetch the top 5 posts from Yammer group 15003.

GET /api/Yammer/group/15003/feeds/5 
Host: ?.azurewebsites.net
Authorization: Bearer eyJ…
Press enter or click to view image in full size
Figure 0x05 — Fetching top 5 feeds from group 15003

Reading More Information

Get Meareg | ማዕረግ | 𐩧𐩴oמארג | 𐩣’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The application is hardcoded only to fetch top 5 feeds from group ID 15003. I tried to fetch top 1000 feeds and check if I can disclose sensitive information.

Press enter or click to view image in full size
Figure 0x06 — More info top 1000 feed

Result

I was able to read more posts holding sensitive information but most importantly I was able to discover other Yammer group IDs. Such as — 30300774400:

GET /api/Yammer/group/30300774400/feeds/5000 
Host: ?.azurewebsites.net
Authorization: Bearer eyJ…
Press enter or click to view image in full size
Figure 0x07 — Reading feeds from a different group

Sample result of the above request in a readable form:

Press enter or click to view image in full size
Fig 0x08 — Sample confidential conversation between Microsoft employees
Press enter or click to view image in full size
Figure 0x09 —Another example

Additional example from different group — 16002774:

GET /api/Yammer/group/16002774/feeds/5000 
Host: ?.azurewebsites.net
Authorization: Bearer eyJ…
Press enter or click to view image in full size
Figure 0x10 — Reading message from group 16002774
Press enter or click to view image in full size
Fig 0x11 — Confidential information regarding Business Strategy

Report Timeline

September 10, 2021— Report to MSRC

September 13, 2021 — Triage

September 13, 2021 — Microsoft Fix the bug

July 13, 2022 — Request for disclosure & draft submitted

July 14, 2022 — Feedback from Microsoft to obfuscate a few pictures

July 26, 2022 — Approved by Microsoft for public disclosure
