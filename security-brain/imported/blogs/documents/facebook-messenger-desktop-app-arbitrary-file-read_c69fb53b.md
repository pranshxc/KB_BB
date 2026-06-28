---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-04_facebook-messenger-desktop-app-arbitrary-file-read.md
original_filename: 2021-02-04_facebook-messenger-desktop-app-arbitrary-file-read.md
title: Facebook Messenger Desktop App Arbitrary File Read
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: c69fb53bb3538d7747b69d5943c20462a489fbc439d6b5a231bfaaa377ecfa31
text_sha256: 0f1a91ffbc3a31e280b15801bdb23fc496924792169513eecf053f303c526d93
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Messenger Desktop App Arbitrary File Read

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-04_facebook-messenger-desktop-app-arbitrary-file-read.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `c69fb53bb3538d7747b69d5943c20462a489fbc439d6b5a231bfaaa377ecfa31`
- Text SHA256: `0f1a91ffbc3a31e280b15801bdb23fc496924792169513eecf053f303c526d93`


## Content

---
title: "Facebook Messenger Desktop App Arbitrary File Read"
url: "https://medium.com/@renwa/facebook-messenger-desktop-app-arbitrary-file-read-db2374550f6d"
authors: ["Renwa (@RenwaX23)"]
programs: ["Meta / Facebook"]
bugs: ["Arbitrary file read"]
bounty: "2,000"
publication_date: "2021-02-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3934
scraped_via: "browseros"
---

# Facebook Messenger Desktop App Arbitrary File Read

Facebook Messenger Desktop App Arbitrary File Read
Renwa
Follow
2 min read
·
Feb 3, 2021

171

I’m a daily user of Facebook Messenger on Mobile and Web, someday i got a banner in my Web version saying that Messenger is available on Desktop too.

I downloaded the App and started to play with it, with first impressions i knew it’s using Electron using asar i decompiled the application and started to look at it, most of user inputs where safe and couldn’t find any XSS

Sending links to someone would open external browser and there wasn’t any way to XSS or opening an HTML file

Playing with functionalities i noticed something, when going to Message Requests then opening Spam/Filtered Messages it would open a new window and needed to re-authenticate by clicking Continue.

In that new window Spam messages or messages that user don’t want to see will be moved to there

Using another account i sent a URL and moved it to Spam section then when i clicked the link it opened a new Electron window not external browser, now we have a controlled window that we can execute any code we want

Going back to the source code and checking options nodeIntegration and contextIsolation was set to false that mean we can’t directly access node JS functions and get full RCE but with contextIsolation set to false there is possibility to override preload.js internal functions and get code execution

I couldn’t find a good method to override so went to look other options, with both our saviors isn’t available i had to find something new and that is <webview> :)

webviewTag was set to true in the application that means we can use <webview> tag not very much different from <iframe> but with some greater functionalities.

webview can load internal files using file:// uri, so <webview src=”file:///etc/passwd”></webview> will display contents of passwd file inside the page

Get Renwa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

One of the best functions <webview>.executeJavaScript(code) when the webview loads we can execute JS codes and steal the content of the loaded file, example:

Press enter or click to view image in full size

While chaining all together we can get File Read and send it to our server, steps to reproduce:

Attacker sends a malicious link to unknown victim
Victims open Spam section and Clicks the link
Using <webview> we load an internal file
With <webview>.executeJavaScript(code) we steal it’s content

This photo demonstrates how it worked

Press enter or click to view image in full size

Video POC showing how easy it is:

Reward: 2k$

Thanks, buh bye ~
