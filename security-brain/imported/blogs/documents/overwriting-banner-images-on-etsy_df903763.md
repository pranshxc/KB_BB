---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-05-21_overwriting-banner-images-on-etsy.md
original_filename: 2013-05-21_overwriting-banner-images-on-etsy.md
title: Overwriting Banner Images on Etsy
category: documents
detected_topics:
- access-control
- xss
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- access-control
- xss
- command-injection
- otp
- cloud-security
language: en
raw_sha256: df9037635e53c430eb1ac6647e0d6a225d00afbc4f294e74ff561583ed79e01f
text_sha256: ab643c54c18c8ef6443fe386d555f94e42d789e2b675ad8bb186a29391b27eac
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Overwriting Banner Images on Etsy

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-05-21_overwriting-banner-images-on-etsy.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `df9037635e53c430eb1ac6647e0d6a225d00afbc4f294e74ff561583ed79e01f`
- Text SHA256: `ab643c54c18c8ef6443fe386d555f94e42d789e2b675ad8bb186a29391b27eac`


## Content

---
title: "Overwriting Banner Images on Etsy"
page_title: "Overwriting Banner Images on Etsy – Jack"
url: "https://whitton.io/articles/overwriting-banner-images-on-etsy/"
final_url: "https://whitton.io/articles/overwriting-banner-images-on-etsy/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Etsy"]
bugs: ["Broken authorization"]
publication_date: "2013-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6405
---

# [Overwriting Banner Images on Etsy](https://whitton.io/articles/overwriting-banner-images-on-etsy/ "Overwriting Banner Images on Etsy")

## May 21, 2013

__Reading time ~1 minute

When you create a shop on [Etsy](https://www.etsy.com), you can upload an image to be used as a banner.

The upload form in the administration section stops you changing the shop to one you don’t control, as expected.

[ ![](/images/etsybanner/etsy-banner-1.png) ](/images/etsybanner/etsy-banner-1.png)

There is, however, an AJAX end-point which can also be used to upload these images. This _doesn’t_ check you’re the owner on upload.

[ ![](/images/etsybanner/etsy-banner-2-1.png) ](/images/etsybanner/etsy-banner-2-1.png)

We can easily upload any image we want onto any shop we want. This could be used to damage a business’s reputation, or like what happened on the [Silk Road](http://allthingsvice.com/2013/01/23/whos-got-it-in-for-the-silk-road/), upload a banner which prompts any prospective customers to send any orders and payments to an email address we control.

[ ![](/images/etsybanner/etsy-banner-3.png) ](/images/etsybanner/etsy-banner-3.png)

### Fix

Etsy fixed this in a simple way - they now check you’re the owner on upload.

[ ![](/images/etsybanner/etsy-banner-4.png) ](/images/etsybanner/etsy-banner-4.png) [etsy](https://whitton.io/tags/#etsy "Pages tagged etsy")[websec](https://whitton.io/tags/#websec "Pages tagged websec")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[authentication](https://whitton.io/tags/#authentication "Pages tagged authentication") Updated on May 21, 2013 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/overwriting-banner-images-on-etsy/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/overwriting-banner-images-on-etsy/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/overwriting-banner-images-on-etsy/ "Share on Google Plus")

[Read More](https://whitton.io/articles/stealing-facebook-access-tokens-with-a-double-submit/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016
