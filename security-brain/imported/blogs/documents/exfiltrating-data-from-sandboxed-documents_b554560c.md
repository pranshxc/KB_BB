---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-14_exfiltrating-data-from-sandboxed-documents.md
original_filename: 2024-06-14_exfiltrating-data-from-sandboxed-documents.md
title: Exfiltrating Data from Sandboxed Documents
category: documents
detected_topics:
- xss
- command-injection
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- command-injection
- clickjacking
- api-security
language: en
raw_sha256: b554560c527da00274550f67ab370585210fe66e654116960caf339be9e36cf7
text_sha256: 0b3eaf83d961db38d18646a1bedfe0abcce57ab2efe05099f3643e3263c9b41a
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Exfiltrating Data from Sandboxed Documents

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-14_exfiltrating-data-from-sandboxed-documents.md
- Source Type: markdown
- Detected Topics: xss, command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `b554560c527da00274550f67ab370585210fe66e654116960caf339be9e36cf7`
- Text SHA256: `0b3eaf83d961db38d18646a1bedfe0abcce57ab2efe05099f3643e3263c9b41a`


## Content

---
title: "Exfiltrating Data from Sandboxed Documents"
url: "https://www.monke.ie/p/exfiltrating-data-from-sandboxed-documents"
final_url: "https://www.monke.ie/p/exfiltrating-data-from-sandboxed-documents"
authors: ["Monke (@pmofcats)"]
bugs: ["postMessage", "DOM XSS", "CSP bypass"]
publication_date: "2024-06-14"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 250
---

This website uses cookies

