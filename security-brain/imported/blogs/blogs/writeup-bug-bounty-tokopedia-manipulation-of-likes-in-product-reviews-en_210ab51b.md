---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-15_writeupbug-bountytokopedia-manipulation-of-likes-in-product-reviews-en.md
original_filename: 2019-11-15_writeupbug-bountytokopedia-manipulation-of-likes-in-product-reviews-en.md
title: '[Writeup][Bug Bounty][Tokopedia] Manipulation of Likes in Product Reviews
  [EN]'
category: blogs
detected_topics:
- idor
- command-injection
- password-reset
- rate-limit
tags:
- imported
- blogs
- idor
- command-injection
- password-reset
- rate-limit
language: en
raw_sha256: 210ab51b1c596267cbee614c2e047df54de98119c8f5e069b60cd34fa98a8403
text_sha256: 04e7dea733ca7bdbc86415f092837f2c7f54907fab3ff235aec01c9df5d29ecb
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# [Writeup][Bug Bounty][Tokopedia] Manipulation of Likes in Product Reviews [EN]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-15_writeupbug-bountytokopedia-manipulation-of-likes-in-product-reviews-en.md
- Source Type: markdown
- Detected Topics: idor, command-injection, password-reset, rate-limit
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `210ab51b1c596267cbee614c2e047df54de98119c8f5e069b60cd34fa98a8403`
- Text SHA256: `04e7dea733ca7bdbc86415f092837f2c7f54907fab3ff235aec01c9df5d29ecb`


## Content

---
title: "[Writeup][Bug Bounty][Tokopedia] Manipulation of Likes in Product Reviews [EN]"
page_title: "[Writeup][Bug Bounty][Tokopedia] Manipulation of Likes in Product Reviews [EN] | Home"
url: "https://fadhilthomas.github.io/post/bug-bounty-tokopedia-01-en/"
final_url: "https://fadhilthomas.github.io/post/bug-bounty-tokopedia-01-en/"
authors: ["Muhammad Thomas Fadhila Yahya (@fadhilthomas)"]
programs: ["Tokopedia"]
bugs: ["IDOR"]
bounty: "135"
publication_date: "2019-11-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4941
---

