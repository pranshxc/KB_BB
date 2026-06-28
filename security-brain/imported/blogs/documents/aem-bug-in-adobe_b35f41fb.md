---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-20_aem-bug-in-adobe.md
original_filename: 2023-05-20_aem-bug-in-adobe.md
title: AEM Bug in Adobe
category: documents
detected_topics:
- command-injection
- automation-abuse
- mobile-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- mobile-security
language: en
raw_sha256: b35f41fbb8560cb2f8cd9226aa71e26e0af0822f8b025ed894c2cc19d656b34d
text_sha256: 451dde367f296aeface90d76b1d90749ddb1d7cb0cb1355c3891a01e4af12d3b
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# AEM Bug in Adobe

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-20_aem-bug-in-adobe.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `b35f41fbb8560cb2f8cd9226aa71e26e0af0822f8b025ed894c2cc19d656b34d`
- Text SHA256: `451dde367f296aeface90d76b1d90749ddb1d7cb0cb1355c3891a01e4af12d3b`


## Content

---
title: "AEM Bug in Adobe"
url: "https://realm3ter.medium.com/aem-bug-in-adobe-416763d3ad04"
authors: ["Muhammad Mater (@micro0x00)"]
programs: ["Adobe"]
bugs: ["AEM", "Missing authentication", "Security misconfiguration"]
publication_date: "2023-05-20"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1131
scraped_via: "browseros"
---

# AEM Bug in Adobe

AEM Bug in Adobe
Muhammad Mater
Follow
3 min read
·
May 21, 2023

290

2

hi hackers

When I was sleeping in bed, I got the idea to look for security vulnerabilities in Adobe Hunting them to find bugs

Adobe have a bug bounty program hosted on the HackerOne platform

let’s check it

after doing some good recon (we will discuss the process in another post here don’t worry )

I have a lot of domains and analyze the technologies used in developing target-specific web applications.

I got a lot of web technologies in Adobe

web servers

domains run by PHP , domains run by java

The technology that caught my attention is AEM (Adobe Experience Manager).

AEM stands for Adobe Experience Manager. This comprehensive content management solution enables organizations to create, manage, and deliver digital experiences across various channels, including websites, mobile apps, and forms. AEM is designed to help businesses effectively manage their digital content, streamline workflows, and personalize customer experiences.

The first thing I do before starting hunting.

I would like to understand how a web application works and what it does, and explore all its features as a regular user in the beginning to better understand its functionality and operations.

Initially, I wanted to understand how AEM works.

Adobe Experience Manager (AEM) has the following components and functionality:

Content Repository: Stores digital assets, content, and configurations using Apache Jackrabbit Oak.

OSGi Framework: Enables modular development and extensibility.

Authoring Environment: Web-based interface for content creation, editing, and workflow management.

Dispatcher: Caching and load balancing component that improves performance.

Publish Environment: Serves published content to end-users.

Integration and APIs: Integrates with Adobe Marketing Cloud solutions and offers APIs for customization and integration with external systems.

Scalability and Deployment: Supports horizontal scalability and cloud deployments for flexibility and scalability.

Get Muhammad Mater’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This architecture allows AEM to manage and deliver personalized digital experiences across multiple channels effectively.

try to run one

I found that some paths in the web application lack authentication because of a misconfiguration, allowing common users to make changes. Ideally, these edits should only be able to be made by granted administrators.

paths like these :

crx/de
crx/de/index.jsp
crx/explorer/browser/index.jsp
crx/explorer/index.jsp
crx/explorer/nodetypes/index.jsp
crx/explorer/ui/search.jsp?Path=&Query=

okay I have an idea

Let’s search for a wordlist that contains these endpoints

I found them.

AEM-List/paths at main · clarkvoss/AEM-List
Contribute to clarkvoss/AEM-List development by creating an account on GitHub.

github.com

Starting fuzzing paths and endpoints

and found paths like this

target/crx/explorer/ui/namespace_editor.jsp

Result :

Press enter or click to view image in full size

time to report

and it’s valid

Time to do automation

You can use a nuclei template to detect the AEM (CMS)

nuclei-templates/aem-cms.yaml at 36c26fc99b709f834412b976053a6f21ac7fa926 ·…
Community-curated list of templates for the nuclei engine to find security vulnerabilities. …

github.com

After detecting cms ,do fuzzing to all targets with a wordlist

And you can run a Scanners

https://github.com/0ang3el/aem-hacker

https://github.com/0ang3el/aem-rce-bundle

happy hunting
