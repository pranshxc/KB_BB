---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-04_js-file-enumeration-for-bug-bounty-hunters.md
original_filename: 2023-03-04_js-file-enumeration-for-bug-bounty-hunters.md
title: JS file enumeration for bug bounty hunters
category: documents
detected_topics:
- idor
- rate-limit
- command-injection
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- idor
- rate-limit
- command-injection
- otp
- information-disclosure
- api-security
language: en
raw_sha256: ffeca434a0d6c3b7d2ce09594386e356192b30b389931e0f64e91f8b8c32a25f
text_sha256: f2b199d5744fff7678182722c0510500be2405cc7d15afa9c51d022ff9927fe6
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# JS file enumeration for bug bounty hunters

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-04_js-file-enumeration-for-bug-bounty-hunters.md
- Source Type: markdown
- Detected Topics: idor, rate-limit, command-injection, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `ffeca434a0d6c3b7d2ce09594386e356192b30b389931e0f64e91f8b8c32a25f`
- Text SHA256: `f2b199d5744fff7678182722c0510500be2405cc7d15afa9c51d022ff9927fe6`


## Content

---
title: "JS file enumeration for bug bounty hunters"
page_title: "JS file enumeration for bug bounty hunters | ScreaMy Blog"
url: "https://screamy7.github.io/posts/Javascript/"
final_url: "https://screamy7.github.io/posts/Javascript/"
authors: ["Aadarsh Anand (@ScreamZoro)"]
bugs: ["Information disclosure", "IDOR"]
publication_date: "2023-03-04"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1428
---

### TLDR;__

  1. Importance of js files in Bug Bounty
  2. My workflow for finding js files
  3. Inspecting the files
  4. Some of my findings
  5. About new tool in progress and the following writeup

# About JS files

As a bug bounty hunter, efficiently enumerating and reading JS files is an important skill, and if you are skipping this step just because it’s a tedious process you are overlooking a vital portion of your target web application. And this may be the reason you end up finding dupes on programs. If are going through the same requests as other researchers of course you will end up dupes. So to avoid dupes you need to be different than others and put in more effort for high bounties. Personally, some of the highest bounties I have received have been from reading JS files. If you don’t know much about JS analysis read [zseano blog](https://www.bugbountyhunter.com/guides/?type=javascript_files) it talks about why to search for in JS files and then come back here.

# My workflow

Reading multiple JS files which contains thousands of JS file is tedious, it’s just like finding a needle in a haystack but the rewards are quite generous. So I will be sharing my workflow about collecting and inspecting JS files. Also if you’re a manual hacker like me then this is the preferred approach as you will significant amount of time.

Step 1 : Going through the application

Just browse through the application, and check every page within the scope. As some pages maybe be having additional JS files meant for that specific endpoint.

Step 2 : Setting the scope

Setting the correct scope is very important, as sometimes JS files maybe stored in CDNs using CloudFront,Stackpath, etc. So add the correct scope as required needed to get all the JS files used by the application.

Step 3 : Extracting JS files

I use [Uproot-js](https://github.com/0xDexter0us/uproot-JS) for extracting files. This is burp plugin that extracts and downloads all the JS files within the scope of burp history. Huge shout out to my friend [dexter0us](https://twitter.com/0xDexter0us) for making this amazing plugin.

## Going in deeper __

After this, you should be having a folder full of JS files. Now open the folder in any editor, and the files are there. I personaly use VS code as it has[beautify](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify) to beautify and it causes less strain to eyes.

After this briefly go though all the files and mark the files which are interesting and start reading. As you gain experience you will what you will understand what to look for js files. However I am sharing some common pattern which I usually look for:

`"/` , `'/`, `/api` , `https:` \- to find more endpoints.

`POST` , `GET` , `method:` \- API calls.

`params` \- parameters being used

`Content-Type` \- Content type is being set by JS,so this could endpoints as well

`keys` , `token` \- API tokens

This isn’t the same for all organizations, so it is important to learn about the targets, rather than using `Ctrl+F` on the same patterns I mentioned above.

# Some reports

Some of my highest bounties have been through JS analysis. This also lessens my chances for duplicates, as reading JS files is a gradual process and not everyone does this.

### High severity IDOR from email ???__

One morning, I was reading a JS file of a private program that had about 90k lines, I used the same workflow as I mentioned above , and found an endpoint which required the email of the user as parameter , to leak confidential data about the user. By the I reported it was already evening(JS files are tedious but rewarding)

###  Info disclosure from a hidden path __

On a different program I found`/rmt_stage` being mentioned in JS files. Words like this are hard to brute force so this is why JS files are a treasure to look through. However `subs.target.com/rmt_stage` had a blank response. After fuzzing I found an accessible CKFinder, which is a vulnerability itself as it images of financial records of the company. As I spent some more time on this, I realized that there is more to it as there is a internal proxy at ‘/rmt_stage’ which mean `sub.target.com` and `sub.target.com/rmt_stage` are two different servers. I ensured it as the `info.php` on the servers had different php versions. I ended up finding three more High bugs there , one of them included an admin panel pwn as well which is a writeup for another day. However, the program decreased the severity of them all, so I am still salty about it.

# Next write-up

There are still some things left to cover on JS analysis,like how get old JS files or how to analyze JS webpacks which will be in next blog. it will also contain detail about a new tool that I am currently working on this will further help in JS analysis. All this will be released in the next blog.
