---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-30_google-cloud-shell-xss.md
original_filename: 2021-12-30_google-cloud-shell-xss.md
title: Google Cloud Shell XSS
category: documents
detected_topics:
- xss
- access-control
- command-injection
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- xss
- access-control
- command-injection
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: 91565184b8d870a7d7547f9cf083a7296fda39d298273889b5c2133f2b6bafd0
text_sha256: 621f66aab695f5a7d323c23375e2e80ff8afc6e78f685b3e6e51d18a31a3c515
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Google Cloud Shell XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-30_google-cloud-shell-xss.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `91565184b8d870a7d7547f9cf083a7296fda39d298273889b5c2133f2b6bafd0`
- Text SHA256: `621f66aab695f5a7d323c23375e2e80ff8afc6e78f685b3e6e51d18a31a3c515`


## Content

---
title: "Google Cloud Shell XSS"
page_title: "Google Cloud Shell XSS (Awarded $5000) | Writeups"
url: "https://ndevtk.github.io/writeups/2021/12/30/cloud-shell-xss/"
final_url: "https://ndevtk.github.io/writeups/2021/12/30/cloud-shell-xss/"
authors: ["NDevTK (@ndevtk)"]
programs: ["Google"]
bugs: ["XSS"]
bounty: "5,000"
publication_date: "2021-12-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3050
---

# [Writeups](https://ndevtk.github.io/writeups/)

This is an attempt to make a better write up than [575924 – (CVE-2021-41038) XSS in @theia/plugin-ext webview](https://bugs.eclipse.org/bugs/show_bug.cgi?id=575924) :) (It’s a Theia bug but Google paid for improving the security of the project after some discussion.)

<https://shell.cloud.google.com/> embeds the [Theia IDE](https://theia-ide.org/) from a subdomain of “cloudshell.dev” that can request access to the GCP API via postMessage(), So bugs in the Theia project may affect the security of Google Cloud. (it’s not on the Public Suffix List, used to be on appspot.com that is listed) I’m not sure when the API opt in was added, I think it used to have credentials by default.
  
  
  window.parent.postMessage({
  target: 'ID from URL of webview',
  channel: 'onmessage',
  data: {
  type: 'LOG_IN'
  }
  }); // Childs are trusted just rename “channel” to “command” and remove “target”.
  

Theia has an implementation of the VS Code webviews which are like iframes and are used to render arbitrary html this can be done via postMessage() from any origin. [(message listener)](https://github.com/eclipse-theia/theia/blob/d3501165bb4e87c3612a1a02c34a1d16ab81802c/packages/plugin-ext/src/main/browser/webview/pre/host.js#L28) [(assignment)](https://github.com/eclipse-theia/theia/blob/d3501165bb4e87c3612a1a02c34a1d16ab81802c/packages/plugin-ext/src/main/browser/webview/pre/main.js#L501)

For security webviews are meant to use a unique origin so the [sandbox restrictions](https://github.com/eclipse-theia/theia/blob/d3501165bb4e87c3612a1a02c34a1d16ab81802c/packages/plugin-ext/src/main/browser/webview/pre/main.js#L480) get enforced but they don’t due to the “allow-same-origin”. [(What I’ve learned so far while bringing VS Code’s Webviews to the web – UWTB)](https://blog.mattbierner.com/vscode-webview-web-learnings/).

Google Cloud Shell does not isolate webviews into their own origins like said [here](https://github.com/eclipse-theia/theia/tree/master/packages/plugin-ext#environment-variables) and the webviews are allowed to run terminal commands anyway via postMessage()
  
  
  window.parent.postMessage({
  target: 'ID from URL of webview',
  channel: 'onmessage',
  data: {
  text: "echo ':)'",
  type: 'RUN_IN_TERMINAL'
  }
  });
  

However they do use [CSP frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors) to block embedding of the IDE and its webviews, `Content-Security-Policy: frame-ancestors 'self' https://*.corp.google.com:* https://*.sandbox.google.com:* https://*.googleplex.com:* https://byteboard.googleplex.com https://byteboard.dev https://edge.byteboard.dev https://enginterview.withgoogle.com https://console.cloud.google.com https://ide.cloud.google.com https://shell.cloud.google.com https://ssh.cloud.google.com;` So to prevent webview hijacking/xss Theia now checks that messages are from window.parent or a child of the webview. [(Change)](https://github.com/eclipse-theia/theia/pull/10202/files) Other web IDEs may still be vulnerable if the webviews have no embedding protection like “vscode-webview.net” [(CVE-2022-24526)](https://github.com/microsoft/vscode/issues/144703) or they have [copied](https://github.com/microsoft/vscode/blob/ba40bd16433d5a817bfae15f3b4350e18f144af4/src/vs/workbench/contrib/webview/browser/pre/host.js) from VS Code, However VS Code now uses MessageChannel and [only sends to window.parent](https://github.com/microsoft/vscode/blob/6960f154ec1db21df82e87c7b043f760e6d45b8f/src/vs/workbench/contrib/webview/browser/pre/main.js#L298).

## Exploitation

In order to exploit this an attacker needs to send a message to the webview. After looking at the code in `https://www.gstatic.com/_/cloudshell/_/js/` I found that using the `opencloudcodewelcome` URL parameter it will embed Theia and open a webview automatically. [https://shell.cloud.google.com/?show=ide&opencloudcodewelcome=true](https://shell.cloud.google.com/?show=ide&opencloudcodewelcome=true) (this now uses [COOP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy) allow-popups so the opener can’t be exploited)

Then to get [XSS](https://owasp.org/www-community/attacks/xss/) any opener can send a message to the embedded webview.
  
  
  w[2][0].postMessage(
  {
  channel: 'content',
  args: {
  options: {allowScripts: true},
  contents: '<script>document.write(document.domain)</script>'
  }
  },
  '*'
  );
  

# Further research

Cant tell if the `Missing Schema Check` is a valid concern for CVE-2022-24526 since `parentOrigin` should contain the scheme, however hash collisions may be possible. <https://github.com/google/security-research/security/advisories/GHSA-h924-7cqw-j96h>

# Embed users content from Google Cloud Shell in cross-site iframes (Fixed)

Since there’s no embedding protection on /_cloudshell/ and a “SameSite None” cookie is used for “CloudShellAuthorization” it’s possible to embed the files on to an attacker controlled website like
  
  
  iframe.src = '8080-SERVER.cloudshell.dev/_cloudshell/file?path=/entrypoint.sh';
  

When the Theia subdomain is known (DNS is normally insecure) this allows attacks like [The Human Side Channel](https://ronmasas.com/posts/the-human-side-channel) and [Element leaks](https://xsleaks.dev/docs/attacks/element-leaks/).  
It would be worse if the “SERVER” could be leaked without network access, That’s prevented because the redirector [https://ssh.cloud.google.com/devshell/proxy?port=8080&devshellProxyPath=%2Ffoo](https://ssh.cloud.google.com/devshell/proxy?port=8080&devshellProxyPath=%2Ffoo) blocks embedding and has COOP.

[Improve this page](https://github.com/NDevTK/writeups/edit/main/_posts/2021-12-30-cloud-shell-xss.md) Default Random Basic Shader Wallpapers Chrome Cast Surveillance Chromium Advisories Side Channel Echo Grove ParentalControlLock Light Cyberpunk Code Matrix Blueprint Redacted Glitch Old Terminal Gradient Comic Base64 Emoji Minecraft Flip 🦆 Rainbow text Typoifier Summarizer AI Audio Spoof Oceanic Depths Retro Gamification NoScript
