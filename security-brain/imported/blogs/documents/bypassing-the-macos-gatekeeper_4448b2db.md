---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-15_bypassing-the-macos-gatekeeper.md
original_filename: 2021-12-15_bypassing-the-macos-gatekeeper.md
title: Bypassing the macOS Gatekeeper
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- clickjacking
- mobile-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- clickjacking
- mobile-security
- supply-chain
language: en
raw_sha256: 4448b2dba3edc9067a68bfb7c640ff283344fbc936b352f2ca43b39dda4317bb
text_sha256: 3db5a98e0356b5930d72a5302b5e9f391f4d2ae425d3791281f5ced848a30272
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing the macOS Gatekeeper

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-15_bypassing-the-macos-gatekeeper.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, clickjacking, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `4448b2dba3edc9067a68bfb7c640ff283344fbc936b352f2ca43b39dda4317bb`
- Text SHA256: `3db5a98e0356b5930d72a5302b5e9f391f4d2ae425d3791281f5ced848a30272`


## Content

---
title: "Bypassing the macOS Gatekeeper"
url: "https://breakpoint.sh/posts/bypassing-the-macos-gatekeeper"
final_url: "https://breakpoint.sh/posts/bypassing-the-macos-gatekeeper"
authors: ["Ron Masas (@RonMasas)"]
programs: ["Apple"]
bugs: ["Local Privilege Escalation", "Gatekeeper bypass", "MacOS"]
publication_date: "2021-12-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3087
---

# [Breakpoint](/)

  * [RESEARCH](/research)
  * [ABOUT](/about)
  * [CONTACT](/cdn-cgi/l/email-protection#1472667b7939677d607154766671757f647b7d7a607860703a777b79)

# Bypassing the macOS Gatekeeper

Ron Masas

3 minute read

15 December, 2021

![](/bypassing-the-macos-gatekeeper/cover.png)

Content

1. What is the macOS GateKeeper?2. Automator3. The Bug4. Steps to reproduce

* * *

Timeline

Report sent to Apple

6 October, 2021

Apple validated the report

15 November, 2021

Apple assigns CVE-2021-30990 for this vulnerability

13 December, 2021

Apple adjudicates this issue as eligible for the Apple Security Bounty 🎉

29 January, 2022

Earlier this year I discovered the wild world of iOS and macOS security.  
One of the [OBTS](https://objectivebythesea.com/v4/index.html) conference talks just showed up on my Twitter feed, needless to say, I was hooked.

I was inspired to hunt for this bug by CVE-2021-30657 uncovered by [Cedric Owens](https://twitter.com/cedowens), and the post [All Your Macs Are Belong To Us](https://objective-see.com/blog/blog_0x64.html) by [Patrick Wardle](https://twitter.com/patrickwardle).

The majority of my career has been focusing on developing and hacking web applications, so as you could imagine I have a lot to learn. This is not going to be a super in-depth write-up, as frankly, I don't currently have the technical skill to truly produce one in a reasonable amount of time - with all of this said, let's get to it!

## What is the macOS GateKeeper?

GateKeeper is essentially a series of steps macOS enforces before running a program. The main goal of those steps is to prevent/make it harder for users to infect themselves with malware.

  1. File Quarantine - introduced in 2007, file quarantine provides a warning to the user and requires the user confirmation before execution. For example, when downloading an application from the internet.
  2. "Gatekeeper" - introduced in OSX Lion (10.7), built on top of File Quarantine, Gatekeeper checks the code signing information of downloaded items.
  3. Notarization - introduced in macOS Catalina (10.15), this step ensure that Apple has scanned and approved all software before it is allowed to run.

The bug I've found allowed me to bypass all of those steps, taking your macOS system back to 2006 😉.  
Upon clicking the downloaded application (which can be masked as an image or a pdf.) the program would immediately execute, no questions asked.

CVE-2021-30990 proof of concept video

## Automator

![](/bypassing-the-macos-gatekeeper/automator.png) Automator is your personal automation assistant for creating "automation recipes" in macOS. With Automator, users can create workflows that automate applications, execute scripts, etc. 

I've started digging into the application structure, playing with the _info.plist_ and _document.wflow_ files with no much progress.  
I was curious about the MacOs binary _Automator Application Stub_ , so I created another application and replaced it's binary with my previous application. I've run my app and it executed just fine confirming that the Automator binaries are interchangeable, they are simply executing the instructions on the _document.wflow_ file.

## The Bug

With the realization that the binaries are interchangeable, and that the code executes from the relative _document.wflow_ file, I asked myself the following question, a question that, believe it or not, helped me find dozens of bugs.

What if I put a symlink there?

Turns out the answer to this question is, the application would execute normally. **Even with the quarantine attribute, even if it's unsigned.**

This means that if an attacker would know the absolute path to a copy of the _Automator Application Stub_ binary on your system, he could craft an application that may bypass all of the Gatekeeper checks.

At this point I thought to myself, this is cool and all, but it would be awesome if a copy of _Automator Application Stub_ would be shipped with macOS at a constant path.  
A few find commands later I found that In Big Sur and Monterey, a copy of _Automator Application Stub_ binary can be found at:

`/System/Library/CoreServices/Automator Application Stub.app/Contents/MacOS/Automator Application Stub`

**Making them vulnerable by default.**

## Steps to reproduce

  1. Open Automator and build a simple _Run Shell Script_ automation.
  2. Export it as an application and run the following commands inside the `Contents/MacOS` folder of your app.

  
  
  rm "Automator Application Stub"
  ln -s "/System/Library/CoreServices/Automator Application Stub.app/Contents/MacOS/Automator Application Stub" "Automator Application Stub"
  

  3. Zip your application and your done!

## Proof of concept

You can download my proof of concept [here](/bypassing-the-macos-gatekeeper/cat.zip)

## Closing thoughts

I think this vulnerability demonstrates you don't have to be a macOS expert to find bugs. Please don't forget update your macOS systems to Monterey 12.1.

Timeline

Report sent to Apple

6 October, 2021

Apple validated the report

15 November, 2021

Apple assigns CVE-2021-30990 for this vulnerability

13 December, 2021

Apple adjudicates this issue as eligible for the Apple Security Bounty 🎉

29 January, 2022

### Open Source

  * [VooDoo](https://github.com/breakpointHQ/VOODOO)
  * [Snoop](https://github.com/breakpointHQ/snoop)
  * [Chrome Bandit](https://github.com/breakpointHQ/chrome-bandit)
  * [TCC ClickJacking](https://github.com/breakpointHQ/TCC-ClickJacking)

### Company

  * [About](/about)
  * [Github](https://github.com/breakpointHQ)
  * [Research](/research)

### Imprint

BreakPoint Technologies LTD  
Israel, HaPninim 1  
6803001 Tel Aviv-Jaffa
