---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-11_finding-a-p1-in-one-minute-with-shodanio-rce.md
original_filename: 2020-03-11_finding-a-p1-in-one-minute-with-shodanio-rce.md
title: Finding a P1 in one minute with Shodan.io (RCE)
category: documents
detected_topics:
- sso
- command-injection
- api-security
tags:
- imported
- documents
- sso
- command-injection
- api-security
language: en
raw_sha256: b2ae17a848cdee0b5e3cf41df55d85127bca042921a7fb0e15ee52b5b0544c34
text_sha256: f0c5dbb0b6856fbd15ed60985bd6552279683db0c2476cba3e33e6f16c5eeab9
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Finding a P1 in one minute with Shodan.io (RCE)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-11_finding-a-p1-in-one-minute-with-shodanio-rce.md
- Source Type: markdown
- Detected Topics: sso, command-injection, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `b2ae17a848cdee0b5e3cf41df55d85127bca042921a7fb0e15ee52b5b0544c34`
- Text SHA256: `f0c5dbb0b6856fbd15ed60985bd6552279683db0c2476cba3e33e6f16c5eeab9`


## Content

---
title: "Finding a P1 in one minute with Shodan.io (RCE)"
url: "https://medium.com/@sw33tlie/finding-a-p1-in-one-minute-with-shodan-io-rce-735e08123f52"
authors: ["Paolo Arnolfo (@sw33tLie)"]
bugs: ["RCE"]
publication_date: "2020-03-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4723
scraped_via: "browseros"
---

# Finding a P1 in one minute with Shodan.io (RCE)

Finding a P1 in one minute with Shodan.io (RCE)
sw33tLie
Follow
2 min read
·
Mar 11, 2020

353

2

What could possibly be better than Finding a P2 in two minutes with Shodan.io?
Easy answer: higher severity, less time!

As usual, I was looking for random servers on Shodan, owned by a company which had a bug bounty program that I was targeting.
After a while I came across a few Jenkins instances which were in-scope.
The first one was pretty boring, it seemed up-to-date and there were no public exploits that could have been useful.

The second instance, though, was much more interesting.
Although it was up-to-date as well, just like the previous one, there was a link to create new accounts in the login screen.
It looked like this:

At this point I tried to sign up and it worked flawlessly.
After logging in, I was able to see everything: usernames, build history and so on.

Get sw33tLie’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I could have reported this finding by now, but since in Jenkins there’s an easy way to run commands on the server I had to try it!
To do that, I went to jenkins-subdomain.redacted.com/script.
Here there was a console where I could write commands and execute them:

Press enter or click to view image in full size

In the picture above you can see the output of the ls command (“ls /”.execute().text), which returned as output the folders in the server’s root directory. RCE!

Lessons learned

You may be wondering how a company running a bug bounty program could let a Jenkins instance misconfigured in such a bad way.
In this case, I believe that the developer who installed Jenkins thought that running it on a non-standard port was enough to hide it from the whole internet.

Unfortunately for him, search engines like Shodan have proved that’s a faulty assumption which should never be made: security by obscurity never worked, and never will.

Thank you for reading, for more writeups and infosec-related news you can follow me on Twitter (@sw33tLie).
