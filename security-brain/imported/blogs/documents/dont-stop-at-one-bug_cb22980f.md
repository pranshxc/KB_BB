---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-10_dont-stop-at-one-bug-.md
original_filename: 2020-07-10_dont-stop-at-one-bug-.md
title: Don’t stop at one bug $$$$
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
- otp
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
- otp
- mobile-security
language: en
raw_sha256: cb22980fb88fd1be397b7f578d3546d5393b59ed16234da6a9d3f061b74a8700
text_sha256: eea9e2401c5ceac6b02ef1e1893947384843f37b539d59b9c47059cc1477ccfe
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Don’t stop at one bug $$$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-10_dont-stop-at-one-bug-.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal, otp, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `cb22980fb88fd1be397b7f578d3546d5393b59ed16234da6a9d3f061b74a8700`
- Text SHA256: `eea9e2401c5ceac6b02ef1e1893947384843f37b539d59b9c47059cc1477ccfe`


## Content

---
title: "Don’t stop at one bug $$$$"
url: "https://medium.com/bugbountywriteup/dont-stop-at-one-bug-d3c56806b5"
authors: ["Dheeraj Madhukar (@Dheerajmadhukar)"]
bugs: ["Open redirect", "XSS", "LFI"]
publication_date: "2020-07-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4419
scraped_via: "browseros"
---

# Don’t stop at one bug $$$$

Top highlight

Don’t stop at one bug $$$$
Dheeraj Madhukar
Follow
3 min read
·
Jul 10, 2020

332

2

3 critical bugs in a single program [ Local File Steal, Java Script injection, Open Redirect ]

First i want to say thanks to all my readers for your support :)

Hello Folks,

T
oday i am going to talk about my submission on a private program where i submitted three critical bugs, which is based on #Android. Whenever talking about an android bug bounty, i prefer to start with decompiling the APK. But this time i did use “JADx-GUI”.

To understand well i am going to use a sample app.

You just need to open JADx-GUI → File → Open file → company-app.apk & Open “AndroidManifest.xml”

Press enter or click to view image in full size

Now you need to search for the android:exported=”true” activities in “AndroidManifest.xml”, i found one.

Follow this link to learn more on android:exported=”true” : https://developer.android.com/guide/topics/manifest/activity-element

Press enter or click to view image in full size

NOTE: An “exported” activity, service, or content can be accessed by other apps. That makes the exported component vulnerable. ;)

H
ere’s the question — what kind of vulnerabilities we can exploit & how?

Let’s figure out : For example consider the activity name is “app.company.ui.events.web.WebViewActivity”

Open this activity in JADx-GUI → Search for “SetJavascriptEnable”

Follow this link for more details about “SetJavascriptEnable”
https://developer.android.com/reference/android/webkit/WebSettings#setJavaScriptEnabled

Press enter or click to view image in full size

You can see the activity contain the “SetJavaScriptEnabled”

Now focus on two areas:

Snippet#1

** Code : → “intent.putExtra(“EXTRA_URL”, str);”

Get Dheeraj Madhukar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In android “putExtra(String name, str)” is used to add extended data to the intent. It has two parameters, first one specifies the name which of the extra data,and the second parameter is the data itself.

Snippet#2

** Code : → “loadUrl(getIntent().getStringExtra(“EXTRA_URL”));”

In this case, getIntent() Return the intent that started this activity. If you start an Activity with some data.

Let’s make it very simple and short, “intent.putExtra(“EXTRA_URL”, str);” means, you can consider “EXTRA_URL” as a variable & getStringExtra(“EXTRA_URL”)) is used here to get the data or value from “EXTRA_URL” variable.

Proof-of-Concepts
Reproduce OpenRedirect:

am start -W -n app.company/.ui.events.web.WebViewActivity -a ACTION_OPEN_WEB -e EXTRA_URL https://evil.com

Press enter or click to view image in full size

2. Reproduce Javascript Injection:

app.company.ui.events.web.WebViewActivity doesn’t validate data pass to intent due to which this activity is vulnerable to Javascript Injection also.

am start -n app.company/.ui.events.web.WebViewActivity -a ACTION_OPEN_WEB -e EXTRA_URL “javascript://google.com%0A alert(lol);”

Press enter or click to view image in full size

3. Reproduce Local File Steal:

That bug can :
→ Reveal token, auth, config etc in app sandbox
→ Reveal User data in app sandbox
→ Access ‘/sdcard’ data, if permitted

am start -n app.company/.ui.events.web.WebViewActivity -a ACTION_OPEN_WEB -e EXTRA_URL ‘file:///sdcard/personal.txt’

Press enter or click to view image in full size

This is how i reported three critical bugs in a private program. BOOM !!! $$$$

I am very happy to connect with you all :) I hope you get some motivation to do bug bounties and See you again in next writeup.

Twitter profile: @Dheerajmadhukar

Linkedin profile: @dheerajtechnolegends
