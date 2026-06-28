---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-28_unauthenticated-cache-purge.md
original_filename: 2021-10-28_unauthenticated-cache-purge.md
title: Unauthenticated Cache Purge
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: c6cd7c1eab27a367833ddfe701643d08303e29fcfa21960d8a7483a16e417edd
text_sha256: c05a11ca060e87817b77bb2f319f414c24089c2378b1df4b2aecf83ae825aee7
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated Cache Purge

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-28_unauthenticated-cache-purge.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `c6cd7c1eab27a367833ddfe701643d08303e29fcfa21960d8a7483a16e417edd`
- Text SHA256: `c05a11ca060e87817b77bb2f319f414c24089c2378b1df4b2aecf83ae825aee7`


## Content

---
title: "Unauthenticated Cache Purge"
url: "https://medium.com/@priyanshbansal25/unauthenticated-cache-purge-c56fac8569e8"
authors: ["Priyansh Bansal (@PriyanshB25)"]
programs: ["Lenovo"]
bugs: ["Unauthenticated cache purge"]
publication_date: "2021-10-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3209
scraped_via: "browseros"
---

# Unauthenticated Cache Purge

Unauthenticated Cache Purge
Priyansh Bansal
Follow
2 min read
·
Oct 27, 2021

27

1

Hello everyone, I am Priyansh and this is my first writeup. Today I will be discussing a vulnerability that I found in one of the subdomains of Lenovo. The vulnerability was reported to Lenovo, and Lenovo responded promptly and took immediate action to fix the issue. The vulnerability name is Unauthenticated Cache Purge.

Let us first see what Cache is and what is the meaning of Cache Purge.

What is Cache?

Cached data is information from a website or app that is stored on your device to make the browsing process faster. Cached data save the loading time of a website or an app.

For example: If you visit a website for the first time, it loads the images, files, fonts, etc from the server. Now if this loading of images, files, etc is done every time you visit the website it increases the request traffic on the server, so to avoid this situation Caches are used. So caches help to reduce the request traffic on the website and load the website much faster whenever you visit the website again.

Press enter or click to view image in full size
Visual Representation Of Caching

I hope the above image for the process of caching made it more clear how the process of Caching works. Now, let us talk about Cache Purging.

What is Cache Purge?

Cache Purge refers to the deletion of the stored cache. Whenever a Cache Purge request is made, it deletes the stored caches and when you open that website it again loads every file, font, image, etc like for the very first time.

Get Priyansh Bansal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now let us talk about the vulnerability.

Unauthenticated Cache Purge

Description: If the Purge request is available to any user even to those who are not authenticated then they can delete the caches stored at a certain resource. This can lead to degraded application performance and an increase in bandwidth cost.

Steps to Perform:

It is very easy to find, you just need to send a CURL command, the command is: curl -X PURGE https://target.com

If the website is vulnerable then the response on the terminal will be in the following format:

{ “status”: “ok”, “id”: “21750–1634079449–30319” }%

If the website is not vulnerable then in response you will get an error message.

Remediation: Disallow cache purge requests or limit to authenticated users only.

Reference Report: https://hackerone.com/reports/154278

So this was all about today’s writeup, hope you liked it. This is my first writeup, so do let me know how was the writeup.

Profile Links:

Twitter: https://twitter.com/PriyanshB25

LinkedIn: www.linkedin.com/in/priyansh-bansal-b10570181
