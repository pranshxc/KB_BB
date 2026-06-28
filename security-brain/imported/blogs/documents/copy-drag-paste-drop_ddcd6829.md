---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-04_copy-drag-paste-drop.md
original_filename: 2020-07-04_copy-drag-paste-drop.md
title: Copy Drag — Paste Drop
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: ddcd6829c509bfa14738030cc0781160a3ae29fe756cb233aee0cd76bbf7b704
text_sha256: e119fbb50508a8a5a0725f81818f0b1734bbe7b3fb77326297ee8e20b8d6cfb1
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Copy Drag — Paste Drop

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-04_copy-drag-paste-drop.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `ddcd6829c509bfa14738030cc0781160a3ae29fe756cb233aee0cd76bbf7b704`
- Text SHA256: `e119fbb50508a8a5a0725f81818f0b1734bbe7b3fb77326297ee8e20b8d6cfb1`


## Content

---
title: "Copy Drag — Paste Drop"
url: "https://medium.com/@renwa/copy-drag-paste-drop-2fd4613ad1d1"
authors: ["Renwa (@RenwaX23)"]
bugs: ["XSS"]
publication_date: "2020-07-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4442
scraped_via: "browseros"
---

# Copy Drag — Paste Drop

Copy Drag — Paste Drop
Renwa
Follow
2 min read
·
Jul 5, 2020

20

Press enter or click to view image in full size

This going to be a small write-up about XSS’ing some contexts that need user interactions by using drag and drop on modern apps, and i think im COVID-19 positive :)

On modern apps almost every website uses XFO deny so it’s impossible to frame the page and trick the user to drag and drop something to the framed page, so we have to find a new way to use some lesser known XSS cases.

Recently there was a nice research about copy-paste XSS https://research.securitum.com/the-curious-case-of-copy-paste/

The problem is that most of the bug bounty companies wouldn’t accept copy paste XSS so instead we can use drag and drop.

Get Renwa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Recently i made a silly XSS challenge to demonstrate this case

It’s a simple website with some content then in the bottom we have a WYSIWYG editor Michał already did a nice research on these editors and i have looked at bug bounty programs i saw many of these editors are still using vulnerable versions; mostly in forums.

In browsers we can override the dragged content and change it to anything we want so in my challenge we can trick the user to drag an image/text then redirect the user to the vulnerable, but the problem is the editor is in the bottom of the page.

For this we can use the new Chrome feature Scroll to Text Fragment so we can scroll the page down to where the editor is, after 2 seconds when the user drops the content it will be dropped inside the editor, solution:

https://renwax23.github.io/X/xschals4j.html

Press enter or click to view image in full size

Thanks to 
terjanq
 he should another technique to scroll the page, by opening a new window then changing its location.hash to an element ID so that the page will be focused and scrolled down to that element which is made by the editor.
