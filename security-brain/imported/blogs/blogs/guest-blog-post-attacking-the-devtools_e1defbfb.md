---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-21_guest-blog-post-attacking-the-devtools.md
original_filename: 2021-07-21_guest-blog-post-attacking-the-devtools.md
title: Guest Blog Post - Attacking the DevTools
category: blogs
detected_topics:
- sso
- access-control
- xss
- command-injection
- mfa
- automation-abuse
tags:
- imported
- blogs
- sso
- access-control
- xss
- command-injection
- mfa
- automation-abuse
language: en
raw_sha256: e1defbfb8876f203a903fb32bdf7a4502465d131433e4bc86fae9f06f96fb4ef
text_sha256: 967995b51b403b890b1f608eaff046374989a4c38cc64aa5d562ed1f02edc677
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Guest Blog Post - Attacking the DevTools

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-21_guest-blog-post-attacking-the-devtools.md
- Source Type: markdown
- Detected Topics: sso, access-control, xss, command-injection, mfa, automation-abuse
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `e1defbfb8876f203a903fb32bdf7a4502465d131433e4bc86fae9f06f96fb4ef`
- Text SHA256: `967995b51b403b890b1f608eaff046374989a4c38cc64aa5d562ed1f02edc677`


## Content

---
title: "Guest Blog Post - Attacking the DevTools"
page_title: "Guest Blog Post - Attacking the DevTools | Microsoft Browser Vulnerability Research"
url: "https://microsoftedge.github.io/edgevr/posts/attacking-the-devtools/"
final_url: "https://microsoftedge.github.io/edgevr/posts/attacking-the-devtools/"
authors: ["David Erceg (@david_erceg)"]
programs: ["Microsoft"]
bugs: ["Browser hacking"]
bounty: "36,000"
publication_date: "2021-07-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3491
---

# Guest Blog Post - Attacking the DevTools

Posted  Jul 21, 2021 

