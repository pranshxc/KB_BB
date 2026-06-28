---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-26_google-xss.md
original_filename: 2022-07-26_google-xss.md
title: Google XSS
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
raw_sha256: 65a190854da428a064fe956eff42cf099ade4daa97e5ccb0ff426b862c3e3867
text_sha256: ac2491434e54146a551cf932091baf2346730d4ec8caa820d5400ca9b778b373
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Google XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-26_google-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `65a190854da428a064fe956eff42cf099ade4daa97e5ccb0ff426b862c3e3867`
- Text SHA256: `ac2491434e54146a551cf932091baf2346730d4ec8caa820d5400ca9b778b373`


## Content

---
title: "Google XSS"
page_title: "Google XSS | Writeups"
url: "https://ndevtk.github.io/writeups/2022/07/26/google-xss/"
final_url: "https://ndevtk.github.io/writeups/2022/07/26/google-xss/"
authors: ["NDevTK (@ndevtk)"]
programs: ["Google"]
bugs: ["XSS"]
bounty: "8,133.70"
publication_date: "2022-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2392
---

# [Writeups](https://ndevtk.github.io/writeups/)

# Google DevSite XSS (cloud.google.com, developers.google.com) $3133.70

Due to a vulnerability in the server-side implementation of `<devsite-language-selector>` part of the URL was reflected as html so it was possible to get XSS on the origins using that component from the 404 page.  
This was found using [DalFox](https://dalfox.hahwul.com/docs/home/) which kept finding the same bug due to it being the “not found” page.

https://developers.google.com/foo%22%3E%3Cimg%20src=x%3E%3C/a%3E%3C/li%3E%3C/ul%3E%3C/devsite-language-selector%3E%3Ch1%3E%3Cscript%3Ealert(document.domain)%3C/script%3E/a https://cloud.google.com/foo%22%3E%3Cimg%20src=x%3E%3C/a%3E%3C/li%3E%3C/ul%3E%3C/devsite-language-selector%3E%3Ch1%3E%3Cscript%3Ealert(document.domain)%3C/script%3E/a

# Google Play XSS (play.google.com) $5000

On the search page of google play console vulnerable code was run when the search resulted in an error.  
Getting an error was simple as doing `/?search=&` and because `window.location` includes the hash which never encodes `'` it’s possible to escape the href context and set other html attributes, unlike the DevSite XSS this is prevented by the CSP but was still awarded more by the panel.
  
  
  b.innerHTML = b.innerHTML.replace(
  /({query})/g,
  "<a href='" + window.location + "'>" + a.g + '</a>'
  );
  

https://play.google.com/console/about/search-results/?search=&#’onclick=alert(document.domain)//

The writeups are referenced on [PortSwigger](https://portswigger.net/daily-swig/xss-vulnerabilities-in-google-cloud-google-play-could-lead-to-account-hijacks)

[Improve this page](https://github.com/NDevTK/writeups/edit/main/_posts/2022-07-26-google-xss.md) Default Random Basic Shader Wallpapers Chrome Cast Surveillance Chromium Advisories Side Channel Echo Grove ParentalControlLock Light Cyberpunk Code Matrix Blueprint Redacted Glitch Old Terminal Gradient Comic Base64 Emoji Minecraft Flip 🦆 Rainbow text Typoifier Summarizer AI Audio Spoof Oceanic Depths Retro Gamification NoScript
