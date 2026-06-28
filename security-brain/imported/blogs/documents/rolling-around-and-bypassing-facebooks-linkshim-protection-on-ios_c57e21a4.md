---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-26_rolling-around-and-bypassing-facebooks-linkshim-protection-on-ios.md
original_filename: 2017-07-26_rolling-around-and-bypassing-facebooks-linkshim-protection-on-ios.md
title: Rolling around and Bypassing Facebook’s Linkshim protection on iOS
category: documents
detected_topics:
- xss
- sso
- command-injection
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- xss
- sso
- command-injection
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: c57e21a478dd65380a0f509298078c1e44bf7541471db904b5588c89e3dfd6ad
text_sha256: 5a5e03cf30e22c3eb906144cdde55a97e83095c7553b69e12030b91276e6b67c
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Rolling around and Bypassing Facebook’s Linkshim protection on iOS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-26_rolling-around-and-bypassing-facebooks-linkshim-protection-on-ios.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `c57e21a478dd65380a0f509298078c1e44bf7541471db904b5588c89e3dfd6ad`
- Text SHA256: `5a5e03cf30e22c3eb906144cdde55a97e83095c7553b69e12030b91276e6b67c`


## Content

---
title: "Rolling around and Bypassing Facebook’s Linkshim protection on iOS"
page_title: "Rolling around and Bypassing Facebook’s Linkshim protection on iOS – Seekurity"
url: "https://www.seekurity.com/blog/general/rolling-around-and-bypassing-facebook-linkshim-protection-on-ios"
final_url: "https://seekurity.com/blog/2017/07/26/seif-elsallamy/general/rolling-around-and-bypassing-facebook-linkshim-protection-on-ios"
authors: ["Seif Elsallamy (@seifelsallamy)"]
programs: ["Meta / Facebook"]
bugs: ["Open redirect"]
publication_date: "2017-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6140
---

