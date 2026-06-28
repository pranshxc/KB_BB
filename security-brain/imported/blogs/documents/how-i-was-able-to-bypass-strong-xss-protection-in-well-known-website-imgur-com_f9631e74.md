---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-21_how-i-was-able-to-bypass-strong-xss-protection-in-well-known-website-imgurcom_2.md
original_filename: 2017-07-21_how-i-was-able-to-bypass-strong-xss-protection-in-well-known-website-imgurcom_2.md
title: How i was able to bypass strong xss protection in well known website. (imgur.com)
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: f9631e74d4569cbee86268ee11303e94f75855acc6376bbddfe328377e8ff0c3
text_sha256: 4a5e3f2fadfc230d8ad19be31750d0f69de06d79214eae0ead261e23a433404e
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How i was able to bypass strong xss protection in well known website. (imgur.com)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-21_how-i-was-able-to-bypass-strong-xss-protection-in-well-known-website-imgurcom_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `f9631e74d4569cbee86268ee11303e94f75855acc6376bbddfe328377e8ff0c3`
- Text SHA256: `4a5e3f2fadfc230d8ad19be31750d0f69de06d79214eae0ead261e23a433404e`


## Content

---
title: "How i was able to bypass strong xss protection in well known website. (imgur.com)"
url: "https://medium.com/bugbountywriteup/how-i-was-able-to-bypass-strong-xss-protection-in-well-known-website-imgur-com-8a247c527975"
authors: ["Armaan Pathan (@armaancrockroax)"]
programs: ["Imgur"]
bugs: ["XSS"]
bounty: "250"
publication_date: "2017-07-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6144
scraped_via: "browseros"
---

# How i was able to bypass strong xss protection in well known website. (imgur.com)

How i was able to bypass strong xss protection in well known website. (imgur.com)
Armaan Pathan
Follow
2 min read
·
Jul 21, 2017

1K

5

after finishing my final exams i have decided to give a dedicated time to bug bounty, not to EARN but to LEARN, so i had selected my target.

so i selected my domain which was imgur.com.

as soon as i selected the target i started browsing the website & at there i found that there is a option

ALBUM DESCRIPTION

Press enter or click to view image in full size

i decide to find that album description is vulnerable to Cross site scripting vulnerability or not.

so first i entered “/><script>alert(1);</script> and i noticed that it had removed the <script> tags from the album description at it was displaying alert(1); without any pop-up.

Get Armaan Pathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I decided to use event handler payload to check that i am getting the pop-up or not. so i tried “/><svg/onload=prompt(1);> & and now i had noticed that it has removed the onload tag from album description and it was only displaying <svg/prompt(1);> tag.

So here i had noticed the behavior of the application that it is stripping out the <script> tags and also stripping out the event handlers.

Then after I finally decided to use both <script> tag and event handlers to bypass the xss protection so i used ”/><svg/on<script>load=prompt(document.domain);>”/><svg/on<script>load=prompt(document.cookie);>

AND

Press enter or click to view image in full size
Press enter or click to view image in full size

i had bypassed the XSS protection over there and was able to store the malicious scripts.

and after reported it was patched & rewarded with sweet bounty :)
