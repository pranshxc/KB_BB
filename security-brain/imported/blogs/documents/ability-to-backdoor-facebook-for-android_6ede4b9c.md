---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-30_ability-to-backdoor-facebook-for-android.md
original_filename: 2020-10-30_ability-to-backdoor-facebook-for-android.md
title: Ability To Backdoor Facebook For Android
category: documents
detected_topics:
- command-injection
- path-traversal
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- path-traversal
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: 6ede4b9c6f5c1c2c465d8dfe10f862cbc86230894b665d54b5d38df62e54aefc
text_sha256: b9cfb42ed819c3eb3260e4727d892f4c74b25f1b814d045a318b0099f7e040bf
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Ability To Backdoor Facebook For Android

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-30_ability-to-backdoor-facebook-for-android.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `6ede4b9c6f5c1c2c465d8dfe10f862cbc86230894b665d54b5d38df62e54aefc`
- Text SHA256: `b9cfb42ed819c3eb3260e4727d892f4c74b25f1b814d045a318b0099f7e040bf`


## Content

---
title: "Ability To Backdoor Facebook For Android"
url: "https://ash-king.co.uk/blog/backdoor-android-facebook"
final_url: "https://ash-king.co.uk/blog/backdoor-android-facebook"
authors: ["Ashley King (@AshleyKingUK)"]
programs: ["Meta / Facebook"]
bugs: ["Insecure deeplink", "Android"]
publication_date: "2020-10-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4169
---

# Ability To Backdoor Facebook For Android 

__Ashley King __30/10/2020 __Meta

![](/assets/img/blog/takeover-splash.png)

[![](/assets/img/blog/takeover-splash.png)](/assets/img/blog/takeover-splash.png)

## Summary

I found a security vulnerability in Facebook for Android which made it possible to backdoor the application. By abusing a development deeplink it was possible to send a packaged version of Facebook to a device including custom code. In this blog post I talk about how I found the deeplink, the making of the payload files and why it's a security vulnerability to include such capabilities in a production build of Facebook.

## Finding the vulnerability

