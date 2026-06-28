---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-11_story-of-my-biggest-bounty-ever-command-execution-on-jenkins.md
original_filename: 2019-07-11_story-of-my-biggest-bounty-ever-command-execution-on-jenkins.md
title: 'Story of my Biggest Bounty ever : Command Execution on Jenkins'
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 1105ecce5953a0f7dbd4079ae3eff4283da238ca255f1af1a67b3c5d027389eb
text_sha256: 095bde682d16b15816d2353fca7a76775b0ccc676c1fd2a4d4d4b22c22d073d0
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Story of my Biggest Bounty ever : Command Execution on Jenkins

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-11_story-of-my-biggest-bounty-ever-command-execution-on-jenkins.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `1105ecce5953a0f7dbd4079ae3eff4283da238ca255f1af1a67b3c5d027389eb`
- Text SHA256: `095bde682d16b15816d2353fca7a76775b0ccc676c1fd2a4d4d4b22c22d073d0`


## Content

---
title: "Story of my Biggest Bounty ever : Command Execution on Jenkins"
url: "https://medium.com/@janijay007/story-of-my-biggest-bounty-evecommand-execution-on-jenkin-a73f5242b1e2"
authors: ["Jay Jani (@JayJani007)"]
bugs: ["RCE", "Exposed Jenkins instance"]
bounty: "8,000"
publication_date: "2019-07-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5157
scraped_via: "browseros"
---

# Story of my Biggest Bounty ever : Command Execution on Jenkins

Story of my Biggest Bounty ever : Command Execution on Jenkin
Jay Jani
Follow
3 min read
·
Jul 11, 2019

315

5

Hello friends,

Today I wanna talk about one of my recent finding on HackerOne’s private program. It was a simple RCE on publicly accessible Jenkin. So let’s get started.

Get Jay Jani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was invited to hunt a private program on HackerOne which had the large scope as *.program.com. I started with basic recon and I got some IPs on which Jenkin instance was available using a script. All thanks to Armaan Pathan (SuperMan :D) for this awesome script

Press enter or click to view image in full size

I browsed the IP and It had publicly available sign up functionality. So i registered myself as their user and my account got successfully activated.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Next thing was to check /script (script console which allows to execute our command) was enabled or having any authentication. But I was not lucky this time :/ I got some weird error while executing “/etc/passwd” in script console.

Press enter or click to view image in full size

But wait a min, I had “manage jenkins” option available :) Without wasting time, I just installed “Terminal” plugin to Jenkins which is basically allows to execute OS command.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

All was good and I got the terminal plugin installed through which I can execute commands.

Press enter or click to view image in full size

I got RCE :D

Press enter or click to view image in full size

The bounty amount was a bit high (even I was also shocked) as that was their main domain IP.

Press enter or click to view image in full size

Reference:
#BugBounty — From finding Jenkins instance to Command Execution.Secure your Jenkins Instance! by Avinash Jain

Shodan + Jenkins to get RCEs on Servers by Uranium238
