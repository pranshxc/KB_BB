---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-08_bypassing-google-maps-api-key-restrictions.md
original_filename: 2020-08-08_bypassing-google-maps-api-key-restrictions.md
title: Bypassing Google Maps API Key Restrictions
category: documents
detected_topics:
- api-security
- mobile-security
- command-injection
- business-logic
- supply-chain
tags:
- imported
- documents
- api-security
- mobile-security
- command-injection
- business-logic
- supply-chain
language: en
raw_sha256: a5277a59127d045c6e46a43b732b6735f0dbf4a21cacd8d59d1bbbc12f00c86f
text_sha256: 7392487a25b29d047f7d847882cce01dcda4bc2b3bfb53d8229b301897454f3e
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Google Maps API Key Restrictions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-08_bypassing-google-maps-api-key-restrictions.md
- Source Type: markdown
- Detected Topics: api-security, mobile-security, command-injection, business-logic, supply-chain
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `a5277a59127d045c6e46a43b732b6735f0dbf4a21cacd8d59d1bbbc12f00c86f`
- Text SHA256: `7392487a25b29d047f7d847882cce01dcda4bc2b3bfb53d8229b301897454f3e`


## Content

---
title: "Bypassing Google Maps API Key Restrictions"
url: "https://blog.dixitaditya.com/bypassing-google-maps-api-key-restrictions/"
final_url: "https://blog.dixitaditya.com/bypassing-google-maps-api-key-restrictions?x-host=blog.dixitaditya.com"
authors: ["Aditya Dixit (@zombie007o)"]
programs: ["Google"]
bugs: ["Logic flaw"]
publication_date: "2020-08-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4340
---

# Bypassing Google Maps API Key Restrictions

UpdatedFebruary 3, 2022

•4 min read•[ __View as Markdown](/bypassing-google-maps-api-key-restrictions.md)

![Bypassing Google Maps API Key Restrictions](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1643881897537%2FRVdYlMv5b.jpeg&w=3840&q=75)

[ A](https://hashnode.com/@adityadixit)

[Aditya Dixit](https://hashnode.com/@adityadixit)

[ __](https://twitter.com/zombie007o)[__](https://www.linkedin.com/in/ad17ya/)

I'm leading the Research at Credshields, and Pentest teams at Cobalt Labs and HackerOne. I occasionally blog about my findings and adventures in pentesting.

On this page

The Proof of ConceptFinding the API KeyThe Bypass

We all know that Google Maps is used at places when there's a requirement to integrate Maps in websites/apps, or when companies want to search the locations entered by users in the Address fields. 

Most of the devs even expose their API keys either through their source code or in one of the requests being sent from their applications. This is not even considered a serious issue because all an attacker can do is send requests to Maps API endpoints using their keys.  
A lot of reports can also be seen on Bug bounty platforms that either mark the accidental exposure of these API keys as Informative or as an Accepted Risk.

The thing which they don't consider is the impact it might have on their budget because these keys have a pay-as-you-go billing cycle. The below-shown pricing table for Google Maps API explains it pretty well.  
These 1000 requests can be sent easily using Burp Suite's Intruder in a few seconds, now imagine the effect this might have on the organization if it's left running for a few hours.

![pricing](https://imgur.com/x8pBgsH.png)

But Google also has few restriction options to prevent unauthorized usage of these keys, they are -

  * HTTP referrers: restricts usage to one or more URLs and is intended for keys that are used in websites and web apps. This type of restriction allows you to set restrictions to a specific domain, page or set of pages in your website.
  * IP addresses: restricts usage to one or more IP addresses, and are intended for securing keys used in server-side requests, such as calls from web servers and cron jobs.
  * Android and iOS app restriction: restricts usage to calls from an Android app with a specified package name.

* * *

## The Proof of Concept

This is a Unique case of how I bypassed some of the restrictions placed by an Android app to their API Keys.

There are two parts to this PoC, the first one explains finding the API key and the second explains the restriction bypass.

### Finding the API Key

First and foremost recon in an Android application starts with decompiling the APK. (Also MobSF).

I'll be using `apktool` to decompile it with this command

`apktool d filename.apk`

A folder with the name of the apk will be generated.

Now I had to go inside the folder and look for any leaked keys. Usually, there are some constants inside strings.xml file which is located in `/res/values` directory. I'll use grep to search for any keys.

`grep "key" strings.xml`

![strings](https://imgur.com/vYqZGaI.png)

As you can see, well, there are lots of API keys in here.

![apikeys](https://imgur.com/wdvfQDx.png)

[https://maps.googleapis.com/maps/api/place/autocomplete/json?key=\&language=en-US&input=mong&components=country%3AIL](https://maps.googleapis.com/maps/api/place/autocomplete/json?key=<key_here>&language=en-US&input=mong&components=country%3AIL)

When tried to use it normally ( **super helpful** \- <https://github.com/streaak/keyhacks>) it gave me this error which hinted that it might be a Referer restriction but when tried with the referer of the app `api.redacted.com` it didn't work as well so there was some other kind of restriction here.  
Now comes the bypassing part.

### The Bypass

LUCKILY, while browsing the android app, I came across this one ongoing request that had two unique headers which caught my attention. They were -  
`X-Android-Cert` and `X-Android-Package`

`X-Android-Cert` contained some kind of SHA1 hash and from the name, it looked like it was of the app's certificate. To test it out -

I extracted the APK using an archive manager and went inside the path `/META-INF` which contains the certificate file. To view information related to the certificate, I used `keytool`.

`keytool -printcert -file CERT.RSA`

![keytool](https://imgur.com/Ag1wu9b.png)

This confirmed that the value in the header `X-Android-Cert` was indeed it's SHA1 hash.

The second header looked already familiar and is pretty descriptive with the name `X-Android-Package`. It had the package name of the APK - `com.redacted.app`

Now using these two headers in my API request to Google Map, I was finally able to bypass the restrictions placed by the app on it's API Keys.

![bypass](https://imgur.com/1T93qjU.png)

Also, It was marked as an accepted risk.

[#tutorial](/tag/tutorial)[#google](/tag/google)[#google-maps](/tag/google-maps)[#hacking](/tag/hacking)[#security](/tag/security)

 __4.7K views
