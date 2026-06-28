---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-10-31_instagrams-one-click-privacy-switch.md
original_filename: 2013-10-31_instagrams-one-click-privacy-switch.md
title: Instagram's One-Click Privacy Switch
category: documents
detected_topics:
- mobile-security
- xss
- command-injection
- otp
- csrf
- cloud-security
tags:
- imported
- documents
- mobile-security
- xss
- command-injection
- otp
- csrf
- cloud-security
language: en
raw_sha256: 5830fe2f38eed36e7ce0f5d89c8cf6b26663b4059a7e964578d4e3e814e593dc
text_sha256: 29e044035fb7168f969feacfc60db0f21c05f724a8e904fc6c1020578596514a
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Instagram's One-Click Privacy Switch

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-10-31_instagrams-one-click-privacy-switch.md
- Source Type: markdown
- Detected Topics: mobile-security, xss, command-injection, otp, csrf, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `5830fe2f38eed36e7ce0f5d89c8cf6b26663b4059a7e964578d4e3e814e593dc`
- Text SHA256: `29e044035fb7168f969feacfc60db0f21c05f724a8e904fc6c1020578596514a`


## Content

---
title: "Instagram's One-Click Privacy Switch"
page_title: "Instagram's One-Click Privacy Switch – Jack"
url: "https://whitton.io/articles/instagrams-one-click-privacy-switch/"
final_url: "https://whitton.io/articles/instagrams-one-click-privacy-switch/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
publication_date: "2013-10-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6390
---

# [Instagram's One-Click Privacy Switch](https://whitton.io/articles/instagrams-one-click-privacy-switch/ "Instagram's One-Click Privacy Switch")

## October 31, 2013

__Reading time ~2 minutes

Back in April I found three CSRF issues on Instagram, stemming from their Android/iOS App API (which is slightly different from their [public API](https://instagram.com/developer) \- it’s hosted on their main domain and doesn’t need an access token).

These issues were present in the following end-points:

  * `accounts/remove_profile_pic` \- This is used to remove the profile picture from an account
  * `accounts/set_private` \- This is used to mark a profile as private
  * `accounts/set_public` \- This is used to mark a profile as public

Obviously the best one out of these is `accounts/set_public`. With a simple GET request we can reveal anyones profile and access their private pictures. Pretty cool.

[ ![](/images/instagramprivacy/instagram-privacy-1-3.png) ](/images/instagramprivacy/instagram-privacy-1-3.png)

Facebook patched the holes pretty quickly and I was awarded a decent bounty for it.

Once patched I checked to make sure that it was indeed fixed, and issuing a GET request returns a [405 Method Not Allowed](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.6) response.

[ ![](/images/instagramprivacy/instagram-privacy-2.png) ](/images/instagramprivacy/instagram-privacy-2.png)

### Round Two

I didn’t blog about the issue and completely forgot about it until recently. I decided to have another look at the Android App to see if there was any new end-points to play around with.

Pretty much all API requests within the app call a method named `setSignedBody`. This generates a hash of the parameters with a secret embedded in an `.so` file, meaning we can’t craft our own request on-the-fly and submit on the users behalf (without extracting the secret).

[ ![](/images/instagramprivacy/instagram-privacy-3.png) ](/images/instagramprivacy/instagram-privacy-3.png)

However, the three end-points I submitted still didn’t use `setSignedBody` (presumably because there are no parameters needed), and therefore no token is sent along. Because of this, we can submit a POST request and still perform the attack which was supposed to be fixed!

[ ![](/images/instagramprivacy/instagram-privacy-4.png) ](/images/instagramprivacy/instagram-privacy-4.png)

The use of `setSignedBody` without a CSRF token means that **all** end-points are vulnerable to a replay attack. You simply submit the request yourself, catch the request in Burp, and replay to the victim. Unfortunately, this is something I realised _after_ the bug was fixed, so no screenshots available.

So the moral here is that you should **double-double-check** that an issue is fixed. If I’d been more thorough in testing the fix I would have spotted it sooner than four months, my bad.

### Fix

This is now patched by requiring all requests to have a `csrftoken` parameter. Any request which is signed also requires a `_uid` parameter to prevent replay attacks (unless you extract the secret…).

The original proof-of-concept now returns a 400 error.

[ ![](/images/instagramprivacy/instagram-privacy-5.png) ](/images/instagramprivacy/instagram-privacy-5.png)

The response body is a JSON object showing the error message.

[ ![](/images/instagramprivacy/instagram-privacy-6.png) ](/images/instagramprivacy/instagram-privacy-6.png) [facebook](https://whitton.io/tags/#facebook "Pages tagged facebook")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[websec](https://whitton.io/tags/#websec "Pages tagged websec")[instagram](https://whitton.io/tags/#instagram "Pages tagged instagram")[csrf](https://whitton.io/tags/#csrf "Pages tagged csrf") Updated on October 31, 2013 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/instagrams-one-click-privacy-switch/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/instagrams-one-click-privacy-switch/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/instagrams-one-click-privacy-switch/ "Share on Google Plus")

[Read More](https://whitton.io/articles/content-types-and-xss-facebook-studio/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016
