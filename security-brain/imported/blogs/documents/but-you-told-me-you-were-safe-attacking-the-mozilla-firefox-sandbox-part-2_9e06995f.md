---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-23_but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-sandbox-part-2.md
original_filename: 2022-08-23_but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-sandbox-part-2.md
title: 'But You Told Me You Were Safe: Attacking The Mozilla Firefox Sandbox (Part
  2)'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 9e06995fb422e33da55c1dfe4692490f4879c3ce1d1ab118ffab17b60898104c
text_sha256: 0ac4cc5a6881f5e4eb70430b367de0655e376d5592a53e95083ec9433ff30030
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# But You Told Me You Were Safe: Attacking The Mozilla Firefox Sandbox (Part 2)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-23_but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-sandbox-part-2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `9e06995fb422e33da55c1dfe4692490f4879c3ce1d1ab118ffab17b60898104c`
- Text SHA256: `0ac4cc5a6881f5e4eb70430b367de0655e376d5592a53e95083ec9433ff30030`


## Content

---
title: "But You Told Me You Were Safe: Attacking The Mozilla Firefox Sandbox (Part 2)"
page_title: "Zero Day Initiative — But You Told Me You Were Safe: Attacking the Mozilla Firefox Sandbox (Part 2)"
url: "https://www.zerodayinitiative.com/blog/2022/8/23/but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-renderer-part-2"
final_url: "https://www.zerodayinitiative.com/blog/2022/8/23/but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-renderer-part-2"
authors: ["Hossein Lotfi (@hosselot)", "Manfred Paul (@_manfp)"]
programs: ["Mozilla"]
bugs: ["Browser hacking", "RCE", "Prototype pollution"]
bounty: "100,000"
publication_date: "2022-08-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2272
---

# Blog

#  But You Told Me You Were Safe: Attacking the Mozilla Firefox Sandbox (Part 2) 

__ August 23, 2022

__ Hossein Lotfi

