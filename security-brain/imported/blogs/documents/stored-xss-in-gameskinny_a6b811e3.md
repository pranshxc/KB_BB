---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-03_stored-xss-in-gameskinny.md
original_filename: 2018-08-03_stored-xss-in-gameskinny.md
title: Stored XSS in GameSkinny
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
raw_sha256: a6b811e36a5a273560435c6e6775b2105c6c30503015517d6ffcb6550d16eb5e
text_sha256: 11ae330d12b7532e4739e5cf57ae44c01775dfc5cecb7ac6d56f26f5789d81f6
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in GameSkinny

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-03_stored-xss-in-gameskinny.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `a6b811e36a5a273560435c6e6775b2105c6c30503015517d6ffcb6550d16eb5e`
- Text SHA256: `11ae330d12b7532e4739e5cf57ae44c01775dfc5cecb7ac6d56f26f5789d81f6`


## Content

---
title: "Stored XSS in GameSkinny"
url: "https://medium.com/@friendly_/stored-xss-in-gameskinny-aa26c6a6ae40"
authors: ["Friendly (@SkeletorKeys)"]
programs: ["GameSkinny"]
bugs: ["Stored XSS"]
publication_date: "2018-08-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5775
scraped_via: "browseros"
---

# Stored XSS in GameSkinny

Stored XSS in GameSkinny
Friendly
Follow
2 min read
·
Aug 3, 2018

116

1

After weeks and weeks of e-mailing GameSkinny and tweeting at them to fix their security issues, they decided to not answer me (I think). That is very unfortunate. I also decided to also remove my tweets towards them as well as it didn’t seem to reach out to them.

Today I have decided to release that to the public (full disclosure) as it still works.

Steps to Reproduce the stored XSS:

Go to: http://gameskinny.com and make an account.

Press enter or click to view image in full size

Next we visit https://www.gameskinny.com/post/edit to make a thread or article — whichever you prefer to call it.

Now we insert our payload: “><svg/onload=alert(1)> ” and it should look a little something like this:

Press enter or click to view image in full size

After that, scroll to the bottom, then click “Save your changes” and click the preview button.

Get Friendly’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

…. We get the famous confirm(1) to popup!

Press enter or click to view image in full size

Gif of the POC:

Press enter or click to view image in full size

If you wanted to do malicious harm, or grab information that you weren’t suppose to have, then you would use a proper payload. I won’t be sharing that here — SORRY!

You can share your drafts with registered users who will be able to see your article and they would see the XSS — or get executed on. You can also send this in to the Editors by clicking “Send to editors” and executing an XSS script on them, which would hijack their cookies or sessions to do malicious activity.

Once again, this post is NOT meant to do anything harmful to the website. I am just a security researcher who is trying to help secure your website — other websites as well.

I hope http://gameskinny.com does fix this issue in the future (hope very soon) to secure their users information.

If you have any questions or comments, feel free to message me on Twitter @Skeletorkeys

Thanks for reading.
