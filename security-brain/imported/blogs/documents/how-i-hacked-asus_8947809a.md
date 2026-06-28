---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-09_how-i-hacked-asus.md
original_filename: 2019-02-09_how-i-hacked-asus.md
title: How I hacked ASUS?
category: documents
detected_topics:
- xss
- access-control
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- xss
- access-control
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 8947809a7e77de028baadc770f02080dc8133fd4247c74b38077c9d742e789f1
text_sha256: b3f9d9c472e275369eeed2b8a1ae8dfff5758a2def420c0924a48412c5e48f04
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked ASUS?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-09_how-i-hacked-asus.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `8947809a7e77de028baadc770f02080dc8133fd4247c74b38077c9d742e789f1`
- Text SHA256: `b3f9d9c472e275369eeed2b8a1ae8dfff5758a2def420c0924a48412c5e48f04`


## Content

---
title: "How I hacked ASUS?"
page_title: "How I hacked ASUS? | Mustafa Kemal Can"
url: "https://mustafakemalcan.com/asus-rce-vulnerability-on-rma-asus-europe-eu/"
final_url: "https://www.mustafakemalcan.com/asus-rce-vulnerability-on-rma-asus-europe-eu/"
authors: ["Mustafa Kemal Can (@muskecan)"]
programs: ["Asus"]
bugs: ["Unrestricted file upload", "RCE"]
publication_date: "2019-02-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5423
---

* [Home](https://muskecan.github.io/)
  * [Blog](https://muskecan.github.io/blog)
  * [About](https://muskecan.github.io/about)

![How I hacked ASUS?](/assets/posts/asus-rce.jpg)

# How I hacked ASUS?

Saturday. February 09, 2019 \-  1 min 

Hello folks! Today I want to talk about **ASUS RCE** vulnerability on rma.asus-europe.eu domain.

I was trying to fill out service apply form for my personal laptop. I had a screen issue.

I realised that there is an upload part to upload some warranty documents.

I was trying to bypass upload restrictions by editing request.

I couldn’t figure it out but it happened very fast! Because interestingly, ASUS didn’t implement serious restrictions on upload part. Most of the rules were on front end part which are easy to bypass.

Thanks to burp and our old null byte friend, I was able to bypass all upload restriction.

![](https://muskecan.github.io/assets/posts/asus-hacked-requst.png)

The next mission was to find upload directory. I need to say thanks to **ASUS developers,** they helped me a lot. The directory was /uploads which is very easy to predict.

## Achievement unlocked! - ASUS RCE 

It is Microsoft-IIS 8.5, help me ASP!

I used a very basic asp rce script for Microsoft-IIS 8.5 and it worked like a charm!

![](https://muskecan.github.io/assets/posts/asus-hacked-1024x729.png)

I did not want to go further and quickly sent an email to the **security@asus.com** but they didn’t respond for a while.

After that they just fixed the issues and close it. There was no response to me.

I sent lots of mails about issue and they decided to add my name to the HoF list.

But they didn’t. I needed to create huge email traffic to do so.

**ASUS acted** very **rudely** about security, I am not happy.

But finally, I’ve added [HoF list](https://www.asus.com/Static_WebPage/ASUS-Product-Security-Advisory/) by ASUS.

[« CyberArk EPM Privilege Escalation Vulnerability - CVE-2018-13052](https://muskecan.github.io/cyberark-epm-privilege-escalation-cve-2018-13052/) [Senate.gov open redirect vulnerability »](https://muskecan.github.io/senate-gov-open-redirect-vulnerability/)

#### Related Posts

  * [CyberArk EPM Privilege Escalation Vulnerability - CVE-2018-13052 ](https://muskecan.github.io/cyberark-epm-privilege-escalation-cve-2018-13052/)
  * [CyberArk EPM file block bypass - CVE-2018-14894 ](https://muskecan.github.io/cyberark-epm-file-block-bypass-cve-2018-14894/)
  * [First Touch Games database information leak ](https://muskecan.github.io/first-touch-games-database-information-leak/)
  * [ITSLEARNING VULNERABILITY STORIES - One more stored XSS ](https://muskecan.github.io/itslearning-vulnerability-stories-episode-3/)
  * [ITSLEARNING XSS PART 2 ](https://muskecan.github.io/itslearning-xss-part-2/)

![](https://muskecan.github.io/)

#### 

[ Tweet ](https://twitter.com/intent/tweet?text=https://muskecan.github.io/asus-rce-vulnerability-on-rma-asus-europe-eu/ - How I hacked ASUS? by @) [ Share ](javascript:void\(0\))

Mustafa Kemal Can ©
