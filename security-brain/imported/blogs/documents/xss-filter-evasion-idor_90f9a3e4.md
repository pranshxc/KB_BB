---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-13_xss-filter-evasion-idor.md
original_filename: 2022-01-13_xss-filter-evasion-idor.md
title: XSS Filter Evasion + IDOR
category: documents
detected_topics:
- xss
- idor
- access-control
- command-injection
- csrf
- information-disclosure
tags:
- imported
- documents
- xss
- idor
- access-control
- command-injection
- csrf
- information-disclosure
language: en
raw_sha256: 90f9a3e415f96ab3385fc73a7577df765155740a0d4a3bb4fcbc90723797d82c
text_sha256: b0003ad76ea65c3cee7c48a5efbcacd73f90cb7f3eb0f47cf7656ef159e2e678
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# XSS Filter Evasion + IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-13_xss-filter-evasion-idor.md
- Source Type: markdown
- Detected Topics: xss, idor, access-control, command-injection, csrf, information-disclosure
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `90f9a3e415f96ab3385fc73a7577df765155740a0d4a3bb4fcbc90723797d82c`
- Text SHA256: `b0003ad76ea65c3cee7c48a5efbcacd73f90cb7f3eb0f47cf7656ef159e2e678`


## Content

---
title: "XSS Filter Evasion + IDOR"
url: "https://systemweakness.com/xss-filter-evasion-idor-3d4624758ff0"
authors: ["JM Sanchez / 0xEchidonut (@jmrcsnchz)"]
bugs: ["XSS", "IDOR"]
bounty: "800"
publication_date: "2022-01-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3009
scraped_via: "browseros"
---

# XSS Filter Evasion + IDOR

XSS Filter Evasion + IDOR
0xEchidonut
Follow
3 min read
·
Jan 13, 2022

151

1

Hi there. I’m JM Sanchez, a student, and a bug bounty hunter. After months of duplicate reports, I finally found a valid high severity bug.

The site that I’m testing offers an online payment integration system in which you can manage customers and issue them invoices. I reported many XSSs, CSRFs, and such but, all of them were dups.

While testing some of the site’s functionality, I came upon a URL like
/MerchantUser/create_customer/CUS-123456–A1B2C3

I immediately tested and found out that it’s vulnerable to IDOR attacks. I copy pasted the same link and opened it on another account. Even without authorization, I was able to view the customer details and edit them.

A 12 Character AlphaNumeric permutation isn’t really impossible to bruteforce but, it’s hella unrealistic.

For instance, if you have an extremely simple and common password that’s seven characters long (“abcdefg”), a pro could crack it in a fraction of a millisecond. Add just one more character (“abcdefgh”) and that time increases to five hours. Nine-character passwords take five days to break, 10-character words take four months, and 11-character passwords take 10 years. Make it up to 12 characters, and you’re looking at 200 years’ worth of security — not bad for one little letter. (https://www.betterbuys.com/estimating-password-cracking-times/)

It would take approx. 200 years to enumerate all possible and valid CustomerIDs. I held my findings for a while and focused on chaining this to another vulnerability and achieve its maximum severity

I looked for information disclosure bugs to enumerate CustomerIDs. Unfortunately, I found nothing. Before giving up, I tested the endpoint one more time for XSS

Exploitation

At this point, I realized that XSS in this endpoint is actually possible! I never tested for it because the filter auto removes html tags. I think it uses the strip_tags function in PHP. If we can’t use tags, then let’s not use tags.

After saving the changes in customer’s information, it is stored in the value attribute of <input>. I tried to escape the attribute with

“> escaped?

and I succeeded.

Press enter or click to view image in full size

It is now parsed as

Get 0xEchidonut’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<input name=”…” class=”…” value=””>escaped? “>

Next is to just add a javascript event handler on to it and inject js commands. But of course, there is a filter.

It removes all event handlers that are possible. Then I remembered, what if I combine the HTML tag with the event handler?

Press enter or click to view image in full size

I came up with a payload like

“ onmo<x>useover=”alert(document[‘cookie’])”>

The filter won’t see the onmouseover event handler, but only the html tag. It will be now saved as

“ onmouseover=”alert(document[‘cookie’])”>

I hovered my cursor and the javascript has been executed. Hooray!

I’m still not satisfied so I entered a payload that does not require user interaction

“ onf<x>ocus=”alert(document[‘cookie’])” autofocus”>

Puzzling them together

I got a stored XSS in the same endpoint that is vulnerable to IDOR. Since we can’t “guess” other user’s customerIDs, I used the IDOR to target them using XSS.

By creating a Customer with the above XSS payload as information, we can just copy the link and send it to our target. Once the target opens the link, we can execute arbitrary javascript on their browser. This can be escalated to account takeovers and stealing private information.

Reported: December 1, 2021

Triaged: January 11, 2022

Reward: $800
