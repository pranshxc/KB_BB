---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-08_steam-fire-and-paste-a-story-of-uxss-via-dom-xss-clickjacking-in-steam-inventory.md
original_filename: 2018-06-08_steam-fire-and-paste-a-story-of-uxss-via-dom-xss-clickjacking-in-steam-inventory.md
title: Steam, Fire, and Paste – A Story of UXSS via DOM-XSS & Clickjacking in Steam
  Inventory Helper
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- clickjacking
- api-security
language: en
raw_sha256: 598be895fb47578abb07cea2cd9e600dd6a0a23ccf57aa3042321e372c75f0e0
text_sha256: 036c16c8da5eb2df7b20f2ef1eaa4590e38cafea2106b14bb7a778c376642e87
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Steam, Fire, and Paste – A Story of UXSS via DOM-XSS & Clickjacking in Steam Inventory Helper

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-08_steam-fire-and-paste-a-story-of-uxss-via-dom-xss-clickjacking-in-steam-inventory.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, clickjacking, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `598be895fb47578abb07cea2cd9e600dd6a0a23ccf57aa3042321e372c75f0e0`
- Text SHA256: `036c16c8da5eb2df7b20f2ef1eaa4590e38cafea2106b14bb7a778c376642e87`


## Content

---
title: "Steam, Fire, and Paste – A Story of UXSS via DOM-XSS & Clickjacking in Steam Inventory Helper"
page_title: "Steam, Fire, and Paste – A Story of UXSS via DOM-XSS & Clickjacking in Steam Inventory Helper – The Hacker Blog"
url: "https://thehackerblog.com/steam-fire-and-paste-a-story-of-uxss-via-dom-xss-clickjacking-in-steam-inventory-helper/index.html"
final_url: "https://thehackerblog.com/steam-fire-and-paste-a-story-of-uxss-via-dom-xss-clickjacking-in-steam-inventory-helper/index.html"
authors: ["Matthew Bryant (@IAmMandatory)"]
bugs: ["DOM XSS", "Universal XSS", "Clickjacking", "Browser extension hacking"]
publication_date: "2018-06-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5848
---

# Steam, Fire, and Paste – A Story of UXSS via DOM-XSS & Clickjacking in Steam Inventory Helper

# Summary

