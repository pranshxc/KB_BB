---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-10_supply-chain-attacks-a-new-era.md
original_filename: 2024-06-10_supply-chain-attacks-a-new-era.md
title: 'Supply Chain Attacks: A New Era'
category: documents
detected_topics:
- supply-chain
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- supply-chain
- access-control
- command-injection
- api-security
language: en
raw_sha256: 06aab97506151a2271ede5641894919f76f4922c5434750f4f42fc53f168b2dc
text_sha256: 4e17b4f07226698124f71948f49acfba5d8b3ee57bd6c4fc71c833b486b4d50c
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: true
---

# Supply Chain Attacks: A New Era

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-10_supply-chain-attacks-a-new-era.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: True
- Raw SHA256: `06aab97506151a2271ede5641894919f76f4922c5434750f4f42fc53f168b2dc`
- Text SHA256: `4e17b4f07226698124f71948f49acfba5d8b3ee57bd6c4fc71c833b486b4d50c`


## Content

---
title: "Supply Chain Attacks: A New Era"
url: "https://osec.io/blog/2024-06-10-supply-chain-attacks-a-new-era"
final_url: "https://osec.io/blog/2024-06-10-supply-chain-attacks-a-new-era/"
authors: ["Bruno Halltari (@BrunoModificato)", "Caue Obici (@caueobici)"]
programs: ["Lavamoat"]
bugs: ["Supply chain attack", "Web3 hacking"]
publication_date: "2024-06-10"
added_date: "2024-07-01"
source: "pentester.land/writeups.json"
original_index: 256
---

#### Jun 10, 2024

### Supply Chain Attacks: A New Era

Unpacking Lavamoat and how it fights supply chain attacks in Web3. We spill the beans on some sneaky bypasses, illustrating just how tricky it is to lock down JavaScript ecosystems.

![Picture of Bruno Halltari](/profiles/bruno.jpeg)#### [Bruno Halltari](https://x.com/BrunoModificato)

![Picture of Caue Obici](/profiles/caue.png)#### [Caue Obici](https://x.com/caueobici)

Copy Link

