---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-01_bypass-mobile-pin-verification.md
original_filename: 2020-01-01_bypass-mobile-pin-verification.md
title: Bypass Mobile PIN Verification
category: documents
detected_topics:
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 4bfed262b56ccaeb9e13cfa0ba03bec14f19f5ae004ad75d5b28d58856a051a7
text_sha256: d7493062817f1390a30053080f728ce9156ad021278191a843e95c8d0722675f
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass Mobile PIN Verification

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-01_bypass-mobile-pin-verification.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `4bfed262b56ccaeb9e13cfa0ba03bec14f19f5ae004ad75d5b28d58856a051a7`
- Text SHA256: `d7493062817f1390a30053080f728ce9156ad021278191a843e95c8d0722675f`


## Content

---
title: "Bypass Mobile PIN Verification"
url: "https://medium.com/sourav-sahana/bypass-mobile-pin-verification-d2c571afa3aa"
authors: ["Sourav Sahana (@kernel_rider)"]
bugs: ["Authentication bypass"]
bounty: "100"
publication_date: "2020-01-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4849
scraped_via: "browseros"
---

# Bypass Mobile PIN Verification

Bypass Mobile PIN Verification
Sourav Sahana
Follow
2 min read
·
Jan 2, 2020

97

1

Hi Hunters! again I’m here with another findings. The bounty of this bug is not enough but I’m still happy with this ¯\_(ツ)_/¯. I’m personally more interested about mobile application testing. I was able to bypass of a application’s PIN verification. Hope you will enjoy this post..

It was 31 Oct, 2019. New program launched on Bugcrowd. Feels like got command from commando for surgical strike. Luckily there was a apk file in scope.

There was a 4 digit PIN protection for opening the application. First I thought this can be bypass using response manipulation. But wait ! not getting any request in the Intercept. may be I did not bypass ssl pining properly. Checked again. All ok! So I’m not getting request for that task it means application is fetching data from internal memory. So opened ADB tool and started finding where the PIN is storing. Finally found a suspicious xml file in shared_prefs directory, Named 6e230139nh78454a8b0abui876b5f4a3.xml . And it contains some hash string. Every time the hash value changes after I change the PIN. So I simply removed the file, and BAAMM… There is no PIN protection when I open the application.

I immediately created a report with a good POC video and waiting for the response. First they marked my report as P as it required physical and root access. Then I argued with them. My replay: “you are right this exploit needs physical access of user’s device. But developer implemented one extra protection for one step better security because of unauthorized users can’t access the application even he has the device on his hand. If attacker can bypass this anyhow then this protection is useless, in that case basic protection will be enough to authenticate users. authentication mechanism is not implemented properly and I believe this is a security issue present in the application”

Get Sourav Sahana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally they accepted my report and I got my bounty. I feel so happy.

Total bounty I got $100. Thank you and happy Hunting.
