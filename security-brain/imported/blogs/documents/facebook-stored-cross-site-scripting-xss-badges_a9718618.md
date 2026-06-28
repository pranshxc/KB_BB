---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-06-16_facebook-stored-cross-site-scripting-xss-badges.md
original_filename: 2014-06-16_facebook-stored-cross-site-scripting-xss-badges.md
title: Facebook – Stored Cross-Site Scripting (XSS) – Badges
category: documents
detected_topics:
- xss
- clickjacking
- command-injection
- otp
- csrf
tags:
- imported
- documents
- xss
- clickjacking
- command-injection
- otp
- csrf
language: en
raw_sha256: a9718618e0d45ce90d674d4b9990abfdb306f8b8a2c7bc9d146cee2909ee4acf
text_sha256: 8399855c8e566bd6b82f4c9f7be8a09017ce9189dd2eb11e44a3360d7cecc126
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook – Stored Cross-Site Scripting (XSS) – Badges

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-06-16_facebook-stored-cross-site-scripting-xss-badges.md
- Source Type: markdown
- Detected Topics: xss, clickjacking, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `a9718618e0d45ce90d674d4b9990abfdb306f8b8a2c7bc9d146cee2909ee4acf`
- Text SHA256: `8399855c8e566bd6b82f4c9f7be8a09017ce9189dd2eb11e44a3360d7cecc126`


## Content

---
title: "Facebook – Stored Cross-Site Scripting (XSS) – Badges"
page_title: "Facebook – Stored Cross-Site Scripting (XSS) – Badges | ziot"
url: "https://buer.haus/2014/06/16/facebook-stored-cross-site-scripting-xss-badges/"
final_url: "https://buer.haus/2014/06/16/facebook-stored-cross-site-scripting-xss-badges/"
authors: ["Brett Buerhaus (@bbuerhaus)"]
programs: ["Meta / Facebook"]
bugs: ["Stored XSS"]
publication_date: "2014-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6369
---

# Facebook – Stored Cross-Site Scripting (XSS) – Badges

June 16, 2014February 25, 2024

The Facebook badges page was vulnerable to stored Cross-Site Scripting (XSS). This was initially reported back in August 2013, but due to communication problems over e-mail it wasn't fixed until early January. Neither party is to blame, but this shows some of the difficulties that companies can face communicating with security researchers.

This [problem](http://techcrunch.com/2013/08/18/security-researcher-hacks-mark-zuckerbergs-wall-to-prove-his-exploit-works/) hit the media earlier this year when a Facebook security report was not clearly understood and led to the exploit being abused on Mark Zuckerberg's wall.

Facebook recently moved their Whitehat communication to their support dashboard instead of over e-mail which is going to help the company and security testers tremendously.

**The Exploit**

Sample request:

URL: <https://www.facebook.com/badges/profile.php>  
POST:  
fb_dtsg=&**layout=horiz** &items%5B%5D=badge_profile_pic&items%5B%5D=badge_test&items%5B%5D=badge_hometown&items%5B%5D=badge_email&items%5B%5D=badge_mobile_status&save=Save&bid=2421&badge_type=0&wizard=badges&owner_id=4

When this request is sent, it would return the following source:

Source: <div class="badge_holder bh_**horiz** ">

The layout request variable was being saved to a database and pulled into the <div>'s class. Because the input was not encoded, it allowed you to break out of the div and inject HTML.

**Example**

URL: <https://www.facebook.com/badges/profile.php>  
POST:  
fb_dtsg=&layout=**" ><b>**&items%5B%5D=badge_profile_pic&items%5B%5D=badge_test&items%5B%5D=badge_hometown&items%5B%5D=badge_email&items%5B%5D=badge_mobile_status&save=Save&bid=2421&badge_type=0&wizard=badges&owner_id=4

Screenshot:

**![image](https://31.media.tumblr.com/afc76c1b52d30d8fd74fa417ad2e26da/tumblr_inline_n7a2jaWevf1svukax.png)**

Normally I would show an iframe or script alert as an example, but this is the only screenshot I still have of this. The entire badge page has since been completely overhauled and no longer functions in a way that a string is passed by the client to a database to be saved.

**The Danger  
**

Although this could force you to save JavaScript/HTML on your badges page, the impact of it is quite small. This request is protected by fb_dtsg which is a csrftoken and Facebook has X-Frame-Options preventing clickjacking.

That means no one can force you to make this request, you would have to damage yourself or the attacker would have to already have access to your Facebook. Even still, you would have to visit the badge page in order for it to execute.

I'm going to bet a lot of you haven't even heard of the badge page until you read this.

Regardless, XSS is XSS! It can force you to execute any action protected by a csrftoken and extract information from your Facebook. That means forcing you to make Facebook posts or stealing private data that you didn't want public.

**The Bug**

Submitted: August 2013

Fixed: January 2014
