---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-06_quasar-compromising-electron-apps.md
original_filename: 2022-09-06_quasar-compromising-electron-apps.md
title: 'Quasar: Compromising Electron Apps'
category: documents
detected_topics:
- supply-chain
- access-control
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- access-control
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 234635caffa9f67d8bf87ebafcce69b7617b67ba17901c220ec61c77a3e08093
text_sha256: 3ef6aafc97d008a8994fe89537b818cd8e743f1a82d9bbb186a26cb03e4c279c
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Quasar: Compromising Electron Apps

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-06_quasar-compromising-electron-apps.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `234635caffa9f67d8bf87ebafcce69b7617b67ba17901c220ec61c77a3e08093`
- Text SHA256: `3ef6aafc97d008a8994fe89537b818cd8e743f1a82d9bbb186a26cb03e4c279c`


## Content

---
title: "Quasar: Compromising Electron Apps"
page_title: "Quasar: Compromising Electron Apps: Taggart Tech"
url: "https://taggart-tech.com/quasar-electron/"
final_url: "https://taggart-tech.com/quasar-electron/"
authors: ["Taggart (@mttaggart)"]
programs: ["Microsoft"]
bugs: ["Local Privilege Escalation"]
publication_date: "2022-09-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2206
---

# Quasar: Compromising Electron Apps

![](/quasar.png) The rare app mass ejection. Here we see Teams getting yeeted at the speed of light. 7 minute read Published: 2022-09-06 

This is the story of how I used Microsoft Teams's own design against itself.

We all _kinda_ know that Electron apps are dangerous—at least to our RAM, am I right??

But seriously, these cross-platform apps, because of how they get installed, present a tasty spot for attackers to take up residence and even inject malicious code into trusted applications, with the poor user being none the wiser.

Here's how it works.

