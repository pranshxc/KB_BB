---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-25_shareit-multiple-vulnerabilities-enable-unrestricted-access-to-adjacent-devices-.md
original_filename: 2019-02-25_shareit-multiple-vulnerabilities-enable-unrestricted-access-to-adjacent-devices-.md
title: SHAREit Multiple Vulnerabilities Enable Unrestricted Access to Adjacent Devices’
  Files
category: documents
detected_topics:
- mobile-security
- oauth
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- mobile-security
- oauth
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: df2685ba19009f7e0b960abcf97f88c07c63fc00e438f8d558e55ab24713127b
text_sha256: 78b44e03a58d2d47c650e2f7aa6cf4ffda707d158c0b9a9ee6de8dd76a3f7bbd
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# SHAREit Multiple Vulnerabilities Enable Unrestricted Access to Adjacent Devices’ Files

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-25_shareit-multiple-vulnerabilities-enable-unrestricted-access-to-adjacent-devices-.md
- Source Type: markdown
- Detected Topics: mobile-security, oauth, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `df2685ba19009f7e0b960abcf97f88c07c63fc00e438f8d558e55ab24713127b`
- Text SHA256: `78b44e03a58d2d47c650e2f7aa6cf4ffda707d158c0b9a9ee6de8dd76a3f7bbd`


## Content

---
title: "SHAREit Multiple Vulnerabilities Enable Unrestricted Access to Adjacent Devices’ Files"
page_title: "SHAREit Multiple Vulnerabilities Enable Unrestricted Access to Adjacent Devices’ Files – Redforce"
url: "https://blog.redforce.io/shareit-vulnerabilities-enable-unrestricted-access-to-adjacent-devices-files/"
final_url: "https://blog.redforce.io/shareit-vulnerabilities-enable-unrestricted-access-to-adjacent-devices-files/"
authors: ["Abdulrahman Nour (@aboodnour)"]
programs: ["SHAREit"]
bugs: ["Android", "Arbitrary file download", "Authentication bypass"]
publication_date: "2019-02-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5389
---

