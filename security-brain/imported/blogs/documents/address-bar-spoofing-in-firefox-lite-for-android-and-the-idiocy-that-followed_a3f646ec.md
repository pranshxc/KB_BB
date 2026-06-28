---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-01_address-bar-spoofing-in-firefox-lite-for-android-and-the-idiocy-that-followed.md
original_filename: 2019-08-01_address-bar-spoofing-in-firefox-lite-for-android-and-the-idiocy-that-followed.md
title: Address bar spoofing in Firefox Lite for Android ...and the idiocy that followed
category: documents
detected_topics:
- command-injection
- mfa
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- mfa
- api-security
- mobile-security
language: en
raw_sha256: a3f646ec4020085a65a0259dc6539f4e8d58c6dc25bf3709684580dbd1e7855e
text_sha256: 6c20c2612dbef7c7ed5365d8a19807903518c4d3a537775281963e5bf837c38d
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Address bar spoofing in Firefox Lite for Android ...and the idiocy that followed

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-01_address-bar-spoofing-in-firefox-lite-for-android-and-the-idiocy-that-followed.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `a3f646ec4020085a65a0259dc6539f4e8d58c6dc25bf3709684580dbd1e7855e`
- Text SHA256: `6c20c2612dbef7c7ed5365d8a19807903518c4d3a537775281963e5bf837c38d`


## Content

---
title: "Address bar spoofing in Firefox Lite for Android ...and the idiocy that followed"
page_title: "Address bar spoofing in Firefox Lite for Android ...and the idiocy that followed - Tinkering the kernel"
url: "https://blog.0x48piraj.com/address-bar-spoofing-in-firefox-lite-for-android-and-the-idiocy-that-followed/"
final_url: "https://blog.0x48piraj.com/address-bar-spoofing-in-firefox-lite-for-android-and-the-idiocy-that-followed/"
authors: ["Piyush Raj (@0x48piraj)"]
programs: ["Mozilla"]
bugs: ["Address Bar Spoofing", "URL spoofing"]
publication_date: "2019-08-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5058
---

August 1, 2020

# Address bar spoofing in Firefox Lite for Android ...and the idiocy that followed

[Piyush Raj](https://blog.0x48piraj.com/authors/0x48piraj/)

Date reported — 2019-08-29

#### Summary

Firefox Lite 1.9.2 for Android and earlier suffer from exhaustive Address Bar Spoofing, allowing attackers to potentially trick a victim into visiting a malicious domain for legitimate domain name. Firefox Lite is almost installed on more than 10M devices.

#### Impact

URL Address Bar spoofing is the worst kind of phishing attack possible because it's the only way to identify the site which the user is visiting for a non-technical user. URL address bar is the only way to trust a website and if this indicator is hijacked, the whole security of any normal user will be compromised.

#### Explanation

The address bar can be spoofed by a crafted javascript page with `setInterval()` function which executes `pwn()` function which ultimately reloads target URL in every 10ms.

#### Proof of concept (POC)

  1. Opening Firefox Lite; Latest version i.e.1.9.1 (13361)
  2. Spawning a HTTP web-server with the attached payload i.e. `spoof.html`
  3. Loading the page e.g <http://10.10.10.10/spoof.html>
  4. URL gets spoofed and shows contents of `spoof.html` while URL points at <https://www.mozilla.org/en-US/>

Video demo — <https://youtu.be/wzpteHxAQSw>

#### Expected behavior

The browser should successfully redirect to the target website.

#### Reply from Mozilla

Quickly acknowledging, validating, and resolving submitted issues while recognizing the researcher's effort is vital for successful vulnerability coordination, but the report didn't got any attention after initial triage and half-hearted discussion.

#### ...11 months later

I got fed up after waiting for months, eleven months to be exact. I emailed [security@mozilla.org](mailto:security@mozilla.org) asking them to look at the stale bug report.

Frederik helped to re-initiate the staled report. This is what happened afterwards —

Thanks for the notification, --REDACTED--! we'll prioritize this issue in the sprint planning later today. --REDACTED--

Hi folks,  
Per the given information and testing result, this issue is reproducible only on old webview versions (70).  
Users has to update Chrome and Firefox Lite to latest version so that they get better security.  
And then the coming tricky problem is we don't have good position to prompt users to update their Chrome.  
As we have very small user base hanging on that (or older) version so the impact is fairly limited.  
That said, we don't see immediate action to take on this issue.

Lingering the report for 11 months while the Google's webview versions regularly updated; establishing low impact with a ridiculous reason. It's like saying — _"Oh yeah, there's RCE possible but we don't use the software which has the bug you know, so the impact is fairly limited"_.

I don't think the reply needs any more explanation. I leave it up to you to judge the response. I'm not gonna do anything now. Let's see what happens.

Peace out.

  * [Bug Bounty](https://blog.0x48piraj.com/tags/bug-bounty/)
  * [Vulnerability](https://blog.0x48piraj.com/tags/vulnerability/)

[ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fblog.0x48piraj.com%2Faddress-bar-spoofing-in-firefox-lite-for-android-and-the-idiocy-that-followed%2F)[ Twitter ](https://twitter.com/share?url=https%3A%2F%2Fblog.0x48piraj.com%2Faddress-bar-spoofing-in-firefox-lite-for-android-and-the-idiocy-that-followed%2F&via=0x48piraj&text=Address%20bar%20spoofing%20in%20Firefox%20Lite%20for%20Android%20...and%20the%20idiocy%20that%20followed)[ Pinterest ](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fblog.0x48piraj.com%2Faddress-bar-spoofing-in-firefox-lite-for-android-and-the-idiocy-that-followed%2F&media=https%3A%2F%2Fblog.0x48piraj.com%2Fmedia%2Fposts%2F6%2Fmozilla-bg.png&description=Address%20bar%20spoofing%20in%20Firefox%20Lite%20for%20Android%20...and%20the%20idiocy%20that%20followed)[ LinkedIn](http://www.linkedin.com/shareArticle?url=https%3A%2F%2Fblog.0x48piraj.com%2Faddress-bar-spoofing-in-firefox-lite-for-android-and-the-idiocy-that-followed%2F&title=Address%20bar%20spoofing%20in%20Firefox%20Lite%20for%20Android%20...and%20the%20idiocy%20that%20followed)

### [Piyush Raj](https://blog.0x48piraj.com/authors/0x48piraj/)

Attracted to hardware hacking, likes to fiddle with software, open-source contributor/evangelist and an independent security researcher by night.
