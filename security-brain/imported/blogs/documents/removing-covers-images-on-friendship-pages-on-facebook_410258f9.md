---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-09-25_removing-covers-images-on-friendship-pages-on-facebook.md
original_filename: 2013-09-25_removing-covers-images-on-friendship-pages-on-facebook.md
title: Removing Covers Images on Friendship Pages, on Facebook
category: documents
detected_topics:
- access-control
- xss
- command-injection
- otp
- automation-abuse
- cloud-security
tags:
- imported
- documents
- access-control
- xss
- command-injection
- otp
- automation-abuse
- cloud-security
language: en
raw_sha256: 410258f9a5778587a62a0dbf16d8bf746e32cd4c20c0f18563a11e3146760595
text_sha256: e1d8e0768925afb47a5954123b58e458c83d83089ea2288f8e529204eeb8939d
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Removing Covers Images on Friendship Pages, on Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-09-25_removing-covers-images-on-friendship-pages-on-facebook.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, otp, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `410258f9a5778587a62a0dbf16d8bf746e32cd4c20c0f18563a11e3146760595`
- Text SHA256: `e1d8e0768925afb47a5954123b58e458c83d83089ea2288f8e529204eeb8939d`


## Content

---
title: "Removing Covers Images on Friendship Pages, on Facebook"
page_title: "Removing Covers Images on Friendship Pages, on Facebook – Jack"
url: "https://whitton.io/articles/removing-covers-images-on-friendship-pages-on-facebook/"
final_url: "https://whitton.io/articles/removing-covers-images-on-friendship-pages-on-facebook/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2013-09-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6397
---

# [Removing Covers Images on Friendship Pages, on Facebook](https://whitton.io/articles/removing-covers-images-on-friendship-pages-on-facebook/ "Removing Covers Images on Friendship Pages, on Facebook")

## September 25, 2013

__Reading time ~1 minute

This is a quick post about a simple bug I found on Friendship Pages on Facebook. (Note: Not nearly as cool as a [full account takeover](http://blog.fin1te.net/post/53949849983/hijacking-a-facebook-account-with-sms), however!)

[Friendship Pages](https://www.facebook.com/help/220629401299124) show you how two users on Facebook are connected, with posts and photos they’re both tagged in, events they’ve both attended and common friends. On these pages, you’re given the option to upload a cover photo (like you would on your profile, or an event).

[ ![](/images/facebookcover/f-c-1-1.png) ](/images/facebookcover/f-c-1-1.png)

### Removing A Cover

The cover photo on someones friendship page, we can remove from _any_ account.

First, we need the `friendship_id`, which can be obtained with an AJAX call to `/ajax/timeline/friendship_cover/selector`, where `profile_id` is one user and `friend_id` is another.

[ ![](/images/facebookcover/f-c-2-1.png) ](/images/facebookcover/f-c-2-1.png)

Using this `friendship_id` we make an AJAX call to `/ajax/timeline/friendship_cover/remove`, placing the value into the `profile_id` parameter.

[ ![](/images/facebookcover/f-c-4-1.png) ](/images/facebookcover/f-c-4-1.png)

Refresh the page, and it’s disappeared.

[ ![](/images/facebookcover/f-c-5-1.png) ](/images/facebookcover/f-c-5-1.png)

### Fix

Now, you can only remove your own cover.

### Timeline

  * 29th August 2013 - Reported
  * 2nd September 2013 - Acknowledgment of Report
  * 2nd September 2013 - Issue Fixed

[facebook](https://whitton.io/tags/#facebook "Pages tagged facebook")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[websec](https://whitton.io/tags/#websec "Pages tagged websec")[authentication](https://whitton.io/tags/#authentication "Pages tagged authentication") Updated on September 25, 2013 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/removing-covers-images-on-friendship-pages-on-facebook/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/removing-covers-images-on-friendship-pages-on-facebook/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/removing-covers-images-on-friendship-pages-on-facebook/ "Share on Google Plus")

[Read More](https://whitton.io/articles/hijacking-a-facebook-account-with-sms/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016
