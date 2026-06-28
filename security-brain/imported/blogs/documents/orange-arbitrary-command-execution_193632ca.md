---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-29_orange-arbitrary-command-execution.md
original_filename: 2022-09-29_orange-arbitrary-command-execution.md
title: Orange Arbitrary Command Execution
category: documents
detected_topics:
- command-injection
- rate-limit
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- rate-limit
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 193632ca3fe182f8825ecee3825927f7cb78eba158bfa59b2a86763c3ccefb7a
text_sha256: 2b76f3a80c4f01793e06a330f7ed83b7d7d7b7615f90675801a12046e921ac49
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Orange Arbitrary Command Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-29_orange-arbitrary-command-execution.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `193632ca3fe182f8825ecee3825927f7cb78eba158bfa59b2a86763c3ccefb7a`
- Text SHA256: `2b76f3a80c4f01793e06a330f7ed83b7d7d7b7615f90675801a12046e921ac49`


## Content

---
title: "Orange Arbitrary Command Execution"
url: "https://omar0x01.medium.com/orange-arbitrary-command-execution-75ba7f283d53"
authors: ["Omar Hashem (@OmarHashem666)"]
programs: ["Orange"]
bugs: ["RCE", "Docker daemon misconfiguration", "Missing authentication"]
publication_date: "2022-09-29"
added_date: "2022-10-02"
source: "pentester.land/writeups.json"
original_index: 2100
scraped_via: "browseros"
---

# Orange Arbitrary Command Execution

Orange Arbitrary Command Execution
Omar Hashem
Follow
4 min read
·
Sep 30, 2022

580

4

Hi everybody Omar Hashem is here, I will share with you how I was able to achieve more than 10 RCE in different companies using the same technique in this write-up.

If you don’t know Orange, in short, it is a multinational telecommunications company with 266 million customers around the world

Now we can start

I started doing some external network scan

Nmap scan:

nmap -A -p0–65535 77.pool85–54–17.dynamic.orange.es

That was the output:

Press enter or click to view image in full size

I found that there are some interesting ports are disclosed publicly that most of the time are used as API internally like 2375 for docker and 3306 for MySQL services

I started testing the Mysql service aspiring to get access to the database so I started with some common misconfiguration like accessing the database with no password (Null Root Password)

┌──(omar㉿kali)-[~]
└─$ mysql -h 77.pool85–54–17.dynamic.orange.es -u root -P 3306

But unfortunately didn’t work

Brute Spray:

It’s a tool used to brute force network services with a common username and password

After the first try failed so i started to use brutespray but after i edited the Custom Wordlist by adding (Mysql better default pass list) from SecList

┌──(omar㉿kali)-[~]
└─$ brutespray — file nmap-output.xml — service mysql — threads 5

But i got nothing too

I started after that to search for common exploits on google and using searchspolit for the version of MySQL and some of the used plugins for MySQL like “mysql_native_password” to get any sort of Authentication bypass

Press enter or click to view image in full size

Searching for an exploit that may contain the plugin or the MySQL version

┌──(omar㉿kali)-[~]
└─$ searchsploit ‘mysql’|egrep ‘native|pass|auth|5.5’

Press enter or click to view image in full size

There is no public exploit for the plugin “mysql_native_password” but there are two interesting exploits for the MySQL service[The second exploit (Auth bypass) and the third exploit (RCE) ]

So i tried both of them but I got nothing too

After that, I started to get look at the docker engine

Get Omar Hashem’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But before that let’s understand

what is docker:

Docker is an open source software platform to create, deploy and manage virtualized application containers on a common operating system (OS)

simply it’s commonly used between developers and DevOps to solve problems that were face developers like might their application code work on machine and not working on other machines [according to missing packages and libraries], Docker was designed to fix this problem

let’s take a look on nmap output

Press enter or click to view image in full size
Exposed Docker API:

When you install docker on a system it will expose an API on your local host located on port 2375. This API can be used to interact with the docker engine which basically gives you the right to do anything you desire unauthenticated. Under these conditions no external party will be able to access your docker API as it isn’t exposed to the world [public internet]. However, in certain instances this API can be changed so that it can be accessed by external resources. If done improperly this will expose the docker API to the world [public internet]

So we need right now to test this misconfiguration of exposing docker API without any type of authentication

Now let’s get the running containers list

ps:allow us to list running containers

docker -H <host>:<port> ps

┌──(omar㉿kali)-[~]
└─$ docker -H 77.pool85–54–17.dynamic.orange.es:2375 ps

Press enter or click to view image in full size

It worked and found that there is 7 containers run there

Now we gonna try to get a shell

exec:allow us to run a command in a running container

Docker -H <host>:<port> exec -it <container name> <command>

┌──(omar㉿kali)-[~]
└─$ Docker -H 77.pool85–54–17.dynamic.orange.es:2375 exec -it ‘limpid_agelast’ /bin/bash

Press enter or click to view image in full size

We got a shell to the container with root privileges and that wasn’t the end as i was able to comprise the other containers with source code and other private data to the company

Hope you guys enjoyed the write-up

Don’t forget to follow on Twitter

Twitter: @OmarHashem666

Stay in touch

Linkedin | Youtube | Twitter

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
