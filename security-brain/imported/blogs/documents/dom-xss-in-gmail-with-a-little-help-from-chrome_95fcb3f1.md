---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-03_dom-xss-in-gmail-with-a-little-help-from-chrome.md
original_filename: 2020-05-03_dom-xss-in-gmail-with-a-little-help-from-chrome.md
title: DOM XSS in Gmail with a little help from Chrome
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
raw_sha256: 95fcb3f1df431ce1289e9c3ae2a0a268df63673a12f3130b3bd3a24fe8302cc7
text_sha256: 19b85d3fa6c4e95b8044a00903b40fbc4e727081d0c30c46c232ea38379ac49c
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# DOM XSS in Gmail with a little help from Chrome

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-03_dom-xss-in-gmail-with-a-little-help-from-chrome.md
- Source Type: markdown
- Detected Topics: xss, command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `95fcb3f1df431ce1289e9c3ae2a0a268df63673a12f3130b3bd3a24fe8302cc7`
- Text SHA256: `19b85d3fa6c4e95b8044a00903b40fbc4e727081d0c30c46c232ea38379ac49c`


## Content

---
title: "DOM XSS in Gmail with a little help from Chrome"
page_title: "DOM XSS in Gmail with a little help from Chrome | OpnSec"
url: "https://opnsec.com/2020/05/dom-xss-in-gmail-with-a-little-help-from-chrome"
final_url: "https://opnsec.com/2020/05/dom-xss-in-gmail-with-a-little-help-from-chrome/"
authors: ["Enguerran Gillier (@opnsec)"]
programs: ["Google"]
bugs: ["DOM XSS"]
bounty: "5,000"
publication_date: "2020-05-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4610
---

May 3, 2020  |  [8 Comments](/2020/05/dom-xss-in-gmail-with-a-little-help-from-chrome/#comments)

How to use browser features to help find DOM XSS.

### The invisible Messages of Gmail

Last year, I looked for DOM XSS in Gmail website. Instead of using url params or the emails themselves as the source of the attack, I decided to use the much more discreet yet ubiquitous [postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) api. At first glance, the Gmail inbox seems a simple webpage, but if you go through the looking glass, it’s actually a dozen of different webpages (or iframes) communicating between each others.

![](/wp-content/uploads/2020/05/iframes-1024x547.png)

My first task was to make the cross-frames messages visible. This is not a native feature in DevTools yet. Instead, you can use this simple [postMessage logger extension](https://github.com/opnsec/postMessage-logger). After reloading, the console is now overwhelmed with frame to frame messages going back and forth.

![](/wp-content/uploads/2020/05/postmessage-1024x547.png)

> Each message has a **target** (the frame which receives the message), a **source** (the frame which sent the message), an **origin** (the domain of the source) and the **data** , which can be a string or a JSON object (or any kind of object that [will be cloned](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) in the process). Messages can be sent by any frame to another, even from different domain and even from different tab if the source has a reference to the target, with window.opener, window.open() and window.frames.

The target receives the message using 
  
  
  addEventListener("message", function(message){/* handle message here */})

like in the extension.

If there are too many messages, you can customize the extension to filter messages by any of their property. I was looking for interesting messages and one message in particular contained an url in the data:

![](/wp-content/uploads/2020/05/frame-1024x340.png)

This message is sent by “hangouts.google.com” to “mail.google.com” . Not only is there a url in the message data, but the url contains the word “frame”. interesting…

### The browser Toolbox

I went to the network tab of DevTools and filtered the requests by type “doc” which means “top window url and iframes src”. The same url was there:

![](/wp-content/uploads/2020/05/network-1024x480.png)

I could also confirm that the request referrer was “mail.google.com” which was a good sign since it’s the domain that received the Message. The value in red circle is the initiator of the request, the JS code that loaded the iframe. You can click on it and it brings you directly to the corresponding code in the source tab. Unminify the code, set a breakpoint, reload and the breakpoint is hit:

![](/wp-content/uploads/2020/05/debug-1024x441.png)

And voila! The function that triggers the request is appendChild(). This is pretty much all we can understand from the code which is unreadable. But with the magic of the debugger we can confirm that the argument contains an iframe with the src set to the url. If you click on the functions in the Call Stack on the right, you can navigate through the “control flow” of the program and understand its logic.

For example, here is how the message is received by the frame:

![](/wp-content/uploads/2020/05/listener.png)

You can even see the code where the source of the message sent it:

![](/wp-content/uploads/2020/05/post.png)

> There are dozens of functions between the listener and the loading of the url, across multiple files and thousands of lines of code. It is not uncommon that the browser freezes, breaks or skips breakpoint when you debug such heavy webpages, it’s a matter of trial and error! 😉

I tried to send a message to the frame from the console with the same data but with “javascript:alert(1)” instead of the url. I didn’t got an alertbox, but a CSP error message.

![](/wp-content/uploads/2020/05/csp-1024x52.png)

Thankfully, this CSP rule wasn’t enforced by IE11 and Edge (at the time) so I was able to trigger the alertbox on those browsers. There was no check on the origin of the message. A simple attack scenario is to start from the attacker webpage, open a new tab to Gmail and inject the payload in the Gmail tab using postMessage. The Gmail tab loads the javascript iframe and the attacker has arbitrary code execution on the victim’s Gmail page, which means it can read and send emails, change password of accounts registered to this email etc…

### The random Channel Name

There was still one issue: with so much communication between so many frames, it is easy to get confused, so messages usually have a channel name. The name is a random 6 char generated by “mail.google.com” and transmitted in the first message to “hangouts.google.com”. In all following messages that it receives, “hangouts.google.com” checks if it contains the correct channel name, and if not it doesn’t process the message.

The attacker doesn’t know the channel name, and 6 alphanumeric is too much possibilities to try all.  
The random generator is “Math.random()” which is not secure and [has been exploited](http://ifsec.blogspot.com/2012/09/of-html5-security-cross-domain.html) in the past by a Google engineer to find an XSS in Facebook! 🙂 However the technique required the state of the random generator to be shared between cross-domain tabs which is not the case anymore.  
The third solution is to load an iframe controlled by the attacker in the hierarchy of frames in the Gmail tab. Because of the way cross-domain redirection of iframes works in the browser, the fact that Gmail X-Frame-Options header is “SAMEORIGIN” and that the messages were sent with the argument targetOrigin “*”, it would then be possible to intercept the channel name and execute the XSS.

### Conclusion

I couldn’t find an easy way to load an iframe inside Gmail, but with all this I was confident enough to send a report to Google VRP and after a few days I received the “Nice Catch” answer and reward. Google fixed it by adding check on the origin of the message containing the url. The XSS doesn’t work anymore, but the message is still sent if you want to check.

Browsers have all the cool features to navigate complex code, and for the features that are still missing, you can build you own extensions easily. With that, good hunting! 🙂

[Tweet](https://twitter.com/intent/tweet?url=https%3A%2F%2Fopnsec.com%2F2020%2F05%2Fdom-xss-in-gmail-with-a-little-help-from-chrome%2F&via=opnsec)

[Google](/category/google/)
