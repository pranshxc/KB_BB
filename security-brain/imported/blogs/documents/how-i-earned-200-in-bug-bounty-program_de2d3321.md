---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-09_how-i-earned-200-in-bug-bounty-program.md
original_filename: 2022-07-09_how-i-earned-200-in-bug-bounty-program.md
title: How I earned 200$ in Bug Bounty Program
category: documents
detected_topics:
- command-injection
- path-traversal
- information-disclosure
tags:
- imported
- documents
- command-injection
- path-traversal
- information-disclosure
language: en
raw_sha256: de2d3321b812711fc5a9010ebc6567bc2abac46923d7252e12dbecb1ef421d03
text_sha256: daa357e770cf14129ef3ad18dadeb1bc1f47f77fc42a676576a2366c5113d5c2
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# How I earned 200$ in Bug Bounty Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-09_how-i-earned-200-in-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, information-disclosure
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `de2d3321b812711fc5a9010ebc6567bc2abac46923d7252e12dbecb1ef421d03`
- Text SHA256: `daa357e770cf14129ef3ad18dadeb1bc1f47f77fc42a676576a2366c5113d5c2`


## Content

---
title: "How I earned 200$ in Bug Bounty Program"
url: "https://medium.com/@idan_malihi/how-i-earned-200-in-bug-bounty-program-6d7225a7ff1a"
authors: ["Idan Malihi"]
bugs: ["Information disclosure"]
bounty: "200"
publication_date: "2022-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2471
scraped_via: "browseros"
---

# How I earned 200$ in Bug Bounty Program

How I earned 200$ in Bug Bounty Program
Idan Malihi
Follow
2 min read
·
Jul 9, 2022

369

11

Hello, welcome to my new article, this article will talk about how I earned 200$ in Bug Bounty Program.
First, let me introduce my self, I am Idan and I am a penetration tester / red teamer.
Also, I am Practitioner Community Manager at CySource.

After a lot of studies and practicing on Web Applications Attacks, I started to try check some websites that related to Bug Bounty Programs.
I wanted to share with you my first bounty that I’ve got from HackerOne.

Unfortunately, the site’s company didn’t want me to publishing their name for this article. Because of this reason, I’ll call the target: “testsite” .
Let’s begin !

As everyone knows, there are a lot of testers in HackerOne platform.
Because of it, I couldn’t to find vulnerabilities on “old” websites.
I was thinking maybe the right approach for being the one of the first testers is to test the newest website that joined to the Bug Bounty Program - Well, I was right!

I’d like to mention you that the target’s site name is https://www.testsite.com
As every tester does, I checked all the functions and all the options that we have in there.
Unfortunately, I could not find anything in the main website of the company’s website.

Get Idan Malihi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I ran some sub-domain finder scripts (SubList3r for example) that helped me to find all the subdomains that related to the target.
After a lot of research, I got the target which called: “derech.testsite.com”
I noticed that this website is a little old and maybe I can find the right vulnerability!

I was checking the functions of this website until I entered to an apply form for a job in the company and I needed to upload a picture of my self (This is where I started to smell my victory).
I filled my personal information until I arrived to upload a picture, here I thought what do I need to do?
Obviously I tried to upload a php script for RCE or other vulnerabilities, I could not to find any vulnerabilities.
But I did think maybe there is more vulnerability that I didn’t try and right here I got the idea to try path traversal vulnerability.
You can read about this vulnerability right here:
https://www.acunetix.com/blog/articles/path-traversal/

So while I uploaded my picture, I captured the request and try my luck for path traversal.
As we know, we cannot put some special characters like !@#$%^&<>, After I did this, I got an error with a message of their IP smb server!

Press enter or click to view image in full size

Finally, I got my first bounty!

After I reported to HackerOne, I got a message from them that I earned 200$ from this vulnerability and the happiest thing is that the company closed this vulnerability successfully!

That’s it for this article, I hope you enjoy from reading! :)