**Update: 9/7/22**. Samuel Attard from the Electron project [informed me](https://twitter.com/MarshallOfSound/status/1567539072868155393?s=20&t=MpQO7Q3w2QWz2mHfXzazZA) that Electron [currently has integrity checking](https://github.com/electron/electron/blob/main/docs/tutorial/asar-integrity.md) as an experimental feature for macOS, and other platforms will hopefully be supported soon. I missed this in my research into the issue, and I apologize for any mischaracterization of the Electron team's work.

## Research Objectives

In truth, my initial plan for this bit of research was not in fact Electron apps in general—rather, my target was Microsoft Teams, looking for any soft spots in this ubiquitous application that could present a risk to an organization like mine. Not all of what I discovered will be disclosed here, but the Electron-centric aspects of the research ended up being broadly applicable to all Electron apps.

The vulnerabilities discussed here result from 3 design decisions in Electron and apps developed with it: installation to user-writeable folders, easily unpackable application files, and lack of integrity checking of those application files.

## ASAR Files

So you're running an Electron app. Things are humming along smoothly, but do you know what's going on under the hood?

Generally speaking, Electron apps are ad-hoc Chromium browsers loading web content to produce the user interface. But these are not static files, oh no. Electron includes an implementation of the Node runtime, meaning that each Electron app has a server/client relationship between the app runner and the interface. This usage of Node will come into play later, but for now let's focus on those user-facing files.

You might think these files are kept flat in some normal folder like `C:\Program Files\Microsoft Teams` or somesuch, right?

![wrong](https://media4.giphy.com/media/cnlrYuoaoHbQBdqMem/giphy.gif?cid=ecf05e47gr04jotgzjghnufex47qvl7k403uvfplyztd8iyk&rid=giphy.gif&ct=g)

Insanely, Electron apps are installed to user-writeable directories. On Windows, this means `%LOCALAPPDATA%`, better known as `C:\Users\<username>\Appdata\Local`. The exact location will differ from app to app, but eventually you'll land on a file called `app.asar`.

![asar files](/asar-1.png)

`asar` is [Electron's special file format](https://github.com/electron/asar) to package up application files. What we're dealing with here is a glorified 0-compression tar file. During the run of an Electron app, this file is queried _constantly_ for all the resources the app needs to function.

![process hacker](/asar-2.png)

_Process Monitor showing constant`ReadFile` events to the `app.asar` file from `Teams.exe`_

Reading ASAR files is a lot easier than I thought it was going to be. In addition to Electron's first-party `npm` module linked above, there exists a [plugin for 7-Zip](https://www.tc4shell.com/en/7zip/asar/)! By installing this plugin it's possible to pack/unpack ASAR files, but you can directly edit the internal contents.

This made for some fun testing, in which I discovered multiple areas to explore. Perhaps the easiest, of course, is `main.bundle.js`.

![main.bundle.js](/asar-3.png)

_Extracted ASAR file showing the app JavaScript_

A quick note about ASAR and its weirdness. You might have noticed an `app.asar.unpacked` folder in addition to the `app.asar` file in the earlier screenshot. ASAR files have sort of a split identity between the components that are packed in the archive and the components that are not. Mostly this appears to be to accommodate the `node_modules` which are installed after packaging and not included in the `app.asar` proper. Nevertheless, both the file and the accompanying unpacked folder are required in the same directory for working with the ASAR format.

## Electron JavaScript

So what can we do with that `main.bundle.js`? Here's the thing about this file: it's "server-side," which means it has access to Node APIs. Including things like, I dunno, [`child_process`](https://nodejs.org/api/child_process.html). Just as a for instance.

![Adding calc](/asar-4.png)

_Adding calc_

![Popping Calc](/asar-5.png)

_Popping calc_

## Other Files

Now of course this is an easy way in for local code execution and persistence. However, wouldn't it be neat if we could compromise the UI as well?

We can!

Teams specifically has a number of HTML files readily available in the source that are editable straight away. Here's what happens when I add a little `alert()` action to `oops.html`, along with a modified `Content-Security-Policy` via the file's `<meta>` tag:

![XSS](/asar-6.png)

_XSS in Teams!_

What an attacker might do with the ability to guide user input via custom HTML/JS, I leave to your imagination.

## QuASAR: An ASAR Manipulation Tool

Now this research focused on Teams, but as I discovered that _all_ Electron apps utilize this ASAR format. To make demonstrating the risk a bit easier, I wrote up a lil JS and called it [QuASAR](https://github.com/mttaggart/quasar).

QuASAR is a simple utility that will analyze ASAR file discover injectable files, and allow you to inject whatever code execution you like via `child_process`. This is **NOT** intended to be a red team tool that you use on engagements. I ain't out here making weapons. Instead, this is designed to demonstrate the risk and help Defenders examine this behavior to better detect and prevent it.

## Usage
  
  
  quasar [options]
  
  Options:
  -i, --input <inputFile>  asar file to mutate (default: "app.asar")
  -c, --command <command>  command to insert (default: "calc.exe")
  -w --write  write evil files directly to application dir
  -h, --help  display help for command

`quasar` requires a `.asar` file as a target. It can either be located elsewhere on the filesystem or, as is default, an `app.asar` file local to the current directory.

You will be presented with a list of injectable `.js` files in the archive. Select one by number, and the command provided by `-c` will be injected.

Without `-w`, the resulting `app.asar` and `app.asar.unpacked` will be created in a new `evil` directory within the current directory. However, if `-w` is provided, the ASAR files will be written back to the original path, and the original files will have `.bak` appended to their filenames.

## quASAR in Action

## Mitigation/Detection

A [long-standing-issue](https://github.com/electron/asar/issues/123) on the Electron project indicates that one mitigation—cryptopgraphic signing of the ASAR files—is not being considered.

Similarly, there seems to be little interest in the types of integrity checking that Chromium-based browsers implement to protect extensions.

For detections, I would consider adding detections for `cmd.exe` and `powershell.exe` of common Electron extensions in your environment. Similarly, you may wish to identify what updaters (like `Squirrel.exe` for Teams) actually _should_ be making changes to your respective `app.asar`s, and alert on anything else doing so. These detections are, in my experience, quite high fidelity given the insular nature of Electron app code.

## Prior work

[Beemka](https://github.com/ctxis/beemka) uses a similar technique, albeit a little less modularly and focuses on front-end code injection.

## Responsible Disclosure

The findings in this writeup were reported to Microsoft and marked as "intended functionality." Put another way, this is how Electron apps are supposed to work. There is plenty of folk wisdom about this potential attack path, but neither the Electron project nor developers using it seem keen to add any mitigations against it. Therefore, this research is published in the hope that it will motivate developers to take this issue seriously—and if not, at least defenders are armed with the knowledge of how to detect this attack path.

* * *

Tagged [redteam](https://taggart-tech.com/tags/redteam/) , [webapp](https://taggart-tech.com/tags/webapp/) , [microsoft](https://taggart-tech.com/tags/microsoft/) and [writeups](https://taggart-tech.com/tags/writeups/)
