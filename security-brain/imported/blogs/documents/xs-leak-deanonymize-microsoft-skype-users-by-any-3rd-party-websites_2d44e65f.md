---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-21_xs-leak-deanonymize-microsoft-skype-users-by-any-3rd-party-websites.md
original_filename: 2023-04-21_xs-leak-deanonymize-microsoft-skype-users-by-any-3rd-party-websites.md
title: 'XS-Leak: Deanonymize Microsoft Skype Users by any 3rd-party websites'
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 2d44e65fc87f3a02f0d01a7da6599b9cbfc26126b644c0df2007769bfa2f29ed
text_sha256: 3e3b4eced0b07d74db06965128aeeefbd1e74ad2a43d4b87ff8783245f867c0b
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# XS-Leak: Deanonymize Microsoft Skype Users by any 3rd-party websites

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-21_xs-leak-deanonymize-microsoft-skype-users-by-any-3rd-party-websites.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `2d44e65fc87f3a02f0d01a7da6599b9cbfc26126b644c0df2007769bfa2f29ed`
- Text SHA256: `3e3b4eced0b07d74db06965128aeeefbd1e74ad2a43d4b87ff8783245f867c0b`


## Content

---
title: "XS-Leak: Deanonymize Microsoft Skype Users by any 3rd-party websites"
url: "https://infosecwriteups.com/xs-leak-deanonymize-microsoft-skype-users-by-any-3rd-party-website-69849e4501a8"
authors: ["Jayateertha Guruprasad (@JayateerthaG)"]
programs: ["Microsoft (Skype)"]
bugs: ["XSLeaks"]
publication_date: "2023-04-21"
added_date: "2023-04-27"
source: "pentester.land/writeups.json"
original_index: 1235
scraped_via: "browseros"
---

# XS-Leak: Deanonymize Microsoft Skype Users by any 3rd-party websites

XS-Leak: Deanonymize Microsoft Skype Users by any 3rd-party websites
Jayateertha Guruprasad
Follow
3 min read
·
Apr 21, 2023

48

XS-Leaks — These are class of vulnerabilities derived from side channel attack. Although browsers have security features like SOP, which prevents access to data of websites from different origin. Browsers support various interactions between different web applications such as embedding a image, loading a sub-resource, postMessage, navigation to different websites etc

XS-Leaks exploit small pieces of information that are exposed during interactions between websites, despite the security mechanisms in place to constrain these behaviors.

XS-Leaks through Error Events — when a website loads a resource from another website using HTML tags like ‘img’ or ‘script’. Depending upon the response status code of the loaded resource ‘onerror’ and ‘onload’ events are triggered, which can inadvertently expose sensitive information.

Vulnerability Summary —

An XS-Leak vulnerability in Skype allows attackers to deanonymize and track users without their knowledge. The attacker can exploit this vulnerability by sending an image attachment to the victim and taking note of the image’s URL. With this information, they can create a malicious website that tries to load the same URL. As only the victim and attacker can access the image, When the victim accesses the website, the ‘onload’ event is triggered, whereas the ‘onerror’ event is triggered for other users. By leveraging this behavior, The attacker can de-anonymize & trace the victim’s online activities without requiring the victim to accept any cookies from the malicious website.

Proof Of Concept —

Proof Of Concept Code —

<html>
<head></head>
<body>
<img src="https://api.asm.skype.com/v1/objects/SECRET/views/imgpsh_fullsize_anim" onload="alert('User Jayateertha Detected !')" onerror="alert('Not User Jayateertha')">
</body>
</html>

Attack Scenario —

An organization/attacker sends image attachments to multiple skype users & note’s down the image link of attachment.
Organization/attacker crafts a malicious website which includes the skype image attachment urls along with onerror/onload event attached to img tag to pinpoint the victim & track his activities online.
Think of a large organization exploiting this vulnerability by embedding multiple such urls to track users , They could use this to pinpoint victim to Microsoft Skype account & also track their activities online even if victim is not logged in to organization account/not opted in to use cookies for the site.

Impact —

This vulnerability can be used for deanonymization, which can be especially dangerous in certain contexts. For example, a victim who is accessing sensitive information may be at risk if an attacker can deanonymize them. This vulnerability can also be used to track individuals and their activities online.

For, ex — Victim is visiting a site where cookies are not being used for tracking & he prefers to perform activities anonymously, But the remote website could use this vulnerability to deanonymize victim to his exact Microsoft Skype account as well as track his activities.

This vulnerability can lead to significant privacy concerns for individuals using Skype. Victims may not be aware that their anonymous activity in a website is being tracked down to their Microsoft Skype account.

Get Jayateertha Guruprasad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Fix Suggestions —

Don’t set SAMESITE attribute to None
Incase, SAMESITE needs to be set to None, use a custom authorization header to access the image with proper authorization checks.
Add a query param & value which is different for attacker & victim such that , only if query param & value is present in the request & is that of victim the image can be accessed.

Reply From Microsoft —

Press enter or click to view image in full size

References:

XS-Leak Deanonymize OpenSea NFT Owners
Account & User Identification Vulnerability involving XS-Leak eligible for FaceBook Bounty
Multiple XS-Leak in Google found by Tezranq
XS-Leak in Slack
XS-Leaks.dev

Time Line:

First Report to MSRC (VULN-097675) — Apr 9, 2023
Second Report to MSRC (VULN-098011) for similar vulnerability in Teams— Apr 15, 2023
Reply from Microsoft ~ Cannot Fix (VULN-097675) — Apr 11, 2023
Third Report to MSRC (VULN-098156) again mentioning impact clearly for VULN-097675 — Apr 18, 2023
Report closed by Microsoft ~ Cannot Fix (VULN-098156) — Apr 21, 2023
Public Disclosure — Apr 21, 2023
