---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-04_url-validation-bypass-using-browser-uri-normalization.md
original_filename: 2022-12-04_url-validation-bypass-using-browser-uri-normalization.md
title: URL Validation Bypass Using Browser URI Normalization
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 367a33a855a5fb065dc50caf680b5c696ec6f1eb37231036bdcb7049dffb93dc
text_sha256: 57ad1ba48238229d2cddeeb27d3a3f8704c64cca43ab336da861d1cd613f5c46
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# URL Validation Bypass Using Browser URI Normalization

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-04_url-validation-bypass-using-browser-uri-normalization.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `367a33a855a5fb065dc50caf680b5c696ec6f1eb37231036bdcb7049dffb93dc`
- Text SHA256: `57ad1ba48238229d2cddeeb27d3a3f8704c64cca43ab336da861d1cd613f5c46`


## Content

---
title: "URL Validation Bypass Using Browser URI Normalization"
url: "https://marxchryz.medium.com/url-validation-bypass-using-browser-uri-normalization-cf545d33d13f"
authors: ["Marx Chryz Del Mundo"]
bugs: ["URL validation bypass"]
publication_date: "2022-12-04"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 1817
scraped_via: "browseros"
---

# URL Validation Bypass Using Browser URI Normalization

URL Validation Bypass Using Browser URI Normalization
Marx Chryz Del Mundo
Follow
4 min read
·
Dec 4, 2022

106

1

Hello everyone, I am Marx Chryz and I do bug bounty hunting for about two years now. It’s also been three and a half years since I started doing web penetration testing.

Introduction

This is a bug I found on a website that has bug bounty program. It is an external program so I can’t disclose the name. The vulnerability is also not yet fixed as of the writing. In that sense, we’ll just call the target as redacted.com

Uniform Resource Identifier (URI) Normalization

Have you ever noticed that when we type HTTPS://GOOGLE.COM in the browser, it automatically converts to https://google.com (lowercase)?

That’s URI Normalization in action! URI Normalization is a process in which web browsers modify the URI to make it standardized and consistent [read more here].

So, URI Normalization converts uppercase to lowercase?

Yep, but that’s not all about URI normalization. URI normalization also converts a ton of other things which we can use to bypass URL validation. Here are some examples:

Figure 1: ⒼⓄⓄⒼⓁⒺ.com is treated as google.com
Figure 2: 𝓰𝓸𝓸𝓰𝓵𝓮.𝓬𝓸𝓶 is treated as google.com
Figure 3: google｡com is treated as google.com
Press enter or click to view image in full size
Figure 4: This cursed text lol is still treated as a valid URL, thanks to URI normalization
URI Normalization Process

The URI normalization shown above are examples in which the browser finds its compatibility equivalent. Here are some examples of compatibility equivalence [read more here].

Table 1: Compatibility Equivalence Examples

Here’s a quick way to check for the compatibility equivalence

Press enter or click to view image in full size
Figure 5: This is the code and the output

Note that the ｡ (full stop symbol show in Figure 3) is not handled by the String.normalize function in JS (I don’t know why)

Now that we have an insight into what URI normalization is, we can use this to bypass URL validation filters! For example, if the website doesn’t want us to input google.com, then we can use ⒼⓄⓄⒼⓁⒺ.com to bypass the validation.

Get Marx Chryz Del Mundo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Exploitation

The bug I found is a lot similar to this Hackerone report of zurke. With that, let’s begin.

A POST parameter in the API accepts a “profilePicture” parameter. If I input a URL like “https://mydomain.com/1.jpg”, the response is “You entered invalid value”
However, if I inputted a URL like “https://img.redacted.com/random.jpg”, the response tells me that the changes I made were successful.
Based on those observations, I can infer that the backend uses some kind of whitelisting that only allows images from img.redacted.com to be inputted. This means that we need to bypass this whitelisting.
I tried several payloads that use URI normalization including:
- https://img.redacted.com｡mydomain.com/1.jpg
- https://img.redacted.com.ⓜⓨⓓⓞⓜⓐⓘⓝ.ⓒⓞⓜ/1.jpg
however, none of the payloads worked because life is not a fairy tale.
I remembered a common bypass for whitelisting, which is:
- https://img.redacted.com@mydomain.com
Even if this does not use URI normalization techniques that I discussed above, guess what? It still didn’t work.

6. I investigated further about URI normalization and stumbled upon something.

Figure 6: Usage of multiple @ symbols

7. I immediately tried to bypass the whitelisting filter by using the payload: https://img.redacted.com@@mydomain.com/1.jpg

It worked! I never knew this payload existed because I think I can’t found this anywhere in the internet. Even swisskyrepo’s PayloadAllTheThings doesn’t have this.

Report Timeline

Nov 18, 2022 — Bug Submitted
Nov 18, 2022 — Triaged
Dec 1, 2022 — Bounty Received
