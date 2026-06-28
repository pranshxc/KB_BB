---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-27_from-hunting-for-a-laptop-to-hunting-down-remote-code-execution.md
original_filename: 2018-12-27_from-hunting-for-a-laptop-to-hunting-down-remote-code-execution.md
title: From Hunting for a Laptop to Hunting down Remote Code Execution
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 4488441bdfeccf3e709a7a1a15a4b9b4c65fa3d020db73dede56de99fdba5683
text_sha256: b448685dbed6b30b05a23084e5c23be3f0e232ec3b97b0d6488461349fb1cc8b
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# From Hunting for a Laptop to Hunting down Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-27_from-hunting-for-a-laptop-to-hunting-down-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `4488441bdfeccf3e709a7a1a15a4b9b4c65fa3d020db73dede56de99fdba5683`
- Text SHA256: `b448685dbed6b30b05a23084e5c23be3f0e232ec3b97b0d6488461349fb1cc8b`


## Content

---
title: "From Hunting for a Laptop to Hunting down Remote Code Execution"
url: "https://medium.com/@aniltom/from-hunting-for-a-laptop-to-hunting-down-remote-code-execution-72cce2761846"
authors: ["Anil Tom (mr_4nk)"]
programs: ["Asus"]
bugs: ["RCE", "WebDAV"]
publication_date: "2018-12-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5503
scraped_via: "browseros"
---

# From Hunting for a Laptop to Hunting down Remote Code Execution

From Hunting for a Laptop to Hunting down Remote Code Execution
Anil Tom
Follow
4 min read
·
Dec 27, 2018

350

3

Hello guys, this is Anil back with another write-up on my bug hunting adventures. This time I helped out Asus. :)

It was another ordinary day that I came home from office and was chatting with my roommates, when one of my friends called up and told he wanted to buy a new laptop and needed some suggestions. So I went online and began hunting for laptops that met his requirements. I was reading about one of the Asus RoG models, when suddenly the Bug Hunter in me woke up and I asked myself why I shouldn’t Recon the Asus website.

So I began my recon of the website, and spent a whole night looking for a bug on their main domain and did not find anything…

The next day morning I went to my office, but my mind was still on the Asus bug hunt. That evening I got a notification on my mobile that there was an update for the Termux app. And suddenly my Bug Hunter senses tingled, and I thought, “Why don’t you run a sublister against asus.com on the mobile?”

Press enter or click to view image in full size

I randomly selected one of Asus’ sub-domains, specifically http://stw.asus.com/ and was greeted by this page

Press enter or click to view image in full size

After seeing this page I felt confident that they were running Microsoft server. It was 5.30 then, so I shutdown my PC and went back to home. Once there, I took my laptop and opened the website. Recalling that a few days prior one of my 1337 friend Rahul had told me about the WEBDAV REMOTE CODE EXECUTION Bug, I decided to check for it.

Aside, What is WEBDAV?

Web Distributed Authoring and Versioning ( WebDAV ) is an extension of the Hypertext Transfer Protocol (HTTP) that allows clients to perform remote Web content authoring operations. WebDAV is defined in RFC 4918 by one of the Internet Engineering Task Force group

Get Anil Tom’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I began to check whether WebDAV was enabled. and tried to Add a network location from my laptop to the website

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Now usually when I trying connecting to something that I don’t have access to, it always shows an irritating pop-up, like this one:

Press enter or click to view image in full size

But when I tried it with http://stw.asus.com/ it proceeded to the next step:

Press enter or click to view image in full size

Yes! It connected, and at that time I was like

I completed the addition of the network location, opened the folder, created a new file and saved it:

Press enter or click to view image in full size

Then I opened that file in the web browser and saw this:

Press enter or click to view image in full size

At that time I was like:

Following this, I made a PoC video and reported it to the Asus team.

Timeline

May 02 Reported the Issue

May 03 Initial Reply

May 07 Fixed and HOF approved for May 2018

Jun 02 Listed in HOF
