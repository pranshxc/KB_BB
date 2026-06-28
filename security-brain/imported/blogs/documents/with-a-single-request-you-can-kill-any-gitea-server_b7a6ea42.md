---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-22_with-a-single-request-you-can-kill-any-gitea-server.md
original_filename: 2023-02-22_with-a-single-request-you-can-kill-any-gitea-server.md
title: With a single request, you can kill any Gitea server
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: b7a6ea4252307370104519cec56ccd50c13b38f78413783b19ba0bb4b588edc1
text_sha256: 4da46aa3c605c3eb56602b5b519556d3d5b7273885b4d4490a5c7b6988465689
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# With a single request, you can kill any Gitea server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-22_with-a-single-request-you-can-kill-any-gitea-server.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `b7a6ea4252307370104519cec56ccd50c13b38f78413783b19ba0bb4b588edc1`
- Text SHA256: `4da46aa3c605c3eb56602b5b519556d3d5b7273885b4d4490a5c7b6988465689`


## Content

---
title: "With a single request, you can kill any Gitea server"
url: "https://medium.com/@knassar702/with-a-single-request-you-can-kill-any-gitea-server-1275c5f3b226"
authors: ["Khaled Nassar (@knassar702)"]
programs: ["Gitea"]
bugs: ["Application-level DoS"]
publication_date: "2023-02-22"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1494
scraped_via: "browseros"
---

# With a single request, you can kill any Gitea server

With a single request, you can kill any Gitea server
MindPatch
Follow
3 min read
·
Feb 22, 2023

52

in this blog I’m going to tell you how I was able to kill/dos any Gitea server I discovered this bug in Gitea version 1.14.2 in 2021

which was fixed in 1.14.3 by the Gitea team
Please note that I wasn’t targeting Gitea at all, I was doing some bug bounty hunting on a private target That target’s staging-dev.target.com has gitea on it

and I thought, “Okay, I think there’s CVES for that product”
and yeah I found some but Unfortunately, the POC isn’t included in the CVE report (only the PR on github)

so I decided to play around and see if there’s any private keys in the repos on this gitea server (I didn’t find any)

and my mind give me an idea, what If I created an account on this server? I thought I could find out more because maybe there’s an option that lets the user make the repositories private for people with an account on Gitea

After creating my account, I didn’t see any difference so the last option I have is to send emojis to Gitea’s issues page for trolling or joking

Then I opened Zaproxy and sent many of these emojis to the issues body API in one request Afterwards, I noticed that subdomain response time is going up I got a 500 error, and boom, the server wasn’t responding when I try to visit the gitea issue that I opened

When I reported this bug to my target’s security team, the response was too fast, saying “Sorry, this is not a part of our products. Could you please forward this report to the Gitea security team” But what’s good is they provide me with more info to make a good report for the Gitea security team like logs, screenshots of CPU usage, etc.

Press enter or click to view image in full size

When someone visits my gitea issue containing the emojis, the CPU usage gets high. That’s because there’s too much text formatting/processing happening in the back-end for the comment After I reported the bug to Gitea, they asked me some questions about the environment and if I could reproduce it at the last version (it’s on try.gitea.io)

Get MindPatch’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I’ve included it in the report

Gitea version : 1.14.2
Git version: 2.32.0
Operating system: Linux
Database: MySQL
Can you reproduce the bug at https://try.gitea.io: Yes (https://try.gitea.io/dtestman/test/issues/1)

They respond after 2 days with validating the bug and a PR, and my name is on the release page for my next release

Press enter or click to view image in full size

here’s the release page: https://blog.gitea.io/2021/06/gitea-1.14.3-is-released/

and the fix PR: go-gitea/gitea#16185

See you

https://media.tenor.com/b8DvJ53k8soAAAAd/rat-bye.gif