My favorite part about any bug bounty program is learning how the application works. I already started to go into detail on my [last post](https://www.ash-king.co.uk/blog/facebook-bug-bounty-09-18) about how to find deeplinks in the FB4A app but here I will share a small script that streamlines this process.

Facebook Android Deeplink Scraper - a small python script designed to extract Facebook deeplinks from an APK file

Source: <https://github.com/ashleykinguk/FBLinkBuilder/> Sample useage: `.\FBLinkBuilder.py -i fb0409.apk`

Running FBLinkBuilder we can compare the generated deeplinks to the previous version of the application. From that we can easily spot what changes have been made between the two releases. Using this method I found the vulnerable deeplink: `fb://rnquantum_notification_handler/?address=`. This was first introduced early 2020 in a production build of FB4A.

The paramater is expected to be any hostname / ip address. I setup a dummy web server and launched the link with my local ip address as the value.`fb://rnquantum_notification_handler/?address=192.168.0.2:8224`. From here we are prompted with the following screen:

[![](/assets/img/blog/enable-quantum.png)](/assets/img/blog/enable-quantum.png)

We are now expected to press the "Enable Quantum" button and restart the application. After re-launching the application nothing appeared to have changed. Flicking through the different activities I couldn't see anything standing out so I decided to inspect the traffic. Not so long ago, Facebook implemented a [feature](https://www.facebook.com/notes/facebook-bug-bounty/security-testing-for-mobile-apps-made-easy/2528930930454451/) for security researchers which allow us to direct traffic through a proxy. Using this feature I noticed the following outgoing connections being made:

  1. http://192.168.0.2:8224/**message?device=Android+SDK+built+for+x86+-+10+-+API+29 &app=com.facebook.katana&clientid=DevSupportManagerImpl**
  2. http://192.168.0.2:8224/**status**

The first _message_ request passes some basic device information and initiates a websocket connection. After some R&D, the second _status_ request was expecting a response of `packager-status:running`. This is based on some react native source code I found on Github: [/com/facebook/react/devsupport/DevServerHelper.java](https://github.com/facebook/react-native/blob/master/ReactAndroid/src/main/java/com/facebook/react/devsupport/DevServerHelper.java)

Once I updated my dummy server to give the expected response, a new request was then made:

  1. http://192.168.0.2:8224/**RKJSModules/EntryPoints/Fb4aBundle.bundle?platform=android &dev=true&minify=false**

This request is looking for the framework of FB4A stored in a packaged bundle. It is expected to be the plain text version of the bundle rather than the normal hbc* version. I tried to provide the hbc version included in the APKs but as soon as the app processes the file it would completely crash the Facebook application. 

Previously, pre-2019, bundles were stored inside the /assets/ folder of the APK in a minified format. In late 2018 Facebook introduced hbc (*Hermes ByteCode) which reduced the sizes of the APKs enormously in addition to making the core script unreadable to the human eye. Whilst I was able to use a tool called [HBCdump](https://github.com/facebook/hermes/tree/master/tools/hbcdump) to generate a 250mb dump of the bundle it didn't help in creating the payload file.

## Taking over the app

I started looking at older versions of the APKs and compared the contents in the plain text bundles to error messages generated from the device - these errors were visible in logcat so it ended up being a "capture the flag" exercise. This is what I found:

  * `__fbBatchedBridge` this object is required in the bundle and consists of various functions synchronised with the application.
  * `__fbBatchedBridge.callFunctionReturnFlushedQueue` this function is called from the back end code every time an action/event occurs. 

There were some additional pre-requisites as well but I managed to create the barebones of what is needed for Facebook to successfully download and execute the bundle [(View on Github)](https://github.com/ashleykinguk/Fb4abundlejs/blob/main/FB4abundle.js)

Now to deliver the bundle automatically I had to update the web server. Here is the python web server I built as part of the proof of concept: [(View on Github)](https://github.com/ashleykinguk/fb_server/blob/main/fb_server.py)

Putting all the of the pieces together, I was able to execute custom code on the device via the development deeplink. I created a small proof of concept video and sent it off to the Facebook security team alongside my report. Inside the poc I demonstrated capturing what you type into the Facebook app. It would capture the first 5 characters, throw an exception to crash the app whilst writing out what you typed into the logfile.

[![](/assets/img/blog/takeover-splash.png)](/assets/img/blog/takeover-splash.png)

Here's the original video submitted to Facebook: 

## Impact

With every security vulnerability you must define the impact, I worded the impact as:

> This type of vulnerability can be abused by anyone with physical access to the device (schools, businesses, airports, police etc). In creating a persistent connection an attacker is able to deliver custom javascript by overriding the default bundle to the device at any time

It should be noted that this vulnerability was originally dismissed by Facebook, closed as not applicable and stated that: 

> Any user that is knowledgable enough to manage servers and write code would also be able to control how the app operates. That is also true for any browser extension or manual app created. A user is also able to proxy all their HTTP Traffic to manipulate those requests. Only being able to make local modifications with a PoC showing actual impact does not fully qualify for the Bug Bounty.

With that being said, I publicly released the above video. An employee of the Facebook security team promptly contacted me within an hour of the video being released, stating that they will be taking another look, I removed the video immediately. YouTube statistics show around 30 other researchers had knowledge of this vulnerability before it was initially patched 2 days later.

## Timeline - Key dates

  * 20 Jun 2020 - Reported to Facebook
  * 22 Jun 2020 - More Information Requested
  * 23 Jun 2020 - More Information Provided
  * 23 Jun 2020 **19:20** \- Closed as N/A
  * 23 Jun 2020 **19:39** \- Publicly released
  * 23 Jun 2020 **20:31** \- Re-opened & asked to remove video
  * 24 Jun 2020 - Triaged
  * 26 Jun 2020 - Issue mitigated by disabling Quantum
  * 20 Aug 2020 - Officially Fixed
  * 17 Sep 2020 - Payout Received

## Response From Facebook Security Team

> After reviewing this issue, we have decided to award you a bounty of $X. Below is an explanation of the bounty amount. Facebook fulfills it's bounty awards through Bugcrowd and HackerOne.  
>  
>  Your report described a scenario in which an attacker could have tricked a user to be redirected to a developer-only setting, configuring the Facebook Android app to connect to an attacker-controlled React Native Development Server and delivering React Native code that would potentially be executed by the app.  
>  
>  Thank you again for your report. We look forward to receiving more reports from you in the future!
