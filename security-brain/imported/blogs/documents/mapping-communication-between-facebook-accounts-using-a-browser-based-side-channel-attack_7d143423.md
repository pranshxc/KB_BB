---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-07_mapping-communication-between-facebook-accounts-using-a-browser-based-side-chann.md
original_filename: 2019-03-07_mapping-communication-between-facebook-accounts-using-a-browser-based-side-chann.md
title: Mapping Communication Between Facebook Accounts Using a Browser-Based Side
  Channel Attack
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 7d14342305cfdeca55c778465db1f923a502d7d0dd4e753b2f1db1c4dbb954ae
text_sha256: 47f173c3dd0bab86b7b39efbe3200695b91650893a43bdc1f24d597729b5fcb0
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Mapping Communication Between Facebook Accounts Using a Browser-Based Side Channel Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-07_mapping-communication-between-facebook-accounts-using-a-browser-based-side-chann.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `7d14342305cfdeca55c778465db1f923a502d7d0dd4e753b2f1db1c4dbb954ae`
- Text SHA256: `47f173c3dd0bab86b7b39efbe3200695b91650893a43bdc1f24d597729b5fcb0`


## Content

---
title: "Mapping Communication Between Facebook Accounts Using a Browser-Based Side Channel Attack"
page_title: "Mapping Communication Between Facebook Accounts Using a Browser-Based Side Channel Attack | Imperva"
url: "https://www.imperva.com/blog/mapping-communication-between-facebook-accounts-using-a-browser-based-side-channel-attack/"
final_url: "https://www.imperva.com/blog/archive/mapping-communication-between-facebook-accounts-using-a-browser-based-side-channel-attack/"
authors: ["Ron Masas (@RonMasas)"]
programs: ["Meta / Facebook"]
bugs: ["Side-channel attack", "Cross-Site Frame Leakage (CSFL)"]
publication_date: "2019-03-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5373
---

### A now-patched vulnerability in the web version of Facebook Messenger allowed any website to expose who you have been messaging with.

In a _[previous post](https://www.imperva.com/blog/facebook-privacy-bug/)_ , I showed how your Facebook likes, location history, and other metadata could have been extracted from your Facebook account using a side-channel attack I named “Cross-Site Frame Leakage,” or CSFL for short.

In this post, I’ll formalize the CSFL attack, cover the latest enhancements to it, and review the vulnerability I disclosed to Facebook.

## What is a CSFL Attack?

Cross-Site Frame Leakage is a side-channel attack, performed on an end user’s web browser, that exploits the cross-origin properties of iframe elements to determine the state of a vulnerable application.

### What’s a state?

Take a search results page as an example. In terms of state, the most useful information the attacker could uncover would be whether or not a given query returned results.

If an attacker could determine the state of the search results page, he could probably infer other information about the currently logged user. Click on the short proof of concept video demonstrating this.

<https://www.imperva.com/blog/wp-content/uploads/sites/9/2019/03/fb-messenger-poc-smaller.mp4>

## Identifying the Threat

Like many people, I use Facebook Messenger to communicate with my friends, family, and businesses. As happens with applications I regularly use, I felt the need to understand how Facebook Messenger works.

I started poking around the Messenger web application and noticed that iframe elements were dominating the user-interface. The chat box, as well as the contact list, were rendered in iframes, opening the possibility for a CSFL attack.

Like in the _[previous bug](https://www.imperva.com/blog/facebook-privacy-bug/)_ , I relied on the ability to count the number of iframes on a cross-origin page located on a background page that could be controlled by an attacker. However, in Messenger, there was no way to create search requests without user interaction. Additionally, unlike the previous bug, the iframe count always reached three once the page was fully loaded, eliminating the possibility to detect a “state” using the number of iframe elements.

I started digging into those three iframes, in order to understand how, why and when they are loaded. I decided to record the iframe count data over time for as many endpoints I could find, with the goal of uncovering interesting and detectable states.

After a few tests, I started looking into the conversation endpoint. I recorded “full state” data, meaning pages that would load my conversation with a user I’ve been in touch with, and some “empty state” data, showing conversations with users I’ve never contacted.

After looking at five examples, it was clear I was on to something. The “empty state” charts consistently produce an interesting pattern as you can see in the visualization below, and in proof of concept video above.

_The top blue line is the iframe count for the empty state, the bottom red line is the count for the full state._

When the current user has not been in contact with a specific user, the iframe count would reach three and then always drop suddenly for a few milliseconds. This lets an attacker reliably distinguish between the full and empty states. This could let him remotely check if the current user has chatted with a specific person or business, which would violate those users’ privacy.

To summarize, by recording the frame count data over time, I found two new ways to leak cross-origin information. By looking at patterns instead of a static number, I was able to leak the “state” of a cross-origin window, either by analyzing the raw pattern or by timing certain “milestones” of the pattern.

## Attack Flow

For this attack to work we need to trick a Messenger user into opening a link to our malicious site. Next, we need the user to click anywhere on the page. For example, this could be a video play button.

Once clicked, a new tab would open while keeping the previous one open in the background.

The new tab would start playing a video, keeping the user busy while we load the user messenger conversation endpoint in the background tab.

While Messenger loads in the background, we record the iframe count as I previously explained, allowing us to detect whether or not the current user has been in contact with specific users or Facebook Messenger bots.

Full POC script: _<https://gist.github.com/masasron/1beca41f42599db1c6d48a89e135f653>_

## Mitigation

Having reported the vulnerability to Facebook under their responsible disclosure program, Facebook mitigated the issue by randomly creating iframe elements, which initially broke my proof of concept. However, after some work, I managed to adapt my algorithm and distinguish between the two states. I shared my finding with Facebook, who decided to completely remove all iframes from the Messenger user interface.

## Closing Thoughts

Browser-based side-channel attacks are still an overlooked subject, while big players like Facebook and Google are catching up, most of the industry is still unaware.

I recently joined an effort to document those attacks and vulnerable DOM APIs, you can find more information on the _[xsleaks](https://github.com/xsleaks/xsleaks/wiki/Browser-Side-Channels)_ repository (currently still under construction).

As a researcher, it was a privilege to have contributed to protecting the privacy of the Facebook user community, as we continuously do for our own Imperva community.

***

Did you know that one-third of businesses have admitted to six or breaches in the past year alone? Or that more than four out of five enterprises can’t hire security professionals fast enough? If you are a security or IT decisionmaker, the data from the 2019 CyberThreat Defense Report from the CyberEdge Group is essential for helping you understand the state of cybersecurity and make informed strategies and decisions. Get your [free copy here.](https://www.imperva.com/resources/resource-library/reports/2019-cyberthreat-defense-report/) And[ listen to the webinar](https://www.imperva.com/resources/resource-library/webinars/security-analytics-becomes-most-wanted-solution-insights-from-cyberedges-2019-cyberthreat-defense-report/) with CyberEdge’s COO Mark Bouchard being interviewed by Imperva senior product marketing manager, Sara Pan.

### Try Imperva for Free

Protect your business for 30 days on Imperva.

[Start Now](https://www.imperva.com/free-trial/)