[Home](https://fadhilthomas.github.io/) » [Posts](https://fadhilthomas.github.io/post/)

# [Writeup][Bug Bounty][Tokopedia] Manipulation of Likes in Product Reviews [EN]

November 15, 2019 · 2 min · fadhilthomas

Table of Contents

  * Affected Endpoint
  * Impact
  * Steps to Reproduce
  * Timeline
  * References

![alt text](/tokopedia01/img1.jpg)

Before starting, IDOR is Insecure Direct Object Reference, hereinafter referred to as IDOR, is a condition in which users can access an object without passing the access rights check. (OWASP, 2019)

With IDOR, a user can access, change, and delete data. This makes IDOR a very dangerous security hole. Please note, the bug discussed in this writeup has been patched by Tokopedia and screenshots will be censored because of PII.

* * *

## Affected Endpoint#
  
  
  https://ws.tokopedia.com/reputationapp/review/api/v1/likedislike
  

* * *

## Impact#

Manipulation of number of likes in Product Reviews

* * *

## Steps to Reproduce#

  * Log in to your Tokopedia account and open a product review page.
  * Intercept the connection request, click the like a review button. ![alt text](https://github.com/fadhilthomas/fadhilthomas.github.io/raw/master/assets/images/tokopedia01/img2.jpg)
  * In the intercepted connection request, there are several parameters, such as: **product_id** is the product id being reviewed, **shop_id** is a shop id, and **user_id** is the user id who likes. ![alt text](https://github.com/fadhilthomas/fadhilthomas.github.io/raw/master/assets/images/tokopedia01/img3.jpg)
  * Forward request, then get a success reply.
  * To try to manipulate the number of likes is by replacing the user id with another user id, without the need for user interaction. Change user_id with another user id and delete some parameters to bypass user authentication. ![alt text](https://github.com/fadhilthomas/fadhilthomas.github.io/raw/master/assets/images/tokopedia01/img4.jpg)
  * Forward request. ![alt text](https://github.com/fadhilthomas/fadhilthomas.github.io/raw/master/assets/images/tokopedia01/img5.jpg)
  * The number of likes has increased. ![alt text](https://github.com/fadhilthomas/fadhilthomas.github.io/raw/master/assets/images/tokopedia01/img6.jpg) ![alt text](https://github.com/fadhilthomas/fadhilthomas.github.io/raw/master/assets/images/tokopedia01/img7.jpg)

* * *

## Timeline#

  * 23 Feb 2019 : Reported to Tokopedia.
  * 23 Feb 2019 : Tokopedia received the report.
  * 25 Feb 2019 : Tokopedia declared valid with Severity Medium.
  * 01 Apr 2019 : The bug has been fixed.
  * 22 May 2019 : Tokopedia sent 1.9 million IDR or $135 as reward.

* * *

## References#

  1. <https://www.owasp.org/index.php/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet>
  2. <https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_(OTG-AUTHZ-004)>
  3. <https://www.bugcrowd.com/how-to-find-idor-insecuredirect-object-reference-vulnerabilities-for-large-bountyrewards/>

  * [bugbounty](https://fadhilthomas.github.io/tags/bugbounty/)
  * [tokopedia](https://fadhilthomas.github.io/tags/tokopedia/)
  * [writeup](https://fadhilthomas.github.io/tags/writeup/)

[« Prev Page  
[Writeup][Bug Bounty][Redacted] No Rate Limit in Forgot Password [ID]](https://fadhilthomas.github.io/post/bug-bounty-redacted-01/) [Next Page »  
[Writeup][Bug Bounty][Tokopedia] Manipulasi Jumlah Likes di Ulasan Produk [ID]](https://fadhilthomas.github.io/post/bug-bounty-tokopedia-01/)

[](https://twitter.com/intent/tweet/?text=%5bWriteup%5d%5bBug%20Bounty%5d%5bTokopedia%5d%20Manipulation%20of%20Likes%20in%20Product%20Reviews%20%5bEN%5d&url=https%3a%2f%2ffadhilthomas.github.io%2fpost%2fbug-bounty-tokopedia-01-en%2f&hashtags=bugbounty%2ctokopedia%2cwriteup)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2ffadhilthomas.github.io%2fpost%2fbug-bounty-tokopedia-01-en%2f&title=%5bWriteup%5d%5bBug%20Bounty%5d%5bTokopedia%5d%20Manipulation%20of%20Likes%20in%20Product%20Reviews%20%5bEN%5d&summary=%5bWriteup%5d%5bBug%20Bounty%5d%5bTokopedia%5d%20Manipulation%20of%20Likes%20in%20Product%20Reviews%20%5bEN%5d&source=https%3a%2f%2ffadhilthomas.github.io%2fpost%2fbug-bounty-tokopedia-01-en%2f)[](https://reddit.com/submit?url=https%3a%2f%2ffadhilthomas.github.io%2fpost%2fbug-bounty-tokopedia-01-en%2f&title=%5bWriteup%5d%5bBug%20Bounty%5d%5bTokopedia%5d%20Manipulation%20of%20Likes%20in%20Product%20Reviews%20%5bEN%5d)[](https://facebook.com/sharer/sharer.php?u=https%3a%2f%2ffadhilthomas.github.io%2fpost%2fbug-bounty-tokopedia-01-en%2f)[](https://api.whatsapp.com/send?text=%5bWriteup%5d%5bBug%20Bounty%5d%5bTokopedia%5d%20Manipulation%20of%20Likes%20in%20Product%20Reviews%20%5bEN%5d%20-%20https%3a%2f%2ffadhilthomas.github.io%2fpost%2fbug-bounty-tokopedia-01-en%2f)[](https://telegram.me/share/url?text=%5bWriteup%5d%5bBug%20Bounty%5d%5bTokopedia%5d%20Manipulation%20of%20Likes%20in%20Product%20Reviews%20%5bEN%5d&url=https%3a%2f%2ffadhilthomas.github.io%2fpost%2fbug-bounty-tokopedia-01-en%2f)
