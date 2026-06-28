---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-12_contentful-access-token-disclosure-in-android-apk.md
original_filename: 2022-09-12_contentful-access-token-disclosure-in-android-apk.md
title: Contentful Access Token Disclosure in Android APK
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- otp
- information-disclosure
- mobile-security
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- otp
- information-disclosure
- mobile-security
language: en
raw_sha256: 1f19d25ea467b48a219b6b21b83a6a00ffe836bdd0ee3162c16c425f735f5fb7
text_sha256: e0e2df18e742626e2e72ca60d5bdb65d28696d55a13b057cd39ac061fdc0777f
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Contentful Access Token Disclosure in Android APK

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-12_contentful-access-token-disclosure-in-android-apk.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, otp, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `1f19d25ea467b48a219b6b21b83a6a00ffe836bdd0ee3162c16c425f735f5fb7`
- Text SHA256: `e0e2df18e742626e2e72ca60d5bdb65d28696d55a13b057cd39ac061fdc0777f`


## Content

---
title: "Contentful Access Token Disclosure in Android APK"
url: "https://medium.com/@cyberali/contentful-access-token-disclosure-in-android-apk-ace5f7bdf98"
authors: ["Cyberali"]
bugs: ["Information disclosure", "Android"]
publication_date: "2022-09-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2179
scraped_via: "browseros"
---

# Contentful Access Token Disclosure in Android APK

Contentful Access Token Disclosure in Android APK
Cyberali
Follow
2 min read
·
Aug 12, 2022

73

3

Hello, My name is Ali, a Penetration Tester and a Certified Ethical Hacker. It’s my first write-up of 2022 on Android APK Pen testing. I was sitting in my office and saw a Hacker One invite alert on my G-Mail inbox. Just saw the scope and was BANG!!! so BIG.

I find it more interesting to test android applications. So, I simply downloaded the APK. Since the dynamic testing of android takes some configuration time I started from static testing, the code review. While doing so I found a file in path apkname/BuildConfig. Just opened and started reviewing, as there were some interesting key-value pairs so I decided to keep observing every value keenly. I saw two keys CONTENTFUL_ACCESS_TOKEN and CONTENTFUL_SPACE.

Press enter or click to view image in full size

Now, I searched on google for any already disclosed reports. But unfortunately couldn’t find any. So I decided to read the documentation from contentful.com.

Contentful is basically used to assemble the content and delivery faster. So to retrieve the content, we need to authenticate ourselves to show that we are legitimate users. Now there were two ways to send authentication request via CURL command:

Get Cyberali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As a query parameter:
curl -v https://cdn.contentful.com/spaces/cfexampleapi/entries?access_token=b4c0n73n7fu1

As a header:
curl -v https://cdn.contentful.com/spaces/cfexampleapi/entries -H ‘Authorization: Bearer b4c0n73n7fu1’

I used the “Query Parameter” option copy/ pasted the command on my Linux terminal, Changed the required parameters, pressed ENTER and BOOM! received my targets information stored on contentful.

Press enter or click to view image in full size

Conclusion:

Always read the documentation of access tokens, API keys or what ever sensitive you find when doing pen testing. It will provide you a new way of exploiting. May be the exploit is written on documentation.

Thank You!!!
