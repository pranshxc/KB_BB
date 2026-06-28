---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-04_came-looking-for-ssrf-and-found-xss.md
original_filename: 2022-08-04_came-looking-for-ssrf-and-found-xss.md
title: Came looking for SSRF and found XSS
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- mfa
- otp
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- mfa
- otp
language: en
raw_sha256: 291648c461ed219f06dc11984990722d2c2c306cf9857165e658f563fd79e2aa
text_sha256: 56a3894260b1110c40a4040d24e261f61b7c2a589f92bce1428ff924e2e96fe6
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Came looking for SSRF and found XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-04_came-looking-for-ssrf-and-found-xss.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `291648c461ed219f06dc11984990722d2c2c306cf9857165e658f563fd79e2aa`
- Text SHA256: `56a3894260b1110c40a4040d24e261f61b7c2a589f92bce1428ff924e2e96fe6`


## Content

---
title: "Came looking for SSRF and found XSS"
page_title: "Came looking for SSRF and found XSS | Write-up"
url: "https://ibraradi.gitbook.io/write-up/came-looking-for-ssrf-and-found-xss"
final_url: "https://ibraradi.gitbook.io/write-up/came-looking-for-ssrf-and-found-xss"
authors: ["Ibrahim Radi (@ibraradi9)"]
bugs: ["XSS", "WAF bypass"]
publication_date: "2022-08-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2366
---

For the complete documentation index, see [llms.txt](https://ibraradi.gitbook.io/write-up/llms.txt). This page is also available as [Markdown](https://ibraradi.gitbook.io/write-up/came-looking-for-ssrf-and-found-xss.md).

Copy

On this page

# Came looking for SSRF and found XSS

My first bug on H1.

## 

Function :

Importing bookmarks from an external website

### 

How it works :

  1. The function takes URL

  2. Sends HTTP request to the URL

  3. Previews the bookmarks into the website

  4. Then storing it into the page

### 

Bookmarks

📌 The function only shows the content of the "a" and "title" tags from that external URL

**I tried every possible SSRF attack I know ,but nothing worked.**

## 

XSS: 

### 

Self XSS :

I just created a website with The next content :

And Sent the request to my website from the bookmarking function

The "a" tag content is being filtered but titile is not,

For now it’s just a self XSS.

![](https://ibraradi.gitbook.io/write-up/~gitbook/image?url=https%3A%2F%2F3079983923-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FeafLyjNWlqNSCbbrOwGR%252Fuploads%252FYX9ASF8XvCQORm1yaUqd%252Fimage.png%3Falt%3Dmedia%26token%3D59d50468-0757-465a-8088-b6fbde07e8c8&width=768&dpr=3&quality=100&sign=62f4fb55&sv=2)

![](https://ibraradi.gitbook.io/write-up/~gitbook/image?url=https%3A%2F%2F3079983923-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FeafLyjNWlqNSCbbrOwGR%252Fuploads%252FaP3eDqdNL6iWsYDVNEGs%252Fimage.png%3Falt%3Dmedia%26token%3D156bbdde-59f8-4174-9213-b58be7e14069&width=768&dpr=3&quality=100&sign=5c1fdb91&sv=2)

### 

Stored XSS :

  * The “Add” function here stores the bookmarks into the website.

  * The self XSS accepted any payload,No kind of XSS prevention is being implemented their.

  * **The add function removes the JS Events from the bookmarks before storing it into the website**

### 

After a good fuzzing the next payload worked:

It’s stored in the next form :

📌 The report was closed as informative because of the program’s policy

They don’t accept XSS for some reason.

[PreviousWeb Cache Poisoning](/write-up/web-cache-poisoning)[NextPhishing Attack using Machine Learning model](/write-up/phishing-attack-using-machine-learning-model)

Last updated 3 years ago
