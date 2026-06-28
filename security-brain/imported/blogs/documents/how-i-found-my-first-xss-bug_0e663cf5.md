---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-25_how-i-found-my-first-xss-bug.md
original_filename: 2021-11-25_how-i-found-my-first-xss-bug.md
title: How I Found My First XSS Bug
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 0e663cf53e366e629ca01c10d6e3fcfc8d9d1320d756ddc1a3d391ae2cb7e282
text_sha256: 4d4c488b574583e786b9be02adea74833c4c12ad63908ef992166efa2989bed0
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found My First XSS Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-25_how-i-found-my-first-xss-bug.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `0e663cf53e366e629ca01c10d6e3fcfc8d9d1320d756ddc1a3d391ae2cb7e282`
- Text SHA256: `4d4c488b574583e786b9be02adea74833c4c12ad63908ef992166efa2989bed0`


## Content

---
title: "How I Found My First XSS Bug"
url: "https://medium.com/@thedarkwayg/how-i-found-my-first-xss-bug-96fb8e85a24c"
authors: ["Thedarkwayg (@shadow_CLAY)"]
programs: ["Atlassian"]
bugs: ["XSS"]
bounty: "600"
publication_date: "2021-11-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3141
scraped_via: "browseros"
---

# How I Found My First XSS Bug

thanhdat1011
 highlighted

How I Found My First XSS Bug via Open Redirect
thanhdat1011
Follow
3 min read
·
Nov 24, 2021

190

1

Hi everyone,

I am @goj0s4t0ru. Today I am going to talk about the process I found my first XSS bug at @Bugcrowd.

Summary:

The story happens when I receive a private invitation for a program (Assuming: redacted.com). This program is affiliated with Atlassian and for testing on this program, I need to create a Jira cloud account.

Press enter or click to view image in full size

After logging into Google account, I will be redirected to the username creation page.

Press enter or click to view image in full size

In my head right now all I can think of is the “Open redirect” bug. I started changing the domain name, adding characters to bypass the open redirect filter, and finally I succeeded.

I immediately created a report and sent it to the Atlassian program.

Then I went to the toilet. At that moment, a thought suddenly occurred to me. Why don’t I try XSS? Without thinking about anything else, I immediately ran up to my room and turned on my computer. In the “&redirecturl=” parameter, I tried with javascript payload: javascript:prompt(1) -> set any username and Continue. Boom! XSS is executed.

Press enter or click to view image in full size
Difficult times to find ways to exploit:

But wait. It seems that the “?cloudId=” parameter corresponds to each account. This means that XSS will only be executed for me individually because the “?cloudId=” parameter is created specifically for me. So now this would be self-XSS if I couldn’t get the victim’s “?cloudId=”.

Press enter or click to view image in full size

I was a bit worried. Although this XSS search process only takes about 5 minutes, all will fail if this is just a self-XSS.

Get thanhdat1011’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I began to continue to exploit and exploit. I finally found 2 ways to get this parameter:

1. The attacker needs to join the victim's Jira team. To do this, an attacker needs to trick the victim into inviting him to join his team.

So how can an attacker not need to join the victim’s Jira group and still be able to steal “cloudId” ?

2. An attacker does not need to log in to his account nor join the victim's team. An attacker just needs to visit the victim's domain and view the "Source page". The parameter "cloudId" will appear there.
Press enter or click to view image in full size
Time to attack:

Now after stealing “cloudId” of the victim. The full link will include: https://www.atlassian.com/signup?cloudId=[victim-id]&requestId=15178645&redirecturl=javascript:prompt(1)&isPermitted=false

When the victim access -> Set user name and Continue -> XSS will be executed

Sweet fruit 😁

At the same time I have provided additional information to prove this is an Reflected-XSS bug. After that, the Atlassian team accepted and considered it a P3

Press enter or click to view image in full size
Advice:

Always stay calm and think when you spot bugs, don’t stop there. Sometimes the bugs you find are not the end result. So my advice is to always find a way to string the bugs you find. The results you get will surprise you :>

Thank you everyone for reading!!! ❤

Happy Hacking :)))

Twitter: https://twitter.com/goj0s4t0ru
