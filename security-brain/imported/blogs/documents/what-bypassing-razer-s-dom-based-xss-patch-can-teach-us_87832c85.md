---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-05_what-bypassing-razers-dom-based-xss-patch-can-teach-us.md
original_filename: 2022-02-05_what-bypassing-razers-dom-based-xss-patch-can-teach-us.md
title: What Bypassing Razer's DOM-based XSS Patch Can Teach Us
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 87832c85af4af062b5ff950ee0fd816403c4659825898d4847ef8c502c3688ac
text_sha256: b61e9f0243cca464636d538777ae3127f4b7e3d21dfd0068c68b52fa94bc532a
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# What Bypassing Razer's DOM-based XSS Patch Can Teach Us

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-05_what-bypassing-razers-dom-based-xss-patch-can-teach-us.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `87832c85af4af062b5ff950ee0fd816403c4659825898d4847ef8c502c3688ac`
- Text SHA256: `b61e9f0243cca464636d538777ae3127f4b7e3d21dfd0068c68b52fa94bc532a`


## Content

---
title: "What Bypassing Razer's DOM-based XSS Patch Can Teach Us"
page_title: "What Bypassing Razer's DOM-based XSS Patch Can Teach Us | EdOverflow"
url: "https://edoverflow.com/2022/bypassing-razers-dom-based-xss-filter/"
final_url: "https://edoverflow.com/2022/bypassing-razers-dom-based-xss-filter/"
authors: ["EdOverflow (@EdOverflow)"]
programs: ["Razer"]
bugs: ["DOM XSS"]
publication_date: "2022-02-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2937
---

Feb 5, 2022

# What Bypassing Razer's DOM-based XSS Patch Can Teach Us

