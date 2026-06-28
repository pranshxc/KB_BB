---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-25_shopping-app-deeplink-arbitrary-urls.md
original_filename: 2022-09-25_shopping-app-deeplink-arbitrary-urls.md
title: Shopping App Deeplink Arbitrary URLs
category: documents
detected_topics:
- xss
- access-control
- command-injection
- mobile-security
- supply-chain
tags:
- imported
- documents
- xss
- access-control
- command-injection
- mobile-security
- supply-chain
language: en
raw_sha256: 6359c8d6ba349ebaa751894645eba896e742b720bbf265a6c5482aec62d01f79
text_sha256: e71aac205f7cc162d094aae7b1727d3942b745b6389cdb91e43295c9104daf95
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Shopping App Deeplink Arbitrary URLs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-25_shopping-app-deeplink-arbitrary-urls.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `6359c8d6ba349ebaa751894645eba896e742b720bbf265a6c5482aec62d01f79`
- Text SHA256: `e71aac205f7cc162d094aae7b1727d3942b745b6389cdb91e43295c9104daf95`


## Content

---
title: "Shopping App Deeplink Arbitrary URLs"
url: "https://nmochea.medium.com/shopping-app-deeplink-arbitrary-urls-91a143a45c11"
authors: ["Neil Mark Ochea (@nmochea)"]
bugs: ["Insecure deeplink", "Android"]
publication_date: "2022-09-25"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2119
scraped_via: "browseros"
---

# Shopping App Deeplink Arbitrary URLs

Shopping App Deeplink Arbitrary URLs
Neil Mark Ochea / mhl_0xnmo
Follow
2 min read
·
Sep 25, 2022

14

In this write-up, I’ll tell you how I was able to launch Arbitrary URLs to the internal web of the shopping application.

Description

Due to the lack of URLs Sanitization that passes through activities, It’s possible to launch Arbitrary URLs to the internal web of the shopping application using a crafted website and malware applications. Also, I tried to bypass the host validation to launch Universal Cross-Site Scripting (UXSS) it seems looks not vulnerable to the attack since there’s another filter to the host.

In file com/redacted/android/maintab/MainTabActivity.java
Press enter or click to view image in full size

As you can see above the vulnerable code contains (scheme redacted://, host messages.redacted.com, and parameter message_target_url=) by adding malicious URLs to an endpoint to launch arbitrary URLs to the internal web of the shopping application here is the final deeplink below.

Press enter or click to view image in full size
Proof of Concept
In file PoC.html
Press enter or click to view image in full size

As you can see above the poc.html was crafted on a malicious website to launch deeplink inside shopping app.

In Malware application
Press enter or click to view image in full size

As you can see above a malware application or third-party application launch arbitrary URLs to the internal web of the shopping app.

Disclosure Timeline
December 18, 2021 — I reported this vulnerability issue.
December 19, 2021 — The report has been review and confirmed the vulnerability.
January 22, 2022 — The vulnerability has been patched and got a bounty.

Thanks for reading this article, I hope you guys learn something new today. Please share this article to spread the knowledge.

Get Neil Mark Ochea / mhl_0xnmo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Don’t forget to follow and connect with me through LinkedIn, and Twitter.