In the first [part of this series](https://www.zerodayinitiative.com/blog/2022/8/17/but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-renderer-part-1), we reviewed how Pwn2Own contestant Manfred Paul was able to compromise the Mozilla Firefox renderer process via a prototype pollution vulnerability in the await implementation. In modern browser architecture design, compromising the renderer gets us just half the way there, since the sandbox prevents further damage. In this blog post, we discuss a second prototype pollution vulnerability that allowed the execution of attacker-controlled JavaScript in the privileged parent process, escaping the sandbox. This vulnerability is known as CVE-2022-1529 and is tracked as [ZDI-22-798](https://www.zerodayinitiative.com/advisories/ZDI-22-798/) on the Zero Day Initiative advisory page. Mozilla fixed this vulnerability along with the first one in Firefox 100.0.2 via [Mozilla Foundation Security Advisory 2022-19](https://www.mozilla.org/en-US/security/advisories/mfsa2022-19/).

**Root Cause**

As described in the previous post, the exploit compromised the renderer by leveraging a prototype pollution vulnerability in some built-in JavaScript code that executes in the renderer process. For the sandbox escape part of the exploit, the researcher used a second prototype pollution vulnerability. This second vulnerability exists in built-in JavaScript code that runs in the fully privileged parent process, also known as the chrome process (not to be confused with Google’s Chrome browser).

How can the sandboxed renderer process affect JavaScript running in the chrome process? The answer is that the renderer can communicate with the chrome process via various interfaces. In fact, some of these interfaces can be reached directly from JavaScript when running in a “privileged” JavaScript context (not to be confused with any OS-level concept of privilege). As we will see, achieving “privileged” JavaScript execution will be the exploit’s first step. 

After achieving privileged JavaScript execution, the exploit can reach out to various endpoints for communication with the chrome process. One of the endpoints is called [NotificationDB.](https://searchfox.org/mozilla-central/rev/cdb2004ea504bab2b66a1196c2267053e5882528/dom/notification/old/NotificationDB.jsm) It is implemented almost entirely in JavaScript. It processes various messages, which it receives via the [content process message manager](https://searchfox.org/mozilla-central/rev/cdb2004ea504bab2b66a1196c2267053e5882528/dom/base/ContentProcessMessageManager.h). In the case of a “Notification:Save” message, a “save” task is queued:

After the “save” task is put on the queue, it is handled in the chrome process, in the “taskSave” function:

At [1], both `origin` and `notification.id` are taken directly from the message data sent by the renderer, without any validation. This means we can set either of these to any serializable JavaScript value. More specifically, we can set them to any values supported by the [structured clone algorithm](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm), since this is the algorithm used to marshal data from the renderer to the chrome process. If we set `origin` to the string `"__proto__"`, then `this.notifications[origin]` will not access a normal data property. Instead, it will access the object’s prototype. This prototype is `Object.prototype`, since `this.notifications` is a plain `Object`. This gives us a prototype pollution primitive. It allows us to write any serializable JavaScript value to any property of `Object.prototype` with only one restriction: the value we write must have an `id` property that matches the property name we are writing to.

Using this prototype pollution, we can corrupt the global JavaScript state in the chrome process. This affects all JavaScript that runs in the chrome process, far beyond `NotificationDB.jsm` itself. Since JavaScript execution contexts are largely shared, all chrome-level JavaScript modules are now exposed to unexpected properties in `Object.prototype`. The exploit will use this corruption to gain chrome-level XSS during tab restoration, leading to native code execution outside the sandbox.

Now that we have a complete picture of what we want to do, let’s begin.

**Achieving Privileged JavaScript Execution**

As mentioned above, before we can invoke `NotificationDB`, we need to access a privileged JavaScript context. In particular, what we need is access to an object called `components`. This is a different object than a much more limited object confusingly also named `Components`, which is intended to be exposed to untrusted script.

To gain access to `components`, the attacker script performs the following steps. Note that all this is made possible because the attacker script has already gained full native code execution within the renderer sandbox, as detailed in [part one](https://www.zerodayinitiative.com/blog/2022/8/17/but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-renderer-part-1) of this series:

1 -- Mark the current JavaScript compartment as `system` by setting the corresponding flag in memory.  
2 -- Patch `CanCreateWrapper` to always return `NS_OK`. This prevents further security checks on the calling context.  
3 -- Call the `GetComponents` method to add the `components` object to the scope.

**Triggering the Prototype Pollution Primitive**

Once we have obtained the `components` object, we are nearly ready to trigger the prototype pollution. One obstacle remains: due to the details of Firefox's “cross-compartment” handling of JavaScript objects, the `ContentProcessMessageManager` object we want to access is hidden behind an opaque proxy object. This can be circumvented by reading the proxy’s underlying object pointer and using a [“fakeObj”](http://phrack.org/issues/70/3.html#article) to convert it to a JavaScript object. We can now call the vulnerable `NotificationDB` interface:

Remember that a limitation applies to the way that we can overwrite properties of `Object.prototype`: we can set any property `name` to any value `val`, but `val.id` must equal `name`. For our purposes, the exact value of `val` will not matter. Only its string representation is important (more precisely, the result of running the ECMAScript `ToString` algorithm). The loose type system of JavaScript helps us here. Consider the following array object:

This object has its `id` property set to the arbitrary string `"foo"`, but `ToString` will represent the object by just the string `"bar"`. Therefore, as long as we only care about the string representation, we can set any property of `Object.prototype` to any value we desire.

**Leveraging the Prototype Pollution for Sandbox Escape**

Consider the following code in [browser/components/sessionstore/TabAttributes.jsm](https://searchfox.org/mozilla-central/rev/6d396b2abda4371f54251e9de8dc790deab706fc/browser/components/sessionstore/TabAttributes.jsm#63), which executes in the chrome process:

Note that a `for ... in` loop will traverse all properties found in the prototype chain, and not only the properties found on the object itself. Therefore, by invoking the code shown above after we have polluted `Object.prototype`, we can cause `tab.setAttribute` to be called with arbitrary parameters. This will set an arbitrary HTML (technically [XUL](https://en.wikipedia.org/wiki/XUL)) attribute of a tab.

How can we cause this function to run? It turns out that the only time it is called is during the restoration of tabs. There are multiple ways to trigger this functionality: 

1 -- Session restoration after restarting the browser.  
2 -- Use of the “reopen closed tab” feature (Ctrl+Shift+T).  
3 -- Reactivating a tab after “Tab Unloading”, which occurs when Firefox starts to run out of memory.  
4 -- Automatically restoring a tab after it has crashed.

The first choice is not an option, since restarting the browser would not preserve the polluted prototype. In the real world, waiting for option #2 might work, but it requires user interaction, making it unsuitable for Pwn2Own. It’s also possible to force option #3 by allocating large chunks of memory. However, by default, it takes at least 10 minutes of inactivity before unloading will happen, which exceeds the Pwn2Own time constraint. This leaves just option #4. Fortunately, crashing the renderer process is trivial: we have already achieved memory corruption, and we can simply write to an invalid address to force a segmentation fault.

So far, the sandbox escape exploit proceeds as follows:

1 -- Trigger the prototype pollution, adding a property and value to `Object.prototype` in the chrome process. The name/value pair we add corresponds to the parameters we want to pass to `tab.setAttribute`. For example, if we add a property named `"a"` with string value `"b"`, then `tab.setAttribute` will ultimately be invoked with parameters `("a", "b")`.  
2 -- Open a new background tab. Note that a simple `window.open` method call without prior user interaction is blocked by the popup blocker. However, the check is entirely renderer-side, and the `services.ww.openWindow` API obtained from the `components` object has no such restriction.  
3 -- In this background tab, crash the renderer. The chrome process will immediately restore the background tab. The polluted prototype will cause the tab restoration logic to set our chosen attribute on the tab.

Next, we must consider: what parameters do we want to pass to `tab.setAttribute`? As the browser UI that contains the tab element is written not in HTML but rather the similar XUL markup language, attributes such as “onload” or “onerror” that are commonly used for XSS do not seem to work. Going through a list of XUL event handlers, there are only two that seem to work without any direct user interaction: “onoverflow” and “onunderflow”. These are triggered when the tab’s title text starts to exceed or no longer exceeds the available space. We can trigger the former by setting a `style` attribute with the value `text-indent: 500px`.

Once we have achieved JavaScript execution within the chrome process, there are many ways to complete the sandbox escape. For example, we could disable all sandboxing in the future by setting a preference:

`Services.prefs.setIntPref("security.sandbox.content.level", 0);`

Afterward, the exploit could run script in a new tab, which will be created without any sandbox protections. Alternatively, it could run script directly in the chrome process. Either way, the file and process APIs that are available in chrome-level JavaScript can be used to gain native code execution not constrained by any sandbox:

Here is a short video demonstrating running the full exploit against Mozilla Firefox 100.0.1 (64-bit):

**Final Notes**

Modern browsers process large volumes of data coming from numerous untrusted sources. Modern browser architecture goes a long way towards containing damage in cases where the renderer process is compromised. However, there remain multiple security checks that are performed on the renderer side. We have seen how these checks could be bypassed, ultimately leading to full compromise of the main browser process. In general, it is wise to reduce renderer-side security checks and move them to the main process wherever it is practical.

You can find me on Twitter at [@hosselot](https://twitter.com/hosselot) and follow the team on [Twitter](https://www.twitter.com/thezdi) or [Instagram](https://www.instagram.com/thezdi) for the latest in exploit techniques and security patches.

  * [Mozilla](/blog/tag/Mozilla)
  * [Firefox](/blog/tag/Firefox)
  * [Pwn2Own](/blog/tag/Pwn2Own)
