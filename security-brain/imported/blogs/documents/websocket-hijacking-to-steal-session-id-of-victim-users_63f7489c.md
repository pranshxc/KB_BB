---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-25_websocket-hijacking-to-steal-session_id-of-victim-users_2.md
original_filename: 2021-08-25_websocket-hijacking-to-steal-session_id-of-victim-users_2.md
title: ‘Websocket Hijacking’ to steal Session_ID of victim users
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 63f7489c69be63fd3f955e6da28ce04105894f3e9a8a0f1c9b439b5e17aa19c8
text_sha256: 4c097fd62a175a2c37407d2bc6107445fb579185f946debb23db6920cdf2309f
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# ‘Websocket Hijacking’ to steal Session_ID of victim users

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-25_websocket-hijacking-to-steal-session_id-of-victim-users_2.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `63f7489c69be63fd3f955e6da28ce04105894f3e9a8a0f1c9b439b5e17aa19c8`
- Text SHA256: `4c097fd62a175a2c37407d2bc6107445fb579185f946debb23db6920cdf2309f`


## Content

---
title: "‘Websocket Hijacking’ to steal Session_ID of victim users"
url: "https://sunilyedla.medium.com/websocket-hijacking-to-steal-session-id-of-victim-users-bca84243830"
authors: ["Sunil Yedla (@sunilyedla2)"]
bugs: ["Cross-Site WebSocket Hijacking (CSWH)"]
publication_date: "2021-08-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3386
scraped_via: "browseros"
---

# ‘Websocket Hijacking’ to steal Session_ID of victim users

‘Websocket Hijacking’ to steal Session_ID of victim users
Sunil Yedla
Follow
3 min read
·
Aug 26, 2021

456

1

Hello everyone, I hope you all are healthy and safe. Today’s writeup is about one of my find in a gaming website. The interesting part here is that, I always thought this type of attack is just a theory. As always I will try to keep my writeup not soo technical so that it will be easy to understand for any beginner. Let’s start!

Before getting into the details, let’s discuss about websocket requests:

What are Websocket’s ?

Using websocket requests, it’s possible to open a two-way interactive communication session between the user’s browser and a server. With this API, you can send messages to a server and receive event-driven responses without having to poll the server for a reply. If you want to know more check this — https://sookocheff.com/post/networking/how-do-websockets-work/

Exploitation:

So I was hunting on this private Hackerone program <redacted>.com. Before start attacking, I have the habit to quickly check the website by intercepting requests in Burpsuite. During this process, I found few websocket requests carrying messages. So I started checking if it’s vulnerable to websocket hijacking or not. So for that I have used this website: http://websocket.org/echo.html [This is a vulnerable website created for connecting to websockets]. All you have to do is to enter the websocket url in location input and check if you are able to send and receive messages. I have entered the targets websocket url like this: wss://www.<redacted>.com/xns-service/secure/client/desktop/000/xxxxxxxx/websocket and immediately I got a response in 3rd party website like this

Press enter or click to view image in full size
Note: 000 — In the actual url this in alphanumeric value but I found that it is accepting any values and same goes to XXXXXX

So far good but what is the Impact? So I started exploring the website further and found that when a user updates their profile then they receive message like this which is disclosing the username of the user

So I understood that if victim is performing any action, the websocket connection established 3rd party is receiving websocket responses with sensitive content. So I went on performing sensitive actions, all actions resulted in same response. But that is when I performed password change action and then boom!! This time Session_Id disclosed : )

Press enter or click to view image in full size

What is the Impact again?

Get Sunil Yedla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So an attacker will be creating a website and host the vulnerable code. Now when the victim opens the attackers website, the connection will be established immediately and they can start seeing the websocket messages whenever the victim is performing an action. The highest impactful action is when victim is trying to update the their password, the attacker can see the Session_Id of the victims account.

To create a real life attack scenario use the code available via: http://websocket.org/echo.html , using which an attacker can acts as the 3rd party and intercept the websocket responses. So I quickly reported the vulnerability in Hackerone and the report was accepted with little less severity and less bounty due to few reasons but the identifying part made me happy since I was always thinking that this type of vulnerability is just a theory!

Press enter or click to view image in full size

Quick summary:

Found websocket requests while playing requests in Burpsuite.
Open: http://websocket.org/echo.html and check if I can send and receive websocket response
Received response from target.
Tried to escalate the severity and found that session_Id is getting disclosed to 3rd party when victim user is updating password.
To show a Real life attack scenario used the code available via: http://websocket.org/echo.html

I hope you like my explanation. If you have any queries feel free to ping me via twitter:https://twitter.com/sunilyedla2 . Stay Positive and Spread Positivity :)