[](https://www.twitter.com/share?url=)

![Heading image of Supply Chain Attacks: A New Era](/posts/supply-chain-attacks-a-new-era/header.jpg)

## Overview

[Supply chain](https://www.cloudflare.com/it-it/learning/security/what-is-a-supply-chain-attack/) attacks are becoming [increasingly popular in Web3](https://www.bleepingcomputer.com/news/security/ledger-dapp-supply-chain-attack-steals-600k-from-crypto-wallets/). In response, Lavamoat has emerged as a robust defense mechanism against supply chain attacks, offering sophisticated isolation and access control features. These help ensure that malicious dependencies cannot execute harmful code.

In this article, we will explore how each component of Lavamoat works, and dive into the various bypasses we reported.

### Introduction

It is important to note that there are three different versions of LavaMoat:

  1. [Lavamoat Browserify](https://github.com/LavaMoat/LavaMoat/tree/f3e53c8c44f063f000adc620b0aa3f7a41dda5c6/packages/browserify) serves as a bundle packer. This helps organize and package JavaScript code for frontend deployment.
  2. [NodeJS Lavamoat](https://github.com/LavaMoat/LavaMoat/tree/f3e53c8c44f063f000adc620b0aa3f7a41dda5c6/packages/node) is a variant of Lavamoat tailored specifically for Node.js environments.
  3. [Lavamoat allow-scripts](https://github.com/LavaMoat/LavaMoat/tree/f3e53c8c44f063f000adc620b0aa3f7a41dda5c6/packages/allow-scripts) are used to prevent malicious code execution on lifecycle scripts.

### Lavamoat's Security Features

The three most important features of Lavamoat1 are:

  * Policy Files
  * NPM Anti Hijacking
  * Scuttling

Let's go over them one by one.

#### Policy Files

Policy files are one important feature of Lavamoat, as they limit access to the potentially dangeorus platform API and Globals.

For example, take the [Metamask Snap policy file](https://github.com/MetaMask/snaps/blob/c5ddd897734f900f459c66a91f3334e76903825c/packages/snaps-execution-environments/lavamoat/browserify/iframe/policy.json#L77):
  
  
  "@metamask/providers": {
  "globals": {
  "Event": true,
  "addEventListener": true,
  "chrome.runtime.connect": true,
  "console": true,
  "dispatchEvent": true,
  "document.createElement": true,
  "document.readyState": true,
  "ethereum": "write",
  "location.hostname": true,
  "removeEventListener": true,
  "web3": true
  },
  "packages": {
  "@metamask/object-multiplex": true,
  "@metamask/providers>@metamask/safe-event-emitter": true
  

The `globals` section in a LavaMoat policy specifies which global variables and properties a module can access, setting permissions for its global scope interactions. Similarly, the `packages` section outlines the module's dependencies and the permissions or trust relationships with those dependencies. This defines how `@metamask/providers` interacts with other packages.

To enforce these policies, LavaMoat uses `lavapack`, a custom webpack that wraps ever dependency and applies the specified rules independently.

#### NPM Anti Hijacking

One important note is that Lavamoat can't rely solely on the names of the packages as they are published on NPM. Otherwise, a malicious actor could create a package with the same name as a popular, trusted package.

Instead, Lavamoat looks at how each package is connected by [walking the modules](https://github.com/LavaMoat/LavaMoat/blob/f3e53c8c44f063f000adc620b0aa3f7a41dda5c6/packages/core/src/walk.js#L22) in a project's dependency tree, thus generating a unique name for each package.

#### Scuttling

Scuttling is an optional feature that adds an extra layer of protection. Even if the real `GlobalThis` object is leaked by an attacker or accessed through a malicious package manager, scuttling removes sensitive APIs, preventing malicious requests from being executed.

For example, [here](https://github.com/LavaMoat/LavaMoat/blob/f3e53c8c44f063f000adc620b0aa3f7a41dda5c6/packages/core/src/scuttle.js#L57) we see how Lavamoat checks if the feature is enabled after the root package compartment is created:
  
  
  if (scuttleOpts.enabled) {
  if (!Array.isArray(scuttleOpts.exceptions)) {
  throw new Error(`LavaMoat - scuttleGlobalThis.exceptions must be an array, got "${typeof scuttleOpts.exceptions}"`)
  }
  scuttleOpts.scuttlerFunc(globalRef, realm => performScuttleGlobalThis(realm, scuttleOpts.exceptions))
  }
  

Subsequently, the code defines a [function](https://github.com/LavaMoat/LavaMoat/blob/f3e53c8c44f063f000adc620b0aa3f7a41dda5c6/packages/core/src/scuttle.js#L74) called `generateScuttleOpts` that creates and returns an options object.

Finally, the `performScuttleGlobalThis` [function](https://github.com/LavaMoat/LavaMoat/blob/f3e53c8c44f063f000adc620b0aa3f7a41dda5c6/packages/core/src/scuttle.js#L125) modifies the properties of the global object (`globalRef`). It starts by creating an array `props`, containing the names of all properties in the prototype chain of globalRef. Then, an empty object is then created to serve as a proxy for scuttled properties. The function then iterates over each property, making changes to the global window object based on the provided configuration.

## Hacking Webpacks

Now let's get to the fun stuff.

Webpack is used to bundle all modules and packages into a single file. It inserts all the code of these modules into the bundle file. Checking Lavapack source code, we can see how this actually happens.
  
  
  const filename = encodeURI(String(moduleData.file))
  let moduleWrapperSource
  if (bundleWithPrecompiledModules) {
  moduleWrapperSource = `function(){
  with (this.scopeTerminator) {
  with (this.globalThis) {
  return function() {
  'use strict';
  // source: ${filename}
  return function (require, module, exports) {
  __MODULE_CONTENT__
  };
  };
  }
  }
  }`
  

Lavapack uses `with()` proxies to restrict the objects accessible by the module, and `__MODULE_CONTENT__` is replaced by the content of a file required by the project being built.

### Injection? Not So Simple

We first tried to inject invalid javascript inside a javascript file, and then attempt to escape the `with` environment:
  
  
  } // end function 1
  } // end function 2
  } // end with 1
  } // end with 2
  
  alert(document.domain)
  

However, when we tried to bundle it, a `ParseError` was thrown. This is because Lavapack is a plugin of [browserify](https://github.com/browserify/browserify), which has a syntax check before replacing the code.

Looking deeper into browserify, we find it has a `syntax` stage on it's pipeline, and uses the `syntax-error` npm package to validate the syntax of each javascript file content. Since Lavapack replaces the `pack` stage on browserify pipeline, which comes after the `syntax`, it was not possible to inject invalid javascript to escape the Lavamoat sandbox.

![Pipeline](/posts/supply-chain-attacks-a-new-era/pipeline.png)

The `syntax-error` package performs a syntax check by using `eval` with function hoisting:
  
  
  try {
  eval('throw "STOP"; (function () { ' + src + '\n})()');
  return;
  }
  catch (err) {
  if (err === 'STOP') return undefined;
  if (err.constructor.name !== 'SyntaxError') return err;
  return errorInfo(src, file, opts);
  }
  

Interestingly, it _is_ possible to inject a `}); (() => {` inside source, and will not throw a syntax error. Unfortunately, this is not enough to bypass the `with()` sandbox of Lavapack.

### SourceMap: The Syntax Killer

Lavapack has a feature to extract source maps files from the code using [convert-source-map](https://www.npmjs.com/package/convert-source-map) npm package:
  
  
  function extractSourceMaps(sourceCode) {
  const converter = convertSourceMap.fromSource(sourceCode)
  // if (!converter) throw new Error('Unable to find original inlined sourcemap')
  const maps = converter && converter.toObject()
  const code = convertSourceMap.removeComments(sourceCode)
  return { code, maps }
  }
  

This code removes the source map comments of the source code, meaning that there actually is a modification of source code in Lavapack after the `syntax` stage. Reviewing the `convert-source-map` code, we can see exactly how this happens.
  
  
  Object.defineProperty(exports, 'commentRegex', {
  get: function getCommentRegex () {
  // Groups: 1: media type, 2: MIME type, 3: charset, 4: encoding, 5: data.
  return /^\s*?\/[\/\*][@#]\s+?sourceMappingURL=data:(((?:application|text)\/json)(?:;charset=([^;,]+?)?)?)?(?:;(base64))?,(.*?)$/mg;
  }
  });
  
  exports.removeComments = function (src) {
  return src.replace(exports.commentRegex, '');
  };
  

Looking deeper at the RegEx, it matches the start of the multiple line comment (`/*`) but doesn't match the end of it, meaning that the syntax would break in the case of multiline source map comments.

### The Bypass

By abusing the `removeComments` function, we could bypass the Lavamoat restrictions by escaping the `with()` sandbox. To do so, we created a multiline source map comment, and injected the invalid javascript inside the comment:
  
  
  /*# sourceMappingURL=data:,{}
  
  }}}}
  }, {
  package: "xpl",
  file: "node_modules/xpl/index.js",
  test: alert(document.domain),
  test1: () => { () => { () => { () => {
  
  /*
  */
  

This allows malicious code to execute without breaking any other package or feature. This payload also makes the supply chain attack more impactful. Any injected code is executed as soon as the bundle file is imported.

### Lavapack Patch

Metamask mitigated the issues we reported on Lavapack by defining `assertValidJS`, an independent check that differs from the browserify syntax check we used to exploit the issue.

The patch was introduced in commit [9c38cd4](https://github.com/LavaMoat/LavaMoat/commit/9c38cd47e7875dde53349dd34971c74ce34004d9).
  
  
  + function assertValidJS(code) {
  +  try {
  +  new Function(code)
  +  } catch (err) {
  +  throw new Error(`Invalid JavaScript: ${err.message}`)
  +  }
  + }
  
  +  // additional layer of syntax checking independent of browserify
  +  assertValidJS(sourceMeta.code)
  

## Hacking JS Realms

Lavamoat scuttling removes unnecessary and dangerous attributes from the `globalThis` object. However, this can be easily bypassed when Lavamoat is running in a browser context.
  
  
  const w = window.open('/non_existent');
  w.alert(document.domain)
  

This opens a new window with a new JS Realm (another `globalThis` object), and uses it to execute code in the context of the scuttled window. Note that the window needs to be same-origin and must not be scuttled.

As a mitigation, some applications integrate SnowJS with scuttling, so every new same-origin window and iframe will be detected and scuttled (check the [Metamask implementation](https://github.com/MetaMask/metama***REDACTED-API-KEY***-snow.js#L22))

### SnowJS Attack Surface

SnowJS is a javascript sandbox implementation that secures same-origin realms in browser applications. It is configured to detect new realms and attach them to the sandbox.

As a mechanism, it hooks functions that can be used to create realms (an iframe, for example). For example, here are some of the [hooked inserters](https://github.com/LavaMoat/snow/blob/ecf1add05c774b90b8baeff934b2e40585e13ca4/src/inserters.js#L9) functions:
  
  
  const map = {
  Range: ['insertNode'],
  DocumentFragment: ['replaceChildren', 'append', 'prepend'],
  Document: ['replaceChildren', 'append', 'prepend', 'write', 'writeln'],
  Node: ['appendChild', 'insertBefore', 'replaceChild'],
  Element: ['innerHTML', 'outerHTML', 'insertAdjacentHTML', 'replaceWith', 'insertAdjacentElement', 'append', 'before', 'prepend', 'after', 'replaceChildren'],
  ShadowRoot: ['innerHTML'],
  HTMLIFrameElement: ['srcdoc'],
  };
  

This means that an attacker can't use any of these functions to create an iframe and bypass the snowJS sandbox, because it will detect the new frame and include it in the sandbox.

Unfortunately, client-side javascript is surprisingly complex with lots of strange behaviours that could be used to bypass the hook security feature.

### Bypassing SnowJS

The deprecated [`document.execCommand`](https://developer.mozilla.org/en-US/docs/Web/API/Document/execCommand) function is used to execute commands inside a `contenteditable` focused context. Despite this being a deprecated function, it is still supported by modern browsers.
  
  
  <div id=test contenteditable autofocus></div>
  

After inserting this element to a page, it is possible to use `insertHTML` command of `document.execCommand` to add a non-sandboxed iframe.
  
  
  document.execCommand('insertHTML', false, '<iframe srcdoc="aaa">');
  

### Impact On Lavamoat Scuttling

As it is recommended to use snowJS integrated with Lavamoat scuttling to prevent bypasses, it is possible to completely bypass the scuttling feature without pre-conditions.

For the exploit, the only used functions are in `document` object, which can never be scuttled once it is a non-writable and non-configurable property in `globalThis` object.

Consider this example, which runs a scuttled `alert` function:
  
  
  document.body.innerHTML = "<div id=test contenteditable autofocus></div>";
  document.getElementById('test').focus();
  document.execCommand('insertHTML', false, '<iframe srcdoc="aaa">');
  document.getElementsByTagName('iframe')[0].contentWindow.alert(document.domain);
  

### SnowJS Patch

Metamask is working on conceptual changes and aiming to integrate SnowJS as a [browser feature within W3C standards](https://www.w3.org/2023/03/secure-the-web-forward/talks/realms.html#talk), with the intention of addressing not only this issue, but also all other well-known issues with SnowJS. [Here](https://github.com/weizman/Realms-Initialization-Control) is their new proposal.

## Chaining The Impacts

We were able to find two vulnerabilities in lavamoat project:

  1. Policy File Bypass
  2. Scuttling Bypass

By combining the exploits, it is possible to completely bypass lavamoat supply-chain protections using a compromised dependency.

Using Metamask as an example, these exploits could be used to retrieve the encrypted keypair in extension storage. The only precondition would be compromising a NPM dependency.

## Conclusion

The vulnerability within the Lavapack module sandboxing, along with the issues we discussed regarding SnowJs and the Scuttling feature, illustrate the complexities of mitigating supply chain attacks within the JavaScript ecosystem. While the lavapack release with a mitigation was available in under two days, the inherent complexity makes designing robust security implementations a challenging task.

![Hello Otetr](/posts/supply-chain-attacks-a-new-era/hello-otter.gif)

## Footnotes

  1. Excluding SES, which was covered [in our last article](https://osec.io/blog/2023-11-01-metamask-snaps) ↩

###### Article Contents

  * 1\. Overview
  * 2\. Hacking Webpacks
  * 3\. Hacking JS Realms
  * 4\. Chaining The Impacts
  * 5\. Conclusion
  * 6\. Footnotes

##### Read more from our blog

[See All](/blog)

[![Preview card for 'Auto reverse-engineering the Hyperliquid risk engine, with some agentic help'](/posts/hyperliquid-risk-engine/title.png)Jun 22, 2026Auto reverse-engineering the Hyperliquid risk engine, with some agentic help](/blog/2026-06-22-hyperliquid-risk-engine)

[![Preview card for 'The Goldmine of Insecure WebView Integrations'](/posts/insecure-webview-integrations/title.png)Jun 18, 2026The Goldmine of Insecure WebView Integrations](/blog/2026-06-18-goldmine-of-insecure-webview-integrations)

[![Preview card for 'Pwning Minecraft: 4-Byte Heap Overflow to RCE'](/posts/minecraft-heap-overflow-to-rce/title.png)Jun 2, 2026Pwning Minecraft: 4-Byte Heap Overflow to RCE](/blog/2026-06-02-minecraft-heap-overflow-to-rce)

### Subscribe to our blogs

Email 

Subscribe
