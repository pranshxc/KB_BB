---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-21_peeping-through-a-web-socket.md
original_filename: 2021-11-21_peeping-through-a-web-socket.md
title: Peeping through a Web-Socket
category: documents
detected_topics:
- command-injection
- automation-abuse
- csrf
tags:
- imported
- documents
- command-injection
- automation-abuse
- csrf
language: en
raw_sha256: de5f3e7093198de05ddb2d12789b6b379c98e7b6f128d608363ca9398889949a
text_sha256: 3177b0f638d483577a47e407089edcfaa1d05ec4992b580aec352162a30a96c0
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Peeping through a Web-Socket

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-21_peeping-through-a-web-socket.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `de5f3e7093198de05ddb2d12789b6b379c98e7b6f128d608363ca9398889949a`
- Text SHA256: `3177b0f638d483577a47e407089edcfaa1d05ec4992b580aec352162a30a96c0`


## Content

---
title: "Peeping through a Web-Socket"
url: "https://cirius.medium.com/peeping-through-a-web-socket-936ed55a2c31"
authors: ["Aditya Verma (@0cirius0)"]
bugs: ["Cross-Site Websocket Hijacking (CSWH)"]
publication_date: "2021-11-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3152
scraped_via: "browseros"
---

# Peeping through a Web-Socket

Peeping through a Web-Socket
Aditya Verma
Follow
3 min read
·
Nov 20, 2021

9

Recently, I had found a bug related to web sockets through which I was able to view all the messages being sent to the victim user.

What are Web Sockets?

Web Socket is an advanced medium of communicating through a web server. It is a two-way communication channel, i.e. once a connection is established then both server and browser can send data to each other persistently.

Web Sockets are usually used in chatting applications, stock/crypto market applications to make sure the data is updated in real time.

What is Web Socket Hijacking?

I would recommend reading the Portswigger Academy’s article on Cross-site Web Socket Hijacking which explains the attack. In short, it is a type of CSRF attack in which rather than a HTTP Request, an attacker sends a request to the server to establish a Web Socket connection on behalf of the victim using his cookies with which he can send and recieve data from the server on behalf of the victim user.

Here it goes

I was exploring the target web application and found a chat feature, which was using the web sockets to send and recieve messages.

The upgrade request that was being made to intialize a web socket connection was way too open as it didn’t even send the user cookies to identify the user, instead it sent a unique identifier of the user to establish a web socket connection.

Some Recon

In the Burp Suite, there is a separate tab for web sockets which show the traffic that is flowing on web socket connection.

Get Aditya Verma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finding the unique identifier was easy enough as we just had to send a message to the victim user using our account, intercept the web socket request in burpsuite and extract the victim identifier from the request.

Further analyzing the request being made to the web socket conenction and the response recieved, I was able to identify few commands that need to be sent to the server after the connection is established to start receiving new messages being sent to the victim user from other users.

Summing it all up

I used Burpsuite repeater to make a new web socket request to the same endpoint but with the victim identfier. It looked similar to the image below.

Press enter or click to view image in full size

Once the connection got established in the repeater tab, now I was able to send the commands to the server(similar to portswigger lab’s “READY” command).

Press enter or click to view image in full size

Once, this was all done, I just had to wait for someone to send a message to the user(or send a message with my account to the victim user). Every message being sent to the victim user along with the link to the attachments sent along the message were visible in the repeater tab. The server kept sending all the messages of the user as this connection was not meant to be expired automatically.

This way I was able to view the messages of all the users without any action requirement by the victim user. Just establish the web socket connections and then wait and watch the messages of the users as they flow through.

Follow me on Twitter to get some interseting tweets/retweets.
