---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-15_tiktok-careers-portal-account-takeover.md
original_filename: 2020-12-15_tiktok-careers-portal-account-takeover.md
title: TikTok Careers Portal Account Takeover
category: documents
detected_topics:
- oauth
- sso
- xss
- command-injection
- otp
- csrf
tags:
- imported
- documents
- oauth
- sso
- xss
- command-injection
- otp
- csrf
language: en
raw_sha256: 13f8f065730ac669f4b54d009bef9b5b0d255bdb003024e3863dbed95445567b
text_sha256: 67897ce2eba3ff7f0e626fb3dad17862c5ce44e3cbdc80b91c540d10a860d237
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# TikTok Careers Portal Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-15_tiktok-careers-portal-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, sso, xss, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `13f8f065730ac669f4b54d009bef9b5b0d255bdb003024e3863dbed95445567b`
- Text SHA256: `67897ce2eba3ff7f0e626fb3dad17862c5ce44e3cbdc80b91c540d10a860d237`


## Content

---
title: "TikTok Careers Portal Account Takeover"
page_title: "(Web-)Insecurity Blog"
url: "https://security.lauritz-holtmann.de"
final_url: "https://security.lauritz-holtmann.de/"
authors: ["Lauritz Holtmann (@_lauritz_)"]
programs: ["TikTok"]
bugs: ["CSRF", "Open redirect", "Account takeover"]
bounty: "2,373"
publication_date: "2020-12-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4067
---

Hi there 👋

My name is Lauritz and I am an IT-Security researcher and penetration tester based in Germany.

[Advisories Latest disclosures, reports & remediations Browse ](/advisories/)[Posts Deep dives into security research & SSO topics Read ](/post/)[Pentests I am available as a Freelancer for pentest projects Learn more ](/pentest/)[About me Background, focus areas & ways to connect Meet Lauritz](/about/)

## Upcoming Events

Talks, workshops, and meetups I will host or am scheduled to attend.

May 30 - June 7, 2026 Hybrid

Meetup

## Bug Bounty Meetup: "Friendly Edition"

Save the date: Our next meetup is around the corner and will come with a surprise - stay tuned!

Past Events 6

March 18, 2026 Remote

Training

## SSO Security Workshop

A remote workshop covering SSO fundamentals, OAuth and OpenID Connect attack surfaces, and practical hardening guidance.

Completed [Workshop details](https://nextcloud.lauritz-holtmann.de/apps/forms/embed/gz5p3aBNpptrMfjerDGtQL9t)

February 14-22, 2026 Remote

Meetup

## Bug Bounty Meetup vol. 5

The fifth Hacking Meetup of the HackerOne Club Germany was fully-remote again. We hacked on two live targets, connect via a WorkAdventure virtual space, collaborated, and learned a lot.

[Event Wrap-up](https://h1.community/e/mbcd6v/)

September 10th - 20th, 2025 Essen

Meetup

## Bug Bounty Meetup vol. 4

For our fourth meetup we gathered in Essen and scored almost 15k $ in bounties on a fresh target. We had a great time connecting, collaborating, and learning together!

[Event Wrap-up](https://h1.community/e/mbkdm3/)

June 2nd - 15th, 2025 Remote

Meetup

## Bug Bounty Meetup vol. 3

Our third meetup was ground-breaking: We had a record-breaking 95k $ in bounties on Exness. 🤯 This was our first remote meetup, but we still gathered virtually for our Show&Tell session and collaborated a lot throughout the event.

[Event Wrap-up](https://h1.community/e/mgpskc/)

February 15th - 22th, 2025 Bochum

Meetup

## Bug Bounty Meetup vol. 2

New year, new meetup! We had a great time connecting, collaborating, and learning together in Bochum. Partner program was Grab and we scored over 15k $ in bounties.

[Event Wrap-up](https://h1.community/e/mgswsg/)

May 21st - 26th, 2024 Bochum

Meetup

## Bug Bounty Meetup vol. 1

The beginning of something great: Our first meetup was a blast! We had a great time connecting, collaborating, and learning together in Bochum. We hacked on ToolsForHumanity and scored over 10k $ in bounties.

[Event Wrap-up](https://h1.community/e/m48tye/)

## Recent Advisories

Recent research and write-ups on relevant web security topics.

[All Advisories](https://security.lauritz-holtmann.de/advisories/)

Jun 19, 2024 OpenID Connect

## [Sign-in with World ID: XSS and ATO via OIDC Form Post Response Mode](/advisories/tfh-form_post-xss-ato/)

Recently, Tools for Humanity partnered with the German HackerOne Club to run a one-week virtual and in-person Hacking Meetup. In the course of the meetup, a critical vulnerability within the Sign-in with World ID implementation was found, which affected the OpenID Connect form_post Response Mode and could allow malicious actors to take over end-user accounts at third-party applications that utilize the Sign-in with World ID mechanism. The vulnerability was addressed within a few hours after triage.

4 min read

[read more ](/advisories/tfh-form_post-xss-ato/)

Jun 18, 2022 Asana

## [Personal Access Token Disclosure in Asana Desktop Application](/advisories/asana-desktop-credential-disclosure/)

This post gives an insight into a sensitive data exposure vulnerability in Asana for Mac that was rated as P1 and was awarded a bounty. This was the very first report of that kind for me. Still, I think this type of deployment and build chain issue is more common than one may think.

5 min read

[read more ](/advisories/asana-desktop-credential-disclosure/)

Dec 18, 2021 OpenID Connect

## [Flickr Account Takeover](/advisories/flickr-account-takeover/)

This post gives a deep dive into a critical security flaw that was present in Flickr’s login flow. The authentication at identity.flickr.com is implemented using AWS Cognito. By exploiting configuration issues and violations of the OpenID Connect specification, it was possible to takeover any Flickr account without user interaction.

8 min read

[read more ](/advisories/flickr-account-takeover/)
