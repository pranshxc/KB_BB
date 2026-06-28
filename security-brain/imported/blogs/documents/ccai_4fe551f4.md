---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-11_ccai.md
original_filename: 2023-03-11_ccai.md
title: CCAI
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
raw_sha256: 4fe551f48d2016434f9698afdba7ad75d4b593ab9ddd8ad8a9d2445a0dc75563
text_sha256: 46c9c38f0b6ab425ed7c956d72270ed06f6fc148ad45f7f609a52bf56dba516a
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# CCAI

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-11_ccai.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `4fe551f48d2016434f9698afdba7ad75d4b593ab9ddd8ad8a9d2445a0dc75563`
- Text SHA256: `46c9c38f0b6ab425ed7c956d72270ed06f6fc148ad45f7f609a52bf56dba516a`


## Content

---
title: "CCAI"
page_title: "CCAI | Writeups"
url: "https://ndevtk.github.io/writeups/2023/03/11/ccai/"
final_url: "https://ndevtk.github.io/writeups/2023/03/11/ccai/"
authors: ["NDevTK (@ndevtk)"]
programs: ["Google"]
bugs: ["XSS"]
publication_date: "2023-03-11"
added_date: "2023-06-12"
source: "pentester.land/writeups.json"
original_index: 1390
---

# [Writeups](https://ndevtk.github.io/writeups/)

[Contact Center AI (CCAI)](https://cloud.google.com/solutions/contact-center-ai-platform) is a Contact Center as a Service platform from Google Cloud based of [UJET](https://ujet.cx/)  
The following was done as part of a [VRP grant](https://www.google.com/about/appsecurity/research-grants/) of $500, later increased by $1337

# Agent XSS

On the agents control panel there was an iframe with the location controlled by the URL parameter `cobrowseDomain`, So you could get an XSS by navigating it to a `javascript:` URL… also no embedding protection.
  
  
  let f = document.createElement('iframe');
  f.hidden = true;
  f.src =
  'https://something.uc1.ccaiplatform.com/agent/?type=popup&popup=cobrowse&cobrowseDomain=javascript:alert(window.origin);%2F%2F';
  document.body.appendChild(f);
  

# Client XSS

Using the chat message feature of Cloud Contact Center an agent could XSS the user on https://websdk.ujet.co by messaging `https://"onmousemove="alert(window.origin)"`  
This could also be done by setting a custom “Waiting for Agent Assignment Message” like `<img src=x onerror=alert(window.origin)>`  
Because the [SDK](https://cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en?hl=en) used a shared origin of `https://websdk.ujet.co` to render all chat sessions from Cloud Contact Center,  
Any website with there own chat could hijack a different websites chat session via the window opener.  
The origin was also trusted by [Cobrowse](https://cobrowse.io/) which is a feature of the SDK.

# Timeline

Reported agent xss on Nov 10, 2022 02:13AM (P2/S2)  
Marked as fixed on Jan 19, 2023 02:00AM  
Reported client xss on Nov 14, 2022 12:25PM (P2/S2)  
Blamed UJET on Nov 14, 2022 03:30PM  
Marked as fixed on Mar 10, 2023 07:10AM  
“cannot provide monetary compensation for CCAI errors reported under the grant” on Apr 18, 2023 10:55AM  
Swag rewarded on Apr 19, 2023 01:55PM ![Chat](https://ndevtk.github.io/writeups/chat.png)

[Improve this page](https://github.com/NDevTK/writeups/edit/main/_posts/2023-03-11-ccai.md) Default Random Basic Shader Wallpapers Chrome Cast Surveillance Chromium Advisories Side Channel Echo Grove ParentalControlLock Light Cyberpunk Code Matrix Blueprint Redacted Glitch Old Terminal Gradient Comic Base64 Emoji Minecraft Flip 🦆 Rainbow text Typoifier Summarizer AI Audio Spoof Oceanic Depths Retro Gamification NoScript