Read our [Privacy policy](https://www.beehiiv.com/privacy) and [Terms of use](https://www.beehiiv.com/tou) for more information.

AcceptCustomizeDecline

[![Logo](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/publication/logo/dee7a871-281b-4a92-91b2-4046c012d53d/7309071b-8fdd-4861-be3d-5a47f23522f7.png)](/)

Search

[MonkeHacks](/)

SUBSCRIBE

[HOME](/)

[ARCHIVE](/archive)

[![Logo](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/publication/logo/dee7a871-281b-4a92-91b2-4046c012d53d/7309071b-8fdd-4861-be3d-5a47f23522f7.png)](/)

# Exfiltrating Data from Sandboxed Documents

![Monke](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/user/profile_picture/aeeccb78-a24f-4aae-ae26-c6f9ac649b1b/me.jpeg)

[Monke](https://www.monke.ie/authors/monke)

Jun 14, 2024

•

7 min read

# Exfiltrating Data from Sandboxed Documents

This is a writeup of a vulnerability I found with [doomerhunter](https://x.com/DoomerOutrun), that allowed us to exfiltrate data from an extremely limited Javascript environment.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/539228de-064a-4519-9e31-12b9248aa184/postMessage-monkey.png)

## The Functionality

This all began when **doomerhunter** saw a feature in the web application that allowed custom HTML and Javascript. The application would take the custom JS widget, and place it within an `iframe` on the main dashboard. This existed to allow users to implement custom logic and CSS. _Any_ kind of feature like this is incredibly difficult to implement correctly, so naturally, we probed further.

So, how was it doing this? Well, they were using `postMessage`! The parent window (the dashboard) was sending a `postMessage` message, containing the JS in a string, to the iframed document. The document endpoint had a listener that would take this data and populate the page with it. So, in a sense, this was a postMessage-based DOM XSS by design.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/285cbbae-995e-416c-b8a2-7e262a85addb/writeup_diagram_1.png)

The logic of this custom JS feature. I hope this makes sense.

Crucially, I noticed that there were **no** origin checks on where this postMessage was coming from. This meant that we could send messages from other origins by using `window.open` to open the iframed page in its own tab, and send our custom JS and CSS to it!

As much as I wish it wasn’t sandboxed to hell… it was sandboxed to hell. There was quite a number of very strict limitations on what could be executed by this custom Javascript.

### Content Security Policy

First of all, `/iframe.html` was in a [sandboxed document](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/sandbox). What is the `sandbox` directive? According to the Mozilla documentation:

❝

It applies restrictions to a page's actions including **preventing popups** , **preventing the execution of plugins and scripts** , and **enforcing a same-origin policy**.

The sandbox attribute provides a way for developers to impose restrictions on what can be executed within the document. The CSP of the document was this:
  
  
  Content-Security-Policy: sandbox allow-scripts allow-top-navigation-to-custom-protocols allow-top-navigation-by-user-activation allow-downloads

  * `allow-scripts` allows the page to run scripts, but not create pop-up windows. Pop-up windows include `alert()` and `window.open` (on a side note, `window.open("https://www.evil.com", "_self")` does _not_ trigger the popup restriction).

  * `allow-top-navigation-to-custom-protocols` allows us to navigate to non-HTTP protocols.

  * `allow-top-navigation-by-user-activation` allows us to navigate the page using activations such as button clicks - anything that can be considered as an intentional user action.

  * `allow-downloads` allows the page to trigger file downloads.

There was also another CSP defined in the HTML via `meta` tags.
  
  
  <meta http-equiv="Content-Security-Policy" content="default-src data: blob:; script-src 'unsafe-inline' 'unsafe-eval' data: blob:; style-src 'unsafe-inline' data: blob:">

  * `default-src` is set to `data:` and `blob:`, meaning that by default, we _cannot_ load anything from external origins. All such requests to external origins are blocked! This includes images, scripts, and anything else you can think of. This also includes `iframe` contents, so we cannot redirect the page with `window.open` targeted to self, as defined earlier - the iframe will simply reject contents that aren’t `blob:` or `data:`.

  * `script-src` and `style-src` are lenient here to allow for customisation. We can execute event handlers and such, as long as it’s all defined within the scope of the document itself.

Finally, `X-Frame-Options` was set to `sameorigin`, effectively ruling out the prospect of iframing this sandboxed document.

To summarise what we have so far:

  * We cannot execute `window.open`, `alert`, or any other popups.

  * The sandboxed page cannot be iframed, and cannot open iframes.

  * The sandboxed page cannot connect to any external resources at all.

  * The sandbox, by nature, is treated as if it is the parent window.

  * We can execute Javascript and CSS, as long as it’s all defined in the scope of the sandboxed document. We can use `window.open` from our attacker domain to open the sandboxed page, and we can send our payload to it using a `postMessage` message. This means that while we can _host_ a phishing page, we need to figure out a way to get the data _out_.

## The Exfiltration

The only way to get data _into_ the sandbox was postMessage. So, naturally, this was probably one of the only ways to get data _out_ of the sandbox. The question is, how do we get a window reference? postMessage is especially dangerous because it’s not limited by factors such as CSP. As I was reviewing the existing functionality within the sandboxed, one line caught my eye.

`var source = event.source;`

This was it! It turns out that `messageEvent` objects, such as postMessage events, have a `source` attribute. You can read more about `messageEvent` objects [here](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent/source). This attribute can either be a [WindowProxy](https://developer.mozilla.org/en-US/docs/Glossary/WindowProxy), [MessagePort](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort) or [ServiceWorker](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorker). If we read the glossary for the WindowProxy:  

❝

All operations performed on a WindowProxy object will also be applied to the underlying Window object it currently wraps. Therefore, **interacting with a WindowProxy object is almost identical to directly interacting with a Window object**.

With this, we can now send messages _back_ to the attacker window, completely bypassing the CSP! However, to do this, we need to lay some groundwork.

  * First, we use `window.open` to open the postMessage communication. On our attacker domain, we also set up an event listener to listen to incoming postMessage events.

  * We use our malicious Javascript payload to set up our _own_ event listener in the iframed page. We can’t set `event.source` immediately in the first payload, since we need to smuggle our Javascript into the page first.

  * We send _another_ message to the window - this one has bogus data. Our malicious Javascript uses this message to store `event.source` in a variable, which is a `WindowProxy` object that effectively works like a `Window` \- they are more or less the same.

  * When the victim enters their credentials into our super cool phishing POC using inline CSS (yes, I spent ages crafting a really convincing CSS for this), the window reference is used to send the credentials back to our attacker domain. Our event listener receives the credentials from the `postMessage` message.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/ca745801-c540-45df-a5ae-4708d6013301/postmessagexchange.png)

Sequence diagram of the attack

## Summary

As fun as this was… it was triaged and paid as _Low_. This was a fair decision from the team, I have no issue with this. It was an interesting POC to build - and yet again demonstrates that custom JS/CSS functionality is really hard to implement perfectly. I’m sure that there are more ways to exfiltrate data in situations like this - if you have ideas, let me know!

And thank you to Doomerhunter for listening to my stupid ideas. Sometimes the stupid ideas do work. I swear.

### Keep Reading

View more

# MonkeHacks

Weekly notes and thoughts from Monke/Ciarán.

[](https://twitter.com/monkehack)[](https://www.linkedin.com/in/ciar%C3%A1n-cotter/)

© 2026 Simian Security.

[Powered by beehiiv](https://www.beehiiv.com/?utm_source=monkehacks&utm_medium=footer)
