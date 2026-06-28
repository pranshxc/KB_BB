---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-23_reflected-cross-site-scripting-on-redacted-program-bounty-750.md
original_filename: 2020-11-23_reflected-cross-site-scripting-on-redacted-program-bounty-750.md
title: 'Reflected Cross Site Scripting on REDACTED Program (Bounty: 750$)'
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
raw_sha256: 9aafd0a2ddf65848c1ca31d30d84378198b139feab32aeead521b84bde69b2e4
text_sha256: 73631d7ba0beef3f37bb351b38b2539938fe58796b6032177088c70d36cf4582
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected Cross Site Scripting on REDACTED Program (Bounty: 750$)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-23_reflected-cross-site-scripting-on-redacted-program-bounty-750.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `9aafd0a2ddf65848c1ca31d30d84378198b139feab32aeead521b84bde69b2e4`
- Text SHA256: `73631d7ba0beef3f37bb351b38b2539938fe58796b6032177088c70d36cf4582`


## Content

---
title: "Reflected Cross Site Scripting on REDACTED Program (Bounty: 750$)"
url: "https://medium.com/bugbountywriteup/reflected-cross-site-scripting-on-private-program-bounty-750-34cc67a931f1"
authors: ["can1337 (@canmustdie)"]
bugs: ["Reflected XSS"]
bounty: "750"
publication_date: "2020-11-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4109
scraped_via: "browseros"
---

# Reflected Cross Site Scripting on REDACTED Program (Bounty: 750$)

Reflected Cross Site Scripting on REDACTED Program (Bounty: 750$)
can1337
Follow
2 min read
·
Nov 23, 2020

248

2

Hi guys, this is my first English write-up.

Obviously, I discovered a bug but I was not sure exactly what caused it. So I said, I have to investigate this case!

I found this worth exploring because this site did not seem to be receiving an input from me. However, the <script> tag I added to the end of the URL was revealing some characters on the page. (like: "}}] )

But, how?

When I examined the source code, every value I added to the end of the URL was assigned to a JSON-generated variable. Then, I saw that the JSON data was put between<script> tag.

Get can1337’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Just like that:

At this point, all we have to do is close it using the </script> tag, then enter XSS payload.

( sorry for the blur :) )

Finally;

target.com/affected/url</script><img src=xss onerror=alert(1)>

And it’s fixed!

Be sure to check the value you add to the end of the URL in the source code, even if it does not appear to be receiving input from the user.

Thanks!!!

Twitter: https://twitter.com/canmustdie
