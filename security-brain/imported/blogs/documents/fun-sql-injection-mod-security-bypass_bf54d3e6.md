---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-16_fun-sql-injection-mod_security-bypass.md
original_filename: 2021-04-16_fun-sql-injection-mod_security-bypass.md
title: Fun sql injection — mod_security bypass
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: bf54d3e61ac25341d31e376b17788a178d8e45b95e7296679da35890f78c5c51
text_sha256: 4a542f297bacb412277a9c37f9e30985f6080580a22f9eb1f69550853beb84f0
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Fun sql injection — mod_security bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-16_fun-sql-injection-mod_security-bypass.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `bf54d3e61ac25341d31e376b17788a178d8e45b95e7296679da35890f78c5c51`
- Text SHA256: `4a542f297bacb412277a9c37f9e30985f6080580a22f9eb1f69550853beb84f0`


## Content

---
title: "Fun sql injection — mod_security bypass"
url: "https://infosecwriteups.com/fun-sql-injection-mod-security-bypass-644b54b0c445"
authors: ["_Y000_ (@_Y000_)"]
bugs: ["SQL injection"]
publication_date: "2021-04-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3738
scraped_via: "browseros"
---

# Fun sql injection — mod_security bypass

Member-only story

Fun sql injection — mod_security bypass
_Y000_
Follow
4 min read
·
Apr 16, 2021

169

1

In this writing I would like to show you a somewhat peculiar case with which I came across testing a website.

This is an sql injection where I could bypass the “mod_security” waf.
When I start the sql injection test I realize that the website is using that waf.

We get the error when using a simple:

site/ejemplo?parameter=-1+union+selec+1,2,3,4,5,6,7+--+

Now, I’m not going to lie to you, just by encoding the payload with comments, I was able to bypass the waf filter.

site/ejemplo?parameter=-1+/*!50000union*/+/*!50000selec*/+1,2,3,4,5,6,7+--+
Press enter or click to view image in full size

We can see that one of the vulnerable columns is number four.

But like all a lover of sql injections I decided not to leave it like that and try other methods, other payloads .. After many tests and failed mixed payloads.

I ended up trying this:

AND mod(29,9)+div+@a:=(concat(database(),"--","_Y000!_"))+UNION+DISTINCTROW+SELECT+1,2,3,@a,5,6,7

Now what is this all about?

we have:

"AND" = The AND operator returns a record if all conditions separated by AND are TRUE.
"mod(29,9)" = The mod function is to make a…