The [“Steam Inventory Helper”](https://chrome.google.com/webstore/detail/steam-inventory-helper/cmeakgjggjdlcpncigglobpjbkabhmjl?hl=en) Chrome extension version 1.13.6 suffered from both a DOM-based Cross-site Scripting (XSS) and a clickjacking vulnerability. By combining these vulnerabilities it is possible to gain JavaScript code execution in the highly-privileged context of the extension’s background page. Due to the extension declaring the “” permission, this vulnerability can be exploited to hijack all sites that the victim is authenticated to. For example, if a user is authenticated to their bank, Steam, Gmail, and Facebook, this vulnerability could be used to access all of those accounts. This vulnerability is fixed in the latest version of the extension and all users should update (if Chrome has not done so for them automatically).

The core of this issue is due to a DOM-based Cross-site Scripting (XSS) in “/html/bookmarks.html” which is frameable from arbitrary web pages due to a the [“web_accessible_resources”](https://developer.chrome.com/extensions/manifest/web_accessible_resources) directive specifying this resource. By submitting an entry with the name of an XSS payload this page can be exploited to gain JavaScript execution in the context of the extension. Since a user is unlikely to paste an XSS payload into this page of their own will, the clickjacking vulnerability is used to redress the UI of the application to trick the victim into exploiting the issue. A pretext of a “Bot Detection” page is used to get the victim to paste the payload (hidden inside of a larger “verification code”) and click the “Add” button to exploit the issue. The full proof-of-concept can be seen in the video below.

# Proof-of-Concept

# Technical Details

The first vulnerability is the DOM-based Cross-site Scripting (XSS) vulnerability in “/html/bookmarks.html”, the following is the vulnerable JavaScript from the included “bookmarks.js”:
  
  
  $('#btAdd').click(function() {
      var btname = $('#txtName').val();
      if ($('.custom-button .name').filter(function() {
          return $(this).text() === btname;
      }).length) return false;
  
      var span = $('<span class="custom-button">');
      span.html('<span class="name">' + btname + '</span>');
      span.append('<a href="javascript:void(0)" title="remove">x</a>');
      span.attr('title', btname);
      span.data('id', (new Date().getTime()));
      $('div.custom-buttons .existing').append(span);
      save_options();
  });
  

The above JavaScript takes the value of the “txtName” text box and uses string concatenation to build HTML which is appended to the DOM via jQuery’s [“append()”](https://api.jquery.com/append/) function. This is the core of the XSS vulnerability since user input should always be contextually escaped to prevent injection of arbitrary markup. Normally, Chrome extension Content Security Policy (CSP) should prevent this vulnerability from being exploited. However, due to the loosening of this policy via [‘unsafe-eval’](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src) and the use of jQuery’s DOM APIs, this was still able to be exploited. This is due to much of jQuery’s DOM APIs making use of [“globalEval()”](https://api.jquery.com/jquery.globaleval/), which automatically passes scripts to [“eval()”](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval) upon appending to the DOM.

While this is a serious vulnerability, on its own exploitation is fairly limited due to the user-interaction required to exploit it. The victim would have to open the page, paste a Cross-site Scripting (XSS) payload into the field, and click the “Add” button to exploit it.

In order to better weaponize this vulnerability we make use of a separate vulnerability (clickjacking) in order to bolster the attack.

The following is an excerpt from the Chrome extension’s manifest:
  
  
  ...trimmed for brevity...
  "web_accessible_resources": [
      "_locales/*",
      "bundle/*",
      "dist/*",
      "assets/*",
      "font/*",
      "html/bookmarks.html",
      "css/*.css",
      "js/*.js",
      "js/jquery/*.js",
      "js/lang/*"
  ],
  ...trimmed for brevity...
  

The above section demonstrates that the extension casts a wide net with its “web_accessible_resources” policy. By default Chrome extensions prevent framing and navigation to Chrome extension pages from arbitrary web pages as an extra security measure. This directive loosens this restriction, allowing for third party pages to navigate to and frame the specified resources. Much of the extension’s privileged UI pages are specified under this directive, rendering the extension vulnerable to clickjacking.

As can also be seen in the excerpt, the “/html/bookmarks.html” page is also able to be framed and thus exploited via clickjacking. We abuse this to iframe this page in our web page, and overlay the frame with DOM elements to redress the layout. This makes it so that the victim is unaware that they are actually interacting with the extension below. The following animation demonstrates this effect:

[![clickjacking-animation-example](/wp-content/uploads/2018/06/clickjacking-animation-example.gif)](/wp-content/uploads/2018/06/clickjacking-animation-example.gif)

The above example demonstrates how we redress the UI to trick the victim. The “Bot Detection” page provides a button to click to copy the “Verification code” to the victim’s clipboard. This “verification code” is actually a Cross-site Scripting (XSS) payload inside of a large amount of random hex bytes. This hides the payload from the victim’s view while they paste it into the extension’s textbox, leading the victim into believing they are just copying and pasting a long random code. Finally, when the victim clicks the “Add” button, the XSS fires.

# Root Cause & Further Thoughts

There are two notable points of interest in this exploit. The first is that we were able to achieve DOM-XSS even with a fairly tight Content Security Policy (CSP) of the following:
  
  
  "script-src 'self' 'unsafe-eval'; object-src 'self'"
  

While this CSP is fairly strong, it crumbles when combined with unsafe usage of jQuery’s DOM manipulation APIs such as “.html()” and “.append()”. This is something to look for when auditing Chrome extensions (and when writing them), if you make use of jQuery and have ‘unsafe-eval’ in your CSP – you’re playing with fire.

The second interesting point is that clickjacking is a valid vulnerability which can absolutely affect Chrome extensions. All that is required is that a privileged Chrome extension UI page be exposed via the [“web_accessible_resources”](https://developer.chrome.com/extensions/manifest/web_accessible_resources) directive. After taking a look at many of the popular extensions on the Chrome store it seems many of them fall victim this simple mistake. Most of the time this is due to accidental overscoping via wildcarding of a privileged extension HTML page. This not only opens up extensions to attacks like clickjacking but can result in other vulnerabilities if the extension takes in user input from “location.hash”, “postMessage”, etc. The default protection given to Chrome extensions via the navigation sandboxing should not be taken for granted by the extension developers.

# Timeline

  * June 4: Disclosed to SIH TechSupport (owners of extension)
  * June 6: Vendor confirms receipt of issue, states they will look into it and fix it.
  * June 7: Vendor updates extension to fix the vulnerabilities.

[chrome extension csp bypass](/tags#chrome extension csp bypass "Pages tagged chrome extension csp bypass")[chrome extension hijacking](/tags#chrome extension hijacking "Pages tagged chrome extension hijacking")[csp jquery](/tags#csp jquery "Pages tagged csp jquery")[unsafe-inline jquery](/tags#unsafe-inline jquery "Pages tagged unsafe-inline jquery")[uxss chrome](/tags#uxss chrome "Pages tagged uxss chrome")[xss chrome extension](/tags#xss chrome extension "Pages tagged xss chrome extension") Matthew Bryant (mandatory)

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=/steam-fire-and-paste-a-story-of-uxss-via-dom-xss-clickjacking-in-steam-inventory-helper/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=/steam-fire-and-paste-a-story-of-uxss-via-dom-xss-clickjacking-in-steam-inventory-helper/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=/steam-fire-and-paste-a-story-of-uxss-via-dom-xss-clickjacking-in-steam-inventory-helper/ "Share on Google Plus")

[About the Author](https://thehackerblog.com)

### Matthew Bryant (mandatory)

![Matthew Bryant \(mandatory\)](/images/avatar.jpg)

Security researcher who needs to sleep more. Opinions expressed are solely my own and do not express the views or opinions of my employer.

  * [__](https://github.com/mandatoryprogrammer)
  * [__](https://www.linkedin.com/in/matthew-bryant-a9403289/)

[Follow @mandatoryprogrammer](https://github.com/mandatoryprogrammer)  
[Follow @IAmMandatory](https://twitter.com/IAmMandatory)

[Read More](/reading-your-emails-with-a-readwrite-chrome-extension-same-origin-policy-bypass-8-million-users-affected/)

### ["Zero-Days" Without Incident - Compromising Angular via Expired npm Publisher Email Domains](/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/)

**NOTE:** *If you're just looking for the high level points, see the"[The TL;DR Summary & High-LevelPoints](#the-tldr-summary--high-level...… [Continue reading](/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/)

#### [Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass (~15.5 Million Affected)](/video-download-uxss-exploit-detailed/ "Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass \(~15.5 Million Affected\)")

Published on February 22, 2019

#### [Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions](/kicking-the-rims-a-guide-for-securely-writing-and-auditing-chrome-extensions/ "Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions")

Published on June 12, 2018
