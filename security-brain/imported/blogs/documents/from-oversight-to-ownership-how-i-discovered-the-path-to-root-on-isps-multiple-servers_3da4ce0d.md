---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-19_from-oversight-to-ownership-how-i-discovered-the-path-to-root-on-isps-multiple-s.md
original_filename: 2023-09-19_from-oversight-to-ownership-how-i-discovered-the-path-to-root-on-isps-multiple-s.md
title: 'From Oversight to Ownership: How I Discovered the Path to Root on ISP’s Multiple
  Servers'
category: documents
detected_topics:
- sqli
- sso
- access-control
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- sqli
- sso
- access-control
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 3da4ce0d4ecace56d72c5c42c62593d18a9408d04d0eadb180e4bd57961ca1f2
text_sha256: d45e368a9f8a71e95294ec0fd15d053da650b1e95cb702f2a257bb01464ba7a5
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# From Oversight to Ownership: How I Discovered the Path to Root on ISP’s Multiple Servers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-19_from-oversight-to-ownership-how-i-discovered-the-path-to-root-on-isps-multiple-s.md
- Source Type: markdown
- Detected Topics: sqli, sso, access-control, xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `3da4ce0d4ecace56d72c5c42c62593d18a9408d04d0eadb180e4bd57961ca1f2`
- Text SHA256: `d45e368a9f8a71e95294ec0fd15d053da650b1e95cb702f2a257bb01464ba7a5`


## Content

---
title: "From Oversight to Ownership: How I Discovered the Path to Root on ISP’s Multiple Servers"
url: "https://medium.com/@hektoravdyli12/from-oversight-to-ownership-how-i-discovered-the-path-to-root-on-isps-multiple-servers-6f14fb55b4f"
authors: ["Hektor"]
bugs: ["Information disclosure", "File disclosure"]
publication_date: "2023-09-19"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 762
scraped_via: "browseros"
---

# From Oversight to Ownership: How I Discovered the Path to Root on ISP’s Multiple Servers

From Oversight to Ownership: How I Discovered the Path to Root on ISP’s Multiple Servers
Hektor
Follow
3 min read
·
Sep 19, 2023

7

Hey, I’m Hektor Avdyli, a security researcher with a passion for uncovering security flaws. In this post, I’ll be sharing a unique experience where I gained control of an Internet Service Provider (ISP) through black-box testing. To maintain confidentiality, I’ll be using pseudonyms and fictional IPs. Join me as I break down the steps.

I would like to clarify that I had explicit authorization from the ISP’s chief to conduct the security testing discussed in this article.

Environment

As mentioned previously this test was conducted in a black-box manner, meaning I had no insider knowledge of the ISP’s infrastructure, network architecture, or system configurations. My sole point of entry was the public-facing website hosted on example.com (do consider im using example.com and it’s IPs to maintain discretion and protect the involved parties).

Fictional Domain: example.com

Fictional Ip: 93.184.216.34

Identifying the Misconfiguration

As usual my next step was to dive headfirst into the web of example.com.

I went through a thorough process of looking for potential vulnerabilities. This involved using various tools and techniques, both automated and manual.

During my investigation, I did find a few outdated libraries within the website. However, after a closer look, I realized that these issues, although important to address for security reasons, didn’t give me the kind of access I needed to the ISP’s servers. It was a bit of a setback, there i drew blank i didn’t know where to look or what to look, took little break and went back, then it hit me he mentioned an “ISP Management Panel”. Started again to look on my scans but nothing that had to do with the Panel, thought that it might not be hosted at example.com, still there were no subdomains of that kind.

At this point i thought this it, just few out-dated libraries, Blind-XSS and info.php leaked.

Get Hektor’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As i was Google Dorking i stumbled upon IP addresses on ipinfo.io, I realized I could dig deeper. I thought that finding out which devices were currently online in a group of IP addresses could give me more information about the Control Panel. So, I used a tool “Angry IP Scanner” to do just that.

Angry IP Scanner is a handy utility designed for network discovery. It allows you to scan IP address ranges to identify active hosts and open ports. In my case, it became a valuable tool to uncover live hosts within the IP ranges I encountered on ipinfo.io.

I set the range from 93.184.216.0 to 93.184.216.255

Active IP addresses

I went with the port 80, where i finally found the Control Panel hosted at the 93.184.216.253, with much excitement started again testing manually and automated.

Not update since 2021 multiple blind sqli, xss, Auth Bypass.

First thought that this may not still be in use since, then used gobuster, found an interesting /backups directory, fascinating i found there the /backups.sh and /program.sh. After downloading the files i found the root:password at the backups.sh file and boom im in! full root user not just at the 93.184.216.253 Control Panel, but the password was used in multiple other servers(example.com,isp servers etc) , had full access at the mysql (databases,client_tables, encrypted_passwords, etc)

Press enter or click to view image in full size
The root ssh connection to the ISP server

With this final run i stopped the test and started writing the report immediately.

I assessed the weaknesses as high-risk, indicating a significant potential impact on security. Which included: Information Leak, Out-dated (Software, OS, Libraries), SQLI, XSS.

Thank you for joining me on this journey. Let’s continue to explore, learn, and grow in the ever-evolving realm of cybersecurity.