Supp!, How are you guys! I hope you’re fine, I’m Seif Elsallamy (again) if you don’t remember me read my previous blog here: [Stored XSS in the heart of the Russian email provider giant (Mail.ru)](https://www.seekurity.com/blog/general/stored-xss-in-the-heart-of-the-russian-email-provider-giant-mail-ru/)

Before we go in depth, lets know What is [**Linkshim**](https://www.facebook.com/notes/facebook-security/link-shim-protecting-the-people-who-use-facebook-from-malicious-urls/10150492832835766/)**?**

Linkshim is a feature/tool built by Facebook’s Integrity Team to protect the users from opening malicious links, The way it works, every time a link is clicked on the site, the link-shim will check that URL against an Facebook’s internally compiled list of malicious links, or against any of many external partners lists McAfee, Google and Web of Trust, etc…

If it appears that this URL is malicious, an interstitial page will be displayed before the browser actually requests the suspicious page warns the user of the nature of continuing to this link.

So Bypassing linkshim means sending any malicious URL to any Facebook user right?  
Nope.

Simply because I used chrome iOS URI scheme to bypass linkshim, So the only affected type of users who have chrome installed on their iPhones.

**So what is[ URI scheme](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)?**  
In information technology, a Uniform Resource Identifier (URI) is a string of characters used to identify a resource. Such identification enables interaction with representations of the resource over a network, typically the World Wide Web, using specific protocols. Schemes specifying a concrete syntax and associated protocols define each URI.

So simply the uri-scheme is the part before the colon in a URI  
As example, https://www.seekurity.com/ the protocol here which is “https” is the uri-scheme we are talking about.

Apple’s iOS (iPhone and iPad Operating system) uses uri-schemes to redirect between apps so if you got twitter on your iPhone you might write on Safari’s address bar twitter:// then click go, Safari browser will launch Twitter app!! What a surprise!

chrome uri-scheme on iOS working exactly the same, that googlechrome://example.com will first launch google chrome then point the browser to navigate to url “http://example.com”

So bypassing linkshim is such an easy thing isn’t it?!

Easy enough but Facebook won’t consider redirecting to google chrome browser because simply this is not their issue! But let’s take everything apart:  
https://l.facebook.com/l.php?u=googlechrome://example.com/

Red: is Facebook’s responsibility

Green: is the OS responsibility

Blue: is the link owner’s responsibility

So who to blame here? The innocent user?!

The result:  
The result of clicking on the above link on Facebook app on iOS would lead the innocent user Facebook app to launch Chrome then redirect chrome to open http://example.com/ RIGHT!!

NOPE, We are not there as of yet! We didn’t actually bypass it, Linkshim is a wild cat and won’t allow us to use such protocols *SAD* :/

BUT I managed to find that Linkshim allowing ALL protocols that contains dots *INTERESTING* Isn’t it?!

So all what we need is to put a dot in uri-scheme to fool our wild cat to proceed! eg. google.chrome://example.com/

Are we done?

Not yet, Don’t go away please because that’s not gonna work on iOS and our Chrome app launch won’t succeed.

So I downloaded the IPA of chrome for iOS on my PC, Decompiled it to find other chrome uri schemes, Then guess what I managed to find that “com.google.sso.chrome.stable://” will work like a charm which appears to be the package name of Chrome App! Whooha!

WOW, I can’t believe it, All those dots and all I needed was just one to lead me in!

I know that you got tired and you want the final proof of concept link, Here it is as prize for your patience: **https://l.facebook.com/l.php?u=com.google.sso.chrome.stable://example.com**

That’s a literal bypass Facebook linkshim!

#### All that glitters is not gold…

I reported this bug to Facebook Security Team and it got rejected but they fixed it

However this bug might be still exploitable because Linkshim still allowing dots on uri-scheme part. Well, It got rejected so i decided to move on and try something else.

My advise to you is to test it yourself, You might have a better mindset or another interesting attack vector, See ya 😉

POC Video:

## **A minute if you please!**

Building a website, an application or any kind of business? Or already have one? Worried about your security? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F26%2Fseif-elsallamy%2Fgeneral%2Frolling-around-and-bypassing-facebook-linkshim-protection-on-ios&linkname=Rolling%20around%20and%20Bypassing%20Facebook%E2%80%99s%20Linkshim%20protection%20on%20iOS "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F26%2Fseif-elsallamy%2Fgeneral%2Frolling-around-and-bypassing-facebook-linkshim-protection-on-ios&linkname=Rolling%20around%20and%20Bypassing%20Facebook%E2%80%99s%20Linkshim%20protection%20on%20iOS "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F26%2Fseif-elsallamy%2Fgeneral%2Frolling-around-and-bypassing-facebook-linkshim-protection-on-ios&linkname=Rolling%20around%20and%20Bypassing%20Facebook%E2%80%99s%20Linkshim%20protection%20on%20iOS "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F26%2Fseif-elsallamy%2Fgeneral%2Frolling-around-and-bypassing-facebook-linkshim-protection-on-ios&linkname=Rolling%20around%20and%20Bypassing%20Facebook%E2%80%99s%20Linkshim%20protection%20on%20iOS "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F26%2Fseif-elsallamy%2Fgeneral%2Frolling-around-and-bypassing-facebook-linkshim-protection-on-ios&linkname=Rolling%20around%20and%20Bypassing%20Facebook%E2%80%99s%20Linkshim%20protection%20on%20iOS "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F26%2Fseif-elsallamy%2Fgeneral%2Frolling-around-and-bypassing-facebook-linkshim-protection-on-ios&linkname=Rolling%20around%20and%20Bypassing%20Facebook%E2%80%99s%20Linkshim%20protection%20on%20iOS "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F26%2Fseif-elsallamy%2Fgeneral%2Frolling-around-and-bypassing-facebook-linkshim-protection-on-ios&linkname=Rolling%20around%20and%20Bypassing%20Facebook%E2%80%99s%20Linkshim%20protection%20on%20iOS "Gmail")[](https://www.addtoany.com/share)

and  around  Bypassing  Facebook  iOS  Linkshim  on  protection  Rolling  Vulnerability
