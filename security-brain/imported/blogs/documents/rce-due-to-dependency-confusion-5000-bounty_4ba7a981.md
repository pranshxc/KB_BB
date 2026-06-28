---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-10_rce-due-to-dependency-confusion-5000-bounty_2.md
original_filename: 2023-05-10_rce-due-to-dependency-confusion-5000-bounty_2.md
title: RCE due to Dependency Confusion — $5000 bounty!
category: documents
detected_topics:
- supply-chain
- command-injection
- api-security
tags:
- imported
- documents
- supply-chain
- command-injection
- api-security
language: en
raw_sha256: 4ba7a9818eb765e410254e6fe6abf5d29a165b5dd78ff4c0cf443367dff8151a
text_sha256: 912a3b0eee8666b4cd4822a87712ea7344fceb615097f850ce1835c83fa8cf7e
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# RCE due to Dependency Confusion — $5000 bounty!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-10_rce-due-to-dependency-confusion-5000-bounty_2.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `4ba7a9818eb765e410254e6fe6abf5d29a165b5dd78ff4c0cf443367dff8151a`
- Text SHA256: `912a3b0eee8666b4cd4822a87712ea7344fceb615097f850ce1835c83fa8cf7e`


## Content

---
title: "RCE due to Dependency Confusion — $5000 bounty!"
url: "https://chevonphillip.medium.com/rce-due-to-dependency-confusion-5000-bounty-fd1b294d645f"
authors: ["Chevon Phillip (@ChevonPhillip)"]
bugs: ["Dependency confusion", "RCE"]
bounty: "5,000"
publication_date: "2023-05-10"
added_date: "2023-05-11"
source: "pentester.land/writeups.json"
original_index: 1170
scraped_via: "browseros"
---

# RCE due to Dependency Confusion — $5000 bounty!

RCE due to Dependency Confusion — $5000 bounty!
Chevon Phillip
Follow
2 min read
·
May 10, 2023

403

8

Press enter or click to view image in full size

Hey everyone! I’m back with another cool write-up about a bug bounty report I submitted to a private program on HackerOne. Guess what? I got a $5,000 reward and they took care of it in just 30 minutes!

I won’t go into the nitty-gritty of dependency confusion since there are plenty of awesome write-ups out there that cover it.

So, I was checking out this custom auth portal where you can get into multiple internal apps after logging in. Bummer, though, they didn’t give us credentials during testing, so only company employees could log in.

But hey, I didn’t give up! I looked at the .js files the app loaded, using the network tab in my browser. I saw that when the auth login page loaded, it bundled an app.[random_characters].js file.

I remembered reading about source maps and how you can put front-end source code back together with them. So, I used this cool tool called Sourcemapper (https://github.com/denandz/sourcemapper) that helps do just that.

Get Chevon Phillip’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

With the source code in hand, I started hunting for vulnerabilities. I found a few interesting ones, but what really caught my eye in the code were the import statements.

I noticed the imports referenced an NPM package that needed to be found on npm.org. So I did what any hacker would do, trying to see if I could highjack that package. To my luck, it worked!

I quickly created a PoC and started to get ping backs to my burp collaborator and was able to pull sensitive data and execute code.

Press enter or click to view image in full size

I reported this issue to the program and it was triage within 30 mins and rewarded with their max bounty.

Press enter or click to view image in full size

P.S: Special shoutout to https://twitter.com/Arl_rose for helping me get this reported right away.

END — If you want to read more of my write ups please follow me here. Twitter, and LinkedIn
