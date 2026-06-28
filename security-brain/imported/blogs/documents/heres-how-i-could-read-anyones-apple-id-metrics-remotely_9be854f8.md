---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-30_heres-how-i-could-read-anyones-apple-id-metrics-remotely.md
original_filename: 2021-12-30_heres-how-i-could-read-anyones-apple-id-metrics-remotely.md
title: Here’s How I Could Read Anyone’s Apple ID Metrics Remotely.
category: documents
detected_topics:
- sso
- command-injection
- information-disclosure
- cloud-security
tags:
- imported
- documents
- sso
- command-injection
- information-disclosure
- cloud-security
language: en
raw_sha256: 9be854f81152ffd16b92145da89b4bc94485029b26a24aa056cadd490828b0f0
text_sha256: 4d37b54e523d21ea67be3b178932edc5dcbedb914b66ddd3922179b26742560e
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Here’s How I Could Read Anyone’s Apple ID Metrics Remotely.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-30_heres-how-i-could-read-anyones-apple-id-metrics-remotely.md
- Source Type: markdown
- Detected Topics: sso, command-injection, information-disclosure, cloud-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `9be854f81152ffd16b92145da89b4bc94485029b26a24aa056cadd490828b0f0`
- Text SHA256: `4d37b54e523d21ea67be3b178932edc5dcbedb914b66ddd3922179b26742560e`


## Content

---
title: "Here’s How I Could Read Anyone’s Apple ID Metrics Remotely."
url: "https://faizanwrites.medium.com/heres-how-i-could-read-anyone-s-iphone-metrics-remotely-28459943b898"
authors: ["Faizan Ahmad Wani"]
programs: ["Apple"]
bugs: ["Information disclosure"]
publication_date: "2021-12-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3046
scraped_via: "browseros"
---

# Here’s How I Could Read Anyone’s Apple ID Metrics Remotely.

Here’s How I Could Read Anyone’s Apple ID Metrics Remotely.
Faizan Ahmad Wani
Follow
3 min read
·
Dec 30, 2021

27

2

Hello, My name is Faizan. I’m a security researcher. Hope you like this blog. If you’ve any questions please feel free to reach out .

Apple has a security program under which it invites private security researchers to hack them and report the flaws in a coordinated and confidential manner. This hit my mind one day, and I decided to look around their servers.
Press enter or click to view image in full size
My Hall Of Fame

TL;DR Version : I was going through the domains owned by Apple, and starting testing out domains which are recently acquired or very less known to other security researchers is what is the most time saving approach, But I decided otherwise. I started testing iforgot.apple.com (one of the primary subdomains of Apple)- which is used by almost every Apple User in order to reset their password. After playing around for a while, I figured I could send a random text as a phone number to the server(which is okay), but at this moment I thought of trying out some injections. I investigated this more and changed the request method — From POST to GET and it disclosed information about the user without authentication. I reported this to Apple and after few discussions and presenting a solid exploitation scenario to the team, they decided to fix this up and added me to their Web Server Notification Hall Of Fame.

Get Faizan Ahmad Wani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s get into the fancy part- Here’s the procedure.

Attacker visits iforgot endpoint and enters victim’s Apple ID.
Press enter or click to view image in full size

2. Apple Before allowing the attacker to reset password tries to verify that the attacker really owns the Apple ID, so it asks attacker to enter the mobile number associated with the Apple ID to verify the ownership.

Press enter or click to view image in full size

3. Attacker enters a very random value.

Press enter or click to view image in full size

4. The request uses an HTTP POST to deliver the phone number to server in order to verify.

Press enter or click to view image in full size

5. The attacker changes the HTTP method (POST to GET) to read information.

Press enter or click to view image in full size

What Could an attacker read?

1) The country victim lives in. (via country code, which from the front end UI is not displayed)

2) Whether his device can be reset with another device.

3) Whether his account is a paid one.

4) Whether family device pairing is enabled on his Apple id.

5) Whether his current device supports remote unlocking.

This information could've aided an adversary in multiple ways (With this information one could think of preparing a massive Apple ID list , which published most vulnerable Apple Users worldwide) and this violated Apple’s commitment to safeguard User’s data and information.
