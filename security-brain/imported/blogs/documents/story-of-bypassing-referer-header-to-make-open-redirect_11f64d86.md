---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-22_story-of-bypassing-referer-header-to-make-open-redirect.md
original_filename: 2017-11-22_story-of-bypassing-referer-header-to-make-open-redirect.md
title: Story of bypassing Referer Header to make open redirect
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 11f64d86706d071a09f0088365219cf970ed0ba23dd27f446f0c2a43e5a91acf
text_sha256: 3fd18d989220eaf67b1ef438e6a122c72d90f46a8662da8006d51f3c68c5d743
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Story of bypassing Referer Header to make open redirect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-22_story-of-bypassing-referer-header-to-make-open-redirect.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `11f64d86706d071a09f0088365219cf970ed0ba23dd27f446f0c2a43e5a91acf`
- Text SHA256: `3fd18d989220eaf67b1ef438e6a122c72d90f46a8662da8006d51f3c68c5d743`


## Content

---
title: "Story of bypassing Referer Header to make open redirect"
url: "https://medium.com/@malcolmx0x/story-of-bypassing-referer-header-to-make-open-redirect-94f938b9d032"
authors: ["Mohammed Eldeeb (@malcolmx0x)"]
bugs: ["Open redirect"]
publication_date: "2017-11-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6042
scraped_via: "browseros"
---

# Story of bypassing Referer Header to make open redirect

Story of bypassing Referer Header to make open redirect
Mohammed Eldeeb
Follow
1 min read
·
Nov 22, 2017

104

3

Hi all,

today i will write about bypass Referer Header to make open redirect

i was testing private program and i was working on one of this program subdomains let’s say subdomain.domain.com

i run dirbuster to see if there is any interesting endpoint and i found some endpoints and let’s say it /endpoint after that i found that subdomain can redirect us to the main domain through this endpoint /endpoint/clkn/http/maindomain.com/

i tried to change the main domain to any other domain it was work but unfortunately was Referer Header protection to prevent this , i searched on google but i did not find anything after that i asked people on slack but no idea so i said to my self let’s try harder

Get Mohammed Eldeeb’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

i said to my self let’s try to put the Referer as the link that we will redirect to , i made this and deleted the Referer Header and WOW! It worked without Referer Header

now let’s try the url unfortunately if i changed anything on the link i got message We’re sorry, but the link you followed appears to be invalid.

after some tries i looked to this tweet https://twitter.com/EdOverflow/status/931862992643411975

and i put only one character so it was like this /endpoint/clkn/http/t-Ô-subdomain.domain.com/

and in response i got redirect to Location: http://t-?subdomain.domain.com/

woho we are in T Host now !

try harder .. you will get what you want

Thanks
