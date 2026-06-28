---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-25_using-dark-web-in-bug-bounty.md
original_filename: 2023-06-25_using-dark-web-in-bug-bounty.md
title: Using Dark Web in Bug Bounty
category: documents
detected_topics:
- automation-abuse
- sso
- command-injection
tags:
- imported
- documents
- automation-abuse
- sso
- command-injection
language: en
raw_sha256: b35f81c10a0c250478ee42bf964ccf46012526ef2d9291386138b4ba1091de6c
text_sha256: b0d2c7f7617591c6a5a453af7d0e1f6e8c5f8a8adc73b0f7f9d377a89625f0a4
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Using Dark Web in Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-25_using-dark-web-in-bug-bounty.md
- Source Type: markdown
- Detected Topics: automation-abuse, sso, command-injection
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `b35f81c10a0c250478ee42bf964ccf46012526ef2d9291386138b4ba1091de6c`
- Text SHA256: `b0d2c7f7617591c6a5a453af7d0e1f6e8c5f8a8adc73b0f7f9d377a89625f0a4`


## Content

---
title: "Using Dark Web in Bug Bounty"
url: "https://realm3ter.medium.com/using-dark-web-in-bug-bounty-3a9530fd454c"
authors: ["Muhammad Mater (@micro0x00)"]
bugs: ["Credential stuffing"]
publication_date: "2023-06-25"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1011
scraped_via: "browseros"
---

# Using Dark Web in Bug Bounty

Top highlight

Using Dark Web in Bug Bounty
Muhammad Mater
Follow
5 min read
·
Jun 25, 2023

763

8

Hi Hackers,

como estas?

Press enter or click to view image in full size

In this article, I’ll talk about some findings and bugs that I’ve reported recently by using CTI and Dark web

At first, I like to say that I love cybersecurity in every detail.

Offensive & Defensive

I like to understand most security tracks, whether offensive or defensive, there are always some cross-skills that can be used for both defensive and offensive paths, like OSINT.

I learned Osint two years ago and became addicted to it

I loved to follow the threats that occurred and the breaches that occurred.

And I discovered that there is a cybersecurity path for these things called CTI OR Cyber threat intelligence

CTI refers to the knowledge and information about potential or ongoing cyber threats, including the tactics, techniques, and procedures (TTPs) used by threat actors. It involves collecting, analyzing, and disseminating actionable intelligence to organizations, enabling them to understand and mitigate risks posed by cyber threats.

CTI got me into the world of the Dark Web

The dark web is a part of the internet that is intentionally hidden and accessible only through specific software, such as Tor. It is often associated with illegal activities, including the sale of stolen data, hacking tools, drugs, counterfeit goods, and various other illicit services.

The relationship between cyber threat intelligence and the dark web lies in the fact that the dark web is a common platform for threat actors to exchange information, tools, and services related to cyber threats. It serves as a marketplace for cybercriminals, where they can buy and sell valuable data, exploit kits, zero-day vulnerabilities, Data Base, and other resources that can be used in cyber attacks.

I wanted to know how this data was stolen and keep myself up-to-date with

The new threats and attack vectors are analysed to understand how they target the victim.

I’m starting to understand that there’s some kind of malware called an info stealer

info stealer malware is a type of malicious software designed to infiltrate a victim’s system and steal sensitive information.

It can capture data through methods such as keylogging, screen capturing, clipboard monitoring, form grabbing, and memory scraping.

Info stealers are typically distributed through malicious email attachments, compromised websites, or as payloads delivered by other malware.

In Bug Bounty Many tools like Cracked Burp suite is an infostealer malware

Press enter or click to view image in full size

These Data belong to bug hunters hh

Hackers have been hacked

These stolen data are sold on the dark web or dark forums AND some telegram channels

I started to learn how I collect and monitor this data From The Dark web By Making Bot get data from Telegram channels and underground hacking forums and parsing the logs to search by the domain of the target

So I decided to use these data in bug bounty Because I’m a Bug hunter.

at first, I tried this on vdp programs

So I started to target the emails of the company employees by a punch of search engines such as https://hunter.io/search/

get all emails for company employees

Get Muhammad Mater’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then, I searched for any leaks for this Company or any old breach to the company,

Press enter or click to view image in full size

And Get leaked data from the dark web.

Ok How?

To monitor the dark web:

Utilize dark web search engines like Grams, Torch, or Ahmia to find websites and hacking forums.

Leverage specialized dark web monitoring tools such as DarkOwl, Flashpoint, or Recorded Future to automate monitoring and analyze content.

There are paid products that offer this service
You can search the hacking forums as I did and used more than one forum to collect data from many resources like me (Telgram, Hackingfourms, Data Breaches)

Exercise caution when joining dark web forums and communities, ensuring to prioritize legal and ethical practices and avoiding engagement in illegal activities or accessing illegal content.

check if any email in leaked or not , after get data with credentials

The next step is searching for any login portal using Dorks

site:target.com inurl:"login"

and tools such as https://github.com/Mr-Robert0/Logsensor ,

logsensor searches about any login panels of the target.

I tried to log in with almost all login panels and portals even the mail portal panel.

Press enter or click to view image in full size

Again and Again

Press enter or click to view image in full size
And Finally, I hacked an employee
Press enter or click to view image in full size

Another scenario that happened I reached the company’s admin panel with one of the credentials.

There are some important tips to be mentioned :

1- not all programs will accept this as a bug, some of them will consider it as an NA or informative so make sure to understand the program policy.

2- most of the triage team if they find out that the data is vailed will ask for additional information to know the source of this information and how you got it:

Can you please provide additional details such as what method of OSINT did you use to identify this finding and what OSINT tool you used? Also, can you please provide steps to reproduce? “ here you will just explain the whole process.

3- try to get the impact of the data don’t just report them.

I want to make a note:

I explained the idea to you and told you how to exploit it and get bounty from it

I did not publish names for hacking forums because this information can be misused away from bug Bounty or black hat activity

Thanks

My Linkedin : https://www.linkedin.com/in/micro0x00/

My Twitter : https://twitter.com/micro0x00

Support me :

https://www.buymeacoffee.com/Micro0x00