An old story of a bug I uncovered and reported to Razer’s vulnerability disclosure programme resurfaced recently while I was chatting with [Linus Särud](https://twitter.com/_zulln). Back in 2017, I uncovered a snippet of JavaScript code on `deals.razerzone.com` which handled redirection after a user logged in.
  
  
  // let rurl = document.location.href;
  if (razerUserLogin) {
  rurl = rurl.split("rurl=")[1];
  location.href = decodeURIComponent(rurl);
  }
  

The code extracted the value from the `rurl` GET parameter, and redirected the user to the value of that GET parameter. For example, `https://deals.razerzone.com/?rurl=https://deals.razerzone.com/settings` would redirect to `https://deals.razerzone.com/settings`.
  
  
  let rurl =
  "https://deals.razerzone.com/?rurl=https://deals.razerzone.com/settings";
  rurl.split("rurl=");
  //=> [ 'https://deals.razerzone.com/?', 'https://deals.razerzone.com/settings' ]
  rurl.split("rurl=")[1];
  //=> 'https://deals.razerzone.com/settings'
  

Besides the obvious open redirect due to a lack of validation of the redirect endpoint (`rurl`), this code was vulnerable to DOM-based XSS.

Setting the `window.location.href` property to a `javascript:` protocol URI will execute JavaScript code in the context of the target web application. Something as simple as `https://deals.razerzone.com/?rurl=javascript:alert(document.domain)` would prompt the user with an alert message displaying the current page’s `document.domain`.

![DOM-based XSS in deals.razerzone.com](https://user-images.githubusercontent.com/18099289/152548384-9da06b14-a364-4a95-9831-975a594816c1.png)

Razer attempted to patch the vulnerability with the following `if` statement.
  
  
  // let rurl = document.location.href;
  // let siteURL = 'https://deals.razerzone.com';
  if (razerUserLogin) {
  rurl = rurl.split("rurl=")[1];
  rurl = decodeURIComponent(rurl);
  if (
  rurl.indexOf(siteURL) > -1 &&
  rurl.split("://")[1].split("/")[0] === siteURL.split("://")[1].split("/")[0]
  ) {
  location.href = rurl;
  }
  }
  

_**Author’s note:** Before continuing to read beyond this point, I encourage the reader to play around with the code and determine if the validation can be bypassed. Please feel free to respond to [this tweet](https://twitter.com/EdOverflow/status/1490038746842075141) with your bypass._

Skimming through the code above may provoke the reader to ponder why a developer would write such code. Most literature on good coding practices will mention something along the lines of “good code should not have any surprises”. More importantly, the purpose (the _“why?”_) of an important piece of code, such as the one highlighted above, should be documented in some form. Even better yet: if possible, [the code should document itself](https://en.wikipedia.org/wiki/Self-documenting_code).

![](https://user-images.githubusercontent.com/18099289/152655879-44325b4b-b8d1-4820-a92e-8cb0e868b972.png)

The attempted patch by Razer failed on all accounts. Why parse `rurl` manually rather than rely on [the built-in `URL` API](https://developer.mozilla.org/en-US/docs/Web/API/URL)? What do all the nested `split()` methods extract from `rurl`?

When performing code review, I like to better understand what might have been going through the developer’s mind. In other words, we need to determine the purpose of the code above and answer the _“why?”_.

  1. `rurl.indexOf(siteURL) > -1` is in a sense fuzzy matching the user-supplied redirect URL (`rurl`) to determine if the trusted URL (`siteURL`) is present in the string. The developer was trying to answer: _Is the trusted`siteURL` a substring of the user-supplied `rurl`?_

  2. `rurl.split("://")[1].split("/")[0]` is an attempt at extracting the hostname from user-supplied redirect URL and comparing it to the hostname from the trusted `siteURL`. `rurl.split("://")[1]` is supposed to remove the protocol scheme portion of the URL (e.g. `https:`), and `.split("/")[0]` discards the URL path revealing the hostname.

  
  
  let rurl = "https://example.com/settings";
  rurl.split("://");
  //=> [ 'https', 'example.com/settings' ]
  rurl.split("://")[1];
  //=> 'example.com/settings'
  rurl.split("://")[1].split("/");
  //=> [ 'example.com', 'settings' ]
  rurl.split("://")[1].split("/")[0];
  //=> 'example.com'
  

It appears the developer was attempting to determine if the trusted URL was present in `rurl` and if the hostname in `rurl` matched their trusted host (`deals.razerzone.com`).

Unfortunately, this validation could be bypassed in several ways. The `indexOf()` check in (1.) merely required `https://deals.razerzone.com` to be present somewhere in `rurl`; not strictly at the beginning of the string. Step (2.) would extract the hostname after the first occurrence of `://`. So `rurl` could still start with `javascript:`. However, `://deals.razerzone.com/` would have to appear at some point in the payload before any further occurrence of `://`.
  
  
  let rurl = "javascript://deals.razerzone.com/";
  rurl.split("://");
  //=> [ 'javascript', 'deals.razerzone.com/' ]
  rurl.split("://")[1];
  //=> 'deals.razerzone.com/'
  rurl.split("://")[1].split("/");
  //=> [ 'deals.razerzone.com', '' ]
  rurl.split("://")[1].split("/")[0];
  ("deals.razerzone.com");
  

As the syntax highlighting in this snippet below gives away, `//` is treated as a single-line comment and therefore comments out the `deals.razerzone.com/` portion of the payload.
  
  
  javascript://deals.razerzone.com/
  

Next, we needed a way to break out of the single-line comment and append JavaScript code. I learnt a trick for this from [Gareth Heyes](https://twitter.com/garethheyes): JavaScript [treats the `U+2028` _Line Separator_ character as a line terminator which results in a newline](https://tc39.es/ecma262/#sec-line-terminators). 1
  
  
  javascript://deals.razerzone.com/%E2%80%A8alert(document.domain)
  

That all being said, any form of line terminator would have worked here including [line feed](https://en.wikipedia.org/wiki/Newline) (`%0A`) and [carriage return](https://en.wikipedia.org/wiki/Carriage_return) (`%0D`). I like the `U+2028` trick because I have encountered situations where newlines were stripped and I needed to bypass this behaviour using `U+2028`.

Finally, to bypass the `indexOf()` check in (1.), one could append `https://deals.razerzone.com` to the end of the payload and comment it out so as not to affect the `alert()` call.
  
  
  javascript://deals.razerzone.com/%E2%80%A8alert(document.domain)//https://deals.razerzone.com
  

![DOM-based XSS patch bypass](https://user-images.githubusercontent.com/18099289/152563729-24bd74c0-f26f-42a2-b72c-935ae44226fc.png)

This illustrates one of many ways the `if` statement could have been bypassed. Something as simple as `javascript:alert()//https://deals.razerzone.com` would have worked too. An even simpler and more humorous bypass which I discovered was `javascript:alert("https://deals.razerzone.com/")`. Can you determine why this would have worked?

A quick fix for the vulnerable code would have been to verify `rurl.indexOf(siteURL) == 0` and hardcode `siteURL` to `https://deals.razerzone.com/` (note the appended `/`). This would have ensured `rurl` started with `https://deals.razerzone.com/`, preventing redirects to external hosts and mitigating the DOM-based XSS vulnerability.

However, this quick fix does not solve the problem of confusing future readers. In addition, the code is incredibly brittle and not future-proof. We are relying heavily on `/` at the end of the `siteURL`. Remove the final `/` from `siteURL` and the whole fix falls apart. This approach feels more like a _“hack”_.

A more adequate fix using the `URL` API may have been:
  
  
  if (razerUserLogin) {
  let params = new URL(document.location).searchParams;
  let rurl = params.get("rurl");
  rurl = new URL(rurl);
  // Validate redirect URI to ensure user is redirected to trusted
  // deals.razerzone.com endpoint. This prevents unvalidated redirects
  // to malicious pages and DOM-based XSS using the javascript: protocol.
  // Reference: https://hackerone.com/reports/292200
  if (rurl.hostname == "deals.razerzone.com" && rurl.protocol == "https:") {
  location.href = rurl;
  }
  }
  

This solution explains _why_ the `if` statement is needed, references the HackerOne report which provoked the code changes, and does not have any surprises lurking amidst the depths of nested `split()` methods. A developer reviewing this code in future does not have to step through the `split()` method calls as described in (2.) to figure out what is going on under the hood.

Further, [@filedescriptor](https://twitter.com/filedescriptor) noted that this implementation also addressed the way Razer were initialising `rurl` to `location.hash`. Parsing the `rurl` from the URI using Razer’s approach could have led to difficulties with URI fragments (i.e. `/#rurl=`)—an approach that would have allowed an attacker to [conceal the XSS payload](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Identifying_resources_on_the_Web#:~:text=the%20fragment%20identifier,%20is%20never%20sent%20to%20the%20server%20with%20the%20request) from firewall rules and server logs. 2

The more refined solution would probably have been to set `location.href` to `'https://deals.razerzone.com/' + rurl`, where `rurl = new URL(rurl).pathname`. Then, no matter what was supplied via the `rurl` GET parameter, the client would always redirect to an endpoint located on `deals.razerzone.com`. This would have spared us having to write any validation.

## Conclusion

Part of the aim of this blog post was to illustrate how I incorporate designing a patch to better understand the code I am exploiting. Often times advisories and vulnerability reports are published focusing entirely on the exploit and little on the mitigation strategy. For newcomers to vulnerability disclosure: I hope this blog post demonstrates my _“learn to make it; then break it”_ approach to security research. Reviewing lots of JavaScript code and my familiarity with the `URL` API allowed me to more easily recognise issues with Razer’s patch.

In addition, I have found success with suggesting patches to vendors when submitting vulnerability reports. Including concrete mitigation steps can reduce the time to resolution—and time to payout, for that matter, when reporting to bug bounty programmes. I find vendors are usually more receptive since the patch encapsulates an alternative approach to the current implementation on their affected product. This is something I regularly advise students in my workshops to do.

In the end, no matter how many hours you invest in refactoring code to resolve a security vulnerability, the simplest solution will always surface eventually.
  
  
  ❯ curl https://deals.razerzone.com/
  curl: (6) Could not resolve host: deals.razerzone.com
  

* * *

  1. The code for handling line terminators in single-line comments in JavaScript can be seen in Google Chrome’s JavaScript engine, [V8](https://en.wikipedia.org/wiki/V8_\(JavaScript_engine\)). The [parser](https://github.com/v8/v8/blob/78bc785227e95efe05f045756463696e06095506/src/parsing/scanner.cc#L208-L217) does not treat line terminator characters as if they were part of the single-line comment—adhering to the ECMAScript specification. ↩︎

  2. The URI fragment portion is never sent to the application server. ↩︎

[xss](https://edoverflow.com/tags/xss) [bug bounty](https://edoverflow.com/tags/bug-bounty) [Razer](https://edoverflow.com/tags/razer) [security engineering](https://edoverflow.com/tags/security-engineering) [Buy me a coffee ☕](https://www.buymeacoffee.com/edoverflow)[←Reading RFCs for bug bounty hunters](https://edoverflow.com/2022/reading-rfcs-for-bug-bounty-hunters/) [security.txt adoption in Switzerland→](https://edoverflow.com/2022/swiss-security-txt/)
