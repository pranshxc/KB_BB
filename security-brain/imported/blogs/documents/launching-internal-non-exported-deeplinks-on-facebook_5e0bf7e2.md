---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-28_launching-internal-non-exported-deeplinks-on-facebook.md
original_filename: 2021-01-28_launching-internal-non-exported-deeplinks-on-facebook.md
title: Launching Internal & Non-Exported Deeplinks On Facebook
category: documents
detected_topics:
- access-control
- xss
- command-injection
- path-traversal
- automation-abuse
- csrf
tags:
- imported
- documents
- access-control
- xss
- command-injection
- path-traversal
- automation-abuse
- csrf
language: en
raw_sha256: 5e0bf7e2f9a41cae267108c7db0b59b6ac5190b0ee29a31b4d4251022b80410d
text_sha256: e2720122b4a0c9c1f1735aba33bcb26cfbca8c698cdbb2543d321cc28574d87a
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Launching Internal & Non-Exported Deeplinks On Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-28_launching-internal-non-exported-deeplinks-on-facebook.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, path-traversal, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `5e0bf7e2f9a41cae267108c7db0b59b6ac5190b0ee29a31b4d4251022b80410d`
- Text SHA256: `e2720122b4a0c9c1f1735aba33bcb26cfbca8c698cdbb2543d321cc28574d87a`


## Content

---
title: "Launching Internal & Non-Exported Deeplinks On Facebook"
page_title: "Launching internal & non-exported deeplinks on Facebook"
url: "https://ash-king.co.uk/blog/Launching-internal-non-exported-deeplinks-on-Facebook"
final_url: "https://ash-king.co.uk/blog/Launching-internal-non-exported-deeplinks-on-Facebook"
authors: ["Ashley King (@AshleyKingUK)", "Rahul Kankrale (@RahulKankrale)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
bounty: "4,000"
publication_date: "2021-01-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3955
---

# Facebook for Android - CSRF Attack

__Ashley King __28/01/2021 __Meta

![](/assets/img/blog/facebook_attack_flow.png?ver=1)

The report was submitted as a collaboration between myself and [Rahul Kankrale](https://twitter.com/RahulKankrale). The split was 70% Ash & 30% Rahul. 

[![](/assets/img/blog/facebook_attack_flow.png)](/assets/img/blog/facebook_attack_flow.png)

## Summary

It was possible to override the main UI of Facebook for Android (FB4a) by launching the activity `FbMainTabActivity` including some additional extras which result in a new music bar being attached across the bottom of the screen. Clicking anywhere in this music bar will launch an attacker controlled deeplink. This deeplink can be both non-exported or an internal Facebook deeplink, bypassing security measures already put in place. The vulnerability affected [Facebook for Android](https://play.google.com/store/apps/details?id=com.facebook.katana) and [Facebook Workplace](https://play.google.com/store/apps/details?id=com.facebook.work)

During our research we have identified an additional 2 internal deeplinks which are vulnerable to XSS. So by chaining the original vulnerability to these restricted vulnerable deeplinks it becomes very similar to the report: [Breaking The Facebook For Android application](https://www.ash-king.co.uk/blog/facebook-bug-bounty-09-18)

## Impact

  * A malicious actor is able to launch internal & non-exported deeplinks on a device on behalf of a user, bypassing custom restrictions around deeplinks.
  * A chained vulnerability allows an actor to run arbitrary javascript on a webview inside the FB4a app on behalf of a user.
  * Overriding webviews with a custom urls can lead to phishing due to the activity not exposing the URL.

## Setup

  * UserA authenticated with FB4a
  * UserA has a Fb_PoC.apk installed on their device

## Steps

  1. UserA launches the installed application FB_PoC
  2. UserA is redirected to the Facebook Application with a new "Music" bar attached to the bottom of the view.
  3. UserA clicks anywhere in this bar in which it opens an attacker controlled deeplink.

The behaviour flow can be seen here

## Understanding the vulnerability

The issue lied within the class `com.facebook.katana.activity.FbMainTabActivity` under the `handleNewIntent` method.

[![](/assets/img/blog/handle_new_intent.png)](/assets/img/blog/handle_new_intent.png)

As seen in the image above this routine required the following ruleset

  * Must include an extra boolean of `should_show_rum_player` with a value of `true`
  * Must include an extra string of `rum_destination_uri`
  * Must include a flag of `FLAG_ACTIVITY_NEW_TASK`

As the `rum_destination_uri` doesn't go through any sort of validation we are able to provide any valid deeplink

An attackers payload may look similar to the below 

## Applying the fix

The resolution for this was to completely remove the code block relating this music bar.

## Timeline

  * 14 Dec 2020 - Reported to Facebook
  * 21 Dec 2020 - More Information Requested. Unable to reproduce
  * 5 Jan 2021 - Triaged
  * 18 Jan 2021 - Fixed
  * 28 Jan 2021 - $4000 Total Bounty Paid

## Response From Facebook Security Team

> After reviewing this issue, we have decided to award you a bounty of $2800. Below is an explanation of the bounty amount. Facebook fulfills its bounty awards through Bugcrowd and HackerOne.  
>  
>  This could have allowed a third party to launch internal deeplinks which could result in various CSRF attack possibilities such as de-anonymization.  
>  
>  Thank you again for your report. We look forward to receiving more reports from you in the future!