By _[David Erceg](https://twitter.com/david_erceg) _

_17 min_ read

Guest Blog Post - Attacking the DevTools __

Contents __

Guest Blog Post - Attacking the DevTools

 _In this post, we’ve invited[David Erceg](https://twitter.com/david_erceg), one of the participants in the [Edge bug bounty program](https://www.microsoft.com/en-us/msrc/bounty-new-edge), to talk about interesting bugs he found in Edge._

_By sharing this information, we hope more security researchers are motivated to work with us to improve the security of Edge and Chromium as a whole._

# Introduction

Within Chromium and its derivatives, the DevTools is an interesting attack surface. That’s because the DevTools itself is fairly highly privileged, especially if it’s attached to a page as part of a debugging session.

Therefore, bugs within the DevTools can allow a malicious extension to escalate its privileges. That’s because an extension may have the ability to load DevTools URLs and once an extension can do that, it can potentially take advantage of any bugs that are present.

The post here will examine how an extension could, in previous versions of Chrome/Edge, run code within the context of the DevTools and how the ability to do that could allow the extension to run code outside of the browser’s sandbox.

# Running code within the DevTools

There have been at least several past issues that would allow an extension to run code within the context of the DevTools.

## Using the remoteBase query parameter __

One issue in Edge involved the use of the`remoteBase` query parameter. That parameter can be used to indicate that a resource should be loaded from a particular external location. However, it’s important that the parameter is validated. A simple example that illustrates why that’s so important is something like the following URL:

`devtools://devtools/bundled/inspector.html?remoteBase=javascript:...`

If the `remoteBase` parameter is used to add an iframe to inspector.html, then in the case above, the iframe will point to a `javascript:` URL and will be same-origin with its parent.

That, essentially, is the issue that was present in the DevTools within Edge.

The first step to finding this issue was to note the following URL showed up when opening the DevTools while logging requests passed through the webRequest API:

`https://devtools.azureedge.net/serve_file/@3bb5c9989b78b4fcfd356345ac1b4c0d626baefa/third_party/webhint/worker_frame.html`

> On a side note, this can be a very useful technique to find requests that are improperly visible from privileged pages. If you create an extension that logs all requests passed to `chrome.webRequest.onBeforeRequest`, then load a privileged page, you might find instances where a privileged page is loading an unprivileged page in a frame. Using the webRequest API you could then redirect those requests to a page you control. If there are any issues with message passing between the frame and its privileged parent, you might then be able to run code within the context of the parent.

The next step after noting that the DevTools was loading the above URL was to try and track down precisely how that was done.

It’s simple enough to debug a DevTools window. If, for example, you have a DevTools window opened on a tab, you can first undock that instance, then press `Ctrl` \+ `Shift` \+ `I` to debug that instance of the DevTools. That allows you to browse and debug the JavaScript code associated with the DevTools.

An issue at this point is that the JavaScript code is minified. If you’re examining the DevTools in Chrome, it’s simple enough to look at the original source via <https://source.chromium.org>. On Edge, that’s not possible, but you can still debug through the code to get an idea of what’s happening.

In the case above, debugging through the code fairly quickly lead to the insight that the URL above was being constructed directly from the `remoteBase` parameter without any validation. Performing a quick test with the following URL confirmed that that was the case:

`devtools://devtools/bundled/inspector.html?remoteBase=javascript:console.log('Frame content set by query parameter')//`

> Note that the `javascript:` portion of the URL here ends in a comment, since the DevTools will append “third_party/webhint/worker_frame.html” onto the end of the base URL that’s set.

One thing to note is that this general issue has also affected Chromium in the past. For example, a very similar problem was first reported in issue [571121](https://crbug.com/571121). The fix made there was then shown to be insufficient in issue [619414](https://crbug.com/619414).

## Using a devtools_page entry __

The`devtools_page` [manifest entry](https://developer.chrome.com/docs/extensions/mv3/devtools/#devtools-page) refers to an extension page that’s loaded in an iframe within the DevTools and has access to the three `chrome.devtools` APIs ([chrome.devtools.inspectedWindow](https://developer.chrome.com/docs/extensions/reference/devtools_inspectedWindow/), [chrome.devtools.network](https://developer.chrome.com/docs/extensions/reference/devtools_network/) and [chrome.devtools.panels](https://developer.chrome.com/docs/extensions/reference/devtools_panels/)).

As in the case above, where the `remoteBase` query parameter wasn’t being validated, it used to be the case in Chromium that the `devtools_page` entry wasn’t being [validated either](https://crbug.com/1059577). This meant that if you set the `devtools_page` entry to a `javascript:` URL, Chromium would load that URL in an iframe within the DevTools. That frame would then have the ability to script the parent DevTools instance.

## Using a devtools_page entry and the debugger permission __

The`devtools_page` manifest entry and debugger permission make a powerful combination. For context, the debugger permission allows an extension to use the [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) to debug a page. This protocol is also what’s used internally by the DevTools, though an extension doesn’t have access to the full set of methods (e.g. `Browser.setDownloadBehavior` is [restricted](https://crbug.com/866426)).

The reason these two features are so powerful together is that an extension with the debugger permission can dispatch input events, including browser shortcuts and, more specifically, the browser shortcut to open the DevTools. That means that an extension with the debugger permission can open the DevTools and the extension’s DevTools page can then script the target page, potentially in cases where the page isn’t accessible via the debugger permission.

Previously, there were [no](https://crbug.com/1059577) [restrictions](https://crbug.com/795595) on when an extension page could script the target page (by using, for example, [chrome.devtools.inspectedWindow.eval](https://developer.chrome.com/docs/extensions/reference/devtools_inspectedWindow/#method-eval)). This meant that if the DevTools was opened on a tab and the tab was navigated to a privileged page, any extension page that was loaded within the DevTools would be able to script that privileged page. Since an extension with the debugger permission can open the DevTools, it could then run code on any privileged page, including a DevTools page, using a `devtools_page` entry.

## Sending a series of crafted messages from an extension’s DevTools page __

Internally, the DevTools[relies](https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/models/extensions/ExtensionAPI.ts;l=947;drc=d662bdf64b7d5168e7746f0cecf74598ec2ed445) on the [channel messaging API](https://developer.mozilla.org/en-US/docs/Web/API/Channel_Messaging_API) to provide the functionality available in the `chrome.devtools` API. This is something that’s markedly different from every other extension API, where the implementation is written in [C++](https://source.chromium.org/chromium/chromium/src/+/main:chrome/browser/extensions/api/) and run within the browser process.

Since the `chrome.devtools` API relies on channel messaging between two JavaScript contexts (the extension page context and the DevTools context), that provides a unique opportunity for potential issues. For example, if the DevTools doesn’t properly validate the messages it receives from an extension page, there’s the potential for privilege escalation. That is, the extension page might be able to run arbitrary code within the DevTools.

Issue [1064519](https://crbug.com/1064519) describes a case in which that was possible.

That particular issue took a while to fully develop. While it was clear after reading through some of the JavaScript code used by the DevTools that values could be overwritten, it wasn’t immediately clear how to fully take advantage of that.

A central problem is that you can really only pass data over a `MessageChannel`, not code. So while you might be able to overwrite a value in a target context, if that context isn’t properly validating messages it receives, you can’t directly invoke any code.

However, one thing an extension page can do is use [chrome.devtools.panels.create](https://developer.chrome.com/docs/extensions/reference/devtools_panels/#method-create) to create a panel. That panel will be created within the DevTools and will contain the page that’s specified by the extension in an iframe.

Crucially, the full path to the page is constructed by appending the page’s path to the extension’s origin and the origin is something that’s stored in JavaScript by the DevTools. Because of how the origin was being stored, it could be overwritten by sending a specially crafted channel message. By setting the origin to a `javascript:` URL, an extension could then cause the DevTools to create an iframe with that URL set as its source, allowing the extension to script the DevTools.

# Privileges granted to the DevTools

Once an extension can run code within the context of the DevTools, the next natural step is to determine precisely what that allows.

## Read local files __

To begin with, the DevTools can read local files. The method to do that is documented in several[different](https://crbug.com/653134) [Chromium](https://crbug.com/662859) [issues](https://crbug.com/607939). For reference, the following code, when run within the context of the DevTools, will log the contents of `file:///c:/`:

____

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11

| 
  
  
  let data = "";
  
  DevToolsAPI.streamWrite = function (id, chunk) {
  data += chunk;
  };
  
  DevToolsAPI.sendMessageToEmbedder("loadNetworkResource", ["file:///c:/", "", 0],
  function (result) {
  console.log(data);
  }
  );
  
  
---|---  
`

## Script extensions and arbitrary sites __

In addition to the Chrome Devtools Protocol, the DevTools also has access to a set of[custom API methods](https://source.chromium.org/chromium/chromium/src/+/main:chrome/browser/devtools/devtools_embedder_message_dispatcher.cc;l=182;drc=a1545e183728a7ee376fd50fcd35de618bbb4b78). One of those methods is `registerExtensionsAPI`.

As the name of the method suggests, this particular method is used to setup extension pages (i.e. the `devtools_page` entries) within the DevTools. As discussed above, the `chrome.devtools` API is implemented using the channel messaging API. That means that the DevTools contains [code](https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/models/extensions/ExtensionServer.ts;l=876;drc=d662bdf64b7d5168e7746f0cecf74598ec2ed445) to process messages it receives.

However, when you call the `chrome.devtools` API from an extension’s DevTools page, you won’t need to use the channel messaging API at all. The reason for that is that the DevTools [injects](https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/models/extensions/ExtensionServer.ts;l=840;drc=d662bdf64b7d5168e7746f0cecf74598ec2ed445) a [script](https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/models/extensions/ExtensionAPI.ts;l=213;drc=d662bdf64b7d5168e7746f0cecf74598ec2ed445) into an extension frame on every navigation of that frame. That script is what then [uses](https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/models/extensions/ExtensionAPI.ts;l=947;drc=d662bdf64b7d5168e7746f0cecf74598ec2ed445) channel messaging behind the scenes.

Looking at how `registerExtensionsAPI` is [called](https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/devtools_compatibility.js;l=547;drc=8fc6f1b872679c83b99796bf37b2ec185b8e9332):

____

`
  
  
  1
  2
  3

| 
  
  
  setInjectedScriptForOrigin(origin, script) {
  DevToolsAPI.sendMessageToEmbedder('registerExtensionsAPI', [origin, script], null);
  }
  
  
---|---  
`

it can be seen that it takes two arguments: an origin and a script.

As an example, if you make the following call in a DevTools context:

____

`
  
  
  1

| 
  
  
  InspectorFrontendHost.setInjectedScriptForOrigin("https://en.wikipedia.org", "console.log('Script run in ' + location.href)//");
  
  
---|---  
`

> Note that the script argument here ends in a comment, since the code that’s injected into the frame will have (“…guid…”) [added](https://source.chromium.org/chromium/chromium/src/+/main:chrome/browser/devtools/devtools_ui_bindings.cc;l=1694-1695;drc=05e487e9af854db7cb73111d92d45df0899325c4) onto the end of it. Without the comment, this would result in: `console.log(...)("...guid...")`, which isn’t valid.

and then load the appropriate iframe:

____

`
  
  
  1
  2
  3

| 
  
  
  let iframe = document.createElement("iframe");
  iframe.src = "https://en.wikipedia.org/wiki/Main_Page";
  document.body.appendChild(iframe);
  
  
---|---  
`

you should expect to see the following message in the console once the frame has loaded:

____

`
  
  
  1

| 
  
  
  Script run in https://en.wikipedia.org/wiki/Main_Page
  
  
---|---  
`

Therefore, if you can run code within the context of the DevTools, you can script any site you can load in an iframe. This includes any http/https website (provided the particular page you’re attempting to load isn’t blocked by the [frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors) content security policy directive).

It also includes any extension page, even those not listed under [web_accessible_resources](https://developer.chrome.com/docs/extensions/mv3/manifest/web_accessible_resources/). The reason for that is that the DevTools has the [ability](https://source.chromium.org/chromium/chromium/src/+/main:extensions/browser/extension_navigation_throttle.cc;l=266;drc=a1545e183728a7ee376fd50fcd35de618bbb4b78) to load any extension resource. One reason that’s important is that without that exception, the page listed under `devtools_page` would have to be web accessible for the DevTools to load it.

Being able to script any extension is potentially very useful, as it means you can also script builtin extensions and those extensions typically have access to private APIs, giving you further options to escalate privileges (such a case is also described further below).

## The Chrome DevTools Protocol __

As mentioned above, the Chrome DevTools Protocol is what powers the DevTools functionality internally. The DevTools frontend is essentially a UI built on top of the Chrome DevTools Protocol and the DevTools relies on this protocol to implement the bulk of its functionality.

If you can run code within the context of a DevTools instance, while that instance is attached to a page, you can then script any page, no matter how privileged. Unlike an extension using the debugger API, which will be detached when the target page is navigated to a privileged location, the DevTools has the ability to debug any page.

Not only can you script any page, you also have full access to the Chrome DevTools Protocol. That means that you can call methods that extensions can’t - such as `Browser.setDownloadBehavior`.

There’s a distinction here between being attached to a page and not being attached. When you open the DevTools in a tab (e.g. using `Ctrl` \+ `Shift` \+ `I` or `F12`), the DevTools is attached, via a debugging session, to the page loaded within that tab.

On the other hand, if you load a DevTools URL within the browser directly, that DevTools instance won’t be attached to anything, so you won’t be able to make use of the Chrome DevTools Protocol.

# Escaping the sandbox

Given all of the above, there are at least two ways you can escape the browser’s sandbox:

## By targeting an extension __

The first would be to use the fact that the DevTools can script any extension to attack a higher privileged extension. In the case of Edge, the Edge Feedback App has access to a`chrome.edgeFeedbackPrivate` API. Previously, this API had a method named `saveBytesToFile`. Because that method didn’t validate paths it received, it was possible to write a file to an arbitrary location using it. That could be used, for example, to save an executable into the user’s startup folder, which would then be run on the next login.

That specific issue in the Edge Feedback App is now fixed, and further more, it’s no longer possible to load App pages in regular tabs either.

In terms of finding potentially vulnerable extensions, `chrome://extensions-internals` is very useful. It contains a list of all extensions currently loaded in the browser. You can use it to see which component (builtin) extensions are loaded, which isn’t something that’s shown on `chrome://extensions`.

Once you’ve identified a particular extension you’d like to investigate, you can load a page from that extension, then check what APIs are available to it.

## By using the Chrome DevTools Protocol __

Since the Chrome DevTools Protocol is only available if the DevTools is actually attached to a page, there are only two feasible ways of making use of that functionality:

  1. The user would need to open the DevTools manually, or
  2. The extension would need to open the DevTools - for example, by sending the `F12` key event using the [Input.dispatchKeyEvent](https://chromedevtools.github.io/devtools-protocol/tot/Input/#method-dispatchKeyEvent) DevTools Protocol method. This would require that the extension have the debugger permission.

A relatively simple way of escaping the sandbox once you can run code within a DevTools context and have the ability to open an attached DevTools instance is to go through the following steps:

  1. Add a console pin within the DevTools. This can be done easily using the following code:

____

`
  
  1
  2

| 
  
  let pin = "..."; // Contains the code to run
  localStorage.consolePins = JSON.stringify([pin]);
  
  
---|---  
`

This doesn’t depend at all on having a DevTools instance that’s attached to a page. So provided that you can script the DevTools, you can immediately add a console pin.

> Note there is a slight difference in terminology here. While the `localStorage` key is called `consolePins`, a console pin is referred to as a “live expression” in the DevTools UI.

  2. Open an attached DevTools instance, through one of the two ways described above.

  3. Navigate the page being debugged to `chrome://downloads`. The downloads page is an interesting case, as it’s one of the very few places in the browser where a local file can be legitimately opened. That means that it’s an ideal end-stage attack target.

To actually open a file, you’ll need to call the [OpenFileRequiringGesture](https://source.chromium.org/chromium/chromium/src/+/main:chrome/browser/ui/webui/downloads/downloads.mojom;l=48;drc=f8a870251c70a05f585edff58b21fdbbf5d01670) mojo method that’s available to that page. As the name of that method suggests, a recent user gesture is required to successfully invoke the method. More specifically, a user gesture needs to have been received within the last [five seconds](https://source.chromium.org/chromium/chromium/src/+/main:content/browser/web_contents/web_contents_impl.cc;l=2224-2225;drc=f8a870251c70a05f585edff58b21fdbbf5d01670).

This can be accomplished by sending a key event using `Input.dispatchKeyEvent`, which you’ll need to do anyway if you open the DevTools using an extension with the debugger permission.

  4. The console pin added in step 1 will be regularly re-evaluated on the target page. This means that any code you add to the pin will be run within the context of `chrome://downloads`, since that’s what the target page was navigated to in step 3. The pin can then call `OpenFileRequiringGesture` to open an executable that’s been downloaded.

This is essentially an indirect use of the Chrome DevTools Protocol, since the console pins functionality internally [uses](https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/core/sdk/RuntimeModel.ts;l=645;drc=79e812efee4be5e4d4378562f8acebffe9771f20) [Runtime.evaluate](https://chromedevtools.github.io/devtools-protocol/tot/Runtime/#method-evaluate) to evaluate the code for any pins within the context of the target page.

# Conclusion

This hopefully provides an overview of some of the attack surface present within the DevTools and how it might be exploited. The DevTools itself is fairly complex and contains a lot of functionality, which creates the opportunity for exploitable issues.

Several example issues are given above that allowed an extension to run code within the context of the DevTools. As is shown, being able to do this may allow an extension to read local files, script other extensions and ultimately escape the sandbox.

Finally, in terms of reward amounts, the issue with the Edge Feedback App was assessed as being a moderate severity issue and therefore wasn’t eligible for a reward (at present, only higher severity issues are rewarded under the Microsoft Edge Bounty Program). The `remoteBase` issue described above was rewarded $30,000 USD by Microsoft. With the addition of the other two Chromium issues I filed and described above (issue [1059577](https://crbug.com/1059577) and issue [1064519](https://crbug.com/1064519)), the total amount rewarded was $36,000 USD. Which shows that finding and reporting these sorts of issues definitely has value.

# Source code references

One of the main difficulties with trying to understand this sort of functionality within Chromium is trying to find the relevant source code. Due to the size of the Chromium codebase, this can be non-trivial at times. To make it easier to get a foothold in this area, here are some links to relevant source code:

  * The DevTools frontend:

<https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/>

This contains the TypeScript code used for the DevTools frontend. If you’re investigating functionality provided by the frontend, this is where you’ll want to look.

  * ExtensionServer.ts:

<https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/models/extensions/ExtensionServer.ts;drc=d662bdf64b7d5168e7746f0cecf74598ec2ed445>

This is the code that handles messages sent from an extension’s DevTools page, in order to implement the `chrome.devtools` functionality.

  * ExtensionAPI.ts:

<https://source.chromium.org/chromium/chromium/src/+/main:third_party/devtools-frontend/src/front_end/models/extensions/ExtensionAPI.ts;drc=d662bdf64b7d5168e7746f0cecf74598ec2ed445>

This is the client-side implementation of ExtensionServer.ts. In other words, the code in this file is loaded within an extension’s DevTools page and is what’s responsible for sending channel messages to the DevTools.

  * The browser-side DevTools functionality implementation:

<https://source.chromium.org/chromium/chromium/src/+/main:chrome/browser/devtools/>

This directory contains C++ code that implements various DevTools functionality on the browser-side. For example, [DevToolsWindow::Create](https://source.chromium.org/chromium/chromium/src/+/main:chrome/browser/devtools/devtools_window.cc;l=1085;drc=f8a870251c70a05f585edff58b21fdbbf5d01670) is what creates a browser window for a DevTools instance.

  * The Chrome DevTools Protocol documentation:

<https://chromedevtools.github.io/devtools-protocol/>

Contains a listing of all methods available within the Chrome DevTools Protocol, though an extension won’t necessarily be able to call all of the methods.

  * The bulk of the browser-side implementation of the Chrome DevTools Protocol:

<https://source.chromium.org/chromium/chromium/src/+/main:content/browser/devtools/protocol/>

Note that not all of the Chrome DevTools Protocol is implemented here. For example, some methods are implemented renderer-side.

Reading through the implementation for a DevTools Protocol method can be very useful, both to determine exactly what the DevTools is doing, as well as to determine what an extension with the debugger permission can do.

__[Vulnerabilities](/edgevr/categories/vulnerabilities/), [Exploit](/edgevr/categories/exploit/)

__[DevTools](/edgevr/tags/devtools/)

This post is licensed under [ CC BY 4.0 ](https://creativecommons.org/licenses/by/4.0/) by the author.

Share [ __](https://twitter.com/intent/tweet?text=Guest%20Blog%20Post%20-%20Attacking%20the%20DevTools%20-%20Microsoft%20Browser%20Vulnerability%20Research&url=https%3A%2F%2Fmicrosoftedge.github.io%2Fedgevr%2Fposts%2Fattacking-the-devtools%2F "Twitter") [ __](https://www.facebook.com/sharer/sharer.php?title=Guest%20Blog%20Post%20-%20Attacking%20the%20DevTools%20-%20Microsoft%20Browser%20Vulnerability%20Research&u=https%3A%2F%2Fmicrosoftedge.github.io%2Fedgevr%2Fposts%2Fattacking-the-devtools%2F "Facebook") [ __](https://telegram.me/share?text=Guest%20Blog%20Post%20-%20Attacking%20the%20DevTools%20-%20Microsoft%20Browser%20Vulnerability%20Research&url=https%3A%2F%2Fmicrosoftedge.github.io%2Fedgevr%2Fposts%2Fattacking-the-devtools%2F "Telegram") [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fmicrosoftedge.github.io%2Fedgevr%2Fposts%2Fattacking-the-devtools%2F "Linkedin") __
