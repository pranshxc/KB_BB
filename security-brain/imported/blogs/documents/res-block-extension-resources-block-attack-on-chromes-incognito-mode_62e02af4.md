---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-16_res-block-extension-resources-block-attack-on-chromes-incognito-mode.md
original_filename: 2020-09-16_res-block-extension-resources-block-attack-on-chromes-incognito-mode.md
title: 'Res-block: Extension Resources Block Attack on Chrome’s Incognito Mode'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- cors
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- cors
- api-security
- supply-chain
language: en
raw_sha256: 62e02af4a45b648f05259987af86f24879db0f0e4d67c64cc7e8f3a44012044e
text_sha256: d90abffcd79497adf82c186adf2d733ff51c3ce1215a20587d2dd6290f5e384c
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Res-block: Extension Resources Block Attack on Chrome’s Incognito Mode

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-16_res-block-extension-resources-block-attack-on-chromes-incognito-mode.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, cors, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `62e02af4a45b648f05259987af86f24879db0f0e4d67c64cc7e8f3a44012044e`
- Text SHA256: `d90abffcd79497adf82c186adf2d733ff51c3ce1215a20587d2dd6290f5e384c`


## Content

---
title: "Res-block: Extension Resources Block Attack on Chrome’s Incognito Mode"
url: "https://medium.com/@0x48piraj/res-block-extension-resources-block-attack-on-chromes-incognito-mode-3a5ae8131142"
authors: ["Piyush Raj (@0x48piraj)"]
programs: ["Google"]
bugs: ["Browser hacking"]
publication_date: "2020-09-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4260
scraped_via: "browseros"
---

# Res-block: Extension Resources Block Attack on Chrome’s Incognito Mode

Res-block: Extension Resources Block Attack on Chrome’s Incognito Mode
Piyush Raj ~ Rex
Follow
4 min read
·
Sep 16, 2020

168

Press enter or click to view image in full size
Res-block Attack

This attack can be used to detect if victim is using incognito mode in latest version of Chrome (77.0.3865.90) by the time of discovery by me exactly a year ago in Sept 2019 by abusing web_accessible_resources. The research can be find over 0x48piraj/PwnHouse.

Anatomy of res-block attack

Sometimes developers share package resources of their Chrome extension, for example, images, HTML, CSS, or JavaScript and make them available to web pages. They do this via utilizing web_accessible_resources.

As per Chrome’s documentation,

An array of strings specifying the paths of packaged resources that are expected to be usable in the context of a web page. These paths are relative to the package root, and may contain wildcards. For example, an extension that injects a content script with the intention of building up some custom interface for example.com would allow any resources that interface requires (images, icons, style-sheets, scripts, etc.) as follows:

{
  ...
  "web_accessible_resources": [
  "images/*.png",
  "style/double-rainbow.css",
  "script/double-rainbow.js",
  "script/main.js",
  "templates/*"
  ],
  ...
}

More info can be found over Chrome’s Manifest — Web Accessible Resources documentation.

These resources then become available in a webpage via the URL chrome-extension://[PACKAGE-ID]/[PATH], which can be generated with the extension.getURL method. Allow-listed resources are served with appropriate CORS headers, so they're available via mechanisms like XHR.

The documentation goes on and states that some work has already been done previously focusing on different domain utilizing web accessible resources as the blob states:

Prior to manifest version 2 all resources within an extension could be accessed from any page on the web. This allowed a malicious website to fingerprint the extensions that a user has installed or exploit vulnerabilities (for example XSS bugs) within installed extensions. Limiting availability to only resources which are explicitly intended to be web accessible serves to both minimize the available attack surface and protect the privacy of users.

The Vulnerability

During my research, what I found interesting was that, these paths chrome-extension://[PACKAGE-ID]/[PATH] were not available to incognito mode, maybe it is because Chrome by default blocks extensions in incognito mode because it can't guarantee that the extensions aren't tracking one's data.

This actually opened a loophole. What if one scans for popular extensions which had web_accessible_resources parameter in their Manifest and then tries to access those one by one?

Testing the waters

Let’s test this with Wappalyzer chrome-extension as I know it has web_accessible_resources in it’s Manifest by looking at it’s source. I chose to go with this chrome extension because I’ve dealt it’s code-base in past during one of my other research which ended with me giving a talk at BSides Delhi 2019.

--SNIP--
  ],
  "web_accessible_resources": [
  "js/inject.js"
  ],
--SNIP--

The path seems to be js/inject.js, now to find the [PACKAGE-ID], we can just visit chrome://extensions, switch to Developer mode, see extensive details about extensions.

Press enter or click to view image in full size

NOTE: As the [PACKAGE-ID] is constant through-out, it is a reliable attack vector.

Final Payload

chrome-extension://gppongmhjkpfnbhagpmjfkannfbllamg/js/inject.js

Press enter or click to view image in full size

As expected, now, let’s test this over incognito mode,

Press enter or click to view image in full size

Aha! It shows an error with code ERR_BLOCKED_BY_CLIENT or say, Failed to load resource: net::ERR_BLOCKED_BY_CLIENT.

Get Piyush Raj ~ Rex’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To make a proof-of-concept exploit, we can just use <script> with src tag to load target resource and,

if it loads successfully, we’re not into incognito mode.
if the page can’t load, we definitely are.

POC (proof-of-concept) for Wappalyzer chrome-extension installed,

<html><body>
<script src="chrome-extension://gppongmhjkpfnbhagpmjfkannfbllamg/js/inject.js"></script>
</body><html>

We can see the error again, programmatically,

So now, we just need to detect this error to tell if an user is using Incognito mode or not. We can use any of the two events here to detect the Incognito mode:

onload – successful load.
onerror – an error occurred.
Chaining for the win

This bug got far more interesting when I found web_accessible_resources in chrome-extensions which come pre-installed in every Chrome web-browser.

This discovery makes this bug very exploitable.

The dump of pre-installed Chrome extensions on latest version 77.0.3865.90 can be found over here.

The chrome-extensions which have web accessible resources:

Google Docs Offline Extension (resblock/vuln-manifests/google-docs-manifest.json)
Chrome Media Router (Chromecast™) Extension (resblock/vuln-manifests/chromecast-manifest.json)

You can find the final proof-of-concept exploit over 0x48piraj/PwnHouse/../resblock/res-block-poc.html.

Demo
Press enter or click to view image in full size

Pwned!
