---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-13_blind-xss-on-google-internal-system.md
original_filename: 2021-05-13_blind-xss-on-google-internal-system.md
title: Blind XSS on Google Internal System
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 7c384065f951af8a13ac13c9620cb33d6713818f0b0767909cd169d96740d3d1
text_sha256: cf2b3b55322d77abc39268588673ba05fa403a516744a968faa0247cead7691a
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Blind XSS on Google Internal System

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-13_blind-xss-on-google-internal-system.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `7c384065f951af8a13ac13c9620cb33d6713818f0b0767909cd169d96740d3d1`
- Text SHA256: `cf2b3b55322d77abc39268588673ba05fa403a516744a968faa0247cead7691a`


## Content

---
title: "Blind XSS on Google Internal System"
page_title: "Blind XSS on Google Internal System  – Kailash"
url: "https://kailashbohara.com.np/blog/2021/05/13/Google-blind-XSS/"
final_url: "https://kailashbohara.com.np/blog/2021/05/13/Google-blind-XSS/"
authors: ["Kailash (@Corrupted_brain)"]
programs: ["Google"]
bugs: ["Blind XSS"]
bounty: "5,000"
publication_date: "2021-05-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3657
---

# [Blind XSS on Google Internal System ](https://corrupted-brain.github.io/blog/blog/2021/05/13/Google-blind-XSS/ "Blind XSS on Google Internal System ")

[Blind cross-site scripting](https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/blind-cross-site-scripting/) (XSS) refers to a type of code injection where an attacker inserts XSS payload in user input fields and they are going to be stored somewhere and executes in an application that is not in control of an attacker.

I ended up finding blind XSS in one of the Google’s internal system (GUTS ticketing system). I used blind XSS payload from [xsshunter](https://xsshunter.com) and filled up randomly input fields on the form from Google supplier portal. The forms from the supplier portal must be tracked from GUTS, that’s what I assume and my payload gets executed.

#### What happened ?

I get a response in my xsshunter after a very long time and at the moment I was unknown which parameter I tested for.![Google reply](/images/posts/google_reply-1.png) I tried to read the [DOM](https://www.w3schools.com/js/js_htmldom.asp) so that we may know the possible parameter. Unfortunately, XSS hunter keeps loading and the browser gets frozen. Only Referer and Cookies are known. I passed the information that I have to the Google team and they finally managed to know the actual cause and rewards me. ![Reward message](/images/posts/google_reward_xss.png)

I requested to disclose a vulnerable endpoint as seen above but ended up with the following message.![Reply](/images/posts/google_final_reply.png) As part of Google’s Vulnerability Reward Program, the panel has decided to issue a reward of $5000 for this issue as it affects the sensitive application.

#### Giveaway ?

Always take a log where we tested for XSS. We don’t know when our luck hits in bug bounty.

* * *

#### Share on

  * [__Twitter](https://twitter.com/intent/tweet?text=Blind XSS on Google Internal System  https://corrupted-brain.github.io/blog/blog/2021/05/13/Google-blind-XSS/ "Share on Twitter")
  * [__Facebook](https://www.facebook.com/sharer/sharer.php?u=https://corrupted-brain.github.io/blog/blog/2021/05/13/Google-blind-XSS/ "Share on Facebook")
  * [__Google+](https://plus.google.com/share?url=https://corrupted-brain.github.io/blog/blog/2021/05/13/Google-blind-XSS/ "Share on Google Plus")
  * [__LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://corrupted-brain.github.io/blog/blog/2021/05/13/Google-blind-XSS/&title=Blind XSS on Google Internal System &summary=Blind cross-site scripting \(XSS\) refers to a type of code injection where an attacker inserts XSS payload in user input fields and...&source=https://corrupted-brain.github.io/blog "Share on LinkedIn")

**Blind XSS on Google Internal System** was published on May 13, 2021.
