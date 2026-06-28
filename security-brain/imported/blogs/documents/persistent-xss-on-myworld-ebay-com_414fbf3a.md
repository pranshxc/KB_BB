---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-01-27_persistent-xss-on-myworldebaycom.md
original_filename: 2013-01-27_persistent-xss-on-myworldebaycom.md
title: Persistent XSS on myworld.ebay.com
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- csrf
- api-security
language: en
raw_sha256: 414fbf3a1963c6259e2fd58d12463cb2f19002ee0ee9f8870a734adb65ab3c66
text_sha256: a5295d33ac69637f8e2021de7cd8421090d3ee9df21d9d8c1317eb08389aee03
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Persistent XSS on myworld.ebay.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-01-27_persistent-xss-on-myworldebaycom.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, csrf, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `414fbf3a1963c6259e2fd58d12463cb2f19002ee0ee9f8870a734adb65ab3c66`
- Text SHA256: `a5295d33ac69637f8e2021de7cd8421090d3ee9df21d9d8c1317eb08389aee03`


## Content

---
title: "Persistent XSS on myworld.ebay.com"
page_title: "Persistent XSS on myworld.ebay.com – Jack"
url: "https://whitton.io/archive/persistent-xss-on-myworld-ebay-com/"
final_url: "https://whitton.io/archive/persistent-xss-on-myworld-ebay-com/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Ebay"]
bugs: ["XSS"]
publication_date: "2013-01-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6412
---

# [Persistent XSS on myworld.ebay.com](https://whitton.io/archive/persistent-xss-on-myworld-ebay-com/ "Persistent XSS on myworld.ebay.com")

## January 27, 2013

__Reading time ~1 minute

On eBay, the [My World](http://myworld.ebay.com/) section allows users and businesses to construct a profile, with shipping information, returns policies, and also blocks of arbitrary text specified by the user.

All of the input boxes have a note below saying that you can’t add HTML, so I was interested to see how it checks/prevents you from entering any.

[ ![](/images/ebayxss/ebay-xss-0.png) ](/images/ebayxss/ebay-xss-0.png)

I tried adding in some tags, <a>, <span>, <script>, however they’re all filtered out. In addition to this, you can’t use double quotes (so you can’t break out of attributes). However, it turns out they use a blacklist of HTML tags. I tried a deprecated tag, <plaintext>, and to my surprise it passed through fine.

[ ![](/images/ebayxss/ebay-xss-1.png) ](/images/ebayxss/ebay-xss-1.png)

I don’t like the plaintext tag, as it caused the rest of the page to render horribly (as expected), so I tried a few more. <fn> and <credit> both passed through too.

Now we have a way to inject HTML, I added an onhover event to the injected element. Without the use of quotes, we can use the [String.fromCharCode](https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/String/fromCharCode) function and eval to load an external script - this is necessary as the character limit on the textbox is 1k.

[ ![](/images/ebayxss/ebay-xss-2.png) ](/images/ebayxss/ebay-xss-2.png)

From this point onwards, it is trivial to weaponise this into a working worm. We get the username from the element _#gh_uh_ , construct a form post to the bio page and add ourselves to the logged in users bio.

[ ![](/images/ebayxss/ebay-xss-3.png) ](/images/ebayxss/ebay-xss-3.png)

There is no CSRF protection on this form, which makes it even easier as we don’t need to scrape a token from anywhere.

In addition to this, all of the cookies are stored under *.ebay.com, and they’re _not_ using [HTTPOnly](https://en.wikipedia.org/wiki/HTTP_cookie#Secure_and_HttpOnly) so we can steal this too.

#### Fix

eBay responded by encoding all HTML entities on output.

[ebay](https://whitton.io/tags/#ebay "Pages tagged ebay")[websec](https://whitton.io/tags/#websec "Pages tagged websec")[bug-bounty](https://whitton.io/tags/#bug-bounty "Pages tagged bug-bounty")[xss](https://whitton.io/tags/#xss "Pages tagged xss") Updated on January 27, 2013 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/archive/persistent-xss-on-myworld-ebay-com/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/archive/persistent-xss-on-myworld-ebay-com/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/archive/persistent-xss-on-myworld-ebay-com/ "Share on Google Plus")

[Read More](https://whitton.io/archive/vodafone-no-pasting-into-password-fields/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016