[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://blog.redforce.io/writer/0xsyndr0me/)

**[Mobile Penetration Testing](https://blog.redforce.io/category/mobile-penetration-testing/)** • February 25, 2019 [ •  17 min read ](https://blog.redforce.io/shareit-vulnerabilities-enable-unrestricted-access-to-adjacent-devices-files/)

## SHAREit Multiple Vulnerabilities Enable Unrestricted Access to Adjacent Devices’ Files

Two recently discovered vulnerabilities affecting SHAREit Android application <= v 4.0.38. The first one allows attacker to bypass SHAREit device authentication mechanism, and the other one enables authenticated attacker to download arbitrary files from user's device. Both vulnerabilities were reported to the vendor and patches have been released. 

![DUMPit - The new SHAREit Vulnerability](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

[ 119 ](javascript:void\(0\))

[ 0 ](https://blog.redforce.io/shareit-vulnerabilities-enable-unrestricted-access-to-adjacent-devices-files/#respond)

[ Tweet ](https://twitter.com/intent/tweet?text=SHAREit Multiple Vulnerabilities Enable Unrestricted Access to Adjacent Devices’ Files&url=https://blog.redforce.io/shareit-vulnerabilities-enable-unrestricted-access-to-adjacent-devices-files/)

[ Share ](https://www.facebook.com/dialog/feed?app_id=&display=popup&caption=Redforce :%20Always Stay Ahead!&description=Two recently discovered vulnerabilities affecting SHAREit Android application <= v 4.0.38. The first one allows attacker to bypass SHAREit device authentication mechanism, and the other one enables authenticated attacker to download arbitrary files from user's device. Both vulnerabilities were reported to the vendor and patches have been released.&link=https://blog.redforce.io/shareit-vulnerabilities-enable-unrestricted-access-to-adjacent-devices-files/&picture=https://blog.redforce.io/storage/2019/02/shareit_post_cover-1040x464.jpg&redirect_uri=https://blog.redforce.io/shareit-vulnerabilities-enable-unrestricted-access-to-adjacent-devices-files/)

## TL;DR

This blog post is about two vulnerabilities affecting SHAREit Android application <= v 4.0.38. The first one allows attacker to bypass SHAREit device authentication mechanism, and the other one enables authenticated attacker to download arbitrary files from user’s device. Both vulnerabilities were reported to the vendor and patches have been released.  
Exploit code is available through our GitHub repository (<https://github.com/redforcesec/DUMPit/>)

## Background

### About SHAREit

As per application’s official website, the application is advertised as:

> SHAREit is the fastest cross-platform app for Android, iOS, PC & Mac. SHAREit allows you to transfer video, music, files and apps from one device to another.  
>  SHAREit has been downloaded by more than 500 million users, and has changed the way we transfer files. Initially launched in the year of 2013, SHAREit app has now become immensely popular across all platforms.

### How it Works

To serve its purpose, SHAREit application hosts multiple services on the device. For the use of this post, we are interested only in two distinct services:

  * **Command Channel (Port 55283):** A regular TCP channel where application exchanges messages with different devices using raw socket connections. This channel is used to communicate with other SHAREit instances running on other devices. This includes device identification, handling file transmission requests, checking connection health…etc.
  * **Download Channel (Port 2999):** SHAREit application’s own HTTP server implementation. This is mainly used by other clients to download shared files.

The regular file transfer session starts with a regular device authentication/identification, then “sender” sends a control message to the “receiver” indicating that it has a file to share and required information to initiate download request. If “receiver” decided that it is not a duplicate file, it goes to download channel and fetches sent file using information from previous control message.

## Vulnerability Details

### 1\. Authenticated Arbitrary File Download

When a download request is initiated, SHAREit client sends a `GET` request to sender’s HTTP server. The requested URL looks like the following `http://shareit_sender_ip:2999/download?metadatatype=photo&metadataid=1337&filetype=thumbnail&msgid=c60088c13d6` .

  * **metadatatype** : is the parameter that defines what resource we are trying to download, is it a photo, a video, a music file, an application or just a regular file (accepts any of the following values `music`, `video`, `photo`, `app`, `game`, `file`, `doc`, `zip`, `ebook`, `contact`.
  * **metdataid** : The identifier for the resource we are trying to download, in case of a photo, video or a sound clip it is an incremented number representing asset id in [Android MediaStore](https://developer.android.com/reference/android/provider/MediaStore), for applications it would be package name and for files it would be the full path of the file.
  * **filetype** : the file type parameter accepts one of the following values `thumbnail`, `raw`, `data`, `external`. As the name suggests, `thumbnail` would fetch a preview of the resource (small image of a video or a photo, application icon, …etc.) and `raw` would fetch the original file.
  * **msgid** : Is a unique identifier for each request to make sure that download request was originally initiated by the sender.

The problem occurs mainly because the application fails to validate `msgid` parameter enabling a malicious client with a valid session to download any resource by directly referencing its identifier. For example to download a file from user’s device, all you need to do is to have a valid SHAREit session with this user at least once to be added to recognized devices then go to
  
  
  http://shareit_sender_ip:2999/download?metadatatype=file&metadataid=%2Fdata%2Fdata%2Fcom.lenovo.anyshare.gps%2Fshared_prefs%2FSettings.xml&filetype=raw.

This will download `/data/data/com.lenovo.anyshare.gps/shared_prefs/Settings.xml` which is the settings file for SHAREit application.

So we can download whatever files we want from victim’s device but getting a valid session would trigger the alarms when they see unusual session and limiting it only to people we exchanged files before would dramatically decrease success rate, so what is next?

### 2\. Authentication Bypass

SHAREit <= v4.0.34 exhibited a very odd behavior that lead to authentication bypass. When a user with no valid session tries to download a file from the device using the previously mentioned URL, the application responds with 403 response code with an error message saying “The request is not from anyshare user!”. Once a valid session is retrieved at least once, application adds the user to recognized devices and accepts any incoming download requests from this user.

The odd behavior occurs when unauthenticated user tries to fetch non-existing page, instead of a regular 404 page, the application responds with 200 status code empty page and **adds user into recognized devices!!** Making this the weirdest and simplest authentication bypass we ever seen :). Yes! a fully functional proof of concept would be as simple as

`curl http://shareit_sender_ip:2999/DontExist`

## Attack Surface

Older versions of SHAREit (< v4.0.X) used to keep the download server running regardless of whether an active file transfer session is running or not. This means that only what attacker needs is to be with your SHAREit android device in the same network to have full unrestricted access to all your files.

Newer versions turn off download server when not in use, this means to exploit the vulnerability, you need to find an active file exchange session around you. Luckily for us, vulnerable SHAREit versions create an easily distinguished open Wi-Fi hotspot which can be used not only to intercept traffic (since it uses HTTP with no SSL/TLS encryption) between the two devices (Both independently [reported by SecureAuth Core Security Team](https://www.secureauth.com/labs/advisories/lenovo-shareit-multiple-vulnerabilities)), but to exploit the discovered vulnerabilities and have unrestricted access to vulnerable device storage. (We managed to download ~ 3000 files having ~ 2GBs in 8 minute transfer session)

## Exploitation

If you know the exact location of the file you would like to retrieve, exploitation can be as simple as a curl command referencing the path of the target file. However, this is not usually the case. To overcome this, we started looking for files with known paths that may contain interesting information in this regard. Analysis showed that two distinct database files related to SHAREit application may be useful in this case:

  * **SHAREit History:** SHAREit history database contains records of all files exchanged using SHAREit application with full path of the file which we can use to fetch it; Not very useful when we are running the exploit against a not so frequent SHAREit user and of course would not contain all nor even most of the records.
  * **SHAREit MediaStore Database:** A smaller instance of Android’s MediaStore database, it exists only in newer versions of SHAREit but if found it will be like a jackpot, since it contains records of most of media files on the device as seen in the following screenshot.

![Screenshot of SHAREit MediaStore Database](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) Screenshot of SHAREit MediaStore database containing interesting information about files in the system including file name, type, size, path and many other information.

So to retrieve all/most of interesting files in the device we start by retrieving such databases and get the files in them. If we could not find those files for whatever reason, we start multi-threaded bruteforcing of Android MediaStore ID (since they are incrementing numeric values) and fetch files of valid IDs.

There are other files that contain juicy information such as user’s Facebook token, Amazon Web Service user’s key, auto-fill data and cookies of websites visited using SHAREit webview and even the plaintext of user’s original hotspot (the application stores it to reset the hotspot settings to original values) and much more.

## Proof of Concept

We created a base exploit toolkit which we used to create two distinct proofs of concept dubbed “DUMPit!”, one with a user friendly GUI that enables you to choose your target and what information you want to fetch, and an auto-pwn module where it automatically detects SHAREit or open WiFi networks, connects to them and scan them for devices running vulnerable SHAREit instances then retrieves as much data as it can in the shortest time. The latter proof of concept managed to retrieve around 3000 unique files having around 2.0 GB in less than 8 minutes. So we’ve gotta give it to SHAREit team, it is FAST 🙂

This proof of concept was originally shared with SHAREit Team and it was recorded in normal playback speed, so feel free to speed it up to get to the interesting parts quickly :))

Exploit can be downloaded from our GitHub repository (<https://github.com/redforcesec/DUMPit/>). Please note that not all exploit modules are deployed but they can be easily implemented by parsing corresponding XML files (Details of each file can be found in juicy files section in case you need it 🙂 )

## Disclosure Timeline

  * **December 2017:** Vulnerability was originally discovered.
  * **7 Jan 2018:** Contacted SHAREit team at public official emails ([[email protected]](/cdn-cgi/l/email-protection), [[email protected]](/cdn-cgi/l/email-protection)) asking for a secure channel to submit finding details with **no response**.
  * **11 Jan 2018:** Pinged SHAREit team [over twitter](https://twitter.com/AboodNour/status/951244396359536640) (@bestSHAREit) with **no luck**.
  * **3 Feb 2018:** Contacted SHAREit team over Facebook and informed them that we will release vulnerability info if we do not get a response within 30 days.
  * **4 Feb 2018:** Got response from SHAREit team over Facebook apologizing for late response and asking for our email address to contact us. We replied to their request on the same day.
  * **5 Feb 2018:** SHAREit Facebook page team asked us to provide vulnerability information over Facebook. We refused and asked for a more secure channel to handle sensitive information. They preferred sending details over email!
  * **6 Feb 2018:** We received an email from Liem Huang from SHAREit, requesting vulnerability details.
  * **7 Feb 2018:** We replied to Liem Huang email with detailed vulnerability advisory and proof of concept.
  * **9 Feb 2018:** We got response from Liem Huang confirming the vulnerabilities and promising a fix in “the near future”
  * **10 Feb 2018:** We asked Liem Huang for planned fix timeline to arrange our public disclosure schedule. **No response!**
  * **18 Feb 2018:** Pinged Liem Huang again for response.
  * **21 Feb 2018:** Liem Huang replied that they are on Chinese holidays and they will reply when they are back. **No feedback!**
  * **19 Mar 2018:** Pinged Liem Huang again for fix status notifying them with our intended public disclosure plans.
  * **22 Mar 2018:** Liem Huang replied that issues have been fixed.

We noticed that this was a silent fix and change logs did not contain any information about a fixed vulnerability and we did not receive a CVE number for the discovered vulnerabilities so we started to reach out to them again

  * **16 Jan 2019:** Asked Liem Huang if vulnerabilities have been assigned CVE numbers or we should request new ones. **No response!**
  * **25 Jan 2019:** Contacted SHAREit team over Facebook again asking for updated information.
  * **26 Jan 2019:** SHAREit Facebook page team replied they would forward details to the team. **No response!**
  * **28 Jan 2019:** Pinged the team over Facebook again. **No response!**
  * **15 Feb 2019:** Informed SHAREit team that we are proceeding with our public disclosure and encouraged them to contact us if they have any inquiries or concerns.
  * **15 Feb 2019:** Got an email from Stella asking for vulnerability details!
  * **15 Feb 2019:** We replied that they are old and fixed vulnerabilities and asked them to provide us with exact patched versions, vulnerabilities CVE numbers and any comments to include in our public disclosure.
  * **17 Feb 2019:** Pinged Stella again and offered assistance if needed to get faster response.
  * **18 Feb 2019:** Received an email from Stella apologizing and refusing to provide us neither of patched versions nor CVE numbers!!!
  * **18 Feb 2019:** We replied with a confirmation that this was not a misunderstanding.
  * **18 Feb 2019:** Received a reply from Stella confirming that yes they refuse to provide us with answers to these requests!!
  * **25 Feb 2019:** This public disclosure.

As seen from previous timelines and responses, communication with SHAREit team was not a good experience at all; Not only they took too long to respond to our messages, they also were not cooperative in any means and we did not feel that our work or efforts were appreciated at all.

![SHAREit Team response refusing to tell us the exact patched version nor assign CVE numbers to discovered vulnerabilities ](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) SHAREit Team response refusing to tell us the exact patched version nor assign CVE numbers to discovered vulnerabilities

## 

## For Our Community <3

Although the vulnerability was originally discovered in December 2017 and officially fixed in March 2018, we decided not to disclose vulnerability details before today given the impact of the vulnerability, its big attack surface and ease of exploitation. We wanted to give as many people as we can the time to update and patch their devices before disclosing such critical vulnerability.

Happy Hacking and use wisely 🙂

[DUMPit](https://blog.redforce.io/tag/dumpit/) [Mobile](https://blog.redforce.io/tag/mobile/) [Penetration Testing](https://blog.redforce.io/tag/penetration-testing/) [SHAREit](https://blog.redforce.io/tag/shareit/) [Web](https://blog.redforce.io/tag/web/)
